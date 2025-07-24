{
  "hero": {
    "title": "Audit Log"
  },
  "title": "Audit Log",
  "summary": "In diesem Artikel findest du Hinweise zu den Audit Logs.",
  "url": "[URL_BASE_TOPICS]account/audit-log",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mit all den Updates und verschiedenen Aktivitäten, die in deiner Uptrends Webanwendung ablaufen, kann es schwierig werden, das Was, Wo, Wann und Wer der Änderungen an den Einstellungen nachzuhalten. In bestimmten Fällen ist es aus verschiedenen Gründen hilfreich, ein Verlaufsprotokoll zu führen. Beispielsweise können versehentliche Änderungen schnell zurückgenommen, Ursachen bei Problemen identifiziert und Berechtigungen überprüft werden.

Das Uptrends **Audit Log** ist ein praktisches Tool, das alle Anforderungen erfüllt! Es zeichnet alle Aktivitäten auf, die in der Uptrends Anwendung vorgenommen werden und liefert detaillierte Informationen über Operator, Zeitraum, Ort und welche speziellen Änderungen am Account erfolgt sind.

![Audit Log Dashboard-Überblick]([LINK_URL_1])

[SHORTCODE_1]
Das **Audit Log** gibt es für alle Abonnements und ist leicht aufrufbar. Navigiere einfach zu [SHORTCODE_3]  Accounteinstellungen > Audit Log [SHORTCODE_4], um die Änderungen an deinem Account anzuzeigen.
[SHORTCODE_2]

## Funktionen des Audit Logs

Das Dashboard Audit Log ermöglicht dir, Protokolle für deinen Account anzuzeigen, zu filtern und zu exportieren.

### Audit Logs anzeigen

Standardmäßig ist das Audit Log Dashboard eine Liste in Tabellenform, bei der die neuesten Änderungen zuerst genannt sind. Die Spalten umfassen:

- **Datum/Uhrzeit** – zeigt tatsächliches Datum und Uhrzeit, an dem die Änderung vorgenommen wurde.
- **Ereignistyp** – gibt die Art der Änderung an, die vom Nutzer durchgeführt wurde, beispielsweise *Anmeldungsaktion, Element aktualisiert oder Mitglieder-Änderung*.
- **Operator** – gibt den Namen des Operators an, der die Änderung vorgenommen hat.
- **Mitteilung** – enthält eine Beschreibung, welches Element erstellt, aktualisiert oder gelöscht wurde. Wenn du zum Beispiel einen neuen Operator erstellst, lautet die Mitteilung *Operator „ABC“ wurde erstellt*.
- **Quelle** – gibt die Quelle an, wo die Änderung vorgenommen wurde. Wenn eine Änderung über die Uptrends Webanwendung erfolgt ist, ist als Quelle *Web-App* angegeben. Erfolgten Änderungen über die API, wird *API* als Quelle angegeben.

### Audit Logs filtern

Um einfach auf bestimmte Aktivitäten in der Anwendung zu filtern, kannst du im Audit Log die Anzeige auf Einträge nach *Ereignistyp* und *Objekt-Typ* beschränken.

Indem du auf das Drop-down-Menü [SHORTCODE_5] Ereignistyp[SHORTCODE_6] klickst, kannst du ganz einfach die Art der Änderung auswählen, die an deinem Account vorgenommen wurde. Du kannst Kategorien wählen wie *Anmeldungsaktion, Mitglieder-Änderung, Berechtigungsänderung, Element erstellt* und viele weitere.

Auf ähnliche Weise ermöglicht dir das Drop-down-Menü [SHORTCODE_7] Objekt-Typ [SHORTCODE_8] nach bestimmten Elementänderungen, die an deinen *Prüfobjekten, Prüfobjektgruppen, Operatoren, Operator-Gruppen* oder andere bestimmte Bereiche vorgenommen wurden, zu filtern.

### Audit Logs exportieren

Wie jedes andere Uptrends Dashboard kann auch das Audit Log als PDF oder im Excel- und HTML-Format exportiert werden. Lies diesen [Knowledge-Base-Artikel]([LINK_URL_2]) mit detaillierten Schritten zum Export deiner Dashboard-Daten des Audit Logs.

Wenn du deine Daten exportiert hast, erhältst du dieselben Details, die dir in der tabellarischen Zusammenfassung im Audit Log Dashboard angezeigt werden. Nur die Spalte *Quelle* fehlt, um die Ansicht zu vereinfachen.

## Audit Log Details

Da die Audit Log Tabelle lediglich eine Übersicht des Änderungsverlaufs in deinem Account anzeigt, geben die **Audit Log Details** mehr Einzelheiten zu den Änderungen an.

Klicke auf jeden Audit Log Eintrag, um die **Audit Log Details** in einem Pop-up-Fenster anzuzeigen:

![Übersicht Audit Log Details]([LINK_URL_3])

Das Pop-up zeigt Daten ähnlich denen, die du in der Tabelle des Audit Log Dashboards schon gesehen hast. Darüber hinaus erhältst du Informationen wie die Audit Log ID (eine einzigartige Kennung des Audit Log Eintrags), den Namen eines Elementtyps (beispielsweise Prüfobjekt, Operator oder Meldedefinition) und spezielle Informationen darüber, welche Elemente erstellt, aktualisiert und gelöscht wurden.

Wenn ein Element erstellt wurde, zeigen die **Audit Log Details** wie dargestellt den Bereich *Erstellt mit Werten* mit dem erstellten Element und seinen Einstellungen. Ähnlich, wenn du ein Element aktualisierst: Die Audit Log Details zeigen den Bereich *Aktualisiert mit neuen Werten* mit den vorherigen und den neuen Werten. Beachte, dass die angezeigten Informationen in den Audit Log Details sich unterscheiden, abhängig von der Art der Änderung und welche Elemente aktualisiert wurden.

## Audit Log Details für jeden Objekt-Typ

Dieser Abschnitt zeigt den Verlauf der Änderungen, die im Audit Log für jeden *Objekt-Typ* erfasst werden.

### Dashboards
Das Audit Log zeichnet Änderungen auf, die an und von den **Dashboards** erfolgen, wenn:
- Berechtigungen zum *Teilen* für Dashboards gewährt oder entfernt wurden

### Meldedefinitionen
Das Audit Log zeichnet Änderungen auf, die an und von den **Meldedefinitionen** erfolgen, wenn:

- eine neue Meldedefinition erstellt wurde
- eine bestehende Meldedefinition umbenannt oder gelöscht wurde
- der Aktiv-Status der Meldedefinition geändert wurde
- Einstellungen an der Reihe der in der Meldedefinition referenzierten Prüfobjekte, Prüfobjektgruppen oder Eskalationsstufen hinzugefügt, geändert oder entfernt wurden
- Berechtigungen für Meldedefinitionen gewährt oder entfernt wurden

### Integrationen
Das Audit Log zeichnet Änderungen auf, die an und von den **Integrationen** erfolgen, wenn:

- eine neue Integration erstellt wurde
- eine bestehende Integration umbenannt oder gelöscht wurde
- der Aktiv-Status der Integration geändert wurde
- vordefinierte Variablen und allgemeine Einstellungen der Integration hinzugefügt, geändert oder entfernt wurden
- Berechtigungen für Integrationen gewährt oder entfernt wurden

### Prüfobjekte
Das Audit Log zeichnet Änderungen auf, die an und von den **Prüfobjekten** erfolgen, wenn:

- ein neues Prüfobjekt erstellt wurde
- ein bestehendes Prüfobjekt umbenannt oder gelöscht wurde
- der Aktiv-Status des Prüfobjekts geändert wurde
- die Prüfobjekteinstellungen, die auf den Registerkarten [SHORTCODE_9] Allgemein [SHORTCODE_10], [SHORTCODE_11] Schritte [SHORTCODE_12], [SHORTCODE_13] Fehlerbedingungen [SHORTCODE_14], [SHORTCODE_15] Erweitert [SHORTCODE_16], [SHORTCODE_17] Checkpoints [SHORTCODE_18], [SHORTCODE_19] Wartungszeiträume [SHORTCODE_20] und [SHORTCODE_21] Mitglied von [SHORTCODE_22] konfiguriert sind, hinzugefügt, aktualisiert oder entfernt wurden
- Prüfobjekte und Prüfobjektmeldungen aktiviert und deaktiviert wurden
- Berechtigungen für Prüfobjekte gewährt oder entfernt wurden

### Prüfobjektgruppen
Das Audit Log zeichnet Änderungen auf, die an und von den **Prüfobjektgruppen** erfolgen, wenn:

- eine neue Prüfobjektgruppe erstellt wurde
- eine bestehende Prüfobjektgruppe umbenannt oder gelöscht wurde
- Prüfobjektdaten hinzugefügt, aktualisiert und entfernt oder die Reihe der Prüfobjekte in der Prüfobjektgruppe geändert wurden
- Berechtigungen für Prüfobjektgruppen gewährt oder entfernt wurden

### Prüfobjektvorlagen.
Das Audit Log zeichnet Änderungen auf, die an und von den **Prüfobjektvorlagen** erfolgen, wenn:

- eine neue Prüfobjektvorlage erstellt wurde
- eine bestehende Prüfobjektvorlage umbenannt oder gelöscht wurde
- Konfigurationen von den allgemeinen Einstellungen, [SHORTCODE_23] Checkpoints [SHORTCODE_24] und [SHORTCODE_25] Wartungszeiträumen [SHORTCODE_26] in der Prüfobjektvorlage hinzugefügt, aktualisiert oder entfernt wurden

### Operatoren
Das Audit Log zeichnet Änderungen auf, die an und von den **Operatoren** erfolgen, wenn:

- ein neuer Operator erstellt wurde
- ein bestehender Operator umbenannt oder gelöscht wurde
- Konfigurationen zu den Registerkarten der allgemeinen Einstellungen,
 [SHORTCODE_27] Dienstplan [SHORTCODE_28] und [SHORTCODE_29] Mitglied von [SHORTCODE_30] der Operatoren hinzugefügt, diese aktualisiert oder entfernt wurden
- Zeitzonen-Einstellungen aktualisiert wurden
- eine Einladung an einen Operator gesendet wurde oder ein Operator eine Einladung akzeptiert hat
- Berechtigungen für Operatoren gewährt oder entfernt wurden

Im Audit Log werden auch auf Operatoren bezogene Objekte nach *Ereignistyp* wie *Anmeldungsaktion* und *Fehlgeschlagener Loginversuch* aufgezeichnet.

### Operator-Gruppen

Das Audit Log zeichnet Änderungen auf, die an und von den **Operator-Gruppen** erfolgen, wenn:

- eine neue Operator-Gruppe erstellt wurde
- Mitglieder einer Operator-Gruppe hinzugefügt oder entfernt wird
- der Name einer Operator-Gruppe bearbeitet wird
- eine bestehende Operator-Gruppe gelöscht wird
- Berechtigungen für Operatorgruppen gewährt oder entfernt wurden

### Private Locations

Das Audit Log zeichnet Änderungen auf, die an und von den **Private Locations** erfolgen, wenn:

- ein privater Standort erstellt wurde
- ein bestehender privater Standort umbenannt oder gelöscht wird
- ein privater Checkpoint aktiviert oder deaktiviert wurde
- die Einstellungen von privaten Standorten hinzugefügt, aktualisiert und entfernt wurden

### SLA-Definitionen

Das Audit Log zeichnet Änderungen auf, die an und von den **SLA-Definitionen** erfolgen, wenn:

- eine neue SLA-Definition erstellt wurde
- eine bestehende SLA-Definition umbenannt oder gelöscht wurde
- der SLA-Zeitplan und die Einstellungen der ausgeschlossenen Zeiträume hinzugefügt, aktualisiert oder entfernt wurden

### Vault

Das Audit Log zeichnet Änderungen auf, die von der **Vault** erfolgen, wenn:

- ein Vault Item erstellt, aktualisiert oder gelöscht wurde
- ein Vault-Bereich erstellt, aktualisiert oder gelöscht wurde
- Vault Items einem Vault-Bereich hinzugefügt, in ihm aktualisiert oder gelöscht wurden
- Berechtigungen für Vault-Bereiche gewährt oder entfernt wurden
