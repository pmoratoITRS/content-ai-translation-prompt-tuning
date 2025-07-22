{
  "hero": {
    "title": "Den Schritte-Editor verstehen"
  },
  "title": "Den Schritte-Editor verstehen",
  "summary": "Der Schritte-Editor wird genutzt, um Schritte und Aktionen eines Transaktionsskripts zu bearbeiten.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/den-step-editor-verstehen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-the-step-editor"
}

Der Schritte-Editor für Transaktionen wird verwendet, um Schritte und Aktionen bei einem Transaktionsskript zu bearbeiten, und kann als visueller Editor mit einer Benutzeroberfläche genutzt werden, um Schritte hinzuzufügen und zu bearbeiten. Es gibt auch einen Skript-Editor, bei dem das Skript als Klartext erscheint. 

Wenn du versiert im Schreiben von eigenen Skripten bist, lies den Abschnitt [Quellcode direkt programmieren]({{< ref path="#scripting-source-code-directly" lang="de" >}}), um mehr über den Skript-Editor zu erfahren.

In den meisten Fällen wirst du kein Skript schreiben, sondern den [Transaktionsrekorder verwenden]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}}), um eine erste Einrichtung des Skripts vorzunehmen, und dann den Schritte-Editor nutzen, um die Feinheiten der Transaktion auszuarbeiten.

{{< callout >}}
**Hinweis**: Uptrends nutzt Transaktions-Credits, um den Preis für dein Transaktionsprüfobjekt festzustellen. Die Anzahl der Credits, die für ein Prüfobjekt genutzt wurden, werden neben dem Prüfobjektnamen im Überblick der *Prüfobjekte* (wechsle nach {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}}) angezeigt. Eine vollständige Erläuterung zu den Credits enthält der Knowledge-Base-Artikel [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="de" >}}).
{{< /callout >}}

## Schritte und Aktionen

Das Skript eines Transaktionsprüfobjekts enthält Schritte (der Transaktion, die du überwachen möchtest). Innerhalb der Schritte findest du Aktionen – die Mikroschritte deiner Transaktion.

Schritte und Aktionen bearbeiten:

1. Rufe {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf.
2. Öffne die Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}}.

![Screenshot Schritte-Editor für Transaktionen](/img/content/scr_transaction-step-editor-041024.min.png)

 Du optimierst und testest dein Transaktionsskript auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}} oder kannst es hier auch von Grund auf selbst schreiben. Nutze dazu die Schaltfläche {{< AppElement type="buttonSecondary" >}} WECHSLE ZUM SKRIPT {{< /AppElement >}} oben rechts im Editor.

Wenn du dein Skript aus dem [Transaktionsrekorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}}) hochgeladen hast, solltest du einen oder mehrere Schritte mit bereits definierten Aktionen sehen. Wenn du dein Skript von Grund auf selbst erstellst, formulierst du jeden Schritt deiner Transaktion mithilfe des Step-Editors. Wir empfehlen, den Transaktionsrekorder zu verwenden, um für den Anfang eine gute Basis zu erhalten.

Das Transaktionsskript besteht aus *Schritten* und *Aktionen*. Sehen wir uns an, was wir mit Schritten und Aktionen meinen.

## Was ist ein Schritt?

Wenn du ein Skript vom Transaktionsrekorder hochlädst, definiert Uptrends automatisch die Schritte für dich. Aber was ist ein Schritt? Ein Schritt ist eine beliebige Gruppierung von Aktionen in deinem Transaktionsskript. Im Allgemeinen solltest du Nutzeraktionen mit deiner Seite in Schritte gruppieren, die mit einer Serveranfrage enden, beispielsweise das Einreichen eines Formulars. Das Gruppieren von Aktionen nach Serveranfrage hilft dir bei der Fehlerbehebung und bei der Analyse von Performance-Berichten.

Du kannst einen Schritt auch als Statuswechsel im Browser betrachten, d. h. eine Aktion, die zu einer neuen Seite führt oder die aktuelle Seite mit neuem Inhalt aktualisiert. Tatsächlich aber kannst du deine Schritte so einrichten, wie die Gruppierungen für deinen Fall und deine Berichtsanforderungen einen Sinn ergeben.

### Schritt-Einstellungen {id="step-settings"}

Klicke auf das Pfeilsymbol **>** neben dem Schrittnamen, um auf die Aktionen und Einstellungen des Schritts zuzugreifen.

![Screenshot einzelner Schritt im Skript](/img/content/scr_transaction-single-step-041024.min.png)

In jedem Schritt werden mehrere Einstellungen angezeigt.

- **Wasserfall** – du kannst optional ein [Wasserfalldiagramm]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}) zu jedem beliebigen Schritt hinzufügen, um die Seitenladezeit, **Core Web Vitals** und **W3C Leistungsmetriken** der Transaktionsschritte zu sehen. Jeder Wasserfallbericht nutzt ein [Credit für Transaktionsschritte]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="de" >}}). Um diese Einstellung zu aktivieren, markiere das **Kontrollkästchen Wasserfall** und passe Folgendes nach deinen Wünschen an:

  1. **Name** – gib jedem Schritt einen beschreibenden Namen. Beispielsweise *Hinzufügen zu Warenkorb*, *Login* oder *Terminanfrage*.

  2. **Fehlerbehandlung** – wenn du möchtest, dass die Transaktionsschritte oder Skripte trotz Seitenfehlern ausgeführt werden, aktiviere die Option **Ignoriere alle Fehler in diesem Schritt**. Uptrends fährt dann mit dem nächsten Schritt fort, ohne auf das Ergebnis des aktuellen Schritts zu warten. Dein **Kontrolldetails**-Bericht zeigt den Fehler, aber das Transaktionsprüfobjekt wird trotzdem weiter ausgeführt. Weitere Informationen findest du im Knowledge-Base-Artikel [Das Ignorieren von Fehlern bei optionalen Schritten und Aktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="de" >}}).

  3. **Leistungsmetriken** – aktiviere diese Option, um **Core Web Vitals und W3C-Werte als separate Messwerte** bei deinen Transaktionsprüfobjekten zu erfassen und zu speichern. Diese Option ermöglicht dir, diese [Metriken]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/monitoring-results-overview" lang="de" >}}) in den [benutzerdefinierten Kacheln Einfaches Daten Diagramm oder Einfache Daten Liste]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="de" >}}) zu speichern, wenn du auf das Symbol {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} klickst.


- **Filmstreifen** – du kannst optional [Timeline Screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="de" >}}) (auch Filmstreifen genannt) für einzelne Schritte hinzufügen. Ein Filmstreifen nutzt ein [Credit für Transaktionsschritte]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}), sofern nicht bereits ein Screenshot in dem Schritt eingefügt wurde. In dem Fall wird der Filmstreifen kostenlos bereitgestellt.

- **Screenshot** – mit einem optionalen [Screenshot]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="de" >}}) siehst du, wie der Bildschirm bei deinen Nutzern am Ende des Schritts aussieht. Einen einzelnen Screenshot fügst du durch die [Aktion](#adding-an-action) ** Screenshot** aus der Kategorie *Kontrolle* ein. Ein Screenshot nutzt ein [Credit für Transaktionsschritte]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}).

- **Seitenquelle** – wähle diese Option, um die Seitenquellinformationen und alle Konsolenprotokolldaten, die während der Ausführung des Schritts erzeugt wurden, zu erhalten. Beachte, dass die Seitenquelle nur zusammen mit dem Wasserfall verfügbar ist.


### Schritte hinzufügen

Um einen neuen Schritt zu deinem Skript hinzuzufügen:

1. Scrolle zum Ende der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}}.
2. Klicke auf {{< AppElement type="buttonSecondary" >}}SCHRITT HINZUFÜGEN{{< /AppElement >}}.
3. Gib dem neuen, derzeit leeren Schritt einen Namen.
4. (Optional) Ziehe den Schritt durch Halten der gepunkteten vertikalen Linien (oben links neben dem Schritt) mit der Maus und bewege den Schritt an die gewünschte Stelle im Skript. 
5. Füge Aktionen hinzu. Weitere Informationen zu Aktionen findest du im nächsten Abschnitt.
6. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um deine Änderungen zu sichern.

## Was ist eine Aktion?

Aktionen sind deine Nutzer-Interaktionen, Inhaltsüberprüfungen und Browser-Interaktionen, die innerhalb eines Schrittes passieren. Sie sind in Kategorien unterteilt: Interaktion, Testen und Kontrolle.

#### Interaktion

Zu den Aktionen des Typs *Interaktion* gehören:

- **Navigieren** – ruft eine bestimmte URL auf
- **Klicken** – findet ein Seitenelement (Schaltflächen, Kontrollkästchen, Optionsschalter) und führt einen Mausklick aus 
- **Übernehmen** – findet und füllt ein Textfeld, Passwortfeld usw. aus 
- **Hover** – findet ein Element und führt den Mauszeiger über das Element, um ausgeblendete Seitenelemente anzuzeigen 
- **Tastenereignis** – führt einen einzelnen Tastendruck aus, z. B., wenn ein Element nicht über eine klickbare Schaltfläche verfügt

Diese Optionen werden im Knowledge-Base-Artikel [Seiteninteraktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="de" >}}) beschrieben.


#### Testen

Die Aktionstypen *Testen* sind entweder Inhaltsprüfungen oder eine Warteaktion. 

- **Prüfe Elementinhalt** – findet und prüft ein Element auf bestimmten Inhalt 
- **Dokumentinhalt** – prüft das gesamte Seitendokument auf den spezifizierten Inhalt 
- **Warte auf Element** – findet und wartet auf ein bestimmtes Seitenelement 
- **Warte eine feste Zeit** – fügt eine benutzerdefinierte Wartezeit hinzu 

Lies die Knowledge-Base-Artikel [Inhaltsprüfungen]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}) beim Transaktions-Monitoring und [Einsatz von Wartebedingungen]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="de" >}}), um zu erfahren, wie sie funktionieren.

#### Kontrolle

Die Aktionskategorie *Kontrolle* bietet die folgenden Optionen:

- **Screenshot** – nimmt einen Screenshot des aktuellen Bildschirms auf 
- **Wechsle Browser Tab** – setzt das neue Fenster/den neuen Tab in den Vordergrund, wenn deine Seite ein weiteres Browser-Fenster geöffnet hat
- **Wechsle Frame** – ermöglicht den [Wechsel zwischen iFrames]({{< ref path="support/kb/synthetic-monitoring/transactions/switching-between-iframes-browser-tabs" lang="de" >}}) auf deiner Seite 
- **Scrolle** – findet ein Seitenelement und scrollt zu der Position auf der Seite (insbesondere hilfreich, wenn Screenshots verwendet werden)
- **Variableninhalt anpassen** – ändert die bestehende Variable mit der Aktion [Inhalt der Variable anpassen]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="de" >}})
- **Browser-Cache leeren** – [löscht den Browser-Cache]({{< ref path="/support/kb/synthetic-monitoring/transactions/clear-browser-cache" lang="de" >}}), um Seitenobjekte direkt vom Server statt aus dem Browser-Cache neu zu laden

### Eine Aktion hinzufügen {id="adding-action"}

Eine neue Aktion zu einem der Schritte in deinem Transaktionsprüfobjekt hinzufügen:

1. Öffne den Schritt, dem du eine Aktion hinzufügen möchtest.
2. Klicke auf {{< AppElement type="buttonSecondary" >}} AKTION HINZUFÜGEN {{< /AppElement >}}. 
   Das Pop-up-Fenster *Aktion hinzufügen* öffnet sich:
   ![Screenshot Pop-up Aktion hinzufügen](/img/content/scr_add-action-popup.min.png)
   Fahre mit der Maus über die Aktionen, um mehr Informationen zu ihnen zu erhalten. 
3. Klicke auf die Aktion, die du zu dem Schritt hinzufügen möchtest. 
4. (Optional) Ändere die Reihenfolge der Aktionen, sofern erforderlich. Ziehe die Aktion durch Halten der gepunkteten vertikalen Linien (oben links neben der Aktion) mit der Maus und bewege die Aktion an die gewünschte Stelle der Aktionsfolge. Du kannst die Aktion auch in einen anderen Schritt ziehen.
5. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um deine Änderungen zu sichern.

### CSS-Selektoren und XPath-Abfragen {id="css-selectors-and-xpath-queries"}

Du hast vielleicht bemerkt, dass einige Aktionen CSS-Selektoren oder XPath-Abfragen enthalten. Sie sagen dem Transaktionsprüfobjekt genau, mit welchem Bildschirmelement es interagieren muss, um eine Aktion abzuschließen. Hast du den Transaktionsrekorder verwendet, so hat dieser bereits ausgewählt, was als beste Methode zum Auffinden eines Seitenelements erscheint, wie im Knowledge-Base-Artikel [Transaktionsrekorder – Selektorenbestimmung]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="de" >}}) beschrieben. 

Der Algorithmus entscheidet sich jedoch nicht in allen Fällen für die beste Möglichkeit. Du kannst weitere Optionen anzeigen, indem du auf die Schaltfläche {{< AppElement type="button" >}}\[...\]{{< /AppElement >}} im Selektor-Wert-Feld klickst. 

Eine weitere Möglichkeit ist, eigene Selektoren und Abfragen zu programmieren. Erfahre mehr über [CSS-Selektoren](https://www.w3schools.com/cssref/css_selectors.asp) oder [XPath-Abfragen](https://www.w3schools.com/xml/xpath_intro.asp). Wenn du Selektoren manuell definierst, kannst du [automatische Variablen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}}) nutzen. Damit hast du noch mehr Flexibilität bei der Selektorenauswahl. 

Wenn du nicht mit der Arbeit mit CSS-Selektoren oder XPath-Abfragen vertraut bist, empfehlen wir dir, dich an den [Uptrends Support]({{< ref path="contact" lang="de" >}}) zu wenden, sodass dieser die erforderlichen Änderungen vornimmt.

### Aktionseinstellungen

Deine Aktionen verfügen über unterschiedliche Einstellungen – je nach Aktionstyp. Der Knowledge-Base-Artikel [Seiteninteraktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="de" >}}) beschreibt die Einstellungen dieser Aktionen.


## Quellcode selbst schreiben {id="scripting-source-code-directly"}

Du kannst immer auch deine Skripte in einem anderen Editor oder einer anderen Umgebung schreiben und dann das Skript nach Uptrends kopieren (oder schreibe das Skript direkt in unserem Text-Editor). Klicke auf {{< AppElement type="buttonSecondary" >}}Wechsle zum Skript{{< /AppElement >}} oben auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}}, um den Text-Editor zu öffnen. Aus dem Text-Editor gelangst du durch Klicken auf {{< AppElement type="buttonSecondary" >}}Wechsle zum visuellen Editor {{< /AppElement >}} zurück. Beim Wechsel zwischen diesen Skriptoptionen wird das Skript validiert.

![Screenshot Ansicht visueller und Skript-Editor](/img/content/scr_transaction-visual-script-editor-041024.min.png)

## Die Transaktions-API verwenden

Du kannst die API von Uptrends verwenden, um Prüfobjekte zu erstellen, Skripte hochzuladen und zu ändern und den Status deines Prüfobjekts zu überprüfen. Alle verfügbaren Methoden werden in der [API]({{< ref path="support/kb/api" lang="de" >}})-Dokumentation beschrieben.
