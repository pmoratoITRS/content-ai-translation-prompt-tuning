{
  "hero": {
    "title": "API Monitoring – Übersicht"
  },
  "title": "API Monitoring – Übersicht",
  "summary": "Was ist das API Monitoring und wie kannst du es für dich nutzen?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/api-uberwachung-im-uberblick",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Eine API (Application Programming Interface) ist eine Software, die eine Kommunikation zwischen Anwendungen ermöglicht. Möglicherweise nutzt du deine eigene API und/oder verlässt dich auf APIs Dritter. So oder so ist die richtige Funktionsweise der APIs grundlegend für den Betrieb deiner Website und Services und du solltest sie überwachen.

Das API Monitoring prüft, ob die APIs, auf die du dich verlässt, verfügbar, funktionstüchtig und leistungsstark sind. Weitere Informationen findest du im Artikel [Was ist API Monitoring?]([LINK_URL_1]).

Das API Monitoring von Uptrends bietet unterschiedliche Prüfobjekttypen, um ein API Monitoring einzurichten. Die Typauswahl hängt davon ab, ob es sich um einen einzelnen Schritt oder eine Reihe von Anfragen mit mehreren Schritten handelt. Das Prüfobjekt für einen Schritt wird mit dem Prüfobjekttyp Webservice HTTP oder Webservice HTTPS eingerichtet. Das Prüfobjekt für eine Reihe aufeinanderfolgender Schritte wird anhand des Multi-Step API-Prüfobjekttyps (MSA-Prüfobjekt) definiert.

Die Uptrends Anwendung verfügt über einen [Multi-Step API-Prüfobjekt-Hub]([LINK_URL_2]), bei dem du Informationen zu diesen Prüfobjekten und dem aktuellen Status an einem Ort findest.

## API-Prüfobjekte einrichten

Die Einrichtung unterschiedlicher Prüfobjekttypen wird in diesen Artikeln beschrieben:

- [Das Webservices-Monitoring einrichten]([LINK_URL_3])
- [Das Web Services Monitoring (SOAP) einrichten]([LINK_URL_4])
- [Das Multi-Step Monitoring einrichten]([LINK_URL_5])
- [Das Postman-API-Monitoring einrichten]([LINK_URL_6])

## Schritte beim Multi-Step API Monitoring definieren

Bei der Einrichtung eines Multi-Step API-Prüfobjekts definierst du einen Schritt für jede HTTP-Anfrage, die Teil des zu überwachenden Szenarios ist. Für jeden Schritt gibt es zwei Aspekte zu bedenken: Zunächst gibst du die Daten für die Anfrage ein und definierst, was ausgeführt und an die API gesendet wird. Dann gibst du die Daten für die Antwort ein und definierst, was in der Antwort der API geprüft werden muss.

Sowohl die Anfrage- als auch Antwort-Teile für jeden Schritt können optional anhand [angepassten Skripten]([LINK_URL_7]) in Javascript erweitert werden. Du kannst deine eigenen Skripte für Authentifizierungen hinzufügen und Berechnungen und eigene Programmierungen ausführen, um die korrekte Funktion und den Inhalt der API-Schritte zu verifizieren.

Es gibt auch einige Definitionen für [benutzerdefinierte Funktionen]([LINK_URL_8]), [Variablen]([LINK_URL_9]) und [benutzerdefinierte Metriken]([LINK_URL_10]). Diese werden global festgelegt (verfügbar bei allen Schritten). In den Artikeln der folgenden Abschnitte erfährst du mehr über das Einrichten der HTTP-Schritte.

### Request

Der HTTP-Schritt Request (Anfrage) wird durch Angabe einer Methode und einer URL sowie des Request Bodys eingerichtet. Dann werden weitere Details wie zum Beispiel die Authentifizierung angegeben. Die Request-Definition kann auch mit eigenen Skripten weiter angepasst werden. Weitere Informationen findest du in den folgenden Artikeln:

-   [Authentifizierung]([LINK_URL_11])
-   [Client-Zertifikate]([LINK_URL_12])
-   [Uptrends' Client-Zertifikat]([LINK_URL_13])
-   [Datei-Uploads bei der Multi-Step API]([LINK_URL_14])
- [Angepasste Skripte]([LINK_URL_15])

### Response

Im Teil Response (Antwort) des Schritts solltest du Assertions (Prüfpunkte) definieren. Assertions sind Prüfungen, die weiter als die Frage gehen, ob es zu der Anfrage eine Antwort gibt. Eine Assertion prüft auch, ob die Antwort gültig ist oder zeitgerecht empfangen wird. Für jeden Schritt kannst du mehrere Assertions bestimmen. Neben der Definition von Assertions auf der Registerkarte Response kannst du vollständig angepasste Prüfungen und eigene Programmierungen mithilfe der Funktion für eigene Skripte einrichten. Weitere Informationen über Assertions findest du in diesen Artikeln:

-   [Assertions – Einführung]([LINK_URL_16])
-   [Assertions – Quellen]([LINK_URL_17])
-   [Assertions – Vergleichsoperatoren]([LINK_URL_18])
-   [Assertions – Beispiele mit XPath]([LINK_URL_19])
-   [Variablen]([LINK_URL_20])
-   [Handhabung von Redirects]([LINK_URL_21])
- [Angepasste Skripte]([LINK_URL_22])

### Globale Definitionen

Es gibt eine Reihe von Aspekten, die du für alle Schritte und sowohl für ihren Anfrage- wie auch den Antwortteil definieren kannst. Das kann praktisch sein, wenn du einen bestimmten Wert oder eine Funktion in unterschiedlichen Schritten verwenden möchtest. In den folgenden Artikeln findest du mehr dazu:

-   [Vordefinierte Variablen]([LINK_URL_23])
-   [Benutzerdefinierte Funktionen]([LINK_URL_24])
-   [Benutzerdefinierte Metriken]([LINK_URL_25])
- [Hashing und Codierung]([LINK_URL_26])

### Die Skript-Ansicht

Du kannst Schrittdefinitionen des Multi-Step API-Prüfobjekts auch direkt in der *Skript-Ansicht* bearbeiten. Dieses Skript enthält die komplette Definition deiner Multi-Step API-Einrichtung, die du kopieren und an anderen Stellen einfügen kannst. Weitere Informationen findest du im Artikel zum [MSA Skript-Editor]([LINK_URL_27]).

Beachte, dass die *Skript-Ansicht* nicht dasselbe ist wie die Funktion [Angepasste Skripte]([LINK_URL_28]), mit der du benutzerdefinierte Logik zu deinen Skripten hinzufügst.

## Credits

API-Prüfobjekte verwenden API-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]([LINK_URL_29]).