{
  "hero": {
    "title": "Fehlerbedingungen – Ladezeit/Laufzeit"
  },
  "title": "Fehlerbedingungen – Ladezeit/Laufzeit",
  "summary": "Definieren von Lade- oder Laufzeit-Limits und ihre Auswirkung auf die Alarmierung",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/ladezeit-limit-einstellungen-alarme-und-warnungen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/load-time-limit-settings-alerts-and-warnings"
}

Bei der Einrichtung deiner Prüfobjekte hast du die Option, Limits für die Lade- oder Laufzeit anzugeben. Du kannst zwei Schwellenwerte eingeben: einen unteren Wert, bei dem die Dauer bedenklich wird, und einen höheren Wert, bei dem die Dauer kritisch ist.

Das Laufzeit-Limit wird bei Transaktionsprüfobjekten und Prüfobjekten, die nicht HTTP(S)- oder browserbasiert sind wie DNS-, Ping- oder Mailserver-Prüfobjekte, angewendet.

Die Ladezeit wird bei den Prüfobjekten HTTP(S), Webservices HTTP(S) und Full Pagecheck verwendet. Dabei wird die Zeit betrachtet, die benötigt wird, eine Prüfung ab erster Anfrage vollständig auszuführen.

{{< callout >}}
**Hinweis**: Bei Uptrends basiert die Seitenladezeit auf der Dauer, die benötigt wird, eine Prüfung ab erster Anfrage vollständig auszuführen. Diese Zeit unterscheidet sich je nach Typ des Prüfobjekts. Für dieselbe URL unterscheidet sich die Seitenladezeit eines einfachen Tests erheblich von der Seitenladezeit eines Real Browser Checks. Erfahre mehr über die [Unterschiede zwischen einem einfachen und einem Real Browser Check]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="de" >}}).
{{< /callout >}}

Während andere [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) immer einen Fehler generieren, wenn die Bedingung nicht erfüllt ist, kann die Seitenladezeit so eingerichtet werden, dass sie einen Fehler erzeugt oder die Situation einfach nur farblich im Dashboard *Prüfobjektstatus* markiert. Beachte, dass du mit dieser Fehlerbedingung Fehler generieren musst, solltest du die [Alarmierungsfunktion]({{< ref path="support/kb/alerting" lang="de" >}}) nutzen wollen.

## Eine Prüfung für die gesamte Laufzeit hinzufügen

Um eine Prüfung für die gesamte Laufzeit hinzuzufügen:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf den Prüfobjektnamen, um ihn zu bearbeiten.
3. Öffne die Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} und erweitere den Abschnitt **Prüfe komplette Laufzeit**.
![screenshot error condition for running times](/img/content/scr_errorconditions-running-times.min.png)
4. Wähle, ob du nur eine Farbcodierung (Dashboard *Prüfobjektstatus*) oder die Erzeugung eines Fehlers bewirken möchtest.
5. Gib die Werte (in Millisekunden) für den unteren (bedenklich) und den oberen (kritisch) Laufzeit-Schwellenwert ein.
6. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

Beim Transaktionsprüfobjekt ist die gesamte Laufzeit die Dauer, die benötigt wird, eine Transaktion vollständig auszuführen.

## Eine Prüfung für Ladezeiten hinzufügen

Um eine Prüfung für Ladezeiten hinzuzufügen:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf den Prüfobjektnamen, um ihn zu bearbeiten.
3. Öffne die Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}} und erweitere den Abschnitt **Prüfe Seitenladezeit**.
![screenshot error condition for page load times](/img/content/scr_errorconditions-load-times.min.png)
4. Wähle, ob du nur eine Farbcodierung (Dashboard *Prüfobjektstatus*) oder die Erzeugung eines Fehlers bewirken möchtest.
5. Gib die Werte (in Millisekunden) für die unteren (bedenklich) und oberen (kritisch) Ladezeit-Schwellenwerte ein.
6. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

## Nur Farb-Code

Wenn du dich für die Option *Nur Farb-Code* für eine oder beide Schwellenwerte entschieden hast, zeigt das Dashboard *Prüfobjektstatus* an, dass die Schwellenwerte erreicht wurden. Wenn der untere Schwellenwert (bedenklich) überschritten wird, erscheint der Wert mit gelbem Hintergrund in der Spalte **Gesamtzeit**. Wurde der höhere Wert (kritisch) überschritten, wird die Zeit mit einem roten Hintergrund hervorgehoben. Du kannst das Dashboard *Prüfobjektstatus* über das Menü {{< AppElement type="menuitem" >}} Überwachung > Prüfobjektstatus {{< /AppElement >}} öffnen.

![Screenshot Dashboard Prüfobjektstatus mit Farbcodes](/img/content/scr_errorconditions-colorcode-loadtime.min.png)

Du wirst bemerken, dass das Dashboard *Prüfobjektstatus* oben zwei Prüfobjekte mit Gesamtzeiten in gelb und rot zeigt, aber der Fehlerindikator links immer noch grün (für erfolgreich ausgeführte Tests) ist. Dies ist das Ergebnis der Option *Nur Farb-Code*.

## Erzeuge einen Fehler {id="generate-error"}

Möchtest du auf Basis der Seitenlade- oder Laufzeit Alarme generieren, verwende bei der Fehlerbedingung die Option **Erzeuge einen Fehler**. Nur wenn Fehler erzeugt werden, kann in der Folge eine Alarmierung ausgelöst werden. Der Knowledge-Base-Artikel [Alarmierung – Überblick]({{< ref path="support/kb/alerting/alerting-overview" lang="de" >}}) erläutert ausführlich, wie die Abfolge von Prüfungen und Alarmierungen funktionert.

Wenn du die Option *Erzeuge einen Fehler* wählst, erhältst du im Dashboard *Prüfobjektstatus* weiterhin die Lade- oder Laufzeiten farbcodiert.
