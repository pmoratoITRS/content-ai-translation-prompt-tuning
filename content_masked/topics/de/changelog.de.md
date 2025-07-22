{
  "hero": {
    "title": "API Changelog"
  },
  "title": "API Changelog",
  "summary": "Lies über die Änderungen, Aktualisierungen und Verbesserungen der Uptrends API",
  "url": "[URL_BASE_TOPICS]api/changelog",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "type": "[FRONTMATTER_TYPE]"
}

{{[HTML_TAG_1]}}

Die Funktionen der Uptrends API werden mit der Zeit verbessert und erweitert. Dementsprechend werden wir neue Endpunkte und Methoden für neue Funktionen hinzufügen.

Bei der Einrichtung neuer Funktionen achten wir darauf, immer rückwärtskompatibel zu bleiben. Änderungen sind jedoch nicht immer vermeidbar und eine neue Version der API wird eventuell nicht mit dem Code kompatibel sein, den du bisher geschrieben und genutzt hast. Schaue regelmäßig im API Changelog nach, um über alle Änderungen auf dem Laufenden zu sein und diese, falls notwendig, zu berücksichtigen.

Zur Dokumentation der API lies unsere Artikel in der Kategorie [Uptrends API]([LINK_URL_1]).

Sollten dich die Änderungen an der Uptrends Anwendung interessieren, schaue in unserem [allgemeinen Changelog]([LINK_URL_2]) nach.

## Mai 2025

### Neue Code-relevante Änderung: auslaufende API-Felder

Im Rahmen unserer laufenden Bemühungen, die Uptrends API zu optimieren, werden bestimmte Felder bei den folgenden [Prüfobjekt]([LINK_URL_3])-Endpunkten ab **27. August 2025** nicht fortgeführt:

- [INLINE_CODE_1] und [INLINE_CODE_2] [INLINE_CODE_3]
- [INLINE_CODE_4], [INLINE_CODE_5] und [INLINE_CODE_6] [INLINE_CODE_7]
- [INLINE_CODE_8] und [INLINE_CODE_9] [INLINE_CODE_10]

Die folgenden nicht fortgesetzten Felder werden nun als [Fehlerbedingungstypen]([LINK_URL_4]) unter dem Array [INLINE_CODE_11] behandelt. Zugehörige Felder werden in einen einzelnen Eintrag zusammengeführt und ersetzen die vorherige Nutzung als eigenes Feld:

| Nicht fortgesetzte Felder | Ersetzt mit Feld |
|--|--|
| [INLINE_CODE_12], [INLINE_CODE_13]| [SHORTCODE_1] [LoadTimeLimit1]([LINK_URL_5]) |
| [INLINE_CODE_14], [INLINE_CODE_15] | [LoadTimeLimit2]([LINK_URL_6]) |
|[INLINE_CODE_16], [INLINE_CODE_17] | [TotalMaxBytes]([LINK_URL_7]) |
|[INLINE_CODE_18], [INLINE_CODE_19] | [TotalMinBytes]([LINK_URL_8]) | 
|[INLINE_CODE_20], [INLINE_CODE_21] | [PageElementMaxSizeWithPercentage]([LINK_URL_9]) |
|[INLINE_CODE_22], [INLINE_CODE_23] | [PageElementFailedWithPercentage]([LINK_URL_10])
|[INLINE_CODE_24], [INLINE_CODE_25] | [HttpStatus]([LINK_URL_11]) |

Unten ist ein Beispiel einer aktualisierten API-Antwort. Es empfiehlt sich, deine API-Aufrufe anzupassen, sodass sie das [INLINE_CODE_26]-Array enthalten. Das entspricht der neuesten API-Struktur und gewährleistet eine korrekte API-Funktion.

[CODE_BLOCK_1]

### Private Checkpoint-Status-Update

Der Endpunkt [INLINE_CODE_27] gibt nun das Feld [INLINE_CODE_28] aus, das alle Alarminformationen zum Checkpoint des Servers enthält. Weitere Informationen findest du in der [Uptrends API v4 Private Locations Checkpoint Status Dokumentation]([LINK_URL_12]).

## April 2025

### Einführung der Private Locations API

Wir haben ein neues Set an API-Endpunkten aufgenommen, damit du die Konfiguration deiner Private Locations besser handhaben kannst. Das umfasst den Status und Checkpoint-Informationen. Weitere Informationen findest du in der [Uptrends API v4 Private Locations Dokumentation]([LINK_URL_13]).

## März 2025

### Update MonitorGroup API 

Der Endpunkt [INLINE_CODE_29] gibt nun die Anzahl Credits pro [Prüfobjekttyp]([LINK_URL_14]) aus:
- [INLINE_CODE_30] – gibt die Anzahl genutzter Credits für [Uptime- bzw. Basic-Prüfobjekte]([LINK_URL_15]) aus.
- [INLINE_CODE_31] – gibt die Anzahl genutzter Credits für [Browser- bzw. Full-Page Check (FPC)-Prüfobjekte]([LINK_URL_16]) aus.
- [INLINE_CODE_32] – gibt die Anzahl genutzter Credits für [Transaktionsprüfobjekte]([LINK_URL_17]) aus.
- [INLINE_CODE_33] – gibt die Anzahl genutzter Credits für [Multi-Step API (MSA)-]([LINK_URL_18]) und [Postman]([LINK_URL_19])-Prüfobjekte aus.

Zuvor gab die MonitorGroup API nur die Gesamtzahl verfügbarer Credits der Gruppe für jede Prüfobjektkategorie aus. Jetzt wird auch die Anzahl genutzter Credits der Gruppe für jede Prüfobjektkategorie angegeben.

## Februar 2025

### Cursor-Parameter-Wert – Update

Der API Cursor-Parameter ist ein Zeichenkettenwert, der als Zeiger funktioniert, um Daten aus der API-Antwort zu übergehen.

Cursor wurden nun in ein längeres Zeichenkettenformat aktualisiert, um eine sicherere Datenhandhabung zu gewährleisten. Alle neu erstellten Cursor haben nun das neue Format. Die alten Cursor-Formate werden weiterhin bis 1. April 2025 funktionieren. Danach können die alten Cursor nicht mehr verwendet werden. Es wird empfohlen, neue Cursor-Werte zu erzeugen, damit sie aktuell sind und wie erwartet funktionieren.

Beachte, dass der Cursor-Parameter an den Endpunkten der [Monitor Check API]([LINK_URL_20]) und Alert API verfügbar ist.

## Januar 2025

### Update Monitor API

Der Endpunkt [INLINE_CODE_34] gibt nun [INLINE_CODE_35] aus, was Datum und Uhrzeit der letzten Aktualisierung des Prüfobjekts enthält. Zuvor konnte nur [INLINE_CODE_36] mit der Monitor API abgerufen werden.

## November 2024

### VaultItem – Update

[INLINE_CODE_37], [INLINE_CODE_38] und [INLINE_CODE_39] akzeptieren nun das Feld [INLINE_CODE_40], wenn das Vault Item [One-Time Passwort Konfiguration]([LINK_URL_21]) erstellt oder aktualisiert wird. Das neue Feld akzeptiert *Hex*- oder *Base32*-Zeichenfolgen als Wert. Das Base32-Format ist die Standardverschlüsselungsmethode, wenn das „SecretEncodingMethod‟-Feld nicht definiert ist.

## September 2024

### VaultItem – Update

[INLINE_CODE_41] gibt nun ein zusätzliches Datenelement, [INLINE_CODE_42] aus. Es enthält Informationen darüber, welche Elemente oder Prüfobjekte jedes Vault Item verwenden.

## August 2024

### Checkpoints API

Der API-Endpunkt [INLINE_CODE_43] gibt nun auch Server privater Standorte an.

### VaultItem – Update

Der Endpunkt [INLINE_CODE_44] kann nun genauso viele Daten für jedes Vault Item zurückgeben, ähnlich wie Daten für ein einzelnes Item über [INLINE_CODE_45] ausgegeben werden.

## Juni 2024

### Code-relevante Änderung: die /Register API für Operatoren, die sich nur per SSO anmelden

Für die Uptrends API ist eine [Registrierung]([LINK_URL_22]) erforderlich, bevor sie genutzt werden kann. Operatoren können eine Reihe API-spezifischer Anmeldedaten erzeugen, basierend auf ihren üblichen Uptrends Anmeldedaten. Es gibt zwei Möglichkeiten, eine Reihe von API-Anmeldedaten zu registrieren:

– Operatoren können über die normale Uptrends Benutzeroberfläche einen API-Nutzer auf der Registerkarte [SHORTCODE_2]API-Management[SHORTCODE_3] in den Operator-Einstellungen hinzufügen.
– Alternativ können sich Operatoren in der API selbst für Anmeldedaten registrieren, in dem sie eine [INLINE_CODE_46]-Anfrage unter Angabe ihrer regulären Uptrends Anmeldedaten eingeben.

Ab diesem Update steht Operatoren, die sich nur mit [Single Sign-on (SSO) anmelden können]([LINK_URL_23]), die zweite Möglichkeit, sich für API-Anmeldedaten zu registrieren, nicht mehr zur Verfügung, da sie keine „regulären“ Uptrends Anmeldedaten haben. 

In diesem Fall empfehlen wir, einen separaten Operator-Account einzurichten und diesen zur Registrierung für API-Anmeldedaten zu verwenden. 

## Oktober 2023

### Code-relevante Änderung: Metrik Seitenladezeiten für browserbasiertes Monitoring

**Hinweis:** Das Folgende ist eine **code-relevante Änderung** für die *MonitorCheck* API. Die Änderung ist ab **Mittwoch, 8. November** in Kraft.

Die Uptrends [MonitorCheck API]([LINK_URL_24]) kann verwendet werden, um detaillierte Informationen zu den einzelnen Überwachungen der Prüfobjekte abzurufen. Für das browserbasierte Monitoring kann das [Wasserfalldiagramm]([LINK_URL_25]) über den Befehl [INLINE_CODE_47] abgerufen werden. Dies gibt alle Wasserfall-Messwerte wieder, einschließlich [Core Web Vitals]([LINK_URL_26]) und [W3C Navigation Timings]([LINK_URL_27]), sofern sie in den Prüfergebnissen enthalten sind. 

Derzeit gibt die MonitorCheck API Core Web Vitals und W3C Navigation Timings in zwei getrennten JSON-Objekten aus: [INLINE_CODE_48] und [INLINE_CODE_49]. Zukünftig werden diese beiden Objekte zu einem einzelnen Array, [INLINE_CODE_50], wie folgt kombiniert:

[CODE_BLOCK_2]


### Variablen von Meldedefinitionen über die API angeben

Bei der Konfiguration der [Alarmierung]([LINK_URL_28]) über eine [benutzerdefinierte Integration]([LINK_URL_29]) in Uptrends können Operatoren die Benutzeroberfläche verwenden, um bestimmte erforderliche Variablen [in der Eskalationsstufe der Meldedefinition]([LINK_URL_30]) anzugeben, statt diese in den Optionen der Integration einzurichten. Damit können Nutzer eine einzige Integration für verschiedene Szenarien einsetzen, zum Beispiel Warnmeldungen für unterschiedliche Prüfobjekte an verschiedene Teams, aber mit demselben Nachrichteninhalt.

Wenn die Option zur Angabe von Variablen in der Eskalationsstufe in den Integrationseinstellungen aktiviert wird, müssen die Variablen stattdessen bei der Einrichtung der Integration bei den Einstellungen der Meldedefinition konfiguriert werden. Dafür erscheint ein zusätzliches Textfeld in der Liste zur Auswahl der Integration in den Meldedefinitionseinstellungen. 

Bisher war diese Option bei der Konfiguration von Meldedefinitionen über die API nicht verfügbar. Wir haben eine neue Option zur Abfrage [INLINE_CODE_51] (mit der du angibst, welche Integrationen zu welcher Eskalationsstufe der Meldedefinition gehören) hinzugefügt. Das neue Merkmal lautet:

[CODE_BLOCK_3]

Dieses Merkmal ist äquivalent mit der Option in der Benutzeroberfläche der Anwendung:

![Konfigurieren einer Integrationsvariable in einer Meldedefinition]([LINK_URL_31])


## September 2023

### Änderung: IPv6-Adressen von Checkpoints

Zuvor wurden bei der Nutzung der Checkpoint API zum Abrufen von Checkpoint-Informationen die IPv4-Adressen des Checkpoints als einfache Liste in einem Array angezeigt. Die IPv6-Adressen (sofern vorhanden) waren eine Liste von Objekten. Beispielsweise wurden die IP-Adressen des Checkpoints Amsterdam früher wie folgt gelistet:

[CODE_BLOCK_4]

Uptrends hat dies nun vereinheitlicht und gibt IPv6-Adressen auf dieselbe Weise an:

[CODE_BLOCK_5]

Beachte bitte, dass dies bei einem automatisierten Abruf von Checkpoint-IP-Adressen, z. B. für Whitelists, eine **code-relevante Änderung** sein kann.

## Januar 2023

Version 3 unserer API wird seit Januar 2023 nicht länger unterstützt und wurde deaktiviert. Die [Dokumentation zu Version 3]([LINK_URL_32]) ist noch in unserer Knowledge Base zu finden, aber diese API-Version selbst wird nicht mehr funktionieren. Wenn du noch aktive Skripte oder Prozesse hast, die API Version 3 verwenden, werden diese einen Fehler melden, und wir empfehlen, so bald wie möglich zu Version 4 zu wechseln. Der [Upgrade-Leitfaden]([LINK_URL_33]) enthält weitere Infos zum Wechsel von API v3 nach API v4.

**Update Mai 2023:** Die Dokumentation für Version 3 unserer API wurde entfernt und kann nicht mehr aufgerufen werden. 

## Dezember 2022

### Erstellungsdatum mithilfe der API überwachen

Der [/Monitor Endpunkt]([LINK_URL_34]) kann unter anderem verwendet werden, um die Prüfobjektdefinitionen deines Accounts (über *GET /Monitor/{monitorGuid}*) abzurufen. Die Antwort wird nun auch ein [INLINE_CODE_52] enthalten, welches angibt, wann das Prüfobjekt eingerichtet wurde.


## November 2022

### Kleine Änderungen am /Register Endpunkt

Wie du vielleicht [über unser reguläres Changelog]([LINK_URL_35]) erfahren hast, haben wir mit diesem Release die Option hinzugefügt [Uptrends API Anmeldedaten über die Benutzeroberfläche zu erstellen und zu entfernen]([LINK_URL_36]). Um Uptrends API v4 mit der Benutzeroberfläche in Einklang zu bringen, haben wir zum /Register Endpunkt zwei neue Optionen hinzugefügt:

– Es ist jetzt möglich, wahlweise eine Beschreibung bei der Registrierung eines neuen API-Accounts über das Feld [INLINE_CODE_53] einzugeben.
– Es ist jetzt möglich, einen API-Account für einen anderen Operatoren zu erstellen, sofern der anfragende Operator über ausreichend Rechte verfügt, indem er das Feld [INLINE_CODE_54] verwendet.

## September 2022

### Bevorstehende Änderung: Zeitstempel bei der API-Antwort

Derzeit werden Zeitstempel, die Teil der Antwort bei einer [API v4]([LINK_URL_37])-Abfrage sind, auf zwei Weisen in JSON konvertiert:

– Millisekundenzählung ist gleich 0:  _2022-09-21T13:08:47_
– Millisekundenzählung ist nicht gleich 0: _2022-09-21T13:08:47[HTML_TAG_2].682[HTML_TAG_3]_

Dieser Unterschied kann zu Problemen führen, wenn Daten mit diesen Zeitstempeln automatisch geparst und verarbeitet werden. Daher gibt es nun eine Änderung: Die Millisekunden werden nicht mehr in den Zeitstempeln einer API-Antwort angezeigt. Zukünftig werden alle Zeitstempel das Format _2022-09-21T13:08:47_ haben.

## Juni 2022

### Zukünftig neue IP-Adressen von Checkpoints 

Die Uptrends API kann für einen Abruf von Checkpoint-IP-Adressen, z. B. für automatisierte Whitelists, genutzt werden. Zuvor enthielten Antworten zu solchen Anfragen hinsichtlich unserer [Checkpoint API]([LINK_URL_38]) in der Regel eine aktuelle Liste aller derzeitigen Checkpoint-IP-Adressen. Uptrends’ Checkpoint-Netzwerk ist jedoch laufend Änderungen unterworfen. Neue Checkpoints werden hinzugefügt, bestehende Checkpoints entfernt oder verschoben oder IP-Adressen ändern sich. Das konnte bedeuten, dass die Listen der IP-Adressen, die du für eine Whitelist verwenden wolltest, bis zur nächsten Synchronisation veraltet war und zu unnötigen Fehlern führte.

Wir listen nun zukünftige Checkpoint-IP-Adressen, sodass sie in der API-Antwort enthalten sind. Auf diese Weise wird deine Whitelist vorzeitig aktualisiert.

### Beziehungen in der Statistics API

Antworten der [Statistics API]([LINK_URL_39]) (die verwendet werden kann, um statistische Daten für Prüfobjekte oder Prüfobjektgruppen abzurufen) enthalten nun einige zusätzliche Metadaten zur Antwort. Das neue Array [INLINE_CODE_55] besteht bereits bei anderen API-Endpunkten. Es enthält zusätzliche Informationen zu Abfragen wie zum Beispiel einen Link zur Monitor- oder MonitorGroup API-Abfrage, um weitere Informationen über das Prüfobjekt oder die Prüfobjektgruppe selbst abzurufen.


[CODE_BLOCK_6]

## Mai 2022

### Fehlerbehebung bei Start-/Ende-Parametern in der Statistics API

Unsere API unterstützt das Abrufen statistischer Prüfobjektdaten mit der [Statistics API]([LINK_URL_40]). Du kannst entweder einen voreingestellten Zeitraum festlegen, für den die Daten abgerufen werden (mit verfügbaren Werten wie [INLINE_CODE_56]) oder einen benutzerdefinierten Zeitraum mit Start- und Ende-URL-Parametern angeben. Zum Beispiel ruft [INLINE_CODE_57] statistische Daten zum angegebenen Zeitraum für ein einzelnes Prüfobjekt ab.

Es gab ein Problem, bei dem die Minutenangabe der Start- und Ende-Zeitstempel nicht richtig abgebildet wurden, was zu unvollständigen (oder sogar leeren) Ergebnissen bei der API-Antwort führen konnte. Dieses Problem wurde nun behoben.

## Februar 2022

### Update: Status API

Die [Status API]([LINK_URL_41]) ruft Statusinformationen für ein bestimmtes Prüfobjekt ab, basierend auf der letzten Prüfung des Prüfobjekts. Dieser Endpunkt kann als Information zu aktuellen Prüfobjektstatus verwendet werden. Wir haben die Antwort erweitert und sie umfasst nun einen Wert für [INLINE_CODE_58] – Informationen über den [Messwert Gesamtzeit]([LINK_URL_42]) für die letzte Prüfung des Prüfobjekts.

## Januar 2022

### Ausgabe der korrekten Monitoring-Daten

Wenn ein Operator, der nicht Administrator ist, mit der [Berechtigung **Daten anzeigen**]([LINK_URL_43]) für ein bestimmtes Prüfobjekt diese Prüfobjektdefinition über die API (mit [INLINE_CODE_59]) abgerufen hat, enthielt die Antwort nicht alle relevanten Daten. Dies war nicht korrekt, da dieselben Daten bereits über die Benutzeroberfläche verfügbar waren, aber nicht über die API. Das wurde nun korrigiert. Wenn diese Operatoren nun ein Prüfobjekt abrufen, sind die Werte  *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive* und *GenerateAlert* enthalten.

## August 2021

### Ankündigung: Auslaufen von Version 3 unserer API

Die [Uptrends API]([LINK_URL_44]) unterstützt derzeit zwei Versionen nebeneinander. Version 3 ist eine ältere Vorgängerversion unserer API und wir empfehlen derzeit, Version 4 zu verwenden. Version 4 verfügt über einen sehr viel vollständigeren Funktionsumfang und ist seit Längerem Entwicklungsschwerpunkt. Wir haben daher entschieden, Version 3 unserer API auslaufen zu lassen. Sie wird ab **Dezember 2022** nicht länger verfügbar sein. 

Für Kunden, die derzeit noch Version 3 unserer API verwenden, weisen wir darauf hin, dass diese Version noch bis zum genannten Zeitpunkt unterstützt wird. Wir empfehlen jedoch, so bald wie möglich das Upgrade zu Version 4 durchzuführen. Um dir dabei zu helfen, haben wir einen [Upgrade-Leitfaden für den Wechsel von API v3 nach v4]([LINK_URL_45]), verfasst, der die Hauptunterschiede zwischen den zwei API-Versionen und wie du sie in deinen Skripten und deiner Software überbrückst behandelt. 

## Juli 2021

### Code-relevante Änderung: Änderung an der Antwort der OperatorGroup Autorisierung

Mit der Uptrends API kannst du [Berechtigungen für Operatoren und Operator-Gruppen]([LINK_URL_46]) verwalten und Rollen wie **Administrator** oder **Ansprechpartner Finanzen** zuweisen sowie **Zugriff auf Infra** gewähren. Die [OperatorGroup API]([LINK_URL_47]) enthält mehrere Optionen, um Berechtigungen abzurufen, hinzuzufügen oder zu löschen. 

Wir haben die Art und Weise geändert, wie Berechtigungen für Operator-Gruppen in der API angegeben werden. Dies kann sich auf eine von dir eingerichtete automatisierte Erstellung, Entfernung oder den Abruf von Informationen über Berechtigungen von Operator-Gruppen auswirken. Derzeit erfolgt der Abruf von Informationen zu Berechtigungen durch:

[INLINE_CODE_60]

was eine Antwort wie unten dargestellt zurückgibt (abhängig von den für die jeweilige Operator-Gruppe eingerichteten Berechtigungen):

[CODE_BLOCK_7]

In Zukunft wird diese Abfrage eine vereinfachte Antwort zurückgeben, bei der die Berechtigungen, aber keine weiteren Informationen gelistet werden. In der Antwort werden weder [INLINE_CODE_61] noch [INLINE_CODE_62] (Letzteres wird komplett entfernt, Berechtigungen werden nicht länger über eine eigene GUID verfügen) enthalten sein. Die Antwort wird folgendermaßen aussehen:

[CODE_BLOCK_8]

Eine neue Berechtigung für eine Operator-Gruppe wird derzeit hinzugefügt durch Senden einer POST-Anfrage an:

 [INLINE_CODE_63] 
 mit einem Request Body, der einen "AuthorizationType" angibt. Die derzeit verfügbaren Werte für AuthorizationType für Operator-Gruppen findest du in der [Uptrends API Swagger UI]([LINK_URL_48]), unter **Models** (unten) und dann **OperatorGroupAuthorizationType**.
 
 Zukünftig kann eine neue Berechtigung für eine Operator-Gruppe hinzugefügt werden durch Senden einer POST-Anfrage an: 

 [INLINE_CODE_64] 
 ohne einen Request Body einzufügen. 

Das Löschen einer Berechtigung aus einer Operator-Gruppe wird derzeit durch Senden einer DELETE-Anfrage an [INLINE_CODE_65] durchgeführt, aber wie oben erwähnt wird „authorizationGuid‟ als Einheit nicht länger unterstützt und kann nicht mehr genutzt werden. Stattdessen kannst du Berechtigungen löschen, indem du dich direkt mit ihrem Namen in der Anfrage-URL auf sie beziehst: [INLINE_CODE_66]

## Februar 2021

### Code-relevante Änderung: sensible Werte bei Multi-Step API-Prüfobjekten

Unser [Prüfobjekttyp Multi-Step API]([LINK_URL_49]) ermöglicht dir, mehrere aufeinanderfolgende HTTP-Anfragen auszuführen, bei denen jede neue Anfrage ein oder mehrere abgerufene Datenteile aus vorherigen Anfragen nutzt, um die Aufgabe auszuführen. Häufig gehört zu einem der Schritte das Senden von Anmeldedaten, um Zugriff auf eine bestimmte Ressource zu erhalten. Früher wurden diese Anmeldedaten als vordefinierte Variablen zur Prüfobjektdefinition hinzugefügt und als *sensibel* gekennzeichnet.

Um die Sicherheit der Handhabung solcher Anmeldedaten zu steigern, geben wir diese Vorgehensweise auf. Stattdessen werden Anmeldedaten in der [Vault]([LINK_URL_50]) abgelegt. Mit dieser Änderung wird bei Multi-Step API-Prüfobjekten die Kennzeichnung vordefinierter Variablen als sensibel überflüssig und wir werden diese Funktion entfernen.

Dies wird sich darauf auswirken, wie du über unsere API Multi-Step API-Prüfobjekte erstellen und mit ihnen interagieren kannst. Derzeit enthält die Prüfobjektdefinition für diesen Prüfobjekttyp ein Array „PredefinedVariables“, bei dem jede einzelne Variable über einen booleschen Wahr-Falsch-„Sensibel“-Ausdruck verfügt. In nächster Zukunft wird dieser boolesche Ausdruck aus der Definition entfernt. Wenn du ein Multi-Step API-Prüfobjekt in deinem Account mithilfe der Uptrends API erstellen oder aktualisieren möchtest, wird dieses Feld nicht mehr verfügbar sein. 

### Änderung: umbenanntes Routing
 
 Bei Uptrends APIv4 ist die Vorgehensweise, Routes zu benennen, nicht einheitlich. In den meisten Fällen werden Singular-Begriffe genutzt, aber in einigen Fällen waren diese auch in der Plural-Form. Die Route enthält nun nur Singular-Elemente, 
 zum Beispiel [INLINE_CODE_67] statt [INLINE_CODE_68].

 Aus Gründen der Rückwärtskompatibilität unterstützen wir weiterhin die alten Routes.

{{[HTML_TAG_4]}}
