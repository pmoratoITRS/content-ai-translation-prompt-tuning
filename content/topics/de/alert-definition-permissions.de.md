{
  "hero": {
    "title": "Berechtigungen für Meldedefinitionen"
  },
  "title": "Berechtigungen für Meldedefinitionen",
  "summary": "",
  "url": "/support/kb/alarme/meldedefinition-berechtigungen",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-definition-permissions"
}

Meldedefinitionen bei Uptrends definieren, wann Alarme zu welcher Eskalationsstufe generiert und welche Benachrichtigungen an Operatoren oder Systeme anhand von Integrationen gesendet werden. Die Meldedefinitionen sind für dein Monitoring und die Alarmierung von grundlegender Bedeutung und du solltest daher steuern können, wer sie ändern darf. Mit den Berechtigungen für Meldedefinitionen hast du diese Kontrolle.

Berechtigungen werden an zwei Orten eingerichtet: Die Berechtigung **Meldedefinition bearbeiten** wird bei einer Meldedefinition eingerichtet und die Berechtigung **Meldedefinitionen erstellen** wird für einen Operator oder eine Operator-Gruppe gesetzt. Es ist die Funktionsweise des Uptrends Berechtigungssystems: Einige Berechtigungen werden für eine Funktion (wie ein Prüfobjekt oder eine Meldedefinition) gesetzt und einige Berechtigungen werden auf Operator- oder Operator-Gruppen-Ebene gesetzt.

Die Berechtigungen, die bei einer Meldedefinition gesetzt werden, werden in diesem Artikel beschrieben. Weitere Infos zur Berechtigung **Meldedefinitionen erstellen**, die sich auf Operatoren bezieht, findest du im Knowledge-Base-Artikel [Berechtigungen]({{< ref path="support/kb/account/users/operators/permissions#create-alert-definition" lang="de" >}}).

## Wer kann Berechtigungen verwalten?

Die Berechtigungen für Meldedefinitionen können im Allgemeinen von Administratoren gesetzt und geändert werden.
Zudem kann ein Operator mit den beiden Berechtigungen **Meldedefinitionen erstellen** (für einen Operator oder eine Operator-Gruppe eingestellt) und **Meldedefinition bearbeiten** (für eine Meldedefinition gesetzt) die Berechtigungen für diese eine Meldedefinition verwalten.

## Berechtigungstypen

### Meldedefinition bearbeiten

Diese Berechtigung berechtigt den Operator oder die Operator-Gruppe, eine Meldedefinition zu ändern.

Einige Aspekte müssen berücksichtigt werden:

- Der Operator kann die Meldedefinition ändern und Prüfobjekte und Prüfobjektgruppen hinzufügen oder entfernen. Dies gilt für alle Prüfobjekte, die der Operator gemäß den [Prüfobjektberechtigungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}}) für diesen Operator anzeigen kann. Besitzt der Operator nicht die Anzeigeberechtigung für ein bestimmtes Prüfobjekt (oder eine Prüfobjektgruppe), kann er das Prüfobjekt oder die Gruppe nicht in der Meldedefinition auswählen.

- Der Operator kann die Meldedefinition ändern und Operatoren oder Operator-Gruppen hinzufügen oder entfernen. Dies gilt nur für Operatoren oder Operator-Gruppen, für die der bearbeitende Operator Anzeigerechte besitzt.

- Es ist möglich, dass andere Operatoren Prüfobjekte oder Prüfobjektgruppen hinzufügen, die du nicht sehen kannst, weil du nicht über die Anzeigeberechtigung verfügst. Das Gleiche gilt für Operatoren und Operator-Gruppen. Wenn verborgene Funktionen mit der Meldedefinition verknüpft sind, wird dazu ein Hinweis angezeigt.

- Die Berechtigung Meldedefinition bearbeiten umfasst das Recht, die Definition zu löschen. Das geht nur, wenn es keine Elemente (Prüfobjekte/Prüfobjektgruppen oder Operatoren/Operator-Gruppen) gibt, die zwar mit der Definition verknüpft, aber nicht für dich sichtbar sind, weil du keine Anzeigeberechtigung besitzt.

## Berechtigungen verwalten

Die Berechtigungen für Meldedefinitionen können entweder bei der Meldedefinition oder bei einer Operator-Gruppe gesetzt werden. Jede Änderung, die an der einen Stelle vorgenommen wird, wird an der anderen übernommen.
### Berechtigungen über die Einstellungen der Operator-Gruppe setzen

1. Rufe {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} auf.
2. Klicke auf {{< AppElement type="buttonPrimary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}, um die vollständige Übersicht der Operator-Gruppen deines Accounts anzuzeigen.
3. Wähle die Gruppe, der du Berechtigungen hinzufügen möchtest und öffne die Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
![screenshot operator group permissions tab](/img/content/scr_alert-definition-permissions-operatorgroups.min.png)
4. Füge im Abschnitt **Berechtigungen für Meldedefinitionen** eine Meldedefinition hinzu, indem du sie aus der Drop-down-Liste auswählst. Um eine Meldedefinition von der Operator-Gruppe zu entfernen, klicke auf das x neben dem Namen der Definition.
5. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um die Änderungen zu sichern.

### Berechtigungen bei der Meldedefinition setzen oder ändern

1. Rufe {{< AppElement type="menuitem" >}}Alarmierung > Meldedefinitionen {{< /AppElement >}} auf.
2. Klicke in der Liste der Meldedefinitionen auf die Definition, die du ändern möchtest.
3. Öffne die Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
4. Klicke auf {{< AppElement type="buttonPrimary" >}} Berechtigung hinzufügen {{< /AppElement >}}.
5. Wähle aus dem Pop-up-Fenster die Operator-Gruppe und die Berechtigung, klicke dann auf {{< AppElement type="buttonPrimary" >}} Hinzufügen {{< /AppElement >}}.
6. Um eine Berechtigung zu entfernen, wähle {{< AppElement type="deletebutton" >}} Löschen {{< /AppElement >}} in der Liste unter **Berechtigungen**.
7. Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die Änderungen zu sichern.
