{
  "hero": {
    "title": "Ein SOAP-Webservice-Prüfobjekt einrichten"
  },
  "title": "SOAP-Einrichtung",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/soap-webservice-pruefobjekt-einrichten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wenn du ein **SOAP-Prüfobjekt** in deinem Uptrends Account einrichten möchtest, findest du die Anleitung in diesem Artikel.

## Ein SOAP-Webservice-Prüfobjekt einrichten

Das Testen eines SOAP-Service beginnt in der Regel mit dem Aufruf einer Methode des Webservice, indem Daten in das Formular eines SOAP Envelopes eingegeben werden, und der anschließenden Verifizierung, dass die Antwort korrekt ist.

1.  Rufe den Konfigurationsbildschirm Prüfobjekt hinzufügen auf. (Wenn du eine Erinnerung brauchst, wie dies geht, lies den Artikel [Ein Prüfobjekt hinzufügen]([LINK_URL_1]) Setze den Prüfobjekttyp auf Webservice HTTP oder Webservice HTTPS.
      
    [SHORTCODE_1]**Hinweis**: Mit dem Prüfobjekttyp Web Service ist sichergestellt, dass wir Content-Type: text/xml nutzen, wenn wir Anfragen an deinen Server senden. Da SOAP Envelopes im XML-Format sind, sollte dies bei den meisten Webservices funktionieren.[SHORTCODE_2]
2.  Gib den entsprechenden Namen ein, prüfe das Interval, die URL und die Port-Angabe.
3.  Rufe die Registerkarte [SHORTCODE_5]Erweitert[SHORTCODE_6] auf und setze die HTTP-Methode auf POST.
4.  Gib dein SOAP Request (den kompletten SOAP Envelope) in das „Post“-Feld ein.
      
    In der Regel sieht dies folgendermaßen aus:
    *… Mitteilung hier einsetzen …*
5.  Dein Webserver erwartet wahrscheinlich einen SOAPAction HTTP-Header, der dem Server mitteilt, welche Methode dein Webservice ausführen soll.
      
    Gib im Feld HTTP Headers den Header im folgenden Format ein:
      
    [INLINE_CODE_1]
      
    [SHORTCODE_3]**Hinweis**: Wenn dein Webserver einen anderen Content-Type erwartet, kannst du einen anderen Content-Type im HTTP-Header-Feld eingeben. Zum Beispiel: Content-Type: application/xml[SHORTCODE_4]
6.  Es wird nützlich sein, zu verifizieren, dass dein Webservice den richtigen Inhalt liefert.
      
    Du kannst nach einem bestimmten Inhalt suchen, indem du ihn in das Feld *Übereinstimmungsmuster* eingibst. Das Feld findest du auf der Registerkarte [SHORTCODE_7]Fehlerbedingungen[SHORTCODE_8].
      
    Der Uptrends Service sucht dann den Inhalt in der HTTP-Antwort, jedes Mal, wenn die Prüfung ausgeführt wird.

## Dein SOAP-Prüfobjekt funktioniert nicht?

Wenn dein SOAP-Prüfobjekt nicht funktioniert, wende dich bitte an den Support, indem du ein [Support-Ticket]([LINK_URL_2]) einreichst.

Bitte sende, sofern möglich, einen Screenshot einer HTTP-Anfrage, von der du weißt, dass sie funktioniert. In der Regel verfügst du über eine funktionierende Einrichtung in deinem eigenen Webservice-Testtool, das du nutzen kannst, um eine Fiddler-Aufzeichnung zu erhalten, oder anhand eines cURL-Befehls, der alle notwendigen Daten (URL/POST-Daten/HTTP-Header) enthält.
