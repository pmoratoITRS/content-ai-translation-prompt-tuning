{
  "hero": {
    "title": "Website Monitoring-Alarme mit ServiceNow erhalten"
  },
  "title": "Die Integration in ServiceNow",
  "summary": "Erhalte Website Monitoring-Alarmierungen von Uptrends in ServiceNow.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/service-now",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**ServiceNow** ist eine cloudbasierte Plattform, die dich bei der allgemeinen Verwaltung deines IT-Betriebs anhand verschiedener ServiceNow-Anwendungen, darunter das Incident Management, unterstützt.

Die Integration von **ServiceNow** bei Uptrends erzeugt automatisch Ereignisse, die in deinem **ServiceNow**-Account wiedergegeben werden. Um mehr über ServiceNow zu erfahren, lies die [ServiceNow Integrations-Dokumentation]([LINK_URL_1]) und [ServiceNow REST APIs]([LINK_URL_2]).

## Die Integration einrichten

Für das Einrichten der Integration für **ServiceNow** bei Uptrends benötigst du ein Konto bei ServiceNow. Stelle sicher, dass du deinen Instance-Namen und die Authentifizierungsdaten bereitliegen hast.

Um die Integration einzurichten:

1. Rufe in der Uptrends Anwendung [SHORTCODE_3] Alarmierung > Integrationen [SHORTCODE_4] auf.
2. Klicke oben rechts auf der Bildschirmseite auf die Schaltfläche [SHORTCODE_5] Integration hinzufügen [SHORTCODE_6].
3. Wähle **ServiceNow** als Fremdanbieter-Integrations-Art in dem Pop-up-Fenster aus.
4. Klicke auf [SHORTCODE_7] Wähle aus [SHORTCODE_8], um eine neue Integration zu erstellen.
5. **ServiceNow** wird die Standard-**Integrations-Art** sein. Gib der neuen Integration einen Namen.
6. Fülle im Abschnitt **Vordefinierte Variablen** die folgenden **Werte** aus:

- [INLINE_CODE_1] – der Instanz-Name von deinem ServiceNow. Diesen findest du in der ServiceNow-basierten URL [INLINE_CODE_2].
- [INLINE_CODE_3] – der Benutzername deiner ServiceNow-Anmeldedaten.
- [INLINE_CODE_4] – das Passwort deiner ServiceNow-Anmeldedaten.

Du kannst diese Werte entweder als **Reintext** eingeben oder in der [Vault]([LINK_URL_3]) gespeicherte **Vault Anmeldedaten** abrufen. Die Integration nutzt automatisch Basic Authentication, um auf die **ServiceNow**-Plattform zuzugreifen.

![ServiceNow Integration]([LINK_URL_4])

7. Optional: Um deine Anmelde- und anderen Integrations-Einstellungen anzupassen, aktiviere das Kontrollkästchen **Integration anpassen**. Durch Aktivieren der Anpassung, kannst du:

- **Vordefinierte Variablen** hinzufügen und bearbeiten, um diese für Authentifizierung, Eskalationsstufen und Schritte-Definitionen zu verwenden.
- Schritte für unterschiedliche Alarmierungstypen hinzufügen und definieren. In den meisten Fällen ist ein einzelner HTTP-Schritt eventuell schon ausreichend für die Einrichtung. Solltest du getrennte Schritte für andere Szenarien benötigen, etwa eine Authentifizierung, klicke auf die Schaltfläche [SHORTCODE_9] Füge Schritte ein [SHORTCODE_10].
- [Warnmeldungen]([LINK_URL_5]) für unterschiedliche Alarmtypen anpassen. Diese Nachricht enthält, welche externen Anbieter oder welche API kontaktiert werden soll, den HTTP-Benachrichtigungsinhalt, die erforderliche Authentifizierung und weitere Informationen.

![Benutzerdefinierte vordefinierte Variablen]([LINK_URL_6])

![Benutzerdefinierte Schrittdefinition]([LINK_URL_7])

8. Optional: Wähle auf dem Tab [SHORTCODE_11] Berechtigungen [SHORTCODE_12] einen Operator oder eine Operator-Gruppe aus, um [Integrations-Berechtigungen]([LINK_URL_8]) hinzuzufügen.

9. Klicke auf [SHORTCODE_13] Speichern [SHORTCODE_14], um alle Änderungen zu bestätigen.

10. Um deine Einrichtung zu verifizieren, teste die benutzerdefinierte Integration über [Sende Test-Alarm]([LINK_URL_9]). Weitere Details findest du im Knowledge-Base-Artikel [Testen von Warnmeldungen an externe Systeme]([LINK_URL_10]).

Damit ist die Einrichtung der Integration von **ServiceNow** bei Uptrends abgeschlossen. Du kannst diese Integration nun verwenden und sie zu deinen [Meldedefinitionen]([LINK_URL_11]) hinzufügen.

[SHORTCODE_1]
**Tipp:** Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
[SHORTCODE_2]

Solltest du Fragen haben, wende dich bitte an unser [Support-Team]([LINK_URL_12]).
