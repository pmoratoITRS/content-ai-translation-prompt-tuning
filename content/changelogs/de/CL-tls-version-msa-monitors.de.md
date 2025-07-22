{
  "title": "Neue TLS-Versionsoption (Kontrollkästchen) bei Multi-Step API (MSA)-Prüfobjekten",
  "date": "2024-11-06",
  "url": "/changelog/november-2024-neue-tls-versions-kontrollkaestchen-msa-pruefobjekte",
  "translationKey": "https://www.uptrends.com/changelog/november-2024-new-tls-versions-checkbox-msa-monitors"
}

Wir haben das Kontrollkästchen *TLS Version(en)* im visuellen MSA Schritte-Editor aufgenommen.

Durch Aktivieren des Kontrollkästchens *Nur bestimmte TLS-Versionen zulassen* kannst du nun bestimmte TLS-Versionen während des TLS-Handshakes für die HTTP-Verbindung von MSA-Prüfobjekten auswählen. Du kannst das Kontrollkästchen auch deaktivieren, wenn keine Einschränkungen erforderlich sind.

Alle [Uptrends Checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="de" >}}) unterstützen TLS 1.1 und TLS 1.2. Auswahl der Option TLS 1.3 limitiert die Checkpoint-Auswahl auf solche Checkpoints mit TLS 1.3-Fähigkeit. Obwohl TLS 1.1 noch verfügbar ist, wird es nicht empfohlen.

![TLS-Versionen-Kontrollkästchen bei MSA-Prüfobjekten](/img/content/scr-tls-versions-option-checkbox.min.png)