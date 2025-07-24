{
  "hero": {
    "title": "Tijdlijn screenshots"
  },
  "title": "Tijdlijn screenshots",
  "summary": "Beschrijving van de tijdlijn screenshots zoals getoond in de watervalresultaten",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-resultaten/tijdlijn-screenshots",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

Het laden van een pagina in een browser gebeurt in verschillende stappen. Naarmate steeds meer pagina-elementen worden geladen, begint de browser de pagina-inhoud weer te geven en de lay-out ervan te verschuiven, totdat het laden is voltooid en uw controleregel (hopelijk) een Ok-resultaat retourneert. Een [watervalgrafiek]([LINK_URL_1]) is een goede weergave van wat er gebeurt tijdens het laden van de pagina, maar als er veel elementen tegelijkertijd worden geladen, kan het moeilijk zijn om een beeld te vormen van wat er eigenlijk gebeurt in de browser.

Om daarbij te helpen bevat ons [controleregeltype Full Page Check (FPC)]([LINK_URL_2]), mits deze is geconfigureerd om **Chrome met extra kengetallen** als browsertype te gebruiken, **Tijdlijn screenshots** (ook wel **filmstrip** genoemd). De filmstrip is een reeks screenshots van de browser, die precies laat zien hoe de pagina eruitzag op verschillende punten tijdens het laadproces. 

![Tijdlijn screenshots]([LINK_URL_3])

Als uw waterval punten van zorg bevat, zoals afbeeldingen die niet kunnen worden geladen of scripts die de rest van de pagina vertragen, kunt u de waterval tijdlijn vergelijken met het relevante screenshot om te zien hoe de pagina er op dat punt uitzag. 

## Wanneer worden tijdlijn screenshots gemaakt?

De tijdlijn screenshots, zoals getoond in Uptrends, zijn rechtstreeks afkomstig van Chrome. Als onderdeel van de standaardfuncties verzamelt Chrome zijn eigen screenshots wanneer een performanceopname wordt gemaakt in zijn Dev Tools-interface. Uit deze set die is vastgelegd door Chrome, proberen we de meest relevante weer te geven:

- We nemen de eerste screenshots na bepaalde mijlpalen (eerste/laatste screenshot, eerste contentful paint, grootste contentful paint, tijd tot interactief). 
- Op basis van de totale tijdsduur van de controleregel bepalen we hoeveel screenshots moeten worden weergegeven, maar met een minimum van zes. 