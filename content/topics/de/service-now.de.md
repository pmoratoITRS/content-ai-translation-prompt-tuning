{
  "hero": {
    "title": "Website Monitoring-Alarme mit ServiceNow erhalten"
  }, 
  "title": "Die Integration in ServiceNow",
  "summary": "Erhalte Website Monitoring-Alarmierungen von Uptrends in ServiceNow.",
  "url": "/support/kb/alerting/integrations/service-now",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/service-now" 
}

**ServiceNow** ist eine cloudbasierte Plattform, die dich bei der allgemeinen Verwaltung deines IT-Betriebs anhand verschiedener ServiceNow-Anwendungen, darunter das Incident Management, unterstützt.

Die Integration von **ServiceNow** bei Uptrends erzeugt automatisch Ereignisse, die in deinem **ServiceNow**-Account wiedergegeben werden. Um mehr über ServiceNow zu erfahren, lies die [ServiceNow Integrations-Dokumentation](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/managing-data/concept/integrations.html) und [ServiceNow REST APIs](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html).

## Die Integration einrichten

Für das Einrichten der Integration für **ServiceNow** bei Uptrends benötigst du ein Konto bei ServiceNow. Stelle sicher, dass du deinen Instance-Namen und die Authentifizierungsdaten bereitliegen hast.

Um die Integration einzurichten:

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Alarmierung > Integrationen {{< /AppElement >}} auf.
2. Klicke oben rechts auf der Bildschirmseite auf die Schaltfläche {{< AppElement type="button" >}} Integration hinzufügen {{< /AppElement >}}.
3. Wähle **ServiceNow** als Fremdanbieter-Integrations-Art in dem Pop-up-Fenster aus.
4. Klicke auf {{< AppElement type="button" >}} Wähle aus {{< /AppElement >}}, um eine neue Integration zu erstellen.
5. **ServiceNow** wird die Standard-**Integrations-Art** sein. Gib der neuen Integration einen Namen.
6. Fülle im Abschnitt **Vordefinierte Variablen** die folgenden **Werte** aus:

- `InstanceName` – der Instanz-Name von deinem ServiceNow. Diesen findest du in der ServiceNow-basierten URL `https://<instancename>.service-now.com`.
- `Username` – der Benutzername deiner ServiceNow-Anmeldedaten.
- `Password` – das Passwort deiner ServiceNow-Anmeldedaten.

Du kannst diese Werte entweder als **Reintext** eingeben oder in der [Vault]({{< ref path="/support/kb/account/vault" lang="de" >}}) gespeicherte **Vault Anmeldedaten** abrufen. Die Integration nutzt automatisch Basic Authentication, um auf die **ServiceNow**-Plattform zuzugreifen.

![ServiceNow Integration](/img/content/scr-service-now-integration.min.png)

7. Optional: Um deine Anmelde- und anderen Integrations-Einstellungen anzupassen, aktiviere das Kontrollkästchen **Integration anpassen**. Durch Aktivieren der Anpassung, kannst du:

- **Vordefinierte Variablen** hinzufügen und bearbeiten, um diese für Authentifizierung, Eskalationsstufen und Schritte-Definitionen zu verwenden.
- Schritte für unterschiedliche Alarmierungstypen hinzufügen und definieren. In den meisten Fällen ist ein einzelner HTTP-Schritt eventuell schon ausreichend für die Einrichtung. Solltest du getrennte Schritte für andere Szenarien benötigen, etwa eine Authentifizierung, klicke auf die Schaltfläche {{< AppElement type="button" >}} Füge Schritte ein {{< /AppElement >}}.
- [Warnmeldungen]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="de" >}}) für unterschiedliche Alarmtypen anpassen. Diese Nachricht enthält, welche externen Anbieter oder welche API kontaktiert werden soll, den HTTP-Benachrichtigungsinhalt, die erforderliche Authentifizierung und weitere Informationen.

![Benutzerdefinierte vordefinierte Variablen](/img/content/scr-service-now-integration-customization.min.png)

![Benutzerdefinierte Schrittdefinition](/img/content/scr-service-now-integration-customization-steps.min.png)

8. Optional: Wähle auf dem Tab {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} einen Operator oder eine Operator-Gruppe aus, um [Integrations-Berechtigungen]({{< ref path="/support/kb/alerting/integrations/integrations-permissions" lang="de" >}}) hinzuzufügen.

9. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

10. Um deine Einrichtung zu verifizieren, teste die benutzerdefinierte Integration über [Sende Test-Alarm]({{< ref path="/support/kb/alerting/integrations/custom-integrations/testing-your-custom-integration" lang="de" >}}). Weitere Details findest du im Knowledge-Base-Artikel [Testen von Warnmeldungen an externe Systeme]({{< ref path="/support/kb/alerting/testing-alert-configurations#sending-a-test-message-to-third-party-systems" lang="de" >}}).

Damit ist die Einrichtung der Integration von **ServiceNow** bei Uptrends abgeschlossen. Du kannst diese Integration nun verwenden und sie zu deinen [Meldedefinitionen]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}) hinzufügen.

{{< callout >}}
**Tipp:** Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
{{< /callout >}}

Solltest du Fragen haben, wende dich bitte an unser [Support-Team](/contact).
