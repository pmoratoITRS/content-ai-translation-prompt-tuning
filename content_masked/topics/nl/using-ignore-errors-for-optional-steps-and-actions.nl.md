{
  "hero": {
    "title": "Negeer fouten gebruiken bij optionele stappen en acties"
  },
  "title": "Negeer fouten fouten gebruiken bij optionele stappen en acties",
  "summary": "Uw transactiescripts moeten kunnen reageren op dynamische site-veranderingen. Het gebruik van negeer fouten geeft u de controle die u nodig heeft om conditionele statements of statements die kunnen worden overgeslagen in te voegen in de stappen en acties van uw script.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/gebruik-van-negeer-fouten-bij-optionele-stappen-en-acties",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het komt zelden voor dat een website geen dynamische variaties heeft in het klikpad van de gebruiker. Uw site kan om verschillende redenen dynamische variaties in inhoud hebben:

-   Paginaverschillen vanwege gebruikerslocatie
-   A/B-testen
-   Wijzigingen in invoervelden
-   Cookiewalls
-   Tijdelijk ingevoegde pagina's

Elke variatie in het klikpad creëert uitdagingen voor uw transactiescripts. Conditionele statements in de vorm van de *negeer fouten*-optie kunnen u helpen bij het navigeren door dynamische site-veranderingen zoals hierboven vermeld.

## Waarin lijkt “negeer fouten” op het maken van een conditioneel statement?

Wanneer u ervoor kiest fouten te negeren, vertelt u de controleregel een actie te proberen, maar afhankelijk van of de assertion of actie mislukt (of slaagt), voer deze actie daarna uit. Beschouw de optie negeer fouten als een manier om een conditioneel statement in te voegen. U kunt negeer fouten instellen op stapniveau of op het niveau van een individuele actie.

-   **Negeer fouten op stapniveau** 
    Door negeer fouten op stapniveau in te stellen, vertelt u het script om de stap te verlaten en door te gaan met de volgende stap als het script een fout tegenkomt. Als actie X in stap Y succesvol is, ga dan verder; als actie X in stap Y mislukt, verlaat dan de stap en ga naar stap Z.
-   **Negeer fouten op actieniveau**  
    Door negeer fouten op actieniveau in te stellen, vertelt u het script door te gaan met de volgende actie, zelfs als de actie mislukt. Als actie X succesvol is, ga dan naar actie Y; als actie X mislukt, ga dan toch verder met actie Y.

## Hoe werken stappen en acties die kunnen worden overgeslagen?

Doorgaans stopt de uitvoering van het script wanneer uw transactie mislukt en legt Uptrends de fout vast. De fout kan ertoe leiden dat Uptrends u een alert stuurt als een ander controlestation de fout verifieert. Als u instelt dat de fout kan worden overgeslagen (negeer fouten), gaat de uitvoering door met de volgende stap of actie, afhankelijk van of u de optie negeer fouten op stapniveau of op de actie heeft geplaatst. Uptrends noteert uw fout in uw rapport Details van de controle; overgeslagen fouten hebben echter geen invloed op de rapportage van uw site.

### Fouten negeren in stappen

Als u negeer fouten in een stap inschakelt, stopt het script met het uitvoeren van de huidige stap en gaat het naar de volgende stap als een actie mislukt. Afbeelding 1 toont bijvoorbeeld een transactie met een cookiewall. De cookiewall vereist dat de gebruiker op een accepteerknop klikt wanneer de wall verschijnt, maar deze verschijnt niet bij alle gebruikers.

Om met de cookiewall om te gaan plaatsen we een stap die kan worden overgeslagen. In dit geval bepaalt een inhoudcontrole of de site een cookiewall heeft ingevoegd (weergegeven in Stap X in figuur 1). Als er een cookiewall is, slaagt de inhoudcontrole, de controleregel klikt op de knop om de voorwaarden te accepteren en de uitvoering gaat verder met Stap Y. Als de inhoudcontrole geen cookiewall vindt, mislukt Stap X, maar de controleregel gaat toch door naar stap Y. Stap Y is niet ingesteld om fouten te negeren, dus eventuele fouten die optreden in Stap Y zorgen ervoor dat de controleregel het script beëindigt, en Uptrends registreert de fout.

![]([LINK_URL_1])

*Afbeelding 1*: Negeer fouten gebruiken om te testen op een cookiewall en, indien aanwezig, deze te passeren.

### Fouten negeren in acties

Wanneer u fouten in individuele acties negeert, gaat de uitvoering door naar de volgende actie. Afbeelding 2 toont een transactie met een A/B-test. In stap X vereist het script dat de acties 1 en 2 slagen, maar de acties 3 en 4 zijn alleen geldig voor versie A van de pagina. Als u fouten voor acties 3 en 4 niet negeert, zal het script elke keer dat de server pagina B verzendt mislukken.

![]([LINK_URL_2])

*Afbeelding 2*: Stroomdiagram van een transactie met een A/B-test.

## Voorbeelden

Laten we een paar voorbeelden beter bekijken om u te helpen. Uw specifieke gebruiksscenario vereist mogelijk een andere oplossing, [laat het ons weten]([LINK_URL_3]) als u hulp nodig heeft bij uw oplossing.

[SHORTCODE_1]
**Opmerking**: Een algemene regel om te volgen is: gebruik negeer fouten op acties voor een enkele actie, en gebruik negeer fouten op de stap als meer dan één actie moet worden overgeslagen op basis van een enkele voorwaarde.
[SHORTCODE_2]

### Gebruiksscenario: Ander klikpad vanwege gebruikerslocatie

Soms gedragen sites zich om verschillende redenen anders op basis van de locatie van een gebruiker, zoals overheidsvoorschriften, beschikbaarheid van producten in het gebied of de taal. Als een gebruiker zich bijvoorbeeld in de EU bevindt, moet de site bevestiging krijgen dat de gebruiker begrijpt dat de website persoonlijke gegevens van bezoekers verzamelt. De site maakt gebruik van een pop-up waarin de gebruiker een vakje moet aanvinken waarin staat dat hij de voorwaarden kent waaronder de website gegevens verzamelt en bewaart, en de gebruiker moet ook op een doorgaan-knop klikken.

#### Oplossing: Stap die kan worden overgeslagen

In dit voorbeeld moet de gebruiker twee acties uitvoeren om toegang te krijgen tot de volledige site; daarom is een stap die kan worden overgeslagen een goede keuze.

1.  Voeg een stap toe op het punt in de transactie waar de gebruiker de prompt kan ontvangen.
2.  Stel de stap in om fouten te negeren.
3.  Voeg een klikactie in die het selectievakje aanvinkt.
4.  Voeg een klikactie in die op de doorgaan-knop klikt.

Als de klikactie in stap 3 mislukt, werd de prompt niet weergegeven voor de gebruiker. Het script verlaat de stap en gaat naar de eerste actie in de volgende stap; anders bevestigt de controleregel de voorwaarden door de juiste acties uit te voeren en gaat de transactie gewoon verder.

### Gebruiksscenario: A/B-testen

Met een A/B-test kunt u gebruikersinteracties vergelijken op basis van twee verschillende versies van dezelfde pagina. Op pagina A moet de gebruiker meer persoonlijke gegevens verstrekken dan op pagina B. De test bepaalt welke pagina meer conversies genereert. De server levert willekeurig verschillende paginaversies aan gebruikers. De verschillen in de verschillende pagina-interacties kunnen ertoe leiden dat uw controleregel mislukt.

#### Oplossing: Acties die kunnen worden overgeslagen

In deze situatie moet de controleregel een aantal acties voltooien, ongeacht welke pagina wordt geleverd, en een of meer acties overslaan die specifiek zijn voor andere paginaversies. Om met A/B-tests om te gaan:

1.  Gebruik acties die fouten niet negeren voor de interacties die de twee pagina's gemeen hebben.
2.  Stel de extra velden in om fouten te negeren.

Door de acties in te stellen om fouten voor de extra velden te negeren, kan de transactie verdergaan, ongeacht welke versie van de pagina de controleregel ontvangt (zie afbeelding 2).

### Gebruiksscenario: Veranderende veldopties

Denk aan een e-commercesite voor kleding met een snel veranderend aanbod. Uw transactie kiest het eerste item dat in een zoekopdracht naar voren komt, maar het eerste item verandert regelmatig. Hoewel elk item een hoeveelheid-veld heeft, hebben niet alle items een maat (een sjaal), een kleur (alleen verkrijgbaar in zwart) of geen van beide (een handtas). De veranderingen in beschikbare acties kunnen ertoe leiden dat uw controleregel mislukt wanneer deze probeert een kleur te selecteren terwijl kleur geen optie is.

#### Oplossing: Acties die kunnen worden overgeslagen

Aangezien niet alle selectievelden op alle pagina's verschijnen, wilt u fouten negeren bij de acties die waarden instellen voor elementen die niet van toepassing zijn op het item. Omgaan met veranderende veldopties:

1.  Voeg een stap toe.
2.  Voeg de juiste acties toe voor elke mogelijke pagina-interactie: aantal, grootte en kleur.
3.  Als u de optie voor het negeren van fouten uitgeschakeld laat voor aantal, vinkt u de vakjes voor fouten negeren aan voor de acties maat- en kleurselectie.

Het script probeert elke waarde in te stellen, maar als het element niet aanwezig is mislukt de actie en gaat het script toch door naar de volgende actie (zie afbeelding 2).

### Gebruiksscenario: Ingevoegde kennisgevingpagina's

Van tijd tot tijd moet een site zijn gebruikers op de hoogte stellen van verschillende dingen, zoals aankomend onderhoud, wijzigingen in gebruikersvoorwaarden, verkoop- en andere promoties. De website voegt tijdelijke pagina's met de kennisgeving in in het normale klikpad van de gebruiker. De pagina vereist vaak een gebruikersactie om de kennisgeving te bevestigen.

#### Oplossing: Stap of actie die kan worden overgeslagen

Dit scenario kan een of meer gebruikersinteracties hebben om de transactie voort te zetten.

**Als bevestiging een enkele interactie vereist, gebruik dan een actie die kan worden overgeslagen**, voeg de actie in op de juiste plaats en stel de actie in om fouten te negeren.

**Als bevestiging meerdere acties vereist, gebruik dan een stap die kan worden overgeslagen**. 

1.  Voeg een stap toe op het punt in het script waar een bericht kan verschijnen.
2.  Stel de stap in om fouten te negeren.
3.  Voeg de juiste acties toe om de pagina te sluiten: accepteer de nieuwe voorwaarden, bevestig de kennisgeving en dien deze in voor de response.

Als de stap of actie succesvol is, heeft u ervoor gezorgd dat de transactie verdergaat. Als de stap of actie mislukt, is er geen kennisgevingpagina, is er geen verdere actie nodig en gaat het script door naar de volgende actie of stap.
