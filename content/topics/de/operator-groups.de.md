{
  "hero": {
    "title": "Operator-Gruppen"
  },
  "title": "Operator-Gruppen",
  "summary": "Hast du Probleme beim Einrichten von Operator-Gruppen? Erfahre, wie andere Nutzer von Uptrends ihre Gruppen eingerichtet haben.",
  "url": "/support/kb/account/nutzer/operatoren/operator-gruppen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-groups"
}

Beim Einrichten der [Operatoren]({{< ref path="support/kb/account/users/operators" lang="de" >}}) in deinem Uptrends Account kann es hilfreich sein, benutzerdefinierte Operator-Gruppen zu erstellen. Mit Operator-Gruppen wird es einfacher, Zugang zu benutzerdefinierten Berichten zuzuweisen, und sie sind praktisch, wenn du [Meldedefinitionen festlegst]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}). Dieser Artikel erläutert die in deinem Account bereits vorhandenen zwei Operator-Gruppen. Beispiele zeigen, wie du deine Operator-Gruppen organisieren kannst.

Operator-Gruppen sind in der Uptrends Anwendung der Ort, an dem du Nutzern Berechtigungen zuweist. Lies unseren Artikel [Berechtigungen]({{< ref path="support/kb/account/users/operators/permissions" lang="de" >}}), um mehr zu erfahren.

## Eine Operator-Gruppe hinzuzufügen

Um eine neue Operator-Gruppe hinzuzufügen:

1. Rufe den [Nutzer-Management-Hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="de" >}}) auf, indem du im Menü auf {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen (und Subaccounts) {{< /AppElement >}} klickst.
2. Klicke auf {{< AppElement type="buttonSecondary" >}} Operator Gruppe hinzufügen {{< /AppElement >}}.
3. Gib unter **Beschreibung** einen Namen für die Operator-Gruppe ein.
4. Verwende die Baumstruktur **In dieser Gruppe enthaltene Operatoren**, um Operatoren hinzuzufügen oder zu entfernen, indem du das Kontrollkästchen vor dem Namen aktivierst oder deaktivierst. Beachte: Operatoren können zu mehreren Operator-Gruppen gehören.
5. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, wenn du fertig bist.

## Die Operator-Gruppen Jeder und Administratoren

Zu Beginn hast du zwei Operator-Gruppen: Jeder und Administratoren. Diese zwei Spezialgruppen dienen zwei unterschiedlichen Funktionen.

### Jeder

Die Jeder-Gruppe ist genau, was der Name sagt: für jeden. Alle in deinem Account eingerichteten Operatoren erscheinen in dieser Gruppe. Die Operator-Gruppe „Jeder“ kann nicht bearbeitet werden. Verwende die Gruppe, wenn du Zugriffsberechtigungen für alle Operator-Gruppen einrichten möchtest.

### Administratoren

Durch Hinzufügen eines Operators zu dieser Gruppe kannst du dem Operator kompletten Zugang zu allen Funktionen im Uptrends Account geben. Diese Operatoren können Prüfobjekte und Dashboards bearbeiten, Operatoren hinzufügen und entfernen, Meldedefinitionen festlegen und ändern, Account-Einstellungen anpassen und die Rechnungen einsehen sowie Preise für zusätzliche SMS-Credits und Prüfobjekte anfragen. Füge Nutzer dieser exklusiven Gruppe mit Bedacht hinzu.

## Benutzerdefinierte Gruppen

Wenn du keine Idee hast, wie du deine Operatoren organisieren sollst, sieh dir an, wie andere Nutzer von Uptrends in ihren Accounts Gruppen eingesetzt haben.

### Dein Organisationsdiagramm als Grundlage

Ein großartiges Beispiel, wie du deine Operator-Gruppen einrichten kannst, bietet wahrscheinlich ein Organisationsdiagramm deines Unternehmens. Operator-Gruppen werden häufig basierend auf Abteilung oder Team aufgestellt. Du könntest so etwa Operator-Gruppen für das DevOps-Team, das Support-Team oder das Management-Team einrichten. Diese abteilungsbasierten Gruppen sollten eventuell in Teams aufgeteilt werden. Bei dem Beispiel Support könnte dies etwa eine Aufteilung in unterschiedliche Schichten sein.

### nach Operator-Funktion

Es kann nützlich sein, insbesondere für Warnmeldungen, Operator-Gruppen auf Grundlage der Funktion des Operators zu erstellen. Es wird wahrscheinlich nicht hilfreich sein, Probleme in Bezug auf eine API an einen Webdesigner zu leiten. Stattdessen kannst du eine Operator-Gruppe „API“ einrichten, bei der Warnmeldungen bei API-Problemen direkt an das Team gesendet werden, das sie behebt. Das Gleiche gilt für Datenbanken, Performance und Netzwerkinfrastruktur.

### nach Reaktions-/Supportlevel

Bei der Einrichtung der Meldedefinitionen kannst du auch Gruppen auf Grundlage des Reaktionslevels erstellen. Richte zum Beispiel Operator-Gruppen für First-, Second- und Third-Level-Support ein. Zusammen mit Dienstplänen und Eskalationsstufen werden dadurch die diensthabenden Support-Mitarbeiter auf dem entsprechenden Level die Warnmeldung erhalten, wenn das Problem eskaliert.

### Dienstleister und Kunden

Du benötigst eventuell Gruppen für Dienstleister und Kunden, denen du Zugriff auf Berichte von Uptrends gewährst. Möglicherweise besteht eine Vereinbarung mit einem CDN-Anbieter, dass direkt auf CDN-Probleme reagiert werden muss. Auch Kunden, die sich auf deine Services verlassen, fordern eventuell Einblick in Verfügbarkeit und Performance mit direktem Zugang zu den Berichten. Durch Zuweisen dieser besonderen Operatoren in eine eigene Operator-Gruppe kann die Zugangsverwaltung vereinfacht werden.
