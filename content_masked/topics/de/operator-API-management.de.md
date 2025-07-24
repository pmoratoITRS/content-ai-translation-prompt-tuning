{
  "hero": {
    "title": "API-Accountmanagement für Operatoren"
  },
  "title": "API-Accountmanagement für Operatoren",
  "summary": "Registrierte API-Nutzer zu einem Operator hinzufügen oder von ihm entfernen",
  "url": "[URL_BASE_TOPICS]account/nutzer/operatoren/operator-API-management",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wenn du die [Uptrends API]([LINK_URL_1]) nutzen möchtest, benötigst du einen API-Account (was nicht dasselbe ist, wie dein Uptrends Account). Die Anmeldedaten für den API-Account müssen immer anhand des *Basic-Authentifizierungsmodells* übergeben werden, um einen API-Abruf auszuführen. Sieh dir den Artikel [Nutzung deines API-Accounts]([LINK_URL_2]) an, um zu erfahren, wie du die Anmeldedaten bei API-Abrufen eingibst.

Die Registerkarte [SHORTCODE_3] API-Management [SHORTCODE_4] bei den Einstellungen eines Operators ermöglicht dir, alle API-Accounts zu verwalten, die mit diesem jeweiligen Operator verknüpft sind.

[SHORTCODE_1] **Hinweis**: Du kannst Passwörter weder über die Registerkarte *API-Management* noch an anderer Stelle in deinem Account abrufen. Achte darauf, die Passwörter bei der Erstellung eines neuen API-Accounts zu vermerken. [SHORTCODE_2]

## Einen API-Account hinzufügen 

Um einen neuen API-Account zu einem Operator hinzuzufügen:

1. Rufe [SHORTCODE_5] Accounteinstellungen > Operator, Gruppen (und Subaccounts) [SHORTCODE_6] auf.
2. Klicke auf [SHORTCODE_7] Alle Operatoren anzeigen [SHORTCODE_8].
3. Wähle aus der Liste der Operatoren denjenigen, dem du einen API-Account hinzufügen möchtest.
4. Wechsele zur Registerkarte [SHORTCODE_9]API-Management[SHORTCODE_10].
5. Klicke auf [SHORTCODE_11] API-Nutzer hinzufügen [SHORTCODE_12].
6. Folge dem Assistenten, und achte darauf, das Passwort aufzuschreiben. Der API-Account wird der Liste der API-Nutzer hinzugefügt:

   ![Screenshot Registerkarte API-Management bei einem Operator]([LINK_URL_3])

7. Klicke auf [SHORTCODE_13] Speichern [SHORTCODE_14], um die beim Operator vorgenommenen Änderungen zu sichern.

Auf der Registerkarte [SHORTCODE_15] API-Management [SHORTCODE_16] bei den Einstellungen eines Operators kannst du alle API-Accounts sehen, die mit diesem Operator verknüpft sind. Du siehst zudem das Erstellungsdatum und wann der Account zuletzt verwendet wurde. Die folgenden Optionen erscheinen in der Spalte *Zuletzt verwendet*:

- **Unbekannte Nutzung** – wird angezeigt, wenn der API-Account erstellt wurde, bevor die Funktion „Zuletzt verwendet“ verfügbar war.
- **Bislang nicht verwendet** – bedeutet, der API-Account wurde nach Einführung der Funktion „Zuletzt verwendet“ erstellt, aber der Account ist noch nicht genutzt worden.
- **Datum/Uhrzeit** – der Zeitstempel der letzten Nutzung des API-Accounts wird angezeigt, wenn der Account erstellt und genutzt wurde, nachdem die Funktion „Zuletzt verwendet“ eingeführt wurde.

Es gibt noch einen anderen (älteren) Weg, einen API-Account hinzuzufügen, indem du die /Register-Methode der Uptrends API verwendest. Diese Methode wird nicht empfohlen, da sie in den meisten Fällen weniger praktisch ist. Sie funktioniert jedoch weiterhin und die Anweisungen sind unter [Einen API-Account registrieren]([LINK_URL_4]) zu finden. Ein Account, der über die API hinzugefügt wird, erscheint ebenfalls auf der Registerkarte [SHORTCODE_17] API-Management [SHORTCODE_18] eines Operators.

 ## Einen API-Account entfernen 

 Um einen API-Account bei einem Operator zu entfernen:

1. Rufe [SHORTCODE_19] Accounteinstellungen > Operator, Gruppen (und Subaccounts) [SHORTCODE_20] auf.
2. Klicke auf [SHORTCODE_21] Alle Operatoren anzeigen [SHORTCODE_22].
3. Wähle aus der Liste der Operatoren denjenigen, bei dem du einen API-Account entfernen möchtest.
4. Wechsele zur Registerkarte [SHORTCODE_23]API-Management[SHORTCODE_24].
5. Klicke in der Zeile des Accounts, den du entfernen möchtest, auf die Schaltfläche [SHORTCODE_25] API-Nutzer entfernen [SHORTCODE_26].
6. Klicke auf [SHORTCODE_27] Speichern [SHORTCODE_28] unten auf der Bildschirmseite.
