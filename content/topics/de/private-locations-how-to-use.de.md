{
  "hero": {
    "title": "Private Location-Checkpoints nutzen"
  },
  "title": "Private Location-Checkpoints nutzen",
  "summary": "Ein Überblick zur Einrichtung des Monitorings und wie du deinen privaten Standort sowie private Checkpoints nach der Installation verwaltest.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-locations-nutzen",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-how-to-use"
}

Wenn du einen [privaten Standort]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) einrichtest, werden standardmäßig zwei Checkpoints erzeugt. Du kannst die Checkpoints für deinen privaten Standort in der Uptrends Anwendung auswählen und sie in deiner alltäglichen Monitoring-Einrichtung aufnehmen. Der Checkpoint muss für deine neuen oder bestehenden Prüfobjekte auf der Einrichtungsseite der Prüfobjekte festgelegt werden.

Wenn du die Einstellungen deines jeweiligen Checkpoints und privaten Standorts bearbeiten möchtest, kannst du dies über die Seite „Private Locations“ erledigen. Der private Standort enthält deine Checkpoints. Wenn du einen Checkpoint entfernst, bleibt der Standort bestehen. Löschst du einen privaten Standort, wird der komplette Standort mit seinen Checkpoints entfernt.

## Einen Checkpoint in Betrieb nehmen 
Ein Checkpoint wird nicht automatisch genutzt. Wenn du den bzw. die Checkpoints an deinen privaten Standorten nutzen möchtest, musst du sie zunächst zur Checkpoint-Auswahlliste deines Prüfobjekts hinzufügen.

Einen Checkpoint für ein Prüfobjekt auswählen:
1. Gehe in der Uptrends Anwendung zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Suche nach dem Namen des Prüfobjekts, das den Checkpoint nutzen soll, und klicke den zugehörigen Link in der Spalte *Prüfobjektname*. (Hinweis: Wähle nicht die neuen Multi-Step API-Prüfobjekte mit dem Namen des Checkpoints, diese gehören zu deinem privaten Checkpoint.)
3. Der Bildschirm zur Prüfobjektkonfiguration wird angezeigt. Er enthält die Registerkarten mit deinen Prüfobjekteinstellungen. Öffne die Registerkarte {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} und wähle alle Checkpoints von deinem privaten Standort oder einen der privaten Checkpoints. (Du kannst diesen Checkpoint bei allen neuen Prüfobjekten, die du erstellst, auswählen.)
![Screenshot von privaten Checkpoints bei einem Prüfobjekt](/img/content/scr_private-location-checkpoints-tab-monitor.min.png)
4. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

## Private Standorte verwalten 

Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf. Hier kannst du die Checkpoints von deinem privaten Standort verwalten.

### Einen privaten Standort umbenennen

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf.
2. Klicke auf das Bearbeiten (Beleistift)-Symbol.
3. Gib den neuen Namen ein und drücke die Eingabetaste.

### Einen privaten Standort entfernen

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf.
2. Klicke auf die graue Schaltfläche für Standort entfernen (Abfalleimer).
3. Bestätige das Entfernen des ausgewählten privaten Standorts und den damit verbundenen Checkpoints.
4. Optional: Entferne die (zugewiesene) VM mit den gelöschten Checkpoints.

### Um einen Checkpoint zu entfernen:

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf.
2. Klicke auf die Schaltfläche {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} und wähle *Checkpoint löschen*. Alternativ kannst du auf den Namen des Checkpoints klicken und ihn öffnen. Klicke dann auf die graue Schaltfläche *Checkpoint löschen*.
3. Bestätige das Entfernen des ausgewählten Checkpoints.

### Einen privaten Checkpoint deaktivieren

Wenn du einen privaten Checkpoint deaktivierst, kann er keine Prüfungen mehr auszuführen.

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf.
2. Klicke auf die Schaltfläche {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} und wähle *Checkpoint deaktivieren*. Alternativ kannst du auf den Namen des Checkpoints klicken und ihn öffnen. Klicke dann auf die graue Schaltfläche *Checkpoint deaktivieren*.
3. Gib eine Beschreibung ein, weshalb du diesen Checkpoint deaktivierst.
4. Bestätige das Entfernen des ausgewählten Checkpoints durch Klicken auf {{< AppElement type="deletebutton" >}} Deaktivieren {{< /AppElement >}}.

### Einen privaten Checkpoint aktivieren

1. Rufe in der Uptrends Anwendung {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} auf.
2. Klicke auf die Schaltfläche {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} und wähle *Checkpoint aktivieren*. Alternativ kannst du auf den Namen des Checkpoints klicken und ihn öffnen. Klicke dann auf die graue Schaltfläche *Checkpoint aktivieren*.
3. Bestätige die Aktivierung des ausgewählten Checkpoints durch Klicken auf {{< AppElement type="savebutton" >}} Aktivieren {{< /AppElement >}}.

## Private Checkpoints – Registerkarten

### Checkpoint-Zustand 
Zur Überwachung deines privaten Checkpoints bietet die Registerkarte [Checkpoint-Zustand]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="de" >}}) einen Überblick über die wichtigsten Messwerte, die sich auf den Checkpoint auswirken. Das umfasst Informationen zur installierten Software, [Datenschutzeinstellungen]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) und Metriken zum Host.

### Installation 

Nutze den Installationsleitfaden, um deine privaten Checkpoints in Docker einzurichten: [Einen nutzerverwalteten Checkpoint installieren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}).

### Wie man diesen Checkpoint verwendet

Die Registerkarte {{< AppElement type="tab" >}} Diesen Checkpoint nutzen {{< /AppElement >}} bietet eine schnellen Start für die Prüfobjekteinrichtungsseite, wo du deine Prüfobjekte einrichten kannst. Sie wird nur angezeigt, wenn noch keine Prüfungen von diesem Checkpoint erfolgt sind.
 

## Den eigenen privaten Standort überwachen
### Zusätzliche Prüfobjekte in deinem Account

Es ist wichtig, sicherzustellen, dass es immer einen verfügbaren privaten Checkpoint in deinem Account gibt, um die Prüfungen an deinem privaten Standort auszuführen. Wenn keine Checkpoints verfügbar sind, kann Uptrends keine Störungen an deinen Standorten identifizieren. Das heißt: Können Prüfungen nicht ausgeführt werden, wird es keine Warnmeldungen geben, da sie auch keine Fehler melden können.

Damit du über Störungen bei deinem privaten Checkpoint-Netzwerk alarmiert werden kannst, werden die folgenden Prüfobjekte eingerichtet. Bitte [erstelle eine Meldedefinition]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}), sodass die zuständigen Personen informiert werden können, wenn ein privater Checkpoint ausfällt.

| **Prüfobjektname**                                      | **Typ**       |
|-------------------------------------------------------|----------------|
| "checkpoint `<name of the first checkpoint>` health"  | Multi-Step API |
| "checkpoint `<name of the second checkpoint>` health" | Multi-Step API |
| "region `<name of the private location>` health"      | Multi-Step API |

### Neue Prüfobjekte hinzufügen 

Wenn du Prüfobjekte zu deinem Uptrends Account hinzufügst, achte darauf, sie auch in deiner Firewall zu konfigurieren.