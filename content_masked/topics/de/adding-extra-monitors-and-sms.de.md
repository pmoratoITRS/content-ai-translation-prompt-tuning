{
  "hero": {
    "title": "Weitere Prüfobjekte und Credits hinzufügen"
  },
  "title": "Weitere Prüfobjekte und Credits hinzufügen",
  "summary": "Wenn du zusätzliche Prüfobjekte, API-Credits, Transaktions-Credits oder Benachrichtigungs-Credits benötigst, kannst du uns anrufen oder sie über deinen Uptrends Account kaufen.",
  "url": "[URL_BASE_TOPICS]account/bezahlung-und-abonnements/extra-pruefobjekte-und-sms-hinzufuegen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Credits

Uptrends verwendet Credits, um den [Preis]([LINK_URL_1]) unterschiedlicher Monitoring-Services zu berechnen. Credits werden benötigt, um Prüfobjekte und deren Ausführung zu erstellen, zu konfigurieren und zu planen.

Jedes Synthetic-Prüfobjekt wie zum Beispiel [Uptime- oder Basic-Prüfobjekte]([LINK_URL_2]), [Browser-Prüfobjekte (Full Pagechecks bzw. FPCs) ]([LINK_URL_3]), [API-Prüfobjekte]([LINK_URL_4]) und [Transaktionsprüfobjekte]([LINK_URL_5]) hat einen eigenen Credits-Typ:

- Uptime-Prüfobjekte nutzen **Uptime-Credits**
- Browser-Prüfobjekte nutzen **Browser-Credits**
- API-Prüfobjekte nutzen **API-Credits**
- Transaktionsprüfobjekte nutzen **Transaktions-Credits**
- **Credits** – betrifft nur bestehende Accounts, die eine Einzel-Preisstufe nutzen

Die Gesamtzahl deiner Credits hängt von deinem [Prüfobjektmodus]([LINK_URL_6]) und den [Prüfobjekteinstellungen]([LINK_URL_7]) ab. Alle Prüfobjekte im Modus **Staging** oder **Produktion** nutzen Credits. Ein Prüfobjekt im Modus **Development** wird als nicht aktiv erachtet und nutzt keine Credits.

Solltest du nicht über ausreichend Prüfobjekt-Credits verfügen, kannst du ganz leicht [weitere kaufen]([LINK_URL_8]) oder Prüfobjekte einfach im [Development-Modus]([LINK_URL_9]) erstellen und ausführen.

## Credits berechnen

Um den Credit-Stand deiner gesamten Synthetic-Prüfobjekte zu sehen, gehe zu [SHORTCODE_1] Accounteinstellungen > Abonnement und Rechnungen [SHORTCODE_2]. Das Donut-Diagramm zeigt deine Credits für jeden Prüfobjekttyp:

![Prüfobjekt-Credits]([LINK_URL_10])

Wie im Bild zu sehen, hat der Nutzer fünf **Browser-Credits** oder Prüfobjekte. Zwei dieser Prüfobjekte sind derzeit aktiv, und es können noch drei weitere FPC-Prüfobjekte eingerichtet werden. Bei den **Uptime-Credits** verhält es sich ähnlich. Der Nutzer hat 10 Credits oder Uptime-Prüfobjekte. Vier dieser Prüfobjekte sind derzeit aktiv, und es können noch sechs weitere Basic-Prüfobjekte eingerichtet werden.

Bei API- und Transaktionsprüfobjekten ist die Berechnung der Credits etwas komplexer. Credits werden nicht für jedes genutzte Prüfobjekt berechnet, sondern auf Basis jeder Abfrage oder jedes Ladens einer Seite, die das Prüfobjekt prüft. 

Wenn du ein API-Prüfobjekt (Multi-Step API (MSA) oder Postman) eingerichtet hast, zählt jede HTTP-Abfrage als ein Credit. Hast du ein MSA-Prüfobjekt mit drei Schritten eingerichtet, kostet es drei Credits. Wenn du zwei MSA-Prüfobjekte mit jeweils drei Schritten erstellt hast, basiert die Gesamtzahl an Credits auf den 3 Schritten für MSA-A und den 3 Schritte für MSA-B, 6 API-Credits insgesamt.

Dies gilt auch für Transaktionsprüfobjekte: Wir zählen ein Credit für jede neue Abfrage (Laden der Seite), [jedes Wasserfalldiagramm und jeden Filmstreifen]([LINK_URL_11]). Wenn ein Transaktionsprüfobjekt über vier Seiten (neues Laden von Seiten) läuft und das Wasserfalldiagramm sowie den Filmstreifen für den ersten Schritt aktiviert hat, wird dies als 4 Seitenladungen + 1 Wasserfall + 1 Filmstreifen erfasst und ergibt insgesamt 6 Transaktions-Credits. Weitere Informationen zu den Transaktions-Credits findest du unter [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]([LINK_URL_12]).





## Credits hinzufügen

Um zusätzliche Websites, Server, Transaktionen und andere Webservices zu überwachen, gibt es zwei Möglichkeiten, weitere Credits zu kaufen.

1. **Wende dich an uns**  
    Wenn du derzeit ein Abonnement hast und sicherstellen möchtest, dass du die richtige Anzahl an zusätzlichen Prüfobjekten oder Credits zu einem wettbewerbsstarken Preis erhältst, wende dich bitte direkt an deinen Vertriebsvertreter oder [reiche ein Support-Ticket ein]([LINK_URL_13]).  

2. **Füge Credits über die Uptrends Webanwendung hinzu**
    1. Rufe [SHORTCODE_3]  Accounteinstellungen > Zusätzlich kaufen [SHORTCODE_4] auf.
    2. Du kannst die Anzahl an Uptime-, Browser-, API-, Transaktions- und Benachrichtigungs-Credits für deinen Account erhöhen.
    3. Klicke auf [SHORTCODE_5] Weiter [SHORTCODE_6].
    4. Gib deine Rechnungsinformationen ein und wähle die gewünschte **Zahlungsmethode**.
    5. Klicke auf [SHORTCODE_7] Auftrag bestätigen [SHORTCODE_8].
