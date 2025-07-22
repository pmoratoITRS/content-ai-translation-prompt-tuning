{
  "hero": {
    "title": "Automatische Variablen"
  },
  "title": "Automatische Variablen",
  "summary": "Eine Liste automatischer Variablen für den Einsatz in Transaktions- und Multi-step API-Prüfobjekten",
  "url": "/support/kb/synthetic-monitoring/transaktionen/automatische-variablen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/automatic-variables"
}

Uptrends‘ [Transaktions-]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) und [Multi-Step API-]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}})Prüfobjekttypen ermöglichen dir, Abläufe über mehrere Schritte auf einer Webseite oder in direkter Interaktion mit einer API zu testen. In einigen Fällen besteht möglicherweise die Notwendigkeit, Variablendaten zu übergeben. Zum Beispiel könnte ein bestimmtes Formular bei deinen Transaktionen einen Zeitstempel erfordern oder du musst vielleicht eine eindeutige Kennung erzeugen, die in einem der API-Aufrufe verwendet wird. Uptrends unterstützt eine Reihe **automatischer Variablen**, die für dich erzeugt werden. Die meisten sind tatsächlich Funktionen, die einen Wert generieren, den du in den HTTP-Anfragen, zum Ausfüllen von Textfeldern oder zum Hinzufügen von Selektoren bei deinen Transaktionsprüfobjekten verwenden kannst.

## Generische automatische Variablen

Die folgenden automatischen Variablen stehen sowohl für das **Transaktions-** wie auch das **Multi-step API**-Monitoring bereit:

### Datum und Uhrzeit

{{< Code/Symbol type="variable" >}}{{@DateTime(format,offset)}}{{< /Code/Symbol >}}: Die Variable erzeugt dynamische Datums-/Uhrzeit-Werte, je nach von dir angegebenem Format und optionalem Offset. Datum/Zeit (ohne Offset) ist immer die aktuelle Zeit, wie sie in der UTC-Zeitzone (Coordinated Universal Time) erscheint.

Um Datum und Uhrzeit nach deinen Anforderungen zu formatieren, setze den Parameter `format` auf:
  
- einen Wert, der von der Datumsformatierung von .NET unterstützt wird, z. B. `dd/MM/yyyy` oder `MM/dd/yyyy`
- `Iso`, für das Format ISO 8601
- `Unix`, für die Unix-Epochenzeit

Der optionale Parameter `offset` kann verwendet werden, um das Datum und die Uhrzeit auf Basis einer bestimmten Abweichung (in Sekunden) oder einer Datum-/Uhrzeit-Funktion neu zu berechnen. Wenn du keinen Offset-Parameter eingibst, wird dementsprechend kein Offset angewendet. Für die Neuberechnung des Datums und der Uhrzeit, wähle zwischen den folgenden Optionen:

- Setze den Offset-Parameter auf eine positive oder negative Sekundenzahl. Die angegebene Sekundenzahl wird zum bzw. vom aktuellen Datum und der Uhrzeit addiert oder subtrahiert. Ein typisches Fallbeispiel ist die Berechnung des Datums und der Uhrzeit einer unterschiedlichen Zeitzone oder um zu einem anderen Tag vor oder nach dem aktuellen Datum und der Uhrzeit zu wechseln.

  In der folgenden Tabelle findest du einige Beispiele.

- Nutze eine Datums-/Uhrzeit-Funktion, um den ersten oder letzten Tag eines aktuellen, vorherigen oder nächsten Monats in Bezug auf das aktuelle Datum zu berechnen. Die möglichen Werte für das Offset sind:
  - `LastDayOfMonth`
  - `FirstDayOfMonth`
  - `LastDayOfPreviousMonth`
  - `FirstDayOfPreviousMonth`
  - `LastDayOfNextMonth`
  - `FirstDayOfNextMonth`

Die Tabelle unten zeigt einige Beispiele für ein angenommenes aktuelles Datum mit Uhrzeit von 24. Februar 2018 22:30 UTC.
| Ausdruck                                  | Wert                        | Beschreibung                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| `{{@DateTime(dd-MM-yyyy HH:mm)}}`           | 24-02-2018 22:30             | Jetzt, im Format dd-MM-yyyy HH:mm               |
| `{{@DateTime(dd-MM-yyyy HH:mm,-18000)}}`    | 24-02-2018 17:30             | Jetzt, als Eastern Standard Time (UTC-5)         |
| `{{@DateTime(ISO)}}`                        | 2018-02-24T22:30:00.0000000Z | Jetzt, im ISO 8.601 Format                       |
| `{{@DateTime(UNIX)}}`                       | 1.519.511.400                   | Jetzt, in Unix-Epochenzeit                       |
| `{{@DateTime(MM/dd/yyyy,-86400)}}`          | 02/23/2018                   | Gestern, im Format MM/dd/yyyy               |
| `{{@DateTime(MM/dd/yyyy,86400)}}`           | 02/25/2018                   | Morgen, im Format MM/dd/yyyy               |
| `{{@DateTime(MM/dd/yyyy,FirstDayOfMonth)}}` | 02/01/2018                   | Erster Tag dieses Monats, im Format MM/dd/yyyy |
| `{{@DateTime(MM/dd/yyyy,LastDayOfMonth)}}`  | 02/28/2018                   | Letzter Tag dieses Monats, im Format MM/dd/yyyy |

### Zufälliger einzigartiger Bezeichner

{{< Code/Symbol type="variable" >}}{{@RandomGuid}}{{< /Code/Symbol >}} : Diese Variable erzeugt einen Zufallswert in der Form `AB0AD14D-9611-41A8-9C25-7D94B895CFF1`. Du kannst diese Variable nutzen, wenn du einen zufälligen Wert in URL, POST-Daten oder HTTP-Header benötigst.  Wenn du die Variable {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} in mehreren Schritten nutzt, wird jeder Schritt einen anderen Wert erhalten. Jedes Mal, wenn das Monitoring ausgeführt wird, wird ein komplett neuer zufälliger Wert eingesetzt.
### Wiederkehrender zufälliger einzigartiger Bezeichner

{{< Code/Symbol type="variable" >}}{{@UniqueGuid}}{{< /Code/Symbol >}} : Dieser einzigartige, zufällig generierte Wert kann in der gesamten Transaktion mehrmals wiederverwendet werden. Anders als die oben erwähnte {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}}, die jedes Mal einen neuen Wert erzeugt, kannst du diese Variable verwenden, wenn du einen wiederkehrenden Wert in deiner URL, den POST Daten oder im HTTP Header einfügen musst.
Dies kann beispielsweise nützlich sein, wenn du ein Skript für eine Registrierung erstellst, bei dem die generierte E-Mail-Adresse und die bestätigte E-Mail-Adresse genau dieselbe sein müssen.### Zufällige Ganzzahl

{{< Code/Symbol type="variable" >}}{{@RandomInt(min,max)}}{{< /Code/Symbol >}}: Diese Variable erzeugt eine zufällige Ganzzahl zwischen den von dir bestimmten Minimum- und Maximum-Werten (einschließlich des Minimum- und Maximum-Werts). Wenn du zum Beispiel `{{@RandomInt(0,100)}}` spezifizierst, erzeugt diese Variable eine Zahl im Rahmen von 0 bis 100.
### Zufällige Großbuchstaben

{{< Code/Symbol type="variable" >}}{{@RandomChar(length)}}{{< /Code/Symbol >}} : Diese automatische Variable ermöglicht dir, eine zufällige Reihe alphabetischer Zeichen mit vorgegebener Länge zu erzeugen. Alle Zeichen sind Großbuchstaben. Beispielsweise erzeugt `{{@RandomChar(5)}}` einen Zufallswert in der Form von `GPLMQ`.
### Zufällige US Medicare Beneficiary Kennungen (MBI)
{{< Code/Symbol type="variable" >}}{{@RandomUSMedicare}}{{< /Code/Symbol >}} : Diese automatische Variable kannst du einsetzen, um Kennungen von US-Medicare-Leistungsberechtigten zu generieren. Die MBI ist eine Reihe von 11 alphanumerischen Zeichen. zum Beispiel`1EG4TE5MK73`. Bitte beachte, dass dieser Code ohne Bindestriche erzeugt wird. Der MBI-Ccode kann von Unternehmen aus der US-amerikanischen Gesundheitsbranche genutzt werden.

## Transaktionsspezifische (frühere) Variablen

Die folgende Reihe automatischer Variablen ist älter, können aber noch verwendet werden: Diese Variablen werden ausschließlich beim **Transaktions**-Monitoring genutzt.

### Zeitstempel

{{< Code/Symbol type="variable" >}}{timespan 0}{now dd-MM-yyyy}{{< /Code/Symbol >}}: Zu **Erzeugung und Einrichtung eines Zeitstempels** (aktuelles Datum) in einem Textfeld auf deiner Seite.

{{< Code/Symbol type="variable" >}}{timespan 1:0:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}}: Zum **Offset des Tages um 1** (morgen).

{{< Code/Symbol type="variable" >}}{timespan 0:1:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}}: So wie oben, aber **Offset um 1 Stunde**.

{{< Code/Symbol type="variable" >}}{timespan 0:0:1:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} und {{< Code/Symbol type="variable" >}}{timespan 0:0:0:1}{now dd-MM-yyyy}{{< /Code/Symbol >}}: Offset der aktuellen Zeit um eine Minute bzw. eine Sekunde.

### Zufälliger Wert aus einer Matrix

{{< Code/Symbol type="variable" >}}{random 1 2 3 4 5}{{< /Code/Symbol >}}: Setzen eines zufälligen Werts aus einer Matrix. Diese setzt einen zufälligen Wert von eins bis fünf.

{{< Code/Symbol type="variable" >}}{random apple banana orange}{{< /Code/Symbol >}}: Mit dieser Funktion wird eine Zeichenfolge aus der ausgewählten Matrix gesetzt: Es wird entweder `apple`, `banana` oder `orange` gesetzt.

## Spezifische Variablen im Multi-step API Monitoring

Die folgenden automatischen Variablen und Informationen gelten nur für das **Multi-Step API**-Prüfobjekt.

### Serveridentifizierung (ID)

{{< Code/Symbol type="variable" >}}{{@ServerId}}{{< /Code/Symbol >}}: Bei der Ausführung eines Prüfobjekts des Multi-step API Monitorings gibt diese Variable einen numerischen Wert aus, der den Standort von Uptrends‘ Checkpoint identifiziert, der diesen Test durchführt. Wenn der Test zum Beispiel von Uptrends' Checkpoint in Sydney, Australien, ausgeführt wird, gibt die Variable den Wert `30` aus. Die Liste der Checkpoint-Server und ihre zugehörigen **Server IDs** ist mithilfe der [Uptrends API]({{< ref path="support/kb/api" lang="en" >}}) über den [Checkpoint-Endpunkt](https://api.uptrends.com/v4/Checkpoint) verfügbar.

### Redirect URL

{{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}}: Falls einer der Schritte bei dem Monitoring einen Redirect-Code zurückgeben sollte und du diese Redirect-Antwort erfassen und testen möchtest, wird diese automatische Variable die URL enthalten, auf die sich die Weiterleitung bezieht, statt ihr automatisch zu folgen. Dafür musst du jedoch festlegen, Weiterleitungen nicht automatisch zu folgen, und eine Assertion (Prüfpunkt) einrichten, der auf den richtigen Redirect-Code prüft. Dieses Verfahren wird hier detaillierter erläutert: [Multi-step Monitoring – Handhabung von Redirects]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="de" >}}).

### Zufälliger Float

{{< Code/Symbol type="variable" >}}{{@RandomFloat(min,max)}}{{< /Code/Symbol >}} : Nutze diese Funktion, um eine Gleitkommazahl innerhalb der angegebenen Bandbreite (min./max.) zu erzeugen. Die Genauigkeit (die Anzahl der Ziffern nach dem Dezimalpunkt) wird von der höchsten Genauigkeit von den verwendeten Werten `min` und `max` abgeleitet.

Zum Beispiel wird `{{@RandomFloat(-1.2,3.00000)}}` einen zufälligen Float zwischen -1.2 und 3.0 mit einer Genauigkeit von 5, zum Beispiel 2.12345, erzeugen.

## Mehrfaches Verwenden eines automatisch erzeugten Werts

Einige dieser Variablen-Funktionen (insbesondere solche, die Zufalls- oder Datum-/Zeit-Werte erzeugen) werden jedes Mal neu bewertet, wenn du sie einsetzt, und erzeugen jedes Mal einen neuen Wert. Wenn du einen bestimmten Wert generieren und mehrfach in einem mehrstufigen Szenario verwenden möchtest, kannst du (wie in im Artikel [Multi-step Monitoring – Variablen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}) erläutert) eine Variable vordefinieren und eine automatische Variable als Wert nutzen.

### Beispiele vordefinierter Variablen, die automatische Variablen nutzen

| Name          | Wert                            | Einsatz                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SearchDate`  | `{{@DateTime(dd-MM-yyyy)}}`     | Ein Datums-Wert, der als Eingabe einer Suchabfrage eingesetzt wird.                                                                                                                                                                                                                           |
| `UniqueEmail` | `{{@RandomGuid}}@mycompany.com` | Ein zufälliger Guid-Wert zusammen mit festgelegtem Text, um eine E-Mail-Adresse zu erzeugen, die sich jedes Mal unterscheidet.                                                                                                                                                                |
| `OrderAmount` | `{{@RandomInt(1, 10)}}`         | Eine zufällige Zahl zwischen 1 und 10, die als zu bestellende Anzahl von Produkten verwendet wird. Bei einem nachfolgenden Aufruf kann diese Variable nochmals verwendet werden, um den Inhalt eines Einkaufswagens zu prüfen und zu bestätigen, dass dieser tatsächlich diese Menge enthält. |
