{
  "hero": {
    "title": "Übersicht über benutzerdefinierte Integrationen"
  },
  "title": "Übersicht über benutzerdefinierte Integrationen",
  "summary": "Hub mit Informationen zur Einrichtung benutzerdefinierter Integrationen",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/ubersicht-uber-benutzerdefinierte-integrationen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/custom-integrations-overview",
  "sectionlist": false
}

Stell dir vor, deinen Uptrends Account mit den betrieblichen Managementsystemen deines Unternehmens zu verknüpfen. Wenn du die Warnmeldedaten von Uptrends in deine bestehenden Managementabläufe für Ereignisse einspeist, erzeugt dies eine nahtlose Integration des externen Monitorings von Uptrends in die alltäglichen Prozesse deines Teams.

Sollten unsere [vordefinierten Integrations-Typen](/support/kb/alarme/integrationen) deine DevOps-Software nicht unterstützen, kannst du die Möglichkeit der benutzerdefinierten Integration nutzen, um selbst eine Integration zu entwickeln. Der Schlüssel einer erfolgreichen Integration liegt in dem Wissen, welche Form der Nachricht das andere System erwartet. In der Dokumentation der API des Fremdanbieters findest du, welche URL du eingeben musst und mit welchen Inhalten. Sie werden häufig als Webhook-basierte Integrationen bezeichnet, denn sie ermöglichen, dass sich beispielsweise Uptrends in das System „einhaken“ kann, indem es direkte Aufrufe erlaubt. Uptrends kann einen Aufruf bei der Integration initiieren, sobald eine relevante Warnmeldung ausgegeben wird.

Die Artikel in diesem Abschnitt behandeln das Erzeugen des richtigen Nachrichteninhalts (einschließlich der korrekten Formatierung), Erstellen unterschiedlicher Regeln für verschiedene Nachrichtentypen und wie du deine benutzerdefinierte Integration nach ihrer Einrichtung testen kannst.

## Benutzerdefinierte Integrationen einrichten

Um benutzerdefinierte Integrationen zu nutzen, führe diese Schritte aus:

1.  Füge deinem Account eine benutzerdefinierte Integrationsvorlage hinzu. Klicke hierfür auf das {{< AppElement type="button" >}}\+{{< /AppElement >}} neben *Integrationen* im Drop-down-Menü von *Alarme* in der Uptrends Anwendung.
2.  Du wirst über ein Pop-up-Fenster aufgefordert, einen Integrations-Typ einzugeben. Um eine benutzerdefinierte Integration auszuwählen, scrolle zum Ende der Liste und wähle **Uptrends Integration**.
3.  Gib die URL der API ein, zu der du eine Verbindung errichtest. Nutze dafür die *ApiUrl*-Variable unter **Vordefinierte Variablen**. Die richtige URL hierfür solltest du in der Dokumentation oder Benutzeroberfläche des externen Systems finden, mit dem du Uptrends verbindest.
4.  Gib einen angemessenen Namen für diese Integration im Feld **Integrationsname** ein.
5.  Falls erforderlich kannst du die Integration über die Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} modifizieren. Die anderen Kapitel dieses Artikels leiten dich durch den Prozess.
6.  Wenn du mit der Einrichtung fertig bist, klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die neuen Einstellungen zu sichern. Du kannst bei Bedarf die Anpassungen an der Integration später fortsetzen.

## Den richtigen Nachrichteninhalt erzeugen

Diese neue Integration wird eine vordefinierte Vorlage sein, die eine (anpassbare) JSON-formatierte Nachricht mit allen verfügbaren Alarmierungsvariablen enthält. Dieses Standardnachrichtenformat ermöglicht dir, alle verfügbaren Informationen zu jedem Alarm zu verarbeiten, aber du kannst nicht benötigte Daten entfernen, eigene Daten hinzufügen oder das Nachrichtenformat ändern. Du findest den vordefinierten Nachrichtentext unter {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}}, zusammen mit anderen Optionen, anhand derer du deine Integration weiter modifizieren kannst.

-   Um zu verstehen, welche Schritte zur Einrichtung des gewünschten Nachrichteninhalts und zum Einsatz von Variablen erforderlich sind, empfehlen wir zunächst, unseren Artikel [Den richtigen Nachrichteninhalt erzeugen](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/richtigen-nachrichteninhalt-erzeugen) zu lesen.
-   Einen vollständigen Überblick über die verfügbaren Warnmeldungsvariablen findest du in unserer Liste der [Systemvariablen für Warnmeldungen](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/warnmeldungen-systemvariablen).
-   Beachte, dass die ausgehende Nachricht korrekt formatiert sein muss. Lies hierzu unseren [Leitfaden zur Nachrichtenformatierung](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/nachrichtenformatierung), um unnötige Fehler bei der externen Anwendung zu vermeiden.

## Nachrichtentypen

Es gibt unterschiedliche Typen von Alarmierungsnachrichten. Uptrends unterscheidet zwischen **Fehler**meldungen, **Erinnerungen** und **Ok**-Benachrichtigungen. Standardmäßig werden all diese Nachrichtentypen mit der gleichen Einrichtung erstellt. Wenn du jedoch eine benutzerdefinierte Integration einrichtest oder eine bestehende Integration anpasst, kannst du unterschiedliche Aktionssets für jeden einzelnen Nachrichtentyp erstellen. Weitere Informationen findest du im Artikel über [Nachrichtentypen](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/nachrichtentypen).

## Benutzerdefinierte Integrationen testen

Sobald du eine benutzerdefinierte Integration geändert oder erstellt hast, macht es Sinn, sie zu testen, bevor sie aktiviert wird. Unser [Artikel zum Testen deiner benutzerdefinierten Integration](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/benutzerdefinierte-integrationen-testen) stellt die Möglichkeiten zum Testen der neu eingerichteten Integration vor.

## Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie **zu einer oder mehreren Eskalationsstufen hinzufügen, um entsprechende Warnmeldungen** durch die Integration zu erhalten. Um eine Integrationsdefinition einer „Eskalationsstufe“ zuzuweisen:

1.  Rufe die gewünschte Meldedefinition in Uptrends (*Alarme* > *Meldedefinitionen*) auf.
2.  Klicke auf eine bestehende Definition oder erstelle eine neue Definition, indem du auf {{< AppElement type="button" >}}Meldedefinition hinzufügen{{< /AppElement >}} oben rechts klickst.
3.  Klicke auf eine {{< AppElement type="tab" >}}Eskalationsstufen{{< /AppElement >}}-Registerkarte.
4.  Markiere die Kontrollkästchen für deine benutzerdefinierten Integrationsdefinitionen im Abschnitt **Alarmierung durch Integrationen**.
5.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, wenn du fertig bist.

**Und das war‘s schon!** Du hast eine benutzerdefinierte Integration eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team](/contact).
