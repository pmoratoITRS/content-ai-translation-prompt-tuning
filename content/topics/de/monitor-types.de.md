{
  "hero": {
    "title": "Prüfobjekttypen"
  },
  "title": "Prüfobjekttypen",
  "summary": "Ein Überblick aller Prüfobjekttypen bei Uptrends – von einfacher Verfügbarkeit bis komplexe Transaktionen.",
  "url": "/support/kb/basics/pruefobjekttypen",
  "translationKey": "https://www.uptrends.com/support/kb/basics/monitor-types"
}

Uptrends bietet eine große Bandbreite an Prüfobjekttypen, die jeweils bestimmte Überwachungsanforderungen erfüllen. Jedes Synthetic-Prüfobjekt verwendet [Credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="de" >}}), anhand derer der Preis für unterschiedliche Monitoring-Services berechnet wird.

Dieser Artikel bietet einen Überblick darüber, wie jeder Prüfobjekttyp die Performance deiner Websites überwacht.

{{< callout >}} **Hinweis:** Du kannst mehrere Prüfobjekttypen neben dem [Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="de" >}}) nutzen, um die tatsächliche Performance deiner Website auf Grundlage der Nutzererfahrung in ihrem eigenen Netzwerk, tatsächlicher Browser und anderer Aktivitäten zu messen. {{< /callout >}}

## Uptime-Prüfobjekte (Basic-Prüfungen)

Ein Uptime-Prüfobjekt führt grundlegende Prüfungen deiner Websites durch. Es prüft auf Verfügbarkeit der Website und erwartet eine Antwort mit Statuscode 200. Dieses Prüfobjekt erfasst nur die erste Antwort deiner Website und schaut sich nicht komplett die Seitenelemente oder andere bestimmte Website-Komponenten an. 

Ein Uptime-Prüfobjekt prüft bis zu einmal pro Minute. Es liefert einen genaueren Bericht zur Verfügbarkeit der Seite als ein Prüfobjekt für Browser- oder Full Pagecheck.

### Arten von Uptime-Prüfobjekten

Die verschiedenen Arten von Uptime-Prüfobjekten umfassen:

- Webseiten-Prüfungen – **HTTP**- und **HTTPS*-Prüfobjekte* (es wird empfohlen, HTTPS zu nutzen)
- Fortgeschrittene Checks – **DNS**-, **SSL-Zertifikats**-, **SFTP**- und **FTP**-Prüfobjekte
- Mailserver – **SMTP**-, **POP3**- und **IMAP**-Prüfobjekte
- Datenbankserver – **Microsoft SQL-Server**- und **MySQL**-Prüfobjekte
- Netzwerk-Checks – **Ping**- und **Connect**-Prüfobjekte

{{< callout >}} **Hinweis:** Der Prüfobjekttyp **HTTP** ist für neue Nutzer nicht mehr verfügbar. Uptrends hat die Funktionen des **HTTPS**-Prüfobjekttyps erweitert, sodass auf Verfügbarkeit von HTTP-Websites geprüft werden kann. {{< /callout >}}

Weitere Informationen zu den verschiedenen Uptime-Prüfobjekten findest du unter [Uptime Monitoring]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}).

## Browser-Prüfobjekte (Full Pagecheck)

Ein Browser-Prüfobjekt, auch als Full Pagecheck (FPC) oder Real Browser-Prüfobjekt bekannt, prüft die Lade-Performance deiner Webseite für jedes einzelne Element. Dieses Prüfobjekt ruft einen tatsächlichen (realen) Browser auf, um zu simulieren, was Nutzer bei Besuch der Website sehen.

Es untersucht, wie deine Website von Anfang bis Ende lädt, und berücksichtigt dabei, wie sich jedes Seitenelement (wie Skripte, CSS-Dateien, Bilder und Inhalte von Fremdanbietern) verhalten. Browser-Prüfobjekte liefern zudem Informationen zu den Website-Metriken [Core Web Vitals]({{< ref path="" lang="de" >}}) und [W3C Navigation Timings]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}) sowie [Wasserfalldiagramme]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}).

Diese Prüfobjekte werden bis zu einmal alle 5 Minuten ausgeführt und geben dir Hinweise zu Verfügbarkeit, aber mit weniger Genauigkeit als ein Uptime-Prüfobjekt. Weitere Informationen zu den Unterschieden zwischen Basic Checks und Real Browser Checks findest du unter [Einfacher Webseiten-Check im Vergleich zum Real Browser Check]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="de" >}}). Du findest auch weitere Informationen unter [Browser Monitoring]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}).

## API-Prüfobjekte

Ein API-Prüfobjekt ist ein leistungsstarkes Prüfobjekt, das Prüfungen mit einschrittigen API-Abfragen oder aber mehrschrittigen API-Abfragen durchführt. Dieses Prüfobjekt ist eine (benutzeroberflächenbasierte) Lösung, die kein Schreiben von Code erfordert, aber auch [benutzerdefinierte Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}}) nutzt, um HTTP-Anfragen und -Antworten zu testen und deine Monitoring-Anforderungen zu berücksichtigen.

Du kannst eigene Skripte oder [benutzerdefinierte Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="de" >}}) hinzufügen, [benutzerdefinierte Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}) definieren, [Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="de" >}}) einsetzen und weitere Funktionen in Bezug auf die API prüfen.  

### Arten von API-Prüfobjekten

Die verschiedenen Arten von API-Prüfobjekten umfassen:

- [Multi-Step API (MSA)-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) – der primäre API-Monitoringtyp mit fortschrittlicheren und leistungsstärkeren Funktionen im Vergleich zu Webservice HTTP- und HTTPS-Prüfobjekten.  
- [Postman API-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="de" >}}) – ein Prüfobjekt, mit dem du API-Prüfungen durch Ausführen einer Postman Workspace-Sammlung im Uptrends Checkpoint-Netzwerk voll ausschöpfen kannst. 
- [Webservice HTTP- und HTTPS-Prüfobjekte]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/monitoring-web-services" lang="de" >}}) – ein klassischer HTTP-Prüfobjekttyp, der nur Basic-Checks zur Verfügbarkeit und Bereitschaft der API ausführt.

{{< callout >}} **Hinweis:** Für das API-Monitoring sind die Prüfobjekttypen **Webservice HTTP und Webservice HTTPS** für neue Nutzer nicht mehr verfügbar. Uptrends empfiehlt, stattdessen das Multi-Step API-Prüfobjekt zu nutzen und das Verhalten deiner API eingehender zu prüfen. {{< /callout >}}

Weitere Informationen zu den API-Prüfobjekten findest du unter [API-Monitoring]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}).

## Transaktionsprüfobjekte

Ein Transaktionsprüfobjekt, auch bekannt als Webanwendungs- oder User-Journey-Prüfobjekt, simuliert Nutzeraktivitäten mithilfe eines tatsächlichen (realen) Browsers, um die Performance deiner Website zu testen.

Stelle dir einen Nutzer vor, wie er mit deiner Website in einem Browser-Fenster interagiert. Er füllt Formulare aus, klickt auf Schaltflächen und trifft eine Auswahl, während er durch eine Transaktion auf deiner Website navigiert. Transaktionsprüfobjekte ersetzen diesen Nutzer mit einem Roboter, der genau dasselbe macht. Dieser Roboter ist ein Uptrends Checkpoint-Computer, der einen Chrome-Browser aufruft und ein Skript nutzt, um auf deiner Website zu navigieren und sie zu testen. Diese Skripte werden ausgeführt, um dieselben Aktionen zu vollziehen, wie es deine Nutzer jeden Tag machen.

Transaktionsprüfobjekte bieten den [ITRS Uptrends Transaktionsrekorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}}), mit dem du deine Transaktionen automatisieren kannst. Es handelt sich um eine Chrome-Erweiterung, die deinen Bildschirm aufzeichnet, während du durch deine Transaktionen klickst. Sobald deine Transaktionen erfolgreich aufgezeichnet wurden, kannst du sie als Prüfobjekt speichern. Daraufhin werden aus der Aufzeichnung Skripte erzeugt.

Um ein Transaktionsprüfobjekt einzurichten, kannst du folgendermaßen vorgehen:

- Erzeuge ein Transaktionsprüfobjekt von Grund auf anhand des [Schritte-Editors für Transaktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}).
- [Lade den Transaktionsrekorder herunter und nutze ihn]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}}), um Skripte zu erzeugen, die du später bearbeiten und verwalten kannst.
- Lasse das Uptrends Support-Team deine Aufzeichnung nutzen, um für dich das Skript zu schreiben und zu testen.

Weitere Informationen zu Transaktionsprüfobjekten findest du hier:

- [Transaktionsprüfobjekt – Übersicht]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}})
- [Das Transaktions-Monitoring verstehen]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="de" >}})
- [Der ITRS Uptrends Transaktionsrekorder: die User Journey in einem Shop-Tutorial]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/tutorial-introduction" lang="de" >}}) – eine detaillierte Anleitung zur Nutzung des Transaktionsrekorders.