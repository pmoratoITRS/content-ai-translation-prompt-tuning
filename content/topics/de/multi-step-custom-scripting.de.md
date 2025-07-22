{
  "hero": {
    "title": "Eigene Skripte beim Multi-Step API-Prüfobjekt"
  },
  "title": "Eigene Skripte beim Multi-Step API-Prüfobjekt",
  "summary":"Ein Überblick zu den Optionen des benutzerdefinierten Scriptings beim Multi-Step API Monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-eigene-skripte",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-custom-scripting"
}

Das Prüfobjekt Multi-Step API (MSA) verfügt über leistungsstarke [eingebaute Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="de" >}}), die eine anwenderfreundliche und codefreie Lösung zum Testen deiner APIs bieten.

Während man, ohne selbst Code zu schreiben, bereits gute, richtige Überwachungseinrichtungen erhält, kann es sein, dass eine Skriptsprache für tiefgreifende Funktionstests erforderlich ist, um genau zu beschreiben, was du von deinen APIs erwartest. Beispielsweise, wenn du eine benutzerdefinierte Logik hinzufügen oder fortschrittlichere Funktionen behandeln möchtest, die nicht allein mit einer Einrichtung über die Benutzeroberfläche erreicht werden.

Mit dem MSA-Prüfobjekt kannst du sowohl klassische codefreie Funktionen als auch benutzerdefinierte Skripte nutzen. Du kannst vorhandene Funktionen der Benutzeroberfläche neben den Skript-Entsprechungen verwenden. Du musst deine Prüfobjekte nicht von Grund auf neu erstellen, wenn du bereits über API-Prüfobjekte verfügst und benutzerdefinierte Skripte hinzufügen möchtest. Füge einfach deine Skripte hinzu und lasse sie mit der bestehenden Einrichtung ausführen.

## Vor-Anfrage- und Nach-Antwort-Skripte

Ein API-Prüfobjekt kann aus einem einzelnen Schritt bestehen oder mehrere Schritte haben, die nacheinander ausgeführt werden. Für jeden MSA-Schritt (außer Warte-Schritten), gibt es zwei Skript-Editoren,
{{< AppElement type="tab" >}} Vor-Anfrage {{< /AppElement >}} und {{< AppElement type="tab" >}} Nach-Antwort {{< /AppElement >}}:

- Der Skript-Editor **Vor-Anfrage** ermöglicht das Schreiben von Skripten zur Vorbereitung auf das Senden einer HTTP-Anfrage. Daher ist es sehr nützlich, um Werte vorzubereiten und zu berechnen, die mit der Anfrage gesendet werden sollen, etwa Umgebungsvariablen, URL-Parameter, Abfrage-Header oder Inhalt. Das in diesem Editor erfasste Skript wird ausgeführt, *bevor* die API-Anfrage an den Server gesendet wird.

- Der Skript-Editor **Nach-Antwort** ermöglicht das Schreiben von Skripten, um die HTTP-Antwort, die von der API zurückgesendet wird, zu verifizieren und zu verarbeiten. Dies ist nützlich, um benutzerdefinierte Programme zu schreiben, die die Antwort-Header prüfen, die Vollständigkeit und Richtigkeit des Inhalts validieren und diese Inhaltsdaten für weitere Schritte vorbereiten. Das in diesem Editor geschriebene Skript wird nur ausgeführt, *nachdem* die API-Antwort vom Server erhalten wurde. Sollte ein Verbindungsfehler auftreten, wird das Skript nicht ausgeführt und Assertions oder Variablen des Tabs {{< AppElement type="tab" >}} Response {{< /AppElement >}} werden nicht validiert.

Diese Editoren enthalten auch die folgenden Funktionen:
![Tabs für benutzerdefinierte Skripte](/img/content/API-monitoring-custom-scripting-editors-min.png)

- Zeilennummerierung – zeigt die numerischen Werte, die Skripte oder Code nach Zeile identifizieren.
- Code-Markierung – zeigt den Code im farbcodierten Format, sodass Syntaxfehler und Schlüsselwörter schnell identifiziert werden können.
- Code-Vervollständigung – schlägt automatisch Code-Kombinationen vor, um beim Skript-Schreiben zu unterstützen.
- Schnipsel-Bereich – liefert eine Liste nützlicher Code-Schnipsel, die du automatisch in den Code-Editor einfügen kannst.

## Schnipsel

Die Editoren **Vor-Anfrage** und **Nach-Antwort** ermöglichen dir, in JavaScript geschriebene Skripte einzufügen und auszuführen. Neben der kompletten Bandbreite an Möglichkeiten, die Standard-Javascript bietet, kannst du auch **Schnipsel** verwenden.

**Schnipsel** sind spezielle Funktionen, die dir ermöglichen, auf Daten von HTTP-Abfragen (während des Vor-Anfrage-Prozesses) und HTTP-Antworten (während des Nach-Antwort-Prozesses) zuzugreifen. Es ermöglicht dir auch, Protokollmeldungen auszuführen, berechnete Daten als [benutzerdefinierte Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="de" >}}) zu speichern und Tests an Schrittdaten auszuführen. Diese besonderen Funktionen sind durch ein einzigartiges Objekt, `ut`, ansprechbar.

## Allgemeine oder grundlegende ut-Objekte

In diesem Abschnitt lautet die Reihe der allgemeinen `ut`-Objekte wie folgt:

- `ut.request` ermöglicht dir Zugriff auf das API-Anfrageobjekt.
- `ut.response` ermöglicht dir Zugriff auf das API-Antwortobjekt.
- `ut.variables` ist die Sammlung der Variablen, die du bei allen API-Schritten nutzen kannst. Nutze sie, um Werte von einem Schritt zum nächsten zu übergeben. Alle [vordefinierten Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}) oder Variablen, die du auf dem Tab {{< AppElement type="tab" >}} Antwort {{< /AppElement >}} verwendest, sind in dieser Objektsammlung enthalten.
- `ut.log()` ist eine Hilfsfunktion, die die angegebenen Protokolle in das Konsolenprotokoll schreibt. Protokolle werden bei Ausführung der Vor-Anfrage-Skripte im **Konsolenprotokoll des Vor-Anfrage-Skripts** abgelegt, während Protokolle für Nach-Antwort-Skripte im **Konsolenprotokoll des Nach-Antwort-Skripts** zu finden sind.
- `ut.test()` ist die Hauptfunktion, um Testergebnisse zu erfassen. Alle Testergebnisse, die du in jedem `ut.test()`-Aufruf definierst, werden erfasst und als **Assertions**-Ergebnis zusammen mit den Assertions, die du auf dem Tab {{< AppElement type="tab" >}} Response {{< /AppElement >}} bei jedem Schritt definierst, aufgeführt.
- `ut.customMetrics` ist eine Sammlung numerischer Werte, die direkt aus einer API-Antwort stammen. Du kannst deine eigenen Messvariablen definieren, um Werte aus einer API-Antwort zu speichern oder zu berechnen. Dieser Wert wird in den Kontrolldetails des Prüfobjekts für jede Messung angezeigt und kann auch in den Dashboard-Listen und ‑Diagrammen erscheinen.
- `ut.crypto` ermöglicht die Erzeugung von MD5- und SHA-Hashes zur sicheren Handhabung von Daten und Übertragung. Es kann auch zum Parsen der Zertifikats-Widerrufslisten/Revozierungslisten (Certificate Revocation Lists, CRLs) verwendet werden.

Nun kennst du die grundlegenden `ut`-Objekte. In diesem Abschnitt sehen wir uns die Attribute jedes `ut`-Objekts genauer an.

### Request

Attribute von `ut.request`:

- `.url` – fragt ab oder setzt die URL des Requests
- `.method` – fragt ab oder setzt die HTTP-Methode (wie etwa GET oder POST) des Requests
- `.body` – fragt ab oder setzt eine Reintextversion des Request Bodys

### Request Header

Funktionen von `ut.request.headers`:

- `.has(header, value)` – gibt an, ob der Header existiert und einen bestimmten Wert hat
- `.get(header)` – gibt den Wert des Headers wieder. Gibt einen leeren String zurück, wenn der Header nicht existiert
- `.add(header, value)` – erstellt einen neuen Header und den angegebenen `value` (nur, wenn der Header nicht bereits bestimmt war)
- `.upsert(header, value)` – gibt den Header mit dem angegebenen `value` (wenn der Header nicht bereits existiert) ein oder aktualisiert den Header mit dem angegebenen Wert (wenn der Header bereits existiert)
- `.remove(header)` – entfernt den Header

### Response

Attribute von `ut.response`:

- `.code` – fragt den numerischen HTTP-Statuscode ab (z. B. 200, 404, 500)
- `.status`  – ruft die HTTP-Status-Beschreibung ab (wie z. B. OK)
- `.responseSize` – fragt die Größe der Antwort in Bytes ab
- `.bytes` – gibt eine Byte-Zeichenfolge mit der Antwort aus. Antworten sind auf 100 MB begrenzt.

Funktionen von `ut.response`:

- `.text()` – gibt eine Reintextversion des Request Bodys zurück
- `.json()` – gibt ein Objekt zurück, indem der Antworttext als JSON geparst wird

### Response Header

Funktionen von `ut.response.headers`:

- `.has(header)` – gibt an, ob der Header existiert
- `.get(header)` – gibt den Wert des Headers wieder. Gibt einen leeren String zurück, wenn der Header nicht existiert

### Variablen

Funktionen von `ut.variables`:

- `.has(key)` – gibt an, ob die Variable existiert
- `.get(key)` – gibt den Wert der Variable an. Gibt einen leeren String zurück, wenn die Variable nicht existiert
- `.set(key, value)` – erzeugt die Variable (wenn sie nicht existiert) und speichert den angegebenen `value` in der `key`-Variable

### Benutzerdefinierte Metriken

Funktionen von `ut.customMetrics`:

- `.get(key)` – gibt den Wert der benutzerdefinierten Metrikvariable an. Gibt einen leeren String zurück, wenn die benutzerdefinierte Metrik nicht existiert
- `.set(key, value)` – speichert den angegebenen `value` in der `key`-Variable der benutzerdefinierten Metrik

Weitere Informationen findest du in den Knowledge-Base-Artikeln [Einrichtung benutzerdefinierter API-Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="de" >}}) und [Multi-Step Monitoring-Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}).

### Test oder Assert

Uptrends unterstützt die Schnittstellen Expect und Should von Chai JS, siehe [Chai - Should](https://www.chaijs.com/guide/styles/#should "https://www.chaijs.com/guide/styles/#should") und [Chai - Expect](https://www.chaijs.com/guide/styles/#expect "https://www.chaijs.com/guide/styles/#expect"), um zu erfahren, wie verschiedene Tests zu Werten und Vergleiche ausgedrückt werden:

- `ut.expect(value)` + verschiedene Ausdrücke
- `ut.should(value)` + verschiedene Ausdrücke  

Alle `.expect()`- und `.should()`-Ausdrücke (wenn allein verwendet), erzeugen einen Fehler, wenn die gewünschten Kriterien nicht erfüllt werden, und unterbrechen die Ausführung des Prüfobjekts. Alle weiteren Assertions, die im übrigen Skript definiert sind, werden dann nicht ausgeführt.

Verwende `ut.test()`, um alle Assertions auszuführen, unabhängig davon, ob vorhergehende Assertions einen Fehler verursachten:

- `ut.test(descriptionText, testFunction)` – die Ausgabe (Erfolg oder Fehler) eines in der testFunction spezifizierten `.expect` oder `.should` erscheint in der Assertion-Ausgabe des Prüfobjekts. Darüber hinaus sorgt `ut.test()` dafür, dass die Ausführung des Skripts nicht angehalten wird, wenn eine Assertion einen Fehler erzeugt.

## Hashing

Funktion von `ut.crypto`:

- `.md5(value)` – generiert einen MD5-Hash des angegebenen Werts
- `.sha1(value)` – generiert einen SHA-1-Hash des angegebenen Werts
- `.sha256(value)` – generiert einen SHA-256-Hash des angegebenen Werts
- `.sha512(value)` – generiert einen SHA-512-Hash des angegebenen Werts

Die Skriptmethoden zur Generierung von MD5- und SHA-Hashes ermöglichen dir, Werte sicher zu speichern und zu senden. Der Datenschutz wird durch das Hashen gewährleistet. 

Beispiel:

```js
var hashedMD5value = ut.crypto.md5("value here");
var hashedSHA1value = ut.crypto.sha1("value here");
```

- `.cert.parseCrl(bytes)` – parst eine Revozierungsliste von Zertifikaten und gibt ihre Metadaten zurück. Eine CRL-Datei sollte als Input für die Funktion `.cert.parseCrl(bytes)` angegeben werden. Wenn du zum Beispiel das Feld `NextUpdate` aus einer CRL-Datei oder CRL-URL lesen möchtest, kannst du die Funktion wie folgt nutzen:

```js
  var crl = ut.crypto.cert.parseCrl(ut.response.bytes);
  var crlNextUpdate = new Date(crl.NextUpdate);
  ut.log(ut.crypto.cert.parseCrl(ut.response.bytes));

  // Assert the value of a variable
  ut.test("Variable {variable} should equal {value}", () => {
    expect(crlNextUpdate).at.least(new Date(2026, 1, 1));
  });
```