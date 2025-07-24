{
  "hero": {
    "title": "Einen Docker-Checkpoint installieren"
  },
  "title": "Einen Docker-Checkpoint installieren",
  "summary": "Richte einen Docker Host und Checkpoint-Container für das interne Monitoring deiner Netzwerkinfrastruktur ein.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-container-checkpoints-installieren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dieser Knowledge-Base-Artikel ist ein Setup Guide, um Windows Server 2022 oder 2019 als Host-Betriebssystem zu konfigurieren. Er erläutert auch, wie ein [privater Docker-Container-Checkpoint]([LINK_URL_1]) eingerichtet wird.

Stelle vor der Installation sicher, dass alle [Voraussetzungen und Einstellungen]([LINK_URL_2]) erfüllt sind. Uptrends wird dir die erforderlichen Dateien bereitstellen, um das Monitoring aufzunehmen.

## Installationsskript

Uptrends stellt ein Installationsskript bereit, das du als .zip-Datei unter [SHORTCODE_5] Private Locations [SHORTCODE_6] in der [Uptrends Anwendung]([LINK_URL_3]) herunterladen kannst. Dieses Skript ist für jeden deiner [Private Locations]([LINK_URL_4]) verfügbar und führt die hauptsächlichen Installationsschritte aus. Diese Schritte umfassen die Installation von Docker und Docker Compose, Abrufen der Uptrends Container Images, Ausführen eines Start- und Aktualisierungs-Tasks und Starten des Container-Checkpoints.

## Installationsschritte

**Um einen Checkpoint anhand des Skripts zu installieren:**

1. Rufe das [SHORTCODE_7] Private Locations [SHORTCODE_8]-Menü auf.
2. Solltest du noch keine [Private Locations]([LINK_URL_5]) hinzugefügt haben, klicke auf [SHORTCODE_9] Standort hinzufügen [SHORTCODE_10]. Sobald der private Standort hinzugefügt wurde, sind standardmäßig zwei Checkpoints enthalten.
3. Klicke auf den Checkpoint-Namen der Private Locations.
4. Wähle aus dem Drop-down-Menü **Host Betriebssystem** das erforderliche Betriebssystem.
5. Klicke auf die Schaltfläche [SHORTCODE_11] Lade die Installations-Zip-Datei herunter [SHORTCODE_12].

[SHORTCODE_1] **Wichtig:** Bedenke, dass die heruntergeladene .zip-Datei nur den bestimmten Checkpoint des privaten Standorts enthält, den du aus den zwei Standard-Optionen ausgewählt hast. Die .zip-Datei trägt den Dateinamen UptrendsCheckpoints\[HTML_TAG_1].zip, wobei \[HTML_TAG_2] der Name deines Checkpoints ist. [SHORTCODE_2]

5. Entpacke die heruntergeladene Datei an dem Ort, an dem du den privaten Checkpoint installieren möchtest.
6. Um zu verhindern, dass Screenshots in die Cloud geladen werden, kannst du [die Docker-Compose-Datei bearbeiten]([LINK_URL_6]), nachdem du die Dateien heruntergeladen und extrahiert hast.

[SHORTCODE_3] **Wichtig:** Abhängig von den Richtlinien deines Unternehmens musst du eventuell alle Powershell-Skriptdateien (*.ps1) im Zip-Ordner zulassen, bevor du sie ausführst. Für weitere Informationen enthalten die [Anweisungen]([LINK_URL_7]) zum Freigeben von Dateien. [SHORTCODE_4]

7. Öffne eine PowerShell-Konsole und führe sie als Administrator aus. Führe das Skript [INLINE_CODE_1] im Uptrends (Entpackungs)-Verzeichnis aus. Damit wird der Server einmal neu gestartet. Beachte, dass das Skript einen Task konfigurieren wird, der einmal pro Stunde läuft, um auf Aktualisierungen der Uptrends Container zu prüfen.

Die Checkpoints sind nun verfügbar und können auf dem Tab [SHORTCODE_13] Checkpoints [SHORTCODE_14] des Prüfobjekts gewählt werden. Du kannst die Checkpoints auch im Dialogfenster *Kontrolldetails* sehen, wenn du einen schnellen Test direkt in den Prüfobjekteinstellungen über die Schaltfläche [SHORTCODE_15] Jetzt testen [SHORTCODE_16] ausführst.

Um an Private Locations Zertifikate zu installieren, lies [Zertifikate an Private Locations installieren]([LINK_URL_8]).

## Den privaten Checkpoint überwachen

Uptrends wird Änderungen an deinem Account vornehmen, um dich bei der Überwachung deiner privaten Checkpoints besser zu unterstützen. Bitte stelle sicher, dass deine privaten Checkpoint-Server, Firewall, Internetverbindung und andere unterstützende Systeme zugänglich bleiben.

Während der Einrichtung der privaten Checkpoints, fügt Uptrends zusätzliche Prüfobjekte und Konfigurationen hinzu. Bitte ändere oder lösche diese in deinem Account nicht.

Weitere Informationen findest du im Knowledge-Base-Artikel [Private Locations nutzen]([LINK_URL_9]).