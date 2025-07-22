{
  "hero": {
    "title": "Zeitzone"
  },
  "title": "Zeitzone",
  "summary": "Die Zeitzoneneinstellung ist eine Einstellung, die sich darauf auswirkt, wie Überwachungszeiten berichtet werden, basierend auf deiner Zeitzonenauswahl.",
  "url": "/support/kb/account/einstellungen/zeitzonen",
  "translationKey": "https://www.uptrends.com/support/kb/account/timezones"
}

Die **Zeitzone** ist eine Einstellung, die sich darauf auswirkt, wie die überwachten Zeiten im Bericht angezeigt werden – basierend auf deiner Zeitzone.

Diese Einstellung wird während der Einrichtung des Uptrends Accounts vorgenommen und ist unter {{< AppElement type="menuitem" >}} Accounteinstellungen > Account Einstellungen {{< /AppElement >}} und Öffnen der Registerkarte {{< AppElement type="tab" >}} Einstellungen {{< /AppElement >}} zu finden.

Du kannst die Zeitzone selbst ändern, sofern es in deinem Uptrends Account keine erfassten Daten des Real User Monitorings (RUM) gibt. In dem Fall erscheint die Einstellung als nicht bearbeitbar und du musst dich an den [Support]({{< ref path="contact" lang="de" >}}) wenden, um Möglichkeiten zu erörtern.

{{< callout >}}
**Hinweis**: Ändern der Zeitzonen-Einstellung erzeugt entweder eine Lücke oder ein Überschneiden bei deinen Monitoring-Daten, da die Anwendung vorhandene Daten nach einer Zeitzonenänderung nicht neu berechnet.
{{< /callout >}}

## Zeitumstellung Sommer/Winter (DST)

In der Anwendung von Uptrends sind einige Zeitzonen mit einem Sternchen (*) oder dem Hash-Zeichen (#) markiert, um anzuzeigen, dass die Zeitzone einer Zeitumstellung für Sommer/Winter unterliegt.

- \* - Zeitzone liegt auf der Nordhalbkugel und unterliegt Sommer-Winter-Zeitumstellungen.
- \# - Zeitzone liegt auf der Südhalbkugel und unterliegt Sommer-Winter-Zeitumstellungen.
- In einigen Zeitzonen wird nicht auf Sommer- bzw. Winterzeit umgestellt. Daher ist ihnen kein *- oder #-Zeichen angefügt.

Wenn du die UTC-Zeiten (Universal Time Coordinated) verwenden möchtest, wähle hierfür die **UTC**-Zeitzone (ohne *-Markierung). Diese Zeitzonen-Einstellung wird nicht auf Sommer-/Winterzeit umgestellt. Bitte beachte, dass dies nicht das Gleiche wie **UTC* England, Irland** ist, welche nach Sommer-/Winterzeit umstellt.

## Zeitzonen für Operatoren

Die standardmäßige Zeitzone des Uptrends Accounts kann angepasst werden, indem du eine [zusätzliche Zeitzone]({{< ref path="support/kb/account/users/operators/main-settings#timezone" lang="de" >}}) für einzelne Operatoren eingibst. Beachte, dass diese Funktion nur für [Enterprise Accounts]({{< ref path="/pricing#plans" lang="de" >}}) verfügbar ist.
