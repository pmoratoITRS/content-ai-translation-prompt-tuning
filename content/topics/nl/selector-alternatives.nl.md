{
  "hero": {
    "title": "Selectoralternatieven"
  },
  "title": "Selectoralternatieven zoeken",
  "summary": "Soms werken selectors niet of maar een deel van de tijd. In dit artikel worden we enkele veelvoorkomende selectorproblemen en mogelijke oplossingen besproken.",
  "url": "/support/kb/synthetic-monitoring/transacties/selector-alternatieven",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/selector-alternatives"
}

Als u een specifiek pagina-element in uw transactiescript moet identificeren, gebruikt u een XPath- of CSS-selector. U kunt meerdere selectorkeuzes hebben om een typisch element te specificeren, maar sommige selectors zijn problematischer dan andere. Dus voor het vinden van de juiste kunnen enkele slimme toepassingen van XPath- of CSS-selectors nodig zijn.

Als u de Transaction Recorder gebruikt om het klikpad van uw gebruiker vast te leggen, [past de recorder algoritmes toe]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="nl" >}}) om te kiezen wat volgens hem uw beste selectoroptie is. Omdat de Transaction Recorder slechts één momentopname krijgt van hoe uw paginastructuur eruitziet, is de selector die hij kiest misschien niet uw beste keuze. In dit artikel bespreken we enkele situaties en oplossingen die u kunt overwegen bij het zoeken naar alternatieve selectors.

## Veelvoorkomende oorzaken van slechte selectorbepaling

Er kunnen tal van factoren een rol spelen die ervoor zorgen dat uw selector niet werkt zoals u verwacht. Uw tests kunnen bijvoorbeeld resulteren in fouten zoals "Element not found". Slechte selectorkeuzes kunnen de oorzaak zijn van uw problemen. Laten we eens kijken naar een paar van de redenen voor scriptfouten.

### Dynamische ID's

Sommige elementen krijgen elke keer dat de server de pagina verstuurt een nieuwe ID, dus als uw selector verwijst naar de dynamische ID, faalt de selector wanneer uw script het element probeert te vinden. Er zijn een paar verschillende manieren om deze problemen op te lossen. 
  
Voor de volgende voorbeelden gebruiken we een invoerelement voor het selecteren van het item quantity in het HTML-fragment.

    <div class="quantity"> 
      <input type="number" id="quantity_5e5653081acc7" class="input-text qty text"
      step="1" min="1" max="" name="quantity" value="1" title="Qty" size="4" 
      pattern="[0-9]*"inputmode="numeric"
      aria-labelledby="Suraya Bay T-Shirt quantity"> 
    </div>

De ID voor de invoer is deels vast en deels gegenereerd, wat fouten veroorzaakt bij het verwijzen naar de ID zoals vastgelegd door de Transaction Recorder. De Transaction Recorder raadt aan:  
XPath: `//input[@id="quantity_5e5653081acc7"])[1] ` CSS selector: `input#quantity_5e5653081acc7`  
Beide mislukken wanneer ze in de transactie worden gebruikt. U heeft verschillende opties om het probleem op te lossen.

-   **Gebruik een element attribute dat niet verandert**. Door te verwijzen naar een ander element attribute, zoals een elementnaam, kunt u een stabiele selector tot stand brengen.  
    `//input[@name="quantity"]`
-   **Gebruik een relatief pad om door het DOM te navigeren**. De bovenstaande HTML-node is genest in een bovenliggende `<div>`-node. Met XPath kunnen we verwijzen naar het invoerelement in het bovenliggende element. De onderstaande code lokaliseert het bovenliggende gevolgd door het onderliggende invoerelement.  
    //div\[@class="quantity"\]/input
-   **Gebruik een relatief XPath met** `contains` of `starts with`. Als de ID deels vast en deels dynamisch is, zoals `id="quantity_5e5653081acc7"` waarbij het gedeelte "`5e5653081acc7`" verandert, maar het gedeelte "`quantity_`" van de ID hetzelfde blijft, kunt u verwijzen naar het gedeelte dat niet verandert. Bijvoorbeeld,  
    `//select[starts with (@id, "quantity_")]`  
    of  
    `//select[contains(@id, "quantity")]`
-   **Voeg element attributes toe voor transactie tests**. Laat uw ontwikkelaars u bijstaan door speciale element attributes voor tests toe te voegen die niet veranderen. Laten we bijvoorbeeld zeggen dat u een element heeft met een dynamische ID zoals  
    `<button id=”i2fe4owf” class=”btn”>`  
    In dit geval heeft u niets concreets om het element te identificeren, zoals een naam attribute. Als u een andere attribute toevoegt, zoals “data-test-id,” met een statische waarde, kunt u het element altijd vinden. Een toegevoegde attribute kan er ongeveer zo uitzien  
    `<button id=”i2fe4owf” class=”btn” data-test-id =”shoppingcart-test-step2”>`
-   **Identificeer elementen door meerdere element attributes te gebruiken**. Als uw opties `contains` of `starts with` voor het identificeren van een element niet werken omdat de andere elementen op de pagina hetzelfde voor- of achtervoegsel gebruiken met het dynamische gedeelte, kunt u soms meerdere attributes gebruiken om het element te identificeren met XPath.  
    `//select[starts-with(@id, "quantity_" and contains(@class, "qty text")]```

### Meertalige sites

Als u een meertalige website heeft, verandert de pagina vaak van taal op basis van de locatie van de gebruiker. Als het door u geselecteerde controlestation zich in een regio bevindt die taalomschakelingen triggert, kan uw transactiecontroleregel, afhankelijk van hoe u het element heeft geïdentificeerd, mislukken. Als de taal van invloed is op uw inhoud, kunt u in uw selectors beter andere opties gebruiken dan labelwaarden of specifieke woorden op de pagina.

### Dynamische inhoud

Sommige sites gebruiken dynamische inhoud op basis van zaken als seizoenspromoties, feestdagen, gebruikerslogins, cookies of locatiegegevens. De verschuivingen in data veroorzaakt door variaties in de dynamische inhoud kunnen ervoor zorgen dat transactiecontroleregels mislukken. Dynamische inhoud lijkt veel op dynamische ID's, maar de elementen van de hele pagina veranderen met elke serverrequest (denk aan uw Amazon-pagina's met zijn voortdurend veranderende productaanbevelingen). Hoewel de details veranderen, verandert de structuur meestal niet. Door naar elementen te verwijzen op basis van waar ze zich in het DOM bevinden in plaats van op de attributes van het huidige element, zult u betere resultaten krijgen.

Denk bijvoorbeeld aan een e-commercesite die items op de pagina weergeeft op basis van itempopulariteit. De items wisselen bijna elke keer dat de pagina wordt geladen. In plaats van een selector te gebruiken die een item identificeert aan zijn naam of een andere attribute die specifiek is voor een item, is het waarschijnlijk het beste om een relatieve padselector te gebruiken die het eerste item in een lijst kiest, ongeacht welk item wordt weergegeven.

### Verborgen elementen

Fouten als gevolg van verborgen elementen zijn niet per se het gevolg van een slechte selector; in plaats daarvan kan uw selector mislukken omdat u een vervolgactie mist. Dus als u fouten krijgt die melden dat het script het element heeft gevonden, maar dat het element niet zichtbaar is, heeft uw script mogelijk een extra actie nodig voordat u de interactie probeert. Onthoud dat het script, net als uw gebruikers, geen interactie kan hebben met onzichtbare elementen.

**Ontbrekende hoveractie**:

Een ontbrekende hoveractie veroorzaakt fouten. Een menu-item wordt mogelijk pas zichtbaar als de gebruiker de aanwijzer boven een menu-item houdt om het vervolgmenu te genereren. Door de hover-interactie toe te voegen, wordt het element zichtbaar en beschikbaar voor interactie.

**Ontbrekende scrollactie**:

Vaak laden pagina's alleen elementen wanneer de gebruiker die nodig heeft om de illusie van hogere prestaties te wekken en om het datagebruik te verminderen. Terwijl de gebruiker op de pagina naar beneden scrollt, wordt de inhoud geladen. Zonder de scrollactie worden de elementen niet weergegeven en beschikbaar gemaakt voor de interactie van het script. Het toevoegen van een scrollactie lost het probleem op. Let wel, de scrollactie kan alleen momenteel zichtbare elementen zien. Mogelijk moet u twee of meer scrollacties toevoegen voordat het doelelement zichtbaar is op de pagina.

{{< callout >}}
**Opmerking**: De recorder legt geen scroll- en [hoveracties]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="nl" >}}), vast, dus u moet deze acties handmatig toevoegen aan uw script.
{{< /callout >}}

**Verborgen in het DOM maar zichtbaar op het scherm**:

U kunt ook fouten krijgen vanwege elementen die u duidelijk op de pagina kunt zien, maar het element is verborgen in het DOM. Veelvoorkomende voorbeelden van dit probleem zijn keuzerondjes of selectievakjes bedekt door labels. De recorder legt de klikactie op het keuzerondje of selectievakje vast; hoewel die elementen niet zichtbaar zijn voor het DOM, zijn de labels wel zichtbaar. Om het probleem op te lossen schakelt u de klikactie om naar het label dat het element bedekt.

## Selectors wijzigen

Als u problemen heeft ondervonden met uw selectors, kunt u verschillende stappen ondernemen om het probleem op te lossen.

### Gebruik de selectorkiezer

Toen Uptrends uw opname naar een script converteerde, besloot Uptrends op basis van een algoritme welke selector moest worden gebruikt; de recorder kan echter een slechte keuze hebben gemaakt, dus moet u ingrijpen. Uptrends maakt dit gemakkelijk door uw alternatieve selectors voor u beschikbaar te houden. Om toegang te krijgen tot de alternatieve selectors doet u het volgende:

1.  Klik op het grijze vierkant met drie stippen in het selectieveld om het selectordialoogvenster te openen. 
![Knop selectorkiezer ](/img/content/ed5d9588-d944-402f-9899-5ba46a574c2b.png)  

2.  Kies een andere selector in de lijst.
![Dialoogvenster selectorkiezer](/img/content/c8a2a635-1e85-4c3b-b84b-2b1edbe4dd15.png)  

U kunt elk van de selectors in de lijst kiezen en testen. Als geen ervan goed werkt voor u en u er liever niet zelf een schrijft, helpt ons [Support team](/contact) u graag om een oplossing te vinden die wel werkt voor u.

{{< callout >}}
**Opmerking**: Als u met een ouder script werkt, zijn de selectors in de Selectorkiezer waarschijnlijk verouderd. Het kan zijn dat u de nieuwe selector zelf moet schrijven of laat [Support](/contact) u helpen.
{{< /callout >}}

### Schrijf zelf de selector

Als u vertrouwd bent met het werken met selectors of als u ontwikkelaars bij de hand heeft om u te helpen, kunt u uw eigen CSS- of XPath-selectors schrijven. Wie uw selectors ook schrijft, test ze altijd uitvoerig. 

Merk op dat u [automatische variabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}) in de selector kunt gebruiken, u zou bijvoorbeeld een willekeurig getal aan het selectorpad kunnen toevoegen door de automatische variabele `{{@RandomInt(min,max)}}` te gebruiken.

### Krijg hulp van Support

Self-Service Transacties betekent niet dat we u aan uw lot hebben overgelaten. Onze supportmedewerkers staan klaar om u te helpen. Ons ervaren transactieteam heeft het allemaal eerder gezien en ze zijn geweldig in het vinden van alternatieve selectors. Open gewoon een [support ticket](/contact) en vertel ze over uw uitdaging.
