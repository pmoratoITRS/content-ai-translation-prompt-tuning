{
  "hero": {
    "title": "Private Locations – Fehlerbehebung"
  },
  "title": "Private Locations – Fehlerbehebung",
  "summary": "Hinweise zur Fehlerbehebung und Beispiele zur Fehlerbehebung an deinen privaten Standorten Locations.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-fehlerbehebung",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting"
}

Die Installation eines privaten Standorts erfolgt voll automatisiert. Du hast anschließend einen aktiven Container-Checkpoint, der sich selbst auf dem neuesten Stand hält und Messungen für Prüfobjekte ausführen kann. Dieser Leitfaden zeigt Schritte auf, anhand derer du deine [Installation des privaten Standorts verifizieren](#verify-private-location-installation) und deine [Einrichtung einem Smoke Test unterziehen](#smoke-test-your-setup) sowie wie du [Probleme lösen](#how-to-troubleshoot) kannst, die während oder nach der Installation eines privaten Standorts aufgetreten sind. 

## Installation eines privaten Standorts verifizieren

Der erste Schritt besteht darin zu verifizieren, dass dein privater Standort korrekt [installiert und eingerichtet]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="de" >}}) ist. Das automatisierte Installationspaket ist vorkonfiguriert und umfasst drei Schritte.

- Installation der Grundvoraussetzungen (einschließlich eines Neustarts, sofern erforderlich).
- Herunterladen der Uptrends Container Images von Azure
- Installation der Auto-run- und Auto-update-Funktionen


### Installation der Grundvoraussetzungen
Drei Grundvoraussetzungen zur Ausführung der Uptrends Container Images werden installiert: die „Containers“ Windows-Funktion, Docker Engine und Docker Compose. Die Installation der Containers Windows-Funktion erfordert eventuell einen Neustart. Dafür wird eine Aufforderung eingeblendet. Nach dem Neustart wird die Installation automatisch (über einen geplanten Task) fortgesetzt.

Wenn du prüfen möchtest, dass diese drei Voraussetzungen korrekt installiert sind, kannst du drei Befehle ausführen. 

Liste zunächst alle Windows-Funktionen und prüfe, ob „Containers“ in der Liste enthalten ist:
1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zu dem Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe den Befehl ``Get-WindowsFeature | Where-Object {$_. installstate -eq "installed"}`` aus. 
3. Prüfe, ob „Containers“ in der Liste enthalten ist.

Prüfe dann die Version von Docker:
1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zum Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe den Befehl ``Docker -v`` aus. 
3. Das Ergebnis sollte „Docker version 23.0.3, build 3e7cbfd“ ähneln.

Prüfe als Drittes die Version von Docker Compose:
1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zum Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe den Befehl ``Docker-compose -v`` aus. 
3. Das Ergebnis sollte „Docker Compose version v2.17.2“ ähneln.

Wenn du denkst, dass etwas nicht stimmt, siehe dir das Installationsskript, install-checkpoint.ps1, an und führe die einzelnen Teile für die oben genannten Komponenten aus. Prüfe das Ergebnis.
 
### Container Images
Wenn alle Grundvoraussetzungen eingerichtet sind, lädt das [Installationsskript]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="de" >}}) die Uptrends Container Images von Azure herunter. Diese Images sind groß, da jedes eine komprimierte Installation eines Windows Servers enthält. Der Download kann mehrere Minuten (20 Minuten wäre nicht ungewöhnlich) dauern, abhängig vom Netzwerkdurchsatz. Teile der Images werden bei einem Update wiederverwendet, sodass nachfolgende Downloads schneller erfolgen. Ist der Download erfolgt, kannst du dies verifizieren, indem du den Befehl ``docker images`` [ausführst](#managing-running-containers). Du solltest drei Einträge sehen.

Der Download der Images stützt sich auf in Docker enthaltene Funktionen und ist ein stabiler Prozess, bei dem ein Verbindungsausfall kein Problem sein sollte. Sollte der Download jedoch fehlschlagen, ist möglicherweise eine (lokale) Firewall die Ursache, die Docker daran hindert, auf das Azure Container Repository über azurecr.io, das von Microsoft gehostet wird, zuzugreifen.

Zur Authentifizierung beim Download der Images gibt das Installationsskript über die Docker-Anmeldung die Anmeldedaten an. Bei Problemen mit der Authentifizierung rufe das Installationsverzeichnis (der Ordner, der die Datei install-checkpoint.ps1 enthält) auf und führe die folgenden Befehle in PowerShell aus, um:

bestehende Anmeldedaten zu löschen, nutze
``Docker logout``

die registry-login.ps1 erneut auszuführen und das Ergebnis des Befehls zu prüfen, nutze
``.\registry-login.ps1``

### Auto-run und Auto-update
Damit die Container-Checkpoints ausgeführt werden, wird ein geplanter Task erzeugt, um das Skript start-containers.ps1 nach dem Hochfahren des Servers auszuführen. Damit die Docker Images für die Container-Checkpoints [auf dem neuesten Stand bleiben]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-update-containers" lang="de" >}}), wird ein zweiter geplanter Task erzeugt, um regelmäßig auf Image Updates zu prüfen. Prüfe die Ausgabe des PowerShell-Befehls ``Get-ScheduledTask``, um zu bestätigen, dass diese Tasks bestehen. Sie heißen „Start Checkpoint Containers“ und „Update Checkpoint Images“. 

Du kannst die Benutzeroberfläche Windows Scheduled Task nutzen, um die Tasks zu untersuchen, Verläufe und Fehlschläge anzuzeigen oder den Task manuell anzustoßen, um Fehler zu beheben. Verwende das Installationsskript (install-checkpoint.ps1), um bei Bedarf diesen Teil der Installation erneut auszuführen.

### Konfiguration
Alle serverspezifischen Konfigurationen sind in der Konfigurationsdatei Docker-compose.yml enthalten. Diese Datei listet alle drei Container Images und ihre jeweiligen Einstellungen. Diese Konfigurationsdatei enthält bereits alle notwendigen Einstellungen, wenn du sie herunterlädst. Am wichtigsten ist die ``ServerId/Password``-Kombination, die für alle drei Container Images, die in der Datei gelistet sind, konfiguriert sein sollte (d. h. dieselbe Kombination der Credentials ist in der yml-Datei dreimal mit denselben Werten vorhanden). 

{{< callout >}} Die *ServerId* und das *Password* sind für den Container-Checkpoint eindeutig. Mehrere Container-Checkpoint-Server sollten niemals dieselbe *ServerId* haben. {{< /callout >}}

Die Docker Compose-Datei kann verwendet werden, um Checkpoint-spezifische [Datenschutzrichtlinien]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}) und [umgebungsspezifische DNS-Regeln](#dns-issues) zu konfigurieren.
 
### Aktueller Status
Nach der Installation werden die Container für alle drei Images gestartet. Sie sollten dann ununterbrochen ausgeführt werden. Du kannst den Status anhand des Befehls ``docker ps`` prüfen. In der rechten Spalte siehst du, ob die Container tatsächlich ausgeführt werden. Sollte es ein Problem geben, verwende diese Befehle, um zur weiteren Diagnose die Protokolldateien einzusehen:


– Aktueller Status von allen Containern
``Docker ps``

- Protokolle für den Checkpoint Agent-Container abrufen und in Datei schreiben
``Docker logs Checkpoint | Out-File Docker_CS.txt``

- Protokolle für den Transaction Processor-Container abrufen und in Datei speichern
``Docker logs TransactionProcessor | Out-File Docker_TP.txt``

- Alternativ alle Protokolle für die Container kombiniert speichern
``Docker-compose logs -t -n 5000 | Out-File Docker.txt``

## Smoke Test deiner Einrichtung

Sobald die Container Checkpoints installiert sind, sind sie bereit, Messungen auszuführen. Uptrends’ interne Prozesse wechseln automatisch den Wartungsstatus eines Container-Checkpoints, je nach Zustand. Ein Checkpoint, bei dem alles in Ordnung ist, wird auf „Aktiv“ gesetzt, ein Checkpoint, bei dem es ein Problem gibt, wird auf „Deaktiviert“ gesetzt. 

Checkpoints aktualisieren ihren Zustand jede Minute. Du kannst Checkpoints aktivieren oder [deaktivieren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use#disable-a-private-checkpoint" lang="de" >}}) (zum Beispiel zur Wartung oder um die Einrichtung zu testen). Nutze dazu die Benutzeroberfläche unter Private Locations in der Uptrends Webanwendung. Der Standardstatus ist „aktiviert“. 

Einen Container-Checkpoint einem Smoke Test zu unterziehen, geht am besten über die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}}. Idealerweise führst du dies für jeden Prüfobjekttyp durch, den du mit ihm nutzen möchtest. 

Nutze [Checkpoint-Zustand]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="de" >}}) im Bereich Private Locations, um den Zustand problematischer Checkpoints zu festzustellen. 

Beachte, dass alle Messungen „in“ einem Container ablaufen. Du wirst nicht sehen, dass ein Browser auf dem Host-Rechner aufgerufen wird, wenn du die Schaltfläche {{< AppElement type="buttonSecondary" >}} Jetzt testen {{< /AppElement >}} für einen FPC oder eine Transaktion nutzt.

Berücksichtige auch, dass ein neuer Checkpoint Messungen aufnimmt, sobald die Installation beendet ist, wenn du einen Checkpoint, der Teil einer Checkpoint-Auswahl aktiver Prüfobjekte ist, zu einem bestehenden privaten Standort hinzufügst. Sollte das nicht gewünscht sein (wenn du beispielsweise erst testen möchtest), deaktiviere den Checkpoint im Uptrends Bereich Private Locations.


## Probleme beheben

### Container stoppen, starten und neu starten
Führe einen Neustart von Containern aus, die mit der Datei Docker-compose.yaml im aktuellen Verzeichnis verknüpft sind. Das ist üblicherweise der Ordner C:\uptrends\:

1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zum Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe einen oder alle der folgenden Befehle aus.
- Um zu starten, gib `docker-compose up -d` in die Befehlszeile ein. 
- Um zu stoppen, gib `docker-compose down` in die Befehlszeile ein. 
- Um neu zu starten, gib `docker-compose restart` in die Befehlszeile ein.


{{< callout >}} **Tipp**: Mache Gebrauch von der Docker-Hilfe. Zu allen Befehlen erfährst du mehr, indem du den Befehl *docker - -help* eingibst. Dieser Befehl zeigt alle Befehle mit einer allgemeinen Hilfe für alle verschiedenen Befehle an. Du kannst auch zu einem bestimmten Befehl eine Hilfe aufrufen, indem du *docker image - -help* eingibst.{{< /callout >}}


### Ausgeführte Container verwalten
Um eine Liste der Container, die ausgeführt werden, zu erhalten, gib den Befehl ``docker ps`` ein. Damit wird eine containerId angezeigt, die mit anderen Befehlen für diesen Container verwendet werden kann. 

Um eine Liste aller lokalen Images zu erhalten, führe den Befehl ``docker images`` aus. Beachte den Plural, „images“: alle Befehle für ein Image werden mit „image“ (singular) ausgeführt.

Images können recht groß werden. Um Speicherplatz freizugeben, kannst du den Befehl ``docker image prune`` nutzen, um Images zu entfernen, die nicht mehr von aktiven Containern genutzt werden. Oder verwende ``docker image rm <containerid>``, um einen bestimmten Container zu entfernen.

### Entfernen nicht verwendeter Docker-Objekte

Das [Uptrends Installationsskript für Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}) enthält keine Einstellungen zum automatischen Entfernen nicht verwendeter Docker-Objekte. Um nicht verwendete Docker-Objekte zu entfernen, lies die Dokumentation [Prune unused Docker objects](https://docs.docker.com/engine/manage-resources/pruning). Solltest du andere Plattformen nutzen, zum Beispiel Kubernetes, ziehe bitte deren offizielle Dokumentation zurate.

### Befehlszeilen-/Shell-Zugriff in einem Container erhalten
Führe diesen Befehl aus, um eine PowerShell oder einen Befehlszeilenprozess im Container zu starten. Damit kann das Dateisystem in den Containern schnell gelesen werden. Verwende den Befehl ```Docker exec -i checkpoint powershell``` oder ```Docker exec -i checkpoint cmd```.

Bist du nicht sicher, ob du dich im oder außerhalb eines Containers befindest? Gib in die Windows-Befehlszeile ``winver`` ein. Bis du in einem Container, wird es wie folgt aussehen: 

```winver : The term 'winver' is not recognized``` 

Befindest du dich auf dem Host, wird das Pop-up Windows **Info** angezeigt.
Wenn du die PowerShell oder Befehlszeile im Container verlassen und zum Host zurückkehren möchtest, nutze Ctrl+C.

### Protokoll lesen

1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zu dem Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe einen der folgenden Befehle aus.
- Gib für Log Output `Docker-compose logs -t -n 5000` in die Befehlszeile ein. 
- Oder, wenn du dies in einer Datei namens containerlogs.log speichern möchtest, gib ``Docker-compose logs -t -n 5000 > containerlogs.log`` ein.

### Netzwerk
Beim Start wird Docker ein virtuelles Netzwerk auf dem Host erstellen, mit dem die Container verbunden werden. Sie erhalten eine IP-Adresse. 
Bestehende Netzwerke kannst du in Powershell mit ``docker network ls`` anzeigen und ein bestimmtes Netzwerk mit ``docker network inspect <<network name>>``. Um das Netzwerk zu finden, in dem sich ein Container befindet, verwende ``docker inspect <<container name>>`` (und ``docker ps``, um Container-Namen zu finden).

Alle drei Uptrends Docker Container (Checkpoint, CheckpointRelay, TransactionProcessor) müssen in der Lage sein, eine Verbindung zu Uptrends über probemaster1.uptrends.com und probemaster2.uptrends.com aufzubauen. Sowohl der Checkpoint als auch der CheckpointRelay Container, müssen in der Lage sein, mit deinen zu testenden Anwendungen zu verbinden.

### DNS-Probleme

Ein häufiger Grund für Verbindungsprobleme ist die DNS-Auflösung. Folge diesen Schritten zur Fehlerbehebung:

1. Auf dem Host sollte ``nslookup probemaster1.uptrends.com`` 95.211.70.204 ausgeben. Sollte das nicht der Fall sein, können die Container keine Verbindung zu Uptrends herstellen.

2. Unter der Voraussetzung, dass die Container ausgeführt werden (prüfe dies mit ``docker ps``), rufe PowerShell in einem Container auf: ``docker exec -i Checkpoint powershell.exe``.

3. Sobald du dich im Container befindest, sollte ``nslookup probemaster1.uptrends.com`` ebenfalls 95.211.70.204 ausgeben. Erweist sich dies als erfolgreich, sollte der Container in der Lage sein, eine Verbindung zur Uptrends Cloud-Plattform herstellen.

4. Versuche dasselbe für einen Hostnamen einer internen Anwendung, etwa ``nslookup <<name application>>`, und prüfe die zurückgegebene IP-Adresse. Sollte dies zu einer Zeitüberschreitung führen, ist die Anwendung vom Container nicht erreichbar (und kann dann nicht überwacht werden).

Sollte keiner der Schritte zum Erfolg führen, versuche Folgendes:

- Vergleiche die ipconfig vom Host mit der im Container (``docker exec -i Checkpoint powershell.exe``, um eine PowerShell im Checkpoint Container aufzurufen) und verifiziere den bzw. die konfigurierten DNS-Server.

Versuche, ein öffentliches DNS wie 8.8.8.8 (Google) anzugeben, wenn du ein nslookup ausführst: ``nslookup probemaster1.uptrends.com 8.8.8.8``. Wenn es korrekt funktioniert, ohne die öffentliche DNS’ IP-Adresse zu nutzen, aber Probleme auftreten, wenn keine IP-Adresse angegeben ist, kann der Fehler bei der DNS-Auflösung liegen. Beachte, dass der Einsatz von 8.8.8.8 als DNS-Server in Produktion nicht wünschenswert ist, da er nicht die Adresse interner Anwendungen auflösen kann.

Gib spezifische DNS-Server in der Compose-Datei, wie im Code unten gezeigt, an. Dies muss für beide Container in der yaml-Datei erfolgen.

```yaml
TransactionProcessor:
    container_name: TransactionProcessor
    image: uptrends.azurecr.io/win2022/transaction-processor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: local
    environment:
      - ServerId=
      - Password=
    dns:
      - 1.2.3.4
      - 2.3.4.5
```

Gib die IP-Adressen der DNS-Server ein, die du nutzen möchtest. Du kannst diese für probemaster1.uptrends.com wie auch den Hostnamen anhand von nslookup testen. Achte darauf, dies in einem Container auszuführen.

Du wirst eventuell DNS-Anfragen von den Docker-Containern erlauben müssen, falls deine DNS-Server eine Allow-Liste nutzen. Wenn du Container-Checkpoints auf einer Cloud-Plattform wie Google Cloud, AWS oder Azure ausführst, sind eventuell zusätzliche Konfigurationen erforderlich, um die Verbindung aus den Docker-Containern zu gewährleisten. 

## Funktioniert die Einrichtung immer noch nicht? 

Sollte dir zu irgendeinem Zeitpunkt bei der Problembehebung etwas nicht klar sein, oder wenn du sonstige Fragen hast, wende dich bitte an Uptrends, indem du ein [Support-Ticket]({{< ref path="contact" lang="de" >}}). einreichst. Wir werden uns so schnell wie möglich zurückmelden. 