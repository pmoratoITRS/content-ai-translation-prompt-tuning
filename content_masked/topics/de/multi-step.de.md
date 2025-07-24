{
  "hero": {
    "title": "Das Multi-Step API Monitoring einrichten"
  },
  "title": "Das Multi-Step API Monitoring einrichten",
  "summary": "Schritt-für-Schritt-Anleitung für das Einrichten des Multi-step API Monitorings.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Um deine API wirksam zu überwachen, musst du häufig eine Reihe von HTTP-Anfragen erstellen, bei der jede Abfrage Daten von einer vorherigen Abfrage abruft, um die nächste Reihe an Aufträgen auszuführen. Mit dem **Multi-Step API-Prüfobjekt** kannst du mehrere HTTP-Abfragen einrichten, [Variablen]([LINK_URL_1]) definieren, [benutzerdefinierte Funktionen]([LINK_URL_2]) erstellen, [benutzerdefinierte Skripte]([LINK_URL_3]) einrichten und vieles mehr.

Dies sind einige mögliche Szenarien, weshalb du eine Reihe an HTTP-Abfragen ausführen solltest:

- Deine API erfordert einen authentifizierten Zugang – ein API-Client muss zunächst die Anmeldedaten verifizieren, um auf die HTTP-Methoden zuzugreifen (zum Beispiel unter Nutzung der OAuth Authentication).
- Du möchtest ein funktionierendes Szenario bestehend aus mehreren Schritten in deiner API testen, das üblicherweise in einer speziellen Reihenfolge von den Endnutzern ausgeführt wird.
- Deine HTTP-Abfrage gibt eine Weiterleitung zu einer anderen URL zurück, und du möchtest das Verhalten der Antwort untersuchen, bevor die Weiterleitung erfolgt.

## Funktionen des Multi-Step API-Prüfobjekts

Das **Multi-Step API-Prüfobjekt** gibt dir die volle Kontrolle über den kompletten HTTP-Abfrageinhalt. Die Funktionen sind unter anderem:

- Einrichten von HTTP-Methode, URL, Request Header und Request-Inhalte für jede Abfrage.
- [Hinzufügen einer Authentifizierung (Basic/NTLM/Digest/OAuth)]([LINK_URL_4]) oder von [Client-Zertifikaten]([LINK_URL_5]), um Zugriff auf geschützte APIs zu erhalten.
- [Definieren von Assertions (Prüfpunkten) für jede Antwort]([LINK_URL_6]), um HTTP-Statuscode, Inhalt (basierend auf Klartext, JSON-Inhalt oder XML-Inhalt), Abfragedauer und mehr zu verifizieren.
- Extrahieren von Inhalt aus der Antwort, aus den Antwort-Headern sowie aus Cookies und [Speichern dieses Inhalts in Variablen]([LINK_URL_7]). Diese Variablen können in späteren Schritten verwendet werden, um neue URLs, Abfrage-Header usw. zu erzeugen.
- Verwenden globaler Definitionen wie [vordefinierte Variablen]([LINK_URL_8]), [benutzerdefinierte Funktionen]([LINK_URL_9]), [benutzerdefinierte API-Metriken]([LINK_URL_10]) und [Hashing und Codieren]([LINK_URL_11]).

Diese Funktionen stellen sicher, dass deine API sich richtig verhält und innerhalb der von dir spezifizierten Grenzen arbeitet. Dieser schrittweise Ansatz ermöglicht dir, unkompliziert sehr leistungsstarke Szenarien einzurichten. Sofern du weißt, wie deine API sich verhalten sollte, benötigst du keine Programmierkenntnisse, um das API-Monitoring aufzunehmen.

## Ein Multi-Step API Monitoring-Prüfobjekt erstellen

Um ein Multi-Step API Monitoring-Prüfobjekt zu erstellen:

1. Rufe [SHORTCODE_7] API > API-Prüfobjekte einrichten [SHORTCODE_8] auf und klicke auf die Schaltfläche [SHORTCODE_9][SHORTCODE_10].
2. Wähle im Pop-up-Fenster *Wähle einen Prüfobjekttyp aus* zunächst *Multi-Step API* und klicke dann auf die Schaltfläche [SHORTCODE_11] Wähle aus [SHORTCODE_12].  
3. Wenn das Prüfobjekt erstellt wurde, gib ihm einen *Namen*.  
4. Lege das *Überwachungsintervall* fest. Dein [Überwachungsintervall([SHORTCODE_47]) ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.
5. Wechsele zur Registerkarte [SHORTCODE_13] Schritte [SHORTCODE_14], um Informationen für jeden Schritt einzugeben.

Dein neues Prüfobjekt beginnt mit einem (leeren) Schritt. Du kannst Folgendes einrichten:
- Klicke auf [SHORTCODE_15] Füge Abfrage Schritt hinzu [SHORTCODE_16], um zusätzliche Schritte hinzuzufügen.
- Klicke auf das Symbol **>** neben jedem Schritt, um die Details anzuzeigen und zu bearbeiten.
- Klicke auf das **Kopieren**-Zeichen, um eine Kopie eines bestehenden Schritts zu erstellen. 
- Um einen Schritt zu entfernen, klicke auf das **X**-Zeichen.
- Anhand der Schaltflächen *Ein Schritt hoch* und *Ein Schritt runter* kannst du die Reihenfolge der Schritte ändern.

![Beispiel MSA-Schritte]([LINK_URL_12])

## Einen Abfrage-Schritt konfigurieren

Wenn du dir den visuellen Schritte-Editor ansiehst, wirst du den Tab [SHORTCODE_17] Request [SHORTCODE_18] bemerken. Ein Schritt bei einem Multi-Step API Monitoring besteht aus einem vollständigen API-Aufruf (z. B. eine Abfrage und eine Antwort). Bei jedem Schritt kannst du die Abfrage definieren und Uptrends mitteilen, wie es mit der Antwort umgehen soll. Jede Multi-Step API beginnt mit einem leeren Schritt.

### Request

![Details Request-Tab]([LINK_URL_13])

Der Tab **Request** enthält alle benötigten Daten, um eine tatsächliche HTTP-Abfrage in dem Schritt auszuführen. Mindestangaben:

1. Wähle die entsprechende HTTP-Methode, entweder **GET**, **POST**, **PUT**, **PATCH**, **DELETE**, **HEAD** oder **OPTIONS**. [Schreibe uns]([LINK_URL_14]), wenn du eine andere Methode benötigst.
2. Gib die URL für die Abfrage ein. Verwende eine qualifizierte URL, einschließlich des Schemas („[URL_1] oder „[URL_2]), des Domainnamens und Pfads für die API und aller gewünschten Parameter des Abfragestrings.

#### Request Body

Wenn du einen POST, PUT, PATCH, HEAD, OPTIONS, oder DELETE Request angibst, kannst du im Feld **Request Body** spezielle Daten (Payload) als Teil der Abfragedefinition senden. Beispielsweise kannst du einen bestimmten Benutzernamen mit Passwort senden, um ein neues Nutzerkonto zu erstellen.

Dies sind die Datenformate für den Request Body, aus denen du wählen kannst:

- Raw Text – ermöglicht dir, Reintext ohne Formatierung zu senden.
- Lade eine Datei hoch (als Form-Data) – ermöglicht dir, eine Datei (zum Beispiel Bilder und Dokumente aus der [Vault]([LINK_URL_15])) im Form-Datenformat zu senden.
- Lade eine Datei hoch (als Binary) – ermöglicht dir, eine Datei (zum Beispiel Bilder und Dokumente aus der [Vault]([LINK_URL_16])) in einem einfachen Binär-Datenformat zu senden.
- Multipart Form – ermöglicht dir, mehrere Typen von Inhalten in unterschiedlichen Formaten (wie Reintexteinträge oder Dateien aus der [Vault]([LINK_URL_17])) gleichzeitig zu senden.

In den meisten Fällen und abhängig vom ausgewählten Datenformat wird der richtige [INLINE_CODE_1] Request Header-Wert automatisch ausgefüllt (zum Beispiel [INLINE_CODE_2]), damit der Server deine Daten korrekt identifizieren, lesen und verarbeiten kann. Du kannst auch den [INLINE_CODE_3] Request Header selbst angeben. Dies wird im nächsten Abschnitt des Artikels behandelt.

#### Request Headers [ANCHOR_1]

Eine HTTP-Abfrage enthält üblicherweise einige Request Header, um das Format der gesendeten Daten zu spezifizieren oder näher zu beschreiben, welche Art Antwort erwartet wird. Bei der Einrichtung eines Abfrageschritts wirst du bemerken, dass bestimmte Request Header automatisch hinzugefügt wurden. Diese Header bestehen aus einem Standard-Set abhängig von deinem Abfragetyp (beispielsweise ist das Header-Set für GET-Abfragen ein anderes als das Set für POST-Abfragen). Um einen Standard-Header zu überschreiben, füge einfach einen neuen Header mit anderen Werten hinzu, aber gib ihm genau denselben Namen, wie dem vorherigen.

[SHORTCODE_1] **Hinweis:** Aus Gründen der Optimierung wurde **Connection: Keep-Alive** aus der Liste der Standard-Abfrage-Header entfernt. In Hintergrundprozessen erfüllt der Abfrage-Header bereits das Standardverhalten für HTTP/1.1 und wird nicht mehr für HTTP/2 und HTTP/3 unterstützt. [SHORTCODE_2]

Neue Header kannst du auch durch Ausführen der folgenden Schritte hinzufügen:

1. Klicke auf die Schaltfläche [SHORTCODE_19]Request Header hinzufügen[SHORTCODE_20], um einen Namen und Wert für einen Request Header einzugeben.
2. Gib Content-Type als den Header-Namen ein.
3. Der entsprechende Header-Wert hängt von den Daten ab, die du sendest. Die meisten Inhaltstypen sind [INLINE_CODE_4] für JSON-Daten, [INLINE_CODE_5] für XML-Daten und [INLINE_CODE_6] für Webform-Daten.

Wenn deine API erfordert, dass du eine Authentifizierung einfügst, integriere einen Header [INLINE_CODE_7] zusammen mit den richtigen Daten im Feld Wert.

![Beispiele von Request Headern]([LINK_URL_18])

Die Abbildung oben zeigt ein Beispiel eines Abfrageschritts. Beachte Folgendes:

- Es ist eine POST-Abfrage an [INLINE_CODE_8]
- Das Header-Standard-Set für diese Abfrage ist:
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
- Die Werte für den Header [INLINE_CODE_11] werden beim Senden der Abfrage bestimmt.
- Die manuellen Header [INLINE_CODE_12] und [INLINE_CODE_13] wurden hinzugefügt, um jeweils das Datenformat anzugeben und die erforderlichen Anmeldedaten bereitzustellen.
- Das standardmäßige [INLINE_CODE_14] wurde überschrieben.
- Der Request Body enthält [INLINE_CODE_15]-Inhalte mit einigen [Variablen]([LINK_URL_19]).

#### Authentifizierung

Viele APIs sind geschützt und nur nach Angabe von Anmeldedaten zugänglich. Wenn deine API eine Authentifizierung auf HTTP-Protokollebene nutzt, wähle die Art der Authentifizierung (Basic, NTLM oder Digest) und gib den zugehörigen Benutzernamen und das Passwort ein. Alternativ kannst du eine OAuth-basierte Authentifizierung anhand separater Schritte einrichten. [Weitere Informationen zur Einrichtung von einer integrierten oder benutzerdefinierten Authentifizierung]([LINK_URL_20]).

#### Ein Credential Set aus der Vault nutzen

Es ist möglich, an jeder Stelle auf das [Anmeldedaten-Set in der Vault]([LINK_URL_21]) als Teil eines Request Bodys oder Request Headers oder als Wert deiner Benutzername-Passwort-Kombination unter *Authentifizierung* Bezug zu nehmen. Um auf ein Vault Item Bezug zu nehmen, setze die folgende Syntax ein: [INLINE_CODE_16] oder [INLINE_CODE_17], abhängig vom erforderlichen Wert. Du findest die [INLINE_CODE_18] , indem du zu dem Vault Item mit dem Credential Set (Anmeldedaten-Set) navigierst. Kopiere den letzten Teil der URL in die URL-Leiste deines Browsers.

![Beispiele für Bezugnahme auf Vault Items]([LINK_URL_22])

#### TLS-Versionen festlegen

Transport Layer Security (TLS) ist ein Sicherheitsprotokoll, das Verbindungen zwischen Website und Server authentifiziert, verschlüsselt und schützt. Durch Aktivieren des Kontrollkästchens *Nur bestimmte TLS-Versionen zulassen* in deinem MSA-Prüfobjekt kannst du bestimmte TLS-Versionen während des TLS-Handshakes für die HTTP-Verbindung auswählen. Du kannst das Kontrollkästchen auch deaktivieren, wenn keine Einschränkungen erforderlich sind.

Alle [Uptrends Checkpoints]([LINK_URL_23]) unterstützen TLS 1.1 und TLS 1.2. Auswahl der Option TLS 1.3 limitiert die Checkpoint-Auswahl auf solche Checkpoints mit TLS 1.3-Fähigkeit. Obwohl TLS 1.1 noch verfügbar ist, wird es nicht empfohlen.

![Kontrollkästchen TLS-Version bei MSA-Prüfobjekten]([LINK_URL_24])

#### HTTP-Version festlegen

Die Option **HTTP-version** lässt dich steuern, welche HTTP-Version die Checkpoint-Server bei einer Anfrage nutzen: Verwende die Option, um sicherzustellen, dass die Server effektiv hinsichtlich Kompatibilität, Leistung und Sicherheit mit der API kommunizieren.

![HTTP-Version]([LINK_URL_25])

Standardmäßig ist die Option **HTTP-Version** nicht aktiviert. Das heißt, der Server wird automatisch die höchste unterstützte HTTP-Version nutzen, die verfügbar ist. Ersatzweise wird mindestens HTTP/1.1 genutzt.

Derzeit ist HTTP/3 an einigen Checkpoint-Standorten verfügbar. Dies wird bald auf weitere Standorte ausgeweitet.

[SHORTCODE_3] **Hinweis:** Die HTTP-Version lässt dich nur eine Version auswählen, während **TLS Version(en)** unterstützt die Auswahl mehrerer Versionen.
[SHORTCODE_4]

### cURL Requests importieren [ANCHOR_2]

Es ist auch möglich, cURL Requests direkt zu importieren, um Schritte zu erstellen, ohne sie manuell zu erstellen. Das geschieht folgendermaßen:

1. Klicke im **visuellen Schritte-Editor** (auf dem Tab [SHORTCODE_21]Schritte[SHORTCODE_22] bei den Prüfobjekteinstellungen) des Multi-Step API-Prüfobjekts, bei dem du einen Schritt auf Basis eines cURL-Befehls importieren möchtest, auf [SHORTCODE_23]cURL-Import[SHORTCODE_24], um den Importassistenten aufzurufen.
2. Klicke auf [SHORTCODE_25]Weiter[SHORTCODE_26].
3. Füge deine cURL Commandline Statement(s) ein. Nehmen wir beispielsweise an, dass wir einen Schritt einfügen möchten anhand des cURL Statements:

[CODE_BLOCK_1]

Dies ist ein Request, um eine Reservierung auf unserer Test-Urlaubs-Website, [GalacticResorts.com]([LINK_URL_26]), zu erstellen.

Du kannst mehrere Schritte zugleich hinzufügen, indem du mehrere cURL-Befehle eingibst.

4. Sofern erforderlich gib das Befehlsformat an. In den meisten fällen wird „Auto-Erkennung“ ausreichen.
5. Klicke auf [SHORTCODE_27]Weiter[SHORTCODE_28].
6. Klicke im letzten Schritt des Assistenten auf [SHORTCODE_29]Schritte generieren[SHORTCODE_30].

Das Ergebnis für den genannten cURL-Befehl dieses Beispiels sieht folgendermaßen aus:

![Ergebnis cURL-Import]([LINK_URL_27])

Der Prüfobjekttyp Multi-Step API unterstützt nicht alle Optionen, die in der cURL Commandline aufgeführt wurden. Die nicht unterstützten Optionen werden automatisch entfernt. Achte also darauf, den Schritt zu testen, um sicherzustellen, dass er wie erwartet funktioniert.

### Response

Die Registerkarte Response enthält alle Optionen zur Ausführung von Checks bei den Antwortdaten (anhand von Prüfpunkten/Assertions) und zum Verarbeiten der Daten in Vorbereitung auf den nächsten Schritt (anhand von Variablen).

![Antwort-Tab]([LINK_URL_28])

#### Assertions

Die Definition der Schritte und Übergabe der korrekten Daten in diese Schritte ist die Grundlage für eine nutzbringende Einrichtung. Es ist jedoch auch wichtig, die Ergebnisse jedes Schritts zu betrachten. Einfach eine Reihe von URLs aufzurufen, reicht nicht, wenn sie nicht die richtigen Ergebnisse zurückgeben. Assertions helfen bei diesen Statuschecks.

Assertions sind Prüfpunkte, auf die du testen kannst, um zu verifizieren, dass die Antwort in einem bestimmten Schritt wie erwartet ausfällt, zum Beispiel durch Überprüfen des Inhalts oder Verifizieren, dass er innerhalb eines bestimmten Zeitraums erhalten wurde. Wie bei den Variablen gibst du die Quelle für die Überprüfung an, zum Beispiel ein JSON-Merkmal aus dem JSON-Antwortinhalt, eine XPath-Anfrage im XML-Antwortinhalt oder einfach den Statuscode der Antwort, die Dauer oder die Inhaltslänge.

**Weitere Beispiele für Assertions** findest du in unserer [ausführlichen Anleitung zur Definition von Assertions]([LINK_URL_29]).

#### Variablen

Beim Einrichten von mehrstufigen Szenarien ist es wahrscheinlich, dass wenigstens einer der Schritte von dem Input abhängt, der im vorherigen Schritt abgerufen wurde. Durch Erfassen der Eingabe, das temporäre Speichern und die Übernahme in den nächsten Schritten erzeugst du eine natürliche Reihe verbundener Schritte, ohne programmieren zu müssen.

Variablen ermöglichen genau das! Mit jedem Schritt besteht die Möglichkeit, neue Variablen zu erzeugen und auf gespeicherte Variablen zuzugreifen, die in anderen Schritten erstellt wurden. Auf diese Weise können zuvor erfasste Daten deines Szenarios wiederverwendet werden.

Du kannst definieren, woher die Variablen kommen sollen: Wahrscheinlich ist es ein bestimmter Wert aus JSON- oder XML-Daten, aber die Erfassung von Antwort-Headern oder auch von Daten aus einer Weiterleitung ist ebenfalls möglich. Nachdem eine Variable definiert wurde, kannst du sie an jeder Stelle des mehrstufigen Set-ups verwenden, indem du einen Bezug zu ihrem Namen herstellst: [SHORTCODE_37]{{my-variable}}[SHORTCODE_38].

**Weitere Beispiele von Variablen**: [Variablen definieren und einsetzen]([LINK_URL_30]).

#### Maximale Anzahl von Versuchen [ANCHOR_3]

In einigen Fällen benötigt deine API eventuell etwas Zeit, um bestimmte Abfragen zu verarbeiten, bevor sie mit dem erfolgreichen Ausführen der Aktion antworten kann. Nehmen wir beispielsweise an, du lädst eine Datei zur Bearbeitung in deine API hoch. Während dieser Verarbeitung reagiert die API auf die Abfrage des Status mit [INLINE_CODE_19] in einer JSON-codierten Antwort. Sobald diese Verarbeitung abgeschlossen ist, antwortet die API stattdessen mit [INLINE_CODE_20]. In solchen Fällen kannst du das Prüfobjekt mit der Einstellung **Maximale Anzahl Versuche** anweisen, Abfragen an die API zu senden, bis sie mit „erfolgreich“ antwortet.

Mit dieser Funktion konfigurierst du das Prüfobjekt, den Schritt zu wiederholen, wenn eine oder mehrere Assertions des Schritts (wie etwa [SHORTCODE_39]Response Body in JSON[SHORTCODE_40] [SHORTCODE_41]Ergebnis[SHORTCODE_42] [SHORTCODE_43]Ist gleich[SHORTCODE_44] [SHORTCODE_45]Erfolg[SHORTCODE_46] für das oben genannte Beispiel) fehlschlagen. Du kannst einstellen, wie häufig das Prüfobjekt den Versuch wiederholen soll – bis maximal 50 Wiederholungen. Beachte, dass die Mindestzahl der Wiederholungen zwei beträgt, da die erste Abfrage als erster Versuch zählt.

Zusätzlich hast du die Option, die Zeit zwischen diesen Wiederholungen einzugeben. Die Wartezeit zwischen zwei Versuchen sollte zwischen 500 und 30.000 ms betragen. Sie ist standardmäßig auf 1.000 ms gesetzt. 

Für jeden Schritt kannst du eine Höchstzahl an Wiederholungen zusammen mit einer Wartezeit zwischen diesen Wiederholungen konfigurieren.

Das Prüfobjekt wiederholt den Schritt, bis die angegebene Anzahl Versuche erreicht ist oder bis jede Assertion erfüllt wurde. Dann werden das Prüfobjekt und die Schritte in ihrer Reihenfolge wie gewöhnlich weiter ausgeführt. Wenn die angegebene Anzahl Versuche erreicht ist und eine Assertion immer noch nicht bestätigt wurde, verzeichnet das Prüfobjekt einen Fehler im Prüfobjektprotokoll.

Die Kosten für das MSA-Prüfobjekt ändern sich nicht, gleich wie viele Versuche ausgeführt werden sollen.

## Datei-Uploads konfigurieren

Multi-Step API-Prüfobjekte ermöglichen dir, Dateien aus [deiner Vault]([LINK_URL_31]) als Teil eines deiner Abfrageschritte hochzuladen. Bei jedem HTTP-Schritt, den du im Rahmen eines Multi-Step API Monitorings konfigurierst und der einen Abfrageteil enthält, kann es sich entweder um einen Form-Data- oder Binär-Datei-Upload- oder eine Klartext-Abfrage handeln. Dateien werden als [INLINE_CODE_21] oder binärer Inhalt gesendet. Folge diesen Schritten, um eine Datei als Form-Data hinzuzufügen:

1. [Lade die betreffende Datei]([LINK_URL_32]) in deine Vault hoch. Die Dateigröße beträgt maximal 2 MB. 
2. Füge in den Einstellungen deines Multi-Step API-Prüfobjekts einen Request-Schritt hinzu oder nutze einen bestehenden Schritt, um den Datei-Upload auszuführen. 
3. Setze die Abfrage-Methode auf dem Tab **Request** des Schritts, der den Datei-Upload ausführen soll, auf *POST*, *PUT* oder *PATCH* (je nach Anforderung) und gib die Abfrage-URL ein.
4. Wähle unter **Request Body** die Option *Lade eine Datei hoch (als Form-Data)*. 
5. Klicke auf die dann erscheinende Schaltfläche [SHORTCODE_31]Füge Datei aus Vault hinzu[SHORTCODE_32].
6. Wähle die entsprechende Datei aus der Liste „Vault Datei Upload“ und klicke auf [SHORTCODE_33]Auswählen[SHORTCODE_34].
![Auswahl zum Datei-Upload]([LINK_URL_33])
7. Es ist nicht notwendig, besondere Abfrage-Header hinzuzufügen. Wir setzen automatisch einen Request Header für [INLINE_CODE_22] und versehen [INLINE_CODE_23] mit den korrekten Grenzen.
![Beispiel-Header für Datei-Upload]([LINK_URL_34])

Wenn du eine Datei hochladen möchtest, ohne dass Uptrends [INLINE_CODE_24]-Metadaten zum Request Body hinzufügt, kannst du *Lade eine Datei hoch (als Binary)* unter **Request Body** bei Schritt 4 oben wählen. Wir werden immer noch die entsprechenden Header, die unter **Request Header** aufgeführt sind, automatisch generieren, aber ohne diese speziellen Metadaten zur Abfrage hinzufügen. Somit kann deine API, wenn sie Dateien als rohe Binärdaten erwartet, trotzdem getestet werden.

Bedenke, dass deine API eventuell einen bestimmten Wert für den Dateinamen erwartet. Die Abfrage wird den automatisch erstellten Header **Content-Disposition** enthalten, der über einige Metadaten verfügt. Der Wert für diesen Header enthält den Parameter *Name*. Standardmäßig verwenden wir den Dateinamen, der von dir in der Vault angegeben wurde. Achte darauf, dass der Dateiname, den du vergibst, wenn du die Datei der Vault hinzufügst, dem von deiner API erwarteten Wert entspricht. Wenn deine API zum Beispiel erwartet, dass die hochgeladene Datei den Namen „image“ hat, stelle sicher, dass du „image“ (ohne Dateierweiterung) als den Dateinamen beim entsprechenden Vault Item angibst.

## Einen Wartezeit-Schritt konfigurieren

Wenn du bei dem Prüfobjekt eine Folge von „Request“-Schritten eingefügt hast, wird jeder Schritt ausgeführt, sobald der vorherige abgeschlossen ist – ohne Verzögerung. Die sofortige Ausführung kann jedoch für einige Situationen zu schnell sein.

Ein Beispiel ist eine API-Methode, die als Abfrage zur Erstellung einer Berichtsdatei dient. Die API initiiert einen im Backend ablaufenden Vorgang, der die Berichtsdatei erzeugt, und instruiert den Nutzer, eine zweite Abfrage zu senden, um diese neue Datei herunterzuladen. Die Erzeugung dieser Datei kann ein paar Sekunden dauern, sodass der Nutzer einige Sekunden warten sollte, bevor er eine zweite Abfrage sendet. Wenn die zweite Abfrage zu früh gesendet wird, könnte der Vorgang fehlschlagen, da die Berichtsdatei möglicherweise noch nicht komplett erstellt wurde.

In dieser Situation ist es wichtig zu warten, bevor die zweite Abfrage ausgeführt wird. Zu diesem Zweck kann ein Wartezeit-Schritt eingesetzt werden. Diese Art von Schritt ermöglicht dir, die Anzahl Millisekunden für das Warten festzulegen. Um beispielsweise drei Sekunden zu warten, gib 3000 Millisekunden als Wartezeit ein. Diese Wartezeit wird in den Gesamtzeitwerten des Prüfobjekts enthalten sein.

Um einen Wartezeit-Schritt hinzuzufügen, klicke einfach auf [SHORTCODE_35] Füge Wartezeit Schritt hinzu [SHORTCODE_36] und gib die Anzahl Millisekunden für die Wartezeit ein. Du kannst den Wartezeit-Schritt anhand der Pfeil-Schaltflächen bei „Ein Schritt hoch/runter“ an die richtige Position deines Szenarios verschieben.

Die Wartezeit für einen Wartezeit-Schritt ist auf 60 Sekunden beschränkt: Ein Wartezeit-Schritt ist nicht dazu gedacht, eine lange Aufgabe zu überwachen, die mehrere Minuten oder Stunden dauert. Wenn das Prüfobjekt die maximale Gesamtzeit zur Ausführung überschreitet, wird die Prüfung unterbrochen und meldet einen Fehler.

Das Hinzufügen eines Warteschritts ist kostenlos. Der Preis eines Multi-Step API-Prüfobjekts basiert lediglich auf der Anzahl der „Request“-Schritte.

[SHORTCODE_5] **Hinweis:** Die Dauer der Ausführung aller Schritte deines Prüfobjekts darf 4 Minuten (insgesamt) nicht überschreiten. Benötigt das Prüfobjekt länger als 4 Minuten, um von Anfang bis Ende ausgeführt zu werden, wird das Ergebnis einen Fehler zurückgeben. In solchen Fällen macht es möglicherweise Sinn, deine Requests auf mehrere Prüfobjekte zu verteilen, sofern möglich. [SHORTCODE_6]

## Multi-Step Monitoring – Ergebnisse, Fehler und Warnmeldungen

Multi-Step API-Prüfobjekte verhalten sich wie alle anderen Prüfobjekte. Jede Überprüfung erscheint im Prüfobjektprotokoll und zeigt ausführliche Informationen für jeden einzelnen Schritt. Für jeden Schritt besteht diese Information aus Folgendem:

- die **Gesamtdauer** des Schritts (in Millisekunden)
- die **URL**, die während des Schritts aufgerufen wurde
- den **HTTP-Statuscode**, der zurückgegeben wurde
- dem Ergebnis für jede **Assertion** (in Ordnung oder Fehler)
- dem **Abfrage-Header und -Inhalt**, die wir gesendet haben
- dem **Abfrage-Header und -Inhalt**, die wir erhalten haben

Wenn bei einem Schritt ein Problem auftritt oder wenn einer der definierten Prüfpunkte nicht in Ordnung ist, wird das Prüfobjekt einen Fehler melden. Wie üblich können diese Fehler Warnmeldungen basierend auf den von dir festgelegten Meldedefinitionen ausgeben.