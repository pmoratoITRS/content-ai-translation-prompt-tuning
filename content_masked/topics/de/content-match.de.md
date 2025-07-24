{
  "hero": {
    "title": "Fehlerbedingungen – Seiteninhalt"
  },
  "title": "Fehlerbedingungen – Seiteninhalt",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/content-match",
  "summary": "Inhaltsprüfungen sind eine Möglichkeit zu verifizieren, dass die überwachte Seite den richtigen Inhalt anzeigt.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Es gibt Fälle, in denen nur die Hälfte deines Website-Inhalts korrekt lädt. Fehlende Bereiche und Absätze oder fehlender Text erschweren es Nutzern, auf deiner Website zu navigieren. Handelt es sich um eine E-Commerce-Website, wirkt sich dieses schlechte Nutzererlebnis auf die Performance deiner Website aus und du kannst Umsatzeinbußen erleiden, ohne es zu merken.

## Fehlerbedingung Seiteninhalt

Die Fehlerbedingung Seiteninhalt stellt sicher, dass der Inhalt deiner Website korrekt und vollständig lädt. Du kannst einen beliebigen Text, eine Phrase oder einen regulären Ausdruck angeben, woraufhin ein Abgleich erfolgt, ob dieser Inhalt auf deiner Website angezeigt wird.

![Fehlerbedingung Seiteninhalt]([LINK_URL_1])

## Inhaltsprüfung

Eine Inhaltsprüfung ist eine Liste von dir angegebener Wörter, die das Prüfobjekt als Referenz nutzt und mit dem geladenen Inhalt der Website abgleicht:

- Wenn ein Prüfobjekt beim Prüfen einer Seite den Inhalt *findet*, wird *kein Fehler* gemeldet.
- Wenn ein Prüfobjekt beim Prüfen einer Seite den Inhalt *nicht findet*, wird *ein Fehler* gemeldet.

## Inhaltsprüfung für jeden Prüfobjekttyp

Für unterschiedliche Prüfobjekttypen gibt es verschiedene Inhaltsprüfungen. Die Inhaltsprüfung variiert je nach Prüfobjektkategorie und welche Daten erfasst werden:

### Verfügbarkeitsprüfobjekte

Uptime-Prüfobjekte verifizieren den Seiteninhalt, indem eine GET-Abfrage an die URL deiner Website gesendet wird. Ist die Abfrage erfolgreich, validiert das Prüfobjekt den Inhalt der GET-Antwort deiner Website.

Überwachst du beispielsweise die Website URL: [URL_1] könnten Inhaltsprüfungen wie folgt aussehen:

| Inhaltsprüfungstypen | Beispiele |
|--|--|
| Document Object Model (DOM) oder HTML-Elemente | [SHORTCODE_1]
- [INLINE_CODE_1]
- [INLINE_CODE_2]
- [INLINE_CODE_3] 
[SHORTCODE_2] |
| [SHORTCODE_3] Textinhalte mit [regulärem Ausdruck]([LINK_URL_2]) [SHORTCODE_4] | [SHORTCODE_5]
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
[SHORTCODE_6] |
| [SHORTCODE_7] [Erweiterte]([LINK_URL_3]) Inhaltsprüfung [SHORTCODE_8] | [SHORTCODE_9]
- [INLINE_CODE_4][SHORTCODE_10] |

### Browser-Prüfobjekte

Browser-Prüfobjekte verifizieren Seiteninhalte, indem sie die Seitenquelle der Website überprüfen. Die Seitenquelle ist die rohe Struktur der Website im HTML-Format, einschließlich der Meta-Daten und Style-Informationen.

Überwachst du beispielsweise die Website URL: [URL_2] könnten Inhaltsprüfungen wie folgt aussehen:

| Inhaltsprüfungstypen | Beispiele |
|--|--|
| Document Object Model (DOM) oder HTML-Elemente | [SHORTCODE_11]
- [INLINE_CODE_5]
- [INLINE_CODE_6]
- [INLINE_CODE_7] 
[SHORTCODE_12] |
| [SHORTCODE_13] Textinhalte mit [regulärem Ausdruck]([LINK_URL_4]) [SHORTCODE_14] | [SHORTCODE_15]
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
[SHORTCODE_16] |
| [SHORTCODE_17] [Erweiterte]([LINK_URL_5]) Inhaltsprüfung [SHORTCODE_18] | [SHORTCODE_19]
- [INLINE_CODE_8][SHORTCODE_20] |

[SHORTCODE_21] **Hinweis:** Um die Seitenquelle deiner Website zu öffnen, rufe deine Website auf und drücke die Tasten **Ctrl + U**. Oder klicke die rechte Maustaste an einer beliebigen Stelle auf der Seite und wähle **Seitenquelle anzeigen**. Beachte, dass nicht alle Elemente der Seitenquelle gültig für Inhaltsprüfungen sind.[SHORTCODE_22]

### Multi-Step API (MSA)-Prüfobjekte

MSA-Prüfobjekte führen eine Inhaltsprüfung anhand von **Assertions** (Prüfpunkten) durch. Assertions ermöglichen Prüfungen zu definieren, um zu bestätigen, dass die API-Antwort den Erwartungen entspricht. Man kann schauen, ob beispielsweise der Antwortstatuscode 200 lautet oder ob der JSON-Antworttext einen bestimmten Text enthält. Mehr erfährst du unter [MSA Assertions]([LINK_URL_6]).

### Transaktionsprüfobjekte

Transaktionsprüfobjekte validieren Seiteninhalt, indem sie die Seitenobjekte, die im Browser angezeigt werden, prüfen. Sie prüfen auf spezifizierten Text, Schaltflächen, Bilder und andere Elemente der Benutzeroberfläche, die auf deiner Website sichtbar sind. Transaktionsprüfobjekte nutzen **Inhaltsprüfungen**, die als Aktion für jeden Schritt konfiguriert werden, um zu verifizieren, dass jedes Laden der Seite wie erwartet erfolgt. Beispielsweise kann geprüft werden, ob  der Text "Zum Warenkorb hinzugefügt" auf der Seite erscheint. Mehr Informationen findest du unter [Inhaltsprüfungen]([LINK_URL_7]).

## Arten der Inhaltsprüfung

Im Folgenden siehst du Typen einer Inhaltsprüfung, die es für einige Prüfobjekttypen gibt:

### Inhaltsprüfung mit regulären Ausdrücken {id = "regular-content-match"}

Du kannst eine Inhaltsprüfung mittels regulärer Ausdrücke einrichten. Ein regulärer Ausdruck (abgekürzt regex oder regexp) ist ein spezieller Text-String zur Beschreibung eines Suchmusters. Du kannst eine Inhaltsprüfung bestimmen mit:

- einem einzelnen Wort: [INLINE_CODE_9]
- mehreren Wörtern oder Phrasen in bestimmter Reihenfolge: [INLINE_CODE_10] (beispielsweise müssen  product UND order erscheinen)
- Symbolen, die anderen Elementen entsprechen:
  - [INLINE_CODE_11] – nutzt ein Rufzeichen, um die Bedeutung eines Wortes umzukehren oder zu verneinen. Diese Inhaltsprüfung bedeutet, dass das Wort *error* auf der Seite nicht zu sehen sein soll.
  - [INLINE_CODE_12] – nutzt einen Senkrechtstrich, um einem anderen Wort zu gleichen. Diese Inhaltsprüfung bedeutet, dass [INLINE_CODE_13] ODER [INLINE_CODE_14] auf der Website zu sehen sein sollten.

Weitere Informationen findest du unter [Sprachelemente für reguläre Ausdrücke – Kurzübersicht]([LINK_URL_8]).


### Erweiterte Inhaltsprüfung

Du kannst mehrere Übereinstimmungsmuster gleichzeitig verwenden, indem du die Werte im JSON-Format speicherst. Wenn du zwei Muster kombinieren möchtest, die jede beliebige Art Seitenobjekt und regulären Ausdruck umfassen können, nutze:

[CODE_BLOCK_1]

Gib eine gültige Übereinstimmung im Feld [INLINE_CODE_15] ein. Setze [INLINE_CODE_16] auf [INLINE_CODE_17], wenn das Muster deinem Website-Inhalt entsprechen soll, oder auf [INLINE_CODE_18], wenn es mit keinem Inhalt der Website übereinstimmt.  

[SHORTCODE_23] **Hinweis:** Die erweiterte Inhaltsprüfung gibt es für HTTPS-, Webservices HTTP- und HTTPS- sowie Full Pagecheck-Prüfobjekte. [SHORTCODE_24]

Möchtest du den Zeitstempel deiner Website für die Inhaltsprüfung sehen, verwende:

[CODE_BLOCK_2]

Der JSON-Schlüssel [INLINE_CODE_19] kann Werte in regex-Form wie \[HTML_TAG_1], \[HTML_TAG_2], \[HTML_TAG_3], \[HTML_TAG_4], \[HTML_TAG_5] und \[HTML_TAG_6] enthalten. Jeder dieser Werte kann vom Website-Inhalt extrahiert werden und wird mit der aktuellen Server-Zeit zusammengeführt und dann in Bezug auf den UTC bewertet.

[INLINE_CODE_20] ist die Zahl der Minuten, die subtrahiert werden sollte, um sie mit der Server-Zeit in UTC zu vergleichen. Wenn die Webseite einen Zeitstempel in UTC\+1 enthält, sollte der Ausgleich 60 betragen. Wenn die Webseite einen Zeitstempel in EST (UTC-5) enthält, sollte der Ausgleich -300 betragen.

[INLINE_CODE_21] bezieht sich auf den maximalen Zeitunterschied in Minuten, der zwischen der Webseitenzeit und deiner Ortszeit erlaubt ist. Wenn beispielsweise deine Ortszeit 10:06 Uhr ist und die Webseitenzeit 10:00 Uhr, wird ein Fehler angezeigt, wenn [INLINE_CODE_22] auf 5 Minuten oder darunter gesetzt ist.

## Die Inhaltsprüfung konfigurieren

Um eine Inhaltsprüfung zu konfigurieren, ist eine Fehlerbedingung des Typs **Prüfe Seiteninhalt** notwendig:

1. Gehe zu [SHORTCODE_25]Überwachung > Prüfobjekteinrichtung[SHORTCODE_26].
2. Wähle das Prüfobjekt, zu dem du eine Inhaltsprüfung hinzufügen möchtest.  
3. Wechsle zur Registerkarte [SHORTCODE_27] Fehlerbedingungen [SHORTCODE_28].  
4. Gib unter **Prüfe Seiteninhalt** die Informationen zum Übereinstimmungsmuster ein.
5. Klicke auf [SHORTCODE_29] Speichern [SHORTCODE_30], um alle Änderungen zu bestätigen.

Ist dies erfolgt, kannst du eine [Meldedefinition erstellen]([LINK_URL_9]), um benachrichtigt zu werden, wenn die Fehlerbedingung unter **Prüfe Seiteninhalt** erfüllt wird.
