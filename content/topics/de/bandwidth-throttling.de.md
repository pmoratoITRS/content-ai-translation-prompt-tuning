{
  "hero": {
    "title": "Bandbreiten-Drosselung"
  },
  "title": "Bandbreiten-Drosselung",
  "summary": "FPC- und Transaktionsprüfobjekte ermöglichen zwei unterschiedliche Methoden der Bandbreiten-Drosselung: Simulierte und browserbasierte Drosselung mit Chrome.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/bandbreiten-drosselung",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/bandwidth-throttling"
}

Um dein synthetisches Monitoring den tatsächlichen Geschwindigkeiten der Nutzer anzugleichen, empfehlen wir eine Bandbreiten-Drosselung bei den Prüfobjekten des Full Pagechecks (FPC) und der Transaktionen.

## Warum Bandbreiten-Drosselung?

Uptrends' Checkpoint-Computer befinden sich in Datenzentren. Ihre ursprüngliche Geschwindigkeit entspricht der eines üblichen Nutzers, der in einem Hochgeschwindigkeitsnetzwerk arbeitet, wie es auch in deinem Büro zu finden ist. Wenn deine Kundenbasis hauptsächlich aus Desktop-Nutzern besteht, repräsentieren die Geschwindigkeiten an Uptrends’ Checkpoints deine Nutzer wahrscheinlich ganz richtig. Wenn Nutzer aber auf deine Website oder deinen Service über ein Mobilgerät oder eine langsamere DSL-Verbindung zugreifen, solltest du in Betracht ziehen, ein Prüfobjekt einzurichten, das das Erleben deiner Nutzer spiegelt. Dafür haben wir dann die Bandbreiten-Drosselung.

## Arten der Bandbreiten-Drosselung

Uptrends bietet zwei Arten der Bandbreiten-Drosselung: die simulierte und die browserbasierte Drosselung. Für beide bestehen die gleichen Optionen von Verbindungsgeschwindigkeiten. Die browserbasierte Drosselung ist nur für Chrome verfügbar, die simulierte Bandbreiten-Drosselung ist für alle Browsertypen verfügbar.

### Browserbasierte Bandbreiten-Drosselung

Du kannst eine browserbasierte Bandbreiten-Drosselung wählen, wenn du den Chrome-Browser für dein FPC-Monitoring eingestellt hast. Es ist die bevorzugte Art. Browserbasierte Bandbreiten-Drosselung nutzt die gleiche Bandbreiten-Drosselung, die auch in den Chrome-Entwicklertools verfügbar ist. Die Bandbreiten-Drosselung mit Chrome unterscheidet sich von der simulierten Drosselung, da Chrome neben der Simulation einer geringeren Bandbreite Latenz hinzufügt. Die browserbasierte Drosselung bietet eine präzisere Messung, insbesondere bei Webseiten, die entweder sehr wenig oder sehr viele Verbindungen benötigen. Darüber hinaus verfolgt Chrome die Anzahl der Verbindungen und drosselt sie zusammen, was für Websites mit einer geringeren oder höheren durchschnittlichen Anzahl an Quellen genauer ist.

Die browserbasierte Drosselung aktivieren:

1.  Erstelle ein neues FPC-Prüfobjekt oder rufe ein bestehendes FPC-Prüfobjekt auf.
2.  Öffne die Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.
3.  Wähle **Chrome mit extra Metriken** als {{< AppElement type="menuitem" >}}Browsertyp{{< /AppElement >}}.
![Bandbreiten-Drosselung – browserbasiert](/img/content/scr-fpc-bandwidth-browser.min.png)
4.  Wähle **Browser** unter {{< AppElement type="menuitem" >}}Bandbreiten-Drosselung{{< /AppElement >}}, dann die Verbindungsgeschwindigkeit, die du verwenden möchtest (siehe unten).
5.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.

### Simulierte Bandbreiten-Drosselung

Du kannst die simulierte Drosselung mit jedem gewünschten Browser einrichten, außer Chrome. Bei der simulierten Drosselung wird ein Proxy eingesetzt, um eine angemessene Simulation der unterschiedlichen möglichen Verbindungsgeschwindigkeiten zu bieten.

Der Checkpoint drosselt jede Verbindung, die der Browser aufbaut und simuliert dabei die verfügbare Durchschnittsbandbreite des gewählten Verbindungstyps. Der Checkpoint berücksichtigt dabei nicht die Netzwerklatenz und erstellt seine Berechnungen aufgrund einer durchschnittlichen Anzahl von Verbindungen.

1.  Erstelle ein neues FPC-Prüfobjekt oder rufe ein bestehendes FPC-Prüfobjekt auf.
2.  Öffne die Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.
3.  Wähle den {{< AppElement type="menuitem" >}}Browsertyp{{< /AppElement >}}.
![Bandbreiten-Drosselung – simuliert](/img/content/scr-fpc-bandwidth-simulated.min.png)
4.  Wähle **Simuliert** unter {{< AppElement type="menuitem" >}}Bandbreiten-Drosselung{{< /AppElement >}}, dann die Verbindungsgeschwindigkeit, die du verwenden möchtest (siehe unten).
5.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.


## Verbindungsarten

Wir basieren die unterschiedlichen wählbaren Verbindungsarten bei der Bandbreiten-Drosselung auf reale Nutzerszenarien und nicht auf die theoretischen Maximalgeschwindigkeiten, die diese Technologien bereitstellen können. Das browserbasierte Drosseln wendet eine Netzwerklatenz auf deine Ergebnisse an.

**ADSL**: 4 Mbit Download, 0,5 Mbit Upload, 80 ms Round Trip Time  
**Kabel**: 5 Mbit Download, 1 Mbit Upload, 50 ms Round Trip Time  
**Glasfaser**: 15 Mbit Download, 3 Mbit Upload, 10 ms Round Trip Time  
  
**2G**: 200 Kbit Download, 200 Kbit Upload, 1000 ms Round Trip Time  
**3 G**: 1 Mbit Download, 500 Kbit Upload, 300 ms Round Trip Time  
**4 G**: 4 Mbit Download, 4 Mbit Upload, 230 ms Round Trip Time  
