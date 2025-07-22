{
  "hero": {
    "title": "Testen von Warnmeldungen"
  },
  "title": "Testen von Warnmeldungen",
  "summary": "Warnmeldungen können eine sehr nützliche Möglichkeit sein, auf dem aktuellen Stand hinsichtlich Status und Performance von Websites zu bleiben. Achte darauf, sie zu testen.",
  "url": "/support/kb/alarme/warnmeldung-konfigurationen-testen",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/testing-alert-configurations"
}

Warnmeldungen können eine sehr nützliche Möglichkeit sein, auf dem aktuellen Stand hinsichtlich Status und Performance von Websites, Server und Webservices zu bleiben.

Wenn beim Uptrends Monitoring ein Alarm ausgelöst wird, kann eine Warnmeldung an Operatoren oder an eine externe Anwendung gesendet werden. Die Meldung kann per Telefon (Sprachnachricht), E-Mail oder SMS oder als (benutzerdefinierte) Nachricht an eine Anwendung übermittelt werden. Wie das Senden der Meldungen erfolgt, wird in den Integrationen definiert; wann das Senden der Meldungen erfolgt, wird in den Meldedefinitionen festgelegt. Lies hierzu den Artikel [Alarmierung]({{< ref path="support/kb/alerting" lang="de" >}}).

Da es wichtig ist, dass die Nachrichten den Operator oder die Anwendung erreichen, solltest du testen, dass ihre Einrichtung erfolgreich war. Das Senden einer Testnachricht funktioniert für verschiedene Integrationsarten unterschiedlich. Die Schritte für jede Integrationsart werden nachfolgend beschrieben.

## Versenden einer Testnachricht per E-Mail oder SMS

{{< callout >}}
**Hinweis**: Für den Zugriff auf die Account-Daten der Operatoren musst du Administrator sein.
{{< /callout >}}

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen (und Subaccounts) {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operatoren anzeigen {{< /AppElement >}}.
3. Wähle aus der Liste der Operatoren den Operator, bei dem du die Übermittlung der Nachrichten testen möchtest.
4. Stelle sicher, dass die primäre E-Mail-Adresse und die Mobiltelefonnummer auf der Registerkarte {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} eingetragen sind.
5. Klicke auf {{< AppElement type="button" >}}Test E-Mail senden{{< /AppElement >}} oder {{< AppElement type="button" >}}Test SMS senden{{< /AppElement >}}, um eine E-Mail oder eine SMS zu senden.

Der Operator sollte nach der Initiierung eines Tests eine Test-Nachricht erhalten.

Wenn du nicht Administrator bist, kannst du dennoch Testnachrichten für deinen eigenen Account senden.

1. Rufe das Nutzermenü unten im Menü auf und wähle {{< AppElement type="menuitem" >}} Benutzereinstellungen {{< /AppElement >}}.
2. Deine eigenen Account-Daten werden angezeigt.
3. Stelle sicher, dass die primäre E-Mail-Adresse und die Mobiltelefonnummer eingetragen sind. Klicke auf {{< AppElement type="button" >}}Test E-Mail senden{{< /AppElement >}} oder {{< AppElement type="button" >}}Test SMS senden{{< /AppElement >}}, um den Test auszuführen.

## Eine Testnachricht an ein fremdes System senden

Mehrere externe Anwendungen können Alarmierungen von der Uptrends Anwendung empfangen. Es gibt schlüsselfertige [Integrationen]({{< ref path="integrations" lang="de" >}}) für viele Fremdanbieter-Systeme, die über eine Testfunktion verfügen. Um eine Testnachricht senden zu können, musst du diese Integrationen hinzufügen und konfigurieren.

Ist der Test erfolgreich, erhält die externe Anwendung eine Nachricht. Wie dies von dem System gehandhabt und wie es dem Nutzer angezeigt wird, hängt von dem jeweilig verwendeten System ab. Sendest du beispielsweise eine Testnachricht an Slack, sollte diese Testnachricht in dem von dir angegebenen Kanal angezeigt werden.

### Slack und PagerDuty

Für Slack und PagerDuty gibt es eine Standardtestfunktion in der Integration:

1.  Rufe {{< AppElement type="menuitem" >}}Alarmierung > Integrationen {{< /AppElement >}} auf.
2.  Wähle aus der Liste der Integrationen diejenige, die du testen möchtest.
3.  Achte darauf, dass alle erforderlichen Informationen eingegeben wurden.
4.  Klicke auf {{< AppElement type="button" >}} Test Nachricht senden {{< /AppElement >}}.

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Um diese Integrationen mit einem einfachen Test zu prüfen, verwende die Schaltfläche {{< AppElement type="buttonSecondary" >}} Sende Test-Alarm {{< /AppElement >}} unten auf der Integrationsseite.

![Screenshot Integrationstest für Microsoft Teams](/img/content/scr_test-message-to-microsoft-teams.min.png)

Hast du die Integration angepasst, gibt es die Registerkarte {{< AppElement type="tab" >}} Anpassungen {{< /AppElement >}}. Dann kannst du die Funktion der Testnachricht für die benutzerdefinierte Integration wie unten beschrieben nutzen. Dabei werden die von dir hinzugefügten Anpassungen berücksichtigt.

## Das Senden einer Testnachricht für benutzerdefinierte Integrationen

Eine weitere Möglichkeit ist eine benutzerdefinierte Integration, bei der du das Senden von Nachrichten an externe Anwendungen einrichten kannst, für die Uptrends keine Standardintegration anbietet. Du definierst die Integration anhand der API des externen Anbieters. Auch diese Integrationen können daraufhin getestet werden, ob sie eine Nachricht auf die erwartete Weise senden.

1.  Rufe {{< AppElement type="menuitem" >}} Alarmierung > Integrationen {{< /AppElement >}} auf.
2.  Wähle aus der Liste der Integrationen die benutzerdefinierte Integration, die du testen möchtest.
3.  Achte darauf, dass alle erforderlichen Informationen eingegeben wurden.
4.  Wenn du einen einfachen Test ausführen möchtest, verwende die Schaltfläche {{< AppElement type="buttonSecondary" >}} Sende Test-Alarm {{< /AppElement >}} unten auf der Integrationsseite.
5.  Wenn du das Benachrichtigen mit deinen besonderen Einstellungen (Anpassungen) testen möchtest, rufe die Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} auf. Beim Einrichten der Integration solltest du hier die HTTP-Schritte bereits eingegeben haben. Du kannst Schritte für verschiedene Alarmtypen festlegen: Fehler, OK und Erinnerungen. Wenn du dich für unterschiedliche HTTP-Schritte für verschiedene (Kombinationen von) Warnmeldungstypen entschieden hast, existieren mehrere Definitionen von Schritten.
![Screenshot benutzerdefinierte Integrationsschritte für Alarmierungen](/img/content/scr_custom-integration-steps-for-alerts.min.png) 

6.  Klicke für jede HTTP-Schritte-Definition auf {{< AppElement type="button" >}} Sende Test-Alarm {{< /AppElement >}}.

Im Artikel [Benutzerdefinierte Integrationen einrichten]({{< ref path="support/kb/alerting/integrations/custom-integrations" lang="de" >}}) erfährst du mehr über das Senden von Testnachrichten an benutzerdefinierte Integrationen.

## Problembehebung

Sollte deine Nachricht nicht wie erwartet ankommen, findest du hier einige allgemeine Tipps zur Problembehebung: [Alarme – Problembehebung]({{< ref path="support/kb/alerting#troubleshooting" lang="de" >}}).
