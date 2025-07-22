{
  "hero": {
    "title": "Verschlüsselung und die Sicherheit deiner Website"
  },
  "title": "Verschlüsselung und die Sicherheit deiner Website",
  "summary": "Uptrends verwendet fortschrittliche Verschlüsselungsstandards, um Nutzernamen und Passwörter deiner Website zu schützen. ",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/verschluesselung-und-website-sicherheit",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/encryption-and-your-websites-security"
}

Die Sicherheit deiner Website ist wichtig und Uptrends nimmt dies sehr ernst. Die Benutzernamen und Passwörter, die du Uptrends bereitstellst, werden von uns sorgsam gehandhabt. Sensible Daten werden direkt verschlüsselt, bevor wir deine Daten in unserer Datenbank speichern. Der Zugriff auf die verschlüsselte Version der Daten wird in unserem Unternehmen sehr streng kontrolliert.

## Wie wir deine Daten schützen

Unser System verwendet den [Rijndael](https://de.wikipedia.org/wiki/Advanced_Encryption_Standard)-Algorithmus, auch als **Advanced Encryption Standard (AES)** bekannt, zur Verschlüsselung sensibler Daten. Somit verwenden wir [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) (gemäß RFC 2898), um den Verschlüsselungscode zu erzeugen, mit dem wir die Verschlüsselung ausführen. Wir verwenden 256-Bit-verschlüsselte, willkürliche Werte, um die Salt- und IV-Werte zu generieren, die wir zur Erzeugung des Verschlüsselungscodes und zur Umsetzung der Verschlüsselung benötigen. Zu guter Letzt erfolgt jede Kommunikation zwischen Untersystemen von Uptrends über verschlüsselte und authentifizierte Verbindungen.

## Deine Möglichkeiten

Neben der Verschlüsselung und den Zugriffsrichtlinien auf Uptrends' Seite, empfehlen wir unseren Kunden, selbst Sicherheitsmaßnahmen zu treffen.

### Begrenze Zugriffsberechtigungen

Begrenze die Zugriffsberechtigungen, die du uns über die Anmeldedaten bereitstellst. Idealerweise sollten die Benutzer, die in den Transaktions- und anderen Prüfobjekttypen angegeben werden, über minimale Zugriffsberechtigungen verfügen. Weise diesen Benutzern nur die Berechtigungen zu, die zur Ausführung der Prüfungen erforderlich sind.

### Verwende separate Anmeldedaten

Wir empfehlen dir, separate Benutzerkonten in deinem System zu erstellen, die nur den Zweck haben, diese Monitoring-Aufgaben zu übernehmen. Du solltest diese Benutzerkonten eventuell auf einer Whitelist in Bezug auf die Orte ([IP-Adressen, d. h. die Adressen unserer Checkpoint-Server]({{< ref path="checkpoints" lang="de" >}})) führen, von denen die Nutzung der Anmeldedaten gestattet wird.

### Überwache Anmeldeverhalten

Wenn deine Systeme das Verhalten von angemeldeten Konten protokolliert, ist es im Allgemeinen eine bewährte Methode, dieses Verhalten zu überwachen. Beobachte das Verhalten, um sicherzustellen, dass von den Testkonten nichts ausgeführt wird, das du nicht beabsichtigt hast.

### Aktualisiere Passwörter

Denke daran, die Passwörter in deiner Monitoring-Einrichtung und bei den Transaktions-Monitoring-Skripten (siehe [Transaktionswerte ändern]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="de" >}})) zu aktualisieren, wenn deine Sicherheitsrichtlinie in deinem System deren Ablauf erzwingt. Aktuelle Passwörter verhindern, dass deine Prüfobjekte unnötige Fehler melden.

## Partner für die Sicherheit

Mit unserem beständigen Engagement für Sicherheit und deine aktive Mitwirkung bei der Berücksichtigung dieser Sicherheitsmaßnahmen arbeiten wir gemeinsam auf bestmögliche Weise daran, das Schadenpotenzial auf ein Minimum zu beschränken.
