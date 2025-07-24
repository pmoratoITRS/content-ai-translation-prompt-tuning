{
  "hero": {
    "title": "Checkpoint-Zustand"
  },
  "title": "Checkpoint-Zustand",
  "summary": "Erhalte einen Überblick über den Status deiner Checkpoints an privaten Standorten. Funktionieren sie gut oder brauchen sie Aufmerksamkeit?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-standorte/private-locations-checkpoint-health",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Deine Checkpoints an [privaten Standorten]([LINK_URL_1]) können das Monitoring nur richtig ausführen, wenn ihr Zustand einwandfrei ist. Die Registerkarte [SHORTCODE_1] Checkpoint-Zustand [SHORTCODE_2] liefert einen Einblick zu den wichtigen Daten, die sich auf den Zustand eines Checkpoints auswirken. Das umfasst Informationen zur installierten Software genauso wie Metriken zum Host. Weitere Informationen findest du unten.

## Wie erhalte ich die Informationen zu Checkpoint-Zustand?

1. Gehe zu [SHORTCODE_3] Private Locations [SHORTCODE_4].
2. Erweitere in der List der privaten Standorte den Standort mit dem Checkpoint, zu dem du mehr wissen möchtest.
3. Klicke auf den Checkpoint und wähle die Registerkarte [SHORTCODE_5] Checkpoint-Zustand [SHORTCODE_6].

![Screenshot der Registerkarte Checkpoint-Zustand]([LINK_URL_2])

Hinweis: Du siehst die Registerkarte nur, wenn du den Checkpoint vollständig installiert hast. Ansonsten siehst du lediglich die Registerkarte [SHORTCODE_7] Installation [SHORTCODE_8] und musst zunächst den Checkpoint installieren. Folge den Anweisungen im Artikel [Einen Docker-Checkpoint installieren]([LINK_URL_3]), um den Checkpoint in Betrieb zu nehmen.

## Uptrends’ Software

Dieser Abschnitt zeigt an, ob die Software von Uptrends korrekt installiert ist und ob die verschiedenen Services, die für das Monitoring erforderlich sind, funktionieren. Jeder Bereich des Abschnitts über die **Software von Uptrends** kann den Status aktiv oder inaktiv haben. Aber alle sollten den Status „aktiv“ haben, damit der Checkpoint die Monitoring-Aufgaben ausführen kann.

Der Checkpoint-Container wird verwendet, um alle nicht browserbasierten Prüfungen auszuführen.
Der Transaction-Processor-Container wird genutzt, um Real-Browser-Tests ([Full Pagechecks]([LINK_URL_4]), [Transaktionsprüfobjekte]([LINK_URL_5])) auszuführen.
Der Relay-Container wird als ein Kommunikationsrelais zwischen den anderen Containern und den Uptrends Cloud-Diensten verwendet.

Bitte beachte, dass Uptrends Container Images mit übereinstimmenden Versionsnummern veröffentlicht und nur diese Release-Kombinationen testet. Es wird empfohlen, nur übereinstimmende Versionen zu verwenden.

## Browser

Auf dem Checkpoint, der die Real-Browser-Tests ([Full Pagechecks]([LINK_URL_6]), [Transaktionsprüfobjekte]([LINK_URL_7])) ausführen soll, müssen die gewünschten Browser installiert sein.

In diesem Abschnitt siehst du die installierten Browser mit der Versionsnummer und kannst ihre Aktualität überprüfen.
Uptrends stellt Container Images mit den aktuellen Browsern bereit. Achte bitte darauf, deine Container bei Verfügbarkeit zu aktualisieren.

## Host-Details

Die (virtuelle) Maschine, auf der dein Checkpoint installiert ist, muss in einem guten Zustand sein und über ausreichend Speicher verfügen, um die Monitoring-Aufgaben auszuführen.

Überprüfe bitte hier die Infos zu deinem System, um mögliche Engpässe zu erkennen.

## Die Host-Konfiguration

In diesem Abschnitt findest du die Konfigurationsdetails des Host des privaten Standorts, wie DNS Server, Zeitzone und Spracheinstellungen.

## Datenschutzeinstellungen

Dieser Abschnitt zeigt, ob ein Datenschutz aktiviert ist. Ein grüner Haken besagt, dass Daten angezeigt werden, Datenschutz also nicht aktiviert ist. Weitere Infos zur Einrichtung des Datenschutzes bei deinen private Checkpoints findest du im Artikel zum [Datenschutz]([LINK_URL_8]).


