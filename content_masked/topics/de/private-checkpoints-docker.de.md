{
  "hero": {
    "title": "Nutzerverwaltete Checkpoints (Docker-Container)"
  },
  "title": "Nutzerverwaltete Checkpoints (Docker-Container)",
  "summary": "Was ist ein nutzerverwalteter Checkpoint und wie wird das Uptrends Monitoring hinter der Firewall deines Unternehmens in Docker-Containern eingerichtet.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-standorte/private-checkpoints-docker",
  "translationKey": "[URL_1]
}

Uptrends bietet eine Docker-Container-Anwendung zur Ausführung eines Uptrends Checkpoints in deinem Netzwerk (hinter deiner Firewall). Bei dem privaten Checkpoint stehen dir alle Funktionen von Uptrends zur Verfügung und du kannst deine private Infrastruktur testen. Mit der Uptrends Anwendung kannst du wählen, wo die Tests deiner Prüfobjekte ausgeführt werden: intern auf deinem privaten Checkpoint oder extern mit Uptrends‘ [weltweitem Checkpoint-Netzwerk]([LINK_URL_1]) – oder auf beiden.

![]([LINK_URL_2])

Während die Tests in deinem Netzwerk stattfinden, gehen alle anderen Aktivitäten wie etwa die Terminplanung, die Alarmierung und das Reporting von der Uptrends Cloud-Anwendung aus. Uptrends speichert deine Prüfobjektdefinitionen und Testdaten in seinen Datenzentren.

Dein privater Checkpoint ist exklusiv für deinen Uptrends Account und deine Nutzung verfügbar. Du kannst Prüfobjekte intern ausführen, um deine Infrastruktur abseits des Internets zu prüfen, so zum Beispiel:

- Intranet
- Interne webaktivierte Unternehmensanwendungen
- Webservices (APIs)
- Abnahme- und andere Produktionsumgebungen
- Einfaches Verfügbarkeits-Monitoring der Server-Infrastruktur, einschließlich Datenbank-Server, E-Mail-Server und SFTP-Server

## Wie funktioniert ein privater Checkpoint?

Die Einrichtung ist wie folgt: Uptrends‘ private Checkpoints sind in Docker-Containern verpackt. Diese Container werden in deinem eigenen Netzwerk auf einer Container-Plattform gehostet. Die Plattform kann dein eigener Host oder eine virtuelle Maschine sein, oder auch eine Option wie Azure. Die Anweisungen im Artikel [Einen privaten Docker-Checkpoint installieren]([LINK_URL_3]) konzentrieren sich auf die Einrichtung auf einer virtuellen Maschine.

Ein privater Checkpoint verwendet mindestens zwei Windows Docker-Container-Instanzen, die auf deiner mit deinem Netzwerk verbundenen Container-Plattform ausgeführt werden. Diese Instanzen haben nur Zugang zur überwachten Infrastruktur in deinem Netzwerk. Die Docker-Anwendungen müssen dabei vom übrigen Netzwerk isoliert sein. Uptrends stellt die Software bereit, die auf diesen containerisierten Checkpoints ausgeführt wird. Du sorgst für die unterstützende Hardware und Infrastruktur.

Das Uptrends Monitoring-System verwendet ein zentrales Befehls- und Steuerungssystem, die Cloud-Plattform. Die Cloud-Plattform enthält deine Monitoring-Definitionen und entscheidet, wann der nächste Prüfobjekt-Test ausgeführt werden soll – basierend auf deiner Checkpoint-Wahl. Wenn du ein Prüfobjekt konfigurierst, sodass es einen privaten Checkpoint nutzt, wählt Uptrends eine der Container-Instanzen, um die Prüfung auszuführen. Die Container-Instanz führt den Test durch und meldet das Ergebnis an Uptrends. Uptrends verarbeitet und speichert die Daten des Tests, die von deinem privaten Checkpoint ausgeführt wurden. Wenn Uptrends einen Fehler erkennt, führt es sofort einen weiteren Test mit der anderen Container-Instanz durch. Wenn das Prüfobjekt den Fehler ein zweites Mal feststellt, initiiert Uptrends eine Alarmierung aus der Cloud. Weiter unten findest du weitere Infos zur privaten Checkpoint-Architektur.

Wenn dein Checkpoint aus irgendeinem Grund vollständig nicht verfügbar ist, gibt Uptrends eine Fehlermeldung aus, um dich darüber zu informieren, dass dein privater Checkpoint außer Betrieb ist. Einige Gründe für einen Ausfall sind:

- Die Verbindung des privaten Checkpoints zum Internet wurde unterbrochen.
- Alle deine Container-Instanzen verwenden dieselbe Hosting-Plattform, und diese Plattform hat einen Ausfall erlitten.

![]([LINK_URL_4])

1. Die ausgehende HTTPS (darunter WebSockets)-Verbindung zur Uptrends Cloud-Plattform als Befehls- und Steuerzentrum, um Prüfobjektdefinitionen abzurufen und Ergebnisse zurückzusenden. Die ausgehende WebSockets-Verbindung wird verwendet, um Befehle zu erhalten, und wird langfristig offen sein. Sie ist für vier Uptrends Standorte auf der Whitelist.
2. Ausgehende HTTPS-Verbindung, um Container-Updates mit Checkpoint- und Browser-Updates abzurufen
3. Ausgehende Internet-Verbindung, um den Widerrufsstatus von verwendeten Zertifikaten zu validieren
4. Verbindung von Uptrends‘ privatem Checkpoint zur überwachten Infrastruktur mit geblockter Verbindung zu allen anderen Teilen der Plattform

## Wie erhalte ich einen privaten Checkpoint? 

Sobald du entschieden hast, deine interne Infrastruktur mit einem privaten Docker-Checkpoint zu überwachen, bereite die Infrastruktur vor: Richte (vorzugsweise) 2 Windows serverbasierte Hosts wie im Artikel [Einen privaten Docker-Checkpoint installieren]([LINK_URL_5]) erläutert, ein.

Hast du zu irgendeinem Zeitpunkt Fragen, zögere nicht, sie mittels Uptrends’ [Ticket-System]([LINK_URL_6]) zu stellen. Besprechungen und die getroffenen Entscheidungen werden über unser Ticket-System protokolliert. Du kannst diese Besprechungen nachlesen, Anmerkungen machen und dem Support-Mitarbeiter, der deinem Ticket zugewiesen ist, direkt Fragen stellen.

## Sicherheitsbetrachtungen

Obwohl Uptrends die Best-Practices- und Due-Diligence-Standards in Sachen Sicherheit anwendet, liegt die Verantwortung für die Einwirkungen des privaten Checkpoints auf das Netzwerk des Kunden beim Kunden selbst. Unten findest du weitere Infos darüber, wer für welchen Bereich verantwortlich ist.

### Uptrends’ Verantwortlichkeiten

- Stellt private Checkpoint-Container mit aktueller Software bereit
- Hält alle in Containern verwendeten Software-Komponenten (d. h. die Grundlage des Image und die Webbrowser) auf dem neuesten Stand
- Verschlüsselt den gesamten Traffic von und zur Plattform des Kunden
- Stellt Informationen zur Erstellung von Whitelists bereit

### Verantwortlichkeiten des Nutzers:

- Wendet Firewall-Regeln an, die nur Zugang zur Infrastruktur gewähren, die überwacht werden soll
- Verwendet Accounts beim Monitoring mit eingeschränkter Exposition gegenüber der Plattform
- Nutzt Virenscans usw., wo zutreffend
- Wendet, falls erforderlich, zusätzliche Sicherheitsmaßnahmen an (z. B., wenn eine Transaktion einen wiederholten Geldtransfer ausführt)
- Aktualisiert den Docker-Host und -Container vorzugsweise täglich, aber zumindest alle zwei Wochen, um sicherzustellen, dass die aktuellen Browserversionen verwendet und die neuesten Sicherheits-Patches angewendet werden
- Hält das Host-Betriebssystem auf dem neuesten Stand
- Erwägt, bei den Prüfobjekttypen Basic und Browser [Snapshots, Screenshots und Filmstrips zu deaktivieren]([LINK_URL_7]).

[SHORTCODE_1] Solltest du weitere Informationen benötigen, sieh dir unsere Seite [Private Checkpoints – FAQ]([LINK_URL_8]) an. [SHORTCODE_2]
