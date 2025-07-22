{
  "hero": {
    "title": "Betreff von E-Mails anpassen und E-Mails formatieren"
  },
  "title": "Betreff von E-Mails anpassen und E-Mails formatieren",
  "summary": "In diesem Artikel findest du eine Anleitung, wie du den Betreff von Alarmierungs-E-Mails anpasst und die HTML-Formatierung aktivierst.",
  "url": "/support/kb/alarme/alarmierung-email-betreff-anpassen",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/customize-alert-email-subject",
  "tableofcontents": true,
  "sectionlist": true
}

Damit du den Status deiner Prüfobjekte ganz einfach per E-Mail nachhalten und kategorisieren kannst, ermöglicht Uptrends dir, den Betreff von Alarmierungs-E-Mails der Integration **Alerting by Email** anzupassen. Du kannst Alarme sowohl für einzelne Prüfobjekte wie auch für Prüfobjektgruppen erhalten, abhängig vom erzeugten Fehler in einem bestimmten Zeitraum. Der von dir eingerichtete Betreff wird für alle ausgehenden E-Mail-Alarmierungen verwendet.

Um den Betreff der E-Mail anzupassen:

1. Rufe {{< AppElement type="menuitem" >}} Alarmierung > Integrationen {{< /AppElement >}} > **Alerting by Email** auf. 
2. Aktiviere das Kontrollkästchen **Integration anpassen**, um den Tab {{< AppElement type="tab" >}} Anpassungen {{< /AppElement >}} anzuzeigen.
3. Wechsle zum Tab {{< AppElement type="tab" >}} Anpassungen {{< /AppElement >}}.
4. Um E-Mails in HTML-Format zu erhalten, lies die Anweisungen zur [HTML-Formatierung]({{< ref path="/support/kb/alerting/customize-alert-email-subject#html-formatting" lang="de" >}}). Andernfalls fahre mit dem nächsten Schritt fort.
5. Wähle die Kontrollkästchen der [Alarmierungstypen]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="de" >}}) (Fehler, Erinnerung, OK), um den Betreff für jedes einzelne Prüfobjekt oder mehrere Prüfobjekte anzupassen. 
6. Gib einen neuen Betreff ein. Du kannst eine Reihe an Variablen wie [automatische Variablen]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}}) und [Variablen des Alarmierungssystem]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="de" >}}) im Betrefffeld der E-Mail verwenden. Verwende beispielsweise die Variablen `{{@monitor.name}}` und `{{@alert.timestamp}}`, um dich auf den Prüfobjektnamen sowie Datum und Uhrzeit des Alarms zu beziehen.

7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.


![Anpassen des Betreffs einer Alarmierungs-E-Mail](/img/content/scr-customizing-email-subjects_020624.min.png)

## HTML-Formatierung

Du kannst ausgehende Alarmierungs-E-Mails für HTML-Format freigeben, um E-Mails im Rich-Text-Format (mit Bannern, Farben, Bildern und Hyperlinks) statt Reintext zu erhalten. Beachte, dass das Umstellen von Standard-Reintext-E-Mails auf HTML-Format zu Problemen mit den automatisierten Systemen führen kann, die die Formatierung umsetzen. Standardmäßig ist die HTML-Formatierung nur für neue Accounts aktiviert. Um diese Einstellung zu aktivieren oder zu deaktivieren, beachte die folgenden Anweisungen.

Um die HTML-Formatierung zu aktivieren:

1. Wechsele zum Tab {{< AppElement type="tab" >}} Anpassungen {{< /AppElement >}} und aktiviere das Kontrollkästchen **HTML-Mail verwenden**.
2. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Um die HTML-Formatierung zu deaktivieren:

1. Wechsele zum Tab {{< AppElement type="tab" >}} Anpassungen {{< /AppElement >}} und deaktiviere das Kontrollkästchen **HTML-Mail verwenden**.
2. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.
