{
  "hero": {
    "title": "Einrichten von Berechtigungen für Private Locations"
  },
  "title": "Einrichten von Berechtigungen für Private Locations",
  "summary": "Ein Überblick über die Einrichtung von Berechtigungen für Private Locations bei Operatoren und Operator-Gruppen.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-berechtigungen",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-permissions",
  "sectionlist": false,
  "tableofcontents": false
}

[Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="de" >}}) bzw. private Standorte ermöglichen das interne Ausführen von Prüfobjekten innerhalb deiner Server- und Firewall-Umgebung, statt auf den üblichen [öffentlichen Uptrends Checkpoints]({{< ref path="/checkpoints" lang="de" >}}). Für jeden privaten Standort können Operatoren einen Private Locations-Checkpoint aufrufen, erstellen, aktualisieren, deaktivieren und löschen. Es ist wichtig, den Grad der Sichtbarkeit und Berechtigungen der Operatoren aus Gründen der Sicherheit und des Datenschutzes zu steuern.

Anhand der **Berechtigungen für Private Locations** kannst du Rechte für bestimmte Operatoren und Operator-Gruppen festlegen.

Um Berechtigungen für Private Locations zu verwalten:

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Wähle, für welche Operatoren oder Operator-Gruppen die Private Location-Berechtigungen verwaltet werden sollen.
3. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
4. Wähle unter **Private Location-Berechtigungen** eine der folgenden Optionen:

- **Private Locations erstellen** – aktiviere diese Option, um Operatoren und Operator-Gruppen zu erlauben, private Standorte aufzurufen und zu erstellen.
- **Private Location verwenden** – wähle einen privaten Standort aus dem Drop-down-Menü und ziehe den Schieberegler, um Operatoren und Operator-Gruppen zu erlauben, den privaten Standort als Checkpoint auszuwählen, um Prüfobjekte auszuführen.
- **Private Location bearbeiten** – wähle einen privaten Standort aus dem Drop-down-Menü und ziehe den Schieberegler, um Operatoren und Operator-Gruppen zu erlauben, auf Private Locations zuzugreifen, sie zu bearbeiten und zu löschen. Operatoren mit dieser Berechtigung können den privaten Standort auch als Checkpoint auswählen, um Prüfobjekte auszuführen.

Standardmäßig verfügen alle Administratoren über alle Private Location-Berechtigungen, ohne dass eine weitere Einrichtung erforderlich ist. Operatoren mit den Berechtigungen **verwenden** oder **bearbeiten** können private Standorte auf dem Tab {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} des Prüfobjekts auswählen. Operatoren mit den Berechtigungen **erstellen** oder **bearbeiten** können auf private Standorte über das Menü {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} zugreifen.

![Private Locations-Berechtigungen GIF](/img/content/gif-private-locations-permissions.gif)