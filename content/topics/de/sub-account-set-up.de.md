{
  "hero": {
    "title": "Subaccount – Einrichtung"
  },
  "title": "Subaccount – Einrichtung",
  "summary": "In diesem Artikel erläutern wir die Einrichtung eines neuen Subaccounts.",
  "url": "/support/kb/account/nutzer/subaccounts/sub-account-einrichtung",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/sub-account-set-up"
}

## Einen Subaccount erstellen

Um einen Subaccount zu erstellen:

1.  Rufe den Operator-Hub über {{< AppElement type="menuitem" >}} Accounteinstellungen > Operator, Gruppen und Subaccounts {{< /AppElement >}} auf.
2.  Klicke auf {{< AppElement type="buttonSecondary" >}} Subaccount hinzufügen {{< /AppElement >}} im Bereich Subaccounts.

Nun kannst du auf den Registerkarten der Seite *Neuer Subaccount* einige Angaben zum Subaccount machen.

## Allgemein
### Subaccount Info

1.  Gib einen **Subaccount Namen** an. Nach dem Speichern wird dies der Name sein, der verwendet wird, um eine Prüfobjektgruppe und Operator-Gruppe zu erstellen.
2.  Füge einen **Kunden Bezug** (optional) ein.

### Berechtigung

In diesem Abschnitt bestimmst du, ob die Operatoren des Subaccounts Prüfobjekte ändern oder hinzufügen können.

1.  Aktiviere das Kontrollkästchen **Änderungen von Prüfobjekten zulassen**, um Operatoren zu gestatten, Einstellungen anzupassen. Das Aktivieren dieser Funktion erlaubt Subaccount-Besitzer auch, zusätzliche Operatoren hinzuzufügen. Sie können jedoch keine Operatoren löschen.
2.  Aktiviere das Kontrollkästchen **Hinzufügen von Prüfobjekten zulassen**, um Operatoren eines Subaccounts zu gestatten, eigene Prüfobjekte einzurichten. Wenn sie Prüfobjekte einrichten dürfen, kannst du angeben, wie viele sie hinzufügen dürfen. Dafür steht das Feld **Maximale Anzahl von Prüfobjekten** zur Verfügung.

{{< callout >}}
**Hinweis**: Wenn in einem Subaccount Prüfobjekte hinzugefügt werden, unterliegt das neue Prüfobjekt der Verfügbarkeit auf Basis nicht genutzter Prüfobjekte des primären Accounts. Wenn in einem primären Account keine Prüfobjekte mehr verfügbar sind, kann in einem Subaccount kein neues Prüfobjekt hinzugefügt werden, selbst wenn die maximale Anzahl hier noch nicht erreicht ist.
{{< /callout >}}

### Neues Prüfobjekt – Info

Die Erstellung eines Subaccounts erfordert, dass du Informationen für ein HTTP/HTTPS-Prüfobjekt angibst. Wähle den **Prüfobjekt Typ** und gib eine **Prüfobjekt URL** für das neue Prüfobjekt ein. Uptrends wird dieses Prüfobjekt zu einer Prüfobjektgruppe mit dem gleichen Namen wie den des Subaccounts hinzufügen.

## SLA

Wenn mit dem neuen Subaccount-Besitzer eine SLA besteht, lege die Anforderungen für die SLA auf der Registerkarte {{< AppElement type="tab" >}}SLA{{< /AppElement >}} fest. Solltest du Infos zur Einrichtung eines SLA-Monitorings benötigen, leitet dich unser [SLA-Bereich]({{< ref path="support/kb/dashboards-and-reporting/sla" lang="de" >}}) durch den Vorgang.

## Weitere Prüfobjekte

Auf der Registerkarte {{< AppElement type="tab" >}}Weitere Prüfobjekte{{< /AppElement >}} kannst du bereits bestehende Prüfobjekte hinzufügen. Du kannst auch später noch neue Prüfobjekte hinzufügen.

## Operatoren

Auf dieser Registerkarte kannst du bestehende Operatoren für den Subaccount aus der Liste auswählen. Subaccount-Operatoren können nur zur Gruppe *Jeder* und zu ihrer Subaccount-Gruppe gehören.

## Speichern

Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um den neuen Subaccount und das neue Prüfobjekt zu erstellen.

{{< callout >}}
**Hinweis**: Sollen die Subaccount-Operatoren Warnmeldungen erhalten, musst du eine neue [Meldedefinition]({{< ref path="support/kb/alerting/create-alert-definitions" lang="de" >}}) erstellen. Wenn Alarme per SMS oder Telefon/Sprachnachricht gemeldet werden sollen, gib die Mobiltelefonnummern bei den [Operator-Einstellungen]({{< ref path="support/kb/account/users/operators/operator-groups" lang="de" >}}) an.
{{< /callout >}}
