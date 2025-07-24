{
  "hero": {
    "title": "Prüfobjektgruppen"
  },
  "title": "Prüfobjektgruppen",
  "summary": "Die Organisation deiner Prüfobjekte in Prüfobjektgruppen erleichtert das Reporting und die Alarmierungseinrichtung.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-management/pruefobjektgruppen",
  "translationKey": "[URL_1]
}

Bei Prüfobjektgruppen geht es um Organisation und Vereinfachung. Hast du einmal deine Prüfobjektgruppen eingerichtet, vereinfachen und beschleunigen sie das [Anwenden von Vorlagen]([LINK_URL_1]), Hinzufügen von Prüfobjekten zu [Meldedefinitionen]([LINK_URL_2]) und das Konfigurieren von Dashboards und Berichten.

## Prüfobjektgruppen – Entscheidungen

Zwar kann die Gruppe *Alle Prüfobjekte* nicht bearbeitet werden, doch lässt sich jede andere Gruppe anpassen und ein Prüfobjekt kann mehreren Prüfobjektgruppen zugeordnet werden. Es gibt mehrere unterschiedliche Möglichkeiten, Prüfobjektgruppen zu erstellen. Nachfolgend findest du einige Beispiele üblicher Schwerpunkte, nach denen Nutzer ihre Prüfobjektgruppen zusammengestellt haben.

**Prüfobjekttyp**: Es kann sinnvoll sein, Prüfobjektgruppen basierend auf dem [Prüfobjekttyp]([LINK_URL_3]) wie Website-Performance-Prüfobjekte, Performance-Prüfobjekte für Mobilgeräte, Verfügbarkeitsprüfobjekte, API-Prüfobjektgruppe, Transaktionsprüfobjekte und Zertifikatsprüfobjekte zusammenzufassen. Diese Art der Gruppierung ist besonders hilfreich für das Einrichten von Berichten.

**Nach Standort**: Wenn du die Berichte nach geografischem Standort benötigst, richte die Prüfobjektgruppen nach Region oder Land ein. Üblicherweise haben diese geografischen Prüfobjekte die gleichen Checkpoints, wodurch es einfach wird, sie durch Verwendung von Prüfobjektvorlagen zu verwalten.

**Datenzentrum**: Wenn deine Websites durch unterschiedliche Datenzentren gestützt sind, möchtest du vielleicht die Gruppen auf Grundlage der Datenzentren einrichten. Du kannst dann die Verfügbarkeits- und Performance-Daten schnell auf Basis des Datenzentrums abrufen. Die Gruppierung nach Datenzentrum kann hilfreich sein, wenn Wartungszeiträume anhand von Prüfobjektvorlagen eingerichtet werden.

**Priorität**: Prüfobjekte sollten zudem auch nach ihrer Priorität gruppiert werden. Zum Beispiel nimmt die Verfügbarkeit deines Blogs nicht die gleiche Bedeutung ein, wie die Anmeldeseite. Richte Prüfobjektgruppen nach der Wichtigkeit der URL ein, um Prüfobjekte zu ordnen und Berichten Priorität zu geben.

**Domain**: Du unterhältst möglicherweise mehrere Domains oder Subdomains. Die Einrichtung nach Domains vereinfacht eine entsprechende Eskalation von Warnmeldungen.

**Seitenzweck**: Einige Nutzer gruppieren ihre Prüfobjekte häufig auch nach dem Zweck einer URL wie etwa Anmeldeseiten, Homepages und Support-Seiten.

## Überblick Prüfobjektgruppen

Die Seite **Prüfobjektgruppen** bietet dir einen Überblick der Prüfobjektgruppen deines Accounts. Du öffnest sie über [SHORTCODE_1] Accounteinstellungen > Prüfobjektgruppen [SHORTCODE_2].

![Screenshot Dashboard "Prüfobjekt Gruppen"]([LINK_URL_4])

Du siehst alle Prüfobjektgruppen, für die du wenigstens die Berechtigung *Anzeigen* besitzt. Erfahre mehr dazu und andere [Berechtigungstypen]([LINK_URL_5]) für Prüfobjekte und Prüfobjektgruppen.

Die Gruppe *Alle Prüfobjekte* gibt es standardmäßig in jedem Uptrends Account. Sie enthält jedes Prüfobjekt deines Accounts und du kannst sie weder bearbeiten noch löschen. Eventuell wirst du eine ähnliche Gruppe wie die *Alle Prüfobjekte* mit (nahezu) allen Prüfobjekten benötigen, bei der du jedoch die Möglichkeit hast, Berechtigungen zu bearbeiten und Prüfobjekte zu entfernen. Mehr dazu erfährst du unter der Einrichtung einer [Standard-Prüfobjektgruppe]([LINK_URL_6]).

Der Überblick zeigt Infos zu *aktiven Prüfobjekten*, was sich auf die maximale Zahl von Prüfobjekten (pro Typ) bezieht, die in deinen Prüfobjektgruppen eingerichtet sind. Du kannst auch festlegen, dass eine unbegrenzte Anzahl von Prüfobjekten erlaubt ist – und keine Beschränkungen pro Prüfobjekttyp einrichten.

**Beispiele**

- Ist keine Beschränkung festgelegt, und es werden 4 Basic Prüfobjekte genutzt, siehst du die Angabe „Basic Prüfobjekte: 4“.
- Ist eine Beschränkung von 10 Basic Prüfobjekten festgelegt, und es werden 4 genutzt, siehst du die Angabe „Basic Prüfobjekte: 4/10“.

## Eine neue Prüfobjektgruppe erstellen

Um eine neue Prüfobjektgruppe zu erstellen:

1. Gehe zu [SHORTCODE_3] Accounteinstellungen > Prüfobjektgruppen [SHORTCODE_4].
2. Klicke auf [SHORTCODE_5] Prüfobjektgruppe hinzufügen [SHORTCODE_6] oben rechts.
   Klicke alternativ auf das +-Zeichen bei [SHORTCODE_7] Accounteinstellungen > Prüfobjektgruppen [SHORTCODE_8].   

   Die Seite *Neue Prüfobjektgruppe* erscheint.

   ![Screenshot]([LINK_URL_7])

3. Gib in das Feld **Beschreibung** einen bedeutsamen Namen ein.
4. Entscheide, ob du die Anzahl der Prüfobjekte, die zu dieser Gruppe hinzugefügt werden dürfen, beschränken möchtest. Wenn du sie nicht begrenzen möchtest, aktiviere *Unbegrenzte Anzahl an Prüfobjekten erlauben*. Beachte, dass die Gesamtzahl der Prüfobjekte in allen Gruppen nicht die Anzahl der Prüfobjekte des Accounts sein kann.
5. Füge Prüfobjekte hinzu, die in dieser Gruppe vertreten sein sollten: Klicke auf die bestehende Prüfobjektgruppe im Abschnitt *In dieser Gruppe enthaltene Prüfobjekte*, um sie zu erweitern, und wähle dann die Prüfobjektnamen. Beachte, dass du auch ein Prüfobjekt zu einer Prüfobjektgruppe von der Prüfobjektseite selbst hinzufügen kannst. Klicke auf die [SHORTCODE_9]Mitglied von[SHORTCODE_10]-Registerkarte, um diese Änderungen vorzunehmen.
6. Füge auf der Registerkarte [SHORTCODE_11] Berechtigungen [SHORTCODE_12] den Operator (bzw. eine Operator-Gruppe) mit den entsprechenden Zugriffsberechtigungen für diese Prüfobjektgruppe hinzu. Der Knowledge-Base-Artikel [Prüfobjektberechtigungen]([LINK_URL_8]) hält weitere Infos zu den Optionen bereit.
7. Klicke auf [SHORTCODE_13] Speichern [SHORTCODE_14] unten auf der Seite.


Prüfobjektgruppen spielen eine wichtige Rolle bei der Einrichtung von Mitarbeiterteams und der Zuweisung der notwendigen Zugriffsberechtigungen für jedes Mitglied (Operator). Der Artikel [Einrichten eines Teams in deinem Account]([LINK_URL_9]) führt dich detailliert durch die Schritte dieser Einrichtung.
