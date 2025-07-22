{
  "hero": {
    "title": "Öffentliche und geschützte Statusseiten"
  },
  "title": "Öffentliche und geschützte Statusseiten",
  "summary": "Überblick über Public Status Pages und Einrichtung einer geschützten Statusseite für eine eingeschränkte Sichtbarkeit.",
  "url": "/support/kb/dashboards-und-berichte/statusseiten/oeffentliche-und-geschuetzte-statusseiten",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages"
}

## Öffentliche Statusseiten

Eine öffentliche Statusseite – Public Status Page – ermöglicht das Veröffentlichen von Verfügbarkeitsdaten, die von den Prüfobjekten erfasst wurden. Auf diese Weise kann die allgemeine Öffentlichkeit aktuelle Informationen zur Verfügbarkeit deiner Websites und Services sehen. Du kannst steuern, welche Prüfobjekte in deiner Statusseite enthalten sein sollen. Du kannst zudem auch das Look-and-feel der Seite ändern, sodass sie dem Stil deiner Marke entspricht.
Technisch gesehen ist eine öffentliche Statusseite ein spezialisiertes Website-Monitoring-Dashboard, anhand dessen der Verfügbarkeitsstatus einer überwachten Website, eines Webservice oder eines Servers öffentlich präsentiert wird.

Die Public Status Page zeigt den aktuellen Status des Prüfobjekts (farbcodiert zu Beginn jeder Zeile) und den SLA-Status (Symbol in der Tabelle):

![Screenshot Übersicht Public Status Page](/img/content/scr_public-status-page-overview.min.png)

Möchtest du dies detaillierter betrachten und die Verfügbarkeitsdaten eines Prüfobjekts anzeigen, klicke auf die Zeile des entsprechenden Prüfobjekts:

![Screenshot Details Public Status Page](/img/content/scr_public-status-page-monitor-details.min.png)

### Gründe für eine Public Status Page

Lies unsere Seite [Wofür werden öffentliche Statusseiten genutzt?]({{< ref path="support/kb/dashboards-and-reporting/status-pages/why-use-public-status-pages" lang="de" >}}), um herauszufinden, ob eine Public Status Page eine gute Idee für dich ist.

### Eine Public Status Page einrichten

Erfahre mit unserem Knowledge-Base-Artikel [Public Status Pages einrichten]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration" lang="de" >}}), wie du eine Public Status Page einrichtest und konfigurierst.

## Geschützte Statusseiten

{{< callout >}} **Hinweis**: Geschützte Statusseiten sind eine Option des Enterprise-Abos. {{< /callout >}}

Möglicherweise möchtest du den Status deiner Websites und Services Personen außerhalb deines Unternehmens zugänglich machen, ohne aber die ganze Welt teilhaben zu lassen. Um eine geschützte, also Protected Status Page zu erstellen, kannst du die Funktion der Public Status Page nutzen. Für eine Protected Status Page sind Anmeldedaten erforderlich, um den Zugriff zu erhalten. Wenn eine Person außerhalb deines Unternehmens diese Anmeldedaten verwendet, wird sie nur diese Statusseite sehen. Sie kann kein anderes Dashboard aufrufen und keine Änderungen vornehmen. Da die Statusseite geschützt ist, bleibt sie für den Rest der Welt unsichtbar.

### Eine geschützte Statusseite erstellen und Einrichten von Operatoren

Der Knowledge-Base-Artikel [Eine geschützte Statusseite konfigurieren]({{< ref path="support/kb/dashboards-and-reporting/status-pages/protected-status-page-configuration" lang="en" >}}) enthält Anweisungen, wie eine neue geschützte Statusseite eingerichtet wird.

### Eine geschützte Statusseite aufrufen

Sobald der Support dir bestätigt hat, dass die Berechtigungen gesetzt sind, kannst du Personen außerhalb deines Unternehmens über die Protected Status Page in Kenntnis setzen. Es gibt für sie zwei Möglichkeiten, die Seite aufzurufen:

- Sie können die [Uptrends Anwendung](https://app.uptrends.com) aufrufen und ihre von dir erstellten Anmeldedaten eingeben. Sie sehen dann eine Liste der Protected Status Pages, auf die sie Zugriff haben.
- Du kannst ihnen den *Preview*-Link (URL) der geschützten Statusseite senden. Die URL findest du unter {{< AppElement type="menuitem" >}} Accounteinstellungen > Public Status-Pages {{< /AppElement >}} in der Spalte *Preview* neben der Seite. Diese URL kann in den Lesezeichen gespeichert werden. Bei ihrem ersten Besuch muss die Person sich anmelden.

Beachte, dass eine Protected Status Page für Administratoren (Operatoren, die Mitglied der Operator-Gruppe *Administratoren* sind) und reguläre Operatoren immer aufrufbar ist, wenn sie angemeldet sind.
