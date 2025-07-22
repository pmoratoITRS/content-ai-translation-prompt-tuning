{
  "hero": {
    "title": "Uptrends in Zapier integrieren"
  }, 
  "title": "Zapier",
  "summary": "Leitfaden zur Integration von Uptrends' Alarmierungen in Zapier",
  "url": "/support/kb/alarme/integrationen/zapier",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/zapier" 
}

**Zapier** ist ein Online-Automatisierungstool, das deine Apps und Services miteinander verbindet. Es ermöglicht, dein Uptrends Warnmeldesystem mit praktisch jeder anderen Anwendung zu verknüpfen. Mit diesem Leitfaden helfen wir dir bei der Einrichtung der Uptrends-Integration für Zapier, und du erfährst, was du als Nächstes mit den Daten machen kannst.

1.  Einrichten einer *When this happens…*-Aktion in Zapier
2.  Einrichten der Integration bei Uptrends
3.  Testen des Webhooks in Zapier
4.  Einrichten einer *Do this…*-Aktion in Zapier
5.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Hier sind die detaillierten Anweisungen, wie du diese Integration einrichten kannst!

## 1. Einrichten einer When this happens…-Aktion in Zapier

1.  Zapier nennt seine automatisierten Arbeitsabläufe *Zaps*. Wechsle zu *Zaps* und klicke auf *Create Zap.* Alternativ kannst du auf die Schaltfläche *MAKE A ZAP* oben links am Bildschirm klicken.
2.  Gib deinem neuen Zap einen angemessenen Namen.
3.  Wähle *Webhooks by Zapier*.
4.  Wähle *Catch hook* und klicke auf *Continue*.
5.  Kopiere die **Custom Webhook URL**, da du sie später zur Einrichtung der Integration bei Uptrends benötigst.
6.  Klicke auf *Continue*.

Nun wird Zapier dich auffordern, den Webhook zu testen, indem du ihm Daten sendest. Dafür musst du zunächst die Integration bei Uptrends einrichten.

## 2. Einrichten der Integration bei Uptrends

1.  Rufe {{< AppElement type="menuitem" >}}Alarmierung > Integrationen {{< /AppElement >}} auf.
2.  Klicke auf {{< AppElement type="button" >}}Integration hinzufügen{{< /AppElement >}}.
3.  Wähle Zapier als Integrations-Typ.
4.  Gib der Integration einen Namen.
5.  Füge die zuvor kopierte **Custom Webhook URL** in das entsprechende Feld unter {{< AppElement type="menuitem" >}}Vordefinierte Variablen{{< /AppElement >}} ein.
6.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die neuen Einstellungen zu speichern. Die Zapier-Integration wird auf der Integrationen-Seite erscheinen.

## 3. Testen des Webhooks in Zapier

1.  Rufe die neu erstellte **Zapier**-Integration bei Uptrends auf.
2.  Klicke auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} auf die Schaltfläche {{< AppElement type="button" >}}Sende Test-Alarm{{< /AppElement >}}.
3.  Klicke auf {{< AppElement type="button" >}}Test starten{{< /AppElement >}}, um einen Testalarm an den Zapier-Webhook zu senden. Es ist unerheblich, welche *Alarmierungsart* du auswählst.
4.  Klicke in der Zapier-Anwendung auf die Schaltfläche *Test trigger*. Zapier wird daraufhin auf die von uns im vorherigen Schritt gesendeten Daten reagieren und den JSON-Inhalt parsen. Wir werden uns die einzelnen Felder später in der ausgehenden Nachricht ansehen.![](/img/content/5386ad32-943e-41ff-9533-abcb03c30fc5.png)
5.  Klicke in Zapier auf die Schaltfläche *Continue*.

## 4. Einrichten einer Do this…-Aktion in Zapier

### Beispiel 1: E-Mail-Integration über Zapier

Richten wir zunächst als Beispiel eine einfache E-Mail-Integration über Zapier ein.

1.  Finde bei Zapier die integrierte App *Email by Zapier* und wähle sie aus.
2.  Klicke auf *Continue*.
3.  Gib deine E-Mail-Adresse in das **To**-Feld ein.
4.  Die Felder **Subject** und **Body** können mit den von Uptrends eingehenden Daten benutzerdefiniert ausgefüllt werden. Da Zapier bei Schritt 3 einen Testalarm erhalten und geparst hat, kennt es bereits die Daten, die in eingehenden Uptrends Alarmen enthalten sind. Wenn du in eins der Felder klickst, erscheint eine Liste mit der Bezeichnung **Insert data**, aus der du Verweise zu Werten auswählen kannst, die mit einer Uptrends Meldung gesendet werden. Wenn Zapier die ausgehende Nachricht sendet, werden die Felder automatisch mit den richtigen Werten ausgefüllt.![](/img/content/af300fe7-01dd-4e58-b2fe-afa99b1125ff.png)
5.  Nachdem du die ausgehende Nachricht angepasst hast, klicke auf *Continue*.
6.  Bei Bedarf kannst du die ausgehende Nachricht auf dieser Seite testen. Du solltest sofort eine E-Mail mit fiktiven Daten erhalten.![](/img/content/8a4e2e5e-2288-4a6d-91c4-d9f64c54b6f0.png)
7.  Schließe die Einrichtung der Integration bei Zapier ab, indem du auf **TURN ON ZAP** klickst.

### Beispiel 2: Trello-Integration über Zapier

Deine Zapier-Integration kann noch so viel mehr. Richten wir als zweites Beispiel die Integration bei Trello ein. Dafür benötigst du einen Trello-Account, der mit Zapier verbunden ist. Die Möglichkeit dazu findest du unter *My Apps* im Seitenleistenmenü von Zapier.

1.  Füge ein neues Zap hinzu, indem du die gleichen Schritte wie in Abschnitt 1 (*Einrichten einer When this happens…-Aktion in Zapier*) dieses Leitfadens ausführst.
2.  Du erhältst eine neue **Custom Webhook URL**. Füge diese neue Webhook-URL dann zu einer eigenen Integration bei Uptrends hinzu. Folge den Aktionen in Schritt 2, um eine neue Integration bei Uptrends einzurichten und verwende diese neue Webhook-URL.
3.  Wiederhole die Aktionen von Schritt 3, um Testdaten zu diesem neuen Webhook zu senden, sodass Zapier die eingehenden Daten parsen kann. Kurz gesagt: Klicke auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} auf die Schaltfläche {{< AppElement type="button" >}}Sende Test-Alarm{{< /AppElement >}}. Klicke bei Zapier auf die Schaltfläche *Test trigger*. Klicke abschließend auf *CONTINUE*.
4.  Um die Integration mit Trello einzurichten, wähle *Trello* unter **Your Apps** aus.
5.  Wähle dann die Aktion aus, die bei Trello ausgeführt werden soll, wenn eine Uptrends Meldung gesendet wird. Für dieses Beispiel wählen wir *Create Card*. Klicke auf der folgenden Seite auf *CONTINUE*.
6.  Wähle den verknüpften Trello-Account und klicke auf *CONTINUE*.
7.  Wähle **Board** und **List**. Gib die **Beschreibung** für die zu erstellende Karte ein. Auch hier kannst du den Inhalt komplett anpassen und die Alarmierungsdaten von Uptrends, die zuvor von Zapier geparst wurden, nutzen. Aktiviere nach Bedarf alle weiteren Optionen und klicke abschließend auf *CONTINUE*.![](/img/content/52217609-6954-4819-8bc1-9195a448ff72.png)
8.  Bei Bedarf kannst du die ausgehende Nachricht auf dieser Seite testen.![](/img/content/4cea7e0f-e577-4250-aec5-ab31d000935d.png)
9.  Schließe die Einrichtung der Integration bei Zapier ab, indem du auf **TURN ON ZAP** klickst.

{{< callout >}}
**Tipp**: Dies sind lediglich zwei Beispiele. Zapier ermöglicht dir, deine Uptrends Meldungen an praktisch jede externe Plattform zu senden.
{{< /callout >}}

## 5. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie zu einer oder mehreren Eskalationsstufen einer Meldedefinition hinzufügen, um entsprechende Benachrichtigungen zu erhalten.

1.  Wechsle nach {{< AppElement type="menuitem" >}}Alarme > Meldedefinitionen{{< /AppElement >}} und öffne die Definition, zu der die Integration hinzugefügt werden soll.
2.  Jede {{< AppElement type="tab" >}}Eskalationsstufen{{< /AppElement >}}-Registerkarte verfügt über das Element **Alarmierung durch Integrationen** mit einer Liste der verfügbaren Integrationen. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="de" >}}), wie Eskalationsstufen funktionieren.
3.  Wähle die Integration(en), die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die **benutzerdefinierte Integration** für Zapier.
4.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die Änderungen zu sichern.

**Und das war‘s schon!** Du hast die Integration bei Zapier eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team](/contact).
