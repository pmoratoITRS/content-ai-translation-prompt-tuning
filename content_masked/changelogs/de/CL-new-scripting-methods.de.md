{
  "title": "Neue Skriptmethoden sind bei Multi-Step API (MSA)-Prüfobjekten verfügbar",
  "date": "2025-03-12",
  "url": "[URL_BASE_CHANGELOG]maerz-2025-neue-skriptmethoden",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die folgenden Skriptmethoden können nun auf den Tabs für [Vor-Anfrage- und Nach-Antwort-Skripte]([LINK_URL_1]) bei Multi-Step API (MSA)-Prüfobjekten verwendet werden:

- [INLINE_CODE_1] – parst eine Revozierungsliste von Zertifikaten und gibt ihre Metadaten zurück.
- [INLINE_CODE_2] – generiert einen MD5-Hash des angegebenen Werts.
- [INLINE_CODE_3] – generiert einen SHA-1-Hash des angegebenen Werts.
- [INLINE_CODE_4] – generiert einen SHA-256-Hash des angegebenen Werts.
- [INLINE_CODE_5] – generiert einen SHA-512-Hash des angegebenen Werts.
- [INLINE_CODE_6] – gibt eine Byte-Zeichenfolge mit der Antwort aus. Antworten sind auf 100 MB begrenzt.

Beachte, dass [INLINE_CODE_7] nur auf dem Tab [SHORTCODE_1] Nach-Antwort [SHORTCODE_2] des MSA-Prüfobjekts verfügbar ist. Die Skriptmethoden zur Generierung von MD5- und SHA-Hashes ermöglichen dir, Werte sicher zu speichern und zu senden. Der Datenschutz wird durch das Hashen gewährleistet.