{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "Die verfügbaren API-Methoden zur Änderung von Operator-Gruppen.",
  "url": "[URL_BASE_TOPICS]api/monitorgroup-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Diese Seite beschreibt die verfügbaren API-Methoden zur Änderung von Prüfobjektgruppen (Monitor Groups). Weitere Informationen findest du unter [Uptrends Monitor Group API]([LINK_URL_1]).

## MonitorGroup Objektbeschreibung

Das folgende MonitorGroup Objekt wird an den MonitorGroupAPI Endpunkten verwendet:

| Name               | Beschreibung                                                                         | Datentyp |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | Die einzigartige Kennung der Prüfobjektgruppe.                                       | String |
| [INLINE_CODE_2]  | Der Name der Prüfobjektgruppe.                                              | String |
| [INLINE_CODE_3]            | [SHORTCODE_1] 
Gibt an, ob die Prüfobjektgruppe die Standardgruppe [Alle Prüfobjekte]([LINK_URL_2])
 ist. [SHORTCODE_2] | Boolean  |
| [INLINE_CODE_4] | Zeigt an, ob die Anzahl Credits für die Prüfobjektgruppe begrenzt ist.  |  Boolean  |
| [INLINE_CODE_5] |[SHORTCODE_3] 
Gibt die Anzahl genutzter Credits für [Uptime-Prüfobjekte]([LINK_URL_3]) aus. [SHORTCODE_4] | Integer |
| [INLINE_CODE_6]            | [SHORTCODE_5] 
Gibt die Anzahl genutzter Credits für [Browser-(Full-Page Check)-Prüfobjekte]([LINK_URL_4]) aus. [SHORTCODE_6] | Integer |
| [INLINE_CODE_7]            | [SHORTCODE_7]
Gibt die Anzahl genutzter Credits für [Transaktionsprüfobjekte]([LINK_URL_5]) aus.  [SHORTCODE_8] | Integer |
| [INLINE_CODE_8]            | [SHORTCODE_9] 
Gibt die Anzahl genutzter Credits für [Multi-Step API (MSA)-]([LINK_URL_6]) und [Postman-]([LINK_URL_7])Prüfobjekte aus. [SHORTCODE_10] | Integer |
| [INLINE_CODE_9]            | Gibt die Anzahl an Credits aus, die von bestehenden Accounts verwendet wird, die eine Preisstufe für Credits nutzen. | Integer |

### Die Gruppe „Alle Prüfobjekte“

Die Gruppe **Alle Prüfobjekte** ist eine Prüfobjekt- oder Systemgruppe, die standardmäßig all deine Prüfobjekte enthält. Verwende die Guid dieser Gruppe, um Operationen zu verwalten, die alle Prüfobjekte betreffen, zum Beispiel den Start oder das Pausieren aller Prüfobjekte oder Alarme.
Beachte, dass du nicht die Mitglieder dieser Gruppe ändern kannst.


## Endpunkte zum Management einer Prüfobjektgruppe

Die folgenden API-Endpunkte sind zum Erstellen, Ändern und Entfernen von Prüfobjektgruppen sowie den Prüfobjekten in diesen Gruppen verfügbar.

| Abfragetyp | Endpunkt                                                 | Verwendung                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | [INLINE_CODE_10]                                          | Ruft alle Prüfobjektgruppen ab                                        |
| POST         | [INLINE_CODE_11]                                          | Erstellt eine neue Prüfobjektgruppe                                    |
| GET          | [INLINE_CODE_12]                       | Ruft die Informationen über eine Prüfobjektgruppe ab                            |
| PUT          | [INLINE_CODE_13]                       | Aktualisiert eine bestehende Prüfobjektgruppe                              |
| DELETE       | [INLINE_CODE_14]                       | Löscht eine Prüfobjektgruppe                                        |
| GET          | [INLINE_CODE_15]               | Ruft eine Liste aller Prüfobjekte ab, die Mitglied einer Prüfobjektgruppe sind |
| POST         | [INLINE_CODE_16] | Fügt ein bestimmtes Prüfobjekt der Prüfobjektgruppe hinzu                |
| DELETE       | [INLINE_CODE_17] | Entfernt das angegebene Prüfobjekt aus der Prüfobjektgruppe           |

## Weitere Operationen bei Prüfobjektgruppen

Die folgenden API-Endpunkte sind verfügbar, um Operationen bei allen einer Gruppe zugeordneten Prüfobjekten durchzuführen:

| Abfragetyp | Endpunkt                                                 | Verwendung                                                          |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | [INLINE_CODE_18]                  | Stoppt alle Prüfobjekte in der angegebenen Prüfobjektgruppe                           |
| POST         | [INLINE_CODE_19]                 | Startet alle Prüfobjekte in der angegebenen Prüfobjektgruppe                          |
| POST         | [INLINE_CODE_20]             | Stoppt  Alarmierungen für alle Prüfobjekte in der angegebenen Prüfobjektgruppe              |
| POST         | [INLINE_CODE_21]            | Startet Alarmierungen für alle Prüfobjekte in der angegebenen Prüfobjektgruppe             |
| POST         | [INLINE_CODE_22] | Fügt den angegebenen Wartungszeitraum zu allen Prüfobjekten in der angegebenen Gruppe |
