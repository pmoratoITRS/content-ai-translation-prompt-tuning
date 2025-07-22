{
  "hero": {
    "title": "Authentifizierung (Version 4)"
  },
  "title": "Authentifizierung (Version 4)",
  "summary": "Einen API-Account registrieren und wie die Authentifizierung funktioniert",
  "url": "/support/kb/api/authentifizierung-v4",
  "translationKey": "https://www.uptrends.com/support/kb/api/authentication-v4"
}

Jede API-Methode erfordert eine Authentifizierung über deinen API-Account. Also musst du zunächst einen Account erstellen. Dieser API-Account basiert auf deinem Uptrends Account, ist aber nicht dasselbe. Der Vorteil separater Accounts liegt darin, dass du deine API-Anmeldedaten beispielsweise in einem Skript verwenden kannst und nicht deine Anmeldedaten für deinen Uptrends Account preisgeben musst.

## API-Accounts über die Einstellungen des Operators verwalten

API-Accounts werden direkt bei dem Operator verwaltet, zu dem die Accounts zugehören. Sieh dir [API-Accountmanagement für Operatoren]({{< ref path="support/kb/account/users/operators/operator-API-management" lang="de" >}}) an, um Hinweise für das Hinzufügen oder Entfernen eines API-Accounts zu erhalten. In den meisten Fällen ist es der einfachste Weg, einen API-Account zu registrieren und nachzuhalten, welcher Operator welche Accounts hat, da für einen Operator mehrere Accounts registriert werden können.

## Einen API-Account über API-Aufrufe registrieren {id="register-API-account"}

Es besteht auch die Option, einen API-Account mithilfe der Uptrends API zu erstellen. Dies ist eine frühere, weniger komfortable Möglichkeit der Registrierung. Sie funktioniert dennoch, und ein Account, der auf diese Weise erstellt wird, wird auf der Registerkarte {{< AppElement type="tab" >}} API-Management {{< /AppElement >}} des Operators angezeigt.

Die **POST**-Methode des **/Register**-Endpunkts ermöglicht dir die Erstellung eines neuen API-Accounts. In den beschriebenen Schritten verwendest du die Swagger-Umgebung, um direkt auf die API zuzugreifen. Der API-Account, den du erstellst, wird nicht verfallen. Du musst dies also nur einmal durchführen.

1.  Rufe die [Swagger-Seite](https://api.uptrends.com/v4/swagger/) auf und finde und erweitere die [POST /Register](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Register/Register_Post%20)-Methode.

2.  Klicke auf die Schaltfläche zum Ausprobieren (*Try it out*), um mit der Erstellung eines API-Accounts zu beginnen.

3.  Klicke auf die Schaltfläche *Execute*.

4.  Dein Browser wird dich nun nach deinen Uptrends Operator-Anmeldedaten fragen. Gib die E-Mail-Adresse und das Passwort für deine übliche Anmeldung bei Uptrends ein und klicke auf OK.

5.  Nachdem die Anmeldedaten deines Uptrends Accounts verifiziert wurden, enthält der Antworttext Werte für den Benutzernamen und das Passwort.  

```json               
        {
           "UserName": "usernamehere",
           "Password": "passwordhere",
           "AccountId": "123456",
           "OperatorName": "Your name",
           "status": "OK"
        }
```              

    Dies sind die Anmeldedaten für deinen neuen API-Account.

6.  Klicke auf die Schaltfläche *Download* im Antworttext, um diese Anmeldedaten an einem sicheren Ort zu speichern. Verwende sie zur Authentifizierung bei allen anderen API-Aufrufen.

{{< callout >}}
**Hinweis**: Der API-Account wird nicht erlöschen. Wenn du jedoch die Anmeldedaten verlierst, können sie nicht wiederhergestellt werden. Dann wirst du einen neuen Account erstellen müssen.
{{< /callout >}}

## Nutzung deines API-Accounts {id="usage-API-account"}

Nun hast du einen API-Account und kannst ihn verwenden. Wenn du Swagger nutzt, kannst du deine Anmeldedaten in einem Dialogfenster angeben. Bei Software wie cURL oder Postman gibst du sie als Header ein und es erfolgt die erforderliche Codierung. Wenn du deine eigenen Skripte verwendest, musst du zunächst deine Anmeldedaten codieren. Siehe im Abschnitt [Basic-Authentifizierung](#basic-authentication) nach.

{{< callout >}}
**Hinweis**: Denke daran, dass dieser API-Account mit deinem Uptrends Operator-Account verknüpft ist. Er wird also dieselben Berechtigungen wie bei deinem Uptrends Account verwenden.
{{< /callout >}}

### Swagger-Umgebung

Wenn du API-Methoden in der Swagger-Umgebung ausführst, wird ein {{< AppElement type="menuitem" >}}Sign in{{< /AppElement >}}-Fenster (das sich auf https://api.uptrends.com bezieht) angezeigt, in das du deinen Benutzernamen und das Passwort des API-Accounts eingeben musst.

### Basic-Authentifizierung {id="basic-authentication"}

Die Account-Anmeldedaten müssen immer anhand des Basic-Authentifizierungsmodells kodiert und der API als besonderer Header übergeben werden.

Software wie cURL oder Postman übernimmt die erforderliche Codierung der Anmeldedaten und übergibt sie korrekt. Solltest du dein eigenes Skript schreiben, musst du folgenden Header beim API-Aufruf mitgeben:

`Authorization: Basic {{encoded credentials}}`

Die Anmeldedaten müssen base64-codiert sein. Folge diesen Schritten, um den Header zu erstellen:

1.  Definiere eine Zeichenfolge mit der Syntax `username:password`. Ersetze `username` und `password` mit deinen Anmeldedaten. Es dürfen keine Leerstellen enthalten sein.

2.  Die Zeichenfolge `username:password` muss base64-codiert sein. Die Codierungsfunktion kann in deiner Software oder Skriptsprache enthalten sein oder du verwendest ein Tool wie https://www.base64encode.org.

3.  Sobald du die Zeichenfolge codiert hast, erzeuge und nutze einen Header `Authorization: Basic {{encoded credentials}}`, bei dem `encoded credentials` die base64-codierte Zeichenfolge aus dem vorherigen Schritt ist.
