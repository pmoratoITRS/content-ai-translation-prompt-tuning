#!/usr/bin/env python3
"""
Golden Data Preprocessor for Soft Prompt Tuning

This script preprocesses the golden dataset by masking markdown shortcodes,
URLs, and other non-translatable elements before soft prompt tuning.
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse
from dataclasses import dataclass
import logging


@dataclass
class MaskingConfig:
    """Configuration for masking patterns"""
    # Patterns that should be masked (not translated)
    mask_patterns = [
        # Hugo shortcodes
        (r'{{<\s*/?\s*tableformatter\s*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*callout\s*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*AppElement[^>]*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*Code/Symbol[^>]*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*savebutton\s*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*buttonSecondary\s*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*tab\s*>}}', 'SHORTCODE'),
        (r'{{<\s*/?\s*menuitem\s*>}}', 'SHORTCODE'),
        
        # Ref links with lang parameter  
        (r'{{<\s*ref\s+path="[^"]*"\s+lang="[^"]*"\s*>}}', 'SHORTCODE'),
        
        # System variables and functions
        (r'{{@[^}]+}}', 'SYSTEM_VAR'),
        (r'{{[^}]*\([^}]*\)}}', 'FUNCTION'),
        
        # Code blocks (preserve completely)
        (r'```[^`]*```', 'CODE_BLOCK'),
        
        # Inline code
        (r'`[^`]+`', 'INLINE_CODE'),
        
        # Images - mask only the URL part, preserve alt text for translation
        # This pattern will be handled specially in mask_content method
        
        # Links - mask only the URL part, preserve link text for translation  
        # This pattern will be handled specially in mask_content method
        
        # HTML tags
        (r'<[^>]*>', 'HTML_TAG'),
        
        # IDs and anchors
        (r'{id="[^"]*"}', 'ANCHOR'),
        
        # File paths and extensions
        (r'\b\w+\.(md|json|html|css|js|png|jpg|jpeg|gif|svg)\b', 'FILE_PATH'),
        
        # URLs (standalone)
        (r'https?://[^\s\)]+', 'URL'),
    ]


class GoldenDataMasker:
    """Masks non-translatable elements in golden data"""
    
    def __init__(self, config: MaskingConfig):
        self.config = config
        self.setup_logging()
        
        # Compile patterns for efficiency
        self.compiled_patterns = [
            (re.compile(pattern, re.DOTALL | re.IGNORECASE), mask_type)
            for pattern, mask_type in config.mask_patterns
        ]
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def extract_frontmatter(self, content: str) -> Tuple[Optional[Dict], str]:
        """Extract and parse frontmatter from markdown content"""
        if not content.strip().startswith('{'):
            return None, content
        
        # Find the end of the frontmatter JSON
        brace_count = 0
        end_pos = 0
        
        for i, char in enumerate(content):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_pos = i + 1
                    break
        
        if end_pos == 0:
            return None, content
        
        try:
            frontmatter_str = content[:end_pos]
            frontmatter = json.loads(frontmatter_str)
            main_content = content[end_pos:].lstrip('\n')
            return frontmatter, main_content
        except json.JSONDecodeError:
            self.logger.warning("Failed to parse frontmatter as JSON")
            return None, content
    
    def mask_frontmatter(self, frontmatter: Dict) -> Tuple[Dict, Dict[str, str]]:
        """Mask URLs and non-translatable fields in frontmatter"""
        if not frontmatter:
            return frontmatter, {}
        
        masked_frontmatter = frontmatter.copy()
        placeholders = {}
        
        # Handle URL field specially - partial translation
        if 'url' in masked_frontmatter:
            url = masked_frontmatter['url']
            masked_url = self._process_url_field(url, placeholders)
            masked_frontmatter['url'] = masked_url
        
        # Fields that should NOT be translated at all
        non_translatable_fields = ['translationKey', 'type']
        
        for field in non_translatable_fields:
            if field in masked_frontmatter:
                original_value = masked_frontmatter[field]
                placeholder = f"[FRONTMATTER_{field.upper()}]"
                placeholders[placeholder] = original_value
                masked_frontmatter[field] = placeholder
        
        return masked_frontmatter, placeholders
    
    def _process_url_field(self, url: str, placeholders: Dict[str, str]) -> str:
        """Process URL field to mask base paths but preserve translatable slugs"""
        if not isinstance(url, str):
            return url
        
        # Pattern for topics: /support/kb/[translatable-path]
        topics_match = re.match(r'^(/support/kb/)(.+)$', url)
        if topics_match:
            base_path = topics_match.group(1)
            translatable_path = topics_match.group(2)
            
            # Create placeholder for base path
            placeholder = f"[URL_BASE_TOPICS]"
            if placeholder not in placeholders:
                placeholders[placeholder] = base_path
            
            # Return with masked base and translatable path
            return f"{placeholder}{translatable_path}"
        
        # Pattern for changelogs: /changelog/[translatable-path]  
        changelog_match = re.match(r'^(/changelog/)(.+)$', url)
        if changelog_match:
            base_path = changelog_match.group(1)
            translatable_path = changelog_match.group(2)
            
            # Create placeholder for base path
            placeholder = f"[URL_BASE_CHANGELOG]"
            if placeholder not in placeholders:
                placeholders[placeholder] = base_path
            
            # Return with masked base and translatable path
            return f"{placeholder}{translatable_path}"
        
        # For other URLs, mask completely (no translation)
        placeholder = f"[FRONTMATTER_URL]"
        placeholders[placeholder] = url
        return placeholder
    
    def mask_content(self, content: str) -> Tuple[str, Dict[str, str]]:
        """Apply masking to content and return placeholders"""
        masked_content = content
        placeholders = {}
        counter_by_type = {}
        
        # Remove TRANSLATE_THIS: markers if present
        masked_content = re.sub(r'\[TRANSLATE_THIS:\s*', '', masked_content)
        masked_content = re.sub(r'\](?=\([^)]*\))', ']', masked_content)  # Fix broken links
        
        # Handle images specially - mask only URLs, preserve alt text
        masked_content = self._mask_images(masked_content, placeholders, counter_by_type)
        
        # Handle links specially - mask only URLs, preserve link text  
        masked_content = self._mask_links(masked_content, placeholders, counter_by_type)
        
        # Apply other masking patterns
        for pattern, mask_type in self.compiled_patterns:
            matches = pattern.findall(masked_content)
            
            for match in matches:
                if not match:  # Skip empty matches
                    continue
                
                # For non-tuple matches, proceed normally
                if mask_type not in counter_by_type:
                    counter_by_type[mask_type] = 1
                else:
                    counter_by_type[mask_type] += 1
                
                placeholder = f"[{mask_type}_{counter_by_type[mask_type]}]"
                placeholders[placeholder] = match
                masked_content = masked_content.replace(match, placeholder, 1)
        
        return masked_content, placeholders
    
    def _mask_images(self, content: str, placeholders: Dict[str, str], counter_by_type: Dict[str, int]) -> str:
        """Mask only image URLs, preserve alt text for translation"""
        image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]*)\)')
        
        def replace_image(match):
            alt_text = match.group(1)
            url = match.group(2)
            
            # Create placeholder for URL
            if 'IMAGE_URL' not in counter_by_type:
                counter_by_type['IMAGE_URL'] = 1
            else:
                counter_by_type['IMAGE_URL'] += 1
            
            placeholder = f"[IMAGE_URL_{counter_by_type['IMAGE_URL']}]"
            placeholders[placeholder] = url
            
            # Return with preserved alt text but masked URL
            return f"![{alt_text}]({placeholder})"
        
        return image_pattern.sub(replace_image, content)
    
    def _mask_links(self, content: str, placeholders: Dict[str, str], counter_by_type: Dict[str, int]) -> str:
        """Mask only link URLs, preserve link text for translation"""
        link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
        
        def replace_link(match):
            link_text = match.group(1)
            url = match.group(2)
            
            # Don't translate if link text is already a masked token
            if any(link_text.startswith(prefix) for prefix in ['SHORTCODE_', 'APP_', 'REF_', 'SYSTEM_VAR_', 'FUNCTION_']):
                # For masked tokens, mask the URL but don't add translation markers
                if 'LINK_URL' not in counter_by_type:
                    counter_by_type['LINK_URL'] = 1
                else:
                    counter_by_type['LINK_URL'] += 1
                
                placeholder = f"[LINK_URL_{counter_by_type['LINK_URL']}]"
                placeholders[placeholder] = url
                return f"[{link_text}]({placeholder})"
            else:
                # For normal text, preserve for translation but mask URL
                if 'LINK_URL' not in counter_by_type:
                    counter_by_type['LINK_URL'] = 1
                else:
                    counter_by_type['LINK_URL'] += 1
                
                placeholder = f"[LINK_URL_{counter_by_type['LINK_URL']}]"
                placeholders[placeholder] = url
                return f"[{link_text}]({placeholder})"
        
        return link_pattern.sub(replace_link, content)
    
    def mask_file_content(self, content: str) -> Tuple[str, Dict[str, str]]:
        """Mask a complete file's content"""
        # Extract frontmatter
        frontmatter, main_content = self.extract_frontmatter(content)
        
        all_placeholders = {}
        
        if frontmatter:
            # Mask frontmatter
            masked_frontmatter, fm_placeholders = self.mask_frontmatter(frontmatter)
            all_placeholders.update(fm_placeholders)
            
            # Mask main content
            masked_main_content, content_placeholders = self.mask_content(main_content)
            all_placeholders.update(content_placeholders)
            
            # Reconstruct file
            frontmatter_json = json.dumps(masked_frontmatter, indent=2, ensure_ascii=False)
            masked_file_content = f"{frontmatter_json}\n\n{masked_main_content}"
        else:
            # No frontmatter, just mask content
            masked_file_content, all_placeholders = self.mask_content(content)
        
        return masked_file_content, all_placeholders


class GoldenDataPreprocessor:
    """Main preprocessor for golden data"""
    
    def __init__(self, content_dir: Path, output_dir: Path, languages: List[str]):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.languages = languages
        self.masker = GoldenDataMasker(MaskingConfig())
        self.setup_logging()
        
        # Statistics
        self.stats = {
            'files_processed': 0,
            'files_skipped': 0,
            'errors': 0,
            'placeholders_created': 0
        }
    
    def setup_logging(self):
        """Setup logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def process_directory(self, subdir: str = "topics"):
        """Process all files in a subdirectory (topics or changelogs)"""
        self.logger.info(f"Processing {subdir} directory...")
        
        # Process each language
        for lang in self.languages:
            lang_dir = self.content_dir / subdir / lang
            if not lang_dir.exists():
                self.logger.warning(f"Directory not found: {lang_dir}")
                continue
            
            # Create output directory
            output_lang_dir = self.output_dir / subdir / lang
            output_lang_dir.mkdir(parents=True, exist_ok=True)
            
            # Process each markdown file
            for md_file in lang_dir.glob("*.md"):
                try:
                    self.process_file(md_file, output_lang_dir)
                except Exception as e:
                    self.logger.error(f"Error processing {md_file}: {e}")
                    self.stats['errors'] += 1
    
    def process_file(self, input_file: Path, output_dir: Path):
        """Process a single markdown file"""
        self.logger.debug(f"Processing: {input_file.name}")
        
        # Read input file
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.logger.error(f"Failed to read {input_file}: {e}")
            self.stats['errors'] += 1
            return
        
        # Skip if file is empty
        if not content.strip():
            self.logger.warning(f"Skipping empty file: {input_file.name}")
            self.stats['files_skipped'] += 1
            return
        
        # Apply masking
        masked_content, placeholders = self.masker.mask_file_content(content)
        
        # Save masked content
        output_file = output_dir / input_file.name
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(masked_content)
        except Exception as e:
            self.logger.error(f"Failed to write {output_file}: {e}")
            self.stats['errors'] += 1
            return
        
        # Save placeholders mapping for debugging
        if placeholders:
            placeholders_file = output_dir / f"{input_file.stem}_placeholders.json"
            try:
                with open(placeholders_file, 'w', encoding='utf-8') as f:
                    json.dump(placeholders, f, indent=2, ensure_ascii=False)
            except Exception as e:
                self.logger.warning(f"Failed to save placeholders for {input_file}: {e}")
        
        self.stats['files_processed'] += 1
        self.stats['placeholders_created'] += len(placeholders)
        
        self.logger.debug(f"Processed {input_file.name}: {len(placeholders)} placeholders created")
    
    def run(self):
        """Run the preprocessing pipeline"""
        self.logger.info("🚀 Starting golden data preprocessing...")
        self.logger.info(f"Input directory: {self.content_dir}")
        self.logger.info(f"Output directory: {self.output_dir}")
        self.logger.info(f"Languages: {', '.join(self.languages)}")
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Process topics and changelogs
        for subdir in ["topics", "changelogs"]:
            subdir_path = self.content_dir / subdir
            if subdir_path.exists():
                self.process_directory(subdir)
            else:
                self.logger.warning(f"Subdirectory not found: {subdir_path}")
        
        # Generate summary
        self.generate_summary()
        
        self.logger.info("✅ Preprocessing completed!")
    
    def generate_summary(self):
        """Generate preprocessing summary"""
        summary = {
            'input_directory': str(self.content_dir),
            'output_directory': str(self.output_dir),
            'languages_processed': self.languages,
            'statistics': self.stats,
            'masking_patterns': len(MaskingConfig.mask_patterns)
        }
        
        summary_file = self.output_dir / "preprocessing_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Log summary
        self.logger.info("📊 Preprocessing Summary:")
        self.logger.info(f"  Files processed: {self.stats['files_processed']}")
        self.logger.info(f"  Files skipped: {self.stats['files_skipped']}")
        self.logger.info(f"  Errors: {self.stats['errors']}")
        self.logger.info(f"  Total placeholders created: {self.stats['placeholders_created']}")
        self.logger.info(f"  Summary saved to: {summary_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Preprocess golden data for soft prompt tuning by masking non-translatable elements',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all available languages
  python preprocess_golden_data.py --content-dir content --output-dir content_masked
  
  # Process specific languages
  python preprocess_golden_data.py --content-dir content --output-dir content_masked --languages fr de
  
  # Process with verbose logging
  python preprocess_golden_data.py --content-dir content --output-dir content_masked --verbose

This script will:
1. Read your golden dataset from content/
2. Apply masking to protect shortcodes, URLs, and system variables
3. Remove TRANSLATE_THIS: markers (not needed for soft prompts)
4. Save masked versions to the output directory
5. Generate placeholder mappings for debugging
        """
    )
    
    parser.add_argument('--content-dir', type=Path, default='content',
                       help='Input content directory with golden data')
    parser.add_argument('--output-dir', type=Path, default='content_masked',
                       help='Output directory for masked content')
    parser.add_argument('--languages', nargs='+', default=['en', 'fr', 'de', 'nl'],
                       help='Languages to process')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Setup logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate input directory
    if not args.content_dir.exists():
        print(f"❌ Content directory not found: {args.content_dir}")
        return 1
    
    # Run preprocessing
    preprocessor = GoldenDataPreprocessor(
        content_dir=args.content_dir,
        output_dir=args.output_dir,
        languages=args.languages
    )
    
    preprocessor.run()
    return 0


if __name__ == "__main__":
    exit(main()) 