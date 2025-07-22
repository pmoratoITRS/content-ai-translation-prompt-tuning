{
  "hero": {
    "title": "Berechtigungen für automatisch erzeugte Vault Bereiche verwalten"
  },
  "title": "Berechtigungen für automatisch erzeugte Vault Bereiche verwalten",
  "summary": "Wenn du eine Transaktion aufzeichnest, verwahrt Uptrends deine sensiblen Daten in einem automatisch erzeugten Bereich der Uptrends Vault mit Standard-Berechtigungen auf. Erfahre, wie du die Berechtigungen für automatisch erzeugte Vault Items verwaltest.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/berechtigungen-fuer-automatisch-erzeugte-vault-bereiche-verwalten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die [Uptrends Vault]([LINK_URL_1]) bietet dir einen sicheren Ort, um deine sensiblen Zertifikate, öffentlichen Schlüssel und Anmeldedaten, die du für deine Transaktionsskripte benötigst, zu speichern. Wenn du ein neues Transaktionsprüfobjekt mithilfe des Transaction Recorders erstellst oder wenn unser Support ein älteres Prüfobjekt für das neuere Self-Service Transactions-Format umwandelt, schiebt Uptrends automatisch die sensiblen Daten in die Vault. Dein Skript greift auf diese Vault Items zu, sodass die sensiblen Werte nicht im Skript oder in deinen Berichten sichtbar sind ([erfahre mehr]([LINK_URL_2]) darüber, wie du sensible Werte in deinem Skript verwendest).

## Standard-Berechtigungen

Die Vault enthält Elemente bzw. Items, die sie in Vault-Bereiche ablegt. Nur diejenigen individuellen Operatoren oder Operatoren einer [Operator-Gruppe]([LINK_URL_3]), die in der Kachel *Berechtigungen* eines Vault-Bereichs genannt sind, können auf Vault Items in den jeweiligen Bereichen zugreifen und sie ändern.

**Für neue Aufzeichnungen und neu umgewandelte Skripte werden die Standard-Berechtigungen auf die neuen automatisch erzeugten Vault-Bereiche angewendet**. Die Standard-Berechtigungen gelten für die Administratoren-Gruppe und gegebenenfalls für die Nutzergruppe des Sub Accounts.

Neu hochgeladene Aufzeichnungen werden immer zu einem automatisch erzeugten Vault-Bereich mit Standard-Berechtigungen hinzugefügt. Wenn du die Berechtigungen modifizierst, wird der nächste Upload einen neuen Bereich erzeugen, der über die Standard-Berechtigungen verfügt.

[SHORTCODE_1]
**Hinweis**: Um ein mehrfaches automatisches Generieren von Bereichen zu vermeiden, belasse es bei den Standard-Berechtigungen und dupliziere Vault Items in einen benutzerdefinierten Bereich. Lösche sie dann aus dem automatisch generierten Bereich.
[SHORTCODE_2]

## Standard-Berechtigungen ändern

Du kannst die Standard-Berechtigungen bei all deinen Vault-Bereichen ändern, sodass der Zugriff nach Bedarf mehr oder weniger beschränkt ist, indem du Gruppen oder Operatoren ein- oder ausschließt.

1.  Navigiere zu [SHORTCODE_3] Account Setup > Vault [SHORTCODE_4].
2.  Klicke, um den Bereich zu öffnen, für den du die Berechtigungen ändern möchtest.
3.  Um Berechtigungen zu entfernen, klicke auf *Löschen* rechts vom Namen eines Operatoren oder einer Gruppe.
4.  Um Berechtigungen hinzufügen, klicke in der Kachel **Berechtigungen** auf [SHORTCODE_5]+ Berechtigung hinzufügen[SHORTCODE_6].
5.  Wähle die Gruppe oder den Operator aus.
6.  Setze den *Berechtigungs-Level* auf *Nur anzeigen* oder *Komplette Kontrolle*.
7.  Klicke auf [SHORTCODE_7]Hinzufügen[SHORTCODE_8].

![]([LINK_URL_4])
