{
  "hero": {
    "title": "Hashing und Codierung"
  },
  "title": "Hash- und/oder Codierungswerte",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/hashing-und-verschluesselung",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/hashing-and-encoding"
}

In bestimmten Situationen des [API-Monitorings]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring" lang="de" >}}) kann es notwendig sein, Variablen oder Werte als Hash oder codiert zu übergeben. Zum Beispiel kann es für Autorisierungen erforderlich sein, eine Base64-Codierung oder einen HMAC-SHA256-Hash einzusetzen, um richtig zu funktionieren. Oder du musst vielleicht in deiner Anfrage codiertes JSON verwenden. Zu diesem Zweck bietet Uptrends verschieden Codierungs- und Hash-Optionen, die wir in diesem Artikel beschreiben.

## Codieren und Decodieren

Das Codieren ist ein Vorgang, bei dem sichergestellt wird, dass Daten in einer bestimmten Form zuverlässig übermittelt werden können. Eine Zeichenfolge oder eine Datei können so codiert werden, dass der Empfänger das Format versteht und sie dann schließlich wieder decodiert.

### Base64 
Base64 ist ein Codierungssystem, das üblicherweise eingesetzt wird, um binäre Daten als Text zu übermitteln. Es wird häufig bei Protokollen wie der [Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617) verwendet. Um die Base64-Codierung bei deinem Multi-step API-Prüfobjekt zu nutzen, verwende die Funktion `{{@Base64Encode(yourContentHere)}}`.

Die Funktion Base64Encode akzeptiert auch [(vordefinierte) Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}), indem der Variablenhinweis (in geschwungenen Klammern) einfach in die Funktion eingebunden wird: `{{@Base64Encode({{yourVariableName}})}}`.

Die Decodierung wird ebenfalls unterstützt – mit der Funktion `{{@Base64Decode()}}`.

Die Funktionen Base64Encode und -Decode können an beliebiger Stelle der Multi-step API-Prüfobjektkonfiguration verwendet werden. Das heißt, du kannst dich beispielsweise direkt bei der Erzeugung eines Request Headers oder in deinem Request Body darauf beziehen.

![Base64Encode-Funktion bei einem Auth-Header](/img/content/scr-msa-base64-encode-auth-header.min.png)

### JSON und XML

JSON und XML sind übliche Datenaustauschformate, die in der Regel an eine ziemlich strenge Formatierung  gebunden sind, um gültig zu bleiben. In einigen Fällen müssen JSON- oder XML-Inhalte codiert werden, bevor sie gesendet werden können. Beispielsweise kann JSON nicht in sich selbst eingebettet werden (du kannst keine JSON-formatierten Inhalte innerhalb eines JSON-formatierten Inhalts senden), ohne seine Struktur zu zerstören – sofern es nicht kodiert ist. Ein weiteres Beispiel: Wenn dein Klartext-Inhalt Anführungszeichen enthält, haben diese im JSON-Format eine besondere Bedeutung und können nicht ohne vorheriges Codieren in einer Nachricht in JSON-Struktur übermittelt werden.

Ähnlich der oben beschriebenen Funktionen Base64Encoding und -Decoding gibt es die Funktionen JsonEncode(), JsonDecode(), XmlEncode() und XmlDecode(). Weitere Informationen zu ihrer Verwendung findest du in unserer Dokumentation zur [Nachrichtenformatierung bei benutzerdefinierten Integrationen]({{< ref path="support/kb/alerting/integrations/custom-integrations/message-formatting#applying-automatic-formatting" lang="de" >}}).

## Hashing {id="hashing"}

Anders als die Codierung, die entschlüsselt werden kann, ist das Hashing ein Einweg-Vorgang, bei dem ein Algorithmus anhand einer mathematischen Funktion eine Nachricht beliebiger Länge auf einen Wert mit fester Länge abbildet. Ein Hash-Wert kann praktisch nicht umgekehrt werden und jede Eingabe sollte immer zum selben Ergebnis führen. Hashing wird üblicherweise bei der Authentifizierung eingesetzt, da es eine sichere Methode für den Austausch und Vergleich geheimer Daten wie Passwörter oder Signaturen ist.

Uptrends unterstützt die folgenden Hash-Algorithmen:

- MD5
- SHA1
- SHA256
- SHA512
- HMAC-SHA1
- HMAC-SHA256
- HMAC-SHA512

Hash-Funktionen werden über das System der [benutzerdefinierten Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="de" >}}) eingerichtet und die Implementierung einer Hash-Funktion folgt denselben Schritten, die in dem Artikel beschrieben sind. Du kannst eine Hash-Funktion auf jede Klartext-Zeichenfolge, alle [Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}), die als Folge eines der Schritte in deinem Prüfobjekt erstellt wurden, oder alle [vordefinierten Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined-variables" lang="de" >}}) anwenden.

Die HMAC-basierten Hash-Funktionen erfordern die Eingabe eines **geheimen Schlüssels** als statische Eingabe, die sie mit der Nachricht kombinieren, um eine sichere konsistente Ausgabe zu erzeugen. Es kann sich dabei auch um einen Wert eines Anmeldesets aus der [Vault]({{< ref path="/support/kb/account/vault" lang="de" >}}) handeln.

![Ein Beispiel einer Hash-Funktion](/img/content/scr-msa-hashing-function.min.png)


### Base64-Codierung für gehashte Daten

Bestimmte Authentifizierungsmethoden erfordern einen Hash-Wert, der dann Base64-codiert werden muss. Die oben erwähnte `Base64Encode()`-Funktion ist dazu gedacht, Daten des Typs *String* zu codieren. Diese Hash-Funktionen liefern jedoch *Hexadezimal*-Daten. Es bedeutet, dass das Codieren mit der Standard-Base64-Funktion ein nicht korrektes Ergebnis liefern kann, da es sich um unterschiedliche Datentypen handelt.

Um den aus einer Hash-Funktion resultierenden *Hexadezimal*-Wert korrekt zu codieren, verwende die Funktion `{{@HexToBase64()}}` statt der Standard-Funktion `{{@Base64Encode()}}`.
