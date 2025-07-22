{
  "hero": {
    "title": "Einsatz sensibler Transaktionsdaten aus der Vault"
  },
  "title": "Einsatz sensibler Transaktionsdaten aus der Vault",
  "summary": "Wenn du eine Transaktion aufzeichnest, verwahrt Uptrends deine sensiblen Daten in der Uptrends Vault. Erfahre, wie du auf deine sensiblen Daten zugreifst und in deinen Transaktionsskripten verwendest.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/einsatz-sensibler-transaktionsdaten-aus-der-vault",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-sensitive-transaction-data-stored-in-the-vault"
}

In der Uptrends Vault sind die vertraulichen Daten gespeichert, die du für das gegen andere geschützte Monitoring benötigst. Nur Operatoren mit Berechtigung haben Einsicht. Wenn du eine neue Transaktion aufzeichnest oder Uptrends eine ältere Transaktion für Self-Service Transactions umwandelt, schiebt Uptrends automatisch sensible Daten wie etwa Passwörter in die Vault.

## Zugriff auf deine neuen Vault Items

Du kannst auf deine Vault Items unter {{< AppElement type="menuitem" >}} Account Setup > Vault {{< /AppElement >}} zugreifen. In der Vault findest du deine neuen Vault Items unter *Automatically created vault items*. Der Vault-Eintrag hat denselben Namen wie das Prüfobjekt, als du oder unser Support-Team es zuerst erstellt oder konvertiert hat.

## Ändern deiner neuen Vault Items

Wenn du für den Vault-Bereich über die Zugriffs- und Änderungsberechtigungen für einen Vault-Eintrag verfügst, kannst du das Element öffnen und den Namen, die Beschreibung und den Nutzernamen ändern. Das Passwort kann geändert, aber nicht angezeigt werden.

![](/img/content/bce5dcae-cd73-4d14-b45d-5eec4a2f703c.png)

## Ein Vault Item in deinem Skript verwenden

Dein importiertes Skript verweist bereits auf das Vault Item. Alle notwendigen Änderungen an den Anmeldedaten kannst du direkt in der Vault vornehmen. Du kannst ändern, auf welches Vault Item dein Skript zugreift, indem du auf das Auslassungszeichen im Eingabefeld klickst. Der Pop-up-Dialog erlaubt dir den Wechsel auf den Wert Klartext, ein anderes Vault Item zu wählen oder ein neues Vault Item hinzuzufügen.

![](/img/content/scr_MSA_predefined_variables_1.min.png)

In unserem separaten [Artikel](/support/kb/vault) erfährst du mehr über die Nutzung der Vault, um Anmeldedaten, öffentliche Schlüssel und Zertifikate zu schützen.  Das Team vom [Uptrends Support](/contact) hilft dir bei allen Fragen, die du möglicherweise hierzu hast.

