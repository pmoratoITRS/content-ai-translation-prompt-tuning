{
  "hero": {
    "title": "W3C Navigatietijden"
  },
  "title": "W3C Navigatietijden",
  "summary": "Beschrijving van de kengetallen voor W3C Navigatietijden zoals weergegeven in de Full Page Check- en transactiemonitoring-watervallen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-resultaten/w3c-navigatietijden",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het **World Wide Web Consortium** (of kortweg W3C) is een internationale organisatie die zich bezighoudt met het ontwikkelen van standaarden voor het world wide web. Als zodanig heeft het een standaard gedefinieerd voor browsers en webapplicaties om timinginformatie te genereren en weer te geven met betrekking tot het laden van webpagina's. De volledige specificatie van de standaard is te vinden op de [W3C website (Copyright © 2012, World Wide Web Consortium)]([LINK_URL_1]).

Uptrends' controleregels [Full Page Check (FPC)]([LINK_URL_2]) en [transactie]([LINK_URL_3]) bevatten de optie om een subset van kengetallen voor W3C Navigatietijden weer te geven (plus wat aanvullende informatie zoals [Core Web Vitals]([LINK_URL_4])). Dit artikel geeft u een overzicht van de weergegeven kengetallen en wat ze precies betekenen. 

Ter illustratie ziet u in de volgende afbeelding alle timing-gebeurtenissen van de navigatie zoals gedefinieerd door het W3C, op een tijdlijn.

![w3c-navigatietijden]([LINK_URL_5])
(Copyright © 2012, [World Wide Web Consortium]([LINK_URL_6]))

## Kengetallen

Dit is een overzicht van de W3C-kengetallen voor navigatietijden die u kunt vinden in Uptrends' Full Page Checks. 

![W3C Navigatietijden in Uptrends]([LINK_URL_7])

- **Request start**: Gelijk aan de [INLINE_CODE_1] zoals gedefinieerd door W3C. Het is een tijdstempel dat aangeeft wanneer de browser de bron begint op te vragen bij de webserver na de DNS-lookup en de TCP-verbinding. 
- **Time to first byte**: Gelijk aan het verschil tussen [INLINE_CODE_2] en [INLINE_CODE_3] zoals gedefinieerd door W3C. In het kort: het is de tijd tussen het moment waarop de eerste request van de browser naar de server werd verzonden en het moment waarop de eerste byte van de erop volgende response door de browser werd ontvangen (dit is inclusief alle redirects en SSL/TCP-verbindingen). 
- **DOM interactive**: Gelijk aan [INLINE_CODE_4] zoals gedefinieerd door W3C. Het is een tijdstempel dat aangeeft dat de document-gereedheid op "interactief" is gezet, om aan te geven dat de browser is gestopt met het parseren van de pagina en dat de gebruiker ermee kan beginnen te communiceren. Bronnen zoals scripts, afbeeldingen, stylesheets of frames worden mogelijk nog steeds geladen. 
- **DOM completed**: Gelijk aan de [INLINE_CODE_5] zoals gedefinieerd door W3C. Het is een tijdstempel dat aangeeft wanneer het hoofddocument is geparseerd, de DOM volledig is geladen en de pagina-gereedheid is ingesteld op "voltooid".
- **Load event**: Gelijk aan [INLINE_CODE_6] zoals gedefinieerd door W3C. Het is een tijdstempel dat aangeeft wanneer de laadgebeurtenis van het huidige document is voltooid, inclusief alle afhankelijke bronnen zoals stylesheets en afbeeldingen.

## Dashboardrapportage

U kunt alle kengetallen rapporteren op een aangepast dashboard. Voeg gewoon een aangepaste rapporttegel toe van het type [Eenvoudige lijst / grafiek]([LINK_URL_8]). Klik vervolgens op de instellingenknop [SHORTCODE_1] [SHORTCODE_2] op de tegel en kies de waarden die u wilt weergeven door hun selectievakjes aan te vinken. 

U kunt de W3C-navigatiekengetallen van een transactiecontroleregel per individuele stap weergeven. U moet de opties *Waterval* en *Prestatiekengetallen* activeren voor elke stap die u in de grafiek wilt bekijken. In de informatie over [stapinstellingen]([LINK_URL_9]) leest u hoe dit werkt. 

![screenshot detail tegelinstellingen]([LINK_URL_10])
