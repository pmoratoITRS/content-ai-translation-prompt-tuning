{
  "hero": {
    "title": "Checkpoint-Zustand"
  },
  "title": "Checkpoint-Zustand",
  "summary": "Erhalte einen Überblick über den Status deiner Checkpoints an privaten Standorten. Funktionieren sie gut oder brauchen sie Aufmerksamkeit?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-locations-checkpoint-health",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-checkpoint-health"
}

Deine Checkpoints an [privaten Standorten]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) können das Monitoring nur richtig ausführen, wenn ihr Zustand einwandfrei ist. Die Registerkarte {{< AppElement type="tab" >}} Checkpoint-Zustand {{< /AppElement >}} liefert einen Einblick zu den wichtigen Daten, die sich auf den Zustand eines Checkpoints auswirken. Das umfasst Informationen zur installierten Software genauso wie Metriken zum Host. Weitere Informationen findest du unten.

## Wie erhalte ich die Informationen zu Checkpoint-Zustand?

1. Gehe zu {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}}.
2. Erweitere in der List der privaten Standorte den Standort mit dem Checkpoint, zu dem du mehr wissen möchtest.
3. Klicke auf den Checkpoint und wähle die Registerkarte {{< AppElement type="tab" >}} Checkpoint-Zustand {{< /AppElement >}}.

![Screenshot der Registerkarte Checkpoint-Zustand](/img/content/scr_private-location-checkpoint-health.min.png)

Hinweis: Du siehst die Registerkarte nur, wenn du den Checkpoint vollständig installiert hast. Ansonsten siehst du lediglich die Registerkarte {{< AppElement type="tab" >}} Installation {{< /AppElement >}} und musst zunächst den Checkpoint installieren. Folge den Anweisungen im Artikel [Einen Docker-Checkpoint installieren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}), um den Checkpoint in Betrieb zu nehmen.

## Uptrends’ Software

Dieser Abschnitt zeigt an, ob die Software von Uptrends korrekt installiert ist und ob die verschiedenen Services, die für das Monitoring erforderlich sind, funktionieren. Jeder Bereich des Abschnitts über die **Software von Uptrends** kann den Status aktiv oder inaktiv haben. Aber alle sollten den Status „aktiv“ haben, damit der Checkpoint die Monitoring-Aufgaben ausführen kann.

Der Checkpoint-Container wird verwendet, um alle nicht browserbasierten Prüfungen auszuführen.
Der Transaction-Processor-Container wird genutzt, um Real-Browser-Tests ([Full Pagechecks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}), [Transaktionsprüfobjekte]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}})) auszuführen.
Der Relay-Container wird als ein Kommunikationsrelais zwischen den anderen Containern und den Uptrends Cloud-Diensten verwendet.

Bitte beachte, dass Uptrends Container Images mit übereinstimmenden Versionsnummern veröffentlicht und nur diese Release-Kombinationen testet. Es wird empfohlen, nur übereinstimmende Versionen zu verwenden.

## Browser

Auf dem Checkpoint, der die Real-Browser-Tests ([Full Pagechecks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}), [Transaktionsprüfobjekte]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="de" >}})) ausführen soll, müssen die gewünschten Browser installiert sein.

In diesem Abschnitt siehst du die installierten Browser mit der Versionsnummer und kannst ihre Aktualität überprüfen.
Uptrends stellt Container Images mit den aktuellen Browsern bereit. Achte bitte darauf, deine Container bei Verfügbarkeit zu aktualisieren.

## Host-Details

Die (virtuelle) Maschine, auf der dein Checkpoint installiert ist, muss in einem guten Zustand sein und über ausreichend Speicher verfügen, um die Monitoring-Aufgaben auszuführen.

Überprüfe bitte hier die Infos zu deinem System, um mögliche Engpässe zu erkennen.

## Die Host-Konfiguration

In diesem Abschnitt findest du die Konfigurationsdetails des Host des privaten Standorts, wie DNS Server, Zeitzone und Spracheinstellungen.

## Datenschutzeinstellungen

Dieser Abschnitt zeigt, ob ein Datenschutz aktiviert ist. Ein grüner Haken besagt, dass Daten angezeigt werden, Datenschutz also nicht aktiviert ist. Weitere Infos zur Einrichtung des Datenschutzes bei deinen private Checkpoints findest du im Artikel zum [Datenschutz]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}).


