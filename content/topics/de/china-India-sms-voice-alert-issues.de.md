{
  "hero": {
    "title": "Probleme mit SMS- und Sprachnachrichten in China und Indien"
  },
  "title": "Probleme mit SMS- und Sprachnachrichten in China und Indien",
  "summary": "Spam-Filter und Anrufschutz-Registraturen blockieren eventuell Warnmeldungen in einigen Regionen. Überlege den Einsatz dieser anderen Optionen für Operatoren in China oder Indien.",
  "url": "/support/kb/alarme/probleme-mit-sms-und-sprachnachrichten-in-china-und-indien",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/china-india-sms-voice-alert-issues"
}

Erhalten deine Operatoren in China und Indien die an sie gerichteten Warnmeldungen nicht oder nur zum Teil? Behördliche Vorschriften in China und Indiens National Customer Preference Register (auch Do Not Disturb Registry genannt) blockieren einige Telefonanrufe und SMS.

## Spam-Filter in China

China untersucht telefonische Anrufe und SMS, die von außerhalb des Landes eingehen und blockiert Anrufe und SMS, die als Spam erachtet werden: so eine Zusammenfassung der Situation durch [Twilio.](https://support.twilio.com/hc/en-us/articles/360016488474-Calling-Limitations-to-China)

„Unser Netzwerk und unsere Betriebspartner müssen strenge Auflagen erfüllen, um Telefonanrufe nach China zu führen. Diese Auflagen stufen Anrufintervalle von unter zwei Minuten und hohe Anrufvolumen mit derselben Anruferkennung als unerwünscht ein. Hält man sich nicht an diese Vorgaben, riskiert man eine komplette und dauerhafte Blockierung ohne Vorwarnung. Um mit unseren Partnern regelkonform zu bleiben, kann Twilio Anrufe von kurzer Dauer nach China in Zukunft nicht mehr unterstützen. Dies gilt für den gesamten internationalen Telekommunikationsverkehr nach China und betrifft nicht nur die Twilio-Plattform. Weitere Informationen sind in unserem FAQ ‚Calling limitiations to China‘ zu finden.“

Mehrere Aspekte hinsichtlich Chinas strengen Anruf- und SMS-Anforderungen verhindern, dass Uptrends‘ Warnmeldungen ankommen:

- Durchschnittliche Anrufdauer ab 2 Minuten – Sprachnachrichten von Uptrends‘ Warnmeldung per Telefon/Sprachnachricht werden niemals diese Anforderung erfüllen.
- Häufige Anrufe, die von derselben Nummer ausgehen.
- Drei SMS, die dieselbe Nachricht enthalten, führen zu einer Blockierung. Abhängig von deinen Eskalationseinstellungen überschreiten Erinnerungsnachrichten möglicherweise die Beschränkung auf drei SMS.
- Fünf unterschiedliche Nachrichten von derselben ausgehenden Nummer an eine Nummer in China lösen eine individuelle Überprüfung und eine 24-Stunden-Sperre aller Nachrichten aus.

Wie du also siehst, werden **Sprach- und SMS-Nachrichten an Telefonnummern in China nicht zuverlässig, möglicherweise auch gar nicht empfangen.** Daher empfehlen wir, einige unser nachfolgend beschriebenen Alarmierungsmethoden in Betracht zu ziehen.

## Indien Anruf- und SMS-Blockade

Wenn dein Operator in Indien keine Sprach- oder SMS-Warnmeldungen von Uptrends erhält, ist die Nummer des Operators wahrscheinlich im [National Customer Preference Register](https://www.trai.gov.in/faqcategory/unsolicited-commercial-communicationsucc) (NCPR) gelistet. Das NCPR ermöglicht Verbrauchern, Anrufe und SMS je nach Marktsektor oder für alle Marktsektoren zu sperren. Wenn der Operator seine Nummer registriert hat, muss der Operator drei Monate ab der Registrierung warten, bevor er die Nummer von der Liste entfernen kann.

## Alternativen zur Warnmeldung per SMS oder Sprachnachricht für China und Indien

Uptrends bietet dir viele Möglichkeiten neben einer Alarmierung per SMS und Sprachnachricht, um deine Operatoren in China und Indien über Fehler zu unterrichten.

- **E-Mail** ist eine wirksame Alarmierungsmethode für diensthabende Operatoren.
- [**Integrationen**]({{< ref path="/integrations" lang="de" >}}) – wenn du Slack, PagerDuty, StatusHub, Splunk (früher VictorOps) oder ServiceNow nutzt, kannst du die Dienste schnell in deinen Account bei Uptrends integrieren, um Nachrichten an deine Operatoren in China und Indien zu senden.
- [**Webhooks**]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="de" >}}) – wenn dein externer Service oder eine App API-Anfragen erhalten und verarbeiten kann, kannst du Warnmeldungen von Uptrends über diese Services erhalten.
- **Push-Benachrichtigungen über die Uptrends App** – die [Uptrends App]({{< ref path="/mobile-apps" lang="de" >}}) für iPhone und Android kann Push-Benachrichtigungen an deine Operatoren senden.
