{
  "hero": {
    "title": "Fehler löschen"
  },
  "title": "Fehler löschen",
  "summary": "Finde heraus, wie du unrichtige oder unerwünschte Fehler aus der Fehlerübersicht entfernst",
  "url": "/support/kb/alarme/fehler/fehler-ausnahmen",  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/clearing-errors"
}

Es ist möglich, individuelle Fehler bzw. eine Gruppe von Fehlern (sowohl nicht bestätigte wie auch bestätigte) zu löschen, die als falsch oder unerwünscht erachtet werden. Einzelne (oder eine geringe Anzahl an) Fehler können von dir selbst gelöscht werden. Wenn du sehr viele Fehler löschen möchtest, wird Uptrends dir dabei helfen. Mehr dazu findest du unter [Gleichzeitiges Löschen mehrerer Fehler]({{< ref path="#bulk-error-clearance" lang="de" >}}).

Beachte, dass das Löschen von Fehlern nicht automatisch zu einer Neuberechnung der Messwerte, die auf Fehlern basieren, wie etwa den Statistiken der Service Level Agreement ([SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="de" >}})) oder der [Public Status Page]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="de" >}}) führt. Lies bitte [Auswirkung auf Daten für SLA/öffentliche Statusseiten]({{< ref path="#effect-sla-psp-data" lang="de" >}}) zur Neuberechnung von Statistiken. Die Neuberechnung ist abhängig davon, ob du die Fehler selbst oder über eine Anfrage beim Support gelöscht hast.

{{< callout >}}
**Hinweis**: Leider ist es nicht möglich, SLA-Daten, die älter als 90 Tage sind, neu zu berechnen, da Daten nicht länger als dieser Zeitraum aufbewahrt werden.
{{< /callout >}}

## Einzelne Fehler löschen {id="clear-individual-errors"}

Um einen Fehler in deinem Account zu löschen:
1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjektprotokoll{{< /AppElement >}}.
2. Klicke auf den Fehler, den löschen möchtest. Die *Kontrolldetails* zu diesem Fehler werden angezeigt.
3. Klicke am Ende des eingeblendeten Fensters auf die Schaltfläche {{< AppElement type="editbutton" >}} Fehler löschen {{< /AppElement >}}.
4. Bestätige die Aktion mit der Schaltfläche {{< AppElement type="editbutton" >}} Löschen {{< /AppElement >}}.

Der Fehler wird in ein OK-Ergebnis umgewandelt, was sofort im Dashboard *Prüfobjektprotokoll* sichtbar ist.

Die entsprechenden Verfügbarkeitsdaten in Prozent werden ebenfalls geändert. Aufgrund des Caches kann es etwas dauern, bis die Änderungen sichtbar werden.

## Mehrere Fehler löschen {id="bulk-error-clearance"}

Manchmal muss man Fehler für einen bestimmten Zeitraum löschen (zum Beispiel mehrere Tage von Ausfällen). Statt jeden Fehler einzeln zu löschen, empfehlen wir Folgendes:

1. Sofern du die Ansicht der *Kontrolldetaills* aufgerufen hast, klicke am Ende des eingeblendeten Fensters auf die Schaltfläche {{< AppElement type="editbutton" >}} Mehrere Fehler löschen {{< /AppElement >}}. Das Formular *Anfrage zur Fehlerlöschung* wird eingeblendet.
2. Alternativ rufe {{< AppElement type="menuitem" >}} Support {{< /AppElement >}} auf und klicke auf die Option {{< AppElement type="buttonPrimary" >}}  Aufforderung zum Löschen von Fehlern {{< /AppElement >}}. Das Formular *Anfrage zur Fehlerlöschung* wird eingeblendet.
3. Gib die erforderlichen Informationen zum betroffenen Prüfobjekt bzw. zu den Prüfobjekten und zur Datenspanne ein. Füge ggf. weitere optionale Informationen zu deiner Anfrage, wie z. B. einen Statuscode, hinzu.
4. Klicke auf {{< AppElement type="buttonPrimary" >}} Senden {{< /AppElement >}}.

Wenn du die Anfrage absendest, wird automatisch ein Ticket erstellt und deine Anfrage wird bearbeitet. Dies kann etwas dauern, aber du erhältst Nachricht vom Ticket-System, sobald die Fehler gelöscht und die SLA-Daten neu berechnet wurden.

## Auswirkung auf SLAs (Service Level Agreements) und Public Status Page-Daten {id="effect-sla-psp-data"}

Das Löschen von Fehlern ändert nicht automatisch bestehende Statistiken der Service Level Agreement ([SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="de" >}})), einschließlich der [Public Status Page]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="de" >}})-Daten, die auch SLA-Daten sind.

Es ist jedoch möglich diese neu zu berechnen. Wenn du das [Löschen mehrerer Fehler]({{< ref path="#bulk-error-clearance" lang="de" >}}) durch das Support-Team beantragst, erfolgt die Neuberechnung im Rahmen dieses Prozesses. Du musst sie nicht separat beantragen.

Dies unterscheidet sich von den Fällen, in denen du die Fehler selbst gelöscht hast. Melde dich in dem Fall bitte über ein [Support-Ticket]({{< ref path="contact" lang="de" >}}) an den Support, in dem du erläuterst, was dein Anliegen ist.
