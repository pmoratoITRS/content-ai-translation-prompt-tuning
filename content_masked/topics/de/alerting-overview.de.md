{
  "hero": {
    "title": "Alarmierungen – Überblick"
  },
  "title": "Alarmierungen – Überblick",
  "summary": "Wie Alarmierungen funktionieren. Der Check durch ein Prüfobjekt erzeugt einen Fehler, was zu einem Alarm führt, der auf Basis einer Meldedefinition eine Warnmeldung auslöst.",
  "url": "[URL_BASE_TOPICS]alarme/alarmierung-uebersicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In der realen Welt wird erwartet, dass Websites, Server und alle anderen Systeme rund um die Uhr laufen und ununterbrochen verfügbar sind. In einer Welt, in der Services ständig bereitstehen müssen, sind Warnmeldung ein wichtiges Tool, um dich auf dem Laufenden zu halten, wenn ein Problem auftaucht oder wenn etwas in deinem System unregelmäßig erscheint. Warnmeldungen stellen sicher, dass dein System immer verfügbar ist und Ausfallzeiten minimiert werden.

Eine der Hauptfunktionen des Uptrends Monitoring Service ist die **Alarmierung**. Werden von deinen Prüfobjekten Fehler erkannt, wirst du sofort mit einer Warnmeldung benachrichtigt. Die folgende Illustration zeigt eine Zusammenfassung des Alarmierungs-Workflows von Uptrends:

![Illustration Alarmierungs-Workflow]([LINK_URL_1])

Einfach gesagt wird ein Alarm erzeugt, wenn eine dieser vier Definitionen besteht: *Prüfobjektsüberwachung, Fehlerbedingung, Meldedefinition und Integration*. Wenn du dein Prüfobjekt erstellt und die Einstellungen konfiguriert hast, führt das Prüfobjekt mehrere Überwachungen gemäß den Definitionen in den Prüfobjekteinstellungen aus. Wenn ein Check bzw. eine Prüfung eines Prüfobjekts zu einem [bestätigten Fehler]([LINK_URL_2]) führt, wird in der Uptrends Webanwendung ein Alarm generiert. Dieser Alarm löst das Senden einer Warnmeldung an einen Operator oder an eine externe Anwendung aus.


Mit diesem Artikel sehen wir uns den Workflow detailliert an, wie ein Check zu einer Meldung wird.

## Checks durch Prüfobjekte

Am Anfang stehen die Checks durch die Prüfobjekte, die in einem von dir bestimmten Intervall ausgeführt werden. Der Check vom Prüfobjekt umfasst Standardüberprüfungen je nach Prüfobjekttyp, zum Beispiel auf Verfügbarkeit. Dazu kannst du eigene Fehlerbedingungen einrichten. Darunter fallen zum Beispiel Höchstgrenzen zu Ladezeiten oder eine Übereinstimmungsabfrage.

![Einstellungen Prüfobjektchecks]([LINK_URL_3])

Der Knowledge-Base-Artikel [Fehlerbedingungen]([LINK_URL_4]) erläutert im Detail, wie Fehlerbedingungen konfiguriert werden können.

Ein Fehler wird angezeigt, wenn das Prüfobjekt ein Problem aufdeckt, weil der Standardcheck fehlschlägt oder eine Fehlerbedingung erfüllt wird.

## Fehler

Alle Fehler werden im Abschnitt **Fehler Übersicht** aufgeführt. Du kannst einen Filter einrichten, welche Art Fehler (*OK, unbestätigt, bestätigt*) und für welchen Zeitraum diese angezeigt werden sollen. Im [Knowledge-Base-Artikel des Dashboards]([LINK_URL_5]) erfährst du mehr über Filter und anpassen von Dashboard-Einstellungen.

Das folgende Beispiel einer Fehler-Übersicht zeigt unbestätigte (gelb) und bestätigte (rot) Fehler:

![Dashboard Fehler Übersicht]([LINK_URL_6])

Wie die Illustration zeigt, wird das erste Auftreten eines Fehlers als unbestätigter Fehler betrachtet. Es kann ein vorübergehendes Auftreten oder ein Problem am Checkpoint sein. Deshalb wird ein zweiter Prüfobjekt-Check von einem anderen Checkpoint durchgeführt. Wird hier ein Fehler gemeldet, führt dies zu einem bestätigten Fehler, was einen Alarm generiert.

Mehr zu diesem Ablauf findest du im Knowledge-Base-Artikel [Nicht bestätigte und bestätigte Fehler]([LINK_URL_7]).

### Abfolgen von Fehlern

Es gibt unterschiedliche Szenarien für eine Abfolge von Fehlern, die im Bild unten dargestellt werden:

– Ein unbestätigter Fehler, gefolgt von einem OK-Ergebnis. Dies erzeugt keinen Alarm.
– Ein unbestätigter Fehler, gefolgt von einem bestätigten Fehler, dann gefolgt von einem OK-Ergebnis. Dies führt zu einem Alarm, wenn deine Meldedefinition so eingestellt ist, dass sie „einen Alarm, wenn 1 oder mehr Fehler aufgetreten“ sind, generiert.
– Eine Anzahl (n) unbestätigter und bestätigter Fehler treten nacheinander auf. Dies führt zu einem Alarm, wenn deine Meldedefinition so eingestellt ist, dass sie „einen Alarm, wenn n oder mehr Fehler aufgetreten“ sind, generiert. Alternativ kannst du ein Zeitlimit für Fehler einsetzen. Wenn die Abfolge von Fehlern dieses Zeitlimit erreicht, wenn also beispielsweise ein Fehler länger als fünf Minuten auftritt, wird ein Alarm erzeugt.

![]([LINK_URL_8])

## Alarme

Die Meldedefinition steuert die Erzeugung von Alarmen für unterschiedliche Eskalationsstufen. Die Eskalationsstufen werden verwendet, um Alarme in Phasen auszulösen und die ausgewählten Operatoren auf die richtige Weise zu benachrichtigen. Dabei werden die Dringlichkeit des Problems und die gesteigerte Dringlichkeit bei Fortbestehen des Problems berücksichtigt.

Für jede Stufe kannst du eingeben, ob ein Alarm erzeugt wird, welche Operatoren (Gruppen) benachrichtigt werden, wann das Zeitlimit überschritten ist (Fehler dauern länger als x Minuten), oder ob ein Alarm erzeugt wird, nachdem eine Anzahl von Fehlern aufgetreten ist (n oder mehr Fehler sind aufgetreten). Alle Fehler müssen bestätigte Fehler sein. Unbestätigte Fehler werden bei diesen Bedingungen nicht berücksichtigt.

Zusätzlich zum ersten Alarm kannst du einen oder mehrere Erinnerungsalarme einrichten. Du kannst eine Maximalzahl an Erinnerungen und das Intervall, in dem sie erzeugt werden sollen, bestimmen. Diese Option ist für jede Eskalationsstufe individuell einstellbar.

Die Knowledge-Base-Artikel [Erstellen von Meldedefinitionen]([LINK_URL_9]) und [Eskalationsstufen zu Alarmen]([LINK_URL_10]) enthalten weitere Informationen zu Meldedefinitionen.

Hinweis: Im Prüfobjekt muss *Alarme generieren* aktiviert sein, damit überhaupt Warnmeldungen erzeugt werden.

Wenn der Fehler aufgelöst wurde (wenn dieselbe Prüfung also ein OK statt eines Fehlers zurückgibt) wird eine Entwarnungsmeldung (OK-Meldung) erzeugt.

Alle Alarme werden in der **Alarmierungshistorie** angezeigt. Die auf einen Fehler beruhenden Alarme werden rot markiert, OK-Meldungen grün. Solang der Fehler nicht behoben und keine Entwarnungsmeldung erzeugt wird, bleibt der Alarm ein aktiver Alarm. Alle aktiven Alarme werden im Dashboard **Aktuelle Alarmierungen** aufgelistet.

![]([LINK_URL_11])

Suchst du nach einer bestimmten, von dir erstellten **Meldedefinition**? Du kannst die [Suche]([LINK_URL_12]) von Uptrends verwenden, um sie schnell zu finden.

## Benachrichtigungen

Mit dem Dashboard **Alarmierungshistorie** kannst du deine Alarme von einem Ort aus überblicken. Aber es ist auch bequem, Benachrichtigungen in Echtzeit über den Alarmstatus zu erhalten und nicht die Webanwendung aufrufen zu müssen. Uptrends bietet [Integrationen]([LINK_URL_13]), die dir eine ganze Bandbreite an Möglichkeiten gibt Alarmierungsmitteilungen an dich, andere oder externe Systeme zu senden und sofort benachrichtigt zu werden.

Um eine Nachricht zu senden, wenn ein Alarm generiert wird, musst du zunächst die [Meldedefinition]([LINK_URL_14]) einrichten und dann für jede Eskalationsstufe den [Integrationstyp]([LINK_URL_15]) wählen. Sobald dies erfolgt ist, erhältst du ganz einfach Updates auf Grundlage deiner bevorzugten Integration.

### Testen von Warnmeldungen

Da du Warnmeldungen so bald wie möglich erhalten solltest, solltest du als Erstes sicherstellen, dass das Senden von Warnmeldungen tatsächlich funktioniert. Der Knowledge-Base-Artikel [Testen von Warnmeldungen]([LINK_URL_16]) erläutert, wie du dies für unterschiedliche Integrationen testen kannst.

Rufe den Abschnitt [Fehlerbehebung]([LINK_URL_17]) auf, um mehr zu erfahren!
