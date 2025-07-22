{
  "hero": {
    "title": "Vergelijkingsoperatoren in Multi-step monitoring"
  },
  "title": "Vergelijkingsoperatoren in Multi-step monitoring",
  "summary": "Leer welke vergelijkingsoperatoren beschikbaar zijn bij het configureren  van Multi-Step API monitoring.",
  "url": "support/kb/synthetic-monitoring/api-monitoring/vergelijkingsoperatoren-in-multi-step-monitoring",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-comparison-operations",
  "tableofcontents": false
}

Wanneer u een assertion creëert voor een van de stappen in een [multi-step controleregel]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}, moet u definiëren wat voor soort controle wij moeten uitvoeren. Kies een van de onderstaande opties. In de beschrijving van elke optie verwijst *source* naar de waarde van het HTTP-responskenmerk dat u wilt inspecteren; *target value* is de vaste waarde waarmee we vergelijken.

-   **Is gelijk aan**: de bron moet gelijk zijn aan de doelwaarde. We voeren een niet-hoofdlettergevoelige vergelijking uit.

-   **Is niet gelijk aan**: de bron mag NIET gelijk zijn aan de doelwaarde. We voeren een niet-hoofdlettergevoelige vergelijking uit.

-   **Bevat**: de bron moet de doelwaarde bevatten. De bron- en doelwaarden worden beide geïnterpreteerd als tekst (zelfs als ze alleen een getal bevatten) en de doelwaarde moet ergens in de tekst van de bronwaarde voorkomen.

-   **Bevat niet**: de bron mag NIET de doelwaarde bevatten.

-   **Is kleiner dan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron < doel moet waar zijn.

-   **Is kleiner dan of gelijk aan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron <= doel moet waar zijn.

-   **Is groter dan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron > doel moet waar zijn.

-   **Is groter dan of gelijk aan**: bron- en doelwaarde moeten beide een getal zijn en de voorwaarde bron >= doel moet waar zijn.

-   **Is leeg**: bron moet een lege string bevatten (bijv. `"source": ""`).

-   **Is niet leeg**: bron moet wat tekst of een getal bevatten.

-   **Is null**: bron moet de waarde `null` hebben (bijv. `"source": null`).

-   **Is niet null**: bron mag NIET de waarde `null` hebben.

-   **Bestaat**: bron moet bestaan in de response.

-   **Bestaat niet**: bron mag NIET bestaan in de response.

-   **Moet genegeerd worden**: geeft aan dat er geen automatische controle op de bronwaarde moet worden uitgevoerd. Deze optie kan worden gebruikt om de automatische assertions in de velden Status code en Response complete op te heffen. (zie [Brontypes and eigenschappen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="nl" >}})
