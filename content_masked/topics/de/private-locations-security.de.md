{
  "hero": {
    "title": "Private Standorte und Sicherheit"
  },
  "title": "Private Standorte und Sicherheit",
  "summary": "Was sollte beachtet werden, um den sicheren Betrieb von Checkpoints an privaten Standorten zu gewährleisten?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-sicherheit",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wenn du mehr über die Sicherheit der Checkpoint-Installation privater Standorte und was du zum Schutz deiner Daten unternehmen solltest erfahren möchtest, kannst du hier mehr dazu lesen. In diesem Artikel erläutern wir die wichtigsten Sicherheitsmaßnahmen, die Uptrends implementiert hat oder die in deiner Verantwortung liegen.

## Container 

Die Checkpoint-Installation eines privaten Standorts basiert auf Docker-Container. Es gibt einige „eingebaute“ Sicherheitsfunktionen sowie einige von Uptrends vorgenommene Maßnahmen:

- Uptrends verwendet ein eigenes Container Repository auf Microsoft Azure. Das ermöglicht dir, mit einem kleinen Repository zu arbeiten, das nur die vertrauenswürdigen Container enthält, die du brauchst.
- Docker kümmert sich um die Verifizierung der Container.
- Uptrends scannt den Inhalt der Container Images mithilfe von Sicherheitssoftware, bevor sie in das Container-Repository hochgeladen werden. Damit kann Uptrends bekannte Schwachstellen erkennen, bevor die neuen Versionen der Container-Software veröffentlicht werden. Darüber hinaus empfehlen wir, dass du ebenfalls die Container-Pakete (Updates) nach dem Download und vor der Installation scannst.
- Docker Container sind in der Regel hinsichtlich eingehender Kommunikation von der Außenwelt und Kommunikation auf dem Host, auf dem sie installiert sind, eingeschränkt. Du musst die Firewall-Eingangs-Ports nicht öffnen.
- Die Standardinstallation eines privaten Standorts installiert ein Skript, mithilfe dessen Docker-Container automatisch aktualisiert werden. Das stellt sicher, dass private Standorte immer auf Grundlage der letzten Sicherheits-Updates ausgeführt werden.

## Software (nicht Docker-Container-Installation)

Der Betrieb von Checkpoints erfordert die Checkpoint-Software, aber auch noch andere, unterstützende Software. Bedenke die folgenden Themen:

- [Updates]([LINK_URL_1]) von Windows, Browsern usw. sind erforderlich, um Fehlerbehebungen so schnell, wie sie verfügbar sind, zu implementieren, sodass mögliche Sicherheitsprobleme vermieden werden.
- Uptrends ist gemäß ISO 27001 zertifiziert. Die Zertifizierung berücksichtigt Datensicherheit und Entwicklungspraktiken wie:
  - Änderungen an Uptrends’ Software wird von Fachkollegen begutachtet.
  - Es sind Tools und Verfahren eingerichtet, um gegen Schwachstellen bei voneinander abhängiger Software zu schützen.
  - Es gibt einen offiziellen Sicherheitsbeauftragten und Uptrends folgt bei Sicherheitsvorfällen festgelegten Verfahren.
  - Sieh dir das [ISO 27001 Zertifikat]([LINK_URL_2]) von Uptrends an.
- Bei einem Windows-Host ist ein Antivirenscanner auf dem Host ausreichend. Die meisten Antivirenscanner sind in der Lage, die Prozesse und den Traffic im Container zu scannen. Dies solltest du jedoch für den von dir verwendeten Antivirenscanner überprüfen.

## Netzwerk-Traffic 

Die Prüfungen durch Prüfobjekte verursachen etwas Netzwerk-Traffic, bei dem Daten und Abfragen in und außerhalb deines Netzwerk fließen. Bedenke Folgendes:

- Du solltest den Netzwerk-Zugriff auf ein erforderliches Minimum beschränken.
- Private Locations erfordern keine eingehenden Verbindungen, und wir empfehlen, dass du diese komplett deaktivierst. Alle Verbindungen zur Außenwelt sind ausgehend und werden immer vom Host initiiert.
- Die Anweisungen, die ein Checkpoint aus der Uptrends Cloud erhält, sind mit einem geheimen Schlüssel signiert. Der Checkpoint validiert eingehende Anweisungen anhand des zugehörigen öffentlichen Public Keys (dem Checkpoint bekannt) und stellt so sicher, dass die Anweisungen wirklich von Uptrends gesendet wurden.

## Datenschutzeinstellungen/Schutz

Beim Monitoring geht es immer um Daten, ob einfache Informationen, etwa dass eine Prüfung „OK“ war oder einen Fehler gemeldet hat, oder tiefgehendere Informationen wie Screenshots deiner Website während eines bestimmten Transaktionsschritts. Du solltest wissen, welche Art von Informationen in die Uptrends-Cloud-Umgebung gesendet werden und welche Informationen du auf deinen Standort beschränken kannst.

- Zustandsdaten des Checkpoints werden zur Uptrends Cloud gesendet. Sie werden benötigt, um zu wissen, ob der Checkpoint korrekt funktioniert. Mit diesen Zustandsdaten lässt sich ein veralteter oder nicht kompatibler Checkpoint erkennen. Ein nicht funktionierender Checkpoint kann zu falschen Monitoring-Ergebnissen führen.
- Die Zustandsdaten sind auf der Registerkarte Checkpoint-Zustand unter Private Locations zu sehen.
- Neben den Zustandsdaten des Checkpoints werden nur Messdaten an die Uptrends Cloud gesendet.
- Wenn du Bedenken hast, dass Messdaten dein Unternehmen verlassen, ließ bitte den Knowledge-Base-Artikel [Datenschutz]([LINK_URL_3]), um zu erfahren, wie du das Erfassen bestimmter Informationen, zum Beispiel Screenshots, IP-Adressen usw., deaktivieren kannst.

Ein weiteres Thema, dass hinsichtlich Daten und deren Schutz berücksichtigt werden sollte, sind Anmeldedaten. Uptrends weist ausdrücklich darauf hin, dass die Anmeldedaten für das Monitoring sorgfältig gewählt werden sollten. Es sollte nie ein Nutzer mit machtvollen Berechtigungen verwendet werden, um grundlegende Aufgaben zu erfüllen. Halte die Nutzern zugewiesenen Berechtigungen/Rechte auf das Minimum beschränkt, das sie benötigen, um die Aufgaben auszuführen. Rechte, die darüber hinausgehen, könnten Zugriff auf Assets oder Aufgaben geben, auf die Nutzer nicht zugreifen können sollten. Bitte lies den Artikel zu [Anmeldedaten]([LINK_URL_4]), um mehr über das Thema zu erfahren.
