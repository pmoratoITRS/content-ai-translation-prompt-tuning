{
  "hero": {
    "title": "Einen Docker-Checkpoint installieren"
  },
  "title": "Einen Docker-Checkpoint installieren",
  "summary": "Richte einen Docker Host und Checkpoint-Container für das interne Monitoring deiner Netzwerkinfrastruktur ein.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-container-checkpoints-installieren",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-docker-private-checkpoints"
}

Dieser Knowledge-Base-Artikel ist ein Setup Guide, um Windows Server 2022 oder 2019 als Host-Betriebssystem zu konfigurieren. Er erläutert auch, wie ein [privater Docker-Container-Checkpoint]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker#how-do-i-get-a-private-checkpoint" lang="de" >}}) eingerichtet wird.

Stelle vor der Installation sicher, dass alle [Voraussetzungen und Einstellungen]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="de" >}}) erfüllt sind. Uptrends wird dir die erforderlichen Dateien bereitstellen, um das Monitoring aufzunehmen.

## Installationsskript

Uptrends stellt ein Installationsskript bereit, das du als .zip-Datei unter {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} in der [Uptrends Anwendung](https://app.uptrends.com/PrivateLocations) herunterladen kannst. Dieses Skript ist für jeden deiner [Private Locations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) verfügbar und führt die hauptsächlichen Installationsschritte aus. Diese Schritte umfassen die Installation von Docker und Docker Compose, Abrufen der Uptrends Container Images, Ausführen eines Start- und Aktualisierungs-Tasks und Starten des Container-Checkpoints.

## Installationsschritte

**Um einen Checkpoint anhand des Skripts zu installieren:**

1. Rufe das {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}}-Menü auf.
2. Solltest du noch keine [Private Locations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) hinzugefügt haben, klicke auf {{< AppElement type="buttonPrimary" >}} Standort hinzufügen {{< /AppElement >}}. Sobald der private Standort hinzugefügt wurde, sind standardmäßig zwei Checkpoints enthalten.
3. Klicke auf den Checkpoint-Namen der Private Locations.
4. Wähle aus dem Drop-down-Menü **Host Betriebssystem** das erforderliche Betriebssystem.
5. Klicke auf die Schaltfläche {{< AppElement type="buttonPrimary" >}} Lade die Installations-Zip-Datei herunter {{< /AppElement >}}.

{{< callout >}} **Wichtig:** Bedenke, dass die heruntergeladene .zip-Datei nur den bestimmten Checkpoint des privaten Standorts enthält, den du aus den zwei Standard-Optionen ausgewählt hast. Die .zip-Datei trägt den Dateinamen UptrendsCheckpoints\<checkpoint-name\>.zip, wobei \<checkpoint-name\> der Name deines Checkpoints ist. {{< /callout >}}

5. Entpacke die heruntergeladene Datei an dem Ort, an dem du den privaten Checkpoint installieren möchtest.
6. Um zu verhindern, dass Screenshots in die Cloud geladen werden, kannst du [die Docker-Compose-Datei bearbeiten]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection#disable-screenshots-in-docker-compose-file" lang="de" >}}), nachdem du die Dateien heruntergeladen und extrahiert hast.

{{< callout >}} **Wichtig:** Abhängig von den Richtlinien deines Unternehmens musst du eventuell alle Powershell-Skriptdateien (*.ps1) im Zip-Ordner zulassen, bevor du sie ausführst. Für weitere Informationen enthalten die [Anweisungen](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-5.1) zum Freigeben von Dateien. {{< /callout >}}

7. Öffne eine PowerShell-Konsole und führe sie als Administrator aus. Führe das Skript `./install-checkpoint.ps1` im Uptrends (Entpackungs)-Verzeichnis aus. Damit wird der Server einmal neu gestartet. Beachte, dass das Skript einen Task konfigurieren wird, der einmal pro Stunde läuft, um auf Aktualisierungen der Uptrends Container zu prüfen.

Die Checkpoints sind nun verfügbar und können auf dem Tab {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} des Prüfobjekts gewählt werden. Du kannst die Checkpoints auch im Dialogfenster *Kontrolldetails* sehen, wenn du einen schnellen Test direkt in den Prüfobjekteinstellungen über die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} ausführst.

Um an Private Locations Zertifikate zu installieren, lies [Zertifikate an Private Locations installieren]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-certificates-private-locations" lang="de" >}}).

## Den privaten Checkpoint überwachen

Uptrends wird Änderungen an deinem Account vornehmen, um dich bei der Überwachung deiner privaten Checkpoints besser zu unterstützen. Bitte stelle sicher, dass deine privaten Checkpoint-Server, Firewall, Internetverbindung und andere unterstützende Systeme zugänglich bleiben.

Während der Einrichtung der privaten Checkpoints, fügt Uptrends zusätzliche Prüfobjekte und Konfigurationen hinzu. Bitte ändere oder lösche diese in deinem Account nicht.

Weitere Informationen findest du im Knowledge-Base-Artikel [Private Locations nutzen]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="de" >}}).