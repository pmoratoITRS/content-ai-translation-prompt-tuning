{
  "hero": {
    "title": "Fehlerbedingungen – Überblick"
  },
  "title": "Fehlerbedingungen – Überblick",
  "summary": "Welche Fehlerbedingungen gibt es und wie werden sie genutzt? ",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/ubersicht-der-fehlerbedingungen",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
  "tableofcontents": true,
  "sectionlist": false
}

Fehlerbedingungen spielen eine wichtige Rolle bei der Erzeugung von Prüfobjektalarmen. Einrichten einer Fehlerbedingung ist der erste Schritt des [Alarm- und Fehlerablaufs]({{< ref path="support/kb/alerting/alerting-overview" lang="de" >}}), über den du Warnmeldungen erhalten kannst.

Eine **Fehlerbedingung** ermöglicht dir, eine Reihe an Kriterien zu definieren, anhand derer dein Prüfobjekt bei Website, Webservice oder Server Fehler feststellen kann. Sie dient dem Prüfobjekt als Basis, um zu entscheiden, welches Website-Verhalten zu einem Fehler führt und welches dies nicht tut.

Wenn du beispielsweise sicherstellen möchtest, dass deine Website in weniger als drei Sekunden geladen ist, kannst du eine Fehlerbedingung einrichten und Schwellen für die Seitenladezeit angeben. Oder wenn du prüfen möchtest, dass der Inhalt, Plug-ins oder Skripte deiner Website korrekt geladen wurden, kannst du jeweils bestimmte Fehlerbedingungen dafür einrichten.

Sobald eine Fehlerbedingung erfüllt wird, wird ein Fehler generiert, der einen Alarm auslöst. Wurde eine Alarmierung konfiguriert, wirst du sofort mit einer Warnmeldung benachrichtigt.

## Fehlerbedingungen für Prüfobjekttypen {id="error-conditions-by-category"}

Auf dem Tab {{< AppElement type="tab" >}} Fehlerbedingungen {{< /AppElement >}} kannst du unterschiedliche Fehlerbedingungen für jeden Prüfobjekttyp einrichten. Beachte das die Verfügbarkeit von Fehlerbedingungen je nach Kategorie des Prüfobjekts und welche Daten erfasst werden variieren kann:

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen](/img/content/scr_monitor-setup-errorconditions.min.png)

### Verfügbarkeitsprüfobjekt

Die folgenden Fehlerbedingungen sind für [Uptime-Prüfobjekttypen]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}) verfügbar:

| Prüfobjekttyp | Fehlerbedingungen | 
|--|--|
| HTTPS, Webservice HTTP und HTTPS | {{< tableformatter >}} 
- [Prüfe Seitenerreichbarkeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="de" >}}) 
- [Prüfe Seiteninhalt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="de" >}})
- [Prüfe Seitenladezeit]({{< ref path="" lang="de" >}})
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
{{< /tableformatter >}} |
| DNS, SSL, SFTP, FTP | {{< tableformatter >}}
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
- [Prüfe komplette Laufzeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}})
{{< /tableformatter >}} |
| SMTP, POP3, IMAP | {{< tableformatter >}}
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
- [Prüfe komplette Laufzeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}})
{{< /tableformatter >}} |
| Microsoft SQL Server,  MySQL | {{< tableformatter >}}
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
- [Prüfe komplette Laufzeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}})
{{< /tableformatter >}} |
| Ping, Connect | {{< tableformatter >}}
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
- [Prüfe komplette Laufzeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}})
{{< /tableformatter >}} |

### Browser-Prüfobjekte oder Full Pagecheck (FPC)

Die folgenden Fehlerbedingungen sind verfügbar für [Browser- bzw. Full Pagecheck (FPC)-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}):

| Prüfobjekttyp | Fehlerbedingungen |
|--|--|
| Browser- bzw. Full Pagecheck | {{< tableformatter >}}

- [Prüfe Seitenerreichbarkeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="de" >}}) 
- [Prüfe Seiteninhalt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="de" >}})
- [Von der Seite geladene URLs überprüfen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="de" >}}) 
- [Prüfe Seitenladezeit]({{< ref path="" lang="de" >}})
- [Prüfe Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="de" >}})
- [Prüfe W3C-Metriken]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="de" >}})
- [Prüfe Konsoleninhalt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="de" >}})
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
{{< /tableformatter >}} |

### Transaktionsprüfobjekt

Fehlerbedingungen bei [Transaktionsprüfobjekten]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) sind auch für jeden Schritt verfügbar. Abhängig von der [Einrichtung des Transaktionsschritts]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}) sind die folgenden Fehlerbedingungen verfügbar bzw. nicht verfügbar:

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen](/img/content/scr-error-condition-transactions.min.png)

| Prüfobjekttyp | Fehlerbedingungen |
|--|--|
| Transaktion bzw. User Journey | {{< tableformatter >}} 
- [Inhaltsprüfungen]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}).
- [Prüfe Ressourcen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="de" >}})
- [Von der Seite geladene URLs überprüfen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="de" >}}) 
- [Prüfe Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="de" >}})
- [Prüfe W3C-Metriken]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="de" >}})
- [Prüfe Konsoleninhalt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="de" >}})
- [Prüfe Seitenerreichbarkeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="de" >}}) 
- [Prüfe komplette Laufzeit]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}})
{{< /tableformatter >}} |

Beachte, dass ein [Multi-step API (MSA)-Prüfobjekt]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) Fehler auf andere Art feststellt. Der Einsatz von **Assertions** ermöglicht, Prüfungen zu definieren, um zu bestätigen, dass die API-Antwort den Erwartungen entspricht. Mehr erfährst du unter [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="de" >}}).

## Eine Fehlerbedingung einrichten {id="configure-error-condition"}

Du kannst Fehlerbedingungen hinzufügen, wenn du [ein Prüfobjekt von Grund auf einrichtest]({{< ref path="support/kb/basics/adding-monitors" lang="de" >}}) oder wenn du ein bestehendes Prüfobjekt bearbeitest.

Um Fehlerbedingungen einzurichten:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf das Prüfobjekt, bei dem du eine Fehlerbedingung hinzufügen möchtest.
3. Wechsle zum Tab {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}}.
4. Klicke auf die Fehlerbedingung, um den Bereich einzublenden und die Prüfobjekteinstellungen zu konfigurieren.
5. (Optional) Füge eine neue Fehlerbedingung hinzu, indem du auf {{< AppElement type="buttonSecondary" >}} \+Neue Prüfung {{< /AppElement >}} klickst.
6. Setze die Konfiguration von Bedingungen fort.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Um benachrichtigt zu werden, wenn die Fehlerbedingung erfüllt wird, [erstelle eine Meldedefinition]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="de" >}}).

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen](/img/content/gif-set-up-error-condition.gif)