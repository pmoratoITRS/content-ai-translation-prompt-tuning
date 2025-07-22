{
  "hero": {
    "title": "Monitoring von Webservices"
  },
  "title": "Monitoring von Webservices",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/monitoring-webservices",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1] **Hinweis:** Für das API-Monitoring sind die Prüfobjekttypen **Webservice HTTP und Webservice HTTPS** für neue Nutzer nicht mehr verfügbar. Uptrends empfiehlt, stattdessen das [Multi-step API-Prüfobjekt]([LINK_URL_1]) zu nutzen, und das Verhalten deiner API eingehender zu prüfen. [SHORTCODE_2]

Uptrends‛ Webservice HTTP- und HTTPS-Prüfobjekte gehören zu den verschiedenen [Prüfobjekttypen]([LINK_URL_2]), die Uptrends bietet. 

## Welche Webservices werden unterstützt?

Uptrends unterstützt *REST* und *SOAP* sowie alle Webservices, die über *HTTP* bzw. *HTTPS* erreichbar sind.

## Wie funktionieren diese Webservices mit Uptrends?

- Wir überwachen, dass die Webservice-Antwort HTTP 200 OK lautet und messen die Auflösungs-/Verbindungszeit, Ladezeit und Gesamtzeit, genauso wie HTTP(S)-Prüfobjekte.  
- Das Webservice Monitoring unterstützt auch grundlegende Authentifizierung, Inhaltsüberwachung usw.  
- Die meisten Webservice-Prüfobjekte verwenden HTTP POST-Einstellungen, um Daten an den Server als Teil eines Webservice-Aufrufs zu senden.  
- Üblicherweise benötigen SOAP-Services ein XML-Dokument (SOAP-Envelope) als POST-Daten im Anfrage-Body sowie einen bestimmten HTTP-Header, SOAPAction genannt.  
- Einige Webservices erfordern das Einrichten der HTTP-Header für Content-Type

**Zum Beispiel**:

- \[INLINE_CODE_1], wenn die POST-Daten JSON-Daten sind  
- \[INLINE_CODE_2] oder application/xml, wenn die POST-Daten XML sind (dies ist die Standardeinstellung für Webservice-Prüfobjekte, anders als bei regulären HTTP(S)-Prüfobjekten)
