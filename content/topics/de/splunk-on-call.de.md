{
  "hero": {
    "title": "Monitoring-Alarmierungen in Splunk On-Call erhalten"
  }, 
  "title": "Die Integration Splunk On-Call",
  "summary": "Erhalte Website-Monitoring-Meldungen von Uptrends in Splunk On-Call.",
  "url": "/support/kb/alerting/integrations/splunk-on-call",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/splunk-on-call" 
}

**Splunk On-Call** ist eine Incident-Management-Plattform, mithilfe derer DevOps-Teams zusammenarbeiten und Probleme effektiv lösen können. Du kannst dein Team für Bereitschaftsdienst und Ereigniseskalation planen und es umgehend unterrichten, wenn ein Problem sofortige Aufmerksamkeit erfordert.

Die Integration von Splunk On-Call in Uptrends erzeugt automatisch Ereignisse, die in deinem Splunk-On-Call-Dashboard angezeigt werden. Zum Einrichten der Integration in beiden Systemen sind diese Schritte erforderlich:

## 1. Richte deine REST-Integration in Splunk On-Call ein.
1. Melde dich bei deinem Splunk-On-Call-Account an.
2. Klicke auf der Registerkarte {{< AppElement type="tab" >}}Integrations{{< /AppElement >}} auf die REST-Integration, die standardmäßig aktiviert ist. Weitere Informationen findest du unter Splunk On-Call [REST Integration](https://help.victorops.com/knowledge-base/rest-endpoint-integration-guide/).
3. Kopiere die *URL zur Benachrichtigung* ohne den Wert */$routing_key* und speichere ihn für später.

## 2. Einrichten der Integration bei Uptrends
1. Gehe zu deinem Uptrends Account und dann im Menü zu {{< AppElement type="menu" >}} Alarmierung > Integrationen {{< /AppElement >}}.
2. Klicke oben rechts auf der Bildschirmseite auf die Schaltfläche {{< AppElement type="button" >}}Integration hinzufügen{{< /AppElement >}}.
3. Wähle im eingeblendeten Pop-up *Splunk On-Call* als Fremdanbieter-Integrationstyp.
4. Klicke auf {{< AppElement type="button" >}}Wähle aus{{< /AppElement >}}.
5. Du kannst nun die Einzelheiten deiner Integrationseinrichtung bearbeiten. Gib deiner neuen Integration einen Namen.
6. Standardmäßig ist das Feld {{< AppElement type="menuitem" >}}Integration anpassen{{< /AppElement >}} deaktiviert. Aktiviere das Kontrollkästchen und passe die Standardeinstellungen der Integration für Splunk On-Call. Du kannst dies auch belassen, wie es war.

{{< callout >}}
**Hinweis**: Wenn du {{< AppElement type="menuitem" >}}Integration anpassen{{< /AppElement >}} aktivierst, wird die Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} eingeblendet. Darauf kannst du angeben, welche Nachrichten gesendet werden, wenn ein Alarm generiert wird, einschließlich zu kontaktierende Drittanbieter oder API, Inhalt von HTTP-Meldungen oder eine Authentifizierung, die erforderlich ist, usw.

In den meisten Fällen reicht ein einzelner HTTP-Schritt. Es ist jedoch möglich, weitere Schritte hinzuzufügen, wenn du separate Schritte zur Authentifizierung benötigst. Du kannst auch getrennte Schritte für individuelle Alarmierungstypen definieren. Das kann hilfreich sein, wenn deine Fehlermeldungen sich von den OK-Meldungen (für bearbeitete Alarme) unterscheiden müssen. Weitere Informationen findests du in den [Knowledge-Base-Artikeln zu Integrationen]({{< ref path="support/kb/alerting/integrations" lang="de" >}}).
{{< /callout >}}



7. Im Abschnitt Vordefinierte Variablen siehst du den Namen *SplunkOnCallUrl*. Wähle aus dem Drop-down-Menü, welcher Wert angegeben werden soll. Du kannst zum Beispiel die Option *Wert hier eintragen* wählen.
8. Klicke im nächsten Feld neben dem *SplunkOnCallUrl*-Drop-down auf die drei Auslassungspunkte. Es wird ein Pop-up eingeblendet mit zwei Optionen. Du kannst den Wert der *URL zur Benachrichtigung*, den du zuvor gespeichert hast, in das Klartext-Feld eingeben oder einen Benutzernamen und ein Passwort für die [Vault Anmeldedaten]({{< ref path="support/kb/account/vault#credential-set" lang="de" >}}) (sofern zutreffend) wählen.
9. Klicke auf die Schaltfläche {{< AppElement type="button" >}}Auswählen{{< /AppElement >}}.
10. Gib dann den Wert für den *RoutingKey* an, den du verwenden möchtest. [Routing Keys](https://help.victorops.com/knowledge-base/routing-keys/) sind unter der Registerkarte {{< AppElement type="tab" >}} Settings {{< /AppElement >}} in deinem Splunk-On-call-Account zu finden.
11. Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die Integrationseinstellungen zu sichern.

Damit ist die Einrichtung der Integration bei Uptrends abgeschlossen. Du kannst diese Integration nun verwenden und sie zu deinen [Meldedefinitionen]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}) hinzufügen.

**Und das war‘s schon!** Du hast die Integration von Splunk On-Call eingerichtet.

Was passiert, wenn diese Integration eingerichtet ist? Das Beispiel unten zeigt, wie die Integration in deinem Splunk-On-Call-Dashboard angezeigt wird.
![Splunk On-Call Dashboard mit Uptrends Integrationen](/img/content/scr_integration-splunk-on-call.min.png)

{{< callout >}}
**Tipp**: Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
{{< /callout >}}

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team](/contact).
