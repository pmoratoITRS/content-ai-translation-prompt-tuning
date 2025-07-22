{
  "hero": {
    "title": "Berechtigungen für Operatoren und -Gruppen setzen"
  },
  "title": "Berechtigungen für Operatoren und -Gruppen setzen",
  "url": "/support/kb/account/users/operators/operator-berechtigungen",
  "summary": "Ein Überblick zur Einrichtung von Operator-Berechtigungen für deine Operatoren und Operator-Gruppen.",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-permissions"
}

{{< callout >}}Operator-Berechtigungen stehen nur bei **Enterprise** Accounts zur Verfügung.{{< /callout >}}

**Berechtigungen für Operatoren(-Gruppen)** sind Berechtigungen, die Operatoren und Operator-Gruppen mehr Kontrolle und Flexibilität gewähren. Mit diesen Berechtigungen können Administratoren bestimmte Zugriffslevel einrichten, anhand derer Operatoren oder Operator-Gruppen andere Operatoren anzeigen, erstellen (oder hinzufügen) sowie auch löschen oder die Einstellungen bearbeiten können. Somit sind diese Privilegien nicht mehr nur auf Administratoren beschränkt, sondern können auch anderen Operatoren und Operator-Gruppen zugewiesen werden, sofern sie die Berechtigung erhalten haben. Ähnlich kannst du diese Berechtigungen des Anzeigens, Erstellens, Bearbeitens und Löschens an Nicht-Administrator-Accounts vergeben.

Standardmäßig wurden zwei Haupt-[Operator-Gruppen]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="de" >}}) in deinem Uptrends Account eingerichtet: Administratoren und Jeder. Die *Administrator-Gruppe* bezieht sich auf Operatoren, die über eine volle Zugriffsberechtigung verfügen und alles in deinem Uptrends Account verwalten können. Die *Gruppe Jeder* bezieht sich auf alle Operatoren, die dem Account hinzugefügt wurden. Jeder verfügt automatisch über die Berechtigung *alle Operatoren anzeigen* zu können, sodass jeder alle anderen Operatoren, auch Nicht-Administratoren sehen kann.

Es gibt jedoch Fälle, in denen du die uneingeschränkte Sicht der *Gruppe Jeder* aus Datenschutz- und Sicherheitsgründen begrenzen solltest. Beispielsweise sollen nur autorisierte Operatoren Zugang zu den sensiblen Daten deines Unternehmens haben, aber du hast auch Auftragnehmer oder andere Externe eingeladen, Mitglied deines Uptrends Teams zu sein. Um Angreifbarkeit und mögliche Risiken zu vermeiden, ist es besser, diese Dinge getrennt zu halten und öffentlichen Zugang zu beschränken. Anhand der **Operator-Berechtigungen** kannst du die Standardeinstellungen aus der *Gruppe Jeder* so entfernen, dass die Berechtigung der *Sichtbarkeit auf jeden* nicht mehr gilt.

Kurz gesagt, **Operator-Berechtigungen** sind praktisch, um die Sichtbarkeit und die Zugriffsmöglichkeiten deiner Operatoren und Operator-Gruppen zu steuern. Indem du diese Berechtigungen setzt, können Teams effektiv zusammenarbeiten und bestimmte Gruppenaufgaben wie Weitergabe von Dashboard-Daten, Definieren von Alarmierungen, Planen von Berichten usw. ausführen. Genauso können Teams eigenständig Management-Aufgaben mit verstärkter Sicherheit, Flexibilität und Kontrolle in deinem Unternehmen ausführen.

![Operator-Berechtigungen für die Gruppe Jeder und Operatoren, die nicht Administratoren sind](/img/content/scr-everyone-operator-permissions.min.png)

## Berechtigungen für Operatoren und Operator-Gruppen setzen
Operatoren-Berechtigungen können individuell unter **Operatoren** oder für mehrere über **Operator-Gruppen** eingestellt werden. Die Mitglieder einer Operator-Gruppe erhalten automatisch die Berechtigungseinstellungen.

{{< callout >}} Alle Mitglieder der Administratoren-Operator-Gruppe können Operatoren anzeigen, erstellen und bearbeiten sowie neue Operatoren zu jeder Gruppe hinzufügen. {{< /callout >}}

## Zugriffsberechtigungen
Es gibt vier Stufen von Zugriffsberechtigungen, die du bei jedem Operator und/oder jeder Operator-Gruppe setzen kannst.
- Kein Zugriff: Operator und/oder Operator-Gruppe haben keine besonderen Berechtigungen. Um die Sichtbarkeit von Operatoren(-Gruppen) gegenüber anderen zu beschränken, muss zunächst die Standardsichtbarkeit der *Gruppe Jeder* entfernt werden.
- Operatoren sehen: Gestattet Operatoren, die Operator-Gruppe und die Operatoren in der Gruppe anzuzeigen.
- Einstellungen bearbeiten: Gestattet Operatoren, die Einstellungen für jeden Operator in der Gruppe zu bearbeiten.
- Erstellen und Löschen: Gestattet Operatoren, Operatoren in der Gruppe zu erstellen und zu löschen.

### Berechtigungen über Operatoren setzen

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="button" >}} Alle Operatoren anzeigen {{< /AppElement >}}.
3. Wähle den Namen des Operators, dem du Berechtigungen erteilen möchtest.
4. Unter der Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} siehst du den Bereich *Operator-Berechtigungen*. Füge die Operatoren durch Auswahl über das Drop-down-Menü hinzu und setze die Berechtigungen anhand des Schiebereglers. Um Berechtigungen zu entfernen oder eine komplette Zeile zu löschen, klicke auf das *X*-Symbol.
![Einstellungen Operator-Berechtigungen](/img/content/scr-operator-permissions.min.png)
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite, um die Änderungen zu bestätigen.

### Berechtigungen über Operator-Gruppen setzen

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="button" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}.
3. Wähle den Namen der Operator-Gruppe, der du Berechtigungen erteilen möchtest.
4. Unter der Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} siehst du den Bereich *Operator-Berechtigungen*. Füge die Operator-Gruppen durch Auswahl über das Drop-down-Menü hinzu und setze die Berechtigungen anhand des Schiebereglers. Um Berechtigungen zu entfernen oder eine komplette Zeile zu löschen, klicke auf das *X*-Symbol.
![Einstellungen der Berechtigungen für Operator-Gruppen](/img/content/scr-operator-group-permissions.min.png)
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite, um die Änderungen zu bestätigen.

{{< callout >}} **Hinweis**: Die Berechtigungsstufe, die über die **Operator-Berechtigungen** konfiguriert wird, wirkt sich auch an anderen Stellen der Anwendung aus, an denen Operatoren ausgewählt werden können, zum Beispiel bei den *Meldedefinitionen* und *Geplanten Berichten*. Die Sichtbarkeit jedes Operators oder jeder Operator-Gruppe variert abhängig von den gesetzten Einstellungen.
