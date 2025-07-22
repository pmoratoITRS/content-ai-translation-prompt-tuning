{
  "hero": {
    "title": "Transaktions-Monitoring – Übersicht"
  },
  "title": "Transaktions-Monitoring – Übersicht",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/ubersicht-uber-die-transaktionsuberwachung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Mit dem Transaktions-Monitoring, auch Web Application Monitoring genannt, prüfst du, ob Nutzeraktionen auf deiner Website korrekt funktionieren. Bei den Interaktionen kann es sich zum Beispiel um einfache Anmeldungen oder alle Vorgänge handeln, die bei einem Kauf in deinem Webshop ablaufen.

Um diese Nutzerinteraktionen zu überwachen, müssen sie mit einem Skript dargestellt werden, das immer und immer wieder ausgeführt werden kann, um auch später zu bestätigen, dass weiterhin alles wie erwartet funktioniert. Uptrends bietet dir einen Transaktionsrekorder (in Form einer Chrome-Erweiterung), um auf einfache Weise ein Skript zu erstellen. Wenn du das Skript aufgezeichnet hast, kannst du es selbst bearbeiten (Self-Service Transactions) oder dich an den Support von Uptrends wenden, damit dieser das Skript abschließend bearbeitet (Full-Service Transactions). Möchtest du das Skript von Grund auf selbst schreiben, kannst du den Schritt der Aufzeichnung auslassen und dein eigenes Skript mit einem Transaktionsprüfobjekt verwenden.

Beim Hochladen der Transaktionsaufzeichnung in deinen Uptrends Account wird ein Transaktionsprüfobjekt mit den grundlegenden Daten erstellt. Du wirst einige Einstellungen nach deinen Anforderungen anpassen müssen.

Nachdem du dein Transaktionsprüfobjekt ausprobiert hast und es zufriedenstellend funktioniert, kannst du mit den Einstellungen der [Alarmierung]([LINK_URL_1]) fortfahren. Denn darum geht es schließlich: die Warnmeldungen, wenn etwas nicht wie erwartet funktioniert.

[SHORTCODE_1]
Es gibt ein detailliertes Tutorial zur [User Journey bei Shop-Funktionen]([LINK_URL_2]), das von den Grundlagen bis hin zum Transaktions-Monitoring und dem Prüfen der Monitoring-Daten alles erläutert.
[SHORTCODE_2]

## 1. Einführung

Wenn das Webanwendungs-/Transaktions-Monitoring etwas Neues für dich ist, findest du Grundlagen und Infos hierzu in den folgenden Artikeln:

- Eine Einführung – [Was ist Web Application Monitoring?]([LINK_URL_3])
- Erfahre, [weshalb du das Web Application Monitoring nutzen solltest]([LINK_URL_4])
- Stelle fest, ob das Web Application Monitoring die [richtige Lösung]([LINK_URL_5]) für dich ist

## 2. Das Transaktions-Monitoring planen

Zu verstehen, wie deine Transaktionen funktionieren, welche Funktionen du testen musst und wie sich das Monitoring auf dein System auswirkt, ist ein wichtiger Teil der Planung deiner Transaktionen. Bei der Einrichtung eines Transaktions-Monitorings musst du eventuell auch andere Teams deines Unternehmens einbeziehen.

- [Skizziere mögliche Transaktionspfade]([LINK_URL_6])
- Lege fest, [was getestet wird]([LINK_URL_7])
- [Vorbehalte, Tipps und Tricks]([LINK_URL_8]): Dinge, die du berücksichtigen und auf die du besonders achten musst, wenn du dein Monitoring einrichtest
- [Gründe, weshalb du eventuell die Hilfe anderer Teams]([LINK_URL_9]) deines Unternehmens benötigst

## 3. Die Transaktion aufzeichnen

Der richtige Einsatz des [Transaktionsrekorders]([LINK_URL_10]) führt zu klaren Aufzeichnungen und einer schnelleren Einrichtung des Prüfobjekts.

- [Den Transaktionsrekorder herunterladen und nutzen]([LINK_URL_11])
- Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]([LINK_URL_12]) an, um zu erfahren, wie der Transaktionsrekorder funktioniert
- Wähle zwischen [Full-Service und Self-Service Transactions]([LINK_URL_13])

## 4. Deine Transaktionsskripte bearbeiten und testen

Wenn du deine Transaktion aufgezeichnet und dich entschieden hast, das Skript selbst zu testen (du kannst das Testen auch unserem Support-Team überlassen), solltest du Fehler beim Skript beheben, gegebenenfalls noch Inhaltsprüfungen einrichten und die Vault-Berechtigungen für neu geschaffene Elemente ändern. Und schließlich solltest du dein Prüfobjekt im Staging-Modus prüfen, bevor du es in Produktion nimmst.

- Um mehr über den Editor, die Schritte und die Aktionen zu erfahren, lies bitte [Den Step-Editor verstehen]([LINK_URL_14]).

- Aktionen sind der Kern von Transaktionen. Erfahre mehr über sie:
   - [Seiteninteraktionen – Navigieren, Klicken, Übernehmen usw.]([LINK_URL_15])
   - [Testaktionen – Inhaltsprüfungen und Warten ]([LINK_URL_16])
   - [Kontrollaktionen – (Inline) Frames oder Tabs wechseln]([LINK_URL_17])
   - [Kontrollaktionen – Variableninhalt anpassen]([LINK_URL_18])
   - [Fehler bei optionalen Schritten und Aktionen ignorieren]([LINK_URL_19])
   - [Selektoren nutzen]([LINK_URL_20]) und [Selektoralternativen]([LINK_URL_21])
   - [Transaktionsvariablen]([LINK_URL_22]) und [Inhalt der Variable anpassen]([LINK_URL_23])

- In der Übung [Testen und Bearbeiten deiner Skripte]([LINK_URL_24]) erfährst du mehr zur Funktion *Jetzt testen*, zur Handhabung dynamischer IDs und zu Zeitüberschreitungsfehlern. Es ist auch eine [Test-Checkliste]([LINK_URL_25]) enthalten.

- Einige andere Dinge, die du je nach Einrichtung und Transaktionen berücksichtigen solltest:
  - [Sensible Daten handhaben]([LINK_URL_26]), die automatisch während der Aufzeichnung zur Vault hinzugefügt wurden
  - [Vault-Autorisierungen verwalten (automatisch erstellte Bereiche)]([LINK_URL_27])
  - Transaktions-Monitoring [für Mobilgeräte]([LINK_URL_28])
  - Arbeiten mit [Shadow DOMs]([LINK_URL_29]) bei Transaktionen
  - Arbeiten mit der [SMS-basierten 2FA]([LINK_URL_30]) oder [Einmal-Passwort-basierten 2FA]([LINK_URL_31]) bei Transaktionen

  - Hinzufügen von [extra Metriken]([LINK_URL_32]) wie [Core Web Vitals]([LINK_URL_33]) und [W3C Navigation Timings]([LINK_URL_34]) zu deinen Transaktionsergebnissen

  - Umgehen oder Überschreiben des Standard-DNS-Systems mit einem [DNS Bypass]([LINK_URL_35]) bei deiner Transaktion

## 5. Ergebnisse des Transaktions-Monitorings

Sobald deine Transaktionen überwacht werden, erhältst du Feedback. Es gibt einige Ressourcen, die du dir ansehen kannst, um zu erfahren, warum Fehler gemeldet wurden.

- [Screenshots]([LINK_URL_36])

- [Wasserfall-Berichte]([LINK_URL_37])

- [W3C Navigation Timings]([LINK_URL_38])

- [Core Web Vitals]([LINK_URL_39])

- [Fehler analysieren]([LINK_URL_40])

## 6. Problembehebung

Sollte das Transaktions-Monitoring nicht so funktionieren, wie du es erwartest, siehe dir Folgendes an:

- [Ausschluss A/B-Tests]([LINK_URL_41])

- [Inkognito-Modus nutzen]([LINK_URL_42])

- [Vorbehalte, Tipps und Tricks]([LINK_URL_43])

## Credits

Transaktionsprüfobjekte verwenden Transaktions-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]([LINK_URL_44]).
