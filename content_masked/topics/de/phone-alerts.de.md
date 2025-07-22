{
  "hero": {
    "title": "Einrichtung der telefonischen (Sprach-)Alarmierung"
  },
  "title": "Einrichtung der telefonischen (Sprach-)Alarmierung",
  "summary": "Alles, was du zu Uptrends‘ telefonischer Alarmierung wissen musst: Einrichtung, Beispielnachrichten, Testen und Auswahl der ausgehenden Telefonnummer. ",
  "url": "[URL_BASE_TOPICS]alarme/telefon-alarm",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Manchmal reicht eine E-Mail, SMS oder eine integrierte Nachricht von Slack oder PagerDuty einfach nicht aus. Manchmal muss man das Telefon klingeln hören, damit die Aufmerksamkeit von anderen Beschäftigungen auf die Nachricht gelenkt wird. Telefonalarmierungen bieten das. Auf Grundlage deiner Alarmierungs- und Eskalationsstufen sowie Operatorzeitpläne kannst du einstellen, dass der diensthabende Operator einen Telefonanruf mit automatischer Sprachmitteilung über die Alarmierungsbedingung erhält. Dieser Knowledge-Base-Artikel informiert dich über:

-   [Einrichten der Telefonalarmierungen]([LINK_URL_1])
-   [Einrichten der Operatoren für Telefonalarmierungen]([LINK_URL_2])
-   [Einrichten der Meldedefinitionen für Telefonalarmierungen]([LINK_URL_3])
-   [Einsatz von Nachrichten-Credits]([LINK_URL_4])
-   [Was passiert, wenn du den Anruf entgegennimmst]([LINK_URL_5])

## Uptrends für Telefonalarmierungen einrichten [ANCHOR_1]

Um deinem Arsenal an Benachrichtigungstools Telefonalarmierungen hinzuzufügen, musst du mindestens über einen Premium-Account verfügen.

[SHORTCODE_1]
**Hinweis**: Du kannst ganz einfach von der Einstiegsstufe aufrüsten, indem du dich mit deinem Vertriebspartner in Verbindung setzt. Du kannst auch ein Ticket über unseren Support einreichen und wir melden uns umgehend bei dir. Besuche die [Kontakt]([LINK_URL_6])-Seite, um weitere Informationen zu erhalten.
[SHORTCODE_2]

Die Telefonalarmierung ist nicht direkt standardmäßig aktiviert. Um Telefonalarmierungen zu erhalten, musst du diese auf der Seite **Integrationen** im Menü [SHORTCODE_9]Alarme[SHORTCODE_10] aktivieren. Sobald diese aktiviert sind, kannst du Telefonalarmierungen in den Eskalationsstufen hinzufügen. Telefonalarmierungen aktivieren:

1.  Wähle **Telefon** im Feld **Integrations-Art** aus.
2.  Verwende den Standardnamen oder ändere ihn im Feld **Integrationsname**.
3.  Wähle aus dem Feld **Ausgehende Telefonnummer** eine Nummer. Wähle die Nummer auf Grundlage deines Standorts. Sollte dein Land nicht in der Liste aufgeführt sein, wähle das nächstgelegene. Du (und dein Team) können die Nummer in deinen Kontakten zur schnellen Identifikation aufnehmen. Wenn du den **Systemstandard** aktiviert lässt, wird Uptrends die beste Telefonnummer auf Grundlage der Ländervorwahl des Empfängers (Operators) auswählen.
    [SHORTCODE_3]**Hinweis:** Prüfe die [Liste unterstützter Länder]([LINK_URL_7]) und Ländervorwahlen der empfangenden Telefonnummer des Operators. Findest du Land und Ländervorwahl des Operators nicht in der Liste, werden sie KEINE Alarmierungsanrufe erhalten.[SHORTCODE_4]
4.  Wähle die **Sprache** für die Telefonalarmierung nur, wenn du die Spracheinstellungen auf Operatorebene überschreiben möchtest.
5.  Prüfe, dass der Prüfobjektname für die Sprachausgabe geeignet ist. Sollte dies nicht so sein, aktiviere das Kontrollkästchen **Nutze abweichende Überwachungsnamen**. Erfahre mehr über das [Aktivieren und Einrichten sprachausgabegeeigneter Prüfobjektnamen]([LINK_URL_8]).
6.  Markiere das Kontrollfeld **Aktiv**, sofern es noch nicht aktiviert ist
7.  Klicke auf [SHORTCODE_11]Speichern[SHORTCODE_12].

![screenshot phone integration]([LINK_URL_9])

## Einrichten von Operatoren [ANCHOR_2]

Auf der Registerkarte [SHORTCODE_13]Allgemein[SHORTCODE_14] auf der Einrichtungsseite von Operatoren besteht die Option, eine **Mobiltelefonnummer** hinzuzufügen und die ausgehende **Telefonnummer** zu überschreiben, die du bei der Aktivierung der Telefonalarmierung angegeben hast. Solltest du bereits die Alarmierung per SMS in der Meldedefinition definiert haben, musst du die Operator-Profile eventuell nicht anpassen.

### Eine Mobiltelefonnummer hinzufügen:

Das System verwendet die Mobilnummer des Operators, um SMS-Warnmeldungen zu senden. Uptrends verwendet dieselbe Nummer für Telefonalarmierung. Eine Telefonnummer hinzufügen

1.  Gib das Plus-Zeichen (+) gefolgt von der Landesvorwahl und dann der Telefonnummer ein.
2.  Verwende keine nicht numerischen Zeichen. Die Telefonnummer für einen Anschluss in den USA sollte zum Beispiel folgendermaßen aussehen: +15551234567.
3.  Klicke auf [SHORTCODE_15]Speichern[SHORTCODE_16].

[SHORTCODE_5]
**Hinweis**: Du kannst auch eine Festnetznummer in das Feld **Mobiltelefon** eingeben (hat noch jemand Festnetz?), aber wenn du auch die SMS-Warnmeldungen nutzen möchten, wird der Operator keine SMS-Warnmeldungen erhalten. Wenn du für einen Operator eine Festnetznummer statt Mobilnummer eingibst, füge diesen Operator in den Eskalationseinstellungen nicht für SMS-Warnmeldungen hinzu.
[SHORTCODE_6]

### Die standardmäßige ausgehende Telefonnummer überschreiben

Wenn du eine **ausgehende Telefonnummer** auf der Telefonintegrationsseite eingegeben hast, musst du dies eventuell für einzelne Operator überschreiben. Durch Auswahl von **Überschreibe Telefonintegrations-Einstellungen** wird Uptrends die von dir in dem Telefonauswahlmenü ausgewählte alternative Nummer verwenden.

![Screenshot Operator Telefoneinstellungen]([LINK_URL_10])
## Eskalationen für Telefonalarmierungen einrichten [ANCHOR_3]

Wenn du die Telefonalarmierungen aktiviert und den Operatoren Telefonnummern zugewiesen hast, kannst du die Eskalationseinstellungen für die Telefonalarmierung festlegen.

1.  Wähle **Meldedefinitionen** aus der Option **Alarmierung** im Hauptmenü.
2.  Klicke auf eine bestehende Definition oder erstelle eine neue Definition, indem du auf [SHORTCODE_17]Meldedefinition hinzufügen[SHORTCODE_18] im Schnellmenü klickst.
3.  Klicke auf eine der Registerkarten für [SHORTCODE_19]Eskalationsstufen[SHORTCODE_20].
4.  Markiere das Kontrollkästchen **Telefon** im Abschnitt **Alarmierung durch Integrationen**. Sollte dir die Telefonoption hier nicht zur Verfügung stehen, musst du die Telefonalarmierung entweder noch aktivieren oder du musst das Kontrollkästchen **Aktiv** auf der Telefonintegrationsseite (siehe [Einrichtung]([LINK_URL_11]) oben) markieren.
5.  Klicke auf [SHORTCODE_21]Speichern[SHORTCODE_22].

![Screenshot Meldedefinition Telefonintegration]([LINK_URL_12])

Das war's schon! Wenn ein Fehler für diese Definition und Eskalationsstufe einen Alarm auslöst, wird Uptrends die Telefonnummer des diensthabenden Operators nutzen und den Operator mit einer automatischen Nachricht anrufen.

## Kosten der Telefonalarmierung [ANCHOR_4]

Wenn du bereits SMS-Warnmeldungen nutzt, bist du wahrscheinlich mit den Credits für SMS vertraut. Jede Account-Stufe beinhaltet Credits. Sind diese aufgebraucht, kannst du zusätzliche Credits erwerben. Andernfalls werden dir keine Telefon- oder SMS-Warnmeldungen gesendet. Telefonalarmierungen und SMS-Warnmeldungen erfordern die gleiche Anzahl Credits. Weitere Informationen findest du auf der [Credits für SMS-/Telefonalarmierungen]([LINK_URL_13])-Seite.

[SHORTCODE_7]
**Hinweis**: KOSTENLOSES Testen der Telefonalarmierungen und SMS-Warnmeldungen. Uptrends verwendet deine Credits nicht für das Testen deiner Einstellungen.
[SHORTCODE_8]

## Was passiert, wenn das Telefon klingelt [ANCHOR_5]

Was erfährst du also bei einer Telefonalarmierung? Wenn das System eine Fehlerinformation an dich weitergibt, hörst du zum Beispiel Folgendes:

> "Hallo, dies ist Uptrends.
> Wir haben einen Fehler für das Prüfobjekt Home Page festgestellt. Der Fehler war ein HTTP-Musterabgleich und er trat vor 1 Minute auf.
> Der HTTP-Fehlercode lautet 500.
> Die Zeitbeschränkung von 12 wurde überschritten.
> Auf Wiederhören."

Dies ist nur ein Beispiel. Deine Nachricht wird sich auf deine spezielle Alarmierungssituation des jeweiligen Prüfobjekts beziehen. Sollte die Information nicht verfügbar sein, hörst du zum Beispiel Folgendes:

> "Hallo, dies ist Uptrends.
> Ein Fehler ist für eines deiner Prüfobjekte aufgetreten. Derzeit sind keine weiteren Informationen verfügbar. Bitte überprüfe den Status deiner Prüfobjekte in Uptrends.
> Auf Wiederhören."

## Problembehebung bei der Telefonalarmierung

Hast du Probleme mit Telefonalarmierungen? Wir haben einen [Leitfaden für Telefonalarmierungen]([LINK_URL_14]) erstellt.

## Hast du Fragen?

Solltest du weitere Unterstützung zur Einrichtung von Operatoren, Meldedefinitionen und Eskalationsstufen benötigen, besuche die Uptrends [Knowledge Base]([LINK_URL_15]). Wenn du dann noch nicht alle benötigten Informationen gefunden hast, stehen wir gerne zur Verfügung. Besuche die [Kontakt]([LINK_URL_16])-Seite, um Support-Telefonnummern zu finden oder ein Support-Ticket einzureichen.
