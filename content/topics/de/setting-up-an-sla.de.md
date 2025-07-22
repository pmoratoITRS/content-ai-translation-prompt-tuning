{
  "hero": {
    "title": "Eine SLA einrichten"
  },
  "title": "Eine SLA einrichten",
  "summary": "Du kannst die Einhaltung von SLAs (Service Level Agreements) mit Uptrends überwachen.",
  "url": "/support/kb/dashboards-und-berichte/sla/einrichten-einer-sla",
  "translationKey": "https://www.uptrends.com/support/kb/sla/setting-up-an-sla"
}

## SLA-Definitionen

Wenn du eine SLA-Definition erstellst, kannst du dieselben Mindestanforderungen, wie sie von deinem Anbieter festgelegt sind, konfigurieren und anhand des Dashboards **SLA Übersicht** überwachen. Du findest es im Menü unter {{< AppElement type="menuitem" >}}Dashboards > Synthetics > SLA Übersicht {{< /AppElement >}}. Wenn die Website oder der Service den Mindestanforderungen der SLA nicht entspricht, wird dies in der SLA Übersicht rot angezeigt. Weitere Informationen zum Dashboard SLA Übersicht findest du im Artikel [Mit SLA-Daten und -Berichten arbeiten]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-sla-data-and-reports" lang="de" >}}).

{{< callout >}}
**Hinweis**: Solltest du in deinem SLA Übersichts-Bericht nur Striche und Nullen statt Daten sehen, sind die Einstellungen deiner Kachel/deines Dashboards mit den Daten kollidiert und haben zu ungültigen Daten geführt. Der Knowledge-Base-Artikel [Fehlende SLA-Übersichtsdaten]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="de" >}}) bietet weitere Infos zu den möglichen Ursachen.
{{< /callout >}}

### SLA-Schwellen

Die folgenden Elemente werden als die **SLA-Schwellen** bezeichnet. Deine SLA-Definition kann nur die Verfügbarkeit, aber auch jegliche sonstigen SLA-Schwellen enthalten.

- **Fehler-Verfügbarkeitsrate** – SLA-Verfügbarkeitsergebnisse unter der Schwelle erfüllen nicht das SLA-Ziel: Sie erzeugen einen rot markierten Fehler in den SLA-Berichten. Werte über der Schwelle (aber geringer als die gewünschte Verfügbarkeitsrate) erzeugen in den SLA-Berichten Warnungen.
- **Gewünschte Verfügbarkeitsrate** – SLA-Verfügbarkeitsergebnisse mit diesem Wert (oder höher) sind gut. Sie erfüllen das SLA-Ziel. Werte zwischen dieser Schwelle und der Fehler-Verfügbarkeitsrate erzeugen in den SLA-Berichten gelb markierte Warnungen.
- **Seitenladezeit** – Die Höchstladezeit wie in der SLA vereinbart.
- **Operator-Antwortzeit** – Der Zeitraum zwischen einer Warnmeldung von Uptrends und dem Zeitpunkt, an dem ein Operator sich bei Uptrends anmeldet und den Alarm bestätigt, um anzuzeigen, dass die Situation bearbeitet wird. Eine Alarmierung kann im Dashboard **Aktuelle Alarmierungen** unter ({{< AppElement type="menuitem" >}} Alarmierung > Aktuelle Alarmierungen {{< /AppElement >}}) bestätigt werden.

 Solltest du mehr über die Berechnung der Verfügbarkeitsrate erfahren wollen, lies den Knowledge-Base-Artikel [Berechnung der Verfügbarkeit und Ausfallzeiten]({{< ref path="support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="de" >}}).

 ### SLA-Zeitplan {id="sla-schedule"}

Falls deine SLA nicht jeden Tag rund um die Uhr aktiv ist, zum Beispiel, wenn sie nur reguläre Bürozeiten berücksichtigt oder wenn du planmäßig Wartungszeiten anberaumst, kannst du einen SLA-Zeitplan einrichten. SLA-Zeitpläne erlauben dir, die Aktivzeiten für die SLA anzugeben. Jeder Ausfall, erhöhte Ladezeiten oder Fehler außerhalb dieser Zeiten werden im SLA-Bericht nicht berücksichtigt. Den SLA-Zeitplan konfigurierst du über die Registerkarte {{< AppElement type="tab" >}}Zeitplan{{< /AppElement >}}, wo du einen Zeitraumplan und die Möglichkeit zum Ausschluss von Tagen für geplante Wartungen findest.

Beachte, dass bei der Einrichtung von SLA-Zeitplänen die Uhrzeit und das Datum des Haupt-Uptrends Accounts verwendet werden. Datum und Uhrzeit eines Computers (an dem du die Bearbeitung des SLA-Zeitplans vornimmst) mit einer anderen Zeitzone werden ignoriert. Damit wird es einfacher, wenn du mit Operatoren unterschiedlicher Zeitzonen zusammenarbeitest, da die SLA-Zeitpläne nun nur auf Datum und Uhrzeit vom Uptrends Account beruhen.

- **Zeiträume** – Für jede Stunde jedes Tages der Woche kannst du bestimmen, ob diese SLA aktiv sein soll.

- **Ausgeschlossene Zeiträume** – Wenn es keine routinemäßigen Zeiten gibt, kannst du Zeiten auf Basis bestimmter Kalendertage und Uhrzeiten ausschließen.

## Eine SLA-Definition einrichten

Definieren von SLA-Bestimmungen:

1. Scrolle zu {{< AppElement type="menuitem" >}} Accounteinstellungen > SLA Definitionen{{< /AppElement >}}.
2. Klicke auf {{< AppElement type="button" >}}SLA Definition hinzufügen {{< /AppElement >}} oben rechts.
3. Gib der Definition einen beschreibenden Namen.
4. Gib die Fehler-Verfügbarkeitsrate im gelb umrandeten Feld für die Verfügbarkeit ein. Verfügbarkeitsergebnisse unter diesem Wert werden im SLA-Übersichtsbericht rot markiert.
5. Gib im Feld **Verfügbarkeit** beim grün umrandeten Kästchen den Prozentwert ein, bei dem die Verfügbarkeit für die Einhaltung der SLA bedenklich wird. Verfügbarkeitsergebnisse zwischen dieser und der Fehler-Verfügbarkeitsrate werden in den SLA-Übersichtsberichten gelb markiert.
6. (Optional) Sofern es bei deiner SLA erforderlich ist, gib die **Seitenladezeit** und/oder die **Operator Reaktionszeit** ein.
7. (Optional) Gilt deine SLA nicht durchgängig, kannst du einen Zeitplan einrichten. In dem Plan auf der Registerkarte {{< AppElement type="tab" >}}Zeitplan{{< /AppElement >}} zeigen blaue Felder, dass die SLA aktiv ist, während weiße Felder anzeigen, dass es sich um nicht aktive Zeiten handelt. Klicke auf ein Quadrat, um von einem aktiven zu einem inaktiven Zustand zu wechseln. Wenn du einen kompletten Tag oder an jedem Tag dieselbe Uhrzeit deaktivieren möchtest, klicke auf die Spalten- oder Zeilentitel, statt auf einzelne Felder.
8. (Optional) Für geplante Ausfallzeiten (abseits des Zeitplans) kannst du Ausschlüsse über die Registerkarte {{< AppElement type="tab" >}}Zeitplan{{< /AppElement >}} hinzufügen:

   1. Klicke auf {{< AppElement type="button" >}}Hinzufügen ausgeschlossener Zeiträume{{< /AppElement >}}.
   2. Gib dem Ausschließungszeitraum einen beschreibenden Namen.
   3. Wähle die Startzeit und die Endzeit in den Feldern **Von** und **Bis**.
   4. Klicke auf {{< AppElement type="button" >}}Übernehmen{{< /AppElement >}}.

9. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten links auf der Bildschirmseite.
