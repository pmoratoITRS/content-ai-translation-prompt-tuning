{
  "hero": {
    "title": "Operatoren hinzufügen oder entfernen"
  },
  "title": "Operatoren hinzufügen oder entfernen",
  "summary": "Einen Operator hinzufügen und einrichten oder einen Operator entfernen. Jeder Operator muss mit Kontakt- und Anmeldeinformationen sowie Zugriffsrechten eingerichtet werden",
  "url": "/support/kb/account/nutzer/operatoren/operator-hinzufuegen-oder-loeschen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/add-or-delete-operator"
}

Der [User Management Hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="de" >}}) von Uptrends ist der Ort, an dem du Operatoren (und Operator-Gruppen) verwaltest.

## Einen Operator hinzuzufügen

1. Navigiere zum [User Management Hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="de" >}}). Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Operator hinzufügen {{< /AppElement >}}.
3. Unter **Operator Einrichtung** kannst du entscheiden, ob du den neuen Operator manuell (innerhalb der Uptrends Anwendung) einrichtest oder ob du eine [Einladung sendest](#by-invitation) und es dem neuen Operator überlässt, seine Anmeldedaten selbst einzugeben.
4. Hast du die *manuelle Account Einrichtung* gewählt, kannst du die E-Mail-Adresse deines neuen Operators, Passwort, vollständigen Namen, Backup-E-Mail-Adresse und Mobiltelefonnummer (beginnend mit einem +-Zeichen und der Ländervorwahl, gefolgt von der Telefonnummer ohne Bindestriche oder Leerzeichen) angeben.
5.  Sofern du alle Konfigurationen für den Operator vorgenommen hast, klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.
6. Danach kannst du dem Operator das Passwort mitteilen. Bei der manuellen Einrichtung wird keine automatische E-Mail gesendet.


Weitere Informationen über alle Optionen der Operator-Einrichtung findest du in den Artikeln unter [Operatoren und Operator-Gruppen]({{< ref path="support/kb/account/users/operators" lang="de" >}}).
### Auf Einladung  {id="by-invitation"}

Die Einladung wird per E-Mail über die *E-Mail*-Einstellung unter **Login Information** gesendet und enthält einen Link, der einen neuen Nutzer zur Passwort-Einrichtung leitet. Die Einladung bleibt 21 Tage aktiv. Danach erlischt der Link in der Einladung.

Du kannst eine Einladung noch einmal versenden, wenn du dem neuen Operator eine Erinnerung daran übermitteln möchtest, dass er seinen Account noch aktivieren muss, oder wenn die erste Einladung erloschen ist.

Du siehst den Status der Einladung auf der Einstellungsseite des Operators.

Eine weitere Möglichkeit, den Status der Einladung zu prüfen, ist die Seite der Operatoren, die du unter {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} findest.  Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operatoren anzeigen {{< /AppElement >}}. Auf der Seite Operatoren gibt es eine Spalte, die das Datum und die Uhrzeit der letzten Anmeldung eines Nutzers und den Status der (ausstehenden) Einladungen angibt. Die Spalte heißt *Letzter Login* und kann folgende Werte enthalten:

   - Zeitstempel der letzten Anmeldung – der Account wurde aktiviert und genutzt.
   - Eingeladen – die Einladung wurde gesendet und ist noch gültig.
   - Einladung abgelaufen – die Einladung wurde versendet, aber 21 Tage sind vergangen, bevor der Nutzer auf den Link in der E-Mail geklickt hat.
   - Nie eingeloggt – die Einladung wurde durch Klicken auf den Link angenommen, aber seitdem hat sich der Nutzer nicht angemeldet.


{{< callout >}} **Hinweis**: Operatoren, die Single Sign-on (SSO) verwenden, können nur per Einladung hinzugefügt werden, wenn Benutzername/Passwort und die SSO-Anmeldeoptionen aktiviert sind. {{< /callout >}}

## Einen Operator entfernen

Um einen Operator zu entfernen:

1. Navigiere zum [User Management Hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="de" >}}). Je nach Accounttyp kann der Weg dahin sich leicht unterscheiden.
  - Rufe bei einem **Enterprise** Account {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen und Subaccounts {{< /AppElement >}} auf.
  - Rufe bei allen anderen Accounts {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.

2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operatoren anzeigen {{< /AppElement >}}, um die vollständige Übersicht der Operatoren in deinem Account anzuzeigen.
3. Klicke in der Liste auf den Namen des Operators, den du löschen möchtest. Gib den Namen, die E-Mail-Adresse oder einen Teil davon in das Suchfeld ein, um die Ergebnisse einzuschränken.
4. Klicke in den Operator-Einstellungen auf {{< AppElement type="deletebutton" >}} Diesen Operator löschen {{< /AppElement >}} unten am Bildschirm.

Der Operator wird daraufhin entfernt. Beachte, dass du nur einen Operator entfernen kannst, wenn er innerhalb des Accounts nicht mit Dashboards, Public Status Pages oder geplanten Berichten verknüpft ist. Im Allgemeinen sind Operatoren, die diese Objekte erstellt haben, ihr Besitzer. In einem solchen Fall kannst du die Objekte entfernen oder einen neuen Besitzer zuweisen oder dich an den [Support]({{< ref path="/contact" lang="de" >}}) wenden.