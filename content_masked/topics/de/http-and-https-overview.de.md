{
  "hero": {
    "title": "HTTP- und HTTPS-Prüfobjekte – Überblick"
  },
  "title": "HTTP- und HTTPS-Prüfobjekte – Überblick",
  "summary": "Wie das Uptime-Monitoring bei HTTP- und HTTPS-Prüfobjekten funktioniert und die fortgeschrittenen Optionen des HTTP Monitorings",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/http-und-https/http-und-https-ubersicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

[SHORTCODE_1] **Hinweis:** Der Prüfobjekttyp **HTTP** ist für neue Nutzer nicht mehr verfügbar. Uptrends hat die Funktionen des **HTTPS**-Prüfobjekttyps erweitert, sodass auf Verfügbarkeit von HTTP-Websites geprüft werden kann. [SHORTCODE_2]

Die Prüfobjekte Hypertext Transfer Protocol (HTTP) und Hypertext Transfer Protocol Secure (HTTPS) gehören zu den Uptime-[Prüfobjekttypen]([LINK_URL_1]), die du im Handumdrehen einrichten kannst. Diese Prüfobjekte verhalten sich ähnlich und ermöglichen dir die Verfügbarkeit von Websites auf Basis von HTTP- und HTTPS-Anfragen zu überwachen.

Die Prüfobjekte führen grundlegende Tests bei deinen [INLINE_CODE_1] und [INLINE_CODE_2] Websites von zugewiesenen, weltweiten [Checkpoints]([LINK_URL_2]) aus. Die grundlegenden Prüfungen umfassen die Verifizierung der Statuscodes der Website-Antwort, Seitenladezeit und Laden von Inhaltsressourcen. HTTP- und HTTPS-Prüfobjekte rufen einfach angefragte Ressourcen von der Website ab. Die primäre Funktion besteht darin, festzustellen, ob eine fehlerfreie Antwort vom Webserver erhalten wird, und zu bestätigen, dass die Seite verfügbar ist. Weitere Informationen findest du unter [Funktionsweise eines HTTP-Prüfobjekts]([LINK_URL_3]).

Für eingehendere Prüfungen, um die Leistung und Verfügbarkeit deiner Website genau zu messen, empfiehlt Uptrends den [Full Pagecheck]([LINK_URL_4]) zu nutzen. Einzelheiten dazu findest du im Knowledge-Base-Artikel [Einfache Checks im Vergleich zu Full Pagechecks oder Real-Browser Checks]([LINK_URL_5]).

## Ein HTTP- oder HTTPS-Prüfobjekt einrichten

Es gibt einen kleinen Unterschied bei der Einrichtung des Uptime HTTP-Prüfobjekts gegenüber einem HTTPS-Prüfobjekt. Da das HTTPS-Prüfobjekt eine erweiterte und gesicherte Version des HTTP-Prüfobjekts ist, umfasst dieses Prüfobjekt einen zusätzlichen Test, um auf SSL-Zertifikatsfehler zu prüfen. Um diese Einstellung zu konfigurieren, wechsle zum Tab [SHORTCODE_3] Erweitert [SHORTCODE_4] in der Prüfobjekteinrichtung und aktiviere das Kontrollkästchen **SSL Zertifikat Fehler prüfen**.

Aktivieren dieser Option erlaubt deinem HTTPS-Prüfobjekt zu verifizieren, dass das SSL-Zertifikat keine Fehler verursacht. Deaktiviere die Option nur, um Probleme, die vom SSL-Zertifikat erzeugt werden, zu ignorieren. Möchtest du dein SSL-Zertifikat eingehender überwachen, richte den Prüfobjekttyp [SSL-Zertifikat]([LINK_URL_6]) ein, um weitere Tests auszuführen.

Zur Erstellung deines eigenen HTTP- oder HTTPS-Prüfobjekts findest du im Knowledge-Base-Artikel [Ein HTTP- oder HTTPS-Prüfobjekt hinzufügen]([LINK_URL_7]) weitere Informationen.

## Erweiterte HTTP-Einstellungen

Über den Tab [SHORTCODE_5] Erweitert [SHORTCODE_6] kannst du deine HTTP- oder HTTPS-Prüfobjekteinrichtung weiter anpassen und Folgendes konfigurieren:

- [User Agent]([LINK_URL_8]) 
- Authentifizierung – wenn die zu überwachende HTTP-Ressource eine Authentifizierung im Rahmen der HTTP-Anfrage erfordert, wähle den entsprechenden Authentifizierungstyp (Keine, Basic Authentication, NTLM (Windows) Authentication und Digest Authentication). Gib die Anmeldedaten in den Feldern **Benutzername** und **Passwort** ein. Beachte, dass Uptrends deine Daten immer [verschlüsselt]([LINK_URL_9]).
- Benutzerdefinierte HTTP Request Felder – konfiguriere die Optionen **HTTP Methode** (GET/POST), **HTTP Request Header**, **SSL Zertifikat Fehler prüfen** und **TLS Version(en)**. Weitere Einzelheiten findest du in diesem [Knowledge-Base-Artikel]([LINK_URL_10]).
