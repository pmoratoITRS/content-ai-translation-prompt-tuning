{
  "hero": {
    "title": "Fehlerbedingungen – von der Seite geladene URLs überprüfen"
  },
  "title": "Fehlerbedingungen – von der Seite geladene URLs überprüfen",
  "summary": "Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-url-check",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Browserbasierte Monitoring-Typen wie etwa [Full Pagechecks]([LINK_URL_1]) und [Transaktionen]([LINK_URL_2]) laden deine Seiten in einem tatsächlichen Browser. Beim Laden erzeugt der Browser ein [Wasserfalldiagramm]([LINK_URL_3]), in dem alle Seitenobjekte und auf der Website geladene Ressourcen aufgeführt sind.

Diese geladenen Objekte umfassen eigene Inhalte wie das original HTML-Dokument, Bilder, Videos und andere Medien, die vom selben Netzwerk gehostet werden. Es können auch Fremdanbieterinhalte oder externe Ressourcen wie Monitoring-Skripte oder Analyse-Tools enthalten sein. Jedes dieser Objekte erscheint als einzelner Eintrag im Wasserfalldiagramm, mit einer eigenen Abfrage-URL und Ladezeitwerte.

## Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟

Die [Fehlerbedingung]([LINK_URL_4]) **Von der Seite geladene URLs überprüfen** prüft, ob bestimmte Seitenobjekte von deiner Website geladen werden. Sie verifiziert, ob die Abfrage-URL dieser Objekte im Wasserfalldiagramm aufgeführt ist oder nicht.

Beispielsweise möchtest du vielleicht feststellen, ob das [Uptrends Real User Monitoring]([LINK_URL_5]) auf einer Seite geladen wird. Die Fehlerbedingung **Von der Seite geladene URLs überprüfen** weist das Prüfobjekt an, zu prüfen, ob die Abfrage-URL eines der Wasserfall-Objekte [INLINE_CODE_1] entspricht.

Darüber hinaus ermöglicht diese Fehlerbedingung, bestimmte Kriterien zur Prüfung der Werte jeder Abfrage-URL anzugeben. Wenn du zum Beispiel einen Fehler erzeugen möchtest, wenn dein Bild [INLINE_CODE_2] länger als 2 Sekunden lädt oder wenn eine Datei einen Statuscode über 400 ergibt, kannst du für jedes Kriterien festlegen.

## „Von der Seite geladene URLs überprüfen‟ einrichten

Um zu prüfen, ob ein bestimmtes Seitenobjekt auf deiner Website sichtbar ist, benötigst du eine Fehlerbedingung des Typs **Von der Seite geladene URLs überprüfen**:

1. Gehe zu [SHORTCODE_1] Überwachung > Prüfobjekteinrichtung [SHORTCODE_2].
2. Klicke auf das Prüfobjekt, für das du eine Abfrage-URL prüfen möchtest.
3. Wechsle zum Tab [SHORTCODE_3]Fehlerbedingungen[SHORTCODE_4].
4. Klicke auf [SHORTCODE_5] + Neue Prüfung [SHORTCODE_6] unter **Von der Seite geladene URLs überprüfen**.
5. Wähle einen Fehlertyp, um festzulegen, ob das Prüfobjekt einen Fehler erzeugen soll, falls die Abfrage-URL im Wasserfalldiagramm erscheint oder nicht erscheint.
6. Gib die Abfrage-URL in das Textfeld ein. Es können reguläre Ausdrücke als Wert angegeben werden.
7. (Optional) Um zusätzliche Kriterien zur Prüfung der Abfrage-URL einzurichten, klicke auf [SHORTCODE_7] +Zusätzliche Bedingung hinzufügen [SHORTCODE_8]. Gib dann deine Bedingungen anhand der verfügbaren Optionen an:

  - Wähle **Antwortgröße** mit entsprechendem Vergleichsoperator und dem Wert in Bytes (B).
  - Wähle **Gesamtzeit** mit entsprechendem Vergleichsoperator und dem Wert in Millisekunden (ms).
  - Wähle **Status Code** mit entsprechendem Vergleichsoperator und dem Wert.

8. Klicke auf die [SHORTCODE_9]Speichern[SHORTCODE_10]-Schaltfläche, um die Prüfobjektänderungen zu sichern.

![Zusätzliche Bedingungen für von der Seite geladene URLs überprüfen]([LINK_URL_6])

## Beispiele

### Uptrends RUM-Skript lädt auf der Website

Das Beispiel zeigt die Fehlerbedingung, die prüft, ob das Uptrends RUM-Skript korrekt konfiguriert wurde. Wenn die [INLINE_CODE_3]-Abfrage-URL nicht in der Liste geladener Seitenobjekte ist, erzeugt das Prüfobjekt einen [Fehler]([LINK_URL_7]).

![Prüfe URL: Uptrends RUM]([LINK_URL_8])

### Bild lädt auf der Website

Das Beispiel zeigt die Fehlerbedingung, die prüft, ob die Abfrage-URL, [INLINE_CODE_4], in der Liste geladener Seitenobjekte mit mehr als 1000 Millisekunden erscheint. Wenn die Ladezeit der URL die Gesamtzeit überschreitet, erzeugt das Prüfobjekt einen [Fehler]([LINK_URL_9]).

![Prüfe URL: Uptrends RUM]([LINK_URL_10])