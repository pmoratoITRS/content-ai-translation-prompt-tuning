{
  "hero": {
    "title": "Transaktions-Monitoring verstehen"
  },
  "title": "Transaktions-Monitoring verstehen",
  "summary": "In diesem Artikel erfährst du, was das Transaktions-Monitoring (auch bekannt als Web Application Monitoring) ist, wie es funktioniert und welche Arten von Transaktionen du überwachen kannst. ",
  "url": "/support/kb/synthetic-monitoring/transaktionen/web-application-monitoring-verstehen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-web-application-monitoring"
}

Was ist das Transaktions-Monitoring, auch Web Application Monitoring genannt? Eine detaillierte Beschreibung findest du unter [Web Application Monitoring]({{< ref path="what-is/web-application-monitoring" lang="de" >}}). Aber kurz gefasst:

*Web Application Monitoring ist ein synthetische Prüfobjekt oder ein Bot, bei dem Nutzeraktionen auf einer Website oder bei einer Webanwendung in regelmäßigen Intervallen ausgeführt werden. Das Prüfobjekt verwendet einen Webbrowser (wie deine Nutzer), um zu verifizieren, dass die Website oder Anwendung korrekt funktioniert und eine gute Performance zeigt.*

Jede Transaktion also, die ein Nutzer auf deiner Website über einen Browser vornehmen kann, kann ein Transaktionsprüfobjekt in regelmäßigen Intervallen ebenfalls ausführen. Das Transaktions-Monitoring prüft deine Website rund um die Uhr, sieben Tage in der Woche. Wenn die Transaktion einen Fehler meldet oder zu lange dauert, warnt dich das Alarmierungssystem von Uptrends.

## Warum Webanwendung überwachen? {id="why-monitor-your-web-applications"}

Warum solltest du Transaktionen überwachen? Schließlich würdest du bemerken, wenn etwas nicht läuft. Klar, irgendwann bemerkst du den Fehler, aber welchen Schaden hat bis dahin dann das Vertrauen deiner Nutzer und dein Ruf genommen?

### Die hohen Kosten langsamer und fehlerhafter Webanwendungen

Sollten deine Website oder dein Service nicht richtig funktionieren, werden deine Nutzer einfach zur Konkurrenz wechseln.  Und sie wechseln nicht nur zur Konkurrenz, viele von ihnen kehren nie wieder zu dir zurück.

Fehler in Webanwendungen kosten dich später mehr Einnahmen, als sie es zum Zeitpunkt der Störung tun. Denn wie vertrauensvoll würdest du deine persönlichen Daten einer Marke überlassen, wenn ihre Anwendung langsam und fehlerhaft ist?

Indem du deine Transaktionen mit dem Transaktions-Monitoring überwachst, erfährst du sofort, wenn ein Problem auftritt. Du kannst Probleme direkt beheben, bevor sie sich auf deine Nutzer auswirken.

### Es kann mehr daneben gehen, als du denkst

Einige Unternehmen prüfen ihre Transaktionen sporadisch während des Arbeitstages. Was aber passiert in der Nacht, wenn die Mitarbeiter zu Hause sind? Die Spitzen-Traffic-Zeiten mögen vielleicht vorbei sein, aber sollte deine Anwendung nicht auch zu den weniger starkbesuchten Zeiten funktionieren? Dein Arbeitstag mag beendet sein, aber die Website ist rund um die Uhr in Betrieb. Es können viele unterschiedliche Dinge schiefgehen, die dir eventuell nicht auffallen, wenn du sie nicht 24/7 überwachst. Wenn du deine Transaktionen 24 Stunden am Tag überprüfst, wirst du möglicherweise auf folgende Probleme aufmerksam gemacht:

- Langsam ladende Seiten und Transaktionen aufgrund von Inventaraktualisierung am frühen Morgen oder aufgrund anderer Backend-Prozesse. Prozesse, die zu Zeiten ablaufen, von denen du denkst, dass deine Nutzer sie nicht bemerken (was sie aber trotzdem tun).
- Prozesse abhängig von externen Systemen, die nicht korrekt funktionieren:
  -   **Unternehmenseigentümer**: Aktualisierungen des Produktbestands, Preisberechnungen und Bestellsysteme
  -   **Systemintegrationen**: Externe Zahlungsabwickler, Standortdienste, SharePoint-/Office365-Integrationen und externe Berechnungsmodule
  -   **E-Commerce- und Web-Analyse**: Nutzerverhalten-Tracker, Google Analytics und Werbeanzeigensysteme

    Obwohl diese von externen Systemen abhängigen Prozesse wie Add-ons erscheinen, können sich Ausfallzeiten, langsame Performance oder ein schlechtes Verhalten des externen Systems auf deine Gesamt-Performance auswirken und Anzeige und Verhalten deiner eigenen Seiten stören.

## Welche Arten von Transaktionen werden überwacht?

Die Frage sollte eigentlich lauten „Welche Transaktionen kann ich nicht mit dem Transaktions-Monitoring überwachen?". Dies sind einige Beispiele von Transaktionen, deren Performance und Funktionstüchtigkeit du eventuell überwachen solltest.

- Erfolgreiche Logins
- Verwendung der Suchfunktion deiner Website
- Nutzung der Kalenderfunktion in einem Reservierungssystem
- Warenkorbfunktionen: Hinzufügen, Entfernen und Auswahl von Produktvarianten
- Formulare ausfüllen, beispielsweise Bestellformulare, die mit anderen Services wie Adressenverifizierung oder Versandkostenberechnung verknüpft sind
- Erfolgreiche Finanztransaktionen: Verbindung zu Händlerservices, Validierung der Nutzereingabe und Empfang gültiger Server-Antworten

## Auswahl der erforderlichen Transaktionen für ein Monitoring

Deine Website verfügt wahrscheinlich über viele Nutzerszenarien. Du kannst nicht jedes Szenario testen, wie also triffst du die beste Wahl? Natürlich solltest du solche Transaktionen testen, die für den Erfolg deiner Website wichtig sind und auf die sich deine Nutzer verlassen (viele haben wir bereits oben genannt). Wähle zudem Transaktionen, die sich auf viele unterschiedliche Systeme und Services stützen, um richtig zu funktionieren und eine gute Performance zu bieten. Wähle Transaktionen, die viele Teile deiner Systeme ansteuern, um Folgendes zu verifizieren:

- Verfügbarkeit und Antwortzeiten unterstützender Server
- Datenbankzugriff und -antworten: Gibt es mehr als eine Datenbank, wähle Transaktionen, die jede ansprechen. Beispiele sind etwa eine Nutzerdatenbank, die Produktdatenbank, Bestellbeschaffung, Nutzerdaten und jede andere Datenbank, auf die sich dein System stützt
- Verfügbarkeit und Funktion externer Services: zum Beispiel Orts- und Adressverifizierung, Postleitzahlsuche, Bestandsmanagementsysteme, Logistik, Händlerservices oder CRM-Systeme

## Mit welchen Daten testen?

Bei der Wahl, mit welchen Daten geprüft wird, solltest du Testdaten einsetzen. Zum Beispiel bei einer E-Commerce-Website solltest du Produkt-IDs verwenden, die nicht mit tatsächlichen Produkten des Inventars verknüpft sind, um unerwünschte Folgen zu vermeiden. Wir haben einen Artikel zu den Fallen, die bei der Überwachung deiner Website und Services zu berücksichtigen sind. Einige der Probleme sind direkt auf die Daten zurückzuführen, die du für das Testen auswählst. Lies hierzu den Artikel [Vorbehalte, Tipps und Tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}}), um weitere Infos zu möglichen Problemen und ihre Lösung zu erhalten. Es gibt jedoch einige datenspezifische Probleme, die du bedenken solltest.

### E-Commerce
Bedenke bei der Wahl von Produkten fürs Testen, dass das Prüfobjekt einen Fehler meldet, wenn das Produkt nicht mehr verfügbar ist.

- Dein Prüfobjekt erzeugt möglicherweise Bestellungen, die den verfügbaren Bestand aufbrauchen. Die aus den Tests hervorgehenden Bestellungen verhindern möglicherweise, dass Nutzer das Produkt kaufen, da es nicht mehr verfügbar zu sein scheint.
- Bestellungen aufgrund von Tests lösen möglicherweise Nachbestellungen bei deinem Lieferanten über ein automatisches Bestellsystem aus.
- Der Test erzeugt eventuell Pick-Zettel und Versandetiketten, aufgrund derer die Versandabteilung möglicherweise veranlasst wird, die im Test bestellten Produkte zu verpacken und zu versenden.
- Bestellbestätigungs-E-Mails werden eventuell ausgesendet und überfüllen jemandes Postfach, vielleicht sogar dein eigenes.
- Das Testen von Zahlungssystemen verbraucht möglicherweise verfügbare Guthaben und erzeugt echte Gebühren.

### Reservierungssysteme
Reservierungssysteme und ähnliche Lösungen haben ihre eigenen Herausforderungen.

- Dein Prüfobjekt bucht eventuell alle verfügbaren Termine und verhindert, dass echte Nutzer Termine wahrnehmen können.
- E-Mail-Bestätigungen überfüllen Postfächer.
- Bezahlte Reservierungen erzeugen Kreditkarten- und Service-Gebühren.

### Anmeldedaten

Anmeldedaten sollten sicher verwahrt werden. Es sollten keine Duplikate aufgrund automatisierter Anmeldedaten erzeugt werden. Beachte diese Empfehlungen:

- Wähle Anmeldedaten sorgfältig aus.
- Beschränke die [Berechtigungen]({{< ref path="support/kb/account/permissions" lang="de" >}}) des Test-Nutzers und überwache den Account stets in Bezug auf ungewöhnliche Aktivitäten.
- Schütze Anmeldedaten mit der Uptrends [Vault]({{< ref path="support/kb/account/vault" lang="de" >}}).
- Melde den Nutzer am Ende einer Transaktion ab, um Anmeldefehler zu vermeiden, wenn derselbe Nutzer beim nächsten Test versucht, sich anzumelden.

### Analyse und Real User Monitoring

Dein Monitoring wirkt sich auf deine Webanalyse- und Real User Monitoring-Daten aus. Dies kann durch Einsatz der [Blockierung von URL und Analytics]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="de" >}}) vermieden werden.

## Ist ein Transaktionsprüfobjekt immer die beste Wahl? {id="transaction-best-choice"}

Ein Transaktionsprüfobjekt ist toll, wenn es darum geht, sicherzustellen, dass alles funktioniert und das von dir erwartete Ergebnis liefert. Andere Prüfobjekttypen liefern dir jedoch mehr Informationen zur Performance insgesamt und Verfügbarkeit deiner Website oder Webservices.

### Website-Verfügbarkeit 

Transaktionsprüfobjekte prüfen deine Website nur in Fünf-Minuten-Intervallen oder länger. Das heißt es kann zwischen den Prüfungen zu sehr viel Ausfallzeiten kommen. Mit Verfügbarkeitsprüfobjekten kannst du die Verfügbarkeit von Webseiten und Webservices mit kürzeren Intervallen testen. Du hast auch die Möglichkeit, [erweiterte Verfügbarkeitsprüfobjekte]({{< ref path="/products/synthetics/advanced-availability-monitoring" lang="de" >}}) für Datenbanken, E-Mail-Server, FTP-/SFTP–Server, SSL-Zertifikate und DNS-Antworten einzusetzen.

### Website-Performance

Das Transaktions-Monitoring erfasst Seitenladezeiten und nach Wunsch kannst du Wasserfallberichte hinzufügen, um zusätzliche Ladezeitdaten zu erhalten. Jedoch berücksichtigt das Performance Monitoring in Hinblick auf deine Transaktionen mehr die Reaktionsfähigkeit deiner Server auf Nutzerinteraktionen wie etwa das Klicken von Schaltflächen. Das [Web Performance Monitoring]({{< ref path="products/synthetics/web-performance-monitoring" lang="de" >}}) bietet dir detailliertere Daten zur Seiten-Performance von der ersten Anfrage bis zum vollständigen Laden der Seite. Ein Prüfobjekt des Typs [Full Pagecheck]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) liefert detaillierte Informationen zu den Ladezeiten einer einzelnen Seite. Du siehst den Ladevorgang und die Performance für die gesamte Seite und für jedes Element. Du bekommst nicht nur mehr Details zu jedem Check. Uptrends hat auch die Performance-Dashboards zur Anzeige der Ladezeitdaten einzelner Seiten optimiert, um eine größere Vergleichbarkeit zu ermöglichen.

### API-Monitoring

Deine Transaktion verfügt wahrscheinlich über mehrere API-Abfragen. Während einige Abfragen Einzelabfragen sind, erfordern andere mehrere Abfragen, um die ganze Transaktion auszuführen. Wenn du die APIs separat von deinen Transaktionen mit einem [API Monitoring]({{< ref path="products/synthetics/api-monitoring" lang="de" >}}) überwachst, kann dies API-Probleme schneller aufdecken. Du erhältst zudem mehr Daten für die Ursachenanalyse, wenn deine Transaktion fehlschlägt.

Um die Verfügbarkeit deiner Webservices zu prüfen, verwende die Prüfobjekttypen Webservice HTTP oder Webservice HTTPS. Diese testen die API-Verfügbarkeit jede Minute des Tages. Du kannst SLA-Vorgaben, die mit der API verknüpft sind, verfolgen und auf Verfügbarkeitsprobleme schneller reagieren als mit einem Transaktions-Monitoring.

Das Prüfobjekt für eine Reihe aufeinanderfolgender Schritte wird anhand des [Multi-step API-Prüfobjekttyps (MSA-Prüfobjekt)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) definiert. Dieser Prüfobjekttyp verifiziert Antworten und Performance für gesamte API-Interaktionen (gleich ob sie eine Antwort oder mehrere umfassen). Du erhältst detaillierte Informationen über API-Antworten mit Validierung.

Das Web Application Monitoring konzentriert sich auf die komplette Interaktion zwischen einem Nutzer und einer Anwendung, während sich das Multi-step API Monitoring auf jede API-Interaktion konzentriert, die über die Webanwendung hinausgeht. Zum Beispiel solltest du eventuell ein Multi-step API-Prüfobjekt einsetzen, um die Kommunikation zwischen einem Sicherheitssystem und dem Dienstanbieter zu testen oder um Transaktionen mit dem Zahlungsanbieter für Kreditkarten zu überwachen.

## Muss ich Entwickler sein, um Transaktionsprüfobjekte einzurichten?{id="programming-skills"}

Es wäre von Vorteil, aber eine Kenntnis, wie deine Apps und Services funktionieren, helfen dir enorm weiter, selbst wenn du kein Entwickler bist. Lies unseren Artikel [Optionen für Transaktionsskripte]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="de" >}}), um mehr über denSelf-Service, Full-Service oder das Programmieren von Transaktionen zu erfahren. Deine Entwickler oder dein DevOps-Team muss eventuell:

- Skripte für Mirror-Sites in mehreren Sprachen oder für ähnliche Arbeitsabläufe und Funktionen duplizieren und anpassen;
- Skripte für bevorstehende Website-Updates zur gleichzeitigen Ausbringung des Update-Plans anpassen, der von deinem System zur kontinuierlichen Integration/Auslieferung (continuous integration/continuous deployment,CI/CD) ausgelöst wird;
- die Uptrends API nutzen, um deine Monitoring-Einrichtung als wertvolles Asset in deinem Qualitätssicherungssystem einzusetzen.
