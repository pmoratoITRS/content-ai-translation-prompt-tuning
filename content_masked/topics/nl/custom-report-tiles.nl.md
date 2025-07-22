{
  "hero": {
    "title": "Aangepaste tegels"
  },
  "title": "Aangepaste tegels",
  "summary": "Toon uw monitoringdata als lijst of grafiek op aangepaste dashboards met aangepaste tegels",
  "url": "[URL_BASE_TOPICS]dashboards-en-rapportages/dashboards/aangepaste-tegels",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends biedt een breed scala aan rapporttegels die geschikt zijn voor al uw monitoringbehoeften. Deze rapporttegels tonen op handige wijze de statistieken van uw controleregels, controlestations en foutstatus via diagrammen. Als onderdeel van uw [dashboardinstellingen]([LINK_URL_1]) bevatten deze tegels verschillende typen, variërend van een tabel met informatie, lijngrafieken, staafdiagrammen en cirkeldiagrammen.

Om te beginnen [voegt u een rapporttegel toe]([LINK_URL_2]) aan uw standaard Uptrends-dashboards of maakt u uw set-up helemaal zelf. Klik na het toevoegen op het pictogram [SHORTCODE_1] [SHORTCODE_2] om toegang te krijgen tot de tegelinstellingen en de configuratie aan te passen.

Dit knowledgebase-artikel leidt u door de verschillende typen rapporttegels en hun instellingen.

## Eenvoudige lijst of grafiek [ANCHOR_1]

Met dit type rapporttegel kunt u controleregels of controleregelgroepen selecteren om statistieken weer te geven uit de opties **Algemeen**, **Core Web Vitals** en **W3C Navigatie**. Deze statistieken kunnen variëren, afhankelijk van het controleregeltype en andere configuratie-instellingen.

Om de **Core Web Vitals** en **W3C Navigatiekengetallen** van uw controleregels in te schakelen, moet u ervoor zorgen dat het [browsertype]([LINK_URL_3]) van uw controleregel is gewijzigd in **Chrome met extra kengetallen**. Zorg ervoor dat u voor Transactiecontroleregels ook de [Prestatiekengetallen]([LINK_URL_4]) heeft ingeschakeld in de **Waterval**-instellingen van uw transactiestapinstellingen.

Houd er rekening mee dat de periode vóór deze wijziging geen data van **Core Web Vitals** en **W3C Navigatiekengetallen** weergeeft. U kunt de rapportageperiode aanpassen in de tegelinstellingen om alleen het bereik weer te geven waarin **Chrome met extra kengetallen** was ingeschakeld.

Na configuratie toont de Eenvoudige lijst of grafiek een grafiek die overeenkomt met de kengetallen. Controleer de legenda en hover over de grafiek voor meer informatie over de stappen. Raadpleeg het knowledgebase-artikel [Berekening van uptime en downtime]([LINK_URL_5]).

![Kengetallen Eenvoudige lijst of grafiek]([LINK_URL_6])  


### Algemeen

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:

- Totale tijd, resolve tijd, connectietijd en downloadtijd
- Uptimepercentage, downtime percentage, uptime en downtime
- Bevestigde en onbevestigde fouten
- Controles, alerts en totaal bytes
- SLA doel uptimepercentage, SLA doel totale tijd, SLA doel operator responstijd en operator responstijd

![Eenvoudige grafiek Algemene kengetallen]([LINK_URL_7])  

### Core Web Vitals

De controleregels FPC en Transactie verzamelen beide data van de [Core Web Vitals]([LINK_URL_8]) wanneer het browsertype is ingesteld op [Chrome met extra kengetallen]([LINK_URL_9]).

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:

 - First contentful paint
 - Largest contentful paint
 - Time to interactive
 - Total blocking time
 - Cumulative layout shift

![Eenvoudige grafiek Core Web Vitals-kengetallen]([LINK_URL_10])  


### W3C Navigatie

De controleregels FPC en Transactie verzamelen beide data van de [W3C Navigatie]([LINK_URL_11]) en [Core Web Vitals]([LINK_URL_12]) wanneer het browsertype is ingesteld op [Chrome met extra kengetallen]([LINK_URL_13]).

Selecteer een van de volgende kengetallen om de data in de rapporttegel weer te geven:
  - Request start
  - Time to first byte
  - DOM interactive
  - DOM completed
  - Load event

![Eenvoudige lijst W3C Navigatiekengetallen]([LINK_URL_14])  


## Controleregel lijst of grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens wat u wilt weergeven:

- SLA uptimepercentage, SLA doel uptimepercentage
- SLA totale tijd, SLA doel totale tijd, SLA downtime
- SLA operator responstijd, SLA doel operator responstijd
- Totale tijd, Controles, Bevestigde fouten, Onbevestigde fouten
- Uptimepercentage, Downtimepercentage
- Sorteeropties en Regels tonen-opties
  
![screenshot tegel controleregel grafiek]([LINK_URL_15])  
  
![screenshot tegel controleregel lijst]([LINK_URL_16])  

## Lijst van fouttypes of Fouttype grafiek  

Selecteer controleregels of controleregelgroepen en periode-opties.  
  
![screenshot fouttype lijst en grafiek]([LINK_URL_17])  

## Controlestation lijst of grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies dan wat u wilt weergeven: 

- Totale tijd, Resolve tijd
- Connectietijd, Downloadtijd
- Controles, Bevestigde fouten en Sorteeropties 
  
![screenshot tegel controlestation grafiek]([LINK_URL_18])

![screenshot tegel controlestation lijst]([LINK_URL_19])  

## Multicontrolestation lijst of/ grafiek  

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens welk kengetal u in de hele lijst of grafiek wilt weergeven.  
  

![screenshot tegel multicontrolestation grafiek]([LINK_URL_20]) 
  
![screenshot tegel multicontrolestation lijst]([LINK_URL_21]) 

## Multicontroleregel lijst of grafiek   

Selecteer controleregels of controleregelgroepen, periode en kies vervolgens welk kengetal u via de lijst of grafiek wilt weergeven.  
  
![screenshot tegel multicontroleregel grafiek]([LINK_URL_22])  

![screenshot tegel multicontroleregel lijst]([LINK_URL_23])

## Details Laatste controle [ANCHOR_2]

Geef weer wanneer een controleregel of controleregelgroepen voor het laatst zijn gecontroleerd en selecteer de periode waarover de data moeten worden weergegeven .  
![screenshot aangepaste tegels details controleregelcheck]([LINK_URL_24])

## Controleregel log  

Selecteer controleregels of controleregelgroepen, periode en selecteer vervolgens hoe fouten moeten worden gefilterd en of het rapport moet worden opgenomen in een geëxporteerd bestand.  
  
![screenshot tegel controleregel log]([LINK_URL_25]) 

## Alerthistorie 

Toon de historie met alertmeldingen per controleregel of controleregelgroep en filter data op periode. 

![screenshot tegel alerthistorie]([LINK_URL_26])

## Lijst met staptijden of Staptijden grafiek  

Voor transactie- en Multi-step API-controleregels en slechts één controleregel tegelijk. Toont de duur van stappen in de tijd.
  
![screenshot tegel stapduur grafiek]([LINK_URL_27])  

## Lijst met gemiddelde staptijden of Gemiddelde stapduur grafiek  

Voor transactie- en Multi-step API-controleregels en slechts één controleregel tegelijk. Toont de gemiddelde duur van stappen.
  
![screenshot tegel gemiddelde duur van stappen grafiek]([LINK_URL_28])  
