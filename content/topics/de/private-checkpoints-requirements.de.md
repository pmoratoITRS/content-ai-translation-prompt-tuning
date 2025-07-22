{
  "hero": {
    "title": "Private Standorte – Anforderungen"
  },
  "title": "Private Standorte – Anforderungen",
  "summary": "Was sind die technischen Anforderungen bei privaten Standorten??",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-checkpoints-voraussetzungen",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-requirements"
}

## Voraussetzungen und notwendige Einstellungen

Es gibt einige Anforderungen an Hardware und Netzwerk sowie an den Netzwerkeinstellungen. Diese Anforderungen beruhen auf übliche Anwendungsbereiche. Solltest du nicht genau wissen, was du brauchst, wende dich an den [Uptrends Support]({{< ref path="contact" lang="de" >}}). Achte darauf, die Anforderungen zu erfüllen und die Einstellungen vorgenommen zu haben, bevor du einen Checkpoint installierst.

## Private Standorte – Kapazität

Die privaten Standorte werden nur für deine Prüfobjekte genutzt. Die Voraussetzungen hängen von der Art des Monitorings ab, das von den Checkpoints an privaten Standorten ausgeführt wird.

Nicht browserbasiertes Monitoring wie HTTPS, Connect, Ping und Multi-step API wirkt sich hauptsächlich auf die verfügbare Netzwerkkapazität aus. Browserbasierte Prüfobjekte wirken sich hauptsächlich auf die Serverkapazität (CPU, Speicher, Datenträger-E/A) aus.

### Berechnung einer typischen Kapazitätsanforderung 

Die übliche Kapazität für eine empfohlene Einrichtung eines privaten Standorts bei Nutzung der empfohlenen [Hardware]({{< ref path="#hardware-requirements" lang="de" >}}) sowie zwei Checkpoints wäre:

- 2 x 10 Transaktionen mit 5-Minuten-Intervallen
- 2 x 10 Full Pagechecks mit 5-Minuten-Intervallen
- 100 Basic Prüfobjekte mit 1-Minuten-Intervallen

Die Dauer der Transaktion wirkt sich auf die Kapazität aus.

Die Einrichtung berücksichtigt Kapazitäten für:

- Bestätigung [unbestätigter Fehler]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}})
- Wartung eines der Checkpoints, um z. B. ein Upgrade des Docker-Hosts oder der Container durchzuführen

### Redundanz

Die oben beschriebene Kapazität berücksichtigt nicht die Redundanz von Prüfobjekten. Es gibt einige Konfigurationen, bei denen ein privater Standort tatsächlich weitere Monitoring-Aufgaben als oben angegeben ausführen kann. So zum Beispiel, wenn auf unterschiedlichen Ebenen eine Redundanz vorhanden ist, etwa beim Einsatz mehrerer privater Standorte für dein Monitoring.

## Hardware-Anforderungen {id="hardware-requirements"}

Prüfe die folgenden Hardware-Anforderungen für den Einsatz eines Checkpoints. Aus Gründen der Zuverlässigkeit, empfehlen wir, zwei Checkpoints zu verwenden. Die beste Performance erhältst du, wenn du drei oder mehr Checkpoints einsetzt. Jeder Checkpoint sollte den folgenden Spezifizierungen entsprechen.

|   | Empfohlen | Minimum |
| --- | --- | --- |
| **CPU** | Quad-Core | Dual-Core |
| **RAM** | 8 GB | 4 GB |
| **Speicher** | 60 GB auf SSD | 60 GB |
| **Betriebssystem** | Windows Server 2022 LTSC Standard | Windows Server 2019 LTSC Standard* |

* Bitte beachte, dass für Docker auf Windows Server 2019 Probleme bei der DNS-Auflösung bekannt sind.

## Netzwerk-Anforderungen

Die folgenden Netzwerkanforderungen müssen erfüllt werden.

**IPv4** – Feste IPv4-Adresse für jeden Checkpoint-Server

**IPv6** – Optional, abhängig davon, ob IPv6 in der überwachten Infrastruktur verwendet wird

**Netzwerk** – Obwohl wir 1 Gbit/s empfehlen, ist die Auslastung der Verbindung sehr viel geringer (in der Regel 1 bis 10 Mbit/s zu 95 % der Zeit) und sehr konstant.
Eine Verbindung mit dem Internet, die gut dimensioniert ist, um die Messdaten an die Uptrends Plattform zu übertragen.



## Netzwerkeinstellungen

### Firewall

Es sollte keine SSL Inspection auf dem Traffic zwischen den Checkpoints und den Cloud-Servern von Uptrends geben.

Stelle sicher, dass keine Gruppenrichtlinienobjekte (Group Policy Objects, GPOs) eingerichtet sind, was Docker daran hindern würde, eine lokale Firewall zu erzeugen. Setze für den Rechner, auf dem Docker ausgeführt wird, die Gruppenrichtlinie *Lokale Firewallregeln anwenden* auf „Ja“.

### IPv6-Anforderungen

Ist für das interne Netzwerk IPv6 aktiviert, gib eine feste IPv6-Adresse und ein Gateway für jeden Checkpoint-Server ein. Die IPv6-IP-Adresse ermöglicht uns, deine Infrastruktur über IPv6 (mit der richtigen Firewall-Konfiguration) zu überwachen. Ohne feste IPv6-Adresse kann Uptrends nur über IPv4 überwachen.

### DNS-Server

Der Checkpoint erfordert, dass auf dem Docker-Host ein oder mehrere DNS-Server konfiguriert sind. Standardmäßig nutzen Container die DNS-Konfiguration des Hosts, um Host-Namen für die geprüften Anwendungen und für die Verbindung zur Uptrends Cloud-Plattform aufzulösen.

### FCrDNS

Wenn du Mail-Server über eine externe Route überwachen möchtest, konfiguriere ein Reverse DNS, sodass checkpoint_name@uptrends.net auf die entsprechende externe IP-Adresse aufgelöst wird.


