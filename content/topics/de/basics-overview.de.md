{
  "hero": {
    "title": "Grundlagenübersicht"
  },
  "title": "Grundlagenübersicht",
  "summary": "Ist Uptrends komplett neu für dich? Lies diese Artikel, um eine Einführung und ein grundlegendes Verständnis dessen zu erhalten, wie die Uptrends Anwendung dir nutzen kann.",
  "url": "/support/kb/basics/grundlagenuebersicht",
  "translationKey": "https://www.uptrends.com/support/kb/basics/basics-overview",
  "sectionlist": false
}

Uptrends ist ein SaaS (Software as a Service) Digital Experience Monitoring Tool, das seinen Nutzern detaillierte Einsichten in die Verfügbarkeit und Performance ihrer Websites und -services aus der Endnutzer-Perspektive bietet. Uptrends lässt sich einfach konfigurieren und unterstützt eine große Breite an [Monitoring-Typen]({{< ref path="/support/kb/basics/monitor-types" lang="de" >}}) für jedes Überwachungsszenario sowie auch das [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="de" >}}).

## Synthetic Monitoring

Beim proaktiven [Synthetic Monitoring]({{< ref path="/products/synthetics/synthetic-monitoring" lang="de" >}}) nutzt Uptrends sein weltweites [Netzwerk an Checkpoints]({{< ref path="/checkpoints" lang="de" >}}), um deine Websites und Prozesse rund um die Uhr auf Verfügbarkeit und Performance zu prüfen – von Standorten, die für dein Unternehmen von Bedeutung sind. Verschiedene Prüfobjekttypen bilden jeden deiner möglichen Einsatzfälle ab.

{{< Support/storylane url="https://app.storylane.io/demo/tqewkqp0c4ly" >}}

### Uptime Monitoring {id="synthetic-monitoring"}

[Uptime Monitoring]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring" lang="de" >}}) ist ein Hoch-Frequenz-Monitoring der Verfügbarkeit deiner Websites und -services. Prüfobjekte wie der [HTTPS-Prüfobjekttyp]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https" lang="de" >}}) prüfen deine Website auf Verfügbarkeit und richtiges Funktionieren, so häufig wie jede Minute und von überall auf der Welt.

![Ein Protokoll eines Basic-Prüfobjekts](/img/content/scr-basics-uptimelog_020224.min.png)

Es gibt weitere Basic-Prüfobjekttypen wie das [DNS-Prüfobjekt]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="de" >}}), bei dem die Korrektheit deiner DNS-Einrichtung geprüft wird, in dem eine Anfrage an einen DNS-Server gesendet wird, und das [Prüfobjekt für SSL-Zertifikate]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="de" >}}), um die Gültigkeit deiner SSL-Zertifikate zu bestätigen und Warnmeldungen zu senden, wenn sie nicht mehr korrekt sind oder demnächst ablaufen.

### Browser Monitoring {id="browser-monitors"}

Anders als beim Uptime Monitoring wird beim [Browser Monitoring]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) ein tatsächlicher Browser verwendet, um deine Websites aufzurufen. Auf diese Weise kann der Prüfobjekttyp Full Pagecheck (FPC) deine Seite vollständig laden, genauso wie es die Endnutzer machen, und du erhältst eine große Menge detaillierter Performance-Messwerte.

Diese Messwerte umfassen ein [Wasserfalldiagramm]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}) (eine detaillierte Aufschlüsselung technischer Daten und Performance-Metriken, die das Laden einer Seite ausmachen, für jedes einzelne Objekt), aber auch Schlüsselwerte wie die [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}) und [W3C Navigation Timings]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}), die sich auf das Kundenerlebnis oder auf Suchmaschinen-Rankings auswirken.

![Beispiel Full Pagecheck-Ergebnisse](/img/content/scr-fpc-result-basics.min.png)

### Transaktions- / Web Application Monitoring {id="transaction-monitoring"}

Ein [Transaktionsprüfobjekt (oder Web Application-Prüfobjekt)]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="de" >}}) lädt deine Seite in einen tatsächlichen Browser und führt dann ein Skript aus, um mit der Seite zu agieren. Dabei werden die Aktionen eines echten Nutzers imitiert. Dieser Prüfobjekttyp kann verwendet werden, um komplette User Journeys, also Pfade eines Nutzers, auf deiner Website zu testen, beispielsweise Anmeldung, Shop-Funktionen mit Suche nach Produkten, Hinzufügen zum Warenkorb und Bezahlen sowie Ausfüllen von Formularen usw.

Ein typischer Nutzerablauf, bei dem der Nutzer mit deiner Website in mehreren Schritten interagiert, um eine bestimmte Aktion auszuführen, betrifft mehrere Webserver, Datenbanken, APIs oder externe Ressourcen. Transaktions-Monitoring ist der beste Weg zu prüfen, dass alle Aspekte deiner wichtigen Nutzeraktionen korrekt funktionieren. Es ist leicht, dies auch on Programmierkenntnisse einzurichten, wenn du das [Transaktionsrekorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}})-Plug-in für Chrome verwendest.

![Der Schritteditor für Transaktionen](/img/content/scr-transaction-steps-basics_020224.min.png)

#### API-Monitoring

Der [Multi-Step API (MSA)Prüfobjekttyp]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring" lang="de" >}}) macht für Backend/APIs, was das Transaktions-Monitoring für Frontend/User Journeys macht. APIs ermöglichen die Kommunikation zwischen Anwendungen und sind das Rückgrat des modernen Internets.

Dein Unternehmen verlässt sich auf die eine oder andere Art mit Sicherheit auf mehrere APIs, aber das Erkennen möglicher Probleme, die eventuell auftreten, kann schwierig sein, da API-Kommunikation und Interaktionen im Hintergrund ablaufen. Mit dem Multi-Step API Monitoring kannst du deine APIs direkt prüfen, indem du Aufrufe erzeugst und die Antworten auf Richtigkeit, Vollständigkeit und Zeitnähe testest.

## Real User Monitoring

Neben dem Synthetic Monitoring bietet Uptrends ein [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="de" >}}). RUM verwendet ein einfaches Skript, dass im HTML deiner Seite eingebettet ist, um tatsächliche Performance-Daten deiner Endnutzer in Echtzeit zu erfassen. In Ergänzung zu den Synthetic Monitoring-Daten kann RUM dir Einblicke in das Erlebnis deiner tatsächlichen Nutzer geben, ungeachtet davon, wo sie sich befinden. Es liefert dir Informationen zu den Einrichtungen deiner Nutzer in Bezug auf die von ihnen benutzten Browser und Betriebssysteme.

![Ein Beispiel für RUM-Daten](/img/content/scr-rum-map-basics_020224.min.png)

## Alarme

Uptrends’ Monitoring umfasst ein leistungsstarkes und vielseitiges [Alarmierungssystem]({{< ref path="/support/kb/alerting" lang="de" >}}). Lege fest, wann Alarme erzeugt und Benachrichtigungen gesendet werden – durch Einrichten von [Meldedefinitionen]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="de" >}}). Verwende unsere schlüsselfertigen [Integrationen]({{< ref path="/support/kb/alerting/integrations/what-are-integrations" lang="de" >}}), um Warnmeldungen per E-Mail, SMS oder Telefonanruf zu erhalten oder um sie an eine externe Plattform zu senden. Richte alternativ eine [benutzerdefinierte Integration]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="de" >}}) ein, um eine Verbindung von Uptrends Alarmen zu jeder beliebigen externen Plattform herzustellen, auch solchen, die nicht auf der Integrationenseite gelistet sind.
