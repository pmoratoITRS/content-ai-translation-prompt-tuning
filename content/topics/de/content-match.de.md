{
  "hero": {
    "title": "Fehlerbedingungen – Seiteninhalt"
  },
  "title": "Fehlerbedingungen – Seiteninhalt",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/content-match",
  "summary": "Inhaltsprüfungen sind eine Möglichkeit zu verifizieren, dass die überwachte Seite den richtigen Inhalt anzeigt.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/content-match"
}

Es gibt Fälle, in denen nur die Hälfte deines Website-Inhalts korrekt lädt. Fehlende Bereiche und Absätze oder fehlender Text erschweren es Nutzern, auf deiner Website zu navigieren. Handelt es sich um eine E-Commerce-Website, wirkt sich dieses schlechte Nutzererlebnis auf die Performance deiner Website aus und du kannst Umsatzeinbußen erleiden, ohne es zu merken.

## Fehlerbedingung Seiteninhalt

Die Fehlerbedingung Seiteninhalt stellt sicher, dass der Inhalt deiner Website korrekt und vollständig lädt. Du kannst einen beliebigen Text, eine Phrase oder einen regulären Ausdruck angeben, woraufhin ein Abgleich erfolgt, ob dieser Inhalt auf deiner Website angezeigt wird.

![Fehlerbedingung Seiteninhalt](/img/content/scr-error-condition-page-content.min.png)

## Inhaltsprüfung

Eine Inhaltsprüfung ist eine Liste von dir angegebener Wörter, die das Prüfobjekt als Referenz nutzt und mit dem geladenen Inhalt der Website abgleicht:

- Wenn ein Prüfobjekt beim Prüfen einer Seite den Inhalt *findet*, wird *kein Fehler* gemeldet.
- Wenn ein Prüfobjekt beim Prüfen einer Seite den Inhalt *nicht findet*, wird *ein Fehler* gemeldet.

## Inhaltsprüfung für jeden Prüfobjekttyp

Für unterschiedliche Prüfobjekttypen gibt es verschiedene Inhaltsprüfungen. Die Inhaltsprüfung variiert je nach Prüfobjektkategorie und welche Daten erfasst werden:

### Verfügbarkeitsprüfobjekte

Uptime-Prüfobjekte verifizieren den Seiteninhalt, indem eine GET-Abfrage an die URL deiner Website gesendet wird. Ist die Abfrage erfolgreich, validiert das Prüfobjekt den Inhalt der GET-Antwort deiner Website.

Überwachst du beispielsweise die Website URL: https://galacticresorts.com/, könnten Inhaltsprüfungen wie folgt aussehen:

| Inhaltsprüfungstypen | Beispiele |
|--|--|
| Document Object Model (DOM) oder HTML-Elemente | {{< tableformatter >}}
- `<title>Home Page - GalacticResorts.com</title>`
- `<a class="btn btn-primary btn-lg" href="/Products/Index/97f8fcc9-11b5-4d86-b208-ccb6d2be35e3">Book now!</a>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Textinhalte mit [regulärem Ausdruck]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="de" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
{{< /tableformatter >}} |
| {{< tableformatter >}} [Erweiterte]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="de" >}}) Inhaltsprüfung {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "GalacticResottt", "IsPositive": false }]`{{< /tableformatter >}} |

### Browser-Prüfobjekte

Browser-Prüfobjekte verifizieren Seiteninhalte, indem sie die Seitenquelle der Website überprüfen. Die Seitenquelle ist die rohe Struktur der Website im HTML-Format, einschließlich der Meta-Daten und Style-Informationen.

Überwachst du beispielsweise die Website URL: https://galacticresorts.com/, könnten Inhaltsprüfungen wie folgt aussehen:

| Inhaltsprüfungstypen | Beispiele |
|--|--|
| Document Object Model (DOM) oder HTML-Elemente | {{< tableformatter >}}
- `<h2>Norcadia Prime</h2>`
- `<li><a href="/APIHelp" target="_blank">API</a></li>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Textinhalte mit [regulärem Ausdruck]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="de" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
{{< /tableformatter >}} |
| {{< tableformatter >}} [Erweiterte]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="de" >}}) Inhaltsprüfung {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "Holiday destinations", "IsPositive": true }]`{{< /tableformatter >}} |

{{< callout >}} **Hinweis:** Um die Seitenquelle deiner Website zu öffnen, rufe deine Website auf und drücke die Tasten **Ctrl + U**. Oder klicke die rechte Maustaste an einer beliebigen Stelle auf der Seite und wähle **Seitenquelle anzeigen**. Beachte, dass nicht alle Elemente der Seitenquelle gültig für Inhaltsprüfungen sind.{{< /callout >}}

### Multi-Step API (MSA)-Prüfobjekte

MSA-Prüfobjekte führen eine Inhaltsprüfung anhand von **Assertions** (Prüfpunkten) durch. Assertions ermöglichen Prüfungen zu definieren, um zu bestätigen, dass die API-Antwort den Erwartungen entspricht. Man kann schauen, ob beispielsweise der Antwortstatuscode 200 lautet oder ob der JSON-Antworttext einen bestimmten Text enthält. Mehr erfährst du unter [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="de" >}}).

### Transaktionsprüfobjekte

Transaktionsprüfobjekte validieren Seiteninhalt, indem sie die Seitenobjekte, die im Browser angezeigt werden, prüfen. Sie prüfen auf spezifizierten Text, Schaltflächen, Bilder und andere Elemente der Benutzeroberfläche, die auf deiner Website sichtbar sind. Transaktionsprüfobjekte nutzen **Inhaltsprüfungen**, die als Aktion für jeden Schritt konfiguriert werden, um zu verifizieren, dass jedes Laden der Seite wie erwartet erfolgt. Beispielsweise kann geprüft werden, ob  der Text "Zum Warenkorb hinzugefügt" auf der Seite erscheint. Mehr Informationen findest du unter [Inhaltsprüfungen]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}).

## Arten der Inhaltsprüfung

Im Folgenden siehst du Typen einer Inhaltsprüfung, die es für einige Prüfobjekttypen gibt:

### Inhaltsprüfung mit regulären Ausdrücken {id = "regular-content-match"}

Du kannst eine Inhaltsprüfung mittels regulärer Ausdrücke einrichten. Ein regulärer Ausdruck (abgekürzt regex oder regexp) ist ein spezieller Text-String zur Beschreibung eines Suchmusters. Du kannst eine Inhaltsprüfung bestimmen mit:

- einem einzelnen Wort: `Uptrends`
- mehreren Wörtern oder Phrasen in bestimmter Reihenfolge: `product.*order` (beispielsweise müssen  product UND order erscheinen)
- Symbolen, die anderen Elementen entsprechen:
  - `!error` – nutzt ein Rufzeichen, um die Bedeutung eines Wortes umzukehren oder zu verneinen. Diese Inhaltsprüfung bedeutet, dass das Wort *error* auf der Seite nicht zu sehen sein soll.
  - `On Sale|Best Sellers` – nutzt einen Senkrechtstrich, um einem anderen Wort zu gleichen. Diese Inhaltsprüfung bedeutet, dass `On Sale` ODER `Best Sellers` auf der Website zu sehen sein sollten.

Weitere Informationen findest du unter [Sprachelemente für reguläre Ausdrücke – Kurzübersicht](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference).


### Erweiterte Inhaltsprüfung

Du kannst mehrere Übereinstimmungsmuster gleichzeitig verwenden, indem du die Werte im JSON-Format speicherst. Wenn du zwei Muster kombinieren möchtest, die jede beliebige Art Seitenobjekt und regulären Ausdruck umfassen können, nutze:

```json
    [
      {
        "Pattern": "PhraseA",
        "IsPositive": true
      },
      { 
        "Pattern": "PhraseB", 
        "IsPositive": false 
      }
    ]
```

Gib eine gültige Übereinstimmung im Feld `Pattern` ein. Setze `IsPositive` auf `true`, wenn das Muster deinem Website-Inhalt entsprechen soll, oder auf `false`, wenn es mit keinem Inhalt der Website übereinstimmt.  

{{< callout >}} **Hinweis:** Die erweiterte Inhaltsprüfung gibt es für HTTPS-, Webservices HTTP- und HTTPS- sowie Full Pagecheck-Prüfobjekte. {{< /callout >}}

Möchtest du den Zeitstempel deiner Website für die Inhaltsprüfung sehen, verwende:

```json
    [
    {
      "Pattern": "some content before the timestamp value (?<hour>\\d\\d):(?<minute>\\d\\d)",
      "IsPositive": true,
      "DateTime": { 
        "OffsetUTC": 60, 
        "MaxDifference": 5 
      } 
    } 
    ]
```

Der JSON-Schlüssel `Pattern` kann Werte in regex-Form wie \<year\>, \<month\>, \<day\>, \<hour\>, \<minute\> und \<second\> enthalten. Jeder dieser Werte kann vom Website-Inhalt extrahiert werden und wird mit der aktuellen Server-Zeit zusammengeführt und dann in Bezug auf den UTC bewertet.

`OffsetUTC` ist die Zahl der Minuten, die subtrahiert werden sollte, um sie mit der Server-Zeit in UTC zu vergleichen. Wenn die Webseite einen Zeitstempel in UTC\+1 enthält, sollte der Ausgleich 60 betragen. Wenn die Webseite einen Zeitstempel in EST (UTC-5) enthält, sollte der Ausgleich -300 betragen.

`MaxDifference` bezieht sich auf den maximalen Zeitunterschied in Minuten, der zwischen der Webseitenzeit und deiner Ortszeit erlaubt ist. Wenn beispielsweise deine Ortszeit 10:06 Uhr ist und die Webseitenzeit 10:00 Uhr, wird ein Fehler angezeigt, wenn `MaxDifference` auf 5 Minuten oder darunter gesetzt ist.

## Die Inhaltsprüfung konfigurieren

Um eine Inhaltsprüfung zu konfigurieren, ist eine Fehlerbedingung des Typs **Prüfe Seiteninhalt** notwendig:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Wähle das Prüfobjekt, zu dem du eine Inhaltsprüfung hinzufügen möchtest.  
3. Wechsle zur Registerkarte {{< AppElement type="tab" >}} Fehlerbedingungen {{< /AppElement >}}.  
4. Gib unter **Prüfe Seiteninhalt** die Informationen zum Übereinstimmungsmuster ein.
5. Klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}, um alle Änderungen zu bestätigen.

Ist dies erfolgt, kannst du eine [Meldedefinition erstellen]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="de" >}}), um benachrichtigt zu werden, wenn die Fehlerbedingung unter **Prüfe Seiteninhalt** erfüllt wird.
