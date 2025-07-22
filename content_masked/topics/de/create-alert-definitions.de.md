{
  "hero": {
    "title": "Erstellen von Meldedefinitionen"
  },
  "title": "Erstellen von Meldedefinitionen",
  "summary": "In diesem Artikel findest du Anweisungen, wie du Website-Verfügbarkeits- und Leistungsmeldungen definierst, sodass du nur unter erwünschten Umständen eine Warnmeldung erhältst.",
  "url": "[URL_BASE_TOPICS]alarme/meldedefinitionen-einrichten",
  "translationKey": "[URL_1]
}

Eine Meldedefinition beschreibt, wie du anhand von Eskalationsstufen eine Warnmeldung and welche Personen sendest. Bevor eine Meldedefinition (wie gewünscht) funktioniert, musst du [Fehlerbedingungen]([LINK_URL_1]) einrichten – die Regeln, die eine Alarmierung auslösen.

Eine [Eskalationsstufe]([LINK_URL_2]) enthält eine Reihe von Parametern für die Erzeugung eines Alarms, eine Anzahl an Erinnerungen, Methoden und möglicher Empfänger.

[SHORTCODE_1]
**Hinweis**: Eine Standard-Meldedefinition besteht bereits in deinem Uptrends Account. Du kannst ihre Regeln entweder ändern oder eine eigene Meldedefinition von Grund auf erstellen.
[SHORTCODE_2]

## Erstellen einer Meldedefinition

Um eine benutzerdefinierte Meldedefinition zu konfigurieren:

1. Rufe im Menü [SHORTCODE_5]Alarmierung > Meldedefinitionen [SHORTCODE_6] auf.
2. Klicke auf [SHORTCODE_7]Meldedefinition hinzufügen [SHORTCODE_8].
3. Füge einen Namen für die Meldedefinition ein
3. Markiere das Kontrollfeld **Aktiv**, um die Alarmierung zu aktivieren.
4. Wähle die Prüfobjekte, für die die Meldedefinition gelten soll.
5. Richte die Eskalationsstufen ein. In dem Knowledge-Base-Artikel zu [Eskalationsstufen]([LINK_URL_3]) findest du detaillierte Informationen.
6. Klicke auf die [SHORTCODE_9] Speichern [SHORTCODE_10]-Schaltfläche.

Du hast gerade deine eigene Meldedefinition erstellt! Diese wird nun im **Dashboard Meldedefinitionen** unter [SHORTCODE_11] Alarmierung > Meldedefinitionen [SHORTCODE_12] angezeigt.

## Das Dashboard Meldedefinitionen

Das **Dashboard Meldedefinitionen** gibt eine Tabelle mit allen Zusammenfassungen von Meldedefinitionen an einem Ort wieder. Du kannst ganz einfach deine Meldedefinitionseinstellungen sehen und prüfen, darunter:

- **Name** – der Name deiner Meldedefinitionseinrichtung
- **Aktive Eskalationsstufen** – die Anzahl aktiver oder aktivierter Eskalationsstufen. Derzeit ist das Minimum keine Eskalationsstufe, das Maximum ist 3. Alle nicht aktiven Eskalationsstufen erzeugen keine Alarme.
- **Aktiv** – der Status der Meldedefinition. Der Eintrag lautet *Ja*, wenn die Meldedefinition aktiv ist, andernfalls *Nein*.

Alle Dashboards von Uptrends können exportiert werden, um einen größeren Einblick zu haben und später darauf zuzugreifen. Lies diesen [Artikel]([LINK_URL_4]), um mehr über die Schritte zum Export deiner Dashboards zu erfahren.

Wenn du deine Daten im gewünschten Format heruntergeladen hast, siehst du über die oben genannten Meldedefinitionseinstellungen hinausgehende zusätzliche Details. Zusätzliche Datenspalten sind:

- **Prüfobjekte** – Prüfobjekte, die die Meldedefinition nutzen
- **Prüfobjektgruppen** – Prüfobjektgruppen, die die Meldedefinition nutzen
- **Ist die Meldedefinition aktiv** – *Yes*, wenn die Meldedefinition aktiviert wurde und aktiv ist, andernfalls *No*
- **Ist Eskalationsstufe n aktiv** – *Yes*, wenn die Eskalationsstufe aktiviert wurde und aktiv ist, andernfalls *No*
- **Operatoren für Eskalationsstufe n** – welche Operatoren sind den Eskalationsstufen zugewiesen
- **Operator Groups für Eskalationsstufe n** – welche Operatorgruppen sind den Eskalationsstufen zugewiesen
- **Integrationen für Eskalationsstufe n** – Integrationstyp oder welche Plattform die Alarme für jede Eskalationsstufe erhält. Integrationen können *Alerting by E-Mail, Alerting by SMS, Alerting by Phone* oder [benutzerdefinierte Integrationen]([LINK_URL_5]) sein.

[SHORTCODE_3]
Da Uptrends über drei Eskalationsstufen verfügt, bezieht sich das **n** auf die jeweilige Stufe der Eskalation der Alarmierung, die du in der Meldedefinition eingerichtet hast.
[SHORTCODE_4]