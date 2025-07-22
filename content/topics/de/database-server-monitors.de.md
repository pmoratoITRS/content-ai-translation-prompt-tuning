{
  "hero": {
    "title": "Prüfobjekt Database Server"
  },
  "title": "Prüfobjekt Database Server",
  "summary": "Uptrends unterstützen zwei Arten von Datenbank-Server-Monitor: MySQL und Microsoft SQL Server.",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/pruefobjekt-database-server",
  "translationKey": "https://www.uptrends.com/support/kb/database-server-monitors"
}

Sofern Sie Ihren Kunden nicht eine statische Website als Broschüre bieten, stützt sich Ihre Website oder Ihr Webservice auf eine Datenbank, um Inhalte abzurufen, Benutzer zu verwalten und Aufträge zu verarbeiten. Wenn Sie dann die Antwortzeiten Ihrer Datenbank kennen, können Sie dafür sorgen, eine Katastrophe zu vermeiden. Mit dem Prüfobjekt Database Server von Uptrends wissen Sie immer, wenn es ein Problem mit Ihrer Datenbank gibt.

Uptrends nutzt seine {{% Features/Variable variable="CheckpointCount" %}} Checkpoints, um Ihren Datenbankserver von außen zu überwachen.

{{< callout >}}
**Hinweis:** Sollte Ihre Datenbank nicht mit dem Internet verbunden sein, können Sie diesen Prüfobjekttyp nicht verwenden. Sie können jedoch Server hinter Ihrer Firewall mit [Uptrends Infra](/produkte/infra/server-monitoring) überwachen.
{{< /callout >}}

## Wie das funktioniert?

Mit dem Database Monitoring von Uptrends' können Sie Microsoft-SQL-Server und MySQL-Server überwachen. Die Checkpoints von Uptrends versuchen, eine Verbindung zu der IP-Adresse und der Datenbank herzustellen, die Sie auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} angeben. Wenn Sie die Anmeldedaten bereitstellen, wird sich der Checkpoint anmelden. Außer bei Überschreitung der Antwortzeiten, die Sie auf der Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} angeben, wird Uptrends auch einen Alarm auslösen, wenn die Verbindung fehlschlägt oder unterbrochen wird.

{{< callout >}}
**Hinweis:** Sorgen Sie sich wegen der Sicherheit und der Veröffentlichung Ihrer Authentifizierungsinformationen für die Datenbank? Lesen Sie, wie Uptrends Ihre Anmeldedaten schützt: [Verschlüsselung und die Sicherheit Ihrer Website]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="de" >}}).
{{< /callout >}}

Ein Datenbank-Prüfobjekt sendet dir Warnmeldungen auf Grundlage von Antwortzeiten und Konnektivitätsprobleme. Du wirst sehen, dass die Einrichtung des Datenbank-Prüfobjekts ähnlich der Einrichtung eines HTTPS-Prüfobjekts ist, abgesehen von einigen Spezialfeldern. Weitere Informationen zur Einrichtung von Prüfobjekten und Fehlerbedingungen findest du in der [Knowledge Base](/support/kb). Zur Einrichtung eines Database-Prüfobjekts musst du Folgendes wissen:

-   Datenbankname
-   Datenbank-URL oder IP-Adresse und optional
-   Anmeldedaten für die Datenbank

## Prüfobjekteinrichtung

Um ein Datenbank-Prüfobjekt einzurichten

1.  Klicke auf {{< AppElement type="button" >}}+ Prüfobjekt hinzufügen{{< /AppElement >}} unter {{< AppElement type="menuitem" >}}Überwachung{{< /AppElement >}} im Hauptmenü.
2.  Wähle entweder **Microsoft SQL Server** oder **MySQL** unter **Datenbankserver** im Feld **Typ**.
3.  Gib den Domainnamen oder die IP-Adresse für den Datenbankserver im Feld **Netzwerk Adresse** ein.
4.  Fülle die anderen Felder auf der Registerkarte {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} aus.
5.  Gib die erwarteten Antwortzeiten auf der Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} ein.
6.  Klicke auf die Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.
7.  Gib einen **Benutzernamen** und **Passwort** ein, sofern erforderlich.
8.  Gib den **Datenbanknamen** ein.
9.  Wähle die Checkpoints auf der Registerkarte {{< AppElement type="tab" >}}Checkpoints{{< /AppElement >}}.
10.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.


