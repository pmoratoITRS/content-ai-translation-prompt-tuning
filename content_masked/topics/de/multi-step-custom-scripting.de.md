{
  "hero": {
    "title": "Eigene Skripte beim Multi-Step API-Prüfobjekt"
  },
  "title": "Eigene Skripte beim Multi-Step API-Prüfobjekt",
  "summary": "Ein Überblick zu den Optionen des benutzerdefinierten Scriptings beim Multi-Step API Monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-eigene-skripte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Das Prüfobjekt Multi-Step API (MSA) verfügt über leistungsstarke [eingebaute Funktionen]([LINK_URL_1]), die eine anwenderfreundliche und codefreie Lösung zum Testen deiner APIs bieten.

Während man, ohne selbst Code zu schreiben, bereits gute, richtige Überwachungseinrichtungen erhält, kann es sein, dass eine Skriptsprache für tiefgreifende Funktionstests erforderlich ist, um genau zu beschreiben, was du von deinen APIs erwartest. Beispielsweise, wenn du eine benutzerdefinierte Logik hinzufügen oder fortschrittlichere Funktionen behandeln möchtest, die nicht allein mit einer Einrichtung über die Benutzeroberfläche erreicht werden.

Mit dem MSA-Prüfobjekt kannst du sowohl klassische codefreie Funktionen als auch benutzerdefinierte Skripte nutzen. Du kannst vorhandene Funktionen der Benutzeroberfläche neben den Skript-Entsprechungen verwenden. Du musst deine Prüfobjekte nicht von Grund auf neu erstellen, wenn du bereits über API-Prüfobjekte verfügst und benutzerdefinierte Skripte hinzufügen möchtest. Füge einfach deine Skripte hinzu und lasse sie mit der bestehenden Einrichtung ausführen.

## Vor-Anfrage- und Nach-Antwort-Skripte

Ein API-Prüfobjekt kann aus einem einzelnen Schritt bestehen oder mehrere Schritte haben, die nacheinander ausgeführt werden. Für jeden MSA-Schritt (außer Warte-Schritten), gibt es zwei Skript-Editoren,
[SHORTCODE_1] Vor-Anfrage [SHORTCODE_2] und [SHORTCODE_3] Nach-Antwort [SHORTCODE_4]:

- Der Skript-Editor **Vor-Anfrage** ermöglicht das Schreiben von Skripten zur Vorbereitung auf das Senden einer HTTP-Anfrage. Daher ist es sehr nützlich, um Werte vorzubereiten und zu berechnen, die mit der Anfrage gesendet werden sollen, etwa Umgebungsvariablen, URL-Parameter, Abfrage-Header oder Inhalt. Das in diesem Editor erfasste Skript wird ausgeführt, *bevor* die API-Anfrage an den Server gesendet wird.

- Der Skript-Editor **Nach-Antwort** ermöglicht das Schreiben von Skripten, um die HTTP-Antwort, die von der API zurückgesendet wird, zu verifizieren und zu verarbeiten. Dies ist nützlich, um benutzerdefinierte Programme zu schreiben, die die Antwort-Header prüfen, die Vollständigkeit und Richtigkeit des Inhalts validieren und diese Inhaltsdaten für weitere Schritte vorbereiten. Das in diesem Editor geschriebene Skript wird nur ausgeführt, *nachdem* die API-Antwort vom Server erhalten wurde. Sollte ein Verbindungsfehler auftreten, wird das Skript nicht ausgeführt und Assertions oder Variablen des Tabs [SHORTCODE_5] Response [SHORTCODE_6] werden nicht validiert.

Diese Editoren enthalten auch die folgenden Funktionen:
![Tabs für benutzerdefinierte Skripte]([LINK_URL_2])

- Zeilennummerierung – zeigt die numerischen Werte, die Skripte oder Code nach Zeile identifizieren.
- Code-Markierung – zeigt den Code im farbcodierten Format, sodass Syntaxfehler und Schlüsselwörter schnell identifiziert werden können.
- Code-Vervollständigung – schlägt automatisch Code-Kombinationen vor, um beim Skript-Schreiben zu unterstützen.
- Schnipsel-Bereich – liefert eine Liste nützlicher Code-Schnipsel, die du automatisch in den Code-Editor einfügen kannst.

## Schnipsel

Die Editoren **Vor-Anfrage** und **Nach-Antwort** ermöglichen dir, in JavaScript geschriebene Skripte einzufügen und auszuführen. Neben der kompletten Bandbreite an Möglichkeiten, die Standard-Javascript bietet, kannst du auch **Schnipsel** verwenden.

**Schnipsel** sind spezielle Funktionen, die dir ermöglichen, auf Daten von HTTP-Abfragen (während des Vor-Anfrage-Prozesses) und HTTP-Antworten (während des Nach-Antwort-Prozesses) zuzugreifen. Es ermöglicht dir auch, Protokollmeldungen auszuführen, berechnete Daten als [benutzerdefinierte Metriken]([LINK_URL_3]) zu speichern und Tests an Schrittdaten auszuführen. Diese besonderen Funktionen sind durch ein einzigartiges Objekt, [INLINE_CODE_1], ansprechbar.

## Allgemeine oder grundlegende ut-Objekte

In diesem Abschnitt lautet die Reihe der allgemeinen [INLINE_CODE_2]-Objekte wie folgt:

- [INLINE_CODE_3] ermöglicht dir Zugriff auf das API-Anfrageobjekt.
- [INLINE_CODE_4] ermöglicht dir Zugriff auf das API-Antwortobjekt.
- [INLINE_CODE_5] ist die Sammlung der Variablen, die du bei allen API-Schritten nutzen kannst. Nutze sie, um Werte von einem Schritt zum nächsten zu übergeben. Alle [vordefinierten Variablen]([LINK_URL_4]) oder Variablen, die du auf dem Tab [SHORTCODE_7] Antwort [SHORTCODE_8] verwendest, sind in dieser Objektsammlung enthalten.
- [INLINE_CODE_6] ist eine Hilfsfunktion, die die angegebenen Protokolle in das Konsolenprotokoll schreibt. Protokolle werden bei Ausführung der Vor-Anfrage-Skripte im **Konsolenprotokoll des Vor-Anfrage-Skripts** abgelegt, während Protokolle für Nach-Antwort-Skripte im **Konsolenprotokoll des Nach-Antwort-Skripts** zu finden sind.
- [INLINE_CODE_7] ist die Hauptfunktion, um Testergebnisse zu erfassen. Alle Testergebnisse, die du in jedem [INLINE_CODE_8]-Aufruf definierst, werden erfasst und als **Assertions**-Ergebnis zusammen mit den Assertions, die du auf dem Tab [SHORTCODE_9] Response [SHORTCODE_10] bei jedem Schritt definierst, aufgeführt.
- [INLINE_CODE_9] ist eine Sammlung numerischer Werte, die direkt aus einer API-Antwort stammen. Du kannst deine eigenen Messvariablen definieren, um Werte aus einer API-Antwort zu speichern oder zu berechnen. Dieser Wert wird in den Kontrolldetails des Prüfobjekts für jede Messung angezeigt und kann auch in den Dashboard-Listen und ‑Diagrammen erscheinen.
- [INLINE_CODE_10] ermöglicht die Erzeugung von MD5- und SHA-Hashes zur sicheren Handhabung von Daten und Übertragung. Es kann auch zum Parsen der Zertifikats-Widerrufslisten/Revozierungslisten (Certificate Revocation Lists, CRLs) verwendet werden.

Nun kennst du die grundlegenden [INLINE_CODE_11]-Objekte. In diesem Abschnitt sehen wir uns die Attribute jedes [INLINE_CODE_12]-Objekts genauer an.

### Request

Attribute von [INLINE_CODE_13]:

- [INLINE_CODE_14] – fragt ab oder setzt die URL des Requests
- [INLINE_CODE_15] – fragt ab oder setzt die HTTP-Methode (wie etwa GET oder POST) des Requests
- [INLINE_CODE_16] – fragt ab oder setzt eine Reintextversion des Request Bodys

### Request Header

Funktionen von [INLINE_CODE_17]:

- [INLINE_CODE_18] – gibt an, ob der Header existiert und einen bestimmten Wert hat
- [INLINE_CODE_19] – gibt den Wert des Headers wieder. Gibt einen leeren String zurück, wenn der Header nicht existiert
- [INLINE_CODE_20] – erstellt einen neuen Header und den angegebenen [INLINE_CODE_21] (nur, wenn der Header nicht bereits bestimmt war)
- [INLINE_CODE_22] – gibt den Header mit dem angegebenen [INLINE_CODE_23] (wenn der Header nicht bereits existiert) ein oder aktualisiert den Header mit dem angegebenen Wert (wenn der Header bereits existiert)
- [INLINE_CODE_24] – entfernt den Header

### Response

Attribute von [INLINE_CODE_25]:

- [INLINE_CODE_26] – fragt den numerischen HTTP-Statuscode ab (z. B. 200, 404, 500)
- [INLINE_CODE_27]  – ruft die HTTP-Status-Beschreibung ab (wie z. B. OK)
- [INLINE_CODE_28] – fragt die Größe der Antwort in Bytes ab
- [INLINE_CODE_29] – gibt eine Byte-Zeichenfolge mit der Antwort aus. Antworten sind auf 100 MB begrenzt.

Funktionen von [INLINE_CODE_30]:

- [INLINE_CODE_31] – gibt eine Reintextversion des Request Bodys zurück
- [INLINE_CODE_32] – gibt ein Objekt zurück, indem der Antworttext als JSON geparst wird

### Response Header

Funktionen von [INLINE_CODE_33]:

- [INLINE_CODE_34] – gibt an, ob der Header existiert
- [INLINE_CODE_35] – gibt den Wert des Headers wieder. Gibt einen leeren String zurück, wenn der Header nicht existiert

### Variablen

Funktionen von [INLINE_CODE_36]:

- [INLINE_CODE_37] – gibt an, ob die Variable existiert
- [INLINE_CODE_38] – gibt den Wert der Variable an. Gibt einen leeren String zurück, wenn die Variable nicht existiert
- [INLINE_CODE_39] – erzeugt die Variable (wenn sie nicht existiert) und speichert den angegebenen [INLINE_CODE_40] in der [INLINE_CODE_41]-Variable

### Benutzerdefinierte Metriken

Funktionen von [INLINE_CODE_42]:

- [INLINE_CODE_43] – gibt den Wert der benutzerdefinierten Metrikvariable an. Gibt einen leeren String zurück, wenn die benutzerdefinierte Metrik nicht existiert
- [INLINE_CODE_44] – speichert den angegebenen [INLINE_CODE_45] in der [INLINE_CODE_46]-Variable der benutzerdefinierten Metrik

Weitere Informationen findest du in den Knowledge-Base-Artikeln [Einrichtung benutzerdefinierter API-Metriken]([LINK_URL_5]) und [Multi-Step Monitoring-Variablen]([LINK_URL_6]).

### Test oder Assert

Uptrends unterstützt die Schnittstellen Expect und Should von Chai JS, siehe [Chai - Should]([LINK_URL_7]) und [Chai - Expect]([LINK_URL_8]), um zu erfahren, wie verschiedene Tests zu Werten und Vergleiche ausgedrückt werden:

- [INLINE_CODE_47] + verschiedene Ausdrücke
- [INLINE_CODE_48] + verschiedene Ausdrücke  

Alle [INLINE_CODE_49]- und [INLINE_CODE_50]-Ausdrücke (wenn allein verwendet), erzeugen einen Fehler, wenn die gewünschten Kriterien nicht erfüllt werden, und unterbrechen die Ausführung des Prüfobjekts. Alle weiteren Assertions, die im übrigen Skript definiert sind, werden dann nicht ausgeführt.

Verwende [INLINE_CODE_51], um alle Assertions auszuführen, unabhängig davon, ob vorhergehende Assertions einen Fehler verursachten:

- [INLINE_CODE_52] – die Ausgabe (Erfolg oder Fehler) eines in der testFunction spezifizierten [INLINE_CODE_53] oder [INLINE_CODE_54] erscheint in der Assertion-Ausgabe des Prüfobjekts. Darüber hinaus sorgt [INLINE_CODE_55] dafür, dass die Ausführung des Skripts nicht angehalten wird, wenn eine Assertion einen Fehler erzeugt.

## Hashing

Funktion von [INLINE_CODE_56]:

- [INLINE_CODE_57] – generiert einen MD5-Hash des angegebenen Werts
- [INLINE_CODE_58] – generiert einen SHA-1-Hash des angegebenen Werts
- [INLINE_CODE_59] – generiert einen SHA-256-Hash des angegebenen Werts
- [INLINE_CODE_60] – generiert einen SHA-512-Hash des angegebenen Werts

Die Skriptmethoden zur Generierung von MD5- und SHA-Hashes ermöglichen dir, Werte sicher zu speichern und zu senden. Der Datenschutz wird durch das Hashen gewährleistet. 

Beispiel:

[CODE_BLOCK_1]

- [INLINE_CODE_61] – parst eine Revozierungsliste von Zertifikaten und gibt ihre Metadaten zurück. Eine CRL-Datei sollte als Input für die Funktion [INLINE_CODE_62] angegeben werden. Wenn du zum Beispiel das Feld [INLINE_CODE_63] aus einer CRL-Datei oder CRL-URL lesen möchtest, kannst du die Funktion wie folgt nutzen:

[CODE_BLOCK_2]