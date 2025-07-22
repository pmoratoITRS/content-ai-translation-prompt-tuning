{
  "hero": {
    "title": "Selector voor de Transaction Recorder bepalen"
  },
  "title": "Selector voor de Transaction Recorder bepalen",
  "summary": "Als u de Transaction Recorder gebruikt, bepaalt de recorder op basis van verschillende factoren hoe de afzonderlijke elementen op de pagina worden geïdentificeerd. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transaction-recorder-selector-bepalen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u de Transaction Recorder gebruikt, retourneert de recorder een lange lijst met mogelijke selectors die Uptrends gebruikt in uw Self-Service Transaction-stappen om een pagina-element te identificeren. Elke stap of actie gebruikt slechts één van deze selectors in uw script. Daarom gebruikt Uptrends een algoritme om de beste selector te bepalen.

## Selectors

Terwijl u uw transactie opneemt met de Transaction Recorder, genereert de recorder, terwijl u met de verschillende pagina-elementen interacteert, een lijst met mogelijke selectors om elk element te identificeren. De lijst met mogelijke selectors bevat verschillende tekst-, ID-, CSS- en XPath-selectors. De Transaction Recorder genereert een lijst met de mogelijke selectors voor elk element. De recorder zelf bevat geen logica om de ene selector boven de andere te kiezen, dus nemen de Uptrends-servers deze beslissing tijdens het conversieproces.

Om de beste selectors te selecteren kijkt Uptrends naar de waarde van de selectors en kiest een selectorwaarde en -type dat niet te vaag of te ingewikkeld is en ook niet vaak op de pagina voorkomt.

[SHORTCODE_1]
**Opmerking**: U kunt de andere selectors bekijken door te klikken op de ellips [SHORTCODE_3]...[SHORTCODE_4] in het veld selectorwaarde.
[SHORTCODE_2]

## Selectieproces

De volgende stappen worden uitgevoerd om de beste selector te vinden:

1.  **Normalisatie**: Het normalisatieproces filtert alle selectors uit die dezelfde waarde hebben en op dezelfde kenmerken selecteren.
2.  **Het verwijderen van niet-ondersteunde locators**: Het proces verwijdert alle selectors die Self Service Transacties niet ondersteunen (tekstselectors).
3.  **Prioritering van de elementtypen**: Het proces geeft prioriteit aan selectors op basis van type (in volgorde van prioriteit): tekst, ID, naam, CSS, XPath (tekst), XPath (attributes), XPath (index), XPath (node).
4.  **Prioritering van kortere selectors boven langere**: Uptrends geeft prioriteit aan de selector op basis van het aantal tekens in de string en geeft prioriteit aan de kortste selector.
5.  **Prioritering van het aantal overeenkomende elementen**: Elke selector kan meerdere elementen op de pagina hebben met dezelfde beschrijving, dus dit proces geeft prioriteit aan selectors op basis van uniciteit.
6.  **Prioritering van selectors met één overeenkomst**: Uptrends geeft de hoogste prioriteit aan selectors die slechts met één element op de pagina overeenkomen.
7.  **Definitieve selectie**: In de resulterende lijst zijn de selectors geprioriteerd en Uptrends kiest de eerste selector in de lijst voor de actie.
