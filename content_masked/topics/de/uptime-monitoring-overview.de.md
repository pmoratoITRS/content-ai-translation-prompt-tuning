{
  "hero": {
    "title": "Uptime Monitoring – Überblick"
  },
  "title": "Uptime Monitoring – Überblick",
  "summary": "Welche Arten Uptime-Prüfobjekte bietet Uptrends und wie lassen sie sich einrichten?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/uptime-monitoring-ubersicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": true
}

**Uptime-Prüfobjekte** gehören zu den verschiedenen [Prüfobjekttypen]([LINK_URL_1]), die Uptrends bietet. Mit Uptime-Prüfobjekten werden grundlegende Prüfungen wie Testen der Website-Verfügbarkeit, Seiteninhalt und Ladezeit ausgeführt.

Das Prüfobjekt ruft im Hintergrund die URL deiner Website ab und sendet eine Anfrage an diese URL. Das Prüfobjekt erwartet eine Antwort, ruft dabei die komplette Seitenquelle der Website (HTML-Dokument) und den Antwort-Statuscode 200 ab. Sobald diese Anforderungen zufrieden gestellt sind, gilt deine Website als erreichbar und wie erwartet betriebsbereit.

## Uptime-Prüfobjekttypen

Es stehen mehrere Uptime-Prüfobjekttypen zur Auswahl:

### HTTP- und HTTPS-Prüfobjekte

Ein **HTTP**-Prüfobjekttyp prüft auf Verfügbarkeit von HTTP-Websites, ein **HTTPS**-Prüfobjekt prüft auf Verfügbarkeit sowohl von HTTP als auch HTTPS-Websites (Websites, die anhand eines SSL-Zertifikats gesichert sind). 

Der Prüfobjekttyp **HTTP** ist seit Kurzem für neue Nutzer nicht mehr verfügbar. Uptrends hat die Funktionen des **HTTPS**-Prüfobjekttyps erweitert, sodass auf Verfügbarkeit von HTTP-Websites geprüft werden kann. Weitere Informationen findest du unter [HTTP- und HTTPS-Prüfobjekte – Überblick]([LINK_URL_2]).

### Netzwerk-Server-Prüfobjekte [ANCHOR_1]

Es gibt zwei hauptsächliche Netzwerk-Server-Prüfobjekte, die du wählen kannst:

- **Ping**  – prüft die Verfügbarkeit und Betriebsbereitschaft jeder beliebigen IP-Adresse, die außerhalb deiner Firewall erreichbar ist.  
- **Connect** – prüft die Verfügbarkeit und Betriebsbereitschaft deines Netzwerks, indem eine Low-Level-TCP-Verbindung zu einem bestimmten Port erstellt wird.

Weitere Informationen findest du unter [Überblick Netzwerk-Checks]([LINK_URL_3]) und [Ein Prüfobjekt für Netzwerk-Checks einrichten]([LINK_URL_4]).

### Datenbankserver-Prüfobjekte

Uptrends stellt zwei hauptsächliche Prüfobjekttypen bereit, **Microsoft SQL** und **MySQL**, um die Verfügbarkeit und Betriebsbereitschaft bestimmter Datenbanken zu prüfen. Weitere Informationen sind unter [Datenbankserver-Prüfobjekte]([LINK_URL_5]) zu finden.

### Mailserver-Prüfobjekte

Uptrends bietet drei hauptsächliche Mailserver-Prüfobjekte zur Auswahl:

- Simple Mail Transfer Protocol (SMTP)
- Post Office Protocol (POP3)
- Internet Message Access Protocol (IMAP)

Weitere Informationen sind unter [Mailserver-Prüfobjekte]([LINK_URL_6]) zu finden.

### Erweiterte Verfügbarkeitsprüfobjekte

Uptrends bietet fortschrittlichere Verfügbarkeitsprüfobjekte, die für Datentransfers verwendet werden:

- File Transfer Protocol (FTP) und Secure File Transfer Protocol (SFTP) – prüft die Verfügbarkeit und Betriebsbereitschaft von [FTP- und SFTP-Prüfobjekten]([LINK_URL_7]).
- Domain Name System (DNS) — prüft, ob die DNS-Konfiguration wie erwartet funktioniert und verfügbar ist.
- Secure Sockets Layer (SSL)-Zertifikat – prüft, ob deine SSL-Zertifikate immer gültig und nicht erloschen sind.

## Credits

Uptime-Prüfobjekte verwenden Uptime-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]([LINK_URL_8]).