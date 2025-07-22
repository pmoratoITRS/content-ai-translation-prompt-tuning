{
  "hero": {
    "title": "Website Monitoring-Alarmierungen in PagerDuty erhalten"
  },
  "title": "PagerDuty",
  "summary": "Erhalte Website Monitoring-Alarmierungen in PagerDuty. Melde dich für eine kostenlose 30-tägige Testversion von Uptrends an!",
  "url": "/support/kb/alarme/integrationen/pagerduty",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/pagerduty" 
}

PagerDuty bietet Alarme, Dienstplaneinrichtung, Eskalationsrichtlinien und Vorfall-Tracking, um dein Team zu benachrichtigen und Systemdaten zu sammeln. Die Integration von **PagerDuty** in Uptrends ermöglicht das Senden von Warnmeldungen von deinem **Uptrends Account** zu deinem **PagerDuty Account**. Zum Einrichten der Integration sind nur drei Schritte erforderlich:

1.  Einrichten der Integration bei PagerDuty
2.  Einrichten der Integration bei Uptrends
3.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Möchtest du sehen, was passiert, wenn diese Integration eingerichtet ist? Unten zeigen wir ein Beispiel, wie die Integration in PagerDuty aussieht. Nachfolgend findest du die detaillierten Anweisungen, wie du es einrichten kannst!

![](/img/sub/integrations/integration-pagerduty-dashboard.png)

## 1. Einrichten der Integration bei PagerDuty

Dieses Verfahren ist nur relevant, wenn du Warnmeldungen über deinen PagerDuty Account erhalten möchtest. Die Integration von Uptrends in PagerDuty besteht aus Warnmeldungen, die von Uptrends an einen vom Nutzer konfigurierten Service bei PagerDuty gesendet werden. Damit Uptrends Warnmeldungen an diesen PagerDuty Service senden kann, musst du diesen Service bei deinem PagerDuty Account einrichten. Dieser Vorgang wird nachfolgend detailliert beschrieben.

1.  Wähle **Services** aus der oberen Menüleiste des Hauptbildschirms in deinem PagerDuty Account.
2.  Die Seite *Services* wird aufgerufen. Klicke auf die Schaltfläche **+ New Service**.
3.  Die Seite *Create a Service* wird aufgerufen. Auf dieser Seite kannst du die Service-Daten eingeben.
4.  Gib dem Service einen Namen und füge eventuell eine Beschreibung hinzu. Wähle eine bestehende Eskalationsrichtlinie aus oder erstelle bei Bedarf eine neue. Wähle, sofern erforderlich, eine angemessene **Alert Grouping**-Einstellung.
5. Zu diesem Zeitpunkt ist es **nicht** notwendig, eine Integration hinzuzufügen, da automatisch eine erstellt wird. Klicke auf *Create service without an integration*.
6.  Du wirst dann auf die Service-Seite des neu eingerichteten Service weitergeleitet. Auf der Registerkarte *Integrations* ist der **Integration Key** deines Service zu finden.

Damit ist die Einrichtung der Integration bei PagerDuty beendet.

## 2. Einrichten der Integration bei Uptrends

Die Integrationsfunktion von Uptrends kann über das Hauptmenü aufgerufen werden.

1.  Klicke im seitlichen Menü auf **Alarmierung**. Füge eine neue Integration hinzu, indem du auf das **+**-Symbol neben *Integrationen* klickst. ![Eine neue Integration hinzufügen](/img/content/scr-integrations-add_new_integration.png)
2.  Wähle *PagerDuty*, um eine Integration für PagerDuty zu erstellen. ![Auswahl von PagerDuty](/img/content/scr-pagerduty-before_setup.png)
3.  Klicke auf die Schaltfläche **Alert with PagerDuty**, um die Verbindung zwischen Uptrends und PagerDuty einzurichten. Melde dich mit deinen PagerDuty-Anmeldedaten an. ![PagerDuty Anmeldeportal](/img/content/scr-pagerduty-signin.png)
4. Wähle den bzw. die Services von PagerDuty aus, die du zusammen mit der Uptrends Alarmierung nutzen möchtest.
![Auswahl der PagerDuty Services](/img/content/scr-pagerduty-servicesselection.png)
5.  Nachdem du auf *Connect* geklickt hast, wirst du zurück zu Uptrends geleitet.
6.  Zur vollständigen Einrichtung gib einen Namen für die Integration ein und klicke unten links auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}. Nach dem Speichern erscheint das Integrationen-Fenster mit der neu erstellten Integrationsdefinition.
7.  Du kannst auf diese Integration klicken, um sie zu bearbeiten oder um eine Test-Nachricht zu senden.
![PD nach Einrichtung](/img/content/scr-pagerduty-post_setup_integration.png)

{{< callout >}}
**Tipp**: Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen über den PagerDuty Service erhalten möchtest.
{{< /callout >}}

## 3. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie **zu einer oder mehreren Eskalationsstufen hinzufügen, um entsprechende Warnmeldungen** zu erhalten.

1.  Um eine Integrationsdefinition mit einer Eskalationsstufe zu verknüpfen, rufe die gewünschte Meldedefinition und Eskalationsstufe in Uptrends auf.

 ![Navigate to alert definitions](/img/content/scr-integrations-to_alert_defs.png)

2.  Jede {{< AppElement type="tab" >}}Eskalationsstufen{{< /AppElement >}}-Registerkarte verfügt über das Element **Alarmierung durch Integrationen**. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="de" >}}), wie Eskalationsstufen funktionieren.
3. Wähle die Integrationsdefinitionen, die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die Integration bei **PagerDuty**.
4.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die Änderungen zu sichern.

**Und das war‘s schon!** Du hast die Integration bei PagerDuty eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team](/contact).
