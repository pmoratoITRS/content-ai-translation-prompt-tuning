{
  "hero": {
    "title": "Übersicht der Fehler"
  },
  "title": "Übersicht der Fehler",
  "summary": "Wenn bei der Ausführung eines Prüfobjekts ein Problem (wie in den Fehlerbedingungen definiert) erkannt wird, wird ein Fehler angezeigt.",
  "url": "/support/kb/alarme/fehler/ubersicht-der-fehler",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/errors-overview",
  "sectionlist": false,
  "tableofcontents": false
}

Wenn auf deiner Website oder bei deinen Services etwas nicht stimmt, wird von der Prüfung durch das Prüfobjekt ein Fehler angezeigt. Du musst definieren, was genau dies „etwas nicht stimmt“ ist, indem du die [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) für deine Prüfobjekte einrichtest.

Beachte, dass ein Fehler nicht dasselbe ist wie ein Alarm. Sieh dir diese [Alarmierungs-Übersicht]({{< ref path="support/kb/alerting/alerting-overview" lang="de" >}}) an, um besser die Unterschiede zu verstehen und in welchem Bezug sie zueinander stehen.

Fehler werden immer ein zweites Mal geprüft, um sogenannte Falsch-Positive zu vermeiden. Mehr dazu findest du im Knowledge-Base-Artikel [Nicht bestätigte und bestätigte Fehler]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="de" >}}).

Sobald ein Fehler aufgetreten ist, erscheint er im Dashboard *Fehler Übersicht*. Rufe {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Fehler Übersicht {{< /AppElement >}} auf, um das Dashboard anzuzeigen. Weitere Informationen zu dem Fehler findest du in den [Kontrolldetails]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="de" >}}) der Prüfung durch das Prüfobjekt, bei dem der Fehler ausgelöst wurde.

Abhängig vom Prüfobjekt und der Fehlersituation wird ein [Fehler-Screenshot]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="de" >}}) erfasst, der dich bei der Fehlerbehebung unterstützen kann.

Es gibt viele unterschiedliche Fehlertypen. Weitere Informationen zu Fehlern findest du auf der Seite [Fehlertypen]({{< ref path="support/kb/alerting/errors/error-types" lang="de" >}}), indem du nach dem Fehlercode oder anderen Merkmalen suchst.

Sollten Fehler gemeldet werden, von denen du denkst, dass sie nicht richtig sind oder dass sie aus der Fehler-Übersicht entfernt werden sollten, hast du die Möglichkeit, diese [Fehler zu löschen]({{< ref path="support/kb/alerting/errors/clearing-errors" lang="de" >}}).
