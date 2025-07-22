{
  "hero": {
    "title": "Core Web Vitals"
  },
  "title": "Core Web Vitals",
  "summary": "Beschreibung der Core Web Vitals-Werte wie in den Wasserfalldiagrammen beim Full Pagecheck und beim Transaktions-Monitoring angezeigt",
  "url": "/support/kb/synthetic-monitoring/monitoring-ergebnisse/core-web-vitals",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/core-web-vitals"
}


Basierend auf einer Google-Initiative, die Kommunikation über Website-Optimierung zu vereinfachen, sind **Core Web Vitals** eine Reihe wichtiger Messwerte, um die Leistung (Performance) einer Website festzustellen. Diese Messwerte spiegeln unterschiedliche Aspekte der Nutzererfahrung beim Besuch einer Website wider, so etwa die Ladezeit und die visuelle Stabilität. Schlechte Werte bei diesen Messungen können sich direkt auf das Ranking bei der Suchmaschine auswirken. Es ist also sehr wichtig, diese Zahlen zu verfolgen und somit sicherzustellen, dass deine Website richtig optimiert ist und es auch bleibt. 

Uptrends' Prüfobjekttypen [Full Pagecheck (FPC)](/support/kb/synthetic-monitoring/browser-monitoring) und [Transaktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="de" >}}) bieten die Option, eine Reihe an Core Web Vital-Werten (neben einigen zusätzlichen Daten) anzuzeigen. Dieser Artikel gibt einen Überblick der dargestellten Messwerte und was sie genau bedeuten. 

## Messwerte

Uptrends zeigt die folgenden Core Web Vitals (und zugehörige Werte) an:

![Core Web Vitals in Uptrends](/img/content/scr-inp-in-cwv.min.png)

- **First Contentful Paint (FCP):** Der FCP misst, wie lang es dauerte, bis der Browser den ersten Inhalt auf der Seite angezeigt hat.
- **Largest Contentful Paint (LCP):** Der LCP misst die Zeitspanne bis zur Anzeige des größten einzelnen Elements (Bild oder Textblock) auf der Seite. Es ist der Punkt im Zeitstrahl der Seitenladezeit, an dem der Hauptinhalt (oder größte Teil) der Seite begonnen hat zu laden. Der LCP und der FCP können gleich sein, wenn das größte Element das erste ist, das geladen wird.
- **Time to Interactive (TTI):** Der TTI zeigt die Zeitspanne zwischen dem Beginn des Ladens und dem Zeitpunkt, an dem die Seite verlässlich auf eine Aktion des Nutzers antworten kann. Daher ist es eine gute Möglichkeit, festzustellen, wie lange der Nutzer tatsächlich auf das Laden der Seite warten muss. Die Bestimmung des TTI ist erforderlich, um die Total Blocking Time zu berechnen. 
- **Total Blocking Time (TBT):** TBT misst die Zeit, in der der Haupt-Thread des Browsers blockiert ist. Es berücksichtigt die Zeit, in der der Browser mehr als 50 Millisekunden (ms) lang einen Task verarbeitet, wodurch die Seite langsam reagiert und Nutzerinteraktionen blockiert. Für jeden langen Task wird nur der Teil für die TBT gezählt, der über die ersten 50 ms hinausgeht. Tasks die 50 ms oder weniger dauern, werden in diesem Wert nicht erfasst.
- **Cumulative Layout Shift (CLS):** Die CLS gehört zu den letzten bestimmten Werten, nachdem die Seite komplett geladen wurde. Der Wert gibt die Messung von Layoutverschiebungen wieder (sichtbare Elemente bewegen sich unerwartet von einer Stelle an eine andere), nachdem die Seite bereit für Nutzerinteraktionen war, und gibt einen Hinweis auf die visuelle Stabilität.  
- **Interaction to Next Paint (INP):** Der Wert INP ist ein Hinweis auf die allgemeine Reaktionsfähigkeit der Seite auf Nutzerinteraktionen. Es misst die Zeit zwischen einem Klick oder eine Tasteninteraktion mit der Seite und jedem sichtbaren Feedback. Da es eine Seiteninteraktion nach dem ursprünglichen Laden der Seite erfordert, ist INP *nur für Transaktionsprüfobjekte verfügbar*.

## Dashboard-Berichte

Du kannst alle Metriken in einem benutzerdefinierten Dashboard anzeigen. Füge einfach eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="de" >}}) hinzu. Klicke dann auf die Schaltfläche für die Kacheleinstellungen {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} an der Kachel und wähle die gewünschten Werte durch Markieren der Kontrollkästchen. 

Du kannst die Core Web Vitals von Transaktionen für jeden einzelnen Schritt anzeigen. Dazu musst du die Optionen *Wasserfall Grafik* und *Leistungsmetriken* für jeden Schritt aktivieren, den du in der Grafik sehen möchtest. Weitere Information hierzu findest du unter [Schritt-Einstellungen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="de" >}}). 

![Screenshot Einstellungsdetails Kachel](/img/content/scr_simple-data-metrics.min.png)

## Core Web Vitals bei Transaktionsprüfobjekten

Ein [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}) eines [Transaktionsprüfobjekts]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}) zeigt die Core Web Vitals und [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}). Uptrends zeigt die Metriken für alle angegebenen Navigationen in einem Schritt. 

![Screenshot mehrfache Navigationen bei einem Transaktionsschritt](/img/content/scr-cl-transaction-waterfall.min.png)