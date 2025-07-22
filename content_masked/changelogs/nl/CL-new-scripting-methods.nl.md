{
  "title": "Nieuwe scriptingmethodes zijn nu beschikbaar in Multi-step API (MSA)-controleregels",
  "date": "2025-03-12",
  "url": "[URL_BASE_CHANGELOG]maart-2025-nieuwe-scriptingmethodes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De volgende scriptingmethodes kunnen nu worden gebruikt in de tabbladen [Pre-request en Post-response scripting]([LINK_URL_1]) van Multi-step API (MSA)-controleregels:

- [INLINE_CODE_1] — parseert een certificaatintrekkingslijst en retourneert de metadata.
- [INLINE_CODE_2] — genereert een MD5-hash van de opgegeven waarde.
- [INLINE_CODE_3] — genereert een SHA-1-hash van de opgegeven waarde.
- [INLINE_CODE_4] — genereert een SHA-256-hash van de opgegeven waarde.
- [INLINE_CODE_5] — genereert een SHA-512-hash van de opgegeven waarde.
- [INLINE_CODE_6] — retourneert een byte-array met de response body. Responses zijn beperkt tot 100 MB.

Houd er rekening mee dat [INLINE_CODE_7] alleen beschikbaar is in het tabblad [SHORTCODE_1] Post-response [SHORTCODE_2] van uw MSA-controleregel. Met de scriptingmethodes voor het genereren van MD5- en SHA-hashes kunt u waarden veilig opslaan en verzenden, waardoor gegevensbescherming door hashing wordt gewaarborgd.