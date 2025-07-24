{
  "hero": {
    "title": "Multi-step Monitoring – Authentifizierung"
  },
  "title": "Multi-step Monitoring – Authentifizierung",
  "summary": "Erfahre mehr über die verfügbaren Authentifizierungsoptionen beim Multi-step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-authentifizierung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Viele APIs erfordern, dass der Aufrufende Authentifizierungsinformationen angibt, um die Identität – und möglicherweise die Zugriffsberechtigungen – des Aufrufenden zu verifizieren. Authentifizierungsinformationen können über den HTTP-Header (Basic/NTLM/Digest-Authentifizierung), durch Austausch von Zugriffs-Tokens (OAuth), indem vom Client die Mitgabe eines Client-Zertifikats in der Anfrage erwartet wird oder eine Kombination davon weitergegeben werden.  

Dieser Artikel behandelt die HTTP-Header- und Token-basierten Authentifizierungsmethoden bei Uptrends. Um Client-Zertifikate einzurichten, lies bitte [den Artikel zur Client-Zertifikats-Authentifizierung]([LINK_URL_1]). 

## Standard-Authentifizierungsarten

Der Abschnitt Authentifizierung auf der Registerkarte Request bei einem Multi-step API Monitoring-Prüfobjekt stellt mehrere Authentifizierungsarten bereit. Bei allen wird eine Kombination aus Benutzername/Passwort verwendet. Wie diese Anmeldeinformationen verarbeitet und an die API gesendet werden, unterscheidet sich je nach Art:

-   **Basic Authentication**: Benutzername und Passwort sind in einem einfachen Base64-Format verschlüsselt und werden an den API-Server gesendet.
-   **NTLM (Windows) Authentifizierung**: Wenn du diesen Typ wählst, werden mehrere Anfragen an die API gesendet, um die zu verwendende Authentifizierung zu verhandeln, bevor die letztendliche HTTP-Anfrage mit der entsprechenden Authentifizierung gesendet wird. Diese Reihe von Anfragen wird als ein einzelner Schritt betrachtet. Wenn eine Windows-Domain angegeben werden muss, schließe sie im Benutzernamen ein: YOURDOMAIN\username.
-   **Digest Authentication**: Der Benutzername und das Passwort werden mit dem MD5-Hash-Algorithmus gehasht. Der Hash wird dann an den Server gesendet.
-   **Kein**: Wähle *Kein*, wenn du keine Authentifizierung für Deine HTTP-Anfrage nutzt.

### HTTP-Header

Die oben beschriebenen Authentifizierungstypen senden mehrere Abfragen (die jedoch alle als ein Schritt gelten). Die erste Abfrage enthält keine Anmeldedaten (weder gehasht/verschlüsselt noch anderweitig). Der Client wartet dann auf eine Anfrage vom Server in Form eines 401 (Unauthorized) Antwortcodes und eines **WWW-Authentifizierungs**-Headers, der die erforderliche Methode der Authentifizierung angibt. Dann sendet der Client die Abfrage erneut, aber dieses Mal mit dem korrekten Autorisierungs-Header.

Wenn du einen dieser Authentifizierungstypen nutzt, musst du keine weiteren authentifizierungsspezifischen HTTP-Header angeben: Die entsprechenden Autorisierungs-Header werden automatisch erzeugt. Ist die Anfrage jedoch nicht vollständig (weil der Server mit einem anderen Statuscode als 401 antwortet oder weil der WWW-Authentifizierungs-Header fehlt), wird das Prüfobjekt einen Fehler zurückgeben und du musst eventuell den richtigen Autorisierungs-Header manuell festlegen.

Zum Beispiel: Für die Basic Authentifizierung sollte der Server nach der ersten Abfrage mit einer Anfrage reagieren, mit dem Header [INLINE_CODE_1] und dem Statuscode 401: Unauthorized. Wenn dies nicht erfolgt, muss du eventuell den Basic Authentifizierungs-Header manuell einrichten, sodass die Anmeldedaten ohne korrekte Anfrage mitgesendet werden.

Gemäß dem [Basic Authentifizierungsschema]([LINK_URL_2]) müssen die Anmeldedaten in einer Base64-verschlüsselten Zeichenfolge als *Benutzername:Passwort* gesendet werden. Die Base64-verschlüsselte Zeichenfolge von 'Benutzername:Passwort' ergibt [INLINE_CODE_2], was dann in einem Autorisierungs-Header gesendet werden muss. Indem du den Header [INLINE_CODE_3] zum MSA-Schritt hinzufügst, kannst du die Notwendigkeit einer Anfrage vom Server praktisch umgehen.

### Variablen-Support

Benutzername- und Passwort-Felder unterstützen Variablen. Du kannst vordefinierte Variablen (beispielsweise: [SHORTCODE_1]{{username}}[SHORTCODE_2] und [SHORTCODE_3]{{password}}[SHORTCODE_4]) mit den entsprechenden Werten erstellen und diese Variablen in den Authentifizierungsfeldern nutzen. [Weitere Informationen über Variablen und vordefinierte Variablen]([LINK_URL_3]).

## Benutzerdefinierte Authentifizierung

Wenn deine API OAuth als Authentifizierungsprotokoll nutzt, benötigst du ein ausgefeilteres Setup. Abhängig von deiner API benötigst du möglicherweise etwas Spezielles für die Situation. OAuth 2.0 insbesondere nutzt eine separate Anfrage für den Authentifizierungsprozess. Diese Anfrage benötigt Zugang zur API (anhand einer Standard-Authentifizierungsart durch Spezifizieren von Anmeldedaten in der URL oder Ausführen einer Webseitenanmeldung). Nach erfolgreicher Authentifizierung wird das OAuth-Access-Token verzeichnet und in einer Variablen gespeichert, sodass es in nachfolgenden Anfragen genutzt werden kann.

Wenn du nicht OAuth, sondern ein anderes Protokoll verwendest, kann dies immer noch auf ähnliche Weise funktionieren: Du musst die Anmeldedaten angeben, die deine Identität für die API „beweisen“. Der API-Server antwortet dann mit einem Anmelde-Token, das für eine bestimmte Dauer gültig ist. Durch Aufzeichnung dieses Tokens und Speicherung in einer Variablen kannst du eine Reihe von Anfragen ausführen, die dieses Anmelde-Token verwenden, um Zugang zu erhalten.

### Einrichtung der OAuth 2.0 Authentifizierung

Im folgenden Beispiel richten wir eine einfache OAuth 2.0 Authentifizierung ein. Unser Ziel besteht darin, ein Zugangstoken von der API zu erhalten, das wir in späteren Anfragen verwenden können.

Dafür werden wir eine Anfrage senden, die die entsprechenden OAuth-Felder enthält. In diesem Fall bitten wir um Zugang auf Basis eines Autorisierungscodes, einer Client-ID und eines Client-Geheimnisses. Die Client-ID und das Client-Geheimnis sind feststehende Werte, die wir als vordefinierte Variablen bestimmen können. In unserem einfachen Setup wird der Autorisierungscode ein fester Wert sein, aber in deinem Setup kann es notwendig sein, den Autorisierungscode zunächst in einem separaten Schritt abzufragen.

Zuerst fügen wir diese Werte zu den vordefinierten Variablen hinzu:

![Predefined variables]([LINK_URL_4])

Mit diesen definierten Variablen können wir nun eine Anfrage an unsere API einrichten, um Bezüge zu diesen Variablen einzuschließen, zusammen mit anderen Parametern, die von der API erwartet werden. Im ersten Schritt der mehrstufigen Einrichtung sollte diese URL enthalten sein:

[INLINE_CODE_4]

Wir erwarten, dass die API eine Datenstruktur zurückgibt, die das benötigte Access-Token enthält, aber wie wird diese Datenstruktur formatiert sein? Um zu gewährleisten, dass wir JSON-formatierte Daten erhalten, werden wir dem Server sagen, dass wir nur das Format application/json annehmen, indem wir den HTTP-Header angeben:

![MSA accept header]([LINK_URL_5])

Mit dem spezifizierten Header können wir nun erwarten, dass die Antwort wie Folgendes aussieht:

[INLINE_CODE_5]

Alles was wir nun tun müssen, ist das Feld access\_token in der JSON-Antwort aufzuzeichnen. Dafür erzeugen wir eine neue Variable auf der Registerkarte Response bei unserem Schritt:

-   Die Antwort sollte JSON enthalten, wähle daher [SHORTCODE_5]Response Body als JSON[SHORTCODE_6] als Quelle für die Variable.
-   Da das **access_token**-Attribut sich auf oberster Ebene in unserer Datenstruktur befindet, ist unser JSON-Ausdruck einfach [SHORTCODE_7]access_token[SHORTCODE_8].
-   Wir wählen [SHORTCODE_9]accesstoken[SHORTCODE_10] als Variablenname. Auf diesen Namen beziehen wir uns bei späteren Schritten.

![Access token variable]([LINK_URL_6])

Obwohl das Hauptziel dieses ersten Schrittes darin besteht, das Access-Token aufzuzeichnen, wird bereits ein Monitoring ausgeführt: Wenn die API zu diesem Zeitpunkt einen Fehler registriert oder wenn die Antwort kein Access-Token enthält, wird das in diesem Schritt bemerkt und ein Fehler gemeldet.

Da wir nun ein gültiges Access-Token haben, können wir schließlich auf die tatsächliche API-Methode zugreifen, die wir prüfen möchten (und zum Beispiel eine Liste von Produkten abrufen). Erstelle einen neuen Schritt, um diesen API-Aufruf zu definieren. Nach Spezifizieren der Methode und URL für diese neue Anfrage, geben wir das Access-Token ein, das wir gerade aufgezeichnet haben. APIs basierend auf OAuth 2.0 erwarten einen HTTP-Header namens **Authorization** mit einem Wert [INLINE_CODE_6]

![Access token header]([LINK_URL_7])

Wir können dies für jeden zusätzlichen Schritt wiederholen, der dasselbe Access-Token benötigt.
