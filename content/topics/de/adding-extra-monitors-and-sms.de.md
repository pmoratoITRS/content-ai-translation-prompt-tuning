{
  "hero": {
    "title": "Weitere Prüfobjekte und Credits hinzufügen"
  },
  "title": "Weitere Prüfobjekte und Credits hinzufügen",
  "summary": "Wenn du zusätzliche Prüfobjekte, API-Credits, Transaktions-Credits oder Benachrichtigungs-Credits benötigst, kannst du uns anrufen oder sie über deinen Uptrends Account kaufen.",
  "url": "/support/kb/account/bezahlung-und-abonnements/extra-pruefobjekte-und-sms-hinzufuegen",
  "translationKey": "https://www.uptrends.com/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms"
}

## Credits

Uptrends verwendet Credits, um den [Preis]({{< ref path="/pricing" lang="de" >}}) unterschiedlicher Monitoring-Services zu berechnen. Credits werden benötigt, um Prüfobjekte und deren Ausführung zu erstellen, zu konfigurieren und zu planen.

Jedes Synthetic-Prüfobjekt wie zum Beispiel [Uptime- oder Basic-Prüfobjekte]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="de" >}}), [Browser-Prüfobjekte (Full Pagechecks bzw. FPCs) ]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="de" >}}), [API-Prüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}) und [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) hat einen eigenen Credits-Typ:

- Uptime-Prüfobjekte nutzen **Uptime-Credits**
- Browser-Prüfobjekte nutzen **Browser-Credits**
- API-Prüfobjekte nutzen **API-Credits**
- Transaktionsprüfobjekte nutzen **Transaktions-Credits**
- **Credits** – betrifft nur bestehende Accounts, die eine Einzel-Preisstufe nutzen

Die Gesamtzahl deiner Credits hängt von deinem [Prüfobjektmodus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}) und den [Prüfobjekteinstellungen]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="de" >}}) ab. Alle Prüfobjekte im Modus **Staging** oder **Produktion** nutzen Credits. Ein Prüfobjekt im Modus **Development** wird als nicht aktiv erachtet und nutzt keine Credits.

Solltest du nicht über ausreichend Prüfobjekt-Credits verfügen, kannst du ganz leicht [weitere kaufen]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms#add-credits" lang="de" >}}) oder Prüfobjekte einfach im [Development-Modus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode#development-mode" lang="de" >}}) erstellen und ausführen.

## Credits berechnen

Um den Credit-Stand deiner gesamten Synthetic-Prüfobjekte zu sehen, gehe zu {{< AppElement type="menuitem" >}} Accounteinstellungen > Abonnement und Rechnungen {{< /AppElement >}}. Das Donut-Diagramm zeigt deine Credits für jeden Prüfobjekttyp:

![Prüfobjekt-Credits](/img/content/scr-monitor-credits.min.png)

Wie im Bild zu sehen, hat der Nutzer fünf **Browser-Credits** oder Prüfobjekte. Zwei dieser Prüfobjekte sind derzeit aktiv, und es können noch drei weitere FPC-Prüfobjekte eingerichtet werden. Bei den **Uptime-Credits** verhält es sich ähnlich. Der Nutzer hat 10 Credits oder Uptime-Prüfobjekte. Vier dieser Prüfobjekte sind derzeit aktiv, und es können noch sechs weitere Basic-Prüfobjekte eingerichtet werden.

Bei API- und Transaktionsprüfobjekten ist die Berechnung der Credits etwas komplexer. Credits werden nicht für jedes genutzte Prüfobjekt berechnet, sondern auf Basis jeder Abfrage oder jedes Ladens einer Seite, die das Prüfobjekt prüft. 

Wenn du ein API-Prüfobjekt (Multi-Step API (MSA) oder Postman) eingerichtet hast, zählt jede HTTP-Abfrage als ein Credit. Hast du ein MSA-Prüfobjekt mit drei Schritten eingerichtet, kostet es drei Credits. Wenn du zwei MSA-Prüfobjekte mit jeweils drei Schritten erstellt hast, basiert die Gesamtzahl an Credits auf den 3 Schritten für MSA-A und den 3 Schritte für MSA-B, 6 API-Credits insgesamt.

Dies gilt auch für Transaktionsprüfobjekte: Wir zählen ein Credit für jede neue Abfrage (Laden der Seite), [jedes Wasserfalldiagramm und jeden Filmstreifen]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}). Wenn ein Transaktionsprüfobjekt über vier Seiten (neues Laden von Seiten) läuft und das Wasserfalldiagramm sowie den Filmstreifen für den ersten Schritt aktiviert hat, wird dies als 4 Seitenladungen + 1 Wasserfall + 1 Filmstreifen erfasst und ergibt insgesamt 6 Transaktions-Credits. Weitere Informationen zu den Transaktions-Credits findest du unter [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="de" >}}).





## Credits hinzufügen

Um zusätzliche Websites, Server, Transaktionen und andere Webservices zu überwachen, gibt es zwei Möglichkeiten, weitere Credits zu kaufen.

1. **Wende dich an uns**  
    Wenn du derzeit ein Abonnement hast und sicherstellen möchtest, dass du die richtige Anzahl an zusätzlichen Prüfobjekten oder Credits zu einem wettbewerbsstarken Preis erhältst, wende dich bitte direkt an deinen Vertriebsvertreter oder [reiche ein Support-Ticket ein](/contact).  

2. **Füge Credits über die Uptrends Webanwendung hinzu**
    1. Rufe {{< AppElement type="menuitem" >}}  Accounteinstellungen > Zusätzlich kaufen {{< /AppElement >}} auf.
    2. Du kannst die Anzahl an Uptime-, Browser-, API-, Transaktions- und Benachrichtigungs-Credits für deinen Account erhöhen.
    3. Klicke auf {{< AppElement type="buttonPrimary" >}} Weiter {{< /AppElement >}}.
    4. Gib deine Rechnungsinformationen ein und wähle die gewünschte **Zahlungsmethode**.
    5. Klicke auf {{< AppElement type="savebutton" >}} Auftrag bestätigen {{< /AppElement >}}.
