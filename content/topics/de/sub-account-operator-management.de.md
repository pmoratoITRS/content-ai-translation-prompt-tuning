{
  "hero": {
    "title": "Subaccount – Operator-Verwaltung"
  },
  "title": "Subaccount – Operator-Verwaltung",
  "summary": "Nach der ersten Einrichtung wirst du die Operatoren deiner Subaccounts verwalten müssen. In diesem Artikel beschreiben wir das Hinzufügen und Entfernen von Operatoren.",
  "url": "/support/kb/account/nutzer/subaccounts/subaccount-operator-verwaltung",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/sub-account-operator-management",
  "tableofcontents": false
}

Subaccount-Operatoren verfügen über eingeschränkte Berechtigungen. Wenn ein Subaccount-Operator Prüfobjekte ändern kann, kann er auch neue Nutzer hinzufügen. Aber Subaccount-Operatoren können keine Operatoren aus einem Subaccount entfernen. Das Hinzufügen und Entfernen von Operatoren ist gleich dem [Hinzufügen regulärer Operatoren]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="de" >}}) im Parent/Primär-Account. Beim Hinzufügen oder Entfernen von Operatoren muss man jedoch Folgendes berücksichtigen:

**Du kannst keine Operatoren aus der *Administrator*-Gruppe zu einem Subaccount hinzufügen**. Administratoren haben bereits die Berechtigung, Nutzer und Prüfobjekte in einem Subaccount zu verwalten, sodass sie diesem nicht mehr hinzugefügt werden müssen.

**Ein Operator kann nur zu einem Subaccount oder einer regulären Gruppe gleichzeitig gehören** (mit Ausnahme der Gruppe Jeder).

**Du kannst keine Operatoren löschen, die Mitglied bei einem Subaccount sind**. Um einen Subaccount-Operator zu löschen:

1.  Öffne die Einrichtungsseite des Operators unter ({{< AppElement type="menuitem" >}}Accounteinstellungen > Operatoren{{< /AppElement >}}).
2.  Klicke auf den Operatornamen, den du löschen möchtest.
3.  Klicke auf die {{< AppElement type="tab" >}}Mitglied von{{< /AppElement >}}-Registerkarte.
4.  Deaktiviere das Kontrollkästchen neben dem Subaccount in der Liste.
5.  Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.
6.  Öffne erneut die Einstellungsseite des Operators.
7.  Klicke auf {{< AppElement type="deletebutton" >}}Diesen Operator löschen{{< /AppElement >}}.

{{< callout >}}
**Hinweis**: Bis du einen Subaccount-Operator löschst, den du zuvor von einer Subaccount-Gruppe entfernt hast, **ist der Operator immer noch in deinem Account aktiv und hat Lese-Zugriff für den Primär-Account**. Lösche Subaccount-Operatoren sofort nach dem Entfernen aus der Operator-Gruppe des Subaccounts.
{{< /callout >}}
