{
  "hero": {
    "title": "Einrichtung des Real User Monitorings"
  },
  "title": "Einrichtung des Real User Monitorings",
  "summary": "Erfahre, wie du in wenigen, einfachen Schritten das Real User Monitoring einrichtest.",
  "url": "/support/kb/rum/einrichtung",
  "translationKey": "https://www.uptrends.com/support/kb/rum/setup"
}

Beim Real User Monitoring (RUM) werden Performance-Daten in Bezug auf die tatsächlichen Website-Besucher erfasst. Das Synthetic Monitoring von Uptrends läuft in einem berechenbaren Umfeld mit festgelegten Monitoring-Intervallen. Das Synthetic Monitoring ist gut für das Verfügbarkeits-Monitoring und Erkennen von Performance-Änderungen einer Webseite. RUM hingegen wird in weniger vorhersehbaren Umfeldern (z. B. auf den Geräten und Computern des Endbenutzers) durchgeführt und konzentriert sich mehr auf das Messen des tatsächlichen Benutzererlebnisses. Wir haben deine RUM-basierten Daten im Uptrends Account aufgenommen, sodass du sie direkt mit den Daten des Synthetic Monitorings anzeigen kannst.

## Die ersten Schritte bei Uptrends RUM

Die ersten Schritte bei RUM erfordern zwei Aktionen:
- Hinzufügen einer RUM Websitedefinition zu deinem Account
- Einfügen des Skripts in deine tatsächliche Website

### Hinzufügen einer RUM Website zu deinem Account

1. Melde dich bei deinem Uptrends Account an. Solltest du noch keinen Account haben, rufe die [Registrierungsseite]({{< ref path="signup" lang="de" >}}) auf und melde dich für eine kostenlose Testversion an.
2. Solltest du das Real User Monitoring von Uptrends noch nicht nutzen, kannst du es kostenlos mit einer RUM-Testversion ausprobieren. Klicke im Menü Apps & Extras auf die Schaltfläche *Real User Monitoring testen*.
3. Klicke auf der Seite *RUM-Testversion starten* auf {{< AppElement type="button" >}}Probiere das Real User Monitoring{{< /AppElement >}}.
4. Gib die URL der Website ein, die du überwachen möchtest. Klicke auf {{< AppElement type="button" >}} Erste RUM Webseite erstellen{{< /AppElement >}}.
5. Deine RUM-Probeversion ist jetzt eingerichtet. Klicke auf {{< AppElement type="button" >}}Anleitung anzeigen{{< /AppElement >}}, um zu den Einstellungen für deine neue RUM Website zu navigieren.

### Hinzufügen weiterer RUM Websites zu deinem Account

Nach der ersten Einrichtung enthält das Menü unter *RUM* den Bereich *Echte Nutzer*. Hier findest du die Dashboards zu RUM und kannst deine RUM Webseiten verwalten. Um weitere RUM Websites hinzuzufügen:

1. Zeige den *RUM*-Bereich im Menü an.
2. Klicke auf die *+*-Schaltfläche neben *RUM Webseiten*.
![Adding a RUM website](/img/content/scr-RUM-adding_a_RUM_website.png)
3. Gib einen *Namen* für die Website sowie die *URL* ein.
4. Wenn es sich bei deiner Website um eine Single-Page Application (SPA) handelt, aktiviere die Option *Nutze die Messung für Single Page Application*.
5. Wenn die Website URL-Fragmente nutzt (z. B. `#fragment` am Ende) und dies wichtige Teile deiner URLs sind, aktiviere die Option *URL-Fragment einschließen*. Das verhindert, dass das Real User Monitoring alles nach dem #-Symbol entfernt.
6. Wenn du alles eingerichtet hast, klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}} unten links.
7. Das Skript erscheint nun auf der Registerkarte {{< AppElement type="tab" >}}Implementierung{{< /AppElement >}}. Im nächsten Abschnitt sehen wir uns die Implementierung des Skripts an.

### Einfügen des Skripts in deine Website

Anders als beim regulären Website Monitoring musst du hierbei selbst etwas ändern. Uptrends liefert dir JavaScript-Code, das du auf deine Webseiten einfügst, die du mit RUM überwachen möchtest. Uptrends hat das Skript so entwickelt, dass es nicht mit anderen Skripten deiner Website kollidiert. Deine Endnutzer werden nicht bemerken, dass du das Uptrends RUM Skript auf deinen Seiten eingefügt hast. Die [Auswirkung unseres RUM-Skripts auf deine Website]({{< ref path="support/kb/rum/impact-of-the-rum-script-on-your-website" lang="de" >}}) liegt praktisch bei Null.

1. Stelle bitte sicher, dass du über Zugriff auf den Code deiner Website verfügst, sodass der Inhalt auf deinen Seiten geändert werden kann.
2. Rufe {{< AppElement type="menuitem" >}} RUM > Echte Nutzer > RUM Webseiten {{< /AppElement >}} auf.
3. Klicke auf die Website, die du implementieren möchtest.
4. Wechsle zur Registerkarte {{< AppElement type="tab" >}}Implementierung{{< /AppElement >}}.
5. Markiere und kopiere das [RUM-Skript]({{< ref path="/support/kb/rum/understanding-real-user-monitoring#what-does-a-rum-script-look-like" lang="de" >}}).
6. Kopiere das Script zwischen die `<head>`-Tags der Seiten, die du mit RUM überwachen möchtest. Das Skript innerhalb der `<head>`-Tags stellt sicher, dass es so früh wie möglich lädt. Das frühe Laden sorgt dafür, dass das Monitoring so viel angemessene Zeitdaten wie möglich erfasst.

- Wenn deine Website einen Content Security Policy (CSP) Response Header hat, stelle sicher, dass die Uptrends RUM Domain `https://hit.uptrendsdata.com` [hinzugefügt und korrekt](https://content-security-policy.com/) auf deiner Website eingerichtet ist. Um zu verifizieren, dass das Uptrends RUM Skript richtig funktioniert, untersuche den Quellcode deiner Website und schaue nach, ob das Uptrends RUM Skript vorhanden ist. Öffne den *Entwicklertools > Netzwerk Tab* deines Browsers und prüfe, ob die Uptrends RUM Ressourcen ohne Probleme geladen wurden.

7. Lade die Seiten mit dem Skript auf den Website-Server.
8. RUM Daten werden aufgezeichnet, sobald Besucher deine geänderte Website aufrufen. Du solltest die Daten umgehend im [RUM Übersichts-Dashboard ]({{< AppUrl >}}/Report/RumOverview) sehen können – [in Echtzeit]({{< ref path="support/kb/rum/real-time-data" lang="de" >}}).

{{< callout >}}
**Hinweis**: Wenn du die Option *Nutze die Messung für Single Page Application* für eine bestehende RUM Website aktivierst, ändert sich das Skript nach dem Speichern. Daher solltest du daran denken, dass es bei deiner Website ebenfalls aktualisiert werden muss.
{{< /callout >}}

## Lizenz

Uptrends stellt das RUM Skript und die vom Skript verwendeten Komponenten unter der BSD (Berkeley Software Distribution)-Lizenz zur Verfügung. Den vollständigen Text findest du unter <https://hit.uptrendsdata.com/license.txt>.

{{< callout >}}
**Bedenken wegen des Datenschutzes?** Unsere Seite zum [Datenschutz]({{< ref path="support/kb/rum/rum-and-user-privacy" lang="de" >}}) erklärt, wie Uptrends die Privatsphäre der Nutzer schützt, aber auch zusätzliche Schritte, die du unternehmen kannst, den Datenschutz für Nutzer zu steigern und einen Zusatz-Vorschlag zu deinem Datenschutzhinweis.
{{< /callout >}}

## Ein Skript pro Website

Beachte, dass jedes Skript speziell für eine einzelne Website erstellt wurde, da es eine `sid` enthält, die auf einzigartige Weise die zugehörige RUM Website in deinem Account identifiziert. Für jeden Seitenaufruf, den Uptrends für eine bestimmte RUM Website verzeichnet, werden wir verifizieren, dass der Seitenaufruf tatsächlich von der Website-Domain stammt, die du angegeben hast. Sehen wir uns ein Beispiel dazu an.
**Beispiel:** Nehmen wir `www.your-domain.com` als Beispiel-Website. Standardmäßig verzeichnen wir Seitenaufrufe sowohl von `www.your-domain.com` als auch von `your-domain.com`. Wenn du das Skript auf einer Website einfügst, die unter `test.your-domain.com` oder `www.your-other-domain.com` gehostet wird, wird RUM bei diesen Domains nicht funktionieren, da RUM Seitenaufrufe von anderen Domains nicht verzeichnet. Jede Website benötigt eine separate RUM Instanz, um sinnvolle Daten zu erhalten.

Wenn du Daten des Real User Monitorings für mehr als eine Website erfassen möchtest, müssen diese in Uptrends auch als getrennte RUM Websites behandelt werden. Für jede Website-Domain, die du überwachen möchtest, musst du eine weitere RUM Website einrichten, da jede Domain ein anderes Skript erhält.

Die Domain-Verifizierung bedeutet auch, dass RUM nur in deiner tatsächlichen Produktionsumgebung funktioniert. Solltest du getrennte Entwicklungs- und Testumgebungen haben, die lokal oder unter einer anderen Domain ausgeführt werden, wird RUM keine Seitenaufrufe für diese Websites verzeichnen.

{{< callout >}}
**Hinweis**: Vielleicht gibt es besondere Umstände, in denen die genau gleiche Website auf mehreren Domains läuft, die du jedoch als eine einzelne behandeln möchtest. Um dies einzurichten, [wende dich bitte an den Support]({{< ref path="contact" lang="de" >}}).
{{< /callout >}}