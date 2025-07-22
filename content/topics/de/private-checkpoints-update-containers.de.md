{
  "hero": {
    "title": "Docker Container aktualisieren"
  },
  "title": "Docker Container aktualisieren",
  "summary": "Wie funktioniert das Updating eines Docker Containers bei privaten Standort-Checkpoints?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-checkpoints-update-container",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-update-containers"
}

Wenn du einen [nutzerverwalteten Checkpoint installierst]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#script-content" lang="de" >}}), wird ein Skript erzeugt und ein geplanter Task eingerichtet, der den Checkpoint Container jede Stunde aktualisiert. Solltest du über dieses Plan-Update hinaus eine Aktualisierung durchführen wollen, kannst du dies manuell durchführen.

## Wie wird manuell aktualisiert?

Stelle zunächst sicher, dass die in [Einen Docker-Checkpoint installieren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}) erläuterten Schritte bereits ausgeführt wurden.

1. Öffne eine PowerShell-Konsole **im Admin-Modus**.
2. Wechsle zum Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe die folgenden Befehle aus.
3. Gib `docker-compose pull` in die Befehlszeile ein.
4. Gib `docker-compose down` in die Befehlszeile ein.
5. Gib `docker-compose up` in die Befehlszeile ein.

Während der Aktualisierung führen deine anderen private Checkpoints die Prüfungen aus. Der zu aktualisierende Checkpoint muss für ein erfolgreiches Update nicht deaktiviert werden. Da du mindestens über [eine weitere Checkpoint-Instanz]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq#two-default-private-checkpoints" lang="de" >}}) verfügen solltest (was sehr empfohlen ist), kannst du das Update durchführen, ohne Änderungen wie das Deaktivieren von Checkpoints, Pausieren von Prüfobjekten usw. vorzunehmen.

{{< callout >}}
Es ist wichtig, dass deine Docker Container auf dem neuesten Stand sind. Die Containers haben die Browser Chrome und Edge integriert. Diese müssen regelmäßig aktualisiert werden, damit sie kein Sicherheitsrisiko darstellen.
Uptrends zeigt eine Warnmeldung, wenn deine Container veraltet erscheinen.
{{< /callout >}}