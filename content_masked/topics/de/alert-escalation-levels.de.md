{
  "hero": {
    "title": "Eskalationsstufen zu Alarmen"
  },
  "title": "Eskalationsstufen zu Alarmen",
  "summary": "Mit Meldedefinitionen und Eskalationsstufen kannst du Warnmeldungen für bestimmte Empfänger oder Integrationen konfigurieren, die mit den Eskalierungsbestimmungen deines Unternehmens für den Fall eines Ausfalls übereinstimmen.",
  "url": "[URL_BASE_TOPICS]alarme/alarm-eskalationsstufen",
  "translationKey": "[URL_1]
}

## Was sind Eskalationsstufen?

Das Uptrends Alarmierungssystem wurde mit dem Gedanken an Unternehmensteams aufgebaut. Mit anpassbaren Eskalationsstufen kannst du sicherstellen, dass die richtigen Personen bei möglichen Problemen zur richtigen Zeit benachrichtigt werden.

Eine Eskalationsstufe enthält eine Reihe von Parametern für die Erzeugung eines Alarms, eine Anzahl an Erinnerungen, Methoden und mögliche Empfänger. Die Einstellung erfolgt in einer Meldedefinition.

Du kannst bis zu drei Eskalationsstufen einrichten und Warnmeldungen aufgrund deiner eigenen Regeln generieren:

- Erzeuge eine Alarmierung, wenn Fehler in einem bestimmten Zeitraum auftreten oder wenn eine bestimmte Anzahl von Fehlern aufgetreten ist
- Definiere, wie viele Erinnerungen innerhalb eines bestimmten Intervalls gesendet werden
- Richte Alarmierungsmethoden mithilfe von [Integrationen]([LINK_URL_1]) ein
- Gib eine benutzerdefinierte Mitteilung (nur für Slack, PagerDuty und E-Mail-Benachrichtigungen) ein
- Füge ein Traceroute-Protokoll in E-Mails ein
- Füge eine zusätzliche E-Mail-Adresse zur Alarmierung weiterer Personen hinzu
- Wähle, welche Operatoren oder Operator-Gruppen alarmiert werden
- Entscheide (für jede Integration), ob du OK-Meldungen und Erinnerungen senden möchtest

## Eskalationsstufen für Warnmeldungen einrichten

Bei jeder Meldedefinition stehen dir ein bis drei Eskalationsstufen zur Verfügung. Um Eskalationsstufen einzurichten:

1. Rufe [SHORTCODE_1]Alarmierung > Meldedefinitionen [SHORTCODE_2] auf und wähle eine Meldedefinition, die du ändern möchtest. Du kannst auch die [Uptrends Menü-Suche]([LINK_URL_2]) verwenden, um eine bestimmte Definition zu finden. Solltest du einen neue Meldedefinition erstellen müssen, lies [Erstellen von Meldedefinitionen]([LINK_URL_3]).
2. Öffne die Registerkarte [SHORTCODE_3] Eskalationsstufe 1 [SHORTCODE_4].
3. Markiere das Kontrollkästchen **Aktiv**, sofern es noch nicht aktiviert ist.
4. Lege die Regeln für die **Eskalation** fest, indem du die Parameter für *Generiere eine Warnmeldung* eingibst.
5. Lege die Häufigkeit der Erinnerungen fest. Erfahre mehr mit unserem Knowledge-Base-Artikel [Erinnerungen bei Alarmen]([LINK_URL_4]).
6. Wähle eine oder mehrere Optionen unter **Alarmierung durch Integrationen**, z. B. die vordefinierte Integration **Alarmierung durch E-Mail**, **SMS** (SMS benötigt Benachrichtigungs-Credits) oder **Telefon**.
7. Wenn du eine andere Integration konfiguriert hast, kannst du sie hier auswählen. Lies den Knowledge-Base-Artikel [Integrationen]([LINK_URL_5]), um mehr zu erfahren.
8. Für die meisten Integrationen kannst du entscheiden, ob du OK-Meldungen und Erinnerungen erhalten möchtest Erweitere die Integration, indem du auf den Pfeil > vor der Integration klickst und die entsprechenden Optionen aktivierst.

   ![Screenshot Alarmierungsoptionen]([LINK_URL_6])

   Beachte, dass [benutzerdefinierte Integrationen]([LINK_URL_7]) [Nachrichtentypen]([LINK_URL_8]) nutzen, um unterschiedliche Alarmierungen (Fehler, Erinnerung, OK) zu handhaben. Die von dir vorgenommenen Einstellungen bei den Nachrichtentypen werden in der Meldedefinition angezeigt, können dort aber nicht geändert werden. Änderungen müssen in der benutzerdefinierten Integration selbst vorgenommen werden.
9. Gib eine benutzerdefinierte Mitteilung ein (optional und nur bei einigen Integrationen möglich).
10. Aktiviere das Kontrollkästchen **Routenverfolgung**, um in den E-Mails ein Traceroute-Protokoll zu erhalten.
11. Nutze den Bereich **Gruppen und Operatoren**, um die Operatoren für die Eskalationsstufe auszuwählen. Denke daran, dass Warnmeldungen nur an aktive und diensthabende Operatoren gesendet werden. *Aktiv* ist eine Haupteinstellung für einen Operator und diensthabend wird vom [Dienstplan([SHORTCODE_7]) des jeweiligen Operators abgeleitet.
12. Richte die Eskalationsstufen 2 und 3 ein, wenn der Eskalationsweg deines Unternehmens dies vorsieht.
13. Sofern du alle Konfigurationen für die Stufe vorgenommen hast, klicke auf [SHORTCODE_5]Speichern[SHORTCODE_6].

## Alarmierung durch Integrationen

Der Knowledge-Base-Artikel zu [Integrationen]([LINK_URL_9]) erläutert die unterschiedlichen Integrationstypen, darunter Telefon (Benachrichtigungs-Credits erforderlich) und Integrationen wie [PagerDuty]([LINK_URL_10]), [Microsoft Teams]([LINK_URL_11]), [Slack]([LINK_URL_12]) und [StatusHub]([LINK_URL_13]).

## Testen von Alarmkonfigurationen

Sobald du die Eskalationsstufen eingerichtet und die gewünschten Integrationen hinzugefügt hast, kannst du testen, ob Benachrichtigungen erfolgreich gesendet werden. Der Knowledge-Base-Artikel [Testen von Warnmeldungen]([LINK_URL_14]) erläutert die verfügbaren Methoden für unterschiedliche Integrationen.