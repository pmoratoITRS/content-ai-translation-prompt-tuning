{
  "hero": {
    "title": "HTTP- und HTTPS-Prüfobjekte – Überblick"
  },
  "title": "HTTP- und HTTPS-Prüfobjekte – Überblick",
  "summary": "Wie das Uptime-Monitoring bei HTTP- und HTTPS-Prüfobjekten funktioniert und die fortgeschrittenen Optionen des HTTP Monitorings",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/http-und-https/http-und-https-ubersicht",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/http-and-https-overview",
  "sectionlist": false
}

{{< callout >}} **Hinweis:** Der Prüfobjekttyp **HTTP** ist für neue Nutzer nicht mehr verfügbar. Uptrends hat die Funktionen des **HTTPS**-Prüfobjekttyps erweitert, sodass auf Verfügbarkeit von HTTP-Websites geprüft werden kann. {{< /callout >}}

Die Prüfobjekte Hypertext Transfer Protocol (HTTP) und Hypertext Transfer Protocol Secure (HTTPS) gehören zu den Uptime-[Prüfobjekttypen]({{< ref path="support/kb/basics/monitor-types" lang="de" >}}), die du im Handumdrehen einrichten kannst. Diese Prüfobjekte verhalten sich ähnlich und ermöglichen dir die Verfügbarkeit von Websites auf Basis von HTTP- und HTTPS-Anfragen zu überwachen.

Die Prüfobjekte führen grundlegende Tests bei deinen `http://` und `https://` Websites von zugewiesenen, weltweiten [Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="de" >}}) aus. Die grundlegenden Prüfungen umfassen die Verifizierung der Statuscodes der Website-Antwort, Seitenladezeit und Laden von Inhaltsressourcen. HTTP- und HTTPS-Prüfobjekte rufen einfach angefragte Ressourcen von der Website ab. Die primäre Funktion besteht darin, festzustellen, ob eine fehlerfreie Antwort vom Webserver erhalten wird, und zu bestätigen, dass die Seite verfügbar ist. Weitere Informationen findest du unter [Funktionsweise eines HTTP-Prüfobjekts]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/how-an-http-monitor-works" lang="de" >}}).

Für eingehendere Prüfungen, um die Leistung und Verfügbarkeit deiner Website genau zu messen, empfiehlt Uptrends den [Full Pagecheck]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) zu nutzen. Einzelheiten dazu findest du im Knowledge-Base-Artikel [Einfache Checks im Vergleich zu Full Pagechecks oder Real-Browser Checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="de" >}}).

## Ein HTTP- oder HTTPS-Prüfobjekt einrichten

Es gibt einen kleinen Unterschied bei der Einrichtung des Uptime HTTP-Prüfobjekts gegenüber einem HTTPS-Prüfobjekt. Da das HTTPS-Prüfobjekt eine erweiterte und gesicherte Version des HTTP-Prüfobjekts ist, umfasst dieses Prüfobjekt einen zusätzlichen Test, um auf SSL-Zertifikatsfehler zu prüfen. Um diese Einstellung zu konfigurieren, wechsle zum Tab {{< AppElement type="tab" >}} Erweitert {{< /AppElement >}} in der Prüfobjekteinrichtung und aktiviere das Kontrollkästchen **SSL Zertifikat Fehler prüfen**.

Aktivieren dieser Option erlaubt deinem HTTPS-Prüfobjekt zu verifizieren, dass das SSL-Zertifikat keine Fehler verursacht. Deaktiviere die Option nur, um Probleme, die vom SSL-Zertifikat erzeugt werden, zu ignorieren. Möchtest du dein SSL-Zertifikat eingehender überwachen, richte den Prüfobjekttyp [SSL-Zertifikat]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="de" >}}) ein, um weitere Tests auszuführen.

Zur Erstellung deines eigenen HTTP- oder HTTPS-Prüfobjekts findest du im Knowledge-Base-Artikel [Ein HTTP- oder HTTPS-Prüfobjekt hinzufügen]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="de" >}}) weitere Informationen.

## Erweiterte HTTP-Einstellungen

Über den Tab {{< AppElement type="tab" >}} Erweitert {{< /AppElement >}} kannst du deine HTTP- oder HTTPS-Prüfobjekteinrichtung weiter anpassen und Folgendes konfigurieren:

- [User Agent]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks#what-is-a-user-agent" lang="de" >}}) 
- Authentifizierung – wenn die zu überwachende HTTP-Ressource eine Authentifizierung im Rahmen der HTTP-Anfrage erfordert, wähle den entsprechenden Authentifizierungstyp (Keine, Basic Authentication, NTLM (Windows) Authentication und Digest Authentication). Gib die Anmeldedaten in den Feldern **Benutzername** und **Passwort** ein. Beachte, dass Uptrends deine Daten immer [verschlüsselt]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="de" >}}).
- Benutzerdefinierte HTTP Request Felder – konfiguriere die Optionen **HTTP Methode** (GET/POST), **HTTP Request Header**, **SSL Zertifikat Fehler prüfen** und **TLS Version(en)**. Weitere Einzelheiten findest du in diesem [Knowledge-Base-Artikel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/monitoring-websites-other-than-the-production-server" lang="de" >}}).
