{
  "hero": {
    "title": "Einrichten eines Teams in deinem Account"
  },
  "title": "Einrichten eines Teams in deinem Account",
  "summary": "Dieser Artikel beschreibt, wie du ein neues eigenständiges Team in deinem Uptrends Account einrichtest.",
  "url": "/support/kb/account/berechtigungen/einrichten-eines-teams",
  "translationKey": "https://www.uptrends.com/support/kb/permissions/how-to-team-setup"
}

Das Ziel ist die Einrichtung eines neuen eigenständigen Teams in deinem Uptrends Account. Die Schritte zur Einrichtung sind wie folgt:

- Erstellen einer neuen Operator-Gruppe
- Erstellen einer neuen Prüfobjektgruppe und Zuweisen von Berechtigungen
- Zuweisen von Alarmierungs- und Integrationsberechtigungen
- Gewähren des Zugriffs nur auf relevante Prüfobjekte
- Zuweisen bestimmter Prüfobjekt-Berechtigungen

**Tipp**: Nutze das Inhaltsverzeichnis unter "In diesem Artikel:" (links), um schnell zu einem der Schritte zu springen.

{{< callout >}} **Hinweis**: Du musst Administrator sein, um alle Schritte dieser Einrichtung auszuführen. {{< /callout >}}

## Erstellen einer neuen Operator-Gruppe

Um eine neue Gruppe zu erstellen:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke im Abschnitt "Du hast x Operator Gruppen" auf {{< AppElement type="buttonSecondary" >}} Operator Gruppe hinzufügen {{< /AppElement >}}.
3. Gib auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} unter **Beschreibung** einen Namen für die Operator-Gruppe ein. In diesem Beispiel ist das „Team A“.
4. Füge alle bereits in deinem Account eingerichteten Operatoren, die Teil des Teams sein sollen, zu der Operator-Gruppe hinzu. Aktiviere einfach das Kontrollkästchen vor dem Namen eines Operators, um ihn hinzuzufügen.
Sind die Operatoren noch nicht in deinem Account eingerichtet, ist das kein Problem: Du kannst sie auch später hinzufügen.
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

Die neue Operator-Gruppe „Team A“ wurde nun erstellt und mit ihr sind einige Operatoren verknüpft.

## Erstellen einer Prüfobjektgruppe und Zuweisen von Berechtigungen

Da „Team A“ neu ist, hat es keine Berechtigungen für andere Prüfobjektgruppen und die Mitglieder von „Team A“ können nur neue Prüfobjekte erstellen, die Teil von „Monitors A“ sein werden. Daher musst du (als Administrator) sicherstellen, dass bereits bestehende Prüfobjekte zur Prüfobjektgruppe "Monitors A" hinzugefügt wurden, wie unter [Die Prüfobjektgruppe erstellen](#create-monitor-group) erläutert. Es ist das Einzige, was das Team nicht selbst durchführen kann.

### Die Prüfobjektgruppe erstellen {id="create-monitor-group"}

Der nächste Schritt besteht im Erstellen einer neuen Prüfobjektgruppe, die von dem neuen Team verwaltet wird.

1. Gehe im Menü zu {{< AppElement type="menuitem" >}} Accounteinstellungen > Prüfobjektgruppen {{< /AppElement >}}.
2. Klicke auf {{< AppElement type="button" >}} Prüfobjektgruppe hinzufügen {{< /AppElement >}} oben rechts.
3. Gib unter **Beschreibung** einen Namen für die Prüfobjektgruppe ein. In diesem Beispiel ist das „Monitors A“.
4. Wähle aus der Liste **In dieser Gruppe enthaltene Prüfobjekte** die Prüfobjekte, die zur Gruppe hinzugefügt werden sollen. Erweitere die Liste und aktiviere die Kontrollkästchen vor dem Namen eines Prüfobjekts.
   Wurden die Prüfobjekte noch nicht eingerichtet, kannst du oder das neue Team sie später hinzufügen.
5. (Optional) Lege die Höchstzahl der Prüfobjekte (nach Typ) fest, die es in der Prüfobjektgruppe geben kann. Wenn du die Anzahl der Prüfobjekte in der Gruppe nicht begrenzen möchtest, aktiviere **Unbegrenzte Anzahl an Prüfobjekten erlauben**. Beachte, dass niemals mehr Prüfobjekte in einer Gruppe sein können, als in deinem Account verfügbar sind (siehe {{< AppElement type="menuitem" >}} Accounteinstellungen > Account Einstellungen > Abonnement {{< /AppElement >}}, um zu sehen, wie viele du hast). Prüfobjekte können jedoch mehr als einer Gruppe zugeordnet sein.
6. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

Die neue Prüfobjektgruppe „Monitors A“ mit mehreren Prüfobjekten ist jetzt verfügbar.

### Zuweisen von Berechtigungen 

Jetzt hast du eine Operator-Gruppe „Team A“ und eine Prüfobjektgruppe „Monitors A“. Allerdings können die Mitglieder von „Team A“ noch nicht die Prüfobjekte der Prüfobjektgruppe „Monitors A“ verwalten.

Um das zu ermöglichen, musst du die entsprechenden Berechtigungen zuweisen. Führe dazu die folgenden Schritte aus:

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}.
3. Wähle die Operator-Gruppe „Team A“.
4. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
5. Wähle im Bereich **Prüfobjektberechtigungen** in der Liste die Prüfobjektgruppe „Monitors A“.
![Screenshot Prüfobjektberechtigung für Team hinzufügen](/img/content/scr-add-monitor-to-team.min.png)
6. Bewege den Schieberegler in der Zeile von "Monitors A" auf *Erstellen und löschen*.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.


Du hast nun der Operator-Gruppe „Team A“ die Möglichkeit gegeben, neue Prüfobjekte zu erstellen.

Von nun an ist kein (allgemeiner) Administrator mehr erforderlich, um alle neuen Prüfobjekte für das Team zu erstellen. „Team A“ kann jetzt selbst alle eigenen Prüfobjekte verwalten und bei Bedarf neue Prüfobjekte erstellen.

## Zuweisen von Alarmierungs- und Integrationsberechtigungen

Mit einer Operator-Gruppe und einer Prüfobjektgruppe kann „Team A“ den Grundstein für das Monitoring legen. Ein wichtiger Teil des Monitorings ist jedoch die Alarmierung, um sicherzustellen, dass Operatoren benachrichtigt und dass bei Problemen schnell Maßnahmen ergriffen werden. Zu diesem Zweck muss das Team Meldedefinitionen und Integrationen erstellen und/oder verwalten können. Da dies die Einrichtung eines eigenständigen Teams ist, gewährst du „Team A“ die Berechtigungen, sich komplett selbst zu verwalten.

Um „Team A“ die Berechtigungen für Meldedefinitionen und Integrationen zu geben:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke im Abschnitt "Du hast x Operator Gruppen" auf {{< AppElement type="buttonSecondary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}.
3. Klicke auf die Operator-Gruppe „Team A“.
4. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
5. Wähle im Abschnitt **Systemweite Berechtigungen** die Berechtigungen **Meldedefinitionen erstellen** und **Erstelle Integrationen**.
6. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten links auf der Bildschirmseite.

„Team A“ hat nun die Berechtigung, Meldedefinitionen und Integrationen zu erstellen.

### Berechtigungen für bestehende Alarmierungen zuweisen

Mit den neu hinzugefügten Berechtigungen kann das Team eigene Meldedefinitionen und Integrationen erstellen, die das Team braucht. Es werden keine Aktionen seitens eines Administrators benötigt, um die Alarmierungen des Teams zu verwalten. Aber vielleicht solltest du dem Team Zugriff auf Meldedefinitionen und Integrationen geben, die vor der Einrichtung des Teams in deinem Account bestanden haben. Dies ist eine Aufgabe für einen Administrator.

Um „Team A“ einer bestehenden Meldedefinition zuzuweisen:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke im Abschnitt "Du hast x Operator Gruppen" auf {{< AppElement type="buttonSecondary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}.
3. Klicke auf die Operator-Gruppe „Team A“.
4. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
![Screenshot Operator-Gruppe – Berechtigungen](/img/content/scr_team-setup-alertdefinition-permissions.min.png)
5. Verwende im Abschnitt **Berechtigungen für Meldedefinitionen** das Drop-down-Menü, um alle bestehenden Meldedefinitionen auszuwählen und hinzuzufügen, die „Team A“ verwalten können sollte.
6. Hast du versehentlich eine Definition hinzugefügt oder wenn „Team A“ nicht länger eine Definition verwalten können soll, klicke auf das x am Ende der Zeile, um die Berechtigung aufzuheben.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.


Um „Team A“ einer bestehenden Integration zuzuweisen:

1. Rufe {{< AppElement type="menuitem" >}}Alarmierung > Integrationen {{< /AppElement >}} auf.
2. Klicke auf die Integration, die „Team A“ nutzen und/oder bearbeiten können sollte.
3. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
4. Klicke auf {{< AppElement type="buttonPrimary" >}} Berechtigung hinzufügen {{< /AppElement >}}.
5. Wähle im Pop-up-Fenster die Operator-Gruppe „Team A“ und die Berechtigung, die du zuweisen möchtest.
   Wähle die Berechtigung **Nutze Integration**, wenn das Team die Integration bei einer Meldedefinition verwenden können soll.
   Wähle **Integration bearbeiten**, wenn das Team die Integration vollständig verwalten soll, einschließlich des Rechts, eine Integration zu löschen.
6. Klicke auf {{< AppElement type="buttonPrimary" >}} Hinzufügen {{< /AppElement >}}.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

Wiederhole die Schritte für alle bestehenden Integrationen, auf die das neue Team Zugriff haben soll.

„Team A“ hat nun die Berechtigung, Meldedefinitionen einzurichten oder zu ändern und kann ihnen Integrationen hinzufügen. Je nach deinen Einstellungen ist es eventuell auch in der Lage, Integrationen zu bearbeiten.

## Zugriff nur auf relevante Prüfobjekte gewähren

{{< callout >}} **Hinweis**: Diese Aktion ist nur beim ersten Mal notwendig, wenn du ein Team in einem Account einrichtest. {{< /callout >}}

Bei dieser Übung richtest du ein eigenständiges Team ein, das sich nur auf die Monitoring-Daten konzentrieren soll, die für das Team relevant sind. Dafür ist ein kleiner Trick erforderlich, denn:

In einem Uptrends Account gibt es immer die Operator-Gruppe „Jeder“. Alle Operatoren deines Accounts sind Mitglied der Gruppe „Jeder“ und haben standardmäßig Zugriff auf alle Monitoring-Daten aller Prüfobjekte. Du kannst die Gruppe „Jeder“ nicht löschen und du kannst keine Operatoren aus dieser Gruppe entfernen.

Der Trick besteht darin, die Operatoren aus der Gruppe „Jeder“ in die (bestehende) Gruppe „Team A“ und eine neue Gruppe „Main operators“ aufzuteilen.

Du kannst dann der Gruppe „Jeder“ die Berechtigung, alle Daten anzuzeigen, entziehen und die Berechtigungen für die einzelnen Gruppen („Team A“, „Main operators“) nach Wunsch zuweisen.

Erstelle zunächst eine neue Operator-Gruppe „Main operators“:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke im Abschnitt "Du hast x Operator Gruppen" auf {{< AppElement type="buttonSecondary" >}} Operator Gruppe hinzufügen {{< /AppElement >}}.
3. Gib auf der Registerkarte {{< AppElement type="tab" >}} Allgemein {{< /AppElement >}} unter **Beschreibung** einen Namen für die Operator-Gruppe ein. Verwende hier „Main operators“.
4. Füge alle Operatoren hinzu, die nicht Mitglied des neuen Teams („Team A“) sind. Aktiviere einfach das Kontrollkästchen vor dem Namen eines Operators, um ihn hinzuzufügen.
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

Ändere dann die Anzeige-Berechtigungen bei der „Alle Prüfobjekte“-Gruppe:

1. Rufe im Menü {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} auf.
2. Klicke im Abschnitt "Du hast x Operator Gruppen" auf {{< AppElement type="buttonSecondary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}.
3. Wähle die Operator-Gruppe „Jeder“.
4. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
5. Entferne im Bereich **Prüfobjektberechtigungen** die Zeile "Alle Prüfobjekte" (Berechtigung *Daten ansehen*), indem du auf das Kreuz am Ende der Zeile klickst.
![Screenshot Anzeigeberechtigungen entfernen](/img/content/scr-remove-view-permission-from-everyone.min.png)
6. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.
7. In der Liste der **Operator Gruppen**: Wähle die Gruppe "Main operators".
8. Gehe zur Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
9. Füge im Abschnitt **Prüfobjektberechtigungen** die Prüfobjektgruppe "Alle Prüfobjekte" mit der Berechtigung *Daten ansehen* hinzu, indem du die Prüfobjektgruppe aus der Liste auswählst und den Schieberegler auf die Berechtigung ziehst.
10. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}} unten auf der Bildschirmseite.

In den oben beschriebenen Schritten hast du den Zugriff auf alle Monitoring-Daten bei „Team A“ entfernt und dann die ursprüngliche Berechtigung, Daten anzuzeigen, an alle anderen Operatoren (Mitglieder der Gruppe „Main operators“) zurückgegeben, die nicht Mitglied von „Team A“ sind.

„Team A“ hat nun eine eingeschränkte Sicht und kann nur Prüfobjekte der Prüfobjektgruppe „Monitors A“ betrachten, während alle anderen Operatoren immer noch wie zuvor die volle Sicht auf alles haben.

Ist ein Operator Mitglied mehrerer Operator-Gruppen, sieht er eventuell mehr, da andere Operator-Gruppen über eigene Berechtigungen verfügen können.

## Zuweisen bestimmter Prüfobjekt-Berechtigungen

Mit den bisherigen Einstellungen verfügst du über ein Team, das eine eigene Prüfobjektgruppe hat, für die es Prüfobjekte erstellen und bearbeiten kann. Es kann zudem Meldedefinitionen und Integrationen erstellen, die es eventuell braucht. Im Wesentlichen ist es eigenständig und benötigt keine Aktionen seitens der Administratoren. Es kann jedoch auch der Fall sein, dass das Team die Monitoring-Daten anderer Teams sehen oder auch die Prüfobjekte anderer Teams bearbeiten muss.

Um dem neuen „Team A“ Zugriff auf andere Prüfobjekte zu geben, weist du die entsprechenden Berechtigungen zu den Prüfobjektgruppen der anderen Teams zu. Gibt es zum Beispiel ein „Team B“ mit einer Prüfobjektgruppe "Monitors B", kannst du die Operator-Gruppe „Team A“ öffnen und auf der Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} im Abschnitt **Prüfobjektberechtigungen** die Prüfobjektgruppe "Monitors B" aus der Liste hinzufügen und „Team A“ die Berechtigung **Daten ansehen** zuweisen, indem du den Schieberegler auf diese Berechtigung ziehst.
Damit ist „Team A“ in der Lage, die Monitoring-Daten von „Team B“ anzuzeigen, kann sie aber nicht bearbeiten. Auf diese Weise können die Teams miteinander kooperieren, während ihr Zugriff beschränkt bleibt.

