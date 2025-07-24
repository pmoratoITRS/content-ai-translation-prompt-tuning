{
  "hero": {
    "title": "Automatische Variablen"
  },
  "title": "Automatische Variablen",
  "summary": "Eine Liste automatischer Variablen für den Einsatz in Transaktions- und Multi-step API-Prüfobjekten",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/automatische-variablen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends‘ [Transaktions-]([LINK_URL_1]) und [Multi-Step API-]([LINK_URL_2])Prüfobjekttypen ermöglichen dir, Abläufe über mehrere Schritte auf einer Webseite oder in direkter Interaktion mit einer API zu testen. In einigen Fällen besteht möglicherweise die Notwendigkeit, Variablendaten zu übergeben. Zum Beispiel könnte ein bestimmtes Formular bei deinen Transaktionen einen Zeitstempel erfordern oder du musst vielleicht eine eindeutige Kennung erzeugen, die in einem der API-Aufrufe verwendet wird. Uptrends unterstützt eine Reihe **automatischer Variablen**, die für dich erzeugt werden. Die meisten sind tatsächlich Funktionen, die einen Wert generieren, den du in den HTTP-Anfragen, zum Ausfüllen von Textfeldern oder zum Hinzufügen von Selektoren bei deinen Transaktionsprüfobjekten verwenden kannst.

## Generische automatische Variablen

Die folgenden automatischen Variablen stehen sowohl für das **Transaktions-** wie auch das **Multi-step API**-Monitoring bereit:

### Datum und Uhrzeit

[SHORTCODE_1][SYSTEM_VAR_1][SHORTCODE_2]: Die Variable erzeugt dynamische Datums-/Uhrzeit-Werte, je nach von dir angegebenem Format und optionalem Offset. Datum/Zeit (ohne Offset) ist immer die aktuelle Zeit, wie sie in der UTC-Zeitzone (Coordinated Universal Time) erscheint.

Um Datum und Uhrzeit nach deinen Anforderungen zu formatieren, setze den Parameter [INLINE_CODE_1] auf:
  
- einen Wert, der von der Datumsformatierung von .NET unterstützt wird, z. B. [INLINE_CODE_2] oder [INLINE_CODE_3]
- [INLINE_CODE_4], für das Format ISO 8601
- [INLINE_CODE_5], für die Unix-Epochenzeit

Der optionale Parameter [INLINE_CODE_6] kann verwendet werden, um das Datum und die Uhrzeit auf Basis einer bestimmten Abweichung (in Sekunden) oder einer Datum-/Uhrzeit-Funktion neu zu berechnen. Wenn du keinen Offset-Parameter eingibst, wird dementsprechend kein Offset angewendet. Für die Neuberechnung des Datums und der Uhrzeit, wähle zwischen den folgenden Optionen:

- Setze den Offset-Parameter auf eine positive oder negative Sekundenzahl. Die angegebene Sekundenzahl wird zum bzw. vom aktuellen Datum und der Uhrzeit addiert oder subtrahiert. Ein typisches Fallbeispiel ist die Berechnung des Datums und der Uhrzeit einer unterschiedlichen Zeitzone oder um zu einem anderen Tag vor oder nach dem aktuellen Datum und der Uhrzeit zu wechseln.

  In der folgenden Tabelle findest du einige Beispiele.

- Nutze eine Datums-/Uhrzeit-Funktion, um den ersten oder letzten Tag eines aktuellen, vorherigen oder nächsten Monats in Bezug auf das aktuelle Datum zu berechnen. Die möglichen Werte für das Offset sind:
  - [INLINE_CODE_7]
  - [INLINE_CODE_8]
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
  - [INLINE_CODE_11]
  - [INLINE_CODE_12]

Die Tabelle unten zeigt einige Beispiele für ein angenommenes aktuelles Datum mit Uhrzeit von 24. Februar 2018 22:30 UTC.
| Ausdruck                                  | Wert                        | Beschreibung                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| [INLINE_CODE_13]           | 24-02-2018 22:30             | Jetzt, im Format dd-MM-yyyy HH:mm               |
| [INLINE_CODE_14]    | 24-02-2018 17:30             | Jetzt, als Eastern Standard Time (UTC-5)         |
| [INLINE_CODE_15]                        | 2018-02-24T22:30:00.0000000Z | Jetzt, im ISO 8.601 Format                       |
| [INLINE_CODE_16]                       | 1.519.511.400                   | Jetzt, in Unix-Epochenzeit                       |
| [INLINE_CODE_17]          | 02/23/2018                   | Gestern, im Format MM/dd/yyyy               |
| [INLINE_CODE_18]           | 02/25/2018                   | Morgen, im Format MM/dd/yyyy               |
| [INLINE_CODE_19] | 02/01/2018                   | Erster Tag dieses Monats, im Format MM/dd/yyyy |
| [INLINE_CODE_20]  | 02/28/2018                   | Letzter Tag dieses Monats, im Format MM/dd/yyyy |

### Zufälliger einzigartiger Bezeichner

[SHORTCODE_3][SYSTEM_VAR_10][SHORTCODE_4] : Diese Variable erzeugt einen Zufallswert in der Form [INLINE_CODE_21]. Du kannst diese Variable nutzen, wenn du einen zufälligen Wert in URL, POST-Daten oder HTTP-Header benötigst.  Wenn du die Variable [SHORTCODE_5]@RandomGuid[SHORTCODE_6] in mehreren Schritten nutzt, wird jeder Schritt einen anderen Wert erhalten. Jedes Mal, wenn das Monitoring ausgeführt wird, wird ein komplett neuer zufälliger Wert eingesetzt.
### Wiederkehrender zufälliger einzigartiger Bezeichner

[SHORTCODE_7][SYSTEM_VAR_11][SHORTCODE_8] : Dieser einzigartige, zufällig generierte Wert kann in der gesamten Transaktion mehrmals wiederverwendet werden. Anders als die oben erwähnte [SHORTCODE_9]@RandomGuid[SHORTCODE_10], die jedes Mal einen neuen Wert erzeugt, kannst du diese Variable verwenden, wenn du einen wiederkehrenden Wert in deiner URL, den POST Daten oder im HTTP Header einfügen musst.
Dies kann beispielsweise nützlich sein, wenn du ein Skript für eine Registrierung erstellst, bei dem die generierte E-Mail-Adresse und die bestätigte E-Mail-Adresse genau dieselbe sein müssen.### Zufällige Ganzzahl

[SHORTCODE_11][SYSTEM_VAR_12][SHORTCODE_12]: Diese Variable erzeugt eine zufällige Ganzzahl zwischen den von dir bestimmten Minimum- und Maximum-Werten (einschließlich des Minimum- und Maximum-Werts). Wenn du zum Beispiel [INLINE_CODE_22] spezifizierst, erzeugt diese Variable eine Zahl im Rahmen von 0 bis 100.
### Zufällige Großbuchstaben

[SHORTCODE_13][SYSTEM_VAR_14][SHORTCODE_14] : Diese automatische Variable ermöglicht dir, eine zufällige Reihe alphabetischer Zeichen mit vorgegebener Länge zu erzeugen. Alle Zeichen sind Großbuchstaben. Beispielsweise erzeugt [INLINE_CODE_23] einen Zufallswert in der Form von [INLINE_CODE_24].
### Zufällige US Medicare Beneficiary Kennungen (MBI)
[SHORTCODE_15][SYSTEM_VAR_16][SHORTCODE_16] : Diese automatische Variable kannst du einsetzen, um Kennungen von US-Medicare-Leistungsberechtigten zu generieren. Die MBI ist eine Reihe von 11 alphanumerischen Zeichen. zum Beispiel[INLINE_CODE_25]. Bitte beachte, dass dieser Code ohne Bindestriche erzeugt wird. Der MBI-Ccode kann von Unternehmen aus der US-amerikanischen Gesundheitsbranche genutzt werden.

## Transaktionsspezifische (frühere) Variablen

Die folgende Reihe automatischer Variablen ist älter, können aber noch verwendet werden: Diese Variablen werden ausschließlich beim **Transaktions**-Monitoring genutzt.

### Zeitstempel

[SHORTCODE_17]{timespan 0}{now dd-MM-yyyy}[SHORTCODE_18]: Zu **Erzeugung und Einrichtung eines Zeitstempels** (aktuelles Datum) in einem Textfeld auf deiner Seite.

[SHORTCODE_19]{timespan 1:0:0:0}{now dd-MM-yyyy}[SHORTCODE_20]: Zum **Offset des Tages um 1** (morgen).

[SHORTCODE_21]{timespan 0:1:0:0}{now dd-MM-yyyy}[SHORTCODE_22]: So wie oben, aber **Offset um 1 Stunde**.

[SHORTCODE_23]{timespan 0:0:1:0}{now dd-MM-yyyy}[SHORTCODE_24] und [SHORTCODE_25]{timespan 0:0:0:1}{now dd-MM-yyyy}[SHORTCODE_26]: Offset der aktuellen Zeit um eine Minute bzw. eine Sekunde.

### Zufälliger Wert aus einer Matrix

[SHORTCODE_27]{random 1 2 3 4 5}[SHORTCODE_28]: Setzen eines zufälligen Werts aus einer Matrix. Diese setzt einen zufälligen Wert von eins bis fünf.

[SHORTCODE_29]{random apple banana orange}[SHORTCODE_30]: Mit dieser Funktion wird eine Zeichenfolge aus der ausgewählten Matrix gesetzt: Es wird entweder [INLINE_CODE_26], [INLINE_CODE_27] oder [INLINE_CODE_28] gesetzt.

## Spezifische Variablen im Multi-step API Monitoring

Die folgenden automatischen Variablen und Informationen gelten nur für das **Multi-Step API**-Prüfobjekt.

### Serveridentifizierung (ID)

[SHORTCODE_31][SYSTEM_VAR_17][SHORTCODE_32]: Bei der Ausführung eines Prüfobjekts des Multi-step API Monitorings gibt diese Variable einen numerischen Wert aus, der den Standort von Uptrends‘ Checkpoint identifiziert, der diesen Test durchführt. Wenn der Test zum Beispiel von Uptrends' Checkpoint in Sydney, Australien, ausgeführt wird, gibt die Variable den Wert [INLINE_CODE_29] aus. Die Liste der Checkpoint-Server und ihre zugehörigen **Server IDs** ist mithilfe der [Uptrends API]([LINK_URL_3]) über den [Checkpoint-Endpunkt]([LINK_URL_4]) verfügbar.

### Redirect URL

[SHORTCODE_33][SYSTEM_VAR_18][SHORTCODE_34]: Falls einer der Schritte bei dem Monitoring einen Redirect-Code zurückgeben sollte und du diese Redirect-Antwort erfassen und testen möchtest, wird diese automatische Variable die URL enthalten, auf die sich die Weiterleitung bezieht, statt ihr automatisch zu folgen. Dafür musst du jedoch festlegen, Weiterleitungen nicht automatisch zu folgen, und eine Assertion (Prüfpunkt) einrichten, der auf den richtigen Redirect-Code prüft. Dieses Verfahren wird hier detaillierter erläutert: [Multi-step Monitoring – Handhabung von Redirects]([LINK_URL_5]).

### Zufälliger Float

[SHORTCODE_35][SYSTEM_VAR_19][SHORTCODE_36] : Nutze diese Funktion, um eine Gleitkommazahl innerhalb der angegebenen Bandbreite (min./max.) zu erzeugen. Die Genauigkeit (die Anzahl der Ziffern nach dem Dezimalpunkt) wird von der höchsten Genauigkeit von den verwendeten Werten [INLINE_CODE_30] und [INLINE_CODE_31] abgeleitet.

Zum Beispiel wird [INLINE_CODE_32] einen zufälligen Float zwischen -1.2 und 3.0 mit einer Genauigkeit von 5, zum Beispiel 2.12345, erzeugen.

## Mehrfaches Verwenden eines automatisch erzeugten Werts

Einige dieser Variablen-Funktionen (insbesondere solche, die Zufalls- oder Datum-/Zeit-Werte erzeugen) werden jedes Mal neu bewertet, wenn du sie einsetzt, und erzeugen jedes Mal einen neuen Wert. Wenn du einen bestimmten Wert generieren und mehrfach in einem mehrstufigen Szenario verwenden möchtest, kannst du (wie in im Artikel [Multi-step Monitoring – Variablen]([LINK_URL_6]) erläutert) eine Variable vordefinieren und eine automatische Variable als Wert nutzen.

### Beispiele vordefinierter Variablen, die automatische Variablen nutzen

| Name          | Wert                            | Einsatz                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_33]  | [INLINE_CODE_34]     | Ein Datums-Wert, der als Eingabe einer Suchabfrage eingesetzt wird.                                                                                                                                                                                                                           |
| [INLINE_CODE_35] | [INLINE_CODE_36] | Ein zufälliger Guid-Wert zusammen mit festgelegtem Text, um eine E-Mail-Adresse zu erzeugen, die sich jedes Mal unterscheidet.                                                                                                                                                                |
| [INLINE_CODE_37] | [INLINE_CODE_38]         | Eine zufällige Zahl zwischen 1 und 10, die als zu bestellende Anzahl von Produkten verwendet wird. Bei einem nachfolgenden Aufruf kann diese Variable nochmals verwendet werden, um den Inhalt eines Einkaufswagens zu prüfen und zu bestätigen, dass dieser tatsächlich diese Menge enthält. |
