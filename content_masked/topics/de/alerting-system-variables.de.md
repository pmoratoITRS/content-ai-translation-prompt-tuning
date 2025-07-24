{
  "hero": {
    "title": "Variablen für das Alarmierungssystem"
  },
  "title": "Variablen für das Alarmierungssystem",
  "summary": "Eine Übersicht verfügbarer Systemvariablen, die bei (benutzerdefinierten) Integrationen eingesetzt werden können",
  "url": "[URL_BASE_TOPICS]alarme/integrationen/benutzerdefinierte-integrationen/warnmeldungen-systemvariablen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Dieser Artikel enthält einen Überblick über alle verfügbaren **Systemvariablen**, die zur Eingabe relevanter Informationen – beispielsweise, welches Prüfobjekt sie ausgelöst hat, welcher Fehler aufgetreten ist oder den Alarm selbst – in eine ausgehende Warnmeldung verwendet werden können. Weitere Informationen, wie du diese Systemvariablen nutzen kannst findest du in unserem Artikel [Den richtigen Nachrichteninhalt erzeugen]([LINK_URL_1]).

Hinweis: Um die hier aufgeführten Variablen zu nutzen, müssen sie in doppelten geschwungenen Klammern in den Nachrichteninhalt eingefügt werden. Beispiel: [INLINE_CODE_1].

|  Variable   | Beschreibung    |  Beispielwert   |
| --- | --- | --- |
| [INLINE_CODE_2] | Deine Uptrends Account-ID. | [INLINE_CODE_3] |
| [INLINE_CODE_4] | Einzigartige ID dieses Alarms. | [INLINE_CODE_5] |
| [INLINE_CODE_6] | Enthält den Checkpoint-Namen oder Standort, wo der Alarm zuletzt überprüft wurde. | [INLINE_CODE_7] |
| [INLINE_CODE_8] | Textbeschreibung des Fehlers, der die Warnmeldung ausgelöst hat. Enthält gegebenenfalls die Schrittnummer. | [INLINE_CODE_9] |
| [INLINE_CODE_10] | Die Zeit zwischen dem ersten Fehler und dem Zeitstempel des aktuellen (OK) Alarms. | [INLINE_CODE_11] |
| [INLINE_CODE_12] | [SHORTCODE_1] Die Fehlertyp-ID des Fehlers, der diesen Alarm ausgelöst hat. Unter [Fehlertypen]([LINK_URL_2]) findest du eine Liste der Fehlertypen. [SHORTCODE_2] | [INLINE_CODE_13] |
| [INLINE_CODE_14] | Die benutzerdefinierte Fehlermeldung für die jeweilige Aktion bei einem Transaktionsschritt, die den Fehler ausgelöst hat.  | [INLINE_CODE_15] |
| [INLINE_CODE_16] | Das gleiche Datum mit Uhrzeit wie @alert.firstErrorUtc, aber in der Zeitzone deines Accounts. Ebenfalls nach ISO 8601 formatiert. | [INLINE_CODE_17] |
| [INLINE_CODE_18] | Die ID des ersten Fehlers, der die Alarmierung ausgelöst hat. | [INLINE_CODE_19] |
| [INLINE_CODE_20] | Die URL des Deep Links, der dich zu den Details des Fehlers führt, der die Warnmeldung ausgelöst hat. | [INLINE_CODE_21] |
| [INLINE_CODE_22] | Die Fehlerbeschreibung aus der ersten Prüfung, die eine Fehlermeldung ergab. Enthält gegebenenfalls die Schrittnummer. | [INLINE_CODE_23] |
| [INLINE_CODE_24] | Das gleiche Datum mit Uhrzeit wie @alert.firstErrorUtc, aber in Zeitzone und kulturellen Gepflogenheiten deines Accounts. | [INLINE_CODE_25] |
| [INLINE_CODE_26] | Datum und Uhrzeit des ursprünglichen Fehlers, der diese Warnmeldung ausgelöst hat, in UTC-Zeit und nach ISO 8601 formatiert. | [INLINE_CODE_27] |
| [INLINE_CODE_28] | Datum und Uhrzeit des ursprünglichen Fehlers, der diese Warnmeldung ausgelöst hat, in UTC-Zeit und nach den in deinem Account verwendeten Gepflogenheiten formatiert. | [INLINE_CODE_29] |
| [INLINE_CODE_30] | Enthält die Gesamtzahl aufeinanderfolgender Fehler (bestätigte Fehler) des Alarms. | [INLINE_CODE_31] |
| [INLINE_CODE_32] | Die IP-Adresse, die verwendet wurde, um die Prüfung auszuführen. Dies kann eine IPv4- oder IPv6-Adresse sein. | [INLINE_CODE_33] |
| [INLINE_CODE_34] | [SHORTCODE_3] Enthält die Antwort-Header des Alarms in Schlüssel-Wert-Paaren. Beachte, dass der Wert dieser Variable leer sein kann, wenn [Datenschutz für Private Locations]([LINK_URL_3]) bei einem privaten Standort, der die Alarmprüfung durchführt, aktiviert ist. [SHORTCODE_4] | [INLINE_CODE_35] |
| [INLINE_CODE_36] | [SHORTCODE_5] Enthält den erhaltenen Antworttext, sofern verfügbar. Beachte dass der Antworttext Zeichen enthalten kann, die kodiert werden müssen [anhand von @JsonEncode oder @XmlEncode]([LINK_URL_4]). Der Antwortinhalt wird abgeschnitten, wenn er über 1 MB beträgt. [SHORTCODE_6] | [INLINE_CODE_37] |
| [INLINE_CODE_38] | Die IPv4-Adresse des Servers, von dem die Prüfung ausgeführt wurde. | [INLINE_CODE_39] |
| [INLINE_CODE_40] | Die IPv6-Adresse des Servers, von dem die Prüfung ausgeführt wurde. | [INLINE_CODE_41] |
| [INLINE_CODE_42] | Gibt in SSL-Prüfobjektmeldungen Datum mit Uhrzeit wieder, wann das SSL-Zertifikat abläuft. | [INLINE_CODE_43] |
| [INLINE_CODE_44] | Das gleiche Datum mit Uhrzeit wie @alert.timestampUtc, aber in der Zeitzone deines Accounts. Ebenfalls nach ISO 8601 formatiert. | [INLINE_CODE_45] |
| [INLINE_CODE_46] | Das gleiche Datum mit Uhrzeit wie @alert.timestampUtc, aber nach der in deinem Account verwendeten Zeitzone und den verwendeten Gepflogenheiten formatiert. | [INLINE_CODE_47] |
| [INLINE_CODE_48] | Datum und Uhrzeit der Warnmeldung, in UTC-Zeit und nach ISO 8601 formatiert. | [INLINE_CODE_49] |
| [INLINE_CODE_50] | Datum und Uhrzeit der Warnmeldung, in UTC-Zeit und nach den in deinem Account verwendeten Gepflogenheiten formatiert. | [INLINE_CODE_51] |
| [INLINE_CODE_52] | Der Typ dieser Warnmeldung:[HTML_TAG_1];[HTML_TAG_2]- Alarm: Ein neuer Fehler wurde erkannt.[HTML_TAG_3]- OK: Der ursprüngliche Fehler wurde behoben.[HTML_TAG_4]- Erinnerung: Der ursprüngliche Fehler besteht fort. | [INLINE_CODE_53] \| [INLINE_CODE_54] \| [INLINE_CODE_55] |
| [INLINE_CODE_56] | Die einzigartige ID der Meldedefinition, die zur Erzeugung dieser Warnmeldung führte. | [INLINE_CODE_57] |
| [INLINE_CODE_58] | Der Name der Meldedefinition, die zur Erzeugung dieser Warnmeldung führte. | [INLINE_CODE_59] |
| [INLINE_CODE_60] | [SHORTCODE_7] Ein Hinweis auf ein [benutzerdefiniertes Feld]([LINK_URL_5]), das verwendet werden kann, um benutzerdefinierte Daten für einzelne Prüfobjekte aufzunehmen. [SHORTCODE_8] | [INLINE_CODE_61] |
| [INLINE_CODE_62] | Die ID der Eskalationsstufe, die zur Erzeugung dieser Warnmeldung führte. | [INLINE_CODE_63] |
| [INLINE_CODE_64] | Die benutzerdefinierte Nachricht, die in der Eskalationsstufe festgelegt wurde. | [INLINE_CODE_65] |
| [INLINE_CODE_66] | Einzigartige ID des Ereignisses, zu dem diese Warnmeldung erfolgte. Eine Fehlerwarnmeldung und eine Ok-Meldung haben denselben Ereignisschlüssel. | [INLINE_CODE_67] |
| [INLINE_CODE_68] | Die URL eines Deep Links, der dich zum Dashboard dieses Prüfobjekts führt. | [INLINE_CODE_69] |
| [INLINE_CODE_70] | Die URL eines Deep Links, der dich zu den Einstellungen dieses Prüfobjekts führt. | [INLINE_CODE_71] |
| [INLINE_CODE_72] | Die einzigartige ID des Prüfobjekts deines Accounts, das die Warnmeldung ausgelöst hat. | [INLINE_CODE_73] |
| [INLINE_CODE_74] | Der Name des Prüfobjekts deines Accounts, das die Warnmeldung ausgelöst hat. | [INLINE_CODE_75] |
| [INLINE_CODE_76] | Benutzerdefinierte Anmerkungen, die in den Einstellungen des Prüfobjekts eingegeben wurden. | [INLINE_CODE_77] |
| [INLINE_CODE_78] | Enthält den Prüfobjekttyp. | [INLINE_CODE_79] |
| [INLINE_CODE_80] | Die URL oder Netzwerkadresse, die dieses Prüfobjekt testet. | [INLINE_CODE_81] |