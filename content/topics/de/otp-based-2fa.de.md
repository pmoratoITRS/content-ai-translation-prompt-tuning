{
  "hero": {
    "title": "Einmal-Passwort-basierte 2FA"
  },
  "title": "Arbeiten mit der OTP-basierten 2FA bei Transaktionen",
  "summary": "Erfahre, wie du eine Einmal-Passwort-basierte 2FA bei deinen Transaktionsprüfobjekten einrichtest.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/otp-basierte-2fa",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/otp-based-2fa"
}

In einer Welt, in der Sicherheit und Schutz persönlicher Daten immer wichtiger werden, möchten sich viele Organisationen nicht mehr nur auf eine Anmeldeaktion für einen sicheren Zugriff auf Webanwendungen verlassen. Um mit größerer Wahrscheinlichkeit feststellen zu können, dass es sich bei einem Anmeldevorgang um einen echten Nutzer handelt, verwenden Webanwendungen nun die mehrstufige bzw. Multi-Faktor-Authentifizierung (MFA), die häufig als Zwei-Faktor-Authentifizierung (2FA) umgesetzt wird, und verlangen vom Nutzer zwei Identitätsnachweise.

Neben der [SMS-basierten 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="de" >}}) unterstützt Uptrends auch die Einrichtung einer 2FA, bei der normale Nutzer einen Code eingeben müssen, den sie von einer Mobilanwendung erhalten. Dieser Ansatz ist als Multi-Faktor-Authentifizierung mit **zeitbasiertem Einmal-Passwort** (Time-based One-Time Password, TOTP oder OTP) bekannt.

Ein solches zeitbasiertes Einmal-Passwort ist üblicherweise nur für kurze Zeit (in der Regel 30 Sekunden) gültig und muss im Rahmen des Authentifizierungsvorgangs bei der Webanwendung eingegeben werden. Diese Codes werden algorithmisch generiert, basierend auf dem aktuellen Zeitstempel und einem **Geheimnis**: einen Wert, den sowohl die Authentifizierungs-App als auch die Webanwendung kennen (sie berechnen also dieselben Werte). Auf diese Weise kann die Webanwendung, wenn der vom Nutzer eingegebene Wert dem erwarteten Wert entspricht, verifizieren, dass der Nutzer Zugang zum selben geheimen Wert hat und dass ihm Zugriff zur Anwendung gewährt werden soll.

## Üblicher Ablauf eines OTP-basierten 2FA-Szenarios

Der Ablauf, den wir bei einem Zwei-Faktor-Authentifizierungsverfahren über ein von einer Mobilanwendung generiertes Einmal-Passwort für eine Webanwendung erwarten:

1. Auf der Anmeldeseite einer Anwendung gibt der Nutzer seine Anmeldedaten in die entsprechenden Felder ein. Dies ist der erste Schritt des 2FA-Identifizierungsablaufs.
2. Nachdem die Anmeldedaten eingegeben wurden, wechselt die Webanwendung in der Regel auf eine neue Seite mit einem Textfeld, in dem das Einmal-Passwort eingegeben werden soll.
3. Der Nutzer öffnet die entsprechende Authentifizierungsanwendung auf seinem Mobilgerät, die einen Code (üblicherweise 6 Ziffern) mit einem Ablaufzähler anzeigen sollte.
4. Der Nutzer gibt diesen Code in der Webanwendung ein und kann mit der Anmeldung fortfahren (sofern der Code der Erwartung der Webanwendung entspricht und noch nicht abgelaufen ist).

## Überblick über die Uptrends Lösung für die OTP-basierte 2FA

Da die OTP-Codes von einem Algorithmus erstellt werden, besteht die einzige Anforderung an ihre Berechnung in der Kenntnis des *Geheimnisses*. Durch Hinzufügen dieses geheimen Werts in der [Vault deines Accounts]({{< ref path="/support/kb/account/vault" lang="de" >}}) können wir den richtigen Wert berechnen, und er kann auf dieselbe Weise verwendet werden, wie du einen Benutzernamen oder ein Passwort [aus der Vault]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="de" >}}) einsetzen würdest.

Anders als die SMS-basierte 2FA kannst du die OTP-basierte 2FA selbst konfigurieren. Beachte, dass du Zugriff auf das *Geheimnis* benötigst – es ist eventuell in deiner 2FA-Konfiguration aufgeführt oder deine Administratoren können es dir nennen. Wenn dein Unternehmen QR-Codes zur Registrierung des OTP in mobilen Apps nutzt, kannst du das Geheimnis auch diesen entnehmen. Solltest du Hilfe benötigen, zögere nicht, dich an unser [Support-Team]({{< ref path="/contact" lang="de" >}}) zu wenden.

## Schritte zur Einrichtung einer OTP-basierten 2FA bei einer Transaktion

1. Neben den regulären Anmeldedaten (die du [in der Vault speichern und von dort abrufen kannst]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="de" >}})) musst du das **Geheimnis** für deine OTP-Einrichtung kennen. Bei dem Geheimnis handelt es sich in Regel um einen alphanumerischen Code, den du deiner OTP-Konfiguration entnehmen können sollest. Alternativ verwendet dein Unternehmen bzw. deine Organisation QR-Codes, um die mobilen Authentifizierungs-Apps zu konfigurieren. Du kannst auch den QR-Codes das Geheimnis entnehmen (Scannen des Codes führt zu einer URL, die das Geheimnis enthält).
2. Sobald du das Geheimnis kennst, musst du es [zur Vault hinzufügen]({{< ref path="/support/kb/account/vault#adding-a-new-item-to-the-vault" lang="de" >}}). Erzeuge im entsprechenden Vault-Bereich ein Vault Item des Typs **One-Time Passwort Konfiguration**.
3. Gib dem Vault Item einen angemessenen Namen (und optional eine Beschreibung) und gib das **Geheimnis** an. Bei Bedarf kannst du den Hashing-Algorithmus, die Anzahl der Ziffern oder den Ablaufzeitraum für die generierten OTP-Codes bearbeiten, aber die Standardwerte sollten in den meisten Fällen korrekt sein.
4. Speichere das Vault Item.
5. Nun ist die OTP Konfiguration zum Einsatz in deinen Transaktionsskripten bereit, auf dieselbe Weise, [wie du andere Anmeldedaten oder Dateien aus der Vault verwendest]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="de" >}}).
6. Füge an der entsprechenden Stelle im Transaktionsskript eine [Übernehmenaktion]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="de" >}}) ein.
7. Füge den richtigen CSS- oder XPath-Selektor hinzu, um auf das Textfeld auf deiner Seite zu verweisen, das den OTP-Code erwartet.
8. Klicke für den Wert auf das Symbol {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} und wähle **Einmal-Passwort**.
9. Wähle die richtige OTP-Konfiguration aus deiner Vault und klicke {{< AppElement type="button" >}} Auswählen {{< /AppElement >}}, um die OTP-Konfiguration für diese Aktion zu verwenden.

![Auswahl der OTP-Konfiguration in einer Transaktion](/img/content/scr-otp-selection-transaction-nm.min.png)

10. Die Transaktion ist nun konfiguriert, um den richtigen OTP-Code zu generieren und ihn in das Textfeld einzugeben. Nun kannst du die Transaktionseinrichtung wie üblich fortsetzen.

## Kosten

Es entstehen keine zusätzlichen Kosten in Verbindung mit einer OTP-basierten 2FA-Einrichtung bei deiner Transaktion. Es fallen die [üblichen Kosten für eine Transaktion]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}) an.
