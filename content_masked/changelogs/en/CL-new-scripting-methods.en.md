{
  "title": "New scripting methods are now available in Multi-step API (MSA) monitors",
  "date": "2025-03-12",
  "url": "[URL_BASE_CHANGELOG]march-2025-new-scripting-methods",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The following scripting methods can now be used in the [Pre-request and Post-response scripting]([LINK_URL_1]) tabs of Multi-step API (MSA) monitors:

- [INLINE_CODE_1] — parses a certificate revocation list and returns its metadata.
- [INLINE_CODE_2] — generates an MD5 hash of the specified value.
- [INLINE_CODE_3] — generates an SHA-1 hash of the specified value.
- [INLINE_CODE_4] — generates an SHA-256 hash of the specified value.
- [INLINE_CODE_5] — generates an SHA-512 hash of the specified value.
- [INLINE_CODE_6] — returns a byte array containing the response body. Responses are limited to 100 MB.

Note that [INLINE_CODE_7] is only available in the [SHORTCODE_1] Post-response [SHORTCODE_2] tab of your MSA monitor. The scripting methods for generating MD5 and SHA hashes enable you to store and send values securely, ensuring data protection through hashing.