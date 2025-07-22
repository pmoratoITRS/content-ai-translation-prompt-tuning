{
  "title": "Neue TLS-Versionsoption (Kontrollkästchen) bei Multi-Step API (MSA)-Prüfobjekten",
  "date": "2024-11-06",
  "url": "[URL_BASE_CHANGELOG]november-2024-neue-tls-versions-kontrollkaestchen-msa-pruefobjekte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wir haben das Kontrollkästchen *TLS Version(en)* im visuellen MSA Schritte-Editor aufgenommen.

Durch Aktivieren des Kontrollkästchens *Nur bestimmte TLS-Versionen zulassen* kannst du nun bestimmte TLS-Versionen während des TLS-Handshakes für die HTTP-Verbindung von MSA-Prüfobjekten auswählen. Du kannst das Kontrollkästchen auch deaktivieren, wenn keine Einschränkungen erforderlich sind.

Alle [Uptrends Checkpoints]([LINK_URL_1]) unterstützen TLS 1.1 und TLS 1.2. Auswahl der Option TLS 1.3 limitiert die Checkpoint-Auswahl auf solche Checkpoints mit TLS 1.3-Fähigkeit. Obwohl TLS 1.1 noch verfügbar ist, wird es nicht empfohlen.

![TLS-Versionen-Kontrollkästchen bei MSA-Prüfobjekten]([LINK_URL_2])