{
  "hero": {
    "title": "Arbeiten mit mehreren SLA Definitionen"
  },
  "title": "Arbeiten mit mehreren SLA Definitionen",
  "summary": "Du kannst mehrere SLAs mithilfe von SLA Definitionen und benutzerdefinierten Dashboards überwachen.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/sla/arbeiten-mit-mehreren-sla-definitionen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Eine SLA Definition reicht für die meisten Nutzer von Uptrends aus, aber einige Unternehmen unterhalten oder überwachen mehrere SLAs mit unterschiedlichen Mindestwerten in Prozent, Seitenladezeiten oder Operator-Reaktionszeiten. Um zu erfahren, wie du zusätzliche SLA Definitionen einrichtest oder die Standard-SLA Definition änderst, lies den Artikel [Eine SLA einrichten]([LINK_URL_1]). Wenn deine SLA Definitionen eingerichtet sind, und du erfahren möchtest, wie du mehrere SLA Definitionen innerhalb deines Uptrends Accounts nutzt, bist du an der richtigen Stelle.

Uptrends berechnet die SLA-Zahlen/Einhaltung jeder SLA Definition für jedes Prüfobjekt deines Accounts. Du musst nicht bestimmte Prüfobjekte mit bestimmten SLA Definitionen verknüpfen, da du die Daten für alle Prüfobjekte oder Prüfobjektgruppen mit jeder angewendeten SLA Definition anzeigen kannst. Du kannst innerhalb des standardmäßigen SLA Übersichts-Dashboards arbeiten und zwischen Definitionen und Prüfobjekten oder Prüfobjektgruppen wechseln. Du kannst auch benutzerdefinierte SLA Übersichts-Dashboards für spezielle Prüfobjekte oder Prüfobjektgruppen sowie SLA Definitionen erstellen.

[SHORTCODE_1]
**Hinweis**: Solltest du in deinem SLA-Übersichtsbericht nur Striche und Nullen statt Daten sehen, sind die Einstellungen deiner Kachel/deines Dashboards mit den Daten kollidiert und haben zu ungültigen Daten geführt. Der Knowledge-Base-Artikel [Fehlende SLA-Übersichtsdaten]([LINK_URL_2]) bietet weitere Infos zu dieser Art Konflikt.
[SHORTCODE_2]

## Wechsel zwischen SLA Definitionen im SLA Übersichts-Dashboard

Sobald du zusätzliche SLA Definitionen erstellt hast, kannst du wählen, welche du im **SLA Übersichts**-Dashboard anzeigen möchtest. Um zwischen SLA Definitionen zu wechseln:

1. Rufe im Menü [SHORTCODE_3] Dashboards > Synthetics: SLA Übersicht [SHORTCODE_4] auf.
2. Klicke auf das Dreipunkte-Menü [SHORTCODE_5] [SHORTCODE_6] der Kachel, um die Kacheleinstellungen aufzurufen.
3. Wähle eine SLA Definition aus der Liste **SLA basierend auf**.
5. Klicke auf [SHORTCODE_7]Übernehmen[SHORTCODE_8].

Deine Kachel aktualisiert sich auf Grundlage der geänderten SLA Definition. Wenn die SLA Definition neu ist, wirst du wahrscheinlich Striche (–) statt Daten sehen. Uptrends berechnet und speichert die SLA-Daten in Echtzeit nach Erstellung der Definition. Da die SLA Definition neu ist, verfügt das System nicht über vollständige Daten auf Basis dieser neuen Definition und den Datum-/Uhrzeiteinstellungen, sodass der Bericht Striche statt Prozentsätzen auf Basis unvollständiger Daten anzeigt. Erfahre mit unserem Knowledge-Base-Artikel [Fehlende SLA-Übersichtsdaten]([LINK_URL_3]) mehr dazu.

## Benutzerdefinierte SLA Übersichts-Dashboards [ANCHOR_1]

Bei der Arbeit mit mehreren SLA Definitionen kannst du separate Kacheln basierend auf unterschiedlichen Kombinationen von SLA Definitionen und Prüfobjekten in einem benutzerdefinierten Dashboard erstellen oder verschiedene benutzerdefinierte Dashboards basierend auf unterschiedlichen Kombinationen von SLA Definitionen und Prüfobjekten oder Prüfobjektgruppen.

Um ein benutzerdefiniertes SLA-Dashboard zu erstellen, beginnst du mit der Erstellung eines benutzerdefinierten Dashboards oder speicherst eine Kopie des **SLA Übersichts**-Dashboards, um es anzupassen.

### Ein benutzerdefiniertes Dashboard SLA Übersicht erstellen

1. Rufe im Menü [SHORTCODE_9] Dashboards > Synthetics: SLA Übersicht [SHORTCODE_10] auf.
2. Klicke auf das Dreipunkte-Menü [SHORTCODE_11] [SHORTCODE_12] der Kachel, um die Einstellungen aufzurufen.
3. (Optional) Wenn du mehrere Definitionen verwendest, ändere die SLA Definition unter **SLA basierend auf**.
4. Klicke auf die [SHORTCODE_13]Gruppen und Prüfobjekte[SHORTCODE_14]-Registerkarte.
5. Entferne die Aktivierung von **Dashboard Kontext verwenden** (sofern markiert) und wähle die Prüfobjekte oder Gruppen, die im benutzerdefinierten Dashboard aufgenommen werden sollen.
6. Klicke auf [SHORTCODE_15]Übernehmen[SHORTCODE_16].
7. Klicke auf das Hamburger-Symbol [SHORTCODE_17] [SHORTCODE_18].
8. Klicke auf [SHORTCODE_19]Speichern unter[SHORTCODE_20].
9. Gib dem neuen Dashboard einen beschreibenden Namen.
10. Klicke auf [SHORTCODE_21]Speichern[SHORTCODE_22].

Du hast nun ein benutzerdefiniertes Dashboard, das du über [SHORTCODE_23]Dashboards > Benutzerdefinierte Dashboards[SHORTCODE_24] aufrufen kannst.
  
### Zusätzliche SLA-Kacheln erstellen

Statt der Erstellung mehrerer Dashboards, kannst du auch ein Mehrfach-Dashboard mit Kacheln basierend auf unterschiedlichen Kombinationen von SLA Definitionen, Prüfobjekten oder Prüfobjektgruppen einrichten. Erstelle zunächst eine Kopie des Standard-SLA-Dashboards für deine Anpassung (siehe die Anweisungen oben ab Schritt 7). Um Kacheln hinzuzufügen:

1. Öffne dein benutzerdefiniertes Dashboard über[SHORTCODE_25]Dashboards > Benutzerdefinierte Dashboards[SHORTCODE_26] und wähle dann dein Dashboard.
2. Klicke auf das Hamburger-Symbol [SHORTCODE_27] [SHORTCODE_28].
3. Wähle *Kachel hinzufügen*.
4. Wähle **Liste Prüfobjektdaten** unter den Kacheltypen.
5. Klicke auf [SHORTCODE_29]Weiter[SHORTCODE_30].
6. Wähle die Prüfobjekte oder Prüfobjektgruppen, die in dieser Kachel angezeigt werden sollen.
7. Klicke auf [SHORTCODE_31]Beenden[SHORTCODE_32], und die neue Kachel wird erzeugt.
8. Klicke auf das Dreipunkte-Menü [SHORTCODE_33] [SHORTCODE_34] der Kachel, um die Kacheleinstellungen aufzurufen.
9. Wähle eine SLA Definition aus der Liste **SLA basierend auf**.
10. Aktiviere die Kontrollkästchen für die Werte, die angezeigt werden sollen.
11. Passe die anderen Einstellungen nach Bedarf an.
12. Klicke auf [SHORTCODE_35]Übernehmen[SHORTCODE_36].
13. Klicke auf die [SHORTCODE_37]Speichern[SHORTCODE_38]-Schaltfläche im *Schnellmenü*.

Füge alle Kacheln hinzu, die du benötigst.
