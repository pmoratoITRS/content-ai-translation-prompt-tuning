{
  "hero": {
    "title": "Das Postman-API-Monitoring einrichten"
  },
  "title": "Das Postman-API-Monitoring einrichten",
  "summary": "Schritt-für-Schritt-Anleitung für das Einrichten des Postman-API-Monitorings.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/postman-api-monitoring"
}

Uptrends bietet das Postman-API-Prüfobjekt, mit dem du deine bestehenden Postman-Workspace-Sammlungen im Uptrends Checkpoint-Netzwerk direkt ausführen kannst. Du kannst ganz einfach Postman-Skripte planen und ausführen, die Performance deiner APIs testen und alles wie bei jedem anderen Prüfobjekt einrichten.

Postman ist ein Standardtool der Branche, das Entwickler nutzen, um API-Tests zu schreiben, zu dokumentieren und auszuführen. Es wird von Millionen genutzt. Mit diesem Tool kannst du HTTP-Methoden (GET, POST, PUT, DELETE, PATCH) testen und Header, Parameter, Variablen und vieles mehr hinzufügen. Du kannst auch mehrere Abfragen, Postman-Sammlungen genannt, gruppieren und ordnen und sie für andere oder zur späteren Nutzung freigeben. Rufe einfach Postman auf und du kannst deine API-Skripte mit einem Klick ausführen, wenn du deine APIs testen möchtest.

Bei Uptrends musst du nicht Postman aufrufen und dies manuell anstoßen, um Skripte zu testen. Dein Postman-API-Prüfobjekt erledigt die Arbeit für dich. Das Prüfobjekt nimmt deine Postman-Sammlung an API-Skripten, einschließlich Pre- und Post-Request-Skripte, importiert sie anhand einer API-URL oder aus einer JSON-Datei und führt sie dann auf der ganzen Welt aus, ähnlich wie andere Prüfobjekttypen.

## Vorteile des Postman-API-Prüfobjekts

Wenn dein Unternehmen bereits Postman nutzt, setze dieses Prüfobjekt ein und profitiere von den folgenden Vorteilen:

- **Automatische Ausführung deiner Skripte**: Du kannst deine Postman-Skripte jede Minute, alle 5 Minuten oder jede Stunde sowie überall auf der Welt ausführen, statt sie manuell laufen zu lassen. Wir haben über 200 Monitoring [Checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/" lang="de" >}}), unter denen du wählen und mit denen du deine Skripte testen kannst.  

- **Keine Vorbereitungszeit**: Einfach deine bestehenden Skripte in Uptrends importieren und dein Prüfobjekt ist buchstäblich konfiguriert und kann ausgeführt werden. Es besteht keine Notwendigkeit, diese Skripte an Uptrends’ Konventionen anzupassen oder andere Änderungen vorzunehmen.

- **Nichts Neues zu lernen**: Mit deinen Kenntnissen von Postman wird es dir leichtfallen, dieses Prüfobjekt zu nutzen. Verweise einfach auf deine Postman-Skripte und wir berichten dir blitzschnell von den Ergebnissen.

- **Keine Änderungen an deinem aktuellen Workflow**: Du kannst einfach mit der Verwaltung deiner Skripte in Postman fortfahren. Denke einfach daran, nach Änderungen an deiner Sammlung sie erneut in Uptrends abzurufen – dann ist alles auf dem neuesten Stand.

{{< callout >}} [Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/" lang="de" >}}) werden beim Postman-API-Prüfobjekt noch nicht unterstützt. {{< /callout >}}

## Ein Postman-API-Prüfobjekt einrichten

Es gibt zwei Möglichkeiten, ein Postman-API-Prüfobjekt einzurichten: [Importieren von Postman-Skripten aus einer JSON-Datei]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#import-from-a-json-file" lang="de" >}}) oder [Importieren von Postman-Skripten anhand einer API-URL]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#import-using-an-api-url" lang="de" >}}).

{{< callout >}} **Hinweis:** Nutze beim Importieren von Postman-Skripten über eine API-URL die Option **Share** > **Via API**. Diese Option steht nur bei kostenpflichtigen Postman-Accounts zur Verfügung. {{< /callout >}}

### Aus einer JSON-Datei importieren

Diese Option ermöglicht dir, gleichzeitig ein Back-up deiner Postman-Dateien und das Importieren von Änderungen von Postman nach Uptrends.

Um ein Prüfobjekt anhand eines JSON-Dateiimports einzurichten:

1. Gehe im Menü zu {{< AppElement type="menuitem" >}} API-Prüfobjekte einrichten (+) {{< /AppElement >}}.
2. Wähle die Option **Postman-API**.
3. Konfiguriere die [Prüfobjekteinstellungen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="de" >}}) gemäß deinen Monitoring-Anforderungen.

4. Wähle auf dem Tab {{< AppElement type="tab" >}} Postman-Sammlung {{< /AppElement >}}  
**Aus einer JSON-Datei importieren**. Um zu erfahren, wie du eine JSON-Datei aus Postman zu exportierst, lies [Export collections from Postman](https://learning.postman.com/docs/getting-started/importing-and-exporting/exporting-data#export-collections).

5. Klicke auf die Schaltfläche {{< AppElement type="buttonSecondary" >}} Choose File {{< /AppElement >}} und importiere die JSON-Datei. 

Nach dem Import wird der Abschnitt **Sammlungsdetails** automatisch ausgefüllt und zeigt dieselben Informationen wie in Postman. Daten wie der Sammlungsname, die ID und Abfragen sind nun zu sehen.

![Import JSON-Datei](/img/content/scr_postman-import-json-file.min.png)

6. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Dein Prüfobjekt ist nun eingerichtet. Verwende die Schaltfläche **Jetzt testen** im Einrichtungsfenster, um es zu testen und die
[Prüfobjektergebnisse]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#monitor-results" lang="de" >}}) anzuzeigen.

### Anhand einer API-URL importieren

Diese Option erlaubt dir, Änderungen von Postman nach Uptrends anhand einer API-URL zu importieren. Dies ist beim Live-Testen nützlich. Mit einem Klick wird deine Sammlung aktualisiert und es spart zudem Speicherplatz.

Um ein Prüfobjekt anhand der API-URL der Postman-Sammlung zu erstellen:

1. Gehe im Menü zu {{< AppElement type="menuitem" >}} API-Prüfobjekte einrichten (+) {{< /AppElement >}}.
2. Wähle die Option **Postman-API**.
3. Konfiguriere die [Prüfobjekteinstellungen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="de" >}}) gemäß deinen Monitoring-Anforderungen.

4. Wähle auf dem Tab {{< AppElement type="tab" >}} Postman-Sammlung {{< /AppElement >}}  
**Über API-URL importieren**.

5. Füge die Postman-API-URL in das leere Textfeld ein. Um zu erfahren, wo du die Postman-API-URL findest, lies [Share using the Postman API](https://learning.postman.com/docs/collaborating-in-postman/sharing#share-using-the-postman-api).

6. Klicke auf {{< AppElement type="buttonSecondary" >}} SAMMLUNG ABRUFEN {{< /AppElement >}}, um die Daten von der URL abzufragen.

Nach dem Import wird der Abschnitt **Sammlungsdetails** automatisch ausgefüllt und zeigt dieselben Informationen wie in Postman. Daten wie der Sammlungsname, die ID und Abfragen sind nun zu sehen.

![Import anhand einer API-URL](/img/content/scr_postman-import-api-url.min.png)

{{< callout >}} **Hinweis:** Du musst jedes Mal, wenn du Änderungen an deiner Sammlung vornimmst, auf {{< AppElement type="buttonSecondary" >}} SAMMLUNG ABRUFEN {{< /AppElement >}} klicken. Damit wird sichergestellt, dass Uptrends die letzten Änderungen berücksichtigt und die bestehenden Postman-Skripte, die überwacht werden, überschreibt. {{< /callout >}}

7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Dein Prüfobjekt ist nun eingerichtet. Verwende die Schaltfläche **Jetzt testen** im Einrichtungsfenster, um es zu testen und die
[Prüfobjektergebnisse]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring#monitor-results" lang="de" >}}) anzuzeigen.

Weitere Informationen findest du in der [Postman-Dokumentation](https://learning.postman.com/docs/collaborating-in-postman/sharing).

## Ergebnisse überwachen

Die **Ergebnisse des Postman-API-Prüfobjekts** ähneln den Ergebnissen des Multi-Step API Monitorings. Im Bereich **Kontrolldetails** spiegelt jeder Schritt jede Abfrage wider, die in der Postman-Sammlung enthalten ist – mit den folgenden Elementen:

- **Schrittdauer**: die Dauer (in Millisekunden), in der der Schritt ausgeführt wird
- **Schritt-Assertions**: die tatsächlichen Testergebnisse basierend auf den Vor-Anfrage- und Nach-Antwort-Skripten parallel zu den Postman-Testergebnissen. Du kannst die Gesamtzahl der bestätigten und fehlgeschlagenen Assertions sehen. Bestätigte Ergebnisse sind mit grünem Häkchen markiert, fehlgeschlagene Ergebnisse sind mit einem roten X markiert.
- Es werden auch weitere Daten wie Request Header, Request-Inhalte und Response Header auf gleiche Weise wie in Postman angezeigt. Beispielsweise Cache-Control, Content-Length, Server, Date usw.

## Credits

Wie Multi-Step API-Prüfobjekte sind für das Postman-API-Prüfobjekt API-Credits erforderlich. Jede Abfrage, die in der importierten Sammlung enthalten ist, verbraucht einen Credit.