{
  "hero": {
    "title": "Uw transactiescript testen en bewerken"
  },
  "title": "Uw transactiescript testen en bewerken",
  "summary": "Nadat u uw transactie heeft opgenomen en u ervoor kiest uw controleregel zelf te bewerken en te testen, hebben we om u te helpen deze handige handleiding samengesteld.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/tutorial-record-user-journey-in-shop/uw-transactie-testen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In dit artikel gaat u stapsgewijs door het bewerkings- en testproces voor een eenvoudige transactie, en lost u enkele eenvoudige problemen op.

De voorbeelden die hier worden gebruikt komen uit een eerdere oefening: [Het klikpad van de winkelwagengebruiker vastleggen]([LINK_URL_1]). Als u die oefening nog niet heeft voltooid, kunt u dat nu doen, of u kunt [het script kopiëren en plakken]([LINK_URL_2])  in de stap-editor.

## Handmatig testen in development mode

U heeft drie opties voor uw controleregels: development, staging en production mode. Testen in development mode is het belangrijkste dat u kunt doen voordat u een transactiescript naar staging of production mode verplaatst Meer informatie over [controleregel modes]([LINK_URL_3]).

1. Ga in de Uptrends-app naar [SHORTCODE_9] Transacties > Transacties beheren [SHORTCODE_10].
2. Open de transactiecontroleregel die door de transaction recorder is geüpload.
3. Zorg ervoor dat u op het tabblad [SHORTCODE_11] Algemeen [SHORTCODE_12] bent.
4. In het gedeelte *Status* stelt u de *Mode* in op "Development".
5. Klik op de knop [SHORTCODE_13] Opslaan [SHORTCODE_14].

[SHORTCODE_1]
**Tip:** Houd de \[Ctrl\] toets ingedrukt terwijl u op [SHORTCODE_15]Opslaan[SHORTCODE_16] klikt om het controleregelvenster na het opslaan open te houden. Anders bent u terug bij het overzicht *Controleregels*  nadat u een controleregel heeft opgeslagen.
[SHORTCODE_2]

## Begin uw testen met "Test starten"

Of u nu begint met een script rechtstreeks uit de transaction recorder, wijzigingen aanbrengt in uw script of problemen met een script in production oplost, u gebruikt de knop [SHORTCODE_17] Test starten [SHORTCODE_18]. Om te controleren of er problemen zijn, kunt u op deze manier een snelle test uitvoeren.

1. Open de transactiecontroleregel die voor deze tutorial is gemaakt.
2. Druk onder aan de pagina op de knop [SHORTCODE_19] Test starten [SHORTCODE_20]. Het pop-upvenster *Testen vanaf:* verschijnt.
3. Kies een controlestation van waaruit u uw test wilt uitvoeren.
4. Klik op [SHORTCODE_21] Test starten [SHORTCODE_22].

[SHORTCODE_3]
**Belangrijk**: Een succesvolle test in development mode is geen indicator van een gestabiliseerd transactiescript. Volg alle testaanbevelingen op voordat u een transactiescript naar production verplaatst.
[SHORTCODE_4]

Nadat u met de test bent begonnen, scrolt de editor automatisch naar de bovenkant van de pagina en het controlestation voegt uw controleregel toe aan de testwachtrij. Zodra de test start, kunt u de test bekijken terwijl het controlestation door uw script stapt. Als uw script eindigt met een succesvolle test, is dat natuurlijk geweldig, maar er moet nog meer getest worden.

Als u het voorbeeldscript gebruikt, zult u zien dat *Stap 1* (Navigeren) en *Stap 2* (Klikken op een element) succesvol zijn uitgevoerd, maar dat *Stap 3* mislukte op actie 3.3.

![screenshot testresultaat met mislukking]([LINK_URL_4])

[SHORTCODE_5]
**Tip:** Tijdens handmatig testen met de knop [SHORTCODE_23]Test starten[SHORTCODE_24], bevatten uw testresultaten watervalgrafieken en screenshots om u te helpen bij het debuggen. Klik op de knop [SHORTCODE_25]Testresultaten beschikbaar[SHORTCODE_26] om screenshots en watervalrapporten te bekijken. Wanneer u de controleregel naar staging of production mode verplaatst, kunnen alleen gebruikers met een Business- of Enterprise-account kiezen om watervalrapporten en screenshots aan stappen toe te voegen.
[SHORTCODE_6]

## Problemen met het script oplossen

Een transactie kan om vele redenen mislukken in development mode, zoals ontbrekende inhoud of de verkeerde selectorkeuze voor elementen, tabs en frames. Timingproblemen en ontbrekende interacties kunnen ook een rol spelen. Bekijk de volgende tips voor de meest voorkomende problemen.

### Probleem: Element niet gevonden vanwege dynamische ID's

In de voorbeeldscripttest kunt u in de testresultaten zien dat de controleregel het element dat is gespecificeerd in de CSS-selector niet kon vinden. De actie vertelt het controlestation om de hoeveelheid te wijzigen, maar aangezien de controleregel het element niet kan vinden, mislukt de actie. Het Knowledge Base-artikel [Selectoralternativen]([LINK_URL_5]) bevat meer informatie over selectors.

![screenshot mislukte actie]([LINK_URL_6])

De volledige CSS-selector luidt:

[INLINE_CODE_1]

Dus de controleregel kijkt en wacht op een element op de pagina met id="quantity\_6346b8b92ac97", en wanneer het verschijnt, stelt de controleregel de waarde van het element in op "2". Maar het element met ID "quantity\_6346b8b92ac97" is nooit verschenen. Waarom niet? De selector is op zoek naar een specifieke ID, maar de server genereert de ID van het element dynamisch. Elke keer dat de pagina wordt geladen, geeft de server het element een andere ID. Om dit te verhelpen zijn er andere manieren om een element te identificeren dan door zijn ID.

### Oplossing: Gebruik een andere selector

Om het probleem dat wordt veroorzaakt door dynamische ID's te omzeilen, heeft u een andere selector nodig. Klik op de knop met drie stippen [SHORTCODE_27]…[SHORTCODE_28] in het selectorindicatievak om een lijst van andere mogelijke selectors weer te geven.

![screenshot details mislukte actie]([LINK_URL_7])

Een pop-upvenster met [selectoralternatieven]([LINK_URL_8]) verschijnt:

![selectoralternatieven]([LINK_URL_9])

In dit geval ziet u dat verschillende selectors de dynamisch gecreëerde waarde gebruiken, zodat u die selectors meteen kunt uitsluiten. Twee andere opties bevatten de dynamische ID niet: *name* en *xpath:idRelative*. De recorder ordent de selectors automatisch op basis van zijn mening over welke selectors het beste zullen werken. In dit geval kan de tweede aanbeveling, “name” beter werken om het element te identificeren. De naamwaarde is een element attribute en als deze uniek is voor de pagina, is de selector waarschijnlijk uw beste keuze.

Het blijkt dat de optie *xpath:idRelative* in dit geval ook werkt. Uptrends gaf u twee geldige keuzes die prima werken in development mode, maar u weet pas zeker of ze goed werken als u het script naar staging mode verplaatst. Maar u moet nog meer doen voordat u uw script naar staging of production mode verplaatst.

### Probleem: Element niet gevonden vanwege gebrek aan gebruikersinteractie

Net als dynamische ID's kan ook dynamische inhoud die gebruikersinteractie vereist voordat een element zichtbaar is, problemen veroorzaken. Het kan lastig zijn om ze te vinden, maar het beste is om eerst goed te kijken naar de details van de gebruikersinteracties.

### Oplossing: Voeg hoveracties toe

Sommige pagina-elementen worden niet geladen of worden pas zichtbaar als de gebruiker de cursor over het element beweegt. Als een gebruiker bijvoorbeeld over een menu moet hoveren om de submenu's zichtbaar en toegankelijk te maken, moet het script ook de hoveractie uitvoeren. De transaction recorder kan echter geen hovergebeurtenissen vastleggen, en als een element niet zichtbaar is op de pagina, kan het script er niet mee interacteren. U moet een hoveractie toevoegen vóór de afhankelijke interactie. Meer informatie over [hoveracties]([LINK_URL_10]) en hoe u ze configureert.

### Probleem: Fout vanwege time-out

Wanneer het script wordt uitgevoerd, blijft het zoeken en wacht het op het laden van elementen. De standaardwachttijd is 30 seconden, en 30 seconden is meestal ruim voldoende tijd. Echter, als 30 seconden niet genoeg is, moet u misschien extra wachttijden aan een actie toevoegen. Meer informatie over het gebruik van wachtvoorwaarden vindt u in ons Knowledge Base-artikel [Wachtvoorwaarden gebruiken]([LINK_URL_11]).

### Oplossing: Oorzaken en (mogelijke) oplossingen voor timingproblemen

Als u een timingprobleem heeft vastgesteld, kunnen daar verschillende oorzaken en oplossingen voor zijn.

-  **Element is nog niet interactief** - Verleng de wachttijd.
-  **Transactietime-out** - Een transactie heeft een maximale run time. [Vraag support]([LINK_URL_12]) om naar uw script te kijken om u te helpen het probleem te vinden.

[SHORTCODE_7]
**Belangrijk:** We kunnen niet genoeg benadrukken hoe belangrijk inhoudcontroles zijn voor het slagen van uw transactiemonitoring. Voeg inhoudcontroles toe na elke navigatie of inhoudvernieuwing. Gebruik ze vóór elke interactie. [Inhoudcontroles]([LINK_URL_13]) zijn gratis en ze maken uw monitoring robuuster.
[SHORTCODE_8]

### Probleem: Fouten in instellenacties

Ontbrekende klikken vóór [instellenacties]([LINK_URL_14]) kunnen onverwachte fouten veroorzaken. Vermijd fouten door altijd een [klikactie]([LINK_URL_15]) op te nemen bij elke instellenactie.

### Oplossing: Voeg klikacties toe

**Gebruik de Enter-toets niet** - Bij het opnemen van uw transactie heeft u mogelijk de Enter-toets gebruikt in plaats van op een verzendknop te klikken. Als u bijvoorbeeld een zoekfunctie gebruikt, is de natuurlijke actie om op Enter te drukken in plaats van op de zoekknop. De recorder kan het gebruik van de Enter-toets niet opnemen. Als u ontdekt dat u dat heeft gedaan tijdens uw opname, voegt u de klikactie toe. Is er geen knopoptie, [neem dan contact op met support]([LINK_URL_16]) om u te helpen een oplossing te vinden.

**Gemiste klikken** - Verwijder de klikken niet die verschijnen voordat u waarden in velden invoert. Klikgebeurtenissen activeren waardemaskers en andere gebeurtenissen in de browser. In sommige gevallen moeten twee klikken worden toegevoegd voordat u een waarde invoert. 

Meer informatie over [klikacties]([LINK_URL_17]).

## Checklist voor het testen van scripts

Voordat u uw transactiecontroleregel naar staging verplaatst, moet u eerst een aantal dingen controleren.

- **Zet [inhoudcontroles]([LINK_URL_18]) in.** Voeg na elke paginaovergang een inhoudcontrole toe om te controleren of de juiste pagina is geladen met de juiste inhoud.
- **Controleer de [screenshots en watervallen]([LINK_URL_19]).** In development mode genereert elke stap een screenshot van het browservenster en de watervalgrafiek. Controleer de watervallen en screenshots om de paginaflow, inhoud en nauwkeurigheid van producten/items te verifiëren.
- **Lees de [transactiewaarschuwingen]([LINK_URL_20]).** Zorg ervoor dat uw monitoring geen negatieve gevolgen heeft voor uw bedrijf.
- **Voeg [klikacties toe]([LINK_URL_21])** voordat u waarden in tekstvakken invoert.

## Schakel naar staging mode

Nadat u uw code in development mode heeft verfijnd en getest, is de volgende stap om naar staging mode te gaan. Meer informatie over [controleregel modes]([LINK_URL_22])).

1. Ga in de Uptrends-app naar [SHORTCODE_29] Transacties > Transacties beheren [SHORTCODE_30].
2. Open de transactiecontroleregel die voor deze tutorial is gecreëerd.
3. Zorg ervoor dat u op het tabblad [SHORTCODE_31] Algemeen [SHORTCODE_32] bent.
4. Wijzig de **Mode** in "Staging".
5.  Stel de controleregel in op **Actief** door het vakje aan te vinken.
6.  Klik op [SHORTCODE_33] Opslaan [SHORTCODE_34].

Laat uw nieuwe transactiecontroleregel een paar weken in staging mode draaien om de stabiliteit te testen, vooral na site-updates. Het verplaatsen van de tests naar het uitgebreidere controlestationnetwerk kan ook lokale problemen blootleggen.

Hoewel de tests in staging mode geen alerts genereren, kunt u de controleregel logs en het dashboard **Transactie** bekijken om eventuele fouten te zien die uw controleregel is tegengekomen. In de *Controleregel log* (en andere dashboards), ziet u de laboratoriumkolf naast uw controleregel in staging mode.

![screenshot controleregel log]([LINK_URL_23])


Als u op het tijdstempel van de fout klikt, wordt het rapport [Details van de controle]([LINK_URL_24]) geopend dat u informatie geeft over de transactie tot en met de fout.