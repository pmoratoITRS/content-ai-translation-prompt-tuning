{
  "hero": {
    "title": "Vergelijkingsoperatoren in Multi-step monitoring"
  },
  "title": "Vergelijkingsoperatoren in Multi-step monitoring",
  "summary": "Leer welke vergelijkingsoperatoren beschikbaar zijn bij het configureren  van Multi-Step API monitoring.",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Wanneer u een assertion creëert voor een van de stappen in een [multi-step controleregel]([LINK_URL_1]) en de doelwaarde moet ergens in de tekst van de bronwaarde voorkomen.

-   **Bevat niet**: de bron mag NIET de doelwaarde bevatten.

-   **Is kleiner dan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron [HTML_TAG_1] doel moet waar zijn.

-   **Is groter dan of gelijk aan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron >= doel moet waar zijn.

-   **Is leeg**: bron moet een lege string bevatten (bijv. [INLINE_CODE_1]).

-   **Is niet leeg**: bron moet wat tekst of een getal bevatten.

-   **Is null**: bron moet de waarde [INLINE_CODE_2] hebben (bijv. [INLINE_CODE_3]).

-   **Is niet null**: bron mag NIET de waarde [INLINE_CODE_4] hebben.

-   **Bestaat**: bron moet bestaan in de response.

-   **Bestaat niet**: bron mag NIET bestaan in de response.

-   **Moet genegeerd worden**: geeft aan dat er geen automatische controle op de bronwaarde moet worden uitgevoerd. Deze optie kan worden gebruikt om de automatische assertions in de velden Status code en Response complete op te heffen. (zie [Brontypes and eigenschappen]([LINK_URL_2])
