{
  "hero": {
    "title": "Transaktions-Monitoring – Übersicht"
  },
  "title": "Transaktions-Monitoring – Übersicht",
  "url": "/support/kb/synthetic-monitoring/transaktionen/ubersicht-uber-die-transaktionsuberwachung",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transactions-overview",
  "sectionlist": false
}

Mit dem Transaktions-Monitoring, auch Web Application Monitoring genannt, prüfst du, ob Nutzeraktionen auf deiner Website korrekt funktionieren. Bei den Interaktionen kann es sich zum Beispiel um einfache Anmeldungen oder alle Vorgänge handeln, die bei einem Kauf in deinem Webshop ablaufen.

Um diese Nutzerinteraktionen zu überwachen, müssen sie mit einem Skript dargestellt werden, das immer und immer wieder ausgeführt werden kann, um auch später zu bestätigen, dass weiterhin alles wie erwartet funktioniert. Uptrends bietet dir einen Transaktionsrekorder (in Form einer Chrome-Erweiterung), um auf einfache Weise ein Skript zu erstellen. Wenn du das Skript aufgezeichnet hast, kannst du es selbst bearbeiten (Self-Service Transactions) oder dich an den Support von Uptrends wenden, damit dieser das Skript abschließend bearbeitet (Full-Service Transactions). Möchtest du das Skript von Grund auf selbst schreiben, kannst du den Schritt der Aufzeichnung auslassen und dein eigenes Skript mit einem Transaktionsprüfobjekt verwenden.

Beim Hochladen der Transaktionsaufzeichnung in deinen Uptrends Account wird ein Transaktionsprüfobjekt mit den grundlegenden Daten erstellt. Du wirst einige Einstellungen nach deinen Anforderungen anpassen müssen.

Nachdem du dein Transaktionsprüfobjekt ausprobiert hast und es zufriedenstellend funktioniert, kannst du mit den Einstellungen der [Alarmierung]({{< ref path="support/kb/alerting" lang="de" >}}) fortfahren. Denn darum geht es schließlich: die Warnmeldungen, wenn etwas nicht wie erwartet funktioniert.

{{< callout >}}
Es gibt ein detailliertes Tutorial zur [User Journey bei Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop" lang="de" >}}), das von den Grundlagen bis hin zum Transaktions-Monitoring und dem Prüfen der Monitoring-Daten alles erläutert.
{{< /callout >}}

## 1. Einführung

Wenn das Webanwendungs-/Transaktions-Monitoring etwas Neues für dich ist, findest du Grundlagen und Infos hierzu in den folgenden Artikeln:

- Eine Einführung – [Was ist Web Application Monitoring?]({{< ref path="what-is/web-application-monitoring" lang="de" >}})
- Erfahre, [weshalb du das Web Application Monitoring nutzen solltest]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#why-monitor-your-web-applications" lang="de" >}})
- Stelle fest, ob das Web Application Monitoring die [richtige Lösung]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#transaction-best-choice" lang="de" >}}) für dich ist

## 2. Das Transaktions-Monitoring planen

Zu verstehen, wie deine Transaktionen funktionieren, welche Funktionen du testen musst und wie sich das Monitoring auf dein System auswirkt, ist ein wichtiger Teil der Planung deiner Transaktionen. Bei der Einrichtung eines Transaktions-Monitorings musst du eventuell auch andere Teams deines Unternehmens einbeziehen.

- [Skizziere mögliche Transaktionspfade]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="de" >}})
- Lege fest, [was getestet wird]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="de" >}})
- [Vorbehalte, Tipps und Tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}}): Dinge, die du berücksichtigen und auf die du besonders achten musst, wenn du dein Monitoring einrichtest
- [Gründe, weshalb du eventuell die Hilfe anderer Teams]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#programming-skills" lang="de" >}}) deines Unternehmens benötigst

## 3. Die Transaktion aufzeichnen

Der richtige Einsatz des [Transaktionsrekorders]({{< ref path="features/transaction-recorder" lang="de" >}}) führt zu klaren Aufzeichnungen und einer schnelleren Einrichtung des Prüfobjekts.

- [Den Transaktionsrekorder herunterladen und nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}})
- Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="de" >}}) an, um zu erfahren, wie der Transaktionsrekorder funktioniert
- Wähle zwischen [Full-Service und Self-Service Transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="de" >}})

## 4. Deine Transaktionsskripte bearbeiten und testen

Wenn du deine Transaktion aufgezeichnet und dich entschieden hast, das Skript selbst zu testen (du kannst das Testen auch unserem Support-Team überlassen), solltest du Fehler beim Skript beheben, gegebenenfalls noch Inhaltsprüfungen einrichten und die Vault-Berechtigungen für neu geschaffene Elemente ändern. Und schließlich solltest du dein Prüfobjekt im Staging-Modus prüfen, bevor du es in Produktion nimmst.

- Um mehr über den Editor, die Schritte und die Aktionen zu erfahren, lies bitte [Den Step-Editor verstehen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}).

- Aktionen sind der Kern von Transaktionen. Erfahre mehr über sie:
   - [Seiteninteraktionen – Navigieren, Klicken, Übernehmen usw.]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="de" >}})
   - [Testaktionen – Inhaltsprüfungen und Warten ]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}})
   - [Kontrollaktionen – (Inline) Frames oder Tabs wechseln]({{< ref path="support/kb/synthetic-monitoring/transactions/Switching-between-iframes-browser-tabs" lang="de" >}})
   - [Kontrollaktionen – Variableninhalt anpassen]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="de" >}})
   - [Fehler bei optionalen Schritten und Aktionen ignorieren]({{< ref path="support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="de" >}})
   - [Selektoren nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="de" >}}) und [Selektoralternativen]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="de" >}})
   - [Transaktionsvariablen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="de" >}}) und [Inhalt der Variable anpassen]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="de" >}})

- In der Übung [Testen und Bearbeiten deiner Skripte]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="de" >}}) erfährst du mehr zur Funktion *Jetzt testen*, zur Handhabung dynamischer IDs und zu Zeitüberschreitungsfehlern. Es ist auch eine [Test-Checkliste]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction#script-testing-checklist" lang="de" >}}) enthalten.

- Einige andere Dinge, die du je nach Einrichtung und Transaktionen berücksichtigen solltest:
  - [Sensible Daten handhaben]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="de" >}}), die automatisch während der Aufzeichnung zur Vault hinzugefügt wurden
  - [Vault-Autorisierungen verwalten (automatisch erstellte Bereiche)]({{< ref path="support/kb/synthetic-monitoring/transactions/managing-authorizations-for-automatically-created-vault-sections" lang="de" >}})
  - Transaktions-Monitoring [für Mobilgeräte]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup" lang="de" >}})
  - Arbeiten mit [Shadow DOMs]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="de" >}}) bei Transaktionen
  - Arbeiten mit der [SMS-basierten 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="de" >}}) oder [Einmal-Passwort-basierten 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="de" >}}) bei Transaktionen

  - Hinzufügen von [extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) wie [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}) und [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}}) zu deinen Transaktionsergebnissen

  - Umgehen oder Überschreiben des Standard-DNS-Systems mit einem [DNS Bypass]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="de" >}}) bei deiner Transaktion

## 5. Ergebnisse des Transaktions-Monitorings

Sobald deine Transaktionen überwacht werden, erhältst du Feedback. Es gibt einige Ressourcen, die du dir ansehen kannst, um zu erfahren, warum Fehler gemeldet wurden.

- [Screenshots]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-screenshots" lang="de" >}})

- [Wasserfall-Berichte]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}})

- [W3C Navigation Timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="de" >}})

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}})

- [Fehler analysieren]({{< ref path="support/kb/synthetic-monitoring/transactions/analyzing-transaction-errors" lang="de" >}})

## 6. Problembehebung

Sollte das Transaktions-Monitoring nicht so funktionieren, wie du es erwartest, siehe dir Folgendes an:

- [Ausschluss A/B-Tests]({{< ref path="support/kb/synthetic-monitoring/transactions/exclude-a-b-tests-from-transaction-requests" lang="de" >}})

- [Inkognito-Modus nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-incognito-mode" lang="de" >}})

- [Vorbehalte, Tipps und Tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="de" >}})

## Credits

Transaktionsprüfobjekte verwenden Transaktions-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="de" >}}).
