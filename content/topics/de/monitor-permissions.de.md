{
  "hero": {
    "title": "Prüfobjektberechtigungen"
  },
  "title": "Prüfobjektberechtigungen",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/pruefobjekt-berechtigungen",
  "summary": "Ein Überblick zur Einrichtung von Prüfobjektberechtigungen für deine Operatoren und Operator-Gruppen.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-permissions"
}

{{< callout >}}Prüfobjektberechtigungen stehen nur bei **Enterprise-Accounts** zur Verfügung.{{< /callout >}}

Standardmäßig sind alle [einfachen Operatoren]({{< ref path="/support/kb/account/users/operators/permissions#basic-operator" lang="de" >}}) deines Accounts in der Lage, Prüfobjektdaten (Dashboards, Statistiken, Prüfergebnisse) für deine gesamten Prüfobjekte anzuzeigen. Sie können jedoch keine bestehenden Prüfobjekte bearbeiten oder löschen oder neue erstellen. Diese Funktionen stehen standardmäßig nur [Administratoren]({{< ref path="/support/kb/account/users/operators/giving-an-operator-administrator-rights" lang="de" >}}) (Operatoren, die Mitglied der Operator-Gruppe *Administratoren* sind) zur Verfügung.

Für eine granularere Kontrolle darüber, welche Operatoren bestimmte Dinge in deinem Account anzeigen oder bearbeiten dürfen, können Nutzer des Enterprise-Abos **Prüfobjektberechtigungen** einrichten. Kurz gesagt sind Prüfobjektberechtigungen Regeln, die für ein bestimmtes Prüfobjekt oder eine Prüfobjektgruppe gelten und die die Zugriffsstufe eines bestimmten Operators oder einer Operator-Gruppe vorgeben.

Dies bezieht sich nur auf Prüfobjekte in deinem Account. Zu **Operator-Berechtigungen** wie etwa die Erlaubnis, Bestellungen aufzugeben, Rechnungen einzusehen oder auf das Uptrends Infra-Abo zuzugreifen, findest du mehr Infos im Artikel zu den [Operator-Berechtigungen]({{< ref path="/support/kb/account/users/operators/permissions" lang="de" >}}).

## Prüfobjektberechtigungen einrichten

Prüfobjektberechtigungen können für [Prüfobjektgruppen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="de" >}}) oder einzelne Prüfobjekte eingerichtet werden. Dies kann über die Einstellungen des Prüfobjekts (bzw. der Gruppe) erfolgen, aber du kannst Prüfobjektberechtigungen auch direkt in den Einstellungen von [Operator-Gruppen]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="en" >}}) setzen.

#### Berechtigungen über die Einstellungen der Operator-Gruppe setzen:

1. Navigiere zum Überblick der [Operator-Gruppen]({{< AppUrl >}}/Report/OperatorGroups) (entweder durch Klicken auf den Link oder über das Menü unter *Accounteinstellungen > Operator, Gruppen und Subaccounts*) und wähle die Operator-Gruppe, der du Prüfobjektberechtigungen zuweisen möchtest.
2. Du findest die Einstellungen der **Prüfobjektberechtigungen** auf der Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
3. Sofern erforderlich, füge die Prüfobjektgruppe oder einzelne Prüfobjekte hinzu, denen du eine Berechtigung zuweisen möchtest.
4. Setze die Berechtigung auf die richtige Stufe anhand des Schiebereglers. (Unten findest du eine Übersicht zu den verfügbaren Berechtigungsstufen).
![Prüfobjektberechtigungen über Operator-Gruppe](/img/content/scr-operator-group-monitor-permissions.min.png)
5. Vergiss nicht, auf {{< AppElement type="savebutton" >}}Speichern {{< /AppElement >}} links unten auf der Bildschirmseite zu klicken!

Im obigen Beispiel können Mitglieder dieser Operator-Gruppe Prüfobjekte für die *Monitor Group A* erstellen und löschen, die Prüfobjektdaten für *Alle Prüfobjekte* des Accounts anzeigen und die Einstellungen eines einzelnen Prüfobjekts namens *Example SSL Cert monitor* bearbeiten.

#### Berechtigungen über die Einstellungen des Prüfobjekts (bzw. der Prüfobjektgruppe) setzen:

1. Navigiere zur [Prüfobjektgruppe]({{< AppUrl >}}/Report/ProbeGroups) oder zum Prüfobjekt, für das du eine Berechtigung einrichten möchtest.
2. Öffne die Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}, um einen Überblick der aktuell vorhandenen Berechtigungen für die Gruppe oder das Prüfobjekt zu erhalten. Die Operator-Gruppe *Administratoren* verfügt immer über die Berechtigung **Erstellen und Löschen der Prüfobjekte der Gruppe**, welche nicht entfernt werden kann. Standardmäßig besitzt die Operator-Gruppe *Jeder* die Berechtigung **Monitoring Daten der Gruppe betrachten**.
3. Um Berechtigungen zu entfernen, klicke rechts auf die entsprechende Schaltfläche. Fahre dann mit Schritt 7 fort.
4. Um eine neue Berechtigung zu erstellen, klicke auf **Berechtigung hinzufügen** oben rechts. Um eine Berechtigung zu bearbeiten, klicke rechts auf die Schaltfläche **Bearbeiten**.
5. Wähle die Berechtigung, die du erteilen möchtest. Dem folgt ein Überblick über die verfügbaren Berechtigungstypen. Wenn du eine neue Berechtigung erstellst, wähle den Operator oder die Operator-Gruppe aus, dem oder der du die Berechtigung erteilen möchtest.
6. Klicke auf **Hinzufügen** oder **Aktualisieren**, abhängig davon, ob du eine neue Berechtigung hinzufügst oder eine bestehende bearbeitest.
7. Vergiss nicht, auf {{< AppElement type="savebutton" >}}Speichern {{< /AppElement >}} links unten auf der Bildschirmseite zu klicken!

### Prüfobjektberechtigungen und die „Alle Prüfobjekte“-Gruppe

Wenn ein neues Prüfobjekt erstellt wird, wird es automatisch zur Gruppe *Alle Prüfobjekte* hinzugefügt (da diese Gruppe per Definition jedes Prüfobjekt des Accounts enthalten muss). Standardmäßig haben reguläre (Nicht-Administrator) Operatoren jedoch nicht die erforderliche Berechtigung, Prüfobjekte in der Gruppe *Alle Prüfobjekte* zu erstellen/löschen. Das heißt, ein Operator ohne die ausdrückliche Berechtigung, in der Gruppe *Alle Prüfobjekte* Prüfobjekte zu erstellen, könnte niemals ein Prüfobjekt erstellen. Um dieses Problem zu vermeiden, wird die Zugehörigkeit zur Gruppe *Alle Prüfobjekte* bei der Erstellung eines neue Prüfobjekts ignoriert, sofern das Prüfobjekt zumindest einer weiteren Gruppe zugeordnet wird.

Nehmen wir zum Beispiel einen Operator an, der über keine Berechtigungen für die Gruppe *Alle Prüfobjekte* verfügt, aber die Berechtigung zum Erstellen/Löschen für die *Monitor Group A* hat. Dieser Operator kann die bestehenden Prüfobjekte in Gruppe A anzeigen und bearbeiten sowie neue Prüfobjekte erstellen, die zu dieser Gruppe gehören. Er kann keine anderen Prüfobjekte außerhalb der *Monitor Group A* anzeigen oder bearbeiten.

Erstellt der Operator ein neues Prüfobjekt, muss er es mindestens einer der Prüfobjektgruppen zuordnen, für die er die notwendigen Berechtigungen besitzt.

![Die Gruppe Alle Prüfobjekte](/img/content/scr-monitor-permissions-all-mons-group.min.png)

Das Prüfobjekt wird mit Zugehörigkeit sowohl zur *Monitor Group A* als auch zur Gruppe *Alle Prüfobjekte* erstellt. Der Operator benötigt nicht die ausdrückliche Berechtigung zum Erstellen/Löschen für die letztgenannte Gruppe.

## Berechtigungstypen {id="permission-types"}

Es gibt die folgenden Berechtigungstypen:

- **Monitoring Daten der Gruppe betrachten**: Operatoren mit dieser Berechtigung können nur Monitoring-Daten für das Prüfobjekt bzw. die Prüfobjektgruppe anzeigen, für die sie gilt. Monitoring-Daten umfassen Dashboards, Statistiken und Prüfergebnisse. Sie umfassen **nicht** die Prüfobjekteinstellungen.
- **Monitoring Einstellungen in Gruppe betrachten**: Diese Berechtigung ermöglicht das Anzeigen der Monitoring-Daten, aber auch der Prüfobjekteinstellungen. Operatoren mit dieser Berechtigung können Prüfobjekteinstellungen für die Prüfobjekte (Prüfobjektgruppe) anzeigen, für die sie gilt, beispielsweise Monitoring-Intervall, Modus, Checkpoint-Auswahl und Wartungszeiträume. Bedenke, dass die Einstellungen mit dieser Berechtigung **nur im Lesemodus** verfügbar sind und nicht bearbeitet werden können.
- **Bearbeite Prüfobjekt Einstellungen in Gruppe**: Mit dieser Berechtigung können Operatoren Änderungen an einzelnen Prüfobjekten oder an Prüfobjekten der Prüfobjektgruppe vornehmen, für die sie gilt. Operatoren mit dieser Berechtigung können zum Beispiel das Prüfobjekt aktivieren oder deaktivieren, das Monitoring-Intervall ändern, die Checkpoint-Auswahl bearbeiten und Wartungszeiträume hinzufügen.
- **Erstellen und Löschen der Prüfobjekte der Gruppe**: Da dies die weitreichendste Berechtigung ist, die vergeben werden kann, werden einem Operator hiermit im Endeffekt Administratorrechte für bestimmte Prüfobjektgruppen gegeben. Sie können neue Prüfobjekte erstellen (wenn auch nur als Mitglied ihrer zugewiesenen Prüfobjektgruppe) und bestehende Prüfobjekte löschen. Diese Berechtigung ist nur für Prüfobjektgruppen verfügbar und kann nicht für einzelne Prüfobjekte vergeben werden.

Zu beachten ist, dass diese Berechtigungen kumulativ sind. Jeder neue Berechtigungslevel enthält alle Berechtigungen der vorherigen. Zum Beispiel kann ein Operator mit der Berechtigung *Monitoring Einstellungen in Gruppe betrachten* automatisch die Monitoring-Daten anzeigen.

![Example-Berechtigungen](/img/content/scr-permissions-example.min.png)

In der Abbildung oben (die sich auf die *Prüfobjektgruppe Example* bezieht) kann die Operator-Gruppe *Jeder* Monitoring-Daten, also Dashboards, Statistiken und einzelne Prüfergebnisse nur anzeigen. Die Operator-Gruppe *Example* kann Monitoring-Daten anzeigen und Einstellungen für bestehende Prüfobjekte innerhalb dieser Gruppe bearbeiten. Die Gruppe *Administratoren* verfügt über die kompletten CRUD-Berechtigungen (Create, Update, Delete) für die Prüfobjekte, die in der *Prüfobjektgruppe Example* enthalten sind, kann also erstellen, aktualisieren und löschen.

## Standard-Prüfobjektgruppe {id="default-monitor-group"}

Jedes Prüfobjekt deines Accounts ist per Definition in der [Prüfobjektgruppe]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="de" >}})  *Alle Prüfobjekte* eingeordnet. Prüfobjekte können nicht von dieser Gruppe entfernt werden. Das ist für viele Fälle nützlich, aber erweist sich eventuell nicht als ideal, wenn du Berechtigungen zuweisen möchtest, je nach deinen Anforderungen.

Alle Berechtigungen, die du der Gruppe Alle Prüfobjekte zuweist, gelten auch für jedes einzelne Prüfobjekt in deinem Account. Aber du möchtest eventuell bestimmte Berechtigungen zu *allen, außer einigen wenigen* Prüfobjekten zuweisen. Wenn zum Beispiel eine bestimmte [Operator-Gruppe]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="de" >}}) die Einstellungen von den meisten Prüfobjekten ändern können soll, außer von einigen besonderen Prüfobjekten, kann die Berechtigung „Bearbeite Prüfobjekt Einstellungen“ nicht zugewiesen werden, da sie dann alle Prüfobjekte bearbeiten könnten, auch diejenigen, die ausgeschlossen sein sollten.

In so einem Fall kannst du eine **Standard-Prüfobjektgruppe** einrichten. Es ist eine benutzerdefinierte Prüfobjektgruppe ähnlich der Gruppe Alle Prüfobjekte. Der Unterschied ist, dass Prüfobjekte aus dieser Gruppe entfernt werden können. Nachdem eine Standard-Prüfobjektgruppe eingerichtet wurde, wird jedes neu erstellte Prüfobjekt automatisch dieser Gruppe zugeordnet (zusätzlich zur Gruppe Alle Prüfobjekte) und erhält daher dieselben Berechtigungen, ohne dass weitere Einstellungen vorgenommen werden müssen.

Alle Berechtigungen, die du allen außer einigen wenigen Prüfobjekten deines Accounts zuweisen möchtest, können der Standard-Prüfobjektgruppe zugewiesen werden (statt der Gruppe Alle Prüfobjekte).

Eine Standard-Prüfobjektgruppe einrichten:

1. Nutze eine bestehende Prüfobjektgruppe oder erstelle eine neue Gruppe.
2. Stelle sicher, dass diese Prüfobjektgruppe alle Prüfobjekte enthält, für die die gewünschte Berechtigung gelten soll. Unsere [MonitorGroup API]({{< ref path="/support/kb/api/monitorgroup-api" lang="de" >}}) kann nützlich sein, um dieser Gruppe mehrere Prüfobjekte auf einmal zuzuweisen.
3. Navigiere im Menü zu deinen Account Einstellungen über {{< AppElement type="menuitem" >}} Accounteinstellungen > Account Einstellungen {{< /AppElement >}}.
4. Wähle aus der Drop-down-Liste unter **Standard Prüfobjektgruppe** die Prüfobjektgruppe.
![Einstellung Standard-Prüfobjektgruppe](/img/content/scr-default-monitor-group.min.png)
5. Klicke auf {{< AppElement type="savebutton" >}} SPEICHERN {{< /AppElement >}}, um die Einstellungen zu sichern.

