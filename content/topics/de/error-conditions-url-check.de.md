{
  "hero": {
    "title": "Fehlerbedingungen – von der Seite geladene URLs überprüfen"
  },
  "title": "Fehlerbedingungen – von der Seite geladene URLs überprüfen",
  "summary": "Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-url-check",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-url-check",
  "tableofcontents": true
}

Browserbasierte Monitoring-Typen wie etwa [Full Pagechecks]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) und [Transaktionen]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) laden deine Seiten in einem tatsächlichen Browser. Beim Laden erzeugt der Browser ein [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}), in dem alle Seitenobjekte und auf der Website geladene Ressourcen aufgeführt sind.

Diese geladenen Objekte umfassen eigene Inhalte wie das original HTML-Dokument, Bilder, Videos und andere Medien, die vom selben Netzwerk gehostet werden. Es können auch Fremdanbieterinhalte oder externe Ressourcen wie Monitoring-Skripte oder Analyse-Tools enthalten sein. Jedes dieser Objekte erscheint als einzelner Eintrag im Wasserfalldiagramm, mit einer eigenen Abfrage-URL und Ladezeitwerte.

## Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟

Die [Fehlerbedingung]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) **Von der Seite geladene URLs überprüfen** prüft, ob bestimmte Seitenobjekte von deiner Website geladen werden. Sie verifiziert, ob die Abfrage-URL dieser Objekte im Wasserfalldiagramm aufgeführt ist oder nicht.

Beispielsweise möchtest du vielleicht feststellen, ob das [Uptrends Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="de" >}}) auf einer Seite geladen wird. Die Fehlerbedingung **Von der Seite geladene URLs überprüfen** weist das Prüfobjekt an, zu prüfen, ob die Abfrage-URL eines der Wasserfall-Objekte `hit.uptrends.com/.*` entspricht.

Darüber hinaus ermöglicht diese Fehlerbedingung, bestimmte Kriterien zur Prüfung der Werte jeder Abfrage-URL anzugeben. Wenn du zum Beispiel einen Fehler erzeugen möchtest, wenn dein Bild `uptrends.png` länger als 2 Sekunden lädt oder wenn eine Datei einen Statuscode über 400 ergibt, kannst du für jedes Kriterien festlegen.

## „Von der Seite geladene URLs überprüfen‟ einrichten

Um zu prüfen, ob ein bestimmtes Seitenobjekt auf deiner Website sichtbar ist, benötigst du eine Fehlerbedingung des Typs **Von der Seite geladene URLs überprüfen**:

1. Gehe zu {{< AppElement type="menuitem" >}} Überwachung > Prüfobjekteinrichtung {{< /AppElement >}}.
2. Klicke auf das Prüfobjekt, für das du eine Abfrage-URL prüfen möchtest.
3. Wechsle zum Tab {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}}.
4. Klicke auf {{< AppElement type="buttonSecondary" >}} + Neue Prüfung {{< /AppElement >}} unter **Von der Seite geladene URLs überprüfen**.
5. Wähle einen Fehlertyp, um festzulegen, ob das Prüfobjekt einen Fehler erzeugen soll, falls die Abfrage-URL im Wasserfalldiagramm erscheint oder nicht erscheint.
6. Gib die Abfrage-URL in das Textfeld ein. Es können reguläre Ausdrücke als Wert angegeben werden.
7. (Optional) Um zusätzliche Kriterien zur Prüfung der Abfrage-URL einzurichten, klicke auf {{< AppElement type="buttonSecondary" >}} +Zusätzliche Bedingung hinzufügen {{< /AppElement >}}. Gib dann deine Bedingungen anhand der verfügbaren Optionen an:

  - Wähle **Antwortgröße** mit entsprechendem Vergleichsoperator und dem Wert in Bytes (B).
  - Wähle **Gesamtzeit** mit entsprechendem Vergleichsoperator und dem Wert in Millisekunden (ms).
  - Wähle **Status Code** mit entsprechendem Vergleichsoperator und dem Wert.

8. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um die Prüfobjektänderungen zu sichern.

![Zusätzliche Bedingungen für von der Seite geladene URLs überprüfen](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

## Beispiele

### Uptrends RUM-Skript lädt auf der Website

Das Beispiel zeigt die Fehlerbedingung, die prüft, ob das Uptrends RUM-Skript korrekt konfiguriert wurde. Wenn die `hit.uptrends.com/.*`-Abfrage-URL nicht in der Liste geladener Seitenobjekte ist, erzeugt das Prüfobjekt einen [Fehler]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}}).

![Prüfe URL: Uptrends RUM](/img/content/scr-error-conditions-url-check.min.png)

### Bild lädt auf der Website

Das Beispiel zeigt die Fehlerbedingung, die prüft, ob die Abfrage-URL, `stars.png`, in der Liste geladener Seitenobjekte mit mehr als 1000 Millisekunden erscheint. Wenn die Ladezeit der URL die Gesamtzeit überschreitet, erzeugt das Prüfobjekt einen [Fehler]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}}).

![Prüfe URL: Uptrends RUM](/img/content/scr-error-conditions-url-check.min.png)