{
  "hero": {
    "title": "Selectoralternatieven"
  },
  "title": "Selectoralternatieven zoeken",
  "summary": "Soms werken selectors niet of maar een deel van de tijd. In dit artikel worden we enkele veelvoorkomende selectorproblemen en mogelijke oplossingen besproken.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/selector-alternatieven",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u een specifiek pagina-element in uw transactiescript moet identificeren, gebruikt u een XPath- of CSS-selector. U kunt meerdere selectorkeuzes hebben om een typisch element te specificeren, maar sommige selectors zijn problematischer dan andere. Dus voor het vinden van de juiste kunnen enkele slimme toepassingen van XPath- of CSS-selectors nodig zijn.

Als u de Transaction Recorder gebruikt om het klikpad van uw gebruiker vast te leggen, [past de recorder algoritmes toe]([LINK_URL_1]) om te kiezen wat volgens hem uw beste selectoroptie is. Omdat de Transaction Recorder slechts één momentopname krijgt van hoe uw paginastructuur eruitziet, is de selector die hij kiest misschien niet uw beste keuze. In dit artikel bespreken we enkele situaties en oplossingen die u kunt overwegen bij het zoeken naar alternatieve selectors.

## Veelvoorkomende oorzaken van slechte selectorbepaling

Er kunnen tal van factoren een rol spelen die ervoor zorgen dat uw selector niet werkt zoals u verwacht. Uw tests kunnen bijvoorbeeld resulteren in fouten zoals "Element not found". Slechte selectorkeuzes kunnen de oorzaak zijn van uw problemen. Laten we eens kijken naar een paar van de redenen voor scriptfouten.

### Dynamische ID's

Sommige elementen krijgen elke keer dat de server de pagina verstuurt een nieuwe ID, dus als uw selector verwijst naar de dynamische ID, faalt de selector wanneer uw script het element probeert te vinden. Er zijn een paar verschillende manieren om deze problemen op te lossen. 
  
Voor de volgende voorbeelden gebruiken we een invoerelement voor het selecteren van het item quantity in het HTML-fragment.

    [HTML_TAG_1] 
      [HTML_TAG_2] 
    [HTML_TAG_3]

De ID voor de invoer is deels vast en deels gegenereerd, wat fouten veroorzaakt bij het verwijzen naar de ID zoals vastgelegd door de Transaction Recorder. De Transaction Recorder raadt aan:  
XPath: [INLINE_CODE_1] CSS selector: [INLINE_CODE_2]  
Beide mislukken wanneer ze in de transactie worden gebruikt. U heeft verschillende opties om het probleem op te lossen.

-   **Gebruik een element attribute dat niet verandert**. Door te verwijzen naar een ander element attribute, zoals een elementnaam, kunt u een stabiele selector tot stand brengen.  
    [INLINE_CODE_3]
-   **Gebruik een relatief pad om door het DOM te navigeren**. De bovenstaande HTML-node is genest in een bovenliggende [INLINE_CODE_4]-node. Met XPath kunnen we verwijzen naar het invoerelement in het bovenliggende element. De onderstaande code lokaliseert het bovenliggende gevolgd door het onderliggende invoerelement.  
    //div\[@class="quantity"\]/input
-   **Gebruik een relatief XPath met** [INLINE_CODE_5] of [INLINE_CODE_6]. Als de ID deels vast en deels dynamisch is, zoals [INLINE_CODE_7] waarbij het gedeelte "[INLINE_CODE_8]" verandert, maar het gedeelte "[INLINE_CODE_9]" van de ID hetzelfde blijft, kunt u verwijzen naar het gedeelte dat niet verandert. Bijvoorbeeld,  
    [INLINE_CODE_10]  
    of  
    [INLINE_CODE_11]
-   **Voeg element attributes toe voor transactie tests**. Laat uw ontwikkelaars u bijstaan door speciale element attributes voor tests toe te voegen die niet veranderen. Laten we bijvoorbeeld zeggen dat u een element heeft met een dynamische ID zoals  
    [INLINE_CODE_12]  
    In dit geval heeft u niets concreets om het element te identificeren, zoals een naam attribute. Als u een andere attribute toevoegt, zoals “data-test-id,” met een statische waarde, kunt u het element altijd vinden. Een toegevoegde attribute kan er ongeveer zo uitzien  
    [INLINE_CODE_13]
-   **Identificeer elementen door meerdere element attributes te gebruiken**. Als uw opties [INLINE_CODE_14] of [INLINE_CODE_15] voor het identificeren van een element niet werken omdat de andere elementen op de pagina hetzelfde voor- of achtervoegsel gebruiken met het dynamische gedeelte, kunt u soms meerdere attributes gebruiken om het element te identificeren met XPath.  
    [INLINE_CODE_16]`[INLINE_CODE_17][SYSTEM_VAR_1]` te gebruiken.

### Krijg hulp van Support

Self-Service Transacties betekent niet dat we u aan uw lot hebben overgelaten. Onze supportmedewerkers staan klaar om u te helpen. Ons ervaren transactieteam heeft het allemaal eerder gezien en ze zijn geweldig in het vinden van alternatieve selectors. Open gewoon een [support ticket]([LINK_URL_8]) en vertel ze over uw uitdaging.
