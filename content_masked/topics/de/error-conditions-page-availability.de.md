{
  "hero": {
    "title": "Fehlerbedingungen – Erreichbarkeit"
  },
  "title": "Fehlerbedingungen – Erreichbarkeit",
  "summary": "Ein Überblick über die verfügbaren Fehlerbedingungen für die Kategorie *Erreichbarkeit*. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-seitenerreichbarkeit",
  "tableofcontents": true,
  "translationKey": "[URL_1]
}

Die Fehlerbedingungen in der Prüfobjekteinrichtung werden verwendet, um Ereignisse zu definieren, für die du einen Hinweis auf einen Fehler erhalten solltest. Lies bitte den Knowledge-Base-Artikel [Fehlerbedingungen]([LINK_URL_1]), um weitere allgemeine Informationen und wie du [Fehlerbedingungen konfigurierst]([LINK_URL_2]) zu erhalten.

Die Fehlerbedingung **Erreichbarkeit** prüft, ob die Seite (HTTP/S- oder Webservice-Prüfobjekt), die Website (Transaktionen) oder Ressource (andere Prüfobjekte) verfügbar sind. Abhängig vom Prüfobjekttyp zeigen die Fehlerbedingungen unterschiedliche Optionen. Sieh dir die Tabelle unter [Welche Fehlerbedingungen sind verfügbar]([LINK_URL_3]) an, um mehr herauszufinden.

Beispielsweise sieht die Verfügbarkeitsprüfung bei einem HTTP(S)- oder Webservice HTTP(S)-Prüfobjekt so aus:

![Screenshot Fehlerbedingung Seitenverfügbarkeit]([LINK_URL_4])

## Allgemeine Verfügbarkeitsprüfung

Standardmäßig prüfen alle Prüfobjekttypen die Erreichbarkeit einer überwachten Website.

Sofern zutreffend, etwa bei einem HTTP(S)- oder Webservice HTTP(S)-Prüfobjekt, führt jeder Antwortstatuscode, der 400 oder darüber lautet, zu einem Fehler. Bei anderen Prüfobjekttypen, z. B. DNS, (S)FTP, Mailserver oder Datenbankserver, gibt es keinen HTTP-Antwortstatuscode, aber es wird geprüft, ob der Server oder Service erreichbar ist.

## HTTP-Statuscode-Prüfung

Bei Prüfobjekttypen, die mit einem HTTP-Statuscode antworten, besteht die Option, auf einen bestimmten Statuscode zu prüfen.

Manchmal erwartest du statt des erfolgreichen Ladens einen Fehlercode oder anderen Code. Wenn du zum Beispiel auf einer alten Webseite eine Weiterleitung zu einer neuen Seite eingerichtet hast, solltest du wissen, wenn die Weiterleitung nicht funktioniert. Möchtest du auf eine bestimmte Antwort prüfen, wähle die Option **Verifiziere die Response HTTP Status Code Prüfungen ...** und einen Statuscode aus der Liste.

Eine vollständige Liste der Statuscodes findest du in der [HTTP Status Code Registry]([LINK_URL_5]) der Internet Assigned Numbers Authority (IANA).
