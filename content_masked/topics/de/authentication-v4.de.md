{
  "hero": {
    "title": "Authentifizierung (Version 4)"
  },
  "title": "Authentifizierung (Version 4)",
  "summary": "Einen API-Account registrieren und wie die Authentifizierung funktioniert",
  "url": "[URL_BASE_TOPICS]api/authentifizierung-v4",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Jede API-Methode erfordert eine Authentifizierung über deinen API-Account. Also musst du zunächst einen Account erstellen. Dieser API-Account basiert auf deinem Uptrends Account, ist aber nicht dasselbe. Der Vorteil separater Accounts liegt darin, dass du deine API-Anmeldedaten beispielsweise in einem Skript verwenden kannst und nicht deine Anmeldedaten für deinen Uptrends Account preisgeben musst.

## API-Accounts über die Einstellungen des Operators verwalten

API-Accounts werden direkt bei dem Operator verwaltet, zu dem die Accounts zugehören. Sieh dir [API-Accountmanagement für Operatoren]([LINK_URL_1]) an, um Hinweise für das Hinzufügen oder Entfernen eines API-Accounts zu erhalten. In den meisten Fällen ist es der einfachste Weg, einen API-Account zu registrieren und nachzuhalten, welcher Operator welche Accounts hat, da für einen Operator mehrere Accounts registriert werden können.

## Einen API-Account über API-Aufrufe registrieren [ANCHOR_1]

Es besteht auch die Option, einen API-Account mithilfe der Uptrends API zu erstellen. Dies ist eine frühere, weniger komfortable Möglichkeit der Registrierung. Sie funktioniert dennoch, und ein Account, der auf diese Weise erstellt wird, wird auf der Registerkarte [SHORTCODE_5] API-Management [SHORTCODE_6] des Operators angezeigt.

Die **POST**-Methode des **/Register**-Endpunkts ermöglicht dir die Erstellung eines neuen API-Accounts. In den beschriebenen Schritten verwendest du die Swagger-Umgebung, um direkt auf die API zuzugreifen. Der API-Account, den du erstellst, wird nicht verfallen. Du musst dies also nur einmal durchführen.

1.  Rufe die [Swagger-Seite]([LINK_URL_2]) auf und finde und erweitere die [POST /Register]([LINK_URL_3])-Methode.

2.  Klicke auf die Schaltfläche zum Ausprobieren (*Try it out*), um mit der Erstellung eines API-Accounts zu beginnen.

3.  Klicke auf die Schaltfläche *Execute*.

4.  Dein Browser wird dich nun nach deinen Uptrends Operator-Anmeldedaten fragen. Gib die E-Mail-Adresse und das Passwort für deine übliche Anmeldung bei Uptrends ein und klicke auf OK.

5.  Nachdem die Anmeldedaten deines Uptrends Accounts verifiziert wurden, enthält der Antworttext Werte für den Benutzernamen und das Passwort.  

[CODE_BLOCK_1]              

    Dies sind die Anmeldedaten für deinen neuen API-Account.

6.  Klicke auf die Schaltfläche *Download* im Antworttext, um diese Anmeldedaten an einem sicheren Ort zu speichern. Verwende sie zur Authentifizierung bei allen anderen API-Aufrufen.

[SHORTCODE_1]
**Hinweis**: Der API-Account wird nicht erlöschen. Wenn du jedoch die Anmeldedaten verlierst, können sie nicht wiederhergestellt werden. Dann wirst du einen neuen Account erstellen müssen.
[SHORTCODE_2]

## Nutzung deines API-Accounts [ANCHOR_2]

Nun hast du einen API-Account und kannst ihn verwenden. Wenn du Swagger nutzt, kannst du deine Anmeldedaten in einem Dialogfenster angeben. Bei Software wie cURL oder Postman gibst du sie als Header ein und es erfolgt die erforderliche Codierung. Wenn du deine eigenen Skripte verwendest, musst du zunächst deine Anmeldedaten codieren. Siehe im Abschnitt [Basic-Authentifizierung]([LINK_URL_4]) nach.

[SHORTCODE_3]
**Hinweis**: Denke daran, dass dieser API-Account mit deinem Uptrends Operator-Account verknüpft ist. Er wird also dieselben Berechtigungen wie bei deinem Uptrends Account verwenden.
[SHORTCODE_4]

### Swagger-Umgebung

Wenn du API-Methoden in der Swagger-Umgebung ausführst, wird ein [SHORTCODE_7]Sign in[SHORTCODE_8]-Fenster (das sich auf [URL_1] bezieht) angezeigt, in das du deinen Benutzernamen und das Passwort des API-Accounts eingeben musst.

### Basic-Authentifizierung [ANCHOR_3]

Die Account-Anmeldedaten müssen immer anhand des Basic-Authentifizierungsmodells kodiert und der API als besonderer Header übergeben werden.

Software wie cURL oder Postman übernimmt die erforderliche Codierung der Anmeldedaten und übergibt sie korrekt. Solltest du dein eigenes Skript schreiben, musst du folgenden Header beim API-Aufruf mitgeben:

[INLINE_CODE_1]

Die Anmeldedaten müssen base64-codiert sein. Folge diesen Schritten, um den Header zu erstellen:

1.  Definiere eine Zeichenfolge mit der Syntax [INLINE_CODE_2]. Ersetze [INLINE_CODE_3] und [INLINE_CODE_4] mit deinen Anmeldedaten. Es dürfen keine Leerstellen enthalten sein.

2.  Die Zeichenfolge [INLINE_CODE_5] muss base64-codiert sein. Die Codierungsfunktion kann in deiner Software oder Skriptsprache enthalten sein oder du verwendest ein Tool wie [URL_2]

3.  Sobald du die Zeichenfolge codiert hast, erzeuge und nutze einen Header [INLINE_CODE_6], bei dem [INLINE_CODE_7] die base64-codierte Zeichenfolge aus dem vorherigen Schritt ist.
