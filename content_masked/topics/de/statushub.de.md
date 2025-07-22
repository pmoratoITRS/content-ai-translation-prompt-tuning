{
  "hero": {
    "title": "Zeige API- und Website-Status in Statushub"
  },
  "title": "StatusHub-Integration",
  "summary": "Kombiniere die leistungsstarken Alarmierungsmöglichkeiten von StatusHub mit deinen Einstellungen bei Uptrends – mit dieser praktischen Integration.",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/statushub",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Integration von Uptrends in dein Konto von [Statushub]([LINK_URL_1]) ermöglicht automatische Status-Updates der Services auf deiner Statushub-Statusseite. Zum Einrichten der Integration in beiden Systemen sind nur drei Schritte erforderlich:

1.  Einrichten der WebHook-Integrationen bei Statushub.
2.  Erstellen einer Integration und Angabe dieser WebHooks bei Uptrends.
3.  Erstellen von Service-Links in Uptrends, um die Prüfobjekte von Uptrends mit den Statushub-Services zu verknüpfen.

Diese Seite enthält eine detaillierte Beschreibung der Schritte, die erforderlich sind, um Uptrends in die Statushub-Statusseiten zu integrieren.

## 1. Einrichten der WebHook-Integrationen bei Statushub

1.  Zunächst bereiten wir alles auf Seiten von Statushub vor. Melde dich bei deinem Statushub-Account an und klicke das Bleistift-Symbol, um deine Statusseite zu bearbeiten.

2.  Klicke auf „Service & Integrations“ im Menü auf der linken Seite. Danach bearbeitest du jeden Service, den du mit Uptrends kontrollieren willst.

3.  Im Pop-up zur Bearbeitung eines Service findest du den Abschnitt „Enable/disable integrations“. Klicke auf die Uptrends-Schaltfläche und stelle sicher, dass sie hervorgehoben wird.

4.  Am unteren Ende des Pop-up-Fensters klickst du auf „Update Service“. Zurück im Service-Überblick siehst du, dass der Service nun eine URL in folgender Form zeigt:

    [INLINE_CODE_1]

    Wir werden diese URL später verwenden, um Uptrends mit diesem Statushub-Service zu verknüpfen.

5.  Wiederhole diesen Vorgang bei jedem Service, den du mit Uptrends kontrollieren willst.

Damit ist die Einrichtung der Integration bei Statushub beendet.

[SHORTCODE_1]
**Tipp**: In Uptrends gibt es keine Obergrenze für die Anzahl von Statushub-Services. Du kannst mit einem Link anfangen oder so viele Service-Links erstellen, wie du benötigst.
[SHORTCODE_2]

## 2. Einrichten der Integration bei Uptrends

1.  Gehe in deinem Uptrends Account zu [SHORTCODE_5] Alarmierung > Integrationen [SHORTCODE_6] im seitlichen Menü.
2.  Du kannst eine neue Statushub-Integration definieren, indem du auf die Schaltfläche **Integration hinzufügen** oben rechts klickst.
3.  Wähle Statushub als Integrations-Typ. Gib der Integration einen Namen (zum Beispiel einfach *Statushub*).
4.  Speichere die Integration.
5.  Wähle auf der nächsten Bildschirmseite (dem Integrationsüberblick) die gerade von dir gespeicherte Integration.
6.  Zurück auf der Integrationsseite von Statushub musst du Infos zu deinen Statushub-Services eingeben. Klicke auf [SHORTCODE_7]Service hinzufügen[SHORTCODE_8], um einen Service hinzuzufügen.
7.  Gib für jeden Statushub-Service den Namen und die URL des Service ein. Die Service-URL ist die WebHook-URL, die du gerade erzeugt hast, als du die Uptrends-Funktion bei Statushub aktiviert hast.
8.  Klicke schließlich auf [SHORTCODE_9]Speichern[SHORTCODE_10], um die neuen Einstellungen zu speichern. Die Statushub-Integration wird auf der Integrationen-Seite erscheinen.

## 3. Hinzufügen der Statushub-Integration zu Meldedefinitionen

Um die Integration tatsächlich zu nutzen, muss sie mit mindestens einer Meldedefinition verknüpft werden. Es müssen zudem Service-Links eingerichtet werden. Ein Service-Link ist die Verknüpfung zwischen einem Uptrends-Prüfobjekt und einem Statushub-Service. Warnmeldungen für dieses Prüfobjekt werden an den Service gesendet, mit dem du es verknüpfst.

1.  Navigiere zu einer deiner Meldedefinitionen oder erstelle eine neue unter ([SHORTCODE_11] Alarmierung > Meldedefinitionen [SHORTCODE_12]).
2.  Wähle die Eskalationsstufe, zu der du Statushub hinzufügen möchtest.
3.  Markiere das Kontrollkästchen für Statushub im Abschnitt **Alarmierung durch Integrationen**. Erfahre mit dem Knowledge-Base-Artikel [Eskalationsstufen zu Alarmen]([LINK_URL_2]), wie Eskalationsstufen funktionieren.
4.  Die Integration ist noch nicht aktiviert. Klicke auf das Kontrollkästchen, um sie bei dieser Eskalationsstufe zu aktivieren.
5.  Die Schaltfläche [SHORTCODE_13]Füge Service Link hinzu[SHORTCODE_14] erscheint. Klicke auf die Schaltfläche, um eine Verknüpfung zwischen einem Uptrends Prüfobjekt auf der linken und einem Statushub-Service auf der rechten Seite zu erstellen. Mit diesen Einstellungen hast du die genaue Kontrolle darüber, welches Prüfobjekt von Uptrends welchen Service in Statushub aktualisiert. Du kannst dieser Eskalationsstufe so viele Service-Links hinzufügen, wie du benötigst.
6.  Klicke auf [SHORTCODE_15]Speichern[SHORTCODE_16] unten links, um diese Meldedefinition zu sichern.

[SHORTCODE_3]
**Tipp**: Die meisten Einrichtungen verwenden direkte, Eins-zu-Eins-Service-Verknüpfungen zwischen Prüfobjekten und Service. Du kannst jedoch auch erweiterte Einstellungen vornehmen. Beispielsweise ist es möglich, mehrere Service-Links zu erzeugen, die ein einziges Prüfobjekt verwenden, um mehrere Services in Statushub zu aktualisieren.
[SHORTCODE_4]

## Was ist zu erwarten, wenn die Integration erfolgt ist?

Es gelten die üblichen Bedingungen für Meldedefinitionen. Wenn Uptrends einen Fehler bei einem deiner Prüfobjekte verzeichnet, werden wir eine Warnmeldung entsprechend der Einstellungen der Eskalationsstufen erzeugen. Wenn eine Eskalationsstufe eine neue Warnmeldung auslöst, wird bei den entsprechenden Services in Statushub ein neuer Vorfall erzeugt. Der Servicestatus wird auf **Service disruption** gesetzt und der neue Vorfall erhält den Status **Investigating**. Deine Statushub-Statusseite sollte sich sofort aktualisieren und diese Änderungen widerspiegeln.

Diese Situation wird unverändert bleiben, solang die Fehlersituation bei Uptrends fortbesteht. In der Zwischenzeit kannst du deine Statushub-Services nach Bedarf aktualisieren. Sobald Uptrends bemerkt, dass der Fehler behoben wurde, aktualisieren wir deinen Service auf **Service is operating normally** und den Vorfall auf **Monitoring**. Wenn du denkst, dass das Problem gelöst wurde, kannst du den Vorfall in StatusHub auf Resolved setzen. Auf diese Weise kannst du immer steuern, was auf deiner Statusseite angezeigt wird.

Hast du Fragen zur Erstellung der richtigen Einrichtung? [Wende dich bitte an unser Support-Team]([LINK_URL_3]).
