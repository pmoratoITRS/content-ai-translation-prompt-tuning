{
  "hero": {
    "title": "Multi-step Monitoring – Handhabung von Redirects"
  },
  "title": "Multi-step Monitoring – Handhabung von Redirects",
  "summary": "Erfahre, wie du Weiterleitungen bei deinen Multi-step API-Prüfobjekten handhabst.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-redirects"
}

HTTP Redirects erlauben einem Webserver, den Besucher (den HTTP Client) an eine andere URL weiterzuleiten, als ursprünglich angefragt war. Das erfolgt durch Rückgabe eines Statuscodes aus der 3xx-Reihe, zusammen mit der neuen URL, die vom Client angefragt werden sollte. Diese neue URL wird im HTTP-Antwort-Header als Location zurückgegeben.

Ursprüngliche Anfrage und Antwort:

`GET /p/P12345 HTTP/1.1` `HTTP/1.1 302 Redirect  Location: /ProductInfo?productId=P12345`

Anfrage an die neue Location:

`GET /ProductInfo?productId=P12345 HTTP/1.1` `HTTP/1.1 200 OK`

## Überprüfung von Weiterleitungen beim Multi-Step API Monitoring

Bei einem [Multi-step API Monitoring]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) werden Weiterleitungen wie diese automatisch gefolgt. Du musst dir keine Gedanken über die Funktionsweise machen, wie deine API oder Webanwendung eingehende Anfragen behandelt. Konzentriere dich einfach auf die Auswertung der Ergebnisse. Wenn ein Schritt eine URL anfragt, die von deinem Server weitergeleitet wird, führen wir die zweite Anfrage als Teil desselben Schritts aus. Du kannst das Ergebnis der zweiten Anfrage behandeln, als hätte keine Weiterleitung dazwischengelegen. Wenn die zweite Anfrage auch eine Weiterleitung zurückgibt, werden wir dieser ebenfalls folgen, bis zu einer Höchstgrenze von 50 aufeinanderfolgenden Weiterleitungen. In jedem Fall erhältst du die Antwortinhalte und Header, die mit der letzten Anfrage übereinstimmen.

In einigen Fällen kann das automatische Folgen der Weiterleitungen nicht das sein, was du brauchst. Wenn du beispielsweise das Weiterleiten an sich überwachen möchtest (Überprüfung des Statuscodes, des Inhalts des Location Headers, ob ein Cookie zurückgegeben wird oder Prüfen eines anderen Werts), möchtest du diese Werte erhalten, statt die zweite Anfrage sofort auszuführen.

Wenn du eine Assertion einsetzt und angibst, dass der HTTP-Statuscode gleich 301, 302, 303, 307 oder 308 sein soll, werden wir der Weiterleitung nicht folgen. Stattdessen erhältst du direkten Zugang zu dieser Antwort. Dann kannst du diese zusätzlichen Assertions und Variablen im gleichen Schritt verwenden, um mit dieser Antwort zu arbeiten. Zum Beispiel:

### Assertions

{{< Code/Symbol type="source" >}}Statuscode{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Ist identisch mit{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}302{{< /Code/Symbol >}}

{{< Code/Symbol type="source" >}}Response Header{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Location{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Beinhaltet{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}productId=P12345{{< /Code/Symbol >}}

![MSA-Weiterleitung](/img/content/scr-MSA-redirect-check.min.png)

## Der Weiterleitung manuell folgen

Da wir mit einer mehrstufigen Einrichtung arbeiten, können wir die Weiterleitung immer noch manuell ausführen, nachdem wir sie geprüft und optional Werte erfasst haben. Füge einfach einen weiteren Schritt hinzu und gib die neue Location als URL ein.

Dazu kannst du den Wert des Location Headers erfassen, ihn in einer Variablen speichern (zum Beispiel {{< Code/Symbol type="variable" >}}{{location-value}}{{< /Code/Symbol >}}) und die Variable in der URL des nächsten Schritts verwenden. Das kann sich jedoch als knifflig erweisen: Der Wert des Location Headers ist wahrscheinlich eine relative URL, d. h. sie enthält keinen Domainnamen. Wenn du dies manuell einrichtest, musst du das ausgleichen, indem du den Domainnamen in die neue URL einfügst:

`GET https://myapi.example.com/{{location-value}}`

Das ist ein Weg. Wir können es jedoch für dich vereinfachen: Wann immer wir einen Location Header in einer HTTP-Antwort erkennen, werden wir den Wert in eine absolute URL konvertieren (einschließlich des Domainnamens der Originalanfrage) und sie in eine automatische Variable namens {{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}} einsetzen.  Diese Variable kann im nächsten Schritt verwendet werden:

`GET {{@RedirectUrl}}`

## Erfassung von Parametern aus einer Redirect URL

In einigen Fällen möchte man den Weiterleitungs-URLs überhaupt nicht folgen, aber stattdessen einen Parameterwert aus ihnen erfassen. Nehmen wir an, wir haben diesen Antwort-Header in der ursprünglichen Antwort erhalten:

`Location: https://your.clientapp.com/auth?clientId=12345&code=SGV5LCB5b3UgZm91bmQgdGhpcyEgV2VsbCBkb25lIQ==`

Was also, wenn du nicht dieser URL folgen möchtest, aber den Code-Parameterwert nutzen möchtest, der von deinem Server zurückgegeben wurde. Kein Problem: Wir erfassen URL-Parameter aus Location Header automatisch und schreiben sie in automatische Variablen, die du an anderer Stelle verwenden kannst. Das Namensschema für diese automatischen Variablen lautet {{< Code/Symbol type="variable" >}}{{@RedirectUrl.&lt;parameter-name&gt;}}{{< /Code/Symbol >}}. In diesem Fall hast du Zugriff auf {{< Code/Symbol type="variable" >}}{{@RedirectUrl.clientId}}{{< /Code/Symbol >}} und {{< Code/Symbol type="variable" >}}{{@RedirectUrl.code}}{{< /Code/Symbol >}}.
