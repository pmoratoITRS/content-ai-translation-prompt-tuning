{
  "hero": {
    "title": "Meine Website ist nicht verfügbar, aber ich erhalte keine Alarmierung"
  },
  "title": "Website ist nicht verfügbar",
  "summary": "Deine Website ist ausgefallen, aber du hast keine Warnmeldung erhalten? Lies hier, was in dem Fall zu unternehmen ist.",
  "url": "[URL_BASE_TOPICS]alarme/website-ausgefallen-keine-alarmierung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Deine Website, dein Server oder dein Webservice sind ausgefallen, aber du hast keine Alarmierung oder Benachrichtigung erhalten? Was ist da los?! Es kann verschiedene Gründe geben, weshalb du keine Warnmeldung oder Benachrichtigung erhalten hast.

Bedenke, dass Alarmierungen sich auf eine komplette Prozessabfolge stützen. Zu Beginn steht ein Prüfobjekt-Check, der einen Fehler signalisieren kann. Wurde der Fehler durch einen zweiten Check bestätigt, kann er einen Alarm erzeugen, welcher das Senden einer Nachricht (wie in einer Integration definiert) auslösen kann. Mehr hierzu findest du im KB-Artikel [Alarmierungs-Übersicht]([LINK_URL_1]). Die Ursache des Problems kann also in der Alarm- oder Benachrichtigungsphase liegen.

Wenn du keine Alarmierung oder Benachrichtigung erhalten hast, aber eine erwartet hattest, siehe dir unsere nachstehenden Hinweise zur Fehlerbehebung an.

## Prüfobjekte überprüfen

- **Ist das Prüfobjekt aktiviert?**
  Wenn ein Prüfobjekt deaktiviert ist, erhältst du keine Alarmierungen, da das Monitoring aktuell nicht ausgeführt wird.
- **Sind Alarmierungen aktiviert?**
  Die beiden Aktivierungsstatus für Prüfobjekte und Alarmierungen werden im Dashboard für Prüfobjektstatus angezeigt.

  ![Screenshot Dashboard Prüfobjektstatus]([LINK_URL_2])

- **Verfügst du über Credits zur Benachrichtigung?**
  Telefonalarmierungen und SMS-Warnmeldungen erfordern Credits zur Benachrichtigung. Wenn deine Credits zur Benachrichtigung aufgebraucht sind, erhältst du keine dieser Benachrichtigungen, bis du neue Credits erworben hast. Lies den Artikel [Credit-Nutzung für Benachrichtigungen]([LINK_URL_3]), um weitere Informationen zu erhalten.
- **Ist der Fehler während eines festgelegten Wartungszeitraums des Prüfobjekts aufgetreten?**
  Alarme werden nicht gesendet, wenn sich das Prüfobjekt in einem vorkonfigurierten [Wartungszeitraum]([LINK_URL_4]) befindet. Die Einstellung findest du bei dem Prüfobjekt auf der Registerkarte [SHORTCODE_9]Wartungszeiträume [SHORTCODE_10].
- **Enthalten deine Fehlerbedingungen eine Übereinstimmungsabfrage?**
  Wenn du auf ein *Übereinstimmungsmuster* prüfst, muss der geprüfte Inhalt (oder ein Teil) genau dem genannten Wort oder der genannten Phrase entsprechen.

## Alarmierungshistorie überprüfen

Die Anwendung von Uptrends bietet ein aktives Protokoll aller Alarmierungsaktivitäten. Die Alarmierungshistorie gehört zu den wichtigsten Tools, um zu erfahren, ob Warnmeldungen ausgesendet wurden. Wurden keine Alarmierungen gesendet, startet hier die Fehlerbehebung.

Um zu sehen, ob Alarme generiert und Benachrichtigungen gesendet wurden, unternimm Folgendes:
Gehe in der Uptrends Anwendung zum Menüelement [SHORTCODE_11] Alarmierung > Alarmierungshistorie[SHORTCODE_12].
Du siehst nun ein aktives Protokoll aller gesendeten Alarmierungen mit Datum/Uhrzeit, Eskalationsstufe der Empfänger und Daten zu Erinnerungseinstellungen.

Klicke auf einen Eintrag in der Alarmierungshistorie, um detaillierte Infos zu dem speziellen Alarm zu erhalten. Das Fenster „Alarm Details“ öffnet sich mit den Registerkarten [SHORTCODE_13]Details[SHORTCODE_14] und [SHORTCODE_15]Nachrichten[SHORTCODE_16].

![Screenshot Dashboard Alarmierungshistorie mit Kontrolldetail]([LINK_URL_5])

Mehrere Situationen können vorliegen:

- **Es gibt keinen Eintrag in der Alarmierungshistorie**
  Überprüfe die Einstellungen deines Prüfobjekts, danach die Meldedefinitionen.
- **Es gibt einen Eintrag in der Alarmierungshistorie, aber es wurde keine Benachrichtigung gesendet**
  Auf der Registerkarte „Nachrichten“ wird eindeutig angezeigt, welche Benachrichtigungen gesendet wurden und an wen.
- **Es wurden keine Benachrichtigungen an deine benutzerdefinierten Integrationen gesendet**
 Überprüfe die Registerkarte „Nachrichten“, um den Fehler zu finden, der vom externen Service erhalten wurde. Im Beispiel oben hat Slack eine nicht korrekte Benachrichtigung erhalten. Der Slack-Eintrag - "Slack to Master operator" wird rot markiert und die Antwort der Slack API (einschließlich Fehlercodes und Informationen) wird bei Erweiterung des Eintrags angezeigt.

## Operator-Einstellungen überprüfen

[SHORTCODE_1]
**Hinweis**: Für den Zugriff auf die Account-Daten der Operatoren musst du Administrator sein. Wenn du nicht Administrator bist, kannst du lediglich Testnachrichten für deinen eigenen Account senden.
[SHORTCODE_2]

Rufe die Einstellungen für Operatoren über [SHORTCODE_17]Account > Operator[SHORTCODE_18] auf und wähle aus der Liste der Operatoren denjenigen, der keine Benachrichtigungen erhält.

Prüfe Folgendes:

- Ist die Telefonnummer und E-Mail-Adresse für den betreffenden Operator korrekt?
  [SHORTCODE_3]**Hinweis**: Stelle sicher, dass die jeweils richtige Länder- und Orts- bzw. Mobilvorwahl eingegeben wurden![SHORTCODE_4]
- Ist der betreffende Operator als „diensthabend“ eingesetzt?
![]([LINK_URL_6])
- Versuche, von der Seite der Operator-Einstellungen ( [SHORTCODE_19]Account > Operator[SHORTCODE_20]) eine Test-SMS zu senden, um sicherzustellen, dass dies funktioniert. Solltest du die Test-SMS nicht innerhalb von 10 Minuten erhalten, versuche es mit einer SMS-Gateway-Änderung.
  Dies kann als eine allgemeine Einstellung (gültig für alle Operatoren) in der SMS-Integration auf der Registerkarte [SHORTCODE_21]Allgemein[SHORTCODE_22] durch Wahl eines anderen *SMS-Anbieters* erfolgen.
  Oder du änderst die Einstellungen für einen einzelnen Operator in den *Telefon-Einstellungen* auf der Registerkarte [SHORTCODE_23]Allgemein[SHORTCODE_24] des Operators. Gelegentlich ist es notwendig, das Gateway für Operatoren an anderen Standorten zu modifizieren.
  Ändere das Gateway und wiederhole den Test.
  [SHORTCODE_5]**Hinweis**: Nationale Spam-Filter und Anrufschutzlisten können Benachrichtigungen per SMS und Sprachnachricht für Operatoren in China und Indien blockieren. [Mehr erfahren]([LINK_URL_7]) [SHORTCODE_6]
- Versuche, aus den Operator-Einstellungen eine Test-E-Mail zu senden, um sicherzustellen, dass dies funktioniert. [SHORTCODE_7]**Hinweis**: Siehe im Blacklist-/Spam-Ordner deines E-Mail-Servers nach, wenn du keine E-Mail-Alarmierungen erhalten hast, da sie manchmal dorthin verschoben werden. Lies auch unsere Empfehlungen für eine [Whitelist]([LINK_URL_8]) am Ende dieses Artikels.[SHORTCODE_8]

Weitere Informationen zum Senden von Testnachrichten findest du im KB-Artikel [Testen von Warnmeldungen]([LINK_URL_9]).

## Meldedefinitionen und Eskalationsstufen überprüfen

Um Warnmeldungen zu generieren, muss eine Meldedefinition eingerichtet und das Prüfobjekt muss dieser zugewiesen sein. Damit Benachrichtigungen gesendet werden, muss mindestens eine Eskalationsstufe definiert und aktiv sein.

- **Ist die Meldedefinition aktiv?**
  Die Einstellung findest du bei der Prüfobjektgruppe auf der Registerkarte [SHORTCODE_25]Allgemein[SHORTCODE_26].
- **Ist der betroffene überwachte Dienst einer Meldedefinition zugewiesen?**
  Prüfe alle deine Meldedefinitionen, um zu sehen, welche Prüfobjekte mit ihnen verknüpft sind. Verfügst du über viele Meldedefinitionen und findest die gewünschten Informationen nicht, reiche ein [Support-Ticket]([LINK_URL_10]) ein und wir helfen weiter.
- **Sind die Eskalationsstufen aktiviert?**
  Prüfe die Einstellung auf der entsprechenden Registerkarte der [SHORTCODE_27] Eskalationsstufe [SHORTCODE_28].
- **Wie ist die Generierung einer Alarmierung eingerichtet?**
  Es ist zu beachten, dass diese Einstellungen bestimmen, wie und wann Alarmierungen aufgrund von bestätigten und unbestätigten Fehlern gesendet werden.
  **Zum Beispiel**:
  Die Einstellung *Generiere eine Warnmeldung, wenn 1 oder mehr Fehler aufgetreten sind* bedeutet, dass eine Alarmierung nur gesendet wird, sofern ein Fehler bestätigt wurde. Dieser bestätigte Fehler würde im Prüfobjektprotokoll mit einem roten Balken dargestellt
  Die Einstellung *Generiere eine Warnmeldung, wenn 2 oder mehr Fehler aufgetreten sind* bedeutet, dass wir nur Alarmierungen senden, nachdem zwei Fehler hintereinander aufgetreten sind (d. h. ohne eine OK-Prüfung zwischen den beiden Fehlern).

## Prüfe deine IP-Whitelist und E-Mail-Einstellungen [ANCHOR_1]

- Deine E-Mail-Server blockieren eventuell unsere Warnmeldungen oder klassifizieren sie als Spam. Um dies zu verhindern, setze die E-Mail-IPs von Uptrends auf deine Whitelist: Sieh dir die [IP Whitelist]([LINK_URL_11]) an, um die aktuellen IP-Adressen für E-Mail zu erfahren.
- Uptrends nutzt **DKIM-Signaturen** für die E-Mail-Authentifizierung, um Spoofing und Phishing zu verhindern, indem es ausgehenden Nachrichten wie Warnmeldungs-E-Mails eine Signatur hinzufügt. Sollte der DKIM-Mechanismus aus irgendeinem Grund fehlschlagen, werden solche E-Mails als Spam eingestuft.
