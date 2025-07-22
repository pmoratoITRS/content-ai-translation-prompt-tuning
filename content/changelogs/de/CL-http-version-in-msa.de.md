{
  "title": "Bestimmung von HTTP-Versionen wird nun bei Prüfobjektschritten des Multi-Step API (MSA)-Monitoring unterstützt",
  "date": "2025-04-03",
  "url": "/changelog/april-2025-http-version-in-multi-step-api-pruefobjekten",
  "translationKey": "https://www.uptrends.com/changelog/april-2025-http-version-in-multi-step-api-monitors"
}

Es ist nun möglich, die HTTP-Version bei jedem Schritt des Multi-Step API (MSA)-Prüfobjekts zu bestimmen. Damit kannst du steuern, welche HTTP-Version die Checkpoint-Server bei einer Anfrage nutzen:

![HTTP-Version](/img/content/scr-msa-step-http-version.min.png)

Standardmäßig ist die Option **HTTP-Version** nicht aktiviert. Das heißt, der Server wird automatisch die höchste unterstützte HTTP-Version nutzen, die verfügbar ist. Ersatzweise wird mindestens HTTP/1.1 genutzt. Derzeit ist HTTP/3 an einigen Checkpoint-Standorten verfügbar. Dies wird bald auf weitere Standorte ausgeweitet.

Darüber hinaus gilt, dass die HTTP-Konfiguration nur die Auswahl einer Version erlaubt, während die TLS-Konfiguration die Auswahl mehrerer Versionen ermöglicht. Der Grund dafür ist, dass TLS eine Versionsaushandlung während des Verbindungsaufbaus unterstützt, während HTTP/3 dies nicht praktiziert und die Angabe einer bestimmten Version erfordert.