{
  "hero": {
    "title": "Testen von Warnmeldungen"
  },
  "title": "Testen von Warnmeldungen",
  "summary": "Warnmeldungen können eine sehr nützliche Möglichkeit sein, auf dem aktuellen Stand hinsichtlich Status und Performance von Websites zu bleiben. Achte darauf, sie zu testen.",
  "url": "[URL_BASE_TOPICS]alarme/warnmeldung-konfigurationen-testen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Warnmeldungen können eine sehr nützliche Möglichkeit sein, auf dem aktuellen Stand hinsichtlich Status und Performance von Websites, Server und Webservices zu bleiben.

Wenn beim Uptrends Monitoring ein Alarm ausgelöst wird, kann eine Warnmeldung an Operatoren oder an eine externe Anwendung gesendet werden. Die Meldung kann per Telefon (Sprachnachricht), E-Mail oder SMS oder als (benutzerdefinierte) Nachricht an eine Anwendung übermittelt werden. Wie das Senden der Meldungen erfolgt, wird in den Integrationen definiert; wann das Senden der Meldungen erfolgt, wird in den Meldedefinitionen festgelegt. Lies hierzu den Artikel [Alarmierung]([LINK_URL_1]).

Da es wichtig ist, dass die Nachrichten den Operator oder die Anwendung erreichen, solltest du testen, dass ihre Einrichtung erfolgreich war. Das Senden einer Testnachricht funktioniert für verschiedene Integrationsarten unterschiedlich. Die Schritte für jede Integrationsart werden nachfolgend beschrieben.

## Versenden einer Testnachricht per E-Mail oder SMS

[SHORTCODE_1]
**Hinweis**: Für den Zugriff auf die Account-Daten der Operatoren musst du Administrator sein.
[SHORTCODE_2]

1. Rufe im Menü [SHORTCODE_3] Accounteinstellungen > Operator und Gruppen (und Subaccounts) [SHORTCODE_4] auf.
2. Klicke auf [SHORTCODE_5] Alle Operatoren anzeigen [SHORTCODE_6].
3. Wähle aus der Liste der Operatoren den Operator, bei dem du die Übermittlung der Nachrichten testen möchtest.
4. Stelle sicher, dass die primäre E-Mail-Adresse und die Mobiltelefonnummer auf der Registerkarte [SHORTCODE_7]Allgemein[SHORTCODE_8] eingetragen sind.
5. Klicke auf [SHORTCODE_9]Test E-Mail senden[SHORTCODE_10] oder [SHORTCODE_11]Test SMS senden[SHORTCODE_12], um eine E-Mail oder eine SMS zu senden.

Der Operator sollte nach der Initiierung eines Tests eine Test-Nachricht erhalten.

Wenn du nicht Administrator bist, kannst du dennoch Testnachrichten für deinen eigenen Account senden.

1. Rufe das Nutzermenü unten im Menü auf und wähle [SHORTCODE_13] Benutzereinstellungen [SHORTCODE_14].
2. Deine eigenen Account-Daten werden angezeigt.
3. Stelle sicher, dass die primäre E-Mail-Adresse und die Mobiltelefonnummer eingetragen sind. Klicke auf [SHORTCODE_15]Test E-Mail senden[SHORTCODE_16] oder [SHORTCODE_17]Test SMS senden[SHORTCODE_18], um den Test auszuführen.

## Eine Testnachricht an ein fremdes System senden

Mehrere externe Anwendungen können Alarmierungen von der Uptrends Anwendung empfangen. Es gibt schlüsselfertige [Integrationen]([LINK_URL_2]) für viele Fremdanbieter-Systeme, die über eine Testfunktion verfügen. Um eine Testnachricht senden zu können, musst du diese Integrationen hinzufügen und konfigurieren.

Ist der Test erfolgreich, erhält die externe Anwendung eine Nachricht. Wie dies von dem System gehandhabt und wie es dem Nutzer angezeigt wird, hängt von dem jeweilig verwendeten System ab. Sendest du beispielsweise eine Testnachricht an Slack, sollte diese Testnachricht in dem von dir angegebenen Kanal angezeigt werden.

### Slack und PagerDuty

Für Slack und PagerDuty gibt es eine Standardtestfunktion in der Integration:

1.  Rufe [SHORTCODE_19]Alarmierung > Integrationen [SHORTCODE_20] auf.
2.  Wähle aus der Liste der Integrationen diejenige, die du testen möchtest.
3.  Achte darauf, dass alle erforderlichen Informationen eingegeben wurden.
4.  Klicke auf [SHORTCODE_21] Test Nachricht senden [SHORTCODE_22].

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Um diese Integrationen mit einem einfachen Test zu prüfen, verwende die Schaltfläche [SHORTCODE_23] Sende Test-Alarm [SHORTCODE_24] unten auf der Integrationsseite.

![Screenshot Integrationstest für Microsoft Teams]([LINK_URL_3])

Hast du die Integration angepasst, gibt es die Registerkarte [SHORTCODE_25] Anpassungen [SHORTCODE_26]. Dann kannst du die Funktion der Testnachricht für die benutzerdefinierte Integration wie unten beschrieben nutzen. Dabei werden die von dir hinzugefügten Anpassungen berücksichtigt.

## Das Senden einer Testnachricht für benutzerdefinierte Integrationen

Eine weitere Möglichkeit ist eine benutzerdefinierte Integration, bei der du das Senden von Nachrichten an externe Anwendungen einrichten kannst, für die Uptrends keine Standardintegration anbietet. Du definierst die Integration anhand der API des externen Anbieters. Auch diese Integrationen können daraufhin getestet werden, ob sie eine Nachricht auf die erwartete Weise senden.

1.  Rufe [SHORTCODE_27] Alarmierung > Integrationen [SHORTCODE_28] auf.
2.  Wähle aus der Liste der Integrationen die benutzerdefinierte Integration, die du testen möchtest.
3.  Achte darauf, dass alle erforderlichen Informationen eingegeben wurden.
4.  Wenn du einen einfachen Test ausführen möchtest, verwende die Schaltfläche [SHORTCODE_29] Sende Test-Alarm [SHORTCODE_30] unten auf der Integrationsseite.
5.  Wenn du das Benachrichtigen mit deinen besonderen Einstellungen (Anpassungen) testen möchtest, rufe die Registerkarte [SHORTCODE_31]Anpassungen[SHORTCODE_32] auf. Beim Einrichten der Integration solltest du hier die HTTP-Schritte bereits eingegeben haben. Du kannst Schritte für verschiedene Alarmtypen festlegen: Fehler, OK und Erinnerungen. Wenn du dich für unterschiedliche HTTP-Schritte für verschiedene (Kombinationen von) Warnmeldungstypen entschieden hast, existieren mehrere Definitionen von Schritten.
![Screenshot benutzerdefinierte Integrationsschritte für Alarmierungen]([LINK_URL_4]) 

6.  Klicke für jede HTTP-Schritte-Definition auf [SHORTCODE_33] Sende Test-Alarm [SHORTCODE_34].

Im Artikel [Benutzerdefinierte Integrationen einrichten]([LINK_URL_5]) erfährst du mehr über das Senden von Testnachrichten an benutzerdefinierte Integrationen.

## Problembehebung

Sollte deine Nachricht nicht wie erwartet ankommen, findest du hier einige allgemeine Tipps zur Problembehebung: [Alarme – Problembehebung]([LINK_URL_6]).
