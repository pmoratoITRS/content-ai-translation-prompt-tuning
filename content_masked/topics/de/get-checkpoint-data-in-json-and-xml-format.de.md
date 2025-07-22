{
  "hero": {
    "title": "Checkpoint-Daten im JSON- und XML-Format abrufen"
  },
  "title": "Checkpoint-Daten im JSON- und XML-Format abrufen",
  "summary": "Wenn du die Uptrends API nutzt, um Checkpoint-Informationen abzurufen, kannst du diese Informationen in unterschiedlichen Formaten erhalten.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/checkpoint-daten-in-json-und-xml-format-abrufen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

JSON- und XML-Downloads von Checkpoint-Daten sind über unsere API verfügbar. Die vollständige Dokumentation für diese API findest du [hier]([LINK_URL_1]).

Du kannst unsere API verwenden, um eine Liste aller IPv4- oder IPv6-Adressen für alle Checkpoints von Uptrends abzurufen, darunter zukünftige Adressen geänderter oder neuer Checkpoints. Antworten sind sowohl als JSON wie auch als XML, abhängig von deinem [INLINE_CODE_1] Header verfügbar.

Wir halten auch einfache Listen von [IPv4-Adressen]([LINK_URL_2]) und [IPv6-Adressen]([LINK_URL_3]) zum Download bereit.

Alle auf dieser Seite genannten Methoden und Links liefern eine Liste von Checkpoint-IP-Adressen, die auch **zukünftige Adressen** umfassen (wie in unserem monatlichen Newsletter angekündigt).

#### Liste der IPv4-Adressen:
Sende eine GET-Abfrage mit dem Header [INLINE_CODE_2] an [INLINE_CODE_3]. Eine Authentifizierung ist nicht erforderlich.

Wenn du *Curl* nutzt, wäre ein Beispiel:
[CODE_BLOCK_1]

Ersetze *application/json* durch *application/xml*, wenn du eine XML-Antwort benötigst.

#### Liste der IPv6-Adressen: 
Es gilt dasselbe wie für IPv4, die Abfrage sollte aber an [INLINE_CODE_4] gesendet werden.


[SHORTCODE_1]
**Tipp**: Statt *Curl* kannst du ein Powershell Invoke-Webrequest nutzen.
[SHORTCODE_2]
