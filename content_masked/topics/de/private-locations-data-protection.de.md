{
  "hero": {
    "title": "Private Standorte – Datenschutz"
  },
  "title": "Private Standorte – Datenschutz",
  "summary": "Was sind die Vorkehrungen zum Datenschutz bei privaten Standorten?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-standorte/private-locations-datenschutz",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mit diesem Knowledge-Base-Artikel wird erläutert, wie du den Datenschutz bei deinen privaten Standorten bzw. Private Locations einrichtest. Eine der in Uptrends’ Private Locations eingerichteten Vorkehrungen verhindert den Upload von Screenshots in die Cloud. Du kannst auch Seiteninhalt deaktivieren, HTTP-Abfrage- und Antwort-Header sowie die aufgelösten IP-Adressen in den Prüfergebnissen verbergen.

## Die Docker Compose-Datei bearbeiten

Zuerst, sofern nicht schon geschehen, solltest du deinen Checkpoint gemäß den Schritten wie in [Einen Docker-Checkpoint installieren]([LINK_URL_1]) aufgeführt, installieren.

1. Erstelle ein Back-up der extrahierten Docker Compose-Datei. Bitte beachte: Wenn du Änderungen an der bereitgestellten Compose-Datei vornimmst, erfolgt das auf dein eigenes Risiko. [Wende dich an den Support]([LINK_URL_2]), wenn du nicht sicher bist.
2. Öffne die Datei docker-compose.yml und entferne den Kommentar-Tag `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]- AllowScreenshotsInResults=false[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]- AllowPageContentInResults=false[INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10]- AllowHttpHeadersInResults=false[INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13]- AllowResolvedIpAddressesInResults=false[INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16]- AllowResolvedIpAddressesInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.

DNS-Prüfobjekte werden an das Ausführen auf Checkpoint-Servern an deinen privaten Standorten gehindert, wenn dieser Wert auf „false“ gesetzt ist.

[SHORTCODE_3] **Bitte beachten**: Nicht alle Einstellungen decken jeden Prüfobjekttyp ab. Zum Beispiel funktionieren für Basic HTTP(S)-Prüfobjekte nur Fehler-Screenshot-Einstellungen, die Einstellungen zu aufgelösten IP-Adressen gelten nicht für diesen Prüfobjekttyp.
[SHORTCODE_4]

## Status Datenschutzeinstellungen 

Die Registerkarte [Checkpoint-Zustand]([LINK_URL_9]) in der Uptrends Anwendung zeigt den Status der Datenschutzeinstellungen. Ein rotes Kreuz besagt, dass Daten nicht angezeigt werden, ein Datenschutz also aktiviert ist. Beachte bitte, dass dies nur eine Anzeige ohne Bearbeitungsmöglichkeit ist. Die Einstellungen können nur in der Docker-Datei angepasst werden.

![Datenschutzeinstellungen auf der Registerkarte Checkpoint-Zustand]([LINK_URL_10])