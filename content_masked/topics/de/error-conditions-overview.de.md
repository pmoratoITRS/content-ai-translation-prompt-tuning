{
  "hero": {
    "title": "Fehlerbedingungen – Überblick"
  },
  "title": "Fehlerbedingungen – Überblick",
  "summary": "Welche Fehlerbedingungen gibt es und wie werden sie genutzt? ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/ubersicht-der-fehlerbedingungen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": false
}

Fehlerbedingungen spielen eine wichtige Rolle bei der Erzeugung von Prüfobjektalarmen. Einrichten einer Fehlerbedingung ist der erste Schritt des [Alarm- und Fehlerablaufs]([LINK_URL_1]), über den du Warnmeldungen erhalten kannst.

Eine **Fehlerbedingung** ermöglicht dir, eine Reihe an Kriterien zu definieren, anhand derer dein Prüfobjekt bei Website, Webservice oder Server Fehler feststellen kann. Sie dient dem Prüfobjekt als Basis, um zu entscheiden, welches Website-Verhalten zu einem Fehler führt und welches dies nicht tut.

Wenn du beispielsweise sicherstellen möchtest, dass deine Website in weniger als drei Sekunden geladen ist, kannst du eine Fehlerbedingung einrichten und Schwellen für die Seitenladezeit angeben. Oder wenn du prüfen möchtest, dass der Inhalt, Plug-ins oder Skripte deiner Website korrekt geladen wurden, kannst du jeweils bestimmte Fehlerbedingungen dafür einrichten.

Sobald eine Fehlerbedingung erfüllt wird, wird ein Fehler generiert, der einen Alarm auslöst. Wurde eine Alarmierung konfiguriert, wirst du sofort mit einer Warnmeldung benachrichtigt.

## Fehlerbedingungen für Prüfobjekttypen [ANCHOR_1]

Auf dem Tab [SHORTCODE_15] Fehlerbedingungen [SHORTCODE_16] kannst du unterschiedliche Fehlerbedingungen für jeden Prüfobjekttyp einrichten. Beachte das die Verfügbarkeit von Fehlerbedingungen je nach Kategorie des Prüfobjekts und welche Daten erfasst werden variieren kann:

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen]([LINK_URL_2])

### Verfügbarkeitsprüfobjekt

Die folgenden Fehlerbedingungen sind für [Uptime-Prüfobjekttypen]([LINK_URL_3]) verfügbar:

| Prüfobjekttyp | Fehlerbedingungen | 
|--|--|
| HTTPS, Webservice HTTP und HTTPS | [SHORTCODE_1] 
- [Prüfe Seitenerreichbarkeit]([LINK_URL_4]) 
- [Prüfe Seiteninhalt]([LINK_URL_5])
- [Prüfe Seitenladezeit]([LINK_URL_6])
- [Prüfe Ressourcen]([LINK_URL_7])
[SHORTCODE_2] |
| DNS, SSL, SFTP, FTP | [SHORTCODE_3]
- [Prüfe Ressourcen]([LINK_URL_8])
- [Prüfe komplette Laufzeit]([LINK_URL_9])
[SHORTCODE_4] |
| SMTP, POP3, IMAP | [SHORTCODE_5]
- [Prüfe Ressourcen]([LINK_URL_10])
- [Prüfe komplette Laufzeit]([LINK_URL_11])
[SHORTCODE_6] |
| Microsoft SQL Server,  MySQL | [SHORTCODE_7]
- [Prüfe Ressourcen]([LINK_URL_12])
- [Prüfe komplette Laufzeit]([LINK_URL_13])
[SHORTCODE_8] |
| Ping, Connect | [SHORTCODE_9]
- [Prüfe Ressourcen]([LINK_URL_14])
- [Prüfe komplette Laufzeit]([LINK_URL_15])
[SHORTCODE_10] |

### Browser-Prüfobjekte oder Full Pagecheck (FPC)

Die folgenden Fehlerbedingungen sind verfügbar für [Browser- bzw. Full Pagecheck (FPC)-Prüfobjekte]([LINK_URL_16]):

| Prüfobjekttyp | Fehlerbedingungen |
|--|--|
| Browser- bzw. Full Pagecheck | [SHORTCODE_11]

- [Prüfe Seitenerreichbarkeit]([LINK_URL_17]) 
- [Prüfe Seiteninhalt]([LINK_URL_18])
- [Von der Seite geladene URLs überprüfen]([LINK_URL_19]) 
- [Prüfe Seitenladezeit]([LINK_URL_20])
- [Prüfe Core Web Vitals]([LINK_URL_21])
- [Prüfe W3C-Metriken]([LINK_URL_22])
- [Prüfe Konsoleninhalt]([LINK_URL_23])
- [Prüfe Ressourcen]([LINK_URL_24])
[SHORTCODE_12] |

### Transaktionsprüfobjekt

Fehlerbedingungen bei [Transaktionsprüfobjekten]([LINK_URL_25]) sind auch für jeden Schritt verfügbar. Abhängig von der [Einrichtung des Transaktionsschritts]([LINK_URL_26]) sind die folgenden Fehlerbedingungen verfügbar bzw. nicht verfügbar:

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen]([LINK_URL_27])

| Prüfobjekttyp | Fehlerbedingungen |
|--|--|
| Transaktion bzw. User Journey | [SHORTCODE_13] 
- [Inhaltsprüfungen]([LINK_URL_28]).
- [Prüfe Ressourcen]([LINK_URL_29])
- [Von der Seite geladene URLs überprüfen]([LINK_URL_30]) 
- [Prüfe Core Web Vitals]([LINK_URL_31])
- [Prüfe W3C-Metriken]([LINK_URL_32])
- [Prüfe Konsoleninhalt]([LINK_URL_33])
- [Prüfe Seitenerreichbarkeit]([LINK_URL_34]) 
- [Prüfe komplette Laufzeit]([LINK_URL_35])
[SHORTCODE_14] |

Beachte, dass ein [Multi-step API (MSA)-Prüfobjekt]([LINK_URL_36]) Fehler auf andere Art feststellt. Der Einsatz von **Assertions** ermöglicht, Prüfungen zu definieren, um zu bestätigen, dass die API-Antwort den Erwartungen entspricht. Mehr erfährst du unter [MSA Assertions]([LINK_URL_37]).

## Eine Fehlerbedingung einrichten [ANCHOR_2]

Du kannst Fehlerbedingungen hinzufügen, wenn du [ein Prüfobjekt von Grund auf einrichtest]([LINK_URL_38]) oder wenn du ein bestehendes Prüfobjekt bearbeitest.

Um Fehlerbedingungen einzurichten:

1. Gehe zu [SHORTCODE_17]Überwachung > Prüfobjekteinrichtung[SHORTCODE_18].
2. Klicke auf das Prüfobjekt, bei dem du eine Fehlerbedingung hinzufügen möchtest.
3. Wechsle zum Tab [SHORTCODE_19]Fehlerbedingungen[SHORTCODE_20].
4. Klicke auf die Fehlerbedingung, um den Bereich einzublenden und die Prüfobjekteinstellungen zu konfigurieren.
5. (Optional) Füge eine neue Fehlerbedingung hinzu, indem du auf [SHORTCODE_21] \+Neue Prüfung [SHORTCODE_22] klickst.
6. Setze die Konfiguration von Bedingungen fort.
7. Klicke auf [SHORTCODE_23] Speichern [SHORTCODE_24], um alle Änderungen zu bestätigen.

Um benachrichtigt zu werden, wenn die Fehlerbedingung erfüllt wird, [erstelle eine Meldedefinition]([LINK_URL_39]).

![Screenshot Prüfobjekteinrichtung Fehlerbedingungen]([LINK_URL_40])