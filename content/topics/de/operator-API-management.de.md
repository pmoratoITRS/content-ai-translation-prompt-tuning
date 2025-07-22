{
  "hero": {
    "title": "API-Accountmanagement für Operatoren"
  },
  "title": "API-Accountmanagement für Operatoren",
  "summary": "Registrierte API-Nutzer zu einem Operator hinzufügen oder von ihm entfernen",
  "url": "/support/kb/account/nutzer/operatoren/operator-API-management",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-API-management"
}

Wenn du die [Uptrends API]({{< ref path="support/kb/api" lang="de" >}}) nutzen möchtest, benötigst du einen API-Account (was nicht dasselbe ist, wie dein Uptrends Account). Die Anmeldedaten für den API-Account müssen immer anhand des *Basic-Authentifizierungsmodells* übergeben werden, um einen API-Abruf auszuführen. Sieh dir den Artikel [Nutzung deines API-Accounts]({{< ref path="support/kb/api/authentication-v4#usage-API-account" lang="de" >}}) an, um zu erfahren, wie du die Anmeldedaten bei API-Abrufen eingibst.

Die Registerkarte {{< AppElement type="tab" >}} API-Management {{< /AppElement >}} bei den Einstellungen eines Operators ermöglicht dir, alle API-Accounts zu verwalten, die mit diesem jeweiligen Operator verknüpft sind.

{{< callout >}} **Hinweis**: Du kannst Passwörter weder über die Registerkarte *API-Management* noch an anderer Stelle in deinem Account abrufen. Achte darauf, die Passwörter bei der Erstellung eines neuen API-Accounts zu vermerken. {{< /callout >}}

## Einen API-Account hinzufügen 

Um einen neuen API-Account zu einem Operator hinzuzufügen:

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operatoren anzeigen {{< /AppElement >}}.
3. Wähle aus der Liste der Operatoren denjenigen, dem du einen API-Account hinzufügen möchtest.
4. Wechsele zur Registerkarte {{< AppElement type="tab" >}}API-Management{{< /AppElement >}}.
5. Klicke auf {{< AppElement type="buttonPrimary" >}} API-Nutzer hinzufügen {{< /AppElement >}}.
6. Folge dem Assistenten, und achte darauf, das Passwort aufzuschreiben. Der API-Account wird der Liste der API-Nutzer hinzugefügt:

   ![Screenshot Registerkarte API-Management bei einem Operator](/img/content/scr_operator-API-management.min.png)

7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um die beim Operator vorgenommenen Änderungen zu sichern.

Auf der Registerkarte {{< AppElement type="tab" >}} API-Management {{< /AppElement >}} bei den Einstellungen eines Operators kannst du alle API-Accounts sehen, die mit diesem Operator verknüpft sind. Du siehst zudem das Erstellungsdatum und wann der Account zuletzt verwendet wurde. Die folgenden Optionen erscheinen in der Spalte *Zuletzt verwendet*:

- **Unbekannte Nutzung** – wird angezeigt, wenn der API-Account erstellt wurde, bevor die Funktion „Zuletzt verwendet“ verfügbar war.
- **Bislang nicht verwendet** – bedeutet, der API-Account wurde nach Einführung der Funktion „Zuletzt verwendet“ erstellt, aber der Account ist noch nicht genutzt worden.
- **Datum/Uhrzeit** – der Zeitstempel der letzten Nutzung des API-Accounts wird angezeigt, wenn der Account erstellt und genutzt wurde, nachdem die Funktion „Zuletzt verwendet“ eingeführt wurde.

Es gibt noch einen anderen (älteren) Weg, einen API-Account hinzuzufügen, indem du die /Register-Methode der Uptrends API verwendest. Diese Methode wird nicht empfohlen, da sie in den meisten Fällen weniger praktisch ist. Sie funktioniert jedoch weiterhin und die Anweisungen sind unter [Einen API-Account registrieren]({{< ref path="support/kb/api/authentication-v4#register-API-account" lang="de" >}}) zu finden. Ein Account, der über die API hinzugefügt wird, erscheint ebenfalls auf der Registerkarte {{< AppElement type="tab" >}} API-Management {{< /AppElement >}} eines Operators.

 ## Einen API-Account entfernen 

 Um einen API-Account bei einem Operator zu entfernen:

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operatoren anzeigen {{< /AppElement >}}.
3. Wähle aus der Liste der Operatoren denjenigen, bei dem du einen API-Account entfernen möchtest.
4. Wechsele zur Registerkarte {{< AppElement type="tab" >}}API-Management{{< /AppElement >}}.
5. Klicke in der Zeile des Accounts, den du entfernen möchtest, auf die Schaltfläche {{< AppElement type="deletebutton" >}} API-Nutzer entfernen {{< /AppElement >}}.
6. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.
