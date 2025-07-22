{
  "title": "MonitorCheck API",
  "url": "/support/kb/api/monitorcheck-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorcheck-api"
}

Daten aus Prüfobjektchecks können mithilfe der **MonitorCheck** API-Endpunkte, die Teil der [API v4](/support/kb/api/v4) sind, abgerufen werden. Prüfobjektchecks sind einzelne Messungen, die wir für jedes Prüfobjekt erfassen. Die MonitorCheck API ermöglicht Zugang zu diesen Rohdaten. Sobald Du sie abgerufen hast, kannst Du sie in einer Datenbank zur Offline-Analyse, für Audits oder zu Sicherungszwecken speichern. Es gibt die folgenden drei Endpunkte:

| **MonitorCheck-Endpunkt**  | **Einsatz**                                                       |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Gibt alle Prüfobjektcheckdaten des Accounts aus.                  |
| /MonitorCheck/Monitor      | Gibt alle Prüfobjektcheckdaten für ein bestimmtes Prüfobjekt aus. |
| /MonitorCheck/MonitorGroup | Gibt alle Prüfobjektcheckdaten für eine Prüfobjektgruppe aus.     |

Ein typisches Szenario ist der Download Deiner Daten (für alle Prüfobjekte, für eine Gruppe oder ein bestimmtes Prüfobjekt) zu einem bestimmten Zeitraum (beispielsweise für den vorherigen Monat). Abhängig von der Anzahl der Prüfobjekte und des Monitoring-Intervalls, der für sie eingerichtet ist, kann dies eine erhebliche Menge von Daten ergeben. Eine Möglichkeit, mit der API-Abrufe schnell und reaktionsfreudig bleiben, besteht darin, Daten in Blöcken, z. B. 100 Posten in einem Block, herunterzuladen und zu verarbeiten. Die MonitorCheck API-Methoden wurden dafür optimiert, Daten in Blöcken herunterzuladen.

Alle MonitorCheck-Endpunkte haben die folgenden Parameter:

|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Datumszeitraum, nach dem gefiltert wird (Standard: Last24Hours). <br>Lasse dies frei, wenn Du einen benutzerdefinierten Zeitraum <br>mit *start* und *end* angeben möchtest. |
| **start**      | Der Beginn eines benutzerdefinierten Zeitraums. <br>Lasse dies frei, wenn Du den Parameter *period* verwendest.                                                          |
| **end**        | Das Ende eines benutzerdefinierten Zeitraums. <br>Lasse dies frei, wenn Du den Parameter *period* verwendest.                                                            |
| **errorLevel** | Der geringste Fehlerlevel, den Checks ausgeben <br>(Standard: NoError, d. h., es wird kein Filter angewendet).                                                           |
| **cursor**     | Parameter, um zu bestimmten Datensätzen zu springen, siehe unten.                                                                                                    |
| **take**       | Die Anzahl der auszugebenden Zeilen (Standards: 100; es ist auch die Höchstzahl).                                                                                    |
| **sorting**    | Gibt an, ob die Daten nach Datum in Ascending (aufsteigender) <br>oder Descending (absteigender) Reihenfolge geordnet werden (Standard: Descending).                     |

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

<table>
<thead>
  <tr>
    <th class="cell-small"></th>
    <th class="cell-large"></th>
    <th class="cell-large"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="bold">Id</td>
    <td>Die einzigartige Kennung des Prüfobjektchecks. Die Id entspricht der Prüfobjektcheck-Id, die Du in der Adresszeile siehst, wenn Du die Daten eines Checks in Uptrends anzeigst.</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Type</td>
    <td>Der Objekttyp (ein fester Wert „MonitorCheck“ für diese API-Methoden).</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Attributes</td>
    <td>Die Attribute des Objekts, die die tatsächlichen Daten enthalten. Diese Attribute sind:</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">MonitorGuid</td>
    <td>Die GUID des Prüfobjekts, die diesem Prüfobjektcheck entspricht.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">Timestamp</td>
    <td>Das Datum und die Uhrzeit, zu der die Überwachung abgeschlossen wurde, basieren auf der Ortszeit des angemeldeten Operators.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorCode</td>
    <td>Der numerische Fehlercode von Uptrends, falls das Ergebnis einen Fehler zurückgibt; oder 0 im Falle eines OK-Ergebnisses.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalTime</td>
    <td>Die Anzahl Millisekunden, die es gedauert hat, den Prüfobjektcheck durchzuführen.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolveTime</td>
    <td>Die Anzahl Millisekunden, bis die DNS-Abfrage für diesen Check durchgeführt wurde, sofern zutreffend.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ConnectionTime</td>
    <td>Die Anzahl Millisekunden, bis eine Verbindung hergestellt wurde.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">DownloadTime</td>
    <td>Die Anzahl Millisekunden, die es gedauert hat, die Antwortdaten herunterzuladen.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalBytes</td>
    <td>Die Anzahl heruntergeladener Bytes für diesen Check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolvedIpAddress</td>
    <td>Die IP-Adresse, die für den angegebenen Domainnamen im Rahmen des Prüfobjektchecks aufgelöst wurde.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorLevel</td>
    <td>Ein Wert, der den OK-/Fehler-Status für diesen Check angibt: NoError, wenn das Ergebnis OK lautete; Unconfirmed, wenn ein Fehler gefunden wurde; Confirmed, wenn direkt nach einem Unconfirmed-Fehler ein Fehler nach einem doppelten Check gefunden wurde.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorDescription</td>
    <td>Ein Text-Wert, der den gefundenen Fehler beschreibt; oder OK, wenn kein Fehler gefunden wurde.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorMessage</td>
    <td>Zusätzliche Fehlerinformationen, falls verfügbar.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ServerId</td>
    <td>Die Id des Checkpoint-Servers von Uptrends, der den Check durchgeführt hat.</td>
  </tr>
   <tr>
    <td></td>
    <td class="bold">HttpStatusCode</td>
    <td>Der HTTP-Statuscode, der zurückgegeben wurde (sofern zutreffend).</td>
  </tr>
  <tr>
    <td class="bold">Relationships</td>
    <td>Die Beziehungs-Reihe enthält eine Liste zugehöriger Daten/Objekte zu den aktuellen Daten. Diese Liste enthält Links, um die zugehörigen Daten abzurufen. Beziehungsdaten haben dieselbe Struktur, d. h., diese Einträge enthalten die gleichen Id-, Type- und Links-Mitglieder.</td>
    <td></td>
  </tr>
</tbody>
</table>