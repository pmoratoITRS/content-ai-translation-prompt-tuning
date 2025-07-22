{
  "hero": {
    "title": "Fehlerbedingungen – Core Web Vitals"
  },
  "title": "Fehlerbedingungen – Core Web Vitals",
  "summary": "Einsatz von Schwellwerten bei Core Web Vitals, um Fehler auszulösen.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-core-web-vitals",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-core-web-vitals"
}

Google hat Core Web Vitals als eine Standardreihe von Messwerten definiert, um das Nutzererlebnis bei einer Webseite zu messen.

Bei Uptrends messen und berichten Prüfobjekttypen mit dem [Browsertyp mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) die [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}). Da diese Messwerte verfügbar sind, sollten wir sie uns näher ansehen und sie zur Anzeige von Fehlern nutzen, wenn bestimmte Schwellen erreicht werden. Daher sind Bedingungen für Core Web Vitals Teil der [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}).

Beachte, dass verschiedene Prüfobjekttypen unterschiedliche Fehlerbedingungen beinhalten. Sieh dir die Tabelle der [verfügbaren Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) an, um herauszufinden, welche Optionen für bestimmte Prüfobjekttypen möglich sind.

Die Fehlerbedingungen, die sich auf Core Web Vitals beziehen, werden unten erläutert.

## Verwende aktuell empfohlene Core Web Vitals {id="use-current-recommended-core-web-vitals"}

Google beschreibt den Performance-Status deiner Website anhand dreier Status: gut, zu optimieren und schlecht.
Mit Uptrends kannst du einen Fehler anzeigen, sobald der Status „zu optimieren“ gemeldet wird. Uptrends verwendet die Benchmark-Werte, die Google definiert hat. Diese sind aktuell:

**First Contentful Paint:** 1,8 Sekunden  
**Largest Contentful Paint:** 2,5 Sekunden  
**Time to Interactive:** 3,8 Sekunden  
**Cumulative Layout Shift:** 0,1  
**Total Blocking Time:** 0,2 Sekunden (200 ms)  

Verwendest du die Fehlerbedingung *Nutze die empfohlenen Core Web Vitals*, wird ein Fehler ausgelöst, wenn der letzte der Benchmark-Werte überschritten wird.

Du kannst eine Kombination aus *Nutze die empfohlenen Core Web Vitals*- und den einzelnen Core Web Vitals-Fehlerbedingungen verwenden. In diesem Fall werden deine eigenen Einstellungen die empfohlenen überschreiben.

## Maximaler Wert für Time to First Contentful Paint (FCP)

Nutze diese Fehlerbedingung, um einen Höchstwert einzugeben, wie lang es dauern darf, bis der Browser Teile der Seite anzeigt, die der Nutzer zu Anfang sieht. Erhält der Nutzer kein rechtzeitiges visuelles Feedback des Ladens der Seite, kann sich das auf das Nutzererlebnis im Zusammenhang mit der Interaktion mit deiner Website auswirken.

## Maximaler Wert für Time to Largest Contentful Paint (LCP)

Mit dieser Fehlerbedingung gibst du einen Höchstwert an, wie lange es dauern darf, bis der Browser den Hauptinhalt der Seite anzeigt. Muss der Nutzer länger als erwartet auf den Großteil des Inhalts warten, kann sich das auf sein Erlebnis auswirken.

## Maximaler Wert für Time to Interactive (TTI):

Verwende dies zur Angabe eines Höchstwerts, wie lang es dauern darf, bis die Seite auf Nutzerinteraktionen reagiert. Dauert es zu lange, muss der Nutzer auf das Laden der Seite warten, bevor diese schließlich auf die Eingabe des Nutzers reagiert.

## Maximaler Cumulative Layout Shift (CLS) Wert:

Der Wert Cumulative Layout Shift (CLS) misst die visuelle Stabilität, indem er prüft, ob es zu unerwarteten Verschiebungen von Seitenobjekten beim Laden der Seite kommt. Nutze diese Fehlerbedingung, um sicherzustellen, dass es nicht zu Störungen kommt, weil Teile auf der Seite sich aufgrund späten/asynchronen Ladens von beispielsweise Videos bewegen.

## Maximale Total Blocking Time (TBT):

Lege diese Fehlerbedingung fest, um einen Höchstwert anzugeben, wie lang der Browser vom Laden der Seite zurückgehalten werden darf, wenn auf verfügbare Verbindungen, das Ausführen von Skripten oder Rendering gewartet werden muss. Muss der Nutzer auf das Interagieren mit der Seite warten, weil der Browser sie zu lang blockiert hat, wirkt sich das auf das Erlebnis des Nutzers mit deiner Website aus.
