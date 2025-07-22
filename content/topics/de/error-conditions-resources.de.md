{
  "hero": {
    "title": "Fehlerbedingungen – Ressourcen"
  },
  "title": "Fehlerbedingungen – Ressourcen",
  "summary": "Ein Überblick der verfügbaren Fehlerbedingungen für die Kategorie *Ressourcen*. Ressourcen sind Objekte, die deine Webseite lädt, um sie sichtbar und funktionsfähig zu machen.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-ressourcen",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-resources"
}

Jedes Prüfobjekt führt einige Standardüberprüfungen je nach Prüfobjekttyp aus. Zusätzlich kannst du in den Fehlerbedingungen eines Prüfobjekts benutzerdefinierte Prüfungen festlegen, die für bestimmte Situationen Warnmeldungen generieren. Der Knowledge-Base-Artikel [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="de" >}}) erläutert, welche dies sind und wie sie konfiguriert werden können.

Dieser Artikel erläutert, wie die Fehlerbedingungen der Kategorie *Ressourcen* funktionieren. Bei einem Prüfobjekt findest du sie auf der Registerkarte {{< AppElement type="tab" >}} Fehlerbedingungen {{< /AppElement >}} im Abschnitt *Prüfe Ressourcen*. Beachte, dass nicht alle Prüfobjekttypen dieselben Fehlerbedingungen beinhalten. Sieh dir die Tabelle der [verfügbaren Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="de" >}}) an, um herauszufinden, welche Optionen für bestimmte Prüfobjekttypen möglich sind.

## Was ist eine Ressourcenprüfung?

Deine Website stützt sich auf viele Ressourcen (Bilder, Stylesheets, Skripte usw.). Diese Ressourcen sind die Objekte, die für deine Website geladen werden müssen. Ein Prüfobjekttest verzeichnet die Größe (in Kilobytes) der Antwort des Servers. Die Seitengröße (zusammen mit einer Inhaltsprüfung) kann anzeigen, ob eine Seite tatsächlich vollständig geladen wurde.

Überraschende (kleine oder große) Größen können auch auf betrügerische Seitenmanipulation hinweisen. Bei einem Full Pagecheck oder einem Transaktionsprüfobjekt erhältst du ein [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="de" >}}), das eine visuelle Darstellung des Ladevorgangs der Objekte ist. Das Diagramm enthält die Metriken und Details der Prüfung aus dem Monitoring.

Anhand der Fehlerbedingungen im Abschnitt **Prüfe Ressourcen** setzt du einen Schwellenwert für die Gesamtgröße oder einen Prozentsatz zu einzelnen Ressourcen, die nicht laden, bevor du das Laden einer Website als fehlerhaft erachtest.

## Die Inhaltsgröße prüfen (HTTP(S)- und Webservice HTTP(S)-Prüfobjekte)

Bei HTTP(S)- und Webservice HTTP(S)-Prüfobjekten kannst du eine Fehlerbedingung angeben, die auf die Mindestgröße des Inhalts prüft.

![Screenshot Ressourcen prüfen HTTPS(S) oder Webservices](/img/content/scr_errorconditions-resources-https.min.png)

## Prüfe die Summe aller Ressourcen (Full Pagecheck)

Du kannst eine Höchst- und eine Mindestgröße (in kB) angeben, die als Server-Antwort zurückgegeben werden sollte. Wähle die Option **Prüfe die Summe aller Ressourcen** im Abschnitt *Prüfe Ressourcen*.

![Screenshot Fehlerbedingung alle Ressourcen zusammen](/img/content/scr_errorconditions-resources-all.min.png)

Gib eine Mindestgröße ein, indem du unter *Alle Ressourcen zusammen betragen mehr als* den unteren Schwellenwert (in kB) einträgst. Wenn die Größe aller Seitenobjekte zusammen niedriger als dieser Wert ist, kann das darauf hinweisen, dass Seiteninhalte fehlen und die Seite möglicherweise nicht korrekt funktioniert.

Gib eine maximale Größe ein, indem du unter *Alle Ressourcen zusammen betragen weniger als* den oberen Schwellenwert (in kB) einträgst, den du in der Server-Antwort erhältst. Wenn die Größe aller Seitenobjekte zusammen über diesen Wert liegt, wurde zu viel Inhalt geladen. Das kann auf einen Fehler beim Inhalt hinweisen oder darauf, dass auf deiner Website Inhalte geladen wurden, die nicht von dir beabsichtigt oder genehmigt wurden.

Du kannst eine Mindest- und Höchstgrenze bei der Größen-Fehlerbedingung kombinieren. Füge eine neue Fehlerbedingung hinzu, indem du auf {{< AppElement type="buttonSecondary" >}} Neue Prüfung {{< /AppElement >}} klickst.

## Prüfe jede Ressource individuell (Full Pagecheck)

Zusätzlich zur Prüfung der Summe aller Ressourcen kannst du auch individuelle Elemente prüfen lassen. Wähle die Option **Prüfe jede Ressource individuell**, entscheide dann zu prüfen, ob ein bestimmter Anteil der Ressourcen gar nicht lädt, oder ob ein festgelegter Anteil aller Ressourcen über einer Maximalgröße liegt.

Beachte, dass sich die Überschrift der Ressourcenprüfung dynamisch gemäß deiner Optionswahl und Werteingabe ändert. Sie spiegelt wider, was du für die Prüfung definiert hast.

Um zu prüfen, ob ein bestimmter Anteil deiner Ressourcen nicht lädt, wähle die Option **Ressource schlägt beim Laden fehl** und gib einen Prozentsatz (Obergrenze) der Ressourcen an, dessen Laden fehlschlagen darf. Wird die Grenze überschritten, wird ein Fehler ausgelöst.

![Screenshot Fehlerbedingung einzelne Ressource schlägt fehl](/img/content/scr_errorconditions-resources-individual-fail.min.png)

Um zu prüfen, ob einige (ein Prozentsatz) oder alle Ressourcen zusammen eine bestimmte Größe überschreiten, wähle die Option **Ressourcengröße ist über** und gib gegebenenfalls einen Prozentsatz ein. Setzt du die Prozentangabe auf 0 %, wird geprüft, ob es einzelne Ressourcen gibt, die die Schwelle überschreiten. Setzt du die Prozentangabe auf 100 %, wird geprüft, ob alle Ressourcen zusammen die Größengrenze überschreiten.

![Screenshot Fehlerbedingung einzelne Ressourcen sind zu groß](/img/content/scr_errorconditions-resources-individual-percentage.min.png)

