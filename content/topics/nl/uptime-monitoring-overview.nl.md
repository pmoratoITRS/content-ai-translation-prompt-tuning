{
  "hero": {
    "title": "Overzicht Uptime Monitoring"
  },
  "title": "Overzicht Uptime Monitoring",

  "summary": "Welke soorten uptime controleregels biedt Uptrends en hoe kunt u deze instellen?",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/overzicht-uptime-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview",
  "tableofcontents": true,
  "sectionlist": true
}

**Uptime-controleregels** zijn een van de vele [controleregeltypes]({{< ref path="support/kb/basics/monitor-types" lang="nl" >}}) die Uptrends biedt. Uptime-controleregels voeren basiscontroles uit, zoals het controleren van de beschikbaarheid van de website, pagina-inhoud en laadtijd.

In het achtergrondproces krijgt deze controleregel de URL van uw website en stuurt een request naar die URL. Deze controleregel verwacht een respons, waarbij alle paginabronnen van uw website (HTML-document) en een responsstatuscode 200 worden opgehaald. Zodra aan deze vereisten is voldaan, wordt uw website als bereikbaar beschouwd en werkt deze zoals verwacht.

## Uptime-controleregeltypes

U kunt kiezen uit verschillende Uptime-controleregeltypes:

### HTTP- en HTTPS-controleregels

Een **HTTP**-controleregeltype controleert de uptime van HTTP-websites, terwijl het **HTTPS**-controleregeltype zowel de uptime van HTTP- als HTTPS-websites (websites beveiligd met een SSL-certificaat) controleert. 

Sinds kort is het **HTTP**-controleregeltype niet langer beschikbaar voor nieuwe gebruikers. Uptrends heeft de functionaliteit van **HTTPS**-controleregels uitgebreid om de beschikbaarheid van HTTP-websites te kunnen blijven controleren. Zie [Overzicht HTTP- en HTTPS-controleregels]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-and-https-overview" lang="nl" >}}) voor meer informatie.

### Netwerkservercontroleregels {id="network-server-monitors"}

Er zijn twee hoofdnetwerkserver-controleregels waaruit u kunt kiezen:

- **Ping**  — controleert de beschikbaarheid en uptime van elk IP-adres dat buiten uw firewall bereikbaar is.  
- **Connect**  — controleert de beschikbaarheid en uptime van uw netwerk door een low-level TCP-verbinding met een specifieke poort uit te voeren.

Voor meer informatie, zie [Overzicht Netwerkcontroles]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="nl" >}}) en [Een netwerk-controleregel instellen]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="nl" >}}).

### Databaseserver-controleregels

Uptrends biedt twee hoofdtypes controleregels, **Microsoft SQL** en **MySQL**, om de beschikbaarheid en uptime van specifieke databases te controleren. Zie [Databaseserver-controleregels]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/database-server-monitors" lang="nl" >}}) voor meer informatie.

### Mailserver-controleregels

Uptrends biedt drie hoofdtypes mailserver-controleregels waaruit u kunt kiezen:

- Simple Mail Transfer Protocol (SMTP)
- Post Office Protocol (POP3)
- Internet Message Access Protocol (IMAP)

Zie [Mailserver-controleregels]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/mail-server-monitors" lang="nl" >}}) voor meer informatie.

### Geavanceerde beschikbaarheids-controleregels

Uptrends biedt geavanceerdere beschikbaarheids-controleregels die worden gebruikt voor dataoverdrachten:

- File Transfer Protocol (FTP) en Secure File Transfer Protocol (SFTP) — controleert de beschikbaarheid en uptime van uw [FTP- en SFTP-controleregels]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ftp-and-sftp" lang="nl" >}}).
- Een Domain Name System (DNS) — controleert of de DNS-configuratie werkt en beschikbaar is zoals verwacht.
- Een Secure Sockets Layer (SSL)-certificaat — controleert of uw SSL-certificaten altijd geldig en niet verlopen zijn.

## Credits

Uptime-controleregels gebruiken Uptime-credits waarmee u controleregels kunt creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="nl" >}}) voor meer informatie.