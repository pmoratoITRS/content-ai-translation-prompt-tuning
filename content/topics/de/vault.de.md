{
  "hero": {
    "title": "Vault"
  },
  "title": "Vault",
  "url": "/support/kb/account/vault",
  "translationKey": "https://www.uptrends.com/support/kb/account/vault"
}

Mit der Vault kannst du Benutzernamen, Passwörter, Zertifikate und andere sensible Informationen, die du als Teil der Prüfobjekteinrichtung benötigst, verwalten.

Diese Funktion ermöglicht dir, deine Anmeldedaten als **Vault Items** zu speichern und für mehrere Prüfobjekte zu nutzen. Wenn du beispielsweise eine Kombination aus `username` und `password` sowohl für Multi-Step API (MSA)- wie auch bei Transaktionsprüfobjekten benötigst, kannst du diese als Vault Item definieren und bei beiden Prüfobjekten verwenden. Wenn an deinen Vault Items Änderungen vorgenommen werden, wendet die **Vault**  diese Änderungen automatisch bei allen Prüfobjekten an, die das Vault Item nutzen. Auf diese Weise kannst du ganz einfach deine Daten an einem Ort organisieren und nachhalten.

Die **Vault** ist in allen Abonnements ohne zusätzliche Kosten verfügbar.

{{< callout >}}
– Installation der Grundvoraussetzungen (einschließlich eines Neustarts, sofern erforderlich). Nutzen der Vault als Hauptspeicherplatz für geheime Schlüssel oder zur Verwaltung allgemeiner Passwörter ist nicht ratsam.
{{< /callout >}}

## Funktionen der Vault

Die **Vault** bietet verschiedene Funktionen, um deine Daten sicher zu speichern. Diese Funktionen umfassen die Definition deiner **Vault Items**, das Gruppieren von Vault Items anhand von **Vault-Bereichen** und das Verwalten von Zugang mithilfe von **Berechtigungen**.

Rufe die **Vault** über {{< AppElement type="menuitem" >}} Accounteinstellungen > Vault {{< /AppElement >}} auf, um die Vault-Funktionen anzuzeigen.

## Vault-Bereiche

Alle in der Vault gespeicherten Elemente sind in **Vault-Bereiche** geordnet. Diese dienen als Haupt-Container oder übergeordnetes Element deiner Vault Items. Alle Uptrends Accounts haben standardmäßig zu Beginn einen Vault-Bereich. Jedes Element, das du speicherst, kann exakt zu einem Bereich gehören. 

Beachte, dass Mitglieder der Administratorgruppe exklusiven Zugang auf alle Elemente haben, die in diesem StandardBereich gespeichert sind. Alle Administratoren können dann jedes Vault Item anzeigen und ändern.  

Einen neuen **Vault Bereich** erstellen:

1. Klicke oben rechts auf der Bildschirmseite auf die Schaltfläche {{< AppElement type="buttonCta" >}}Vault-Bereich hinzufügen{{< /AppElement >}}.
2. Gib unter **Bereichsdetails** den **Namen** des Vault-Bereichs an. Es empfiehlt sich einen Namen zu wählen, der den Zweck und die gespeicherten Elemente eindeutig definiert.
3. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Zu diesem erstellten Bereich kannst du nun [Vault Items]({{< ref path="/support/kb/account/vault#vault-item-types" lang="de" >}}) hinzufügen und   [Vault-Berechtigungen]({{< ref path="/support/kb/account/vault#vault-permissions" lang="de" >}}) vergeben.

Einen **Vault-Bereich** löschen:

1. Klicke auf {{< AppElement type="deletebutton" >}} Lösche diesen Vault-Bereich {{< /AppElement >}}.
2. Klicke im **Bestätigungs-Pop-up** auf {{< AppElement type="deletebutton" >}} Löschen {{< /AppElement >}}, um die Änderung zu bestätigen.

## Vault-Item-Typen

Nach Einrichtung des Vault-Bereichs kannst du nun Vault Items hinzufügen und in Kategorien ordnen. 

Um ein **Vault Item** hinzuzufügen:

1. Klicke oben rechts auf der Bildschirmseite auf die Schaltfläche {{< AppElement type="buttonCta" >}}Vault Item hinzufügen{{< /AppElement >}}. 
2. Fülle auf dem Tab {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} die **Details** aus:

- Name – gib dem Vault Item einen eindeutigen Namen.
- Bereich – wähle einen bestehenden Vault-Bereich aus der Drop-down-Liste.
- Beschreibung – gib eine Beschreibung oder zusätzlichen Anmerkungen zum Vault-Item-Typ ein.
- Typ – wähle aus der Drop-Down-Liste den entsprechenden Vault-Item-Typ. Die **Vault** unterstützt mehrere Datentypen, die du für bestimmte Zwecke speichern kannst. Dies sind die verfügbaren Vault-Item-Typen:

### Login Daten {id="credential-set"}

Dieser Vault-Item-Typ wird als Benutzername-Passwort-Kombination definiert. Du kannst sie bei Prüfobjekttypen verwenden, die Benutzername/Passwort für die Authentifizierung akzeptieren. Beispiele sind Basic-, NTLM-, Digest-Authentifizierungen bei den Prüfobjekten Multi-Step API, Anmeldungen für SMTP, POP3, IMAP, SQL, FTP und SFTP sowie Benutzernamen und Passwörter, die bei Transaktionsskripten verwendet werden.

### Zertifikats-Archiv

Dieser Vault-Item-Typ gestattet das Speichern eines Sicherheitszertifikats in Form eines PKCS #12 Zertifikats-Archivs (in der Regel eine .p12- oder .pfx-Datei), das den privaten und den öffentlichen Schlüssel des Zertifikats enthält. Sobald du die Zertifikatsdatei hochgeladen hast, kannst du sie als Client-Zertifikat in den Prüfobjekten des Multi-Step API Monitorings aufnehmen.

Wenn du über eine Zertifikats-Archivdatei verfügst (in der Regel eine .p12- oder .pfx-Datei), die den privaten und den öffentlichen Schlüssel des Zertifikats enthält, wähle die Datei im Feld **Neues Archiv hochladen**. Die Archive-Datei ist in den meisten Fällen verschlüsselt, daher musst du das zugehörige Passwort im Feld **Archiv-Passwort** eingeben.

### Public Key des Zertifikats

Dieser Vault-Item-Typ sollte verwendet werden, wenn du ein Single Sign-on für Uptrends einrichtest. Dieser Vault-Item-Typ speichert den öffentlichen Schlüssel, der von deinem Identity Provider (IdP) erzeugt wird. Wenn dein IdP eine SAML-Anmeldeanfrage an Uptrends sendet, wird er diese Anfragen unter Nutzung eines Zertifikats signieren. Uptrends nutzt den von dir bereitgestellten öffentlichen Schlüssel (Public Key), um zu verifizieren, dass die eingehende Anfrage tatsächlich von deinem IdP stammt.

Wenn du der Vault einen öffentlichen Schlüssel hinzufügen möchtest, besitzt du wahrscheinlich schon die Public-Key-Datei (in der Regel eine .pem- oder .cer-Datei). Kopiere den Inhalt der Datei, der Base64-codiert sein sollte und als ein X.509 Zertifikat gelesen werden kann, in das Feld **Public Key**.

### Datei {id="file"}

Dieser Vault-Item-Typ kann genutzt werden, um Dateien zu speichern, die dann als Ablaufbestandteil eines [Self-Service Transaction-Prüfobjekts]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) hochgeladen werden können. Weitere Informationen, wie du Datei-Uploads bei deinen Transaktionen einrichtest, findest du in unserer [Dokumentation zu Seiteninteraktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#file-upload" lang="de" >}}) bei Transaktionsprüfobjekten. Wir unterstützen alle Dateitypen bzw. -erweiterungen und wir setzen gegebenenfalls automatisch den richtigen MIME-Typ (eine allgemeingültige Methode im Internet, um die Art und das Format der Datei anzugeben). Die Dateigröße beträgt maximal 2 MB.

Dateien können mit Klicken auf **Choose file** hochgeladen werden. Die Schaltfläche erscheint, wenn der Dateityp des Vault Items aktiviert wird. Die Eigenschaften Name und MIME-Typ werden automatisch ausgefüllt. Wir empfehlen, dem Vault Item einen geeigneten Namen zu geben, sodass du leicht darauf verweisen kannst, wenn du die [Aktionen zum Datei-Upload]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#file-upload" lang="de" >}}) in deiner Transaktion oder im [Multi-Step API-Prüfobjekt]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) einrichtest.

### One-Time Passwort (OTP) oder Time-based One-Time Passwort (TOTP) Konfiguration {id="one-time-password"}

Dieser Vault-Item-Typ speichert einen *geheimen* Wert, der verwendet wird, um einen Einmal-Passwort-Code zu erzeugen. Du kannst dieses Vault Item als alternative Option verwenden, um [eine OTP-basierte Zwei-Faktor-Authentifizierung (2FA)]({{< ref path="support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="de" >}}) für die Überwachung einer [Webanwendung]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}}) einzurichten, für die ein Nutzer einen Code zur Anmeldeverifizierung eingeben muss.

Die folgenden Felder können gemäß deinen Erfordernissen konfiguriert werden:

- Geheime Verschlüsselungsmethode – die Art der für die geheimen Werte verwendeten Verschlüsselung. – Wähle *Hex*, wenn der von dir eingegebene geheime Wert Hex-verschlüsselt ist (aus Hexadezimalziffern von 0–9 und A–F besteht). Wähle andernfalls das Standardformat von Uptrends, *Base32*, wenn der geheime Wert Base-32-verschlüsselt ist (aus 32 Zeichen von A–Z und 2–7 besteht).
- Anzahl Stellen – die Länge des generierten Einmal-Passwort-Codes. Der Code kann *6, 7 oder 8* Stellen haben.
- Ablaufzeitraum (s) – Zeit, in der das Einmal-Passwort gültig ist. Der Ablaufzeitraum kann *1 bis 120* Sekunden umfassen.
- Algorithmus – die Art des verwendeten Secure-Hash-Algorithmus (SHA). Algorithmen können *SHA512* (64-Byte Hash), *SHA256* (32-Byte Hash) oder *SHA1* (20-Byte Hash) sein.

## Vault-Berechtigungen

### Zugang zur Vault auf bestimmte Personen beschränken
In einigen Fällen ist es nützlich, mehr Kontrolle zu haben: Unterschiedliche Operatoren/Gruppen können verschiedene Verantwortungsbereiche haben. Dann ist es empfehlenswert, den Zugriff auf sensible Daten so weit wie möglich zu begrenzen.

Zugriffsregeln für die Vault können für einzelne Vault-Bereiche eingerichtet werden: Du kannst die Berechtigungen zunächst für den Standardbereich der Vault festlegen. Dann kannst du zusätzliche Vault-Bereiche einrichten und bestimmten Operator-Gruppen und einzelnen Operatoren Zugang gewähren.  
  
Für Vault-Bereiche sind zwei Zugriffsstufen verfügbar:

- **Komplette Kontrolle**: Operatoren/Gruppen, die über diese Zugriffsstufe für einen Vault-Bereich verfügen, können zu diesem Bereich Vault Items hinzufügen und entfernen. Sie können Vault Items in diesem Bereich aktualisieren und die Zugriffsberechtigungen für diesen Bereich verwalten.
- **Nur anzeigen**: Diese Zugriffsstufe ist erforderlich, um die Vault Items des Bereichs anzuzeigen, wenn ein Vault-Element für seinen beabsichtigten Zweck gewählt werden soll (etwa ein Zertifikat oder die Anmeldedaten für Prüfobjekteinstellungen oder als Public Key des Zertifikats bei den Einstellungen eines Single Sign-ons). Wichtig: Sobald ein Vault Item als Teil eines Prüfobjekts konfiguriert wurde, werden die Bearbeitungsberechtigungen für das Prüfobjekt auf die Operatoren beschränkt, die über Anzeigeberechtigungen für den zugehörigen Vault-Bereich verfügen. Die Bearbeitungsberechtigungen werden beschränkt, um nicht autorisierten Zugriff auf den Inhalt des Vault Items zu verhindern.

## Vault API Item Management

Ein Vorteil der Einrichtung eines Vault Items besteht darin, dass alle Änderungen an dem Vault Item automatisch auf alle Prüfobjekte angewendet werden, die das Element nutzen. Das ist nützlich, wenn du eine Richtlinie zum Ablauf von in Prüfobjekten verwendeten Passwörtern für die Anmeldedaten einsetzen möchtest. Nehmen wir an, dass diese Anmeldedaten alle x Tage in deiner eigenen Netzwerkumgebung ablaufen. Dann musst du bei Uptrends nur den Inhalt des Vault Items ändern, das diese Anmeldedaten enthält: Die zugehörigen Prüfobjekte werden automatisch die aktualisierten Anmeldedaten verwenden.  
  
Du kannst einen Schritt weitergehen, indem du die Aktualisierung des Vault Items automatisierst. Rufe hierfür Uptrends’ [Vault API]({{< ref path="/support/kb/api/vault-api" lang="de" >}}) von deinem eigenen Backend aus auf, um die Anmeldedaten bei einem bestehenden Vault Item zu aktualisieren. Weitere Informationen findest du in der [Multi-Step API-Dokumentation]({{< ref path="support/kb/api/v4" lang="de" >}}).
