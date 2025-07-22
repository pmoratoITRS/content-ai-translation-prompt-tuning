{
  "title": "Neu: Berechtigungen bei Private Locations",
  "date": "2025-01-29",
  "url": "/changelog/januar-2025-private-locations-berechtigungen",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-private-locations-permissions"
}

[Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="de" >}}) bzw. private Standorte ermöglichen das Ausführen von Prüfobjekten (intern) innerhalb deiner Server- und Firewall-Umgebung, statt auf den üblichen [öffentlichen Uptrends Checkpoints]({{< ref path="/checkpoints" lang="de" >}}).

Standardmäßig haben alle Operatoren Zugriff auf alle privaten Standorte. Operatoren können jederzeit einen Checkpoint erstellen, aktualisieren, deaktivieren und löschen. Es ist wichtig, den Grad der Sichtbarkeit und die Berechtigungen von Operatoren zu verwalten.

Mit der neuen Funktion **Private Locations verwalten** kannst du Berechtigungen für bestimmte Operator und Operator-Gruppen setzen:

- Erstellen – erlaubt Operatoren und Operator-Gruppen, auf private Standorte zuzugreifen und sie zu erstellen.
- Bearbeiten – erlaubt Operatoren und Operator-Gruppen, auf private Standorte zuzugreifen, sie zu bearbeiten und zu löschen.
- Verwenden – erlaubt Operatoren und Operator-Gruppen, den privaten Standort als Checkpoint auszuwählen und Prüfobjekte auszuführen.

Wenn ein Operator eine dieser Berechtigungen hat, ist der private Standort auf dem Tab {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} eines Prüfobjekts sichtbar, und er kann darauf über das Menü unter {{< AppElement type="menuitem" >}} Private Locations {{< /AppElement >}} zugreifen.

![GIF Private Locations-Berechtigungen](/img/content/gif-private-locations-permissions.gif)