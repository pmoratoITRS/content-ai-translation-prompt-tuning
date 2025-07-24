{
  "hero": {
    "title": "Core Web Vitals"
  },
  "title": "Core Web Vitals",
  "summary": "Beschrijving van de Core Web Vitals-kengetallen zoals weergegeven in de Full Page Check- en transactiemonitoring-watervallen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-resultaten/core-web-vitals",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Gebaseerd op een initiatief van Google om het gesprek over website-optimalisatie te vereenvoudigen, zijn **Core Web Vitals** een set belangrijke kengetallen om websiteprestaties te meten. Deze kengetallen weerspiegelen verschillende aspecten van de gebruikerservaring bij het bezoeken van een site, zoals laadsnelheid en visuele stabiliteit. Slechte scores op dergelijke kengetallen kunnen rechtstreeks van invloed zijn op uw ranking in zoekmachines, wat betekent dat het belangrijk is om deze kengetallen bij te houden, zodat u er zeker van kunt zijn dat uw pagina goed geoptimaliseerd is en blijft. 

Uptrends' controleregeltypes [Full Page Check (FPC)]([LINK_URL_1]) en [transactie]([LINK_URL_2]) bevatten de optie om de set Core Web Vitals (plus wat aanvullende informatie) weer te geven. Dit artikel geeft u een overzicht van de weergegeven kengetallen en wat ze precies betekenen. 

## Kengetallen

Uptrends geeft de volgende Core Web Vitals (en gerelateerde kengetallen) weer:

![Core web vitals in Uptrends]([LINK_URL_3])

- **First contentful paint (FCP):** De FCP meet hoelang het duurde voordat de browser de eerste inhoud op de pagina weergaf.
- **Largest contentful paint (LCP):** De LCP meet de tijd wanneer het grootste afzonderlijke element (afbeelding of tekstblok) op de pagina werd weergegeven. Het markeert het punt in de laadtijdlijn van de pagina waarop het belangrijkste (of grootste) stuk inhoud van de pagina begon te laden. De LCP en FCP kunnen hetzelfde zijn, wanneer het grootste pagina-element het eerste is dat wordt geladen.
- **Time to interactive (TTI):** De TTI is een indicatie van de tijd tussen het begin van het laden en het moment waarop de pagina betrouwbaar kan reageren op gebruikersinvoer. Als zodanig is het een goede manier om te meten hoelang de gebruiker uiteindelijk wacht tot de pagina is geladen. Het is noodzakelijk om de TTI te bepalen om de Total blocking time te kunnen berekenen. 
- **Total blocking time (TBT):** TBT meet de hoeveelheid tijd dat de main thread van de browser geblokkeerd is. Het telt de tijd waar de browser meer dan 50 milliseconden (ms) heeft besteed aan het afhandelen van een taak die ervoor zorgt dat de pagina traag reageert en gebruikersinteracties blokkeert. Bij elke lange taak wordt alleen het deel van de tijd na de eerste 50 ms meegeteld voor de TBT. Taken die 50 ms of korter duren, zijn niet inbegrepen in dit kengetal.
- **Cumulative layout shift (CLS):** De CLS is een van de laatste kengetallen die worden bepaald, nadat de pagina volledig is geladen. Dit beschrijft de mate waarin de paginalay-out verschuift (zichtbare elementen bewegen van de ene plaats naar de andere) nadat de pagina interactief is geworden, wat de visuele stabiliteit aangeeft.  
- **Interaction to next paint (INP):** De INP is een indicatie van de algehele responsiviteit van een pagina op gebruikersinteracties. Het meet de tijd tussen klik- of toetsenbordinteracties met de pagina en elke visuele feedback. Omdat het pagina-interacties vereist die verder gaan dan het laden van de eerste pagina, is INP *alleen beschikbaar voor transactiecontroleregels*.


## Dashboardrapportage

U kunt alle kengetallen rapporteren op een aangepast dashboard. Voeg gewoon een aangepaste rapporttegel toe van het type [Eenvoudige lijst / grafiek]([LINK_URL_4]). Klik vervolgens op de instellingenknop [SHORTCODE_1] [SHORTCODE_2] op de tegel en kies de waarden die u wilt weergeven door hun selectievakjes aan te vinken.

U kunt de Core Web Vitals van transacties voor elke afzonderlijke stap weergeven. U moet de opties *Waterval* en *Prestatiekengetallen* activeren voor elke stap die u in de grafiek wilt weergeven. In de informatie over [stapinstellingen]([LINK_URL_5]) leest u hoe dit werkt.

![screenshot detail tegelinstellingen]([LINK_URL_6])

## Core Web Vitals in transactiecontroleregels

Een [watervalgrafiek]([LINK_URL_7]) in een [transactiecontroleregel]([LINK_URL_8]) geeft Core Web Vitals en [W3C Navigatietijden]([LINK_URL_9]) weer. Uptrends toont deze kengetallen voor alle gespecificeerde navigaties in een stap. 

![screenshot meerdere navigaties in een transactiestap]([LINK_URL_10])