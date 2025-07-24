{
  "hero": {
    "title": "A/B-Tests bei Transaktionsanfragen ausschließen"
  },
  "title": "A/B-Tests bei Transaktionsanfragen ausschließen",
  "summary": "A/B-Tests können Fehler verursachen und unnötige Warnmeldungen auslösen. Sie können unerwünschte Alarme verhindern, indem Sie Uptrends mitteilen, Anfragen an die URL Ihres A/B-Test-Tools auszuschließen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/a-b-tests-bei-transaktionsanfragen-ausschliessen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

A/B-Testtools teilen den Traffic auf Ihrer Webseite, indem Sie eine Nutzergruppe nach Version A und die andere Nutzergruppe nach Version B der Webseite leiten. Das Transaktions-Monitoring kann aufgrund des A/B-Testens Fehler melden, wenn die Seiten unterschiedliche Inhalte aufweisen. Wenn Sie zum Beispiel einer Schaltfläche in Version A das Label "Zum Einkaufskorb hinzufügen" geben und die gleiche Schaltfläche in Version B das Label "Zum Einkaufswagen hinzufügen" hat, werden Sie Fehlermeldungen erhalten, wenn die Ausführung des Scripts sich auf das Finden des Texts "Zum Einkaufskorb hinzufügen" stützt. Wenn das Script beim Transaktions-Monitoring sich also auf das Auffinden eines Elements stützt, das nur bei Version A Ihrer Seite vorhanden ist, ergibt das Script für Version B einen Fehler. Dies können Sie umgehen, indem Sie die URL für Ihr A/B-Testtool von den Anfragen ausschließen, die das Prüfobjekt von Uptrends an Ihre Website sendet.

[SHORTCODE_1]
**Hinweis:** Dies gilt natürlich auch für das Prüfobjekt Full Page Check, wenn Sie eine Überprüfung auf spezielle Inhalte durchführen und diese Inhalte sich während eines A/B-Tests ändern.
[SHORTCODE_2]

## URLs für A/B-Testtools ausschließen

Zum Ausschließen von URLs für A/B-Testtools

1.  Melden Sie sich bei Ihrem Uptrends Account an.
2.  Klicken Sie auf **Prüfobjekte** im Drop-down-Menü [SHORTCODE_5]*Prüfobjekt*[SHORTCODE_6].
3.  Klicken Sie auf das Prüfobjekt, um die Informationen zum Prüfobjekt anzuzeigen.
4.  Klicken Sie auf die Registerkarte [SHORTCODE_7]Erweitert[SHORTCODE_8].
5.  Suchen Sie das Textfeld "'Diese (Teile dieser) URLs blockieren".
6.  Geben Sie die URL des Testtools in das Feld ein. Geben Sie jede auszuschließende URL in eine separate Zeile.
7.  Klicken Sie auf [SHORTCODE_9]Speichern[SHORTCODE_10].

Das ist schon alles. Sobald Sie auszuschließende URLs eingeben, sendet Uptrends beim Monitoring Ihrer Website keine Anfragen an Ihr A/B-Testtool. Ohne die Anfragen löst Uptrends kein A/B-Testscript aus.

## Beispiel

Geben Sie die URL Ihres A/B-Testtools in das Feld "URL/Bestandteile blockieren" ein. Wenn Sie zum Beispiel Visual Website Optimizer für Ihr A/B-Testen verwenden, geben Sie visualwebsiteoptimizer.com in das Feld ein. Sollten Sie Optimizely nutzen, müsse Sie optimizely.com ausschließen.

![]([LINK_URL_1])

[SHORTCODE_3]
**Hinweis:** Obwohl wir aktiv die Anfragen seitens der ausgeschlossenen URL filtern, sind diese dennoch im Wasserfallbericht enthalten. Sie erhalten den Hinweis im Antwort-Header "X-Blocked-By-Uptrends: true."
[SHORTCODE_4]
