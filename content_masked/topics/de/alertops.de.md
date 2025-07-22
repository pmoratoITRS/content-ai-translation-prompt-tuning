{
  "hero": {
    "title": "Alarmierungen in AlertOps erhalten"
  },
  "title": "AlertOps",
  "summary": "Einrichtungsleitfaden für die AlertOps-Integration",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/alertops",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**AlertOps** ist ein Tool für die Echtzeit-Betriebsautomatisierung. Es ermöglicht dir, Ereignisse zu priorisieren sowie deine Prozesse zu automatisieren. Große Vorfälle lassen sich einfach handhaben, wenn Bereitschaftsteams mobilisiert werden und zusätzliche Informationen zur Bewältigung erhalten.

1.  Einrichten der eingehenden Integration bei AlertOps
2.  Einrichten der Integration bei Uptrends
3.  Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Nach dem Einrichten dieser Integration und mit den richtigen Alarmierungseinstellungen wird dein Uptrends Alarmierungssystem auch bei AlertOps Warnmeldungen generieren. Unten siehst du ein Beispiel, wie eine solche Warnmeldung bei AlertOps aussieht.

![]([LINK_URL_1])

Hier sind die detaillierten Anweisungen, wie du diese Integration einrichten kannst!

## 1. Einrichten einer eingehenden Integration bei AlertOps

1.  Navigiere in der Benutzeroberfläche von AlertOps zum Menüpunkt *Inbound Integrations* (unter *Integrations* im seitlichen Menü).
2.  Stelle sicher, dass die Registerkarte **API** angezeigt wird und klicke auf *ADD API INTEGRATION*.
3.  Klicke auf der nächsten Bildschirmseite auf *Uptrends*, um die Standardintegration von Uptrends auszuwählen.
4.  Gib der Integration einen angemessenen Namen und wähle die entsprechenden **Recipient Group(s)/User(s)**.

   ![]([LINK_URL_2])
   
5.  Klicke auf die *Speichern*-Schaltfläche.
6.  Kopiere die **API URL**, die nun in der AlertOps-Benutzeroberfläche aufgelistet wird. Du benötigst sie, wenn du die Integration bei Uptrends einrichtest.

Damit ist die Einrichtung der Integration bei AlertOps beendet.

[SHORTCODE_1]
**Hinweis**: AlertOps bietet eine vordefinierte Uptrends Integration, die direkt funktionsbereit sein sollte. Diese Integration lässt sich auf Seiten von AlertOps weitgehend anpassen. Wir empfehlen jedoch, während der Einrichtung die erweiterten Einstellungsmöglichkeiten nicht zu ändern. Sobald du bestätigt hast, dass die Integration funktioniert, kannst du sie nach deinen Anforderungen anpassen.
[SHORTCODE_2]

## 2. Einrichten der Integration bei Uptrends

Um eine neue Integration für AlertOps bei Uptrends hinzuzufügen, führe diese Schritte aus:

1.  Rufe [SHORTCODE_3]Alarmierung > Integrationen [SHORTCODE_4] auf.
2.  Klicke auf [SHORTCODE_5]Integration hinzufügen[SHORTCODE_6].
3.  Wähle AlertOps als Integrations-Art.
4.  Gib der Integration einen Namen.
5.  Füge die zuvor kopierte AlertOps **API-URL** in das entsprechende Feld unter [SHORTCODE_7]Vordefinierte Variablen[SHORTCODE_8] ein.
6.  Klicke auf [SHORTCODE_9]Speichern[SHORTCODE_10], um die neuen Einstellungen zu sichern. Die AlertOps-Integration wird auf der Integrationen-Seite erscheinen.

Damit ist die Einrichtung der Integration bei Uptrends abgeschlossen. Du kannst diese Integration nun zu deinen Meldedefinitionen hinzufügen.

## 3. Hinzufügen der Integration zu einer Meldedefinition bei Uptrends

Eine Integrationsdefinition an sich bewirkt erst einmal nichts. Du musst sie zu einer oder mehreren Eskalationsstufen einer Meldedefinition hinzufügen, um entsprechende Benachrichtigungen zu erhalten.

1.  Wechsle nach [SHORTCODE_11]Alarme > Meldedefinitionen[SHORTCODE_12] und öffne die Definition, zu der die Integration hinzugefügt werden soll.
2.  Jede [SHORTCODE_13]Eskalationsstufen[SHORTCODE_14]-Registerkarte verfügt über das Element **Alarmierung durch Integrationen** mit einer Liste der verfügbaren Integrationen. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]([LINK_URL_3]), wie Eskalationsstufen funktionieren.
3.  Wähle die Integration(en), die du mit der Eskalationsstufe verknüpfen möchtest. In diesem Fall die **benutzerdefinierte Integration** für AlertOps.
4.  Klicke auf [SHORTCODE_15]Speichern[SHORTCODE_16], um die Änderungen zu sichern.

**Und das war‘s schon!** Du hast die Integration für AlertOps eingerichtet.

Wie immer gilt: Wenn du Fragen hast, [wende dich bitte an unser Support-Team]([LINK_URL_4]).
