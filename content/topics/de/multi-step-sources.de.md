{
  "hero": {
    "title": "Multi-step Monitoring – Quellen"
  },
  "title": "Multi-step Monitoring – Quellen",
  "summary": "Das Extrahieren von Werten für Assertions oder Variablenzuordnungen bei der Einrichtung eines Multi-step API Monitorings.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-quellen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-sources",
  "TableOfContents": true
}

Um bei deinem Multi-Step API-Prüfobjekt eine [Assertion zur Inhaltsprüfung]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="en" >}}) einzurichten oder um einen [Wert zu extrahieren und als Variable zu speichern]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}), musst du angeben, nach welchem Wert gesucht werden soll. Es gibt die folgenden Optionen als Quelle:

## Response Body als JSON
Wähle diese Option, wenn der Inhalt der Antwort JSON-Daten enthält und du ein bestimmtes Element in der JSON-Struktur untersuchen oder aufzeichnen möchtest. Gib im Feld für Merkmal der Assertion oder Variablen an, welches JSON-Element wir untersuchen sollen.

### Beispiele
Nehmen wir an, die JSON-Antwort hat folgenden Inhalt:

```json
{
  "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
  "token_type":"Bearer",
  "expires_in":86400
}
```
      

Um den Wert des Attributs **access_token** aufzuzeichnen, gib {{< Code/Symbol type="property" >}}access_token{{< /Code/Symbol >}} als Merkmal an.

Wenn das Objekt mit dem Schlüssel **access_token** das **Child** bzw. untergeordnete Objekt eines anderen JSON Objekts ist, gib den kompletten „Pfad“ an. Zum Beispiel:

```json
{
   "response":{
      "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
      "token_type":"Bearer",
      "expires_in":86400
   }
}
```

Hier kann auf access_token zugegriffen werden, indem {{< Code/Symbol type="property" >}}response.access_token{{< /Code/Symbol >}} als Merkmal eingegeben wird.


Ein anderes JSON-Beispiel: Nehmen wir an, deine JSON-Daten enthalten ein **Array** eines oder mehrerer Elemente, in diesem Fall eine Reihe von drei Produkten:

```json
[
  {
    "Name": "Alpha Cygnus IX",
    "Price": 20000,
  },
  {
    "Name": "Norcadia Prime",
    "Price": 25000,
  },
  {
    "Name": "Risa", 
    "Price": 37500,
  }
]
```

Um ein Attribut eines dieser Produkte zu erhalten, müssen wir zunächst auf ein besonderes Element der Reihe durch Bereitstellen eines Index zeigen. Der Index des ersten Elements in einem JSON-Array ist immer Null: `[0]`. Um also das Attribut „Price“ des ersten Produkts in unserem Array zu erfassen, würden wir {{< Code/Symbol type="property" >}}[0].Price{{< /Code/Symbol >}} angeben, was den Wert „20000“ zum Ergebnis hat.

Wenn dein JSON ein Array als Child eines anderen Objekts enthält, musst du jeden „Schritt“ angeben, einschließlich des Index für das Element in dem Array. Nehmen wir an, dein JSON enthält etwas wie das Folgende:

```json
{
   "Destinations":[
      {
         "Name":"Alpha Cygnus IX",
         "Price":20000
      },
      {
         "Name":"Norcadia Prime",
         "Price":25000
      },
      {
         "Name":"Risa",
         "Price":37500
      }
   ]
}
```

In diesem Fall kann der Wert beim ersten `Name` als {{< Code/Symbol type="property" >}}Destinations.[0].Name{{< /Code/Symbol >}} (der Wert bei **Name** im ersten Element des Arrays **Destinations**) erfasst werden, was „Alpha Cygnus IX“ ausgeben würde.


{{< callout >}}**Hinweis**: Wenn der Antwortinhalt nicht als JSON geparst werden kann, wird diese Funktion einen Fehler erzeugen.{{< /callout >}}

## Response Body als XML
Wenn der Inhalt der Antwort ein XML-Dokument enthält, wähle diese Option und bestimme eine XPath-Abfrage, um einzugrenzen, welcher Inhalt untersucht oder aufgezeichnet werden soll.

### Beispiel

Nehmen wir an, die XML-Antwort hat folgenden Inhalt:

```xml
<AuthInfo> 
  <access_token>MjAxNy0xMC0wMlQxMDowOTo1My45MDUxNjEyWg==</access_token> 
  <expires_in>86400</expires_in> 
  <token_type>Bearer</token_type> 
</AuthInfo>
```
      
      

Um den inneren Wert des Knotens **access_token** aufzuzeichnen, gib die XPath-Abfrage {{< Code/Symbol type="property" >}}/AuthInfo/access_token/text(){{< /Code/Symbol >}} als Merkmal an.

Weitere Informationen findest du unter [mehr XPath-Beispiele, darunter SOAP XML]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="de" >}}).

Wenn der Antwortinhalt nicht als eigenständiges XML-Dokument geparst werden kann, wenn die XPath-Anfrage ungültig ist oder keinen tatsächlichen Wert aus dem Dokument wählen kann, wird eine Fehlermeldung erzeugt.

## Response Body als Text

Wenn der Antwortinhalt weder JSON noch XML (zum Beispiel unformatierter Text, HTML oder ein proprietäres Format) ist, kannst du diese Option verwenden, um den Inhalt zu durchsuchen. Standardmäßig betrachten wir den gesamten Inhalt der Antwort. Dies reicht aus, wenn du einen einfachen „Beinhaltet“-Abgleich durchführen möchtest. (Zum Beispiel: Die Antwort muss die Phrase „Price“ enthalten. Der Test ist erfolgreich, solang das Wort „Price“ irgendwo im Inhalt erscheint.) Um den gesamten Inhalt für den Prüfpunkt oder als Variablendefinition zu verwenden, sollte das Merkmalfeld frei bleiben.

Wenn du jedoch Inhalt von einer bestimmten Stelle im Dokument extrahieren möchtest, musst du auf irgendeine Weise definieren, welcher Teil des Inhalts dafür infrage kommt. Dafür gibst du einen regulären Ausdruck im Merkmalfeld an. Anhand des Musterabgleichs mit regulären Ausdrücken versuchen wir, den Regex zuzuweisen und verwenden den ersten Abgleich, um den Wert aus dem Inhalt zu erfassen.

Wenn der reguläre Ausdruck eine sogenannte Erfassung einer Gruppe (anhand derer du ein inneres Muster innerhalb des regulären Ausdrucks definieren kannst) enthält, verwenden wir die erste Übereinstimmung für diese Erfassungsgruppe.

Bitte beachte, dass diese Optionen nur für Textinhalte gelten (obwohl sie auch auf Antworten mit JSON oder XML angewendet werden können, da diese auch als Text gelten). Das Durchsuchen binärer Inhalte wird nicht unterstützt.

## Status Code

Diese Option untersucht den numerischen HTTP-Statuscode, der Teil jeder HTTP-Antwort ist. In den meisten Fällen wird man einfach prüfen wollen, dass der Status 200 lautet (was OK bedeutet) oder zumindest keinen Fehlercode darstellt. Tatsächlich ist dies eine Standardüberprüfung: Wenn du keine Assertion für Statuscode angibst, werden wir die folgende Prüfung automatisch ausführen, da 4xx und 5xx Codes in der Regel Fehlercodes sind:

`Status code` {{< Code/Symbol type="comparison" >}}Ist kleiner als{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}400{{< /Code/Symbol >}}

Wenn du jedoch eine Assertion für den Statuscode definierst, wird dies unseren Standardtest außer Kraft setzen. Wenn du beispielsweise

`Status code` {{< Code/Symbol type="comparison" >}}Ist identisch mit{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}200{{< /Code/Symbol >}}

definierst, werden wir genau diese Bedingung prüfen.

{{< callout >}}**Hinweis**: Asssertions mit Statuscode 301, 302, 303, 307 oder 308 (d. h. ein Weiterleitungscode) sind ein Sonderfall. Weitere Informationen findest du im Abschnitt [Handhabung von Redirects]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="de" >}}).{{< /callout >}}

## Status Beschreibung

Diese Option untersucht die Textbeschreibung des HTTP-Statuscodes (zuvor Reason-Phrase genannt). Das kann nützlich sein, wenn man das Verhalten bestimmter Fehlerbedingungen der API überprüft: Damit verifizierst du, dass eine sinnvolle Statusbeschreibung zurückgegeben wird, wenn eine fehlerhafte Eingabe in deiner API erfolgt.

## Response vollständig

Diese Option gibt immer einen booleschen Wert in Bezug darauf zurück, ob eine HTTP-Anfrage vollständig ausgeführt wird. Es gibt ein „falsch“ zurück, wenn wir nicht feststellen konnten, mit welchem Server wir verbinden sollen, wenn keine Verbindung errichtet werden konnte oder wenn der Server nicht mit einer zeitgemäßen HTTP-Antwort reagiert hat. In allen anderen Fällen gibt es ein „wahr“ zurück.

Diese Option muss in den meisten Fällen nicht spezifiziert werden, da wir das automatisch prüfen: Auf Grundlage dieses Assertion-Typs werden wir einen Fehler melden, wenn wir keine HTTP-Antwort von dem Server erhalten.

`Response completed` {{< Code/Symbol type="comparison" >}}Ist identisch mit{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}true{{< /Code/Symbol >}}

In einigen Sonderfällen ist es möglich, diesen Test umzukehren: Wenn du „false“ spezifizierst, werden wir prüfen, dass eine erfolgreiche Antwort NICHT möglich ist. Das kann nützlich sein, wenn man eine Webanwendung oder eine API hat, die nur innerhalb deines Netzwerks verfügbar sein soll, selbst wenn der entsprechende Domainname öffentlich erreichbar ist. Mit dieser Prüfung verifizieren wir, dass wir die API oder Webanwendung nicht erreichen können.

## Response Header 

Diese Option ermöglicht dir, besondere HTTP-Antwort-Header zu untersuchen. Gib dazu den Namen des Headers im Merkmalfeld an.

## Cookie

Diese Option gibt den aktuellen Wert eines Cookies zurück. Gib dazu den Namen des Cookies im Merkmalfeld an. Bitte beachte, dass die von deinem Server zurückgegebenen Cookies als Session-Cookies behandelt werden: Cookie-Werte werden gespeichert, aktualisiert und zurück an den Server gegeben, während das gesamte Szenario bis zum letzten Schritt ausgeführt wird. Danach werden alle Cookies entfernt, unabhängig von den Ablaufanweisungen. Das bedeutet, dauerhafte Cookies werden im Wesentlichen als Session-Cookies behandelt.

## Umfang des Inhalts

Diese Option verzeichnet die Größe (in Bytes) des Antwortinhalts. Bitte beachte, dass dies die tatsächliche Länge des Inhalts ist, nachdem der Antwortinhalt dekomprimiert wurde (sofern dein Server ihn zuvor komprimiert hatte).

## Dauer
Diese Option gibt die Gesamtzeit (in Millisekunden) an, die benötigt wurde, um die Anfrage auszuführen und eine Antwort zu erhalten. Damit kannst du die Performance für einzelne Schritte überwachen.
