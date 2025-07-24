{
  "title": "MonitorCheck API",
  "url": "[URL_BASE_TOPICS]api/monitorcheck-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Daten aus Prüfobjektchecks können mithilfe der **MonitorCheck** API-Endpunkte, die Teil der [API v4]([LINK_URL_1]) sind, abgerufen werden. Prüfobjektchecks sind einzelne Messungen, die wir für jedes Prüfobjekt erfassen. Die MonitorCheck API ermöglicht Zugang zu diesen Rohdaten. Sobald Du sie abgerufen hast, kannst Du sie in einer Datenbank zur Offline-Analyse, für Audits oder zu Sicherungszwecken speichern. Es gibt die folgenden drei Endpunkte:

| **MonitorCheck-Endpunkt**  | **Einsatz**                                                       |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Gibt alle Prüfobjektcheckdaten des Accounts aus.                  |
| /MonitorCheck/Monitor      | Gibt alle Prüfobjektcheckdaten für ein bestimmtes Prüfobjekt aus. |
| /MonitorCheck/MonitorGroup | Gibt alle Prüfobjektcheckdaten für eine Prüfobjektgruppe aus.     |

Ein typisches Szenario ist der Download Deiner Daten (für alle Prüfobjekte, für eine Gruppe oder ein bestimmtes Prüfobjekt) zu einem bestimmten Zeitraum (beispielsweise für den vorherigen Monat). Abhängig von der Anzahl der Prüfobjekte und des Monitoring-Intervalls, der für sie eingerichtet ist, kann dies eine erhebliche Menge von Daten ergeben. Eine Möglichkeit, mit der API-Abrufe schnell und reaktionsfreudig bleiben, besteht darin, Daten in Blöcken, z. B. 100 Posten in einem Block, herunterzuladen und zu verarbeiten. Die MonitorCheck API-Methoden wurden dafür optimiert, Daten in Blöcken herunterzuladen.

Alle MonitorCheck-Endpunkte haben die folgenden Parameter:

|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Datumszeitraum, nach dem gefiltert wird (Standard: Last24Hours). [HTML_TAG_1]Lasse dies frei, wenn Du einen benutzerdefinierten Zeitraum [HTML_TAG_2]mit *start* und *end* angeben möchtest. |
| **start**      | Der Beginn eines benutzerdefinierten Zeitraums. [HTML_TAG_3]Lasse dies frei, wenn Du den Parameter *period* verwendest.                                                          |
| **end**        | Das Ende eines benutzerdefinierten Zeitraums. [HTML_TAG_4]Lasse dies frei, wenn Du den Parameter *period* verwendest.                                                            |
| **errorLevel** | Der geringste Fehlerlevel, den Checks ausgeben [HTML_TAG_5](Standard: NoError, d. h., es wird kein Filter angewendet).                                                           |
| **cursor**     | Parameter, um zu bestimmten Datensätzen zu springen, siehe unten.                                                                                                    |
| **take**       | Die Anzahl der auszugebenden Zeilen (Standards: 100; es ist auch die Höchstzahl).                                                                                    |
| **sorting**    | Gibt an, ob die Daten nach Datum in Ascending (aufsteigender) [HTML_TAG_6]oder Descending (absteigender) Reihenfolge geordnet werden (Standard: Descending).                     |

## Springe mit dem Cursor zu bestimmten Daten

Ein Cursor ist ein Zeichenfolgenwert, der als Zeiger im Zeitstrahl Deiner Daten fungiert. Wenn Du eine große Menge Daten abfragst (zum Beispiel alle Prüfobjektdaten des letzten Monats), gibt die API den ersten Block mit 100 Posten aus. Zusammen mit diesen Daten gibt sie Dir auch einen Cursor-Wert, den Du verwenden kannst, um leicht zum zweiten Block zu gelangen. Du kannst diesen Vorgang wiederholen, bis Du alle Daten für den erforderlichen Zeitraum heruntergeladen hast. Ein leerer Cursor zeigt an, dass das Ende der Sequenz erreicht ist und keine weiteren Daten zu erwarten sind.

## Zeitlich auf- oder absteigende Reihenfolge

Du kannst bestimmen, ob Du mit den neuesten Daten beginnen und dann in der Zeit zurück gehen möchtest (sorting=Descending) oder mit dem Beginn eines vergangenen Zeitraums starten und zum aktuellen Zeitpunkt arbeiten möchtest (sorting=Ascending).  
  
Letzteres ist besonders nützlich und effizient, wenn Du einen automatisierten Prozess eingerichtet hast, der regelmäßig mit aktuellen Daten versorgt wird. Beispielsweise könntest Du die API alle fünf Minuten mit Last24Hours, Ascending und Angabe des Cursor-Werts aus der vorherigen Antwort aufrufen: Die API wird nur Daten zurückgeben, die seit Deiner letzten API-Anfrage erzeugt wurden. Das Ergebnis kann eine leere Liste sein, wenn noch keine Daten verfügbar sind, aber wenn die Antwort der API einen Cursor-Wert enthält, können bei einer späteren Anfrage neue Daten abgerufen werden.

## Abruf von MonitorCheck-Daten

Wenn Du eine Liste MonitorCheck-Daten abrufst, enthält jeder MonitorCheck-Eintrag die grundlegenden Werte für den Check wie nachfolgend beschrieben. Abhängig vom Prüfobjekttyp können jedoch auch detailliertere Daten verfügbar sein. Diese Daten können anhand eines separaten API-Aufrufs abgerufen werden. Die Verbindung zwischen den Hauptdaten des MonitorChecks und allen zugehörigen Daten werden als Beziehungen beschrieben. Wenn ein MonitorCheck tatsächlich mit ein oder mehreren Daten verbunden ist, werden sie in dem „Beziehungs“-Mitglied (siehe unten) angezeigt: Er enthält einen Link zu jedem entsprechenden Daten-Endpunkt, der Zugriff auf die Daten gewährt. Es gibt die folgenden Daten-Endpunkte:

| **Daten-Endpunkt**                         | **Einsatz**                                                                                     |
|--------------------------------------------|-------------------------------------------------------------------------------------------------|
| /MonitorCheck/{monitorCheckId}/Http        | Gibt Daten für einen HTTP-Check, einschließlich HTML-Inhalt und Header-Informationen, aus.      |
| /MonitorCheck/{monitorCheckId}/Waterfall   | Gibt die vollständigen Wasserfall-Daten bei einem Full Page Check oder Transaktionsschritt aus. |
| /MonitorCheck/{monitorCheckId}/Transaction | Gibt die Ergebnisse jedes Transaktionsschritts aus, einschließlich der Zeiten pro Schritt.      |

## Generische Datenstruktur

Eine MonitorCheck-Antwort nutzt das folgende Format, um die tatsächlichen Daten von den bereitgestellten Metadaten zu trennen:

### Root

Root enthält die folgenden Mitglieder:

|            |                                                                                         |
|------------|-----------------------------------------------------------------------------------------|
| **Data**   | Eine Reihe oder ein einzelnes Objekt mit (einem Unterset von) den abgefragten Daten.    |
| **Links**  | Links, die sich auf das selbige oder nächste Datenset beziehen.                         |
| **Cursor** | Enthält Cursor-Werte, die verwendet werden sollten, um in einem Datenset zu navigieren. |

### Data

Das Datenmitglied kann eine Reihe von Objekten oder ein einzelnes Objekt enthalten. Das einzelne MonitorCheck-Objekt wie auch mehrere MonitorCheck-Objekte in einer Reihe werden die folgenden Mitglieder haben:

[HTML_TAG_7]
[HTML_TAG_8]
  [HTML_TAG_9]
    [HTML_TAG_10][HTML_TAG_11]
    [HTML_TAG_12][HTML_TAG_13]
    [HTML_TAG_14][HTML_TAG_15]
  [HTML_TAG_16]
[HTML_TAG_17]
[HTML_TAG_18]
  [HTML_TAG_19]
    [HTML_TAG_20]Id[HTML_TAG_21]
    [HTML_TAG_22]Die einzigartige Kennung des Prüfobjektchecks. Die Id entspricht der Prüfobjektcheck-Id, die Du in der Adresszeile siehst, wenn Du die Daten eines Checks in Uptrends anzeigst.[HTML_TAG_23]
    [HTML_TAG_24][HTML_TAG_25]
  [HTML_TAG_26]
  [HTML_TAG_27]
    [HTML_TAG_28]Type[HTML_TAG_29]
    [HTML_TAG_30]Der Objekttyp (ein fester Wert „MonitorCheck“ für diese API-Methoden).[HTML_TAG_31]
    [HTML_TAG_32][HTML_TAG_33]
  [HTML_TAG_34]
  [HTML_TAG_35]
    [HTML_TAG_36]Attributes[HTML_TAG_37]
    [HTML_TAG_38]Die Attribute des Objekts, die die tatsächlichen Daten enthalten. Diese Attribute sind:[HTML_TAG_39]
    [HTML_TAG_40][HTML_TAG_41]
  [HTML_TAG_42]
  [HTML_TAG_43]
    [HTML_TAG_44][HTML_TAG_45]
    [HTML_TAG_46]MonitorGuid[HTML_TAG_47]
    [HTML_TAG_48]Die GUID des Prüfobjekts, die diesem Prüfobjektcheck entspricht.[HTML_TAG_49]
  [HTML_TAG_50]
  [HTML_TAG_51]
    [HTML_TAG_52][HTML_TAG_53]
    [HTML_TAG_54]Timestamp[HTML_TAG_55]
    [HTML_TAG_56]Das Datum und die Uhrzeit, zu der die Überwachung abgeschlossen wurde, basieren auf der Ortszeit des angemeldeten Operators.[HTML_TAG_57]
  [HTML_TAG_58]
  [HTML_TAG_59]
    [HTML_TAG_60][HTML_TAG_61]
    [HTML_TAG_62]ErrorCode[HTML_TAG_63]
    [HTML_TAG_64]Der numerische Fehlercode von Uptrends, falls das Ergebnis einen Fehler zurückgibt; oder 0 im Falle eines OK-Ergebnisses.[HTML_TAG_65]
  [HTML_TAG_66]
  [HTML_TAG_67]
    [HTML_TAG_68][HTML_TAG_69]
    [HTML_TAG_70]TotalTime[HTML_TAG_71]
    [HTML_TAG_72]Die Anzahl Millisekunden, die es gedauert hat, den Prüfobjektcheck durchzuführen.[HTML_TAG_73]
  [HTML_TAG_74]
  [HTML_TAG_75]
    [HTML_TAG_76][HTML_TAG_77]
    [HTML_TAG_78]ResolveTime[HTML_TAG_79]
    [HTML_TAG_80]Die Anzahl Millisekunden, bis die DNS-Abfrage für diesen Check durchgeführt wurde, sofern zutreffend.[HTML_TAG_81]
  [HTML_TAG_82]
  [HTML_TAG_83]
    [HTML_TAG_84][HTML_TAG_85]
    [HTML_TAG_86]ConnectionTime[HTML_TAG_87]
    [HTML_TAG_88]Die Anzahl Millisekunden, bis eine Verbindung hergestellt wurde.[HTML_TAG_89]
  [HTML_TAG_90]
  [HTML_TAG_91]
    [HTML_TAG_92][HTML_TAG_93]
    [HTML_TAG_94]DownloadTime[HTML_TAG_95]
    [HTML_TAG_96]Die Anzahl Millisekunden, die es gedauert hat, die Antwortdaten herunterzuladen.[HTML_TAG_97]
  [HTML_TAG_98]
  [HTML_TAG_99]
    [HTML_TAG_100][HTML_TAG_101]
    [HTML_TAG_102]TotalBytes[HTML_TAG_103]
    [HTML_TAG_104]Die Anzahl heruntergeladener Bytes für diesen Check.[HTML_TAG_105]
  [HTML_TAG_106]
  [HTML_TAG_107]
    [HTML_TAG_108][HTML_TAG_109]
    [HTML_TAG_110]ResolvedIpAddress[HTML_TAG_111]
    [HTML_TAG_112]Die IP-Adresse, die für den angegebenen Domainnamen im Rahmen des Prüfobjektchecks aufgelöst wurde.[HTML_TAG_113]
  [HTML_TAG_114]
  [HTML_TAG_115]
    [HTML_TAG_116][HTML_TAG_117]
    [HTML_TAG_118]ErrorLevel[HTML_TAG_119]
    [HTML_TAG_120]Ein Wert, der den OK-/Fehler-Status für diesen Check angibt: NoError, wenn das Ergebnis OK lautete; Unconfirmed, wenn ein Fehler gefunden wurde; Confirmed, wenn direkt nach einem Unconfirmed-Fehler ein Fehler nach einem doppelten Check gefunden wurde.[HTML_TAG_121]
  [HTML_TAG_122]
  [HTML_TAG_123]
    [HTML_TAG_124][HTML_TAG_125]
    [HTML_TAG_126]ErrorDescription[HTML_TAG_127]
    [HTML_TAG_128]Ein Text-Wert, der den gefundenen Fehler beschreibt; oder OK, wenn kein Fehler gefunden wurde.[HTML_TAG_129]
  [HTML_TAG_130]
  [HTML_TAG_131]
    [HTML_TAG_132][HTML_TAG_133]
    [HTML_TAG_134]ErrorMessage[HTML_TAG_135]
    [HTML_TAG_136]Zusätzliche Fehlerinformationen, falls verfügbar.[HTML_TAG_137]
  [HTML_TAG_138]
  [HTML_TAG_139]
    [HTML_TAG_140][HTML_TAG_141]
    [HTML_TAG_142]ServerId[HTML_TAG_143]
    [HTML_TAG_144]Die Id des Checkpoint-Servers von Uptrends, der den Check durchgeführt hat.[HTML_TAG_145]
  [HTML_TAG_146]
   [HTML_TAG_147]
    [HTML_TAG_148][HTML_TAG_149]
    [HTML_TAG_150]HttpStatusCode[HTML_TAG_151]
    [HTML_TAG_152]Der HTTP-Statuscode, der zurückgegeben wurde (sofern zutreffend).[HTML_TAG_153]
  [HTML_TAG_154]
  [HTML_TAG_155]
    [HTML_TAG_156]Relationships[HTML_TAG_157]
    [HTML_TAG_158]Die Beziehungs-Reihe enthält eine Liste zugehöriger Daten/Objekte zu den aktuellen Daten. Diese Liste enthält Links, um die zugehörigen Daten abzurufen. Beziehungsdaten haben dieselbe Struktur, d. h., diese Einträge enthalten die gleichen Id-, Type- und Links-Mitglieder.[HTML_TAG_159]
    [HTML_TAG_160][HTML_TAG_161]
  [HTML_TAG_162]
[HTML_TAG_163]
[HTML_TAG_164]