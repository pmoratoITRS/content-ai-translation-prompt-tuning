{
  "hero": {
    "title": "Prüfobjekt Mailserver"
  },
  "title": "Prüfobjekt Mailserver",
  "summary": "Mit den Uptrends SMTP und POP3 Überwachungen sind Sie der erste, der bei E-Mail Server Problemen hiervon erfährt.",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/pruefobjekt-mailserver",
  "translationKey": "https://www.uptrends.com/support/kb/mail-server-monitors",
  "tableofcontents": true
}

E-Mail sind wichtig für Sie und Ihr Geschäft, und daher genauso wichtig ist der ordnungsgemäße Zustand und die Verfügbarkeit Ihres E-Mail-Servers. Selbst wenn Ihr E-Mail-Server für nur einen kurzen Zeitraum nicht verfügbar ist, kann ein solcher Ausfall Produktivitätseinbußen sowie Reputations- oder Einnahmeverluste für Ihr Geschäft bedeuten. Mit Uptrends können Sie ein Monitoring der SMTP-, POP3- oder IMAP-Mailserver durchführen und sicherstellen, dass Ihr Team sofort weiß, wenn es ein Problem mit den Mailservern gibt.

## Verfügbarkeits-Monitoring

Neben Server-Crashes können DNS-Probleme oder andere Konfigurationsprobleme verursachen, dass Mailserver nicht richtig funktionieren. Mit Mailserver-Prüfobjekten wissen Sie sofort, wenn ein Problem auftritt.

## Performance Monitoring

Viele Dinge können die Performance beeinträchtigen, einschließlich Netzwerk-Traffic und fehlerhafte Hardware. Indem Sie Antwortzeiten festlegen, wissen Sie genau, wann Ihre Mailserver Probleme verursachen.

## Einrichtung des Prüfobjekts

Die Einrichtung der Prüfobjekte für Mailserver unterscheidet sich nicht von der Einrichtung deiner anderen Prüfobjekte. Hinweise, wie du ein neues Prüfobjekt einrichtest, findest du im Artikel [Prüfobjekte hinzufügen]({{< ref path="support/kb/basics/adding-monitors" lang="de" >}}). Prüfobjekteinrichtung für Mailserver:

1.  Klicke auf {{< AppElement type="button" >}}+ Prüfobjekt hinzufügen{{< /AppElement >}} unter {{< AppElement type="menuitem" >}}Überwachung{{< /AppElement >}} im Hauptmenü.
2.  Wähle SMTP oder POP3 im Feld **Typ**.
3.  Gib deinem Prüfobjekt einen **Namen**.
4.  Lege das **Überwachungsintervall** fest.
5.  Markiere die Kontrollfelder **Aktiv** und **Alarme generieren**, sofern sie noch nicht aktiviert sind.
6.  Gib entweder die IP-Adresse oder den Domainnamen für deinen Mailserver im Feld **Netzwerk Adresse** ein.
7.  Prüfe, dass die **Port**-Nummer korrekt ist.
8.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.

Mit dieser Grundeinstellung sendet dir Uptrends Warnmeldungen, wenn dein Server nicht erreichbar ist. Du kannst auch die Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} nutzen, um Alarme für die Antwortzeit einzurichten. Du kannst zudem Authentifizierungsinformationen auf der Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}} eingeben, wenn Uptrends versuchen soll, sich beim Server anzumelden (erfahre, wie [Uptrends deine Authentifizierungsdaten schützt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="de" >}})).
