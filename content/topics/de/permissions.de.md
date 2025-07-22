{
  "hero": {
    "title": "Berechtigungen"
  },
  "title": "Berechtigungen",
  "summary": "Die Mitglieder deines Teams füllen unterschiedliche Rollen und Verantwortungsbereiche aus. Wie verhält sich das zu den Operatoren in der Uptrends Anwendung?",
  "url": "/support/kb/account/nutzer/operatoren/berechtigungen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/permissions"
}

{{< callout >}} Die Verfügbarkeit von Berechtigungstypen hängt von deinem Abonnement ab. Das heißt, einige Typen stehen eventuell in deinem Account nicht bereit. Alle Berechtigungen stehen bei Accounts der **Stufe Enterprise** zur Verfügung.{{< /callout >}}


Nutzer von Uptrends werden in der Anwendung als Operatoren bezeichnet. Ein Operator verfügt über ein Nutzerprofil mit Kontaktinformationen, persönlichen Einstellungen und weiteren Angaben.
Operatoren gehören zu einer oder mehreren Operator-Gruppen. Weitere Infos zu diesem Thema findest du im Artikel [Operatoren und Operator-Gruppen]({{< ref path="support/kb/account/users/operators/operator-groups" lang="de" >}}).

Operatoren füllen unterschiedliche Rollen und Verantwortungsbereiche aus. Daher benötigen sie unterschiedliche Berechtigungen innerhalb der Uptrends Anwendung. Ein Beispiel ist die Administrator-Rolle, bei der der Operator Zugriff auf alles hat. Andere Operatoren benötigen nur Zugang zu bestimmten Produkten oder Prüfobjekten. Oder du möchtest einfach beschränken, wer Einblick in Daten erhält oder Einstellungen ändern darf.

Die Uptrends Anwendung verfolgt zwei Ansätze in Bezug auf Berechtigungen: systemweite (oder globale) Berechtigungen, die an Operator-Gruppen oder Operatoren gekoppelt sind, und an bestimmte Funktionen gekoppelte Berechtigungen. Um die Einrichtung zu vereinfachen, können sowohl systemweite als auch funktionsbasierte Berechtigungen auf der Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} eines Operators oder einer Operator-Gruppe eingestellt werden.

Darüber hinaus können [funktionsbasierte Berechtigungen]({{< ref path="#item-based-permissions" lang="de" >}}) bei der Funktion (Prüfobjekt, Meldedefinition usw.) direkt gesetzt werden.

Unabhängig davon, wo du die Berechtigungen setzt, werden sie an anderen entsprechenden Stellen angezeigt.

## Wer kann Berechtigungen verwalten?
Nur Operatoren mit Administrator-Rechten können Berechtigungen ändern. Der Operator muss Mitglied der Operator-Gruppe *Administrator* sein, bei der die *Administrator-Berechtigungen* Standard und erforderlich sind. Bei Enterprise Accounts, können [Operatorberechtigungen (oder für Gruppen)]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="de" >}}) eingerichtet werden, um Operatoren und Operator-Gruppen Rechte zuzuweisen.

## Berechtigungen verwalten

Wir empfehlen, Berechtigungen auf Ebene der Operator-Gruppe zu handhaben. Technisch kannst du auch einzelnen Operatoren Berechtigungen gewähren. Meistens wird es aber einfacher sein, einen Operator einer Operator-Gruppe zuzuweisen, die bereits über Berechtigungen verfügt, statt einem Operator alle Berechtigungen einzeln zuweisen zu müssen.

Die Vorgänge, Berechtigungen zu gewähren und aufzuheben, sind gleich. Die Schritte für Operator-Gruppen werden nachfolgend beschrieben.

Folge diesen Schritten, um Berechtigungen zu gewähren:

1. Rufe den [Nutzer-Management-Hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="de" >}}) auf, indem du im Menü auf {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator und Gruppen {{< /AppElement >}} klickst. Klicke dann auf {{< AppElement type="buttonPrimary" >}} Alle Operator Gruppen anzeigen {{< /AppElement >}}, um die vollständige Übersicht der Operator-Gruppen deines Accounts anzuzeigen.
2. Wähle die Gruppe, der du Berechtigungen erteilen möchtest.
  Die Berechtigungen sind über die Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}} auf der Seite der *Operator Gruppe* zu finden.
3. Wähle die **systemweiten Berechtigungen**, die du zuweisen oder entfernen möchtest, indem du die entsprechenden Kontrollkästchen markierst oder deren Markierung aufhebst.
![Berechtigungen Operator-Gruppen](/img/content/scr_operatorgroup-permissions-091624.min.png)
4. Richte die [funktionsbasierten Berechtigungen]({{< ref path="#item-based-permissions" lang="de" >}}) für Prüfobjekte und Meldedefinitionen usw. ein.
5. Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die Änderungen zu sichern.

## Berechtigungstypen

Alle Berechtigungstypen sind, sofern nicht anders angegeben, auf Operator- und Operator-Gruppen-Ebene verfügbar. Einige Berechtigungen sind zwingend erforderlich. Infos hierzu findest du unten in den Beschreibungen zu den Berechtigungen.

### Basic Operator {id="basic-operator"}

Diese Berechtigung wird jedem neuen Operator standardmäßig zugewiesen und ist nicht bei den Einstellungen der Operator-Gruppe sichtbar.

Die Berechtigung ermöglicht das Anmelden bei der Uptrends Anwendung und das Anzeigen von Prüfobjekten und Dashboards.

Nur ein Administrator im Rahmen eines Enterprise Abos kann diese Berechtigung gewähren oder entfernen und sie kann bei einem einzelnen Operator und bei Operator-Gruppen gesetzt werden.
Sobald diese Berechtigung entfernt wurde, kann der Operator sich nur anmelden und eine [geschützte Statusseite]({{< ref path="/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages#protected-status-pages" lang="de" >}}) aufrufen. Er kann keine weiteren Aktionen mehr ausführen.

### Administrative Rechte

Diese Berechtigung ist erforderlich für die Standard-Operator-Gruppe *Administratoren* und kann keiner anderen Operator-Gruppe und keinem einzelnen Operator gewährt werden.

Wenn ein Operator administrative Rechte benötigt, füge ihn der Operator-Gruppe *Administratoren* zu.

### Meldedefinitionen erstellen {id="create-alert-definition"}

Wenn ein Operator (oder eine Operator-Gruppe) über diese Berechtigung verfügt, kann er neue Meldedefinitionen einrichten. Beachte, dass es auch die damit zusammenhängende Berechtigung [Meldedefinition bearbeiten]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="de" >}}) gibt, die bei der Meldedefinition selbst gesetzt wird, nicht auf Ebene der Operatoren oder Operator-Gruppen.

Wenn du eine Meldedefinition erstellt hast, verfügst du automatisch über die Berechtigung **Meldedefinition bearbeiten** für diese Definition. Das soll sicherstellen, dass du bei der späteren Verwaltung Änderungen an dieser Meldedefinition vornehmen kannst.

Die Kombination der Berechtigungen **Meldedefinitionen erstellen** und **Meldedefinition bearbeiten** gestattet dir auch, Berechtigungen der Meldedefinition zu ändern. Auf diese Weise kannst du deine eigenen Meldedefinitionen mit anderen Operatoren teilen.

Administratoren verfügen standardmäßig über die Berechtigung **Meldedefinitionen erstellen**.

### Erstelle Integrationen {id="create-integration"}

Diese Berechtigung erlaubt dir, allgemein Integrationen zu erstellen. Sobald du eine Integration erstellt hast, erhältst du automatisch die Berechtigung [Integration bearbeiten]({{< ref path="support/kb/alerting/integrations/integrations-permissions#edit-integration" lang="de" >}}) für diese Integration. Somit kannst du später diese Integration verwalten.

Administratoren verfügen standardmäßig über die Berechtigung **Erstelle Integrationen**.

### Ansprechpartner Finanzen {id="financial-operator"}

Ein Operator mit dieser Berechtigung kann Bestellungen aufgeben, Rechnungen einsehen und Zahlungen vornehmen.
Dieser Operator wird benachrichtigt, wenn das Abonnement für den Account abläuft oder das SMS-Credits-Limit erreicht ist. Er erhält zudem eventuell Zahlungserinnerungen.

Es ist zwingend erforderlich, mindestens über einen Operator in deinem Uptrends Account zu verfügen, der diese Berechtigung hat. Sie ist standardmäßig der Operator-Gruppe *Administratoren* zugewiesen.
### Infra Zugriff

Wenn du Uptrends Infra abonniert hast, kannst du Operatoren Zugriff zu diesem Produkt gewähren.

Diese Berechtigung ist zwingend erforderlich für die Standard-Operator-Gruppe *Administratoren*.
### Technischer Ansprechpartner

Diese Berechtigung wird für den Operator gesetzt, der bei technischen Problemen kontaktiert werden soll.

Es ist zwingend erforderlich, mindestens über einen Operator zu verfügen, der den Berechtigungstyp *Technischer Ansprechpartner* hat. Zusätzliche Operatoren mit der Berechtigung für technische Ansprechpartner können hinzugefügt und entfernt werden, sofern mindestens ein Operator über diesen Berechtigungstyp verfügt.

### Private Standorte verwalten {id="manage-private-locations"}

Operatoren mit der Berechtigung *Private Standorte verwalten* können im Account neue oder bestehende [private Standorte]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) erstellen, verwalten oder löschen. Damit Operatoren einen privaten Standort erstellen können, benötigen sie Zugriff auf mindestens eine [Prüfobjektgruppe]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="de" >}}) mit der Berechtigung zum *Erstellen und Löschen von Prüfobjekten in der Gruppe*.
Die Berechtigung *Private Standorte verwalten* ist standardmäßig der Operator-Gruppe *Administratoren* zugewiesen.

### Prüfobjekt Vorlagen verwalten {id="manage-monitor-templates"}

Operatoren mit der Berechtigung *Prüfobjekt Vorlagen verwalten* können [Prüfobjektvorlagen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="de" >}}) bei denjenigen Prüfobjekten verwalten und anwenden, bei denen sie über Bearbeitungsrechte verfügen, und benötigen keine zusätzlichen administrativen Berechtigungen.

## Funktionsbasierte Berechtigungen {id="item-based-permissions"}

Die folgenden Berechtigungen werden bei der Funktion gesetzt, z. B. der Integration oder dem Prüfobjekt, während systemweite Berechtigungen global gesetzt werden.

- [Meldedefinitionen]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="de" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="de" >}})
- [Integrationen]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="de" >}})
- [Prüfobjekte]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="de" >}})
- [Operatoren und Operator-Gruppen]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="de" >}})