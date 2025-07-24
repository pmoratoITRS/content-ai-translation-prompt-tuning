{
  "hero": {
    "title": "Paginabron en console log"
  },
  "title": "Paginabron en console log",
  "summary": "Beschrijving van waar de paginabron en console log-informatie te vinden zijn in FPC's en transactiecontroleregels",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-resultaten/paginabron-console-log",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bij [transactiecontroleregels]([LINK_URL_1]) en [Full Page Check-controleregels]([LINK_URL_2]) heeft u de optie om de **paginabron** te bekijken (d.w.z. het HTML-document zoals ontvangen door het controlestation), evenals de **console log** die werd gegenereerd toen we de pagina laadden. 


## In Full Page Checks

Bij Full Page Checks (FPC's) zijn de paginabroninformatie en de console log te vinden in elk controleregelresultaat, onder de [watervalgrafiek]([LINK_URL_3]). U krijgt altijd de paginabroninformatie, maar de console log is alleen beschikbaar als er daadwerkelijk console log-vermeldingen in de browser waren toen de pagina werd geladen. Meestal genereert de browser console log-vermeldingen wanneer er iets misgaat – als bijvoorbeeld een bepaald element niet correct kan worden geladen of als er een javascript-fout wordt aangetroffen. 

![Voorbeeld van console log die een fout weergeeft]([LINK_URL_4])

## In transactiecontroleregels

Bij transactiecontroleregels moeten de paginabron- en console log-optie expliciet worden ingeschakeld. 
### Paginabron- en console log-registratie instellen in een transactie

Om paginabron- en console log-data voor een specifieke stap in een transactie weer te geven, moet u eerst de optie **Waterval** voor die stap inschakelen (zie onze handleiding over [werken met transactiewatervallen]([LINK_URL_5])). Vervolgens wordt de optie **Paginabron** beschikbaar. Als u deze optie selecteert, betekent dit dat de resultaten van de controleregelcheck zowel de paginabroninformatie als eventuele console log-data bevatten die mogelijk zijn gegenereerd tijdens de uitvoering van die stap. 

![Paginabron selecteren in de transactie-editor]([LINK_URL_6])

### Lokaliseren van de paginabron- en console log-informatie in een transactie

Nadat u de paginabronoptie voor een transactiestap heeft ingeschakeld, kunt u de informatie vinden in de resultaten van uw controleregelcheck die daarna zijn gegenereerd. Zoek de transactie in uw [Controleregel log]([LINK_URL_7]) of navigeer naar het transactiedashboard en klik op een van de controleregelresultaten die zijn gegenereerd nadat u de optie Paginabron heeft ingeschakeld. 


![Paginabron- en console log-pictogrammen in transactie]([LINK_URL_8])

Om de paginabroninformatie voor deze specifieke stap te openen klikt u op het derde pictogram [SHORTCODE_1][SHORTCODE_2] in het resultaat van de controleregelcheck. U kunt de console log vinden door op het laatste pictogram [SHORTCODE_3][SHORTCODE_4], te klikken, maar die is mogelijk niet altijd beschikbaar.

