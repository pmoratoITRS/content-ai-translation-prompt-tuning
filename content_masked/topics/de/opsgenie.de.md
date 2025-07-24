{
  "hero": {
    "title": "Alarmierungen in Opsgenie erhalten"
  },
  "title": "Opsgenie",
  "summary": "Schritte zur Einrichtung von Uptrends Warnmeldungen an Opsgenie",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/opsgenie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Opsgenie** ist die Plattform für Alarmierungen und Vorfallsmanagement von Atlassian. Sie ermöglicht dir, Warnmeldungen und Benachrichtigungen von externen Systemen (wie Uptrends) zu sammeln und zu priorisieren sowie ihnen Maßnahmen zuzuordnen.
Die Integration deiner Uptrends Warnmeldungen in deine Opsgenie-Umgebung ist einfach! Zum Einrichten der Integration in beiden Systemen sind diese Schritte erforderlich:

1.  Einrichten einer API-Integration bei Opsgenie
2.  Einrichten der Integration bei Uptrends
3.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Nach dem Einrichten dieser Integration und mit den richtigen Alarmierungseinstellungen wird dein Uptrends Alarmierungssystem auch bei Opsgenie Warnmeldungen generieren. Unten siehst du ein Beispiel, wie eine solche Warnmeldung bei Opsgenie aussieht.

![]([LINK_URL_1])

Die Opsgenie-Alarmierung wird für das Team generiert, für das du die Integration eingerichtet hast. Wenn du möchtest, dass Warnmeldungen an mehrere Teams gesendet werden, kannst du eine Integration für jedes Team einrichten.

Hier sind die detaillierten Anweisungen, wie du diese Integration einrichten kannst!

## 1. Einrichten der Integration bei Opsgenie

1.  Richte in deiner Opsgenie-Umgebung ein neues Team ein oder verwende ein bestehendes.
2.  Rufe im Bereich der Optionen für dieses Team *Integrationen* auf.
3.  Suche die bereits bestehende *API*-Integration (sie sollte *{teamname}_API}* heißen). Wenn diese Integration noch nicht existiert, kannst du eine neue erstellen, indem du auf **Add integration** klickst und den Integrationstyp ‚API‘ auswählst. Öffne diese Integration und notiere oder kopiere den API-Schlüssel – du benötigst ihn später.
4.  Speichere die Integration.

Damit ist die Einrichtung der Integration bei Opsgenie abgeschlossen.

## 2. Einrichten der Integration bei Uptrends

Um eine neue Integration für Opsgenie bei Uptrends hinzuzufügen, führe diese Schritte aus:

1.  Rufe [SHORTCODE_3]Alarmierung > Integrationen [SHORTCODE_4] auf.
2.  Klicke auf [SHORTCODE_5]Integration hinzufügen[SHORTCODE_6].
3.  Wähle Opsgenie als Integrations-Art.
4.  Gib der Integration einen Namen.
5.  Füge den zuvor notierten/kopierten API-Schlüssel von Opsgenie in [SHORTCODE_7]Vordefinierte Variablen > ApiKey[SHORTCODE_8] ein.
6.  Klicke auf [SHORTCODE_9]Speichern[SHORTCODE_10], um die neuen Einstellungen zu speichern. Die Opsgenie-Integration wird auf der Integrationen-Seite erscheinen.

Standardmäßig wird die Opsgenie-Integration die internationale Opsgenie-Instanz mit [INLINE_CODE_1] als Anfrage-URL nutzen. Solltest du die EU-Instanz von Opsgenie verwenden, dann sollte die Anfrage-URL [INLINE_CODE_2] lauten. Um dies zu ändern:

1. Aktiviere in den Opsgenie-Integrationseinstellungen **Integration anpassen**.
2. Klicke auf die [SHORTCODE_11]Anpassungen[SHORTCODE_12]-Registerkarte, die nun zu sehen ist.
3. Ändere unter **Method und URL** die Anfrage-URL auf [INLINE_CODE_3], um die EU-Instanz der Opsgenie API zu verwenden.
![Opsgenie URL EU-Instanz]([LINK_URL_2])
4. Sende eine Testmeldung, um sicherzustellen, dass du die richtige Instanz nutzt. Klicke hierzu auf [SHORTCODE_13]Sende Test-Alarm[SHORTCODE_14].
5. Speichere die Integration.

Damit ist die Einrichtung der Integration bei Uptrends abgeschlossen. Du kannst diese Integration nun zu deinen Meldedefinitionen hinzufügen.

[SHORTCODE_1]
**Tipp**: Wenn du eine Integrationsdefinition deaktivierst, wird diese Integration nicht mehr für Warnmeldungen verwendet. Dies kann nützlich sein, wenn du beispielsweise temporär keine Warnmeldungen erhalten möchtest.
[SHORTCODE_2]

## 3. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie zu einer oder mehreren Eskalationsstufen einer Meldedefinition hinzufügen, um entsprechende Benachrichtigungen zu erhalten.

1.  Wechsle nach [SHORTCODE_15]Alarme > Meldedefinitionen[SHORTCODE_16] und öffne die Definition, zu der die Integration hinzugefügt werden soll.
2.  Jede [SHORTCODE_17]Eskalationsstufen[SHORTCODE_18]-Registerkarte verfügt über das Element **Alarmierung durch Integrationen** mit einer Liste der verfügbaren Integrationen. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]([LINK_URL_3]), wie Eskalationsstufen funktionieren.
3.  Wähle die Integration(en), die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die **benutzerdefinierte Integration** für Opsgenie.
4.  Klicke auf [SHORTCODE_19]Speichern[SHORTCODE_20], um die Änderungen zu sichern.

**Und das war‘s schon!** Du hast die Integration bei Opsgenie eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team]([LINK_URL_4]).
