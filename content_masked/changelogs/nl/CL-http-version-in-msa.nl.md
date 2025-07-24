{
  "title": "Ondersteuning voor specifieke HTTP-versies is nu beschikbaar in de Multi-step API (MSA)-controleregelstappen",
  "date": "2025-04-03",
  "url": "[URL_BASE_CHANGELOG]april-2025-http-versie-in-multi-step-api-controleregels",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het is nu mogelijk om de HTTP-versie voor elke stap van een MSA-controleregel te specificeren. Hiermee kunt u bepalen welke HTTP-versie de controlestationservers gebruiken bij requests:

![HTTP-versie]([LINK_URL_1])

Standaard is de optie **HTTP-versie** uitgeschakeld, wat betekent dat de server automatisch de hoogste HTTP-versie gebruikt die ondersteund wordt en beschikbaar is, met een fallback niet lager dan HTTP/1.1. HTTP/3 is momenteel beschikbaar op geselecteerde controlestationlocaties en de ondersteuning zal binnenkort worden uitgebreid naar meer locaties.

Overigens kunt u met de HTTP-configuratie slechts één versie selecteren, terwijl de TLS-configuratie de selectie van meerdere versies ondersteunt. Dit komt doordat TLS versieonderhandeling ondersteunt tijdens het verbindingsproces, terwijl HTTP/3 dit niet doet en vereist dat een specifieke versie wordt gedefinieerd.