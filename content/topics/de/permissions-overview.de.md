{
  "hero": {
    "title": "Übersicht über die Berechtigungen"
  },
  "title": "Übersicht über die Berechtigungen",
  "url": "/support/kb/account/berechtigungen/ubersicht-uber-die-berechtigungen",
  "translationKey": "https://www.uptrends.com/support/kb/permissions/permissions-overview",
  "sectionlist": false
}

Die Uptrends Anwendung arbeitet mit einem Berechtigungssystem, um Operatoren Zugriffsberechtigungen zu erteilen, sodass sie Elemente anzeigen, bearbeiten oder erstellen können, die ihren Rollen bzw. Aufgaben entsprechen.

Im Allgemeinen gibt es zwei Arten von Berechtigungen: **Systemweite Berechtigungen** werden einem Operator (bzw. einer Gruppe) zugewiesen, **Kontext-Berechtigungen** hingegen werden für ein Element gesetzt, sodass der Operator (bzw. die Operator-Gruppe) Zugriff auf dieses bestimmte Element erhält. Beide Arten werden unten detaillierter beschrieben.

 {{< callout >}} Die systemweiten Berechtigungen sind für alle Abonnements verfügbar. Kontext-Berechtigungen stehen nur für Enterprise Accounts bereit. {{< /callout >}}


## Wer kann Berechtigungen verwalten (bearbeiten, zuweisen, entfernen)?

Administratoren (Mitglieder der Operator-Gruppe **Administrator**) können immer Berechtigungen ändern.

Bei Kontext-Berechtigungen können auch Nicht-Administratoren Berechtigungen bearbeiten. Dies hängt jedoch vom Level der Kontext-Berechtigung ab, der ihnen gewährt wurde, zusammen mit einer systemweiten Berechtigung.
Lies die Infos zu den einzelnen [Kontext-Berechtigungen]({{< ref path="#context-permissions" lang="de" >}}), um mehr zu der Funktionsweise zu erfahren.

## Systemweite Berechtigungen

Die systemweiten Berechtigungen werden detailliert im Knowledge-Base-Artikel [Berechtigungen]({{< ref path="support/kb/account/users/operators/permissions" lang="de" >}}) erläutert.

Allgemein empfiehlt sich, Berechtigungen auf Ebene von Operator-Gruppe, nicht einzelner Operatoren, zu handhaben. Damit bleibt der Überblick einfacher erhalten. In den meisten Fällen hast du es mit Teams (Operator-Gruppen) zu tun, bei denen jedes Mitglied dieselben Berechtigungen wie das übrige Team haben sollte.

## Kontext-Berechtigungen {id="context-permissions"}

Die folgenden Elemente bei Uptrends ermöglichen das Setzen von Berechtigungen (wie *Anzeigen*, *Bearbeiten*, *Nutzen*, *Erstellen*) auf Element-Basis, indem die Operator-Gruppe mit Berechtigungen mit dem Element verknüpft wird. Die folgenden Knowledge-Base-Artikel beschreiben, wie Berechtigungen gesetzt werden:

- [Meldedefinitionen]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="de" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="de" >}})
- [Integrationen]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="de" >}})
- [Prüfobjekte]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="de" >}})

## Anleitung

Die Anleitung hat Schritt-für-Schritt-Anweisungen für das Einrichten von Berechtigungen für ein neues Team deines Accounts

- [Einrichten eines Teams in deinem Account]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="de" >}})