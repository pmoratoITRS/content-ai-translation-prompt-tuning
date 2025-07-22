{
  "hero": {
    "title": "Blockieren von URLs und Analytics"
  },
  "title": "Blockieren von URLs und Analytics",
  "summary": "Das Blockieren von Analytics und anderen URLs bei deinen Full Pagechecks, Real Browser und Transaktions-Monitorings.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/analytics-blockieren",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/analytics-blocking"
}

{{< callout >}}
**Hinweis**: Das Blockieren von URLs und Analytics ist nur für [Enterprise und Business Accounts]({{< ref path="/pricing" lang="en" >}}) verfügbar.
{{< /callout >}}

Full Pagecheck (FPC) und Transaktions-Monitoring laden deine Webseite zusammen mit allen Elementen der Seite in einen Browser, einschließlich Skripten für Google Analytics und anderen Elementen von Dritten. Die im Browser des Checkpoints ladende Seite wird als tatsächlicher Seitenaufruf in deinen Webanalysen erfasst. Wenn sich das Website Monitoring zu sehr verfälschend auf deine Analytics auswirkt oder es einen anderen Grund gibt, weshalb bestimmte Elemente im Browser nicht geladen werden sollen, gibt es zwei Möglichkeiten.

-   Blockieren von Google Analytics
-   Blockieren von URLs

{{< callout >}}
**Hinweis**: Keine Sorge bei den HTTP(S)-Prüfobjekten in Bezug auf deine Analysen: HTTP(S)-Checks laden die Seite nicht in einem Browser, sodass das Monitoring sowieso nicht in den Analysen auftaucht.
{{< /callout >}}

## Wie funktioniert das Blockieren von Anfragen?

Wenn du ein Wasserfall-Diagramm öffnest, siehst du immer noch die Anfrage nach dem blockierten Element. Warum? Wir können dem Browser nicht einfach sagen, diese URLs nicht zu laden. Stattdessen umgehen wir diese Anfragen, sobald wir sie sehen, und verhindern, dass sie ans Internet gehen. Google Analytics wird diese Anfragen niemals erhalten, sodass deine Analysen gesichert sind. Der Browser benötigt aber dennoch eine Antwort auf diese Anfragen. Um das normale vom Browser erwartete HTTP-Verhalten nicht zu stören, senden wir einen regulären Antwort-Header mit Status 200 OK und einem Inhalt von 512 Bytes.

## Wie wirkt sich das Blockieren von Anfragen auf meine Berichte aus?

Das Blockieren wirkt sich nicht erheblich auf die Berichte aus. Wir zeigen immer noch, wann ein Browser ein blockiertes Element heruntergeladen hätte und wir stoppen alle Anfragen, die solche Elemente generieren. Damit du siehst, dass der Check das Element blockiert hat, erscheint das Element durchgestrichen im Wasserfallbericht. Das Durchstreichen zeigt dir genau, welche Anfragen vom Check auf Grundlage deiner Blockieren-Einstellungen im Prüfobjekt abgefangen wurden.

![](/img/content/e13feb2b-6a95-479e-92aa-eea4deac6169.png)

## Was wird beim Blockieren von Google Analytics blockiert?

Google bietet eine Suite mit Services, die mehr als Analysen enthalten. Daher blockiert Uptrends die üblichsten Google-Elemente. Wenn du aktivierst, dass Google Analytics blockiert werden soll, blockiert Uptrends:

-   google-analytics.com
-   stats.g.doubleclick.net
-   googleadservices.com
-   google.com/ads

Uptrends **blockiert nicht** googletagmanager.com, sodass keine Seiten gestört werden, bei denen es eine Abhängigkeit zu der Funktion dieses Elements gibt.

## Wie blockiere ich Google Analytics?

Da so viele Seiten Google Analytics nutzen, haben wir ein Kontrollkästchen in den Prüfobjekteinstellungen integriert.

1.  Rufe die Prüfobjekteinstellungen auf.
2.  Klicke auf die Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.
3.  Aktiviere das Kontrollkästchen **Google Analytics blockieren**.
4.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.

Das war's schon! Fertig. Solltest du andere Elemente blockieren wollen, lies bitte weiter.

## Wie blockiere ich URLs und andere Elemente?

Du möchtest eventuell eine URL aus unterschiedlichen Gründen bei der Durchführung eines A/B-Tests blockieren. Mit Uptrends Monitoring kannst du so viele Elemente blockieren, wie es erforderlich ist.

1.  Rufe die Prüfobjekteinstellungen auf.
2.  Klicke auf die Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.
3.  Gib die vollständige oder einen Teil der URL, die du blockieren möchtest, in das Feld **URL/Bestandteile blockieren** ein.
4.  Gib jede URL in eine separate Zeile ein.
5.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.

Wenn ein Checkpoint eine ausgehende Anfrage verzeichnet, die eine in dem Feld genannte URL oder Zeichenfolge enthält, wird der Checkpoint die Anfrage blockieren. Solltest du weitere Unterstützung zum Thema Blockieren eines Elements benötigen, [wende dich an unsere Experten]({{< ref path="contact" lang="de" >}})!

{{< callout >}}
**Hinweis**: Das Blockieren kann eventuell die Webseite stören und unnötige Warnmeldungen erzeugen. [Lass uns wissen](/contact), wenn du Hilfe benötigst.
{{< /callout >}}
