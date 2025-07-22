{
  "hero": {
    "title": "FTP and SFTP"
  },
  "title": "FTP und SFTP",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/ftp-and-sftp",
  "translationKey": "https://www.uptrends.com/support/kb/ftp-and-sftp",
  "tableofcontents": true
}

Ihre Kunden verlassen sich auf die Verfügbarkeit Ihrer FTP- (File Transfer Protocol) und SFTP- (Secure File Transfer Protocol) Server, um Dateien von Ihrem Server auf den eigenen Computer herunterzuladen. Die Prüfobjekttypen FTP und SFTP überwachen die Verfügbarkeit Ihrer Server und melden eventuell auftretende Ausfallzeiten. Die Einstellungsmöglichkeiten variieren auf Grundlage Ihrer Wahl des Prüfobjekttyps FTP oder SFTP.

## Welche Aktionen sind mit dem FTP-Prüfobjekt möglich?

Das grundlegende FTP-Prüfobjekt überwacht:

- **Seitenverfügbarkeit und Ladezeit**   
  Durch Aktivieren der Kontrollkästchen **Gesamtzeit** auf der Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} , können Sie prüfen, ob Ihr FTP-Server schnell auf Nutzeranfragen antwortet.
- **Grundlegende Serverauthentifizierung**   
  Prüfen Sie, dass der grundlegende Authentifizierungsprozess richtig funktioniert, indem Sie einen **Benutzernamen** und **Passwort** auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} eingeben.

## Welche Aktionen sind mit dem SFTP-Prüfobjekt möglich?

Das SFTP-Prüfobjekt nutzt eine verschlüsselte Verbindung, um den Dateitransfer durchzuführen. Es ermöglicht eine größere Bandbreite an Testoptionen als das FTP-Prüfobjekt. Ein SFTP-Prüfobjekt kann unterschiedliche Aktionen ausführen. Wählen Sie auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} unter Folgendem aus:

- **Mit SFTP-Server anhand Benutzername und Passwort verbinden**   
  Das Prüfobjekt wird eine Verbindung zum SFTP-Server unter Verwendung des von Ihnen angegebenen Benutzernamens und des Passworts aufbauen. Das Prüfobjekt wird einen Fehler melden, wenn der Server nicht verfügbar ist oder wenn während der Anmeldung ein Fehler auftritt.
- **Prüfen, ob eine Datei auf dem SFTP-Server vorhanden ist**   
  Mit dieser Einstellung verbindet das Prüfobjekt zunächst mit dem SFTP-Server und prüft dann, ob eine bestimmte Datei auf dem Server existiert.
- **Prüfen, ob eine Datei nicht auf dem SFTP-Server vorhanden ist**   
  Manchmal ist es notwendig zu wissen, dass eine bestimmte Datei nicht auf dem SFTP-Server vorhanden ist. Sie können diese Aktion in den Einstellungen des SFTP-Prüfobjekts auswählen.
- **Datei vom SFTP-Server herunterladen**   
  Mit dieser Einstellung wird erst eine Verbindung zum SFTP-Server aufgebaut und überprüft, ob eine bestimmte Datei auf dem Server existiert, bevor die Datei heruntergeladen wird. Die herunterladbare Dateigröße zu diesem Zweck beträgt maximal 1 MB.

## Wir richte ich ein (S)FTP-Prüfobjekt ein?

SFTP (Secure File Transfer Protocol) ist das Standardprotokoll für die Dateiübertragung. SFTP wird verwendet, um Dateien sicher von einem Computer zu einem anderen zu übermitteln. Uptrends ermöglicht dir, deine SFTP-Server für mehr Sicherheit und eine bessere Performance zu überwachen.

Folge diesen Schritten, um das (S)FTP-Prüfobjekt zu erstellen:

1. Klicke auf die +-Schaltfläche im Menü unter {{< AppElement type="menuitem" >}} Überwachung > Prüfobjekteinrichtung {{< /AppElement >}}.
2. Wähle im Pop-up-Fenster *Wähle einen Prüfobjekttyp aus* zunächst den Prüfobjekttyp *FTP* oder *SFTP* und dann klicke auf die Schaltfläche {{< AppElement type="button" >}} Wähle aus {{< /AppElement >}}.
   Das neue Prüfobjekt wird erstellt und du siehst die Konfigurationsseite des Prüfobjekts.
3. Gib deinem Prüfobjekt einen **Namen**.
4. Lege das **Überwachungsintervall** fest. Dein [Überwachungsintervall({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}}) ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.
5. Gib den Domainnamen oder die IP-Adresse deines FTP-Servers in das Feld *Netzwerk Adresse* ein.
6. Wenn der Port deines FTP-Servers anders lautet als der angezeigte Standardwert, ändere diesen in den richtigen Port.
7. Öffne die Registerkarte {{< AppElement type="tab" >}} Erweitert {{< /AppElement >}}.
8. Wähle eine Option im Feld **Aktion**. (Details über die verfügbaren Aktionen findest du auf der [Überblicks]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/ftp-and-sftp" lang="de" >}})seite.)
9. Gib den Dateinamen oder entsprechenden Pfad im Feld **Datei Pfad** an, wenn du eine Datei herunterladen oder verifizieren möchtest.
10. Gib einen **Benutzernamen** und **Passwort** ein, wenn die Benutzerauthentifizierung verwendet werden soll.
11. Sofern du alle Konfigurationen für das neue Prüfobjekt vorgenommen hast, klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}.
      
{{< callout >}}**Hinweis**: Du kannst auch die weiteren [Einstellungen für das Prüfobjekt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="de" >}}) in den Registerkarten oben auf der Prüfobjektkonfigurationsseite erkunden.{{< /callout >}}







