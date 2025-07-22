{
  "hero": {
    "title": "Vault Sicherheit"
  },
  "title": "Vault Sicherheit",
  "url": "/support/kb/account/vault-sicherheit",
  "translationKey": "https://www.uptrends.com/support/kb/account/vault-security"
}

## Vault Sicherheitsfunktion

Uptrends stellt sicher, dass alle sensiblen Daten in der **Vault** verschlüsselt und sicher gespeichert werden.

Jedes Mal, wenn du ein [Vault Item]({{< ref path="/support/kb/account/vault" lang="de" >}}) erstellst, werden deine sensiblen Daten automatisch von der **Vault Engine** verschlüsselt, bevor sie in der Datenbank gespeichert werden. Die **Vault Engine** nutzt eine Verschlüsselungsbibliothek, die dem Advanced Encryption Standard (AES, fortschrittlicher Verschlüsselungsstandard) zur Datenverschlüsselung entspricht. Dieser Prozess umfasst weitere Schritte, zum Beispiel die Generierung von Chiffrierschlüsseln für jede Uptrends Umgebung.

Außerdem nimmt Uptrends die Aktualisierung der Passphrase streng genau und führt sie regelmäßig durch, wodurch das Angriffsrisiko minimiert wird und ein sicherer Zugang zu sensiblen Daten möglich ist. Der Zugriff auf diese Protokolle ist überwacht und sorgfältig eingerichtet. Nutzer können sicher sein, dass die Geheimnisse verborgen und nicht für Mitarbeiter von Uptrends zugänglich sind.

Als Teil von Uptrends Datensicherheit können Geheimnisse, die in der **Vault** gespeichert sind, nicht über die Uptrends Webanwendung oder über die [Vault API]({{< ref path="/support/kb/api/vault-api" lang="de" >}}) abgerufen werden. Bei einem [Credential Set]({{< ref path="/support/kb/account/vault#credential-set" lang="de" >}}) sind nur bestimmte Informationen wie zum Beispiel die Vault Beschreibung, die Vault Item Guid, die Vault Section Guid und der Benutzername zugänglich. Darüber hinaus zeigt Uptrends Geheimnisse als maskierte Werte (`*****`) an. Die Werte können jeder Zeit aktualisiert oder gelöscht werden, werden aber auf keinen Fall entschlüsselt oder angezeigt. 

Uptrends validiert die [Berechtigungen]({{< ref path="/support/kb/account/vault#vault-permissions" lang="de" >}}) und Nutzung jedes Vault Items. Verfügst du nicht über die Berechtigung, auf ein Vault Item zuzugreifen, das bei einem Prüfobjekt genutzt wird, ist die Möglichkeit deaktiviert, die Prüfobjekteinstellungen zu ändern und die Funktion **Jetzt testen** zu nutzen. Dies verhindert, dass nicht autorisierte Nutzer Werte des Vault Items weiterleiten, zum Beispiel indem sie sie an externe Endpunkte wie Webhook-Websites senden. Dies impliziert auch, dass hauptsächlich Nutzer mit Zugriff steuern, welche Prüfobjekte oder Endpunkte Vault Items verwenden. Daher bist du verantwortlich, das unabsichtliche Offenlegen von Geheimnissen zu verhindern.

Auf diese Weise sind all deine sensiblen Daten gegen mögliche Risiken und Schwachstellen geschützt.