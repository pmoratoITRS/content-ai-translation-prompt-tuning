{
  "hero": {
    "title": "Eine Transaktionsvariable anpassen"
  },
  "title": "Eine Transaktionsvariable anpassen",
  "summary": "Bei der Einrichtung eines Transaktionsprüfobjekts möchtest du eventuell Werte extrahieren und anpassen. Die Kontrollaktion *Variable anpassen* ermöglicht dir, den zuvor extrahierten Inhalt zu ändern. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/aktion-variableninhalt-anpassen",
  "translationKey": "[URL_1]
}

Bei einer Transaktion erlaubt dir der Aktionstyp **Inhalt der Variable anpassen**, die Werte einer Variable zu ändern, die in der Aktion [**Prüfe Elementinhalt**]([LINK_URL_1]) im Rahmen eines Transaktionsprüfobjektschritts bestimmt wurden. Die Anpassung erfolgt über einen regulären Ausdruck (RegEx). Die Möglichkeit, den Wert einer Variable zu ändern, kann praktisch sein, wenn du einen Teil oder einen angepassten Teil des Werts nutzen möchtest, der von einem Seitenelement stammt.

[SHORTCODE_1] **Hinweis**: Die Anpassung einer Variable ersetzt den ursprünglichen Wert der Variable. Eine (angepasste) Variable ist ab der Aktion, in der sie definiert/angepasst wurde, und in allen folgenden Aktionen und Schritten verfügbar, bis die Transaktion beendet ist. [SHORTCODE_2]

## Variable definieren [ANCHOR_1]

Lies unseren Knowledge-Base-Artikel zur [Nutzung von Transaktionsvariablen]([LINK_URL_2]), um zu erfahren, wie eine Transaktionsvariable eingerichtet wird.

## Die Variable anpassen [ANCHOR_2]

Im zweiten Teil wirst du die Aktion *Inhalt der Variable anpassen* zum Schritt hinzufügen:

1. Öffne das Transaktionsprüfobjekt, das du ändern möchtest.
2. Wechsele zur Registerkarte [SHORTCODE_3] Schritte [SHORTCODE_4].
3. Öffne den Schritt, in dem du eine Variable ändern möchtest.
4. Klicke auf [SHORTCODE_5] Aktion hinzufügen [SHORTCODE_6].
5. Wähle aus der Liste der **Kontrollaktionen** die Aktion *Inhalt der Variable anpassen* und klicke auf [SHORTCODE_7] Auswählen [SHORTCODE_8], um die Aktion zu dem Schritt hinzuzufügen.

   ![Screenshot Transaktionsaktion Anpassen einer Variable]([LINK_URL_3])

   Die Werte für *Variable*, *Anpassungsart* und *Muster regulärer Ausdruck* sind Pflichtfelder. Die anderen Einstellungen sind optional.

6. Gib den Variablennamen im Format [INLINE_CODE_1] ein. Der Name muss genau so geschrieben sein, wie er unter der [Definition der Variable]([LINK_URL_4]) steht. Groß- und Kleinschreibung werden berücksichtigt.
7. Wähle den *Anpassungstyp*. Dies kann lauten
   - **Behält alles, was mit einem Muster übereinstimmt** – um einen Wert von einer Variable zu extrahieren, der dem *Muster des regulären Ausdrucks* entspricht
   - **Entfernt alles, was mit einem Muster übereinstimmt** – um alles zu extrahieren, außer dem Teil, der dem *Muster des regulären Ausdrucks* entspricht
8. Gib den regulären Ausdruck (RegEx) ein, der zur Anpassung der Variable verwendet werden soll.
   Wenn beispielsweise der Wert der Variable ursprünglich "Your order number is 12345" lautet und deine Bestellnummer immer fünf Ziffern hat, könntest du die Variable auf die Bestellnummer begrenzen, indem du die Einstellung *Behält alles, was mit einem Muster übereinstimmt* in Kombination mit dem regulären Ausdruck [INLINE_CODE_2] als das *Muster des regulären Ausdrucks* nutzt, welches fünf Ziffern in einer Zeile finden wird.
9. Stelle sicher, dass die Anpassung der Variable nach der Übernahme der Variable erfolgt. Du kannst die Aktionen gegebenenfalls in einem Schritt an die gewünschte Stelle ziehen.
10. Klicke auf die [SHORTCODE_9]Speichern[SHORTCODE_10]-Schaltfläche, um alle Änderungen zu sichern.

 Der Wert der angepassten Variable ist bei allen darauffolgenden Aktionen und Schritten bis zum Ende der Transaktion verfügbar. Um dich auf die Variable zu beziehen, nutze den ursprünglichen Namen ({{name}}), den du bei der Definition der Variable vergeben hast. Lies den Abschnitt zur [Übernehmenaktion]([LINK_URL_5]), um mehr über den Einsatz der Variable zum Setzen eines Werts in einem anderen Schritt oder einer Aktion zu erfahren.
