# generate_preprocessed_jsonl.py

import os
import json
import re
from pathlib import Path

# --- Preprocessor Class ---
class TranslationPreprocessor:
    def __init__(self):
        self.shortcode_pattern = re.compile(r"\{\{<\s*(/?)([^\s>]+)(.*?)\s*>}}")
        self.app_element_pattern = re.compile(r"\{\{<\s*AppElement\s+type=\"(.*?)\"\s*>}}|\{\{<\s*/AppElement\s*>}}")
        self.ref_pattern = re.compile(r"\{\{<\s*ref\s+path=\"(.*?)\"\s+lang=\"(.*?)\"\s*>}}")
        self.image_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
        self.link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)")

        # For tracking mappings between input and output
        self.mapping = {}
        self.counter = 1

    def reset_counter(self):
        """Reset counter for new document pair to ensure consistent masking"""
        self.mapping = {}
        self.counter = 1

    def _next_key(self, prefix: str) -> str:
        key = f"{prefix}_{self.counter}"
        self.counter += 1
        return key

    def mask_shortcodes(self, text: str) -> str:
        def replace_shortcode(match):
            key = self._next_key("SHORTCODE")
            self.mapping[key] = match.group(0)
            return f"[{key}]"
        return self.shortcode_pattern.sub(replace_shortcode, text)

    def mask_ref_tags(self, text: str) -> str:
        def replace_ref(match):
            key = self._next_key("REF")
            self.mapping[key] = match.group(0)
            return f"[{key}]"
        return self.ref_pattern.sub(replace_ref, text)

    def mask_app_elements(self, text: str) -> str:
        def replace_app(match):
            key = self._next_key("APP")
            self.mapping[key] = match.group(0)
            return f"[{key}]"
        return self.app_element_pattern.sub(replace_app, text)

    def mask_images(self, text: str) -> str:
        def replace_img(match):
            alt_text, url = match.groups()
            # Check if alt_text already has TRANSLATE_THIS prefix
            if alt_text.startswith("TRANSLATE_THIS: "):
                return f"![{alt_text}]({url})"
            else:
                return f"![TRANSLATE_THIS: {alt_text}]({url})"
        return self.image_pattern.sub(replace_img, text)

    def mask_links(self, text: str) -> str:
        def replace_link(match):
            link_text, url = match.groups()
            # Check if link_text already has TRANSLATE_THIS prefix
            if link_text.startswith("TRANSLATE_THIS: "):
                return f"[{link_text}]({url})"
            else:
                return f"[TRANSLATE_THIS: {link_text}]({url})"
        return self.link_pattern.sub(replace_link, text)

    def mask_images_output(self, text: str) -> str:
        """Mask images for output without TRANSLATE_THIS markers"""
        def replace_img(match):
            alt_text, url = match.groups()
            # Remove TRANSLATE_THIS prefix if present for output
            if alt_text.startswith("TRANSLATE_THIS: "):
                alt_text = alt_text[15:]  # Remove "TRANSLATE_THIS: " prefix
            return f"![{alt_text}]({url})"
        return self.image_pattern.sub(replace_img, text)

    def mask_links_output(self, text: str) -> str:
        """Mask links for output without TRANSLATE_THIS markers"""
        def replace_link(match):
            link_text, url = match.groups()
            # Remove TRANSLATE_THIS prefix if present for output
            if link_text.startswith("TRANSLATE_THIS: "):
                link_text = link_text[15:]  # Remove "TRANSLATE_THIS: " prefix
            return f"[{link_text}]({url})"
        return self.link_pattern.sub(replace_link, text)

    def preprocess_text(self, text: str, is_output: bool = False) -> str:
        """Apply masking to text content"""
        text = self.mask_shortcodes(text)
        text = self.mask_app_elements(text)
        text = self.mask_ref_tags(text)
        
        # Use different image/link masking for input vs output
        if is_output:
            text = self.mask_images_output(text)
            text = self.mask_links_output(text)
        else:
            text = self.mask_images(text)
            text = self.mask_links(text)
        return text

    def preprocess_frontmatter(self, frontmatter: dict, is_output: bool = False) -> dict:
        """Apply masking to frontmatter, preserving structure"""
        processed_frontmatter = frontmatter.copy()
        translatable_keys = {"title", "summary"}
        
        if "hero" in processed_frontmatter and isinstance(processed_frontmatter["hero"], dict):
            if "title" in processed_frontmatter["hero"]:
                if is_output:
                    # For output, remove TRANSLATE_THIS prefix if present
                    title = processed_frontmatter["hero"]["title"]
                    if title.startswith("TRANSLATE_THIS: "):
                        processed_frontmatter["hero"]["title"] = title[15:]
                else:
                    # For input, add TRANSLATE_THIS prefix if not already present
                    title = processed_frontmatter["hero"]["title"]
                    if not title.startswith("TRANSLATE_THIS: "):
                        processed_frontmatter["hero"]["title"] = f"TRANSLATE_THIS: {title}"
                
        for key in list(processed_frontmatter):
            if key in translatable_keys and isinstance(processed_frontmatter[key], str):
                if is_output:
                    # For output, remove TRANSLATE_THIS prefix if present
                    value = processed_frontmatter[key]
                    if value.startswith("TRANSLATE_THIS: "):
                        processed_frontmatter[key] = value[15:]
                else:
                    # For input, add TRANSLATE_THIS prefix if not already present
                    value = processed_frontmatter[key]
                    if not value.startswith("TRANSLATE_THIS: "):
                        processed_frontmatter[key] = f"TRANSLATE_THIS: {value}"
                
        return processed_frontmatter

    def process_document(self, raw_text: str, is_output: bool = False) -> str:
        """Process a complete document (frontmatter + body) and return masked version"""
        if raw_text.startswith("{"):
            try:
                frontmatter_raw, body_raw = raw_text.split("}\n", 1)
                frontmatter = json.loads(frontmatter_raw + "}")
            except Exception:
                frontmatter = {}
                body_raw = raw_text
        else:
            frontmatter = {}
            body_raw = raw_text

        # Apply preprocessing to both frontmatter and body
        processed_frontmatter = self.preprocess_frontmatter(frontmatter, is_output)
        processed_body = self.preprocess_text(body_raw, is_output)
        
        # Reconstruct the document
        if frontmatter:
            return json.dumps(processed_frontmatter, ensure_ascii=False, indent=2) + "\n\n" + processed_body
        else:
            return processed_body

# --- Main Dataset Generator ---
root_dir = "content"
sections = ["changelogs", "topics"]
languages = {"fr": "French", "de": "German", "nl": "Dutch"}
source_lang = "en"

output_files = {
    "fr": open("dataset-fr.jsonl", "w", encoding="utf-8"),
    "de": open("dataset-de.jsonl", "w", encoding="utf-8"),
    "nl": open("dataset-nl.jsonl", "w", encoding="utf-8")
}

count = {"fr": 0, "de": 0, "nl": 0}

for section in sections:
    base_path = os.path.join(root_dir, section, source_lang)
    filenames = [f for f in os.listdir(base_path) if f.endswith(f".{source_lang}.md")]

    for filename in filenames:
        slug = filename.rsplit(f".{source_lang}.md", 1)[0]
        source_path = os.path.join(root_dir, section, source_lang, filename)

        # Read source (English) file
        with open(source_path, encoding="utf-8") as f:
            source_raw_text = f.read()

        for lang_code, lang_name in languages.items():
            target_file = f"{slug}.{lang_code}.md"
            target_path = os.path.join(root_dir, section, lang_code, target_file)

            if os.path.exists(target_path):
                # Read target (translated) file
                with open(target_path, encoding="utf-8") as tf:
                    target_raw_text = tf.read()

                # Create separate preprocessor instances for input and output to ensure consistent masking
                input_preprocessor = TranslationPreprocessor()
                output_preprocessor = TranslationPreprocessor()

                # Process both input and output with masking
                processed_input = input_preprocessor.process_document(source_raw_text)
                processed_output = output_preprocessor.process_document(target_raw_text, is_output=True)

                # Create the training example
                output_line = {
                    "input": f"Translate English to {lang_name}:\n\n{processed_input}",
                    "output": processed_output
                }
                
                output_files[lang_code].write(json.dumps(output_line, ensure_ascii=False) + "\n")
                count[lang_code] += 1

# Close files
for f in output_files.values():
    f.close()

# Report
print("✅ Preprocessing complete. Generated masked input/output pairs:")
for lang_code, total in count.items():
    print(f"  - {total} examples in dataset-{lang_code}.jsonl")

print("\n📋 Masking applied:")
print("  🔹 INPUT (English):")
print("    - Shortcodes: {{< ... >}} → [SHORTCODE_N]")
print("    - App elements: {{< AppElement ... >}} → [APP_N]") 
print("    - Ref tags: {{< ref ... >}} → [REF_N]")
print("    - Images: ![alt](url) → ![TRANSLATE_THIS: alt](url)")
print("    - Links: [text](url) → [TRANSLATE_THIS: text](url)")
print("    - Frontmatter titles/summaries → TRANSLATE_THIS: content")
print("  🔹 OUTPUT (Translated):")
print("    - Shortcodes: {{< ... >}} → [SHORTCODE_N]")
print("    - App elements: {{< AppElement ... >}} → [APP_N]") 
print("    - Ref tags: {{< ref ... >}} → [REF_N]")
print("    - Images: ![alt](url) → ![alt](url) (clean)")
print("    - Links: [text](url) → [text](url) (clean)")
print("    - Frontmatter titles/summaries → clean content (no markers)")
print("  ✅ This teaches the model to translate marked content cleanly!")
