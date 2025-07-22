{
  "hero": {
    "title": "Berekenen van credits voor transactiecontroleregels"
  },
  "title": "Berekenen van credits voor transactiecontroleregels",
  "summary": "Lees hoe we het aantal transactiecredits bepalen dat voor uw transactie is ingesteld.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/berekenen-credits-transactiecontroleregels",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u zich afvraagt hoe Uptrends de kosten van een bepaalde transactiecontroleregel bepaalt, bent u op de juiste plek. Voordat we ingaan op de berekening van het creditsverbruik, bekijken we enkele termen die vaak worden gebruikt bij het bespreken van transactiecontroleregels.

**Transactie**: Een transactie is het traject van een gebruiker om een taak op uw website te voltooien. Transacties omvatten taken als inloggen, een aankoop doen, een formulier versturen, een document aanvragen, een account aanmaken, een nieuw wachtwoord aanvragen enzovoort. Een enkele transactie bestaat uit twee of meer stappen.

**Transactiecredit**: Beschouw een transactiecredit als contant geld. U heeft een toegewezen aantal transactiecredits op basis van uw abonnement (u kunt altijd meer credits kopen). Een transactiecontroleregel kost een bepaald aantal credits op basis van meerdere factoren die we zo meteen bespreken. Wanneer uw controleregel in developmentmodus staat, worden er geen credits verbruikt. U verbruikt credits door de controleregel in staging- of productionmodus te zetten. (Lees meer over [controleregelmodus]([LINK_URL_1]).)

U kunt het aantal beschikbare credits vinden in uw accountinstellingen.

**Gebruikersacties**: Een gebruikersactie is de interactie van een gebruiker met de pagina. Voorbeelden van gebruikersacties zijn klikken, tekstinvoer, hover-acties en inhoudcontroles.  

**Stap**: Een stap is een willekeurige groepering van gebruikersacties. U kunt uw acties groeperen in stappen die voor u het meest logisch zijn en u helpen bij het oplossen van problemen en rapportage. Uptrends rapporteert tijdsduur op een stap-voor-stapbasis (iets om rekening mee te houden bij het instellen van uw stappen). We raden aan elke stap af te sluiten met een actie die ervoor zorgt dat de volgende pagina wordt geladen, en een inhoudcontrole.

## Hoe bepaalt Uptrends het aantal credits dat een transactiecontroleregel gebruikt?

We bepalen hoeveel transactiecredits een transactie gebruikt op basis van een aantal verschillende factoren:

**Het aantal gebruikersacties dat resulteert in een server request**. Elke gebruikersactie (zie de definitie hierboven) in een transactiecontroleregel die resulteert in een server request, verbruikt één transactiecredit. Navigatieacties, bestandsuploads en klikken die nieuwe pagina’s in de browser laden, verbruiken een credit. Tekstinvoer, hover-acties en inhoudcontroles zijn gratis.  
  
**Transactiewatervallen, filmstrips en screenshots**: Elke transactiewaterval of screenshot die in uw transactie wordt gebruikt, verbruikt een transactiecredit. Filmstrips kosten één transactiecredit, behalve wanneer er al één screenshot in de stap is, dan wordt de filmstrip gratis verstrekt. Twee screenshots en één filmstrip kosten twee transactiecredits.

## De berekening van de transactiecontroleregel

Als u een formule wilt voor het berekenen van het aantal credits dat nodig is voor één transactie, probeer dan deze:

**Aantal acties met server requests** \+ **aantal watervalgrafieken** \+ **aantal screenshots** = **totaal aantal verbruikte transactiecredits**

**Opmerking**: Wanneer u een nieuwe controleregel toevoegt of een controleregel wijzigt, toont uw lijst Controleregels het aantal gevolgd door het woord "berekenen" of "berekend". Het systeem heeft enkele momenten nodig om uw transactiestappen te analyseren om de juiste kosten te bepalen. In specifieke gevallen beoordeelt ons support team de gewijzigde of nieuwe controleregel om ervoor te zorgen dat het aantal controleregelcredits dat van toepassing is op de controleregel correct blijft.

## Conclusie

Vraagt u zich nog steeds af hoe we het verbruik van transactiecredits hebben berekend, neem dan [contact op met support]([LINK_URL_2]). Ons support team bekijkt de transactie met u om eventuele misverstanden uit de weg te ruimen.
