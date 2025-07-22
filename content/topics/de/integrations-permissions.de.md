{
  "hero": {
    "title": "Berechtigungen für Integrationen"
  },
  "title": "Berechtigungen für Integrationen",
  "summary": "Verwalte Operator-Berechtigungen für Integrationen",
  "url": "/support/kb/alarme/integrationen/integrations-berechtigungen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/integrations-permissions"
}

{{< callout >}}Berechtigungen für Integrationen stehen nur bei Accounts der **Stufe Enterprise** zur Verfügung.{{< /callout >}}

Integrationen werden in den Eskalationsstufen von Meldedefinitionen verwendet, um die Kommunikationskanäle für Warnmeldungen einzurichten.
Indem du Operatoren Berechtigungen für Integrationen zuweist, steuerst du, wer Integrationen bei Meldedefinitionen erstellen, bearbeiten und nutzen kann.

## Wer kann Berechtigungen verwalten?

Administratoren (Mitglieder der Operator-Gruppe Administrator) können immer Integrationen erstellen, einsetzen und bearbeiten. Sie können auch die Berechtigungen für Integrationen einrichten und ändern.

Zudem kann ein Operator mit den beiden Berechtigungen **Erstelle Integrationen** (für einen Operator oder eine Operator-Gruppe gesetzt) und **Integration bearbeiten** (für eine Integration gesetzt) die Berechtigungen für die Integration verwalten, die er selbst erstellt hat.
## Berechtigungstypen

Es gibt zwei Stellen, an denen Berechtigungen verwaltet werden: beim Operator (Gruppe) oder bei der Integration selbst.

### Integration erstellen

Die Berechtigung **Erstelle Integrationen** wird für einen Operator oder eine Operator-Gruppe festgelegt. Lies in unserem Knowledge-Base-Artikel zu [Berechtigungen]({{< ref path="support/kb/account/users/operators/permissions#create-integration" lang="de" >}}), um zu erfahren, wie es geht.

### Integration nutzen

Die Berechtigung **Nutze Integration** ermöglicht Operatoren, die Integration bei den Eskalationsstufen einer Meldedefinition zu verwenden. In der Liste der Integrationen auf den Eskalationsstufen-Registerkarten (in einer Meldedefinition) siehst du alle Integrationen, bei denen du über die Berechtigung **Nutze Integration** verfügst.

Diese Berechtigung gibt nicht Zugriff auf die Integration an sich. Du siehst sie nicht in der Liste der Integrationen unter {{< AppElement type="menuitem" >}}Alarmierung > Integrationen{{< /AppElement >}}, wo die Integrationen verwaltet werden.

Die Integration **Email** ist zur Nutzung für alle Mitglieder der Operator-Gruppe **Jeder** verfügbar. Das stellt sicher, dass du zumindest eine Integration nutzen kannst, wenn du die Zugriffsberechtigung für Meldedefinitionen hast, dir aber noch keine Zugriffsberechtigung für Integrationen gewährt wurden. Die Integration **Email** verursacht keine zusätzlichen Kosten im Uptrends Account, während die SMS-Integration [SMS Credits]({{< ref path="support/kb/alerting/sms-credit-usage" lang="de" >}}) erfordert.

Nutzt du API-Aufrufe, um Informationen zu Integrationen zu erhalten? Dann gibt eine GET-Abfrage alle Integrationen aus, für die du die Berechtigung **Nutze Integration** hast. Auf diese Weise kannst du die `GUID`-Information der Integration abrufen, die du benötigst, um die Integration mithilfe der APIs einer Meldedefinition hinzuzufügen. Die Abfrage gibt den Namen, den Typ und die `GUID` der Integration aus.

### Integration bearbeiten {id="edit-integration"}

Diese Berechtigung ist höher als die Berechtigung **Nutze Integration**, denn sie ermöglicht dir, die Integration zu ändern. Die Berechtigung **Integration bearbeiten** beinhaltet tatsächlich die Berechtigung **Nutze Integration** – du musst nicht beide zuweisen.

Verfügst du über die Berechtigung **Integration bearbeiten** für eine Integration, siehst du sie in der Liste der Integrationen unter ({{< AppElement type="menuitem" >}}Alarmierung > Integrationen {{< /AppElement >}}).

Diese Berechtigung beinhaltet das Recht, die Integration zu löschen.

## Berechtigungen verwalten

Berechtigungen setzen oder ändern:

1. Rufe {{< AppElement type="menuitem" >}}Alarmierung > Integrationen {{< /AppElement >}} auf.
2. Wähle aus der Liste der Integrationen diejenige, die du bearbeiten möchtest.
3. Öffne die Registerkarte {{< AppElement type="tab" >}} Berechtigungen {{< /AppElement >}}.
4. Klicke auf {{< AppElement type="buttonPrimary" >}} Berechtigung hinzufügen {{< /AppElement >}}.
5. Wähle aus dem Pop-up-Fenster die Operator-Gruppe (oder einen Operator) und den Berechtigungstyp, klicke dann auf {{< AppElement type="buttonPrimary" >}} Hinzufügen {{< /AppElement >}}.
6. Um eine Berechtigung zu entfernen, wähle {{< AppElement type="deletebutton" >}} Löschen {{< /AppElement >}} in der Liste unter **Berechtigungen**.
7. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um die vorgenommenen Änderungen zu sichern.