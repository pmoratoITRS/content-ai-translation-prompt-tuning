{
  "hero": {
    "title": "Multi-step Monitoring – Handhabung von Redirects"
  },
  "title": "Multi-step Monitoring – Handhabung von Redirects",
  "summary": "Erfahre, wie du Weiterleitungen bei deinen Multi-step API-Prüfobjekten handhabst.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-redirects",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

HTTP Redirects erlauben einem Webserver, den Besucher (den HTTP Client) an eine andere URL weiterzuleiten, als ursprünglich angefragt war. Das erfolgt durch Rückgabe eines Statuscodes aus der 3xx-Reihe, zusammen mit der neuen URL, die vom Client angefragt werden sollte. Diese neue URL wird im HTTP-Antwort-Header als Location zurückgegeben.

Ursprüngliche Anfrage und Antwort:

[INLINE_CODE_1] [INLINE_CODE_2]

Anfrage an die neue Location:

[INLINE_CODE_3] [INLINE_CODE_4]

## Überprüfung von Weiterleitungen beim Multi-Step API Monitoring

Bei einem [Multi-step API Monitoring]([LINK_URL_1]) werden Weiterleitungen wie diese automatisch gefolgt. Du musst dir keine Gedanken über die Funktionsweise machen, wie deine API oder Webanwendung eingehende Anfragen behandelt. Konzentriere dich einfach auf die Auswertung der Ergebnisse. Wenn ein Schritt eine URL anfragt, die von deinem Server weitergeleitet wird, führen wir die zweite Anfrage als Teil desselben Schritts aus. Du kannst das Ergebnis der zweiten Anfrage behandeln, als hätte keine Weiterleitung dazwischengelegen. Wenn die zweite Anfrage auch eine Weiterleitung zurückgibt, werden wir dieser ebenfalls folgen, bis zu einer Höchstgrenze von 50 aufeinanderfolgenden Weiterleitungen. In jedem Fall erhältst du die Antwortinhalte und Header, die mit der letzten Anfrage übereinstimmen.

In einigen Fällen kann das automatische Folgen der Weiterleitungen nicht das sein, was du brauchst. Wenn du beispielsweise das Weiterleiten an sich überwachen möchtest (Überprüfung des Statuscodes, des Inhalts des Location Headers, ob ein Cookie zurückgegeben wird oder Prüfen eines anderen Werts), möchtest du diese Werte erhalten, statt die zweite Anfrage sofort auszuführen.

Wenn du eine Assertion einsetzt und angibst, dass der HTTP-Statuscode gleich 301, 302, 303, 307 oder 308 sein soll, werden wir der Weiterleitung nicht folgen. Stattdessen erhältst du direkten Zugang zu dieser Antwort. Dann kannst du diese zusätzlichen Assertions und Variablen im gleichen Schritt verwenden, um mit dieser Antwort zu arbeiten. Zum Beispiel:

### Assertions

[SHORTCODE_1]Statuscode[SHORTCODE_2] [SHORTCODE_3]Ist identisch mit[SHORTCODE_4] [SHORTCODE_5]302[SHORTCODE_6]

[SHORTCODE_7]Response Header[SHORTCODE_8] [SHORTCODE_9]Location[SHORTCODE_10] [SHORTCODE_11]Beinhaltet[SHORTCODE_12] [SHORTCODE_13]productId=P12345[SHORTCODE_14]

![MSA-Weiterleitung]([LINK_URL_2])

## Der Weiterleitung manuell folgen

Da wir mit einer mehrstufigen Einrichtung arbeiten, können wir die Weiterleitung immer noch manuell ausführen, nachdem wir sie geprüft und optional Werte erfasst haben. Füge einfach einen weiteren Schritt hinzu und gib die neue Location als URL ein.

Dazu kannst du den Wert des Location Headers erfassen, ihn in einer Variablen speichern (zum Beispiel [SHORTCODE_15]{{location-value}}[SHORTCODE_16]) und die Variable in der URL des nächsten Schritts verwenden. Das kann sich jedoch als knifflig erweisen: Der Wert des Location Headers ist wahrscheinlich eine relative URL, d. h. sie enthält keinen Domainnamen. Wenn du dies manuell einrichtest, musst du das ausgleichen, indem du den Domainnamen in die neue URL einfügst:

[INLINE_CODE_5]

Das ist ein Weg. Wir können es jedoch für dich vereinfachen: Wann immer wir einen Location Header in einer HTTP-Antwort erkennen, werden wir den Wert in eine absolute URL konvertieren (einschließlich des Domainnamens der Originalanfrage) und sie in eine automatische Variable namens [SHORTCODE_17][SYSTEM_VAR_1][SHORTCODE_18] einsetzen.  Diese Variable kann im nächsten Schritt verwendet werden:

[INLINE_CODE_6]

## Erfassung von Parametern aus einer Redirect URL

In einigen Fällen möchte man den Weiterleitungs-URLs überhaupt nicht folgen, aber stattdessen einen Parameterwert aus ihnen erfassen. Nehmen wir an, wir haben diesen Antwort-Header in der ursprünglichen Antwort erhalten:

[INLINE_CODE_7]

Was also, wenn du nicht dieser URL folgen möchtest, aber den Code-Parameterwert nutzen möchtest, der von deinem Server zurückgegeben wurde. Kein Problem: Wir erfassen URL-Parameter aus Location Header automatisch und schreiben sie in automatische Variablen, die du an anderer Stelle verwenden kannst. Das Namensschema für diese automatischen Variablen lautet [SHORTCODE_19][SYSTEM_VAR_3][SHORTCODE_20]. In diesem Fall hast du Zugriff auf [SHORTCODE_21][SYSTEM_VAR_4][SHORTCODE_22] und [SHORTCODE_23][SYSTEM_VAR_5][SHORTCODE_24].
