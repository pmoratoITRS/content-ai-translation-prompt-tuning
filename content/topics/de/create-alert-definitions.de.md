{
  "hero": {
    "title": "Erstellen von Meldedefinitionen"
  },
  "title": "Erstellen von Meldedefinitionen",
  "summary": "In diesem Artikel findest du Anweisungen, wie du Website-Verfügbarkeits- und Leistungsmeldungen definierst, sodass du nur unter erwünschten Umständen eine Warnmeldung erhältst.",
  "url": "/support/kb/alarme/meldedefinitionen-einrichten",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/create-alert-definitions"
}

Eine Meldedefinition beschreibt, wie du anhand von Eskalationsstufen eine Warnmeldung and welche Personen sendest. Bevor eine Meldedefinition (wie gewünscht) funktioniert, musst du [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) einrichten – die Regeln, die eine Alarmierung auslösen.

Eine [Eskalationsstufe]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="de" >}}) enthält eine Reihe von Parametern für die Erzeugung eines Alarms, eine Anzahl an Erinnerungen, Methoden und möglicher Empfänger.

{{< callout >}}
**Hinweis**: Eine Standard-Meldedefinition besteht bereits in deinem Uptrends Account. Du kannst ihre Regeln entweder ändern oder eine eigene Meldedefinition von Grund auf erstellen.
{{< /callout >}}

## Erstellen einer Meldedefinition

Um eine benutzerdefinierte Meldedefinition zu konfigurieren:

1. Rufe im Menü {{< AppElement type="menuitem" >}}Alarmierung > Meldedefinitionen {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="button" >}}Meldedefinition hinzufügen {{< /AppElement >}}.
3. Füge einen Namen für die Meldedefinition ein
3. Markiere das Kontrollfeld **Aktiv**, um die Alarmierung zu aktivieren.
4. Wähle die Prüfobjekte, für die die Meldedefinition gelten soll.
5. Richte die Eskalationsstufen ein. In dem Knowledge-Base-Artikel zu [Eskalationsstufen]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="de" >}}) findest du detaillierte Informationen.
6. Klicke auf die {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}-Schaltfläche.

Du hast gerade deine eigene Meldedefinition erstellt! Diese wird nun im **Dashboard Meldedefinitionen** unter {{< AppElement type="menuitem" >}} Alarmierung > Meldedefinitionen {{< /AppElement >}} angezeigt.

## Das Dashboard Meldedefinitionen

Das **Dashboard Meldedefinitionen** gibt eine Tabelle mit allen Zusammenfassungen von Meldedefinitionen an einem Ort wieder. Du kannst ganz einfach deine Meldedefinitionseinstellungen sehen und prüfen, darunter:

- **Name** – der Name deiner Meldedefinitionseinrichtung
- **Aktive Eskalationsstufen** – die Anzahl aktiver oder aktivierter Eskalationsstufen. Derzeit ist das Minimum keine Eskalationsstufe, das Maximum ist 3. Alle nicht aktiven Eskalationsstufen erzeugen keine Alarme.
- **Aktiv** – der Status der Meldedefinition. Der Eintrag lautet *Ja*, wenn die Meldedefinition aktiv ist, andernfalls *Nein*.

Alle Dashboards von Uptrends können exportiert werden, um einen größeren Einblick zu haben und später darauf zuzugreifen. Lies diesen [Artikel]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="de" >}}), um mehr über die Schritte zum Export deiner Dashboards zu erfahren.

Wenn du deine Daten im gewünschten Format heruntergeladen hast, siehst du über die oben genannten Meldedefinitionseinstellungen hinausgehende zusätzliche Details. Zusätzliche Datenspalten sind:

- **Prüfobjekte** – Prüfobjekte, die die Meldedefinition nutzen
- **Prüfobjektgruppen** – Prüfobjektgruppen, die die Meldedefinition nutzen
- **Ist die Meldedefinition aktiv** – *Yes*, wenn die Meldedefinition aktiviert wurde und aktiv ist, andernfalls *No*
- **Ist Eskalationsstufe n aktiv** – *Yes*, wenn die Eskalationsstufe aktiviert wurde und aktiv ist, andernfalls *No*
- **Operatoren für Eskalationsstufe n** – welche Operatoren sind den Eskalationsstufen zugewiesen
- **Operator Groups für Eskalationsstufe n** – welche Operatorgruppen sind den Eskalationsstufen zugewiesen
- **Integrationen für Eskalationsstufe n** – Integrationstyp oder welche Plattform die Alarme für jede Eskalationsstufe erhält. Integrationen können *Alerting by E-Mail, Alerting by SMS, Alerting by Phone* oder [benutzerdefinierte Integrationen]({{< ref path="/support/kb/alerting/integrations" lang="de" >}}) sein.

{{< callout >}}
Da Uptrends über drei Eskalationsstufen verfügt, bezieht sich das **n** auf die jeweilige Stufe der Eskalation der Alarmierung, die du in der Meldedefinition eingerichtet hast.
{{< /callout >}}