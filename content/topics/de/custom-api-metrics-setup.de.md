{
  "hero": {
    "title": "Benutzerdefinierte Metriken einrichten"
  },
  "title": "Benutzerdefinierte Metriken einrichten",
  "summary": "Erfahre mehr über benutzerdefinierte Metriken und wie du sie bei Multi-Step API (MSA) Prüfobjekten einrichtest",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/einrichtung-von-custom-api-metrics",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/custom-api-metrics-setup",
  "sectionlist": true
}

Da APIs eine bedeutende Rolle im täglichen Geschäfts-, Plattform- und Servicebetrieb spielen, ist es wichtig, regelmäßig ihr Verhalten zu prüfen und eine Datenvalidierung durchzuführen. Hier erläutern wir, wie du **Benutzerdefinierte Metriken** nutzen kannst, um die Verfügbarkeit deiner API zu überwachen, API-Antwortdaten zu erfassen und diese Daten visuell in Echtzeit-Diagrammen oder als Liste zur Analyse darzustellen.

**Benutzerdefinierte Metriken** ist in [Multi-Step API (MSA)-Prüfobjekten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) verfügbar und ermöglicht dir, bestimmte numerischen Daten von jeder internen oder externen API zu erfassen.
Mit jedem erfassten Datenpunkt kannst du diese Werte in einer [benutzerdefinierten Metrikvariable]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="de" >}}) speichern, um den Fortschritt der Daten über einen Zeitraum visuell anzuzeigen.

## Welchen Nutzen haben benutzerdefinierte Metriken?

Nehmen wir an, wir haben eine API für ein E-Commerce-System, die Echtzeit-Informationen über einen Produktkatalog liefert. Darin sind Preise, Produktinventar und andere Produktdaten enthalten.

Beispielsweise möchten wir die Anzahl pro Produkt im Lagerbestand nachhalten. Statt die API jedes Mal manuell aufzurufen, erfassen benutzerdefinierte Metriken diese Daten automatisch aus der API-Antwort und speichern jeden Datenpunkt in [Variablen benutzerdefinierter Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="de" >}}):

![Benutzerdefinierte Metrikvariable für Produkte](/img/content/scr-custom-metrics-products.min.png)

Jedes Mal, wenn das MSA-Prüfobjekt ausgeführt wird, verfolgt es die Werte dieser Variablen. Dann kannst du damit eine [Liste benutzerdefinierte Metriken]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#custom-metrics-list-or-chart" lang="de" >}}) zur weiteren Daten- oder Trendanalyse erstellen oder deine Geschäftsberichte und die betriebliche Leistung überwachen:

![Benutzerdefinierte Metrikvariable](/img/content/scr-custom-metrics-product-graph.min.png)

Es gibt auch verschiedene Wege, um benutzerdefinierte Metriken in unterschiedlichen Kontexten zu verwenden:

- Bei DevOps kannst du den Status deines Systems oder einer Anwendung überwachen, indem du Metriken wie die Anzahl erfasster Fehler, gleichzeitiger Nutzer und Netzwerkgeschwindigkeit verfolgst.
- Im IT-Betrieb kannst du Umgebungsmetriken von Datenzentren wie Temperatur, Luftfeuchtigkeit und Systemstatus überwachen.
- Beim IT-Support kannst du die Anzahl an Supportanrufen verfolgen, die in der Warteschleife sind, die Anzahl an Tickets und die SLA-Performance.

## Benutzerdefinierte Metriken einrichten

Sobald du ein [MSA-Prüfobjekt eingerichtet hast]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) – mit einem Schritt oder mehreren Schrittdefinitionen –, kannst du **benutzerdefinierte Metriken** auf zwei Weisen spezifizieren: [Mit einer Variable setzen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#set-using-a-variable" lang="de" >}}) oder [Mit Skripting setzen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#set-using-script" lang="de" >}}).

Hinweis: Verwende bei der Erstellung einer neuen benutzerdefinierten Metrik einen Namen, der verständlich ist und der die Funktion in Kontext setzt. Der Metrikname und der Name des Prüfobjekts erscheinen in der Liste verfügbarer benutzerdefinierter Metriken, wenn du diese zu deinem Bericht über benutzerdefinierte API-Daten hinzufügst. Du kannst denselben Namen für benutzerdefinierte Metriken verwenden, um ähnliche Datentypen darzustellen, die zu unterschiedlichen Gruppen gehören. Beispielsweise kann eine benutzerdefinierte Metrik namens `totalSum` sowohl in produktspezifischen APIs als auch in kundenspezifischen APIs genutzt werden. Obwohl der Name derselbe ist, gehören die Daten, für die der Name steht, zu unterschiedlichen Gruppen. Uptrends empfiehlt, direkt die richtigen Namen zu vergeben. Späteres Umbenennen einer benutzerdefinierten Metrik wird als Erstellen einer neuen, anderen Metrik behandelt.

### Mit einer Variable setzen

Anhand dieser Methode kannst du API-Antwortdaten verfolgen und speichern, ohne Code oder ein Skript zu schreiben. Du kannst einfach einen Ausdruck in einer Variable definieren und einen Namen für die benutzerdefinierte Metrik vergeben, um diese Variable als benutzerdefinierte Metrik zu verwenden.

Als Beispiel richten wir eine **benutzerdefinierte Metrik** anhand der [Carbon API](https://api.carbonintensity.org.uk/intensity) ein. Um die Kohlenstoff-`intensity`-Daten anhand der Variablenmethode zu verfolgen:

{{< Support/storylane url="https://app.storylane.io/demo/1eztu52puc8s" >}}

### Mit Skripting setzen

Diese Method ermöglicht dir, deine eigenen [Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="de" >}}) zu schreiben. Damit hast du volle Kontrolle, wie du API-Antwortdaten erfasst und behandelst.

Stelle sicher, dass du [Schnipsel für Custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#custom-metrics" lang="de" >}}) nutzt und einen Namen für die benutzerdefinierte Metrik vergibst, um die Daten als benutzerdefinierte Metrik zu verwenden.

Als Beispiel richten wir eine **benutzerdefinierte Metrik** anhand der [Carbon API](https://api.carbonintensity.org.uk/intensity) ein. Um die Kohlenstoff-`forecast`-Daten anhand der Skripting-Methode zu verfolgen:

{{< Support/storylane url="https://app.storylane.io/demo/wwoetpfkky65" >}}

Um mehr über die Schnipsel und Skripting zu erfahren, lies [Multi-Step API (MSA) Benutzerdefinierte Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}}).

{{< callout >}} **Hinweis:** Innerhalb eines MSA-Prüfobjekts kannst du höchstens fünf [Variablen für benutzerdefinierte Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="de" >}}) festlegen. Um weitere hinzuzufügen, wende dich bitte an das [Support-Team](/contact), das dir weiterhilft. {{< /callout >}}

## Daten der benutzerdefinierten Metriken untersuchen

Untersuche nach der Einrichtung die Daten der benutzerdefinierten Metriken, um sicherzustellen, dass das Prüfobjekt die Daten richtig nachverfolgt und erfasst.

Um die Daten der benutzerdefinierten Metriken, die du überwachst, zu untersuchen:

1. Gehe zur {{< AppElement type="menuitem" >}} API-Prüfobjekteeinrichtung {{< /AppElement >}}.
2. Klicke auf den Link **Geh zu Dashboard** bei dem Prüfobjekt, bei dem du die **Benutzerdefinierte Metrik** erstellt hast.
3. Klicke in der Kachel **Prüfobjekt Protokoll** auf eine beliebige Zeile, um die **Kontrolldetails** zu öffnen.

Im Pop-up-Fenster siehst du die Daten der benutzerdefinierten Metriken, die vom Prüfobjekt abgerufen wurden. Beachte, dass der Wert `CarbonIntensity` 85 beträgt:

![Carbon-intensity-Daten der benutzerdefinierten Metriken](/img/content/scr-check-details-popup-carbon-intensity.min.png)

Du erhältst direkten Zugriff auf die einzelnen Werte der benutzerdefinierten Metrik, wie sie während der Ausführung des MSA-Prüfobjekts erfasst wurden.

### Fehlerbehebung

Solltest du keine Werte der benutzerdefinierten Metriken sehen, bedenke Folgendes:

- Hast du versehentlich die Check-Ergebnisse für einen älteren Check geöffnet, der ausgeführt wurde, bevor die neue benutzerdefinierte Metrik definiert wurde?

- Erfasst deine benutzerdefinierte Metrik numerische Ganzzahldaten? Enthält sie Textdaten oder Kommazahlen (wie etwa 99,9 % oder 3,1415 ), dann wird die benutzerdefinierte Metrik nicht erfasst. Derzeit werden nur Ganzzahlen unterstützt. 

- Wenn bei der Ausführung des MSA-Prüfobjekts ein Fehler aufgetreten ist, wurde die Variable, die deiner benutzerdefinierten Metrik zugewiesen wurde, möglicherweise gar nicht erst erstellt. Prüfe, ob es Tippfehler im Namen der benutzerdefinierten Metrik oder bei den Variablen gibt.

## Benutzerdefinierte Metriken in Dashboards anzeigen

Wenn du dir die Werte genauer ansehen willst und mit den zugrunde liegenden Daten arbeiten möchtest, um plötzliche Änderungen der Werte zu erkennen, kannst du die benutzerdefinierten Metriken in einem Dashboard mit **Liste oder Diagramm Benutzerdefinierte Metriken** anzeigen:

![Diagramm benutzerdefinierter Metriken](/img/content/scr-custom-metric-min-max-values.min.png)

Damit kannst du einen Trend bei der Metrikvariable darstellen, und Tiefst- Durchschnitts- und Höchstwerte anzeigen. Weitere Informationen findest du unter [Liste oder Diagramm Benutzerdefinierte Metriken]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#custom-metrics-list-or-chart" lang="de" >}}).

Du kannst die Daten auch als Liste/Diagramm benutzerdefinierter Metriken in unterschiedlichen Datenformaten über die
Funktion des [Exports von Dashboard-Daten]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="de" >}}) exportieren.
