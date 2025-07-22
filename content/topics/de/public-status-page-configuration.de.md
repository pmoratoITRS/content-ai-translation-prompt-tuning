{
  "hero": {
    "title": "Public Status Pages einrichten"
  },
  "title": "Public Status Pages einrichten",
  "summary": "Dieser Artikel beschreibt, wie du eine neue Public Status Page erstellst und konfigurierst.",
  "url": "/support/kb/dashboards-und-berichte/statusseiten/public-status-page-konfiguration",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration"
}


## Eine Public Status Page erstellen

1. Gehe zu {{< AppElement type="menuitem" >}} Accounteinstellungen > Public Status Pages {{< /AppElement >}}.
2. Du siehst eine Liste deiner aktuellen Public Status Pages. Standardmäßig ist in deinem Account eine Statusseite vorkonfiguriert.
3. Klicke oben rechts auf {{< AppElement type="button" >}}Public Status Page hinzufügen {{< /AppElement >}}.
4. Gib einen bedeutsamen *Namen* für die neue Statusseite ein.
5. Die *URL* wird erzeugt und ist sichtbar, sobald du die Statusseite gespeichert hast. Diese URL wird benötigt, um die [Statusseite in eine Webseite einzubetten]({{< ref path="#embedding-status-page" lang="de" >}}).
6. Aktiviere die Option *Publish*, um deine Public Status Page unter der im Feld *URL* angezeigten URL verfügbar zu machen. Die Seite kann dann ohne Uptrends Anmeldedaten aufgerufen werden.
7. Wechsle dann zur Registerkarte {{< AppElement type="tab" >}}Daten{{< /AppElement >}}.
8. Konfiguriere den **Zeitraum**, für den die Daten abgerufen und öffentlich angezeigt werden sollen.
9. Gib die **SLA** ([Service Level Agreement]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="de" >}})) an. Die Daten deiner Public Status Page basieren auf der ausgewählten SLA.
10. Füge die Prüfobjekte oder Prüfobjektgruppen hinzu, für die du Daten auf der Statusseite anzeigen möchtest.
11. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

Du hast nun deine Public Status Page konfiguriert und wirst zur Hauptliste der Public Status Pages weitergeleitet, wo deine neue Public Status Page aufgeführt wird. Um eine Vorschau veröffentlichter Seiten zu sehen, klicke auf die Preview-Links.

Wenn du weitere Unterstützung benötigen solltest, zögere bitte nicht, ein [Support-Ticket einzureichen]({{< ref path="contact" lang="de" >}}).

## Deine Public Status Page in eine Webseite einbetten {id="embedding-status-page"}

Das Einbetten einer Public Status Page auf deiner Website ist einfach.
1. Wechsle bei den Einstellungen zur Registerkarte {{< AppElement type="tab" >}}Customization{{< /AppElement >}} der Public Status Page.
2. Kopiere den Wert unter *Embed Code*. Er sieht diesem ähnlich: `<iframe src="your public status page URL here">  </iframe>`.
3. Füge den *Embed Code* in den Quelltext deiner Webseite ein.
4. Speichere und aktualisiere die Seite, um das Ergebnis zu sehen.

## Public Status Pages anpassen {id="customize"}

Es gibt eine Reihe von Dingen, die du ändern kannst, um das Erscheinungsbild deiner Public Status Pages anzupassen.
Wechsle zur Registerkarte {{< AppElement type="tab" >}} Customization {{< /AppElement >}} bei den Einstellungen deiner Public Status Page, um die Einstellungen für Farbe, Logo, Titel, Kommentar, Reihenfolge usw. zu ändern.

![Screenshot Registerkarte Customization bei Public Status Page](/img/content/scr_public-status-pages-customization.min.png)

### Kommentare nutzen {id="comments"}

Wenn du deine Kunden über aktuelle Ereignisse informieren und diese auf deinen Public Status Pages veröffentlichen möchtest, gib einen Statusbericht oder eine Mitteilung in das Kommentarfeld ein.

Die Felder **Kommentar Titel** und **Kommentar Text** findest du auf der Registerkarte {{< AppElement type="tab" >}} Customization {{< /AppElement >}}.

Sobald du Titel und Text eingegeben hast, werden diese zwischen Überschriftsfeld und Inhalt deiner Public Status Page angezeigt.

![](/img/content/scr-public-status-pages-comments-front.min.png)

{{< callout >}}**Tipp**: Wenn du deine Nachricht hervorheben möchtest, kopiere ein Emoji wie „Warnung“, „Rufzeichen“ oder „Alarm“ und füge es in das Textfeld deiner Meldung ein.{{< /callout >}}

### Automatisches Neuladen der Seite

Wenn die Seite sich automatisch aktualisieren soll, aktiviere die Einstellung **Auto refresh** auf der Registerkarte {{< AppElement type="tab" >}} Customization {{< /AppElement >}} bei deiner Public Status Page. Die Seite lädt alle 30 Sekunden neu. Die automatische Aktualisierung ist standardmäßig deaktiviert.

### Logo ändern 

Um das Logo deiner Seite zu ändern, musst du zunächst ein [Support-Ticket]({{< ref path="contact" lang="de" >}}) einreichen, das eine 210 X 40 Pixel große PNG- oder JPG-Bilddatei enthält. Beachte, dass größere Bilder angepasst werden. Unser Support fügt dann die Datei deinem Account hinzu, sodass du das vorhandene Logo von Uptrends auf deiner Seite ersetzen kannst.

### Alternative Prüfobjektnamen {id="alternative-monitor-names"}

Die Prüfobjektnamen, die du intern nutzt, sind eventuell nicht so vielsagend für ein externes Publikum. Vielleicht möchtest du auch einfach die innerhalb deines Unternehmens verwendeten Prüfobjektnamen nicht veröffentlichen. In diesem Fall kannst du abweichende Prüfobjektnamen verwenden. Diese werden mit einem benutzerdefinierten Feld mit identischem Namen für die Public Status Page und die Prüfobjekte festgelegt.

Einen abweichenden Prüfobjektnamen festlegen:

1. Gehe zu {{< AppElement type="menuitem" >}} Accounteinstellungen > Public Status Pages {{< /AppElement >}}.
2. Rufe die Einstellungen der Public Status Page auf, für die du einen abweichenden Prüfobjektnamen eingeben möchtest.
3. Wechsle zur Registerkarte {{< AppElement type="tab" >}}Customization{{< /AppElement >}} der Public Status Page.
4. Gib einen benutzerdefinierten Feldnamen im *Feld für individuelle Prüfobjektnamen* ein, z. B. `MyMonitorName`.
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.
6. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
7. Öffne die Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}}.
8. Im Abschnitt **Metadaten** kannst du ein benutzerdefiniertes Feld mit dem Namen hinzufügen, den du bei der Public Status Page verwendet hast, z. B. `MyMonitorName`, und einen Wert eingeben. Dieser Wert ist der alternative Prüfobjektname, der auf der Public Status Page angezeigt wird.
9. Klicke auf die {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}-Schaltfläche.
10. Wiederhole die Schritte 6 bis 9 für alle Prüfobjekte, die einen abweichenden Namen auf der Public Status Page haben sollen.

Hast du mehrere Public Status Pages, bei denen abweichende Prüfobjektnamen angezeigt werden sollen, wiederhole die Schritte 1 bis 5 für diese Seiten.
