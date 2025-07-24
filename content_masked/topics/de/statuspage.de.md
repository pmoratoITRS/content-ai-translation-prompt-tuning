{
  "hero": {
    "title": "Alarmierungen in Statuspage erhalten"
  },
  "title": "Statuspage",
  "summary": "Schritte zur Einrichtung von Uptrends Warnmeldungen an Statuspage. ",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/statuspage",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Statuspage** ist das Status- und Vorfallkommunikationstool von Atlassian. Es ermöglicht dir, den Status deiner Websites und Seiten deinen Nutzern in Echtzeit mitzuteilen.
Die Integration deiner Uptrends Warnmeldungen in deine Statuspage-Umgebung ist einfach! Zum Einrichten der Integration in beiden Systemen sind diese Schritte erforderlich:

1.  Einrichten einer Komponente bei Statuspage
2.  Erzeugen eines Statuspage-API-Schlüssels
3.  Einrichten der Integration bei Uptrends
4.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Nach dem Einrichten dieser Integration und mit den richtigen Alarmierungseinstellungen wird deine Statusseite deinen Nutzern sofort den Echtzeit-Status deiner Seite oder Quelle anzeigen.

![]([LINK_URL_1])

Hier sind die detaillierten Anweisungen, wie du diese Integration einrichten kannst!

## 1. Eine Komponente bei Statuspage hinzufügen

1.  Füge in deiner Statuspage-Umgebung eine neue *Komponente* im **Components**-Menü hinzu. Gib der Komponente einen angemessenen Namen und füge eventuell eine Beschreibung hinzu. Speichere die Komponente.
2.  Öffne die neu erstellte Komponente und notiere bzw. kopiere die URL. Sie wird etwa folgendermaßen aussehen: manage.Statuspage.io/pages/{page_id}/components/{component_id}/edit. Wir benötigen später sowohl die *{page_id}* wie auch *{component_id}*, also notiere diese bitte.

[SHORTCODE_1]
**Tipp**: Es könnte empfehlenswert sein, separate Komponenten für jede Domain zu erstellen, die du mit Uptrends überwachst. Auf diese Weise kannst du besser nachverfolgen, wenn eine Domain mal nicht funktioniert sollte.
[SHORTCODE_2]

## 2. Einen Statuspage-API-Schlüssel erzeugen

1.  Klicke unten auf der Bildschirmseite auf das Nutzer-Symbol, um zur **API-Info** zu wechseln. ![]([LINK_URL_2])
2.  Hier kannst du einen neuen API-Schlüssel durch Klicken auf *Create key* erzeugen. Gib einen angemessenen Namen ein und bestätige.
3.  Der neu erstellte API-Schlüssel wird sofort angezeigt. Notiere oder kopiere den API-Schlüssel – du benötigst ihn später.

Damit ist die Einrichtung der Integration bei Statuspage beendet.

## 3. Einrichten der Integration bei Uptrends

Um eine neue Integration für Statuspage bei Uptrends hinzuzufügen, führe diese Schritte aus:

1.  Rufe [SHORTCODE_7]Alarmierung > Integrationen [SHORTCODE_8] auf.
2.  Klicke auf [SHORTCODE_9]Integration hinzufügen[SHORTCODE_10].
3.  Wähle Statuspage als Integrations-Art.
4.  Gib der Integration einen Namen.
5.  Füge API-Schlüssel, Page_Id und Component_Id von Statuspage in die entsprechenden [SHORTCODE_11]vordefinierten Variablen[SHORTCODE_12]-Felder ein.
6.  Klicke auf [SHORTCODE_13]Speichern[SHORTCODE_14], um die neuen Einstellungen zu speichern. Die Statuspage-Integration wird auf der Integrationen-Seite erscheinen.

Damit ist die Einrichtung der Integration bei Uptrends abgeschlossen. Du kannst diese Integration nun zu deinen Meldedefinitionen hinzufügen.

[SHORTCODE_3]
**Tipp**: Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
[SHORTCODE_4]

## 4. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie zu einer oder mehreren Eskalationsstufen einer Meldedefinition hinzufügen, um entsprechende Benachrichtigungen zu erhalten.

1.  Wechsle nach [SHORTCODE_15]Alarme > Meldedefinitionen[SHORTCODE_16] und öffne die Definition, zu der die Integration hinzugefügt werden soll.
2.  Jede [SHORTCODE_17]Eskalationsstufen[SHORTCODE_18]-Registerkarte verfügt über das Element **Alarmierung durch Integrationen** mit einer Liste der verfügbaren Integrationen. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]([LINK_URL_3]), wie Eskalationsstufen funktionieren.
3.  Wähle die Integration(en), die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die **benutzerdefinierte Integration** für Statuspage.
4.  Klicke auf [SHORTCODE_19]Speichern[SHORTCODE_20], um die Änderungen zu sichern.

[SHORTCODE_5]
**Tipp**: Jede einzelne Statuspage-Integration, die du erstellst, wirkt sich auf eine einzelne Statuspage-Komponente aus. Daher empfehlen wir, einzelne Komponenten auf Seiten von Statuspage mit einzelnen Integrationen und Meldedefinitionen auf Seiten von Uptrends abzustimmen.
[SHORTCODE_6]

**Und das war‘s schon!** Du hast die Integration von Statuspage eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team]([LINK_URL_4]).
