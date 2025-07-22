{
  "hero": {
    "title": "Watervalgrafiek"
  },
  "title": "Watervalgrafiek",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/watervalgrafiek",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/waterfall-chart"
}

De watervalgrafiek is een visuele weergave van de resultaten van de controleregelcheck met betrekking tot het laden van pagina-elementen. De waterval is onderdeel van de details van de controle. 

Bij Full Page Checks (FPC's) wordt de waterval standaard gegenereerd. Bij transactiecontroleregels kunt u per stap beslissen of u een waterval wilt toevoegen, en het Knowledge Base-artikel [Transactiescreenshots en watervallen gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}}) bevat meer informatie over hoe u dat doet. 

## Watervalgrafieken gebruiken voor debuggen

Het is één ding om de paginalaadtijd te zien, maar de waterval splitst de laadtijdprestaties van uw pagina op voor elk element.

-   Bekijk de tijd voor resolve, TCP connect, HTTPS handshake, verzenden, wachten, ontvangen en timeout voor elk element. De timings worden verder uitgelegd in het Knowledge Base-artikel [Waterval timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="nl" >}}).
-   Bekijk de voortgang van het laden van de pagina. Het is eenvoudig om trage en paginablokkerende elementen in de watervalgrafiek te ontdekken.
-   Vind mislukte pagina-elementen. U kunt de request en response headers onderzoeken op aanwijzingen over de fout. U kunt bijvoorbeeld achterhalen of een CDN node de verkeerde inhoud heeft gestuurd of dat de response te traag was.

## Waar bevindt zich de watervalgrafiek? {id="where-is-the-waterfall-chart-located"}

Voor zowel FPC's als transactiecontroleregels bevinden de watervallen zich in de details van de controle, maar de toegang ertoe verschilt enigszins. Voer de hieronder beschreven stappen uit.

### Een FPC-waterval openen

Om het watervalrapport te openen moet u de details van de controle van de controleregel openen. Volg deze stappen:

1. Ga naar het dashboard *Controleregel log*. U kunt er snel komen door 'Controleregel log' in de menu-zoekbalk in te voeren.

2. Open een van de FPC-controleregelchecks door op de rij te klikken. 

3. De details van de controle wordt geopend, met onderaan het watervalrapport.

### Een waterval van een transactiecontroleregelstap openen

Het watervalrapport bevindt zich in de details van de controle.

1. Ga naar de *Controleregel log* en open een transactiecontroleregelcheck.

2. Onderaan vindt u de **Resultaten per stap**. Klik op het watervalpictogram {{< AppElement type="iconWaterfall" >}}{{< /AppElement >}} om de details van de waterval te openen. 

### Voorbeeld watervalgrafiek 

Als u de waterval heeft geopend, ziet de grafiek er ongeveer zo uit:

![screenshot van watervalgrafiek](/img/content/scr_waterfall_chart-overview.min.png)

## Wat wordt weergegeven in de watervalgrafiek? {id="what-is-presented-in-the-waterfall-chart"}

De watervalgrafiek toont de namen (URL's) van de pagina-elementen in de eerste kolom, vervolgens de grootte van het pagina-element en de laadtijdmetingen, genomen tijdens de controleregelcheck, voor alle pagina-elementen die werden geladen. 
De metingen worden chronologisch weergegeven van links naar rechts met één rij voor elk pagina-element.
Om een pagina-element te laden zijn een aantal stappen nodig. 

De verschillende stappen zijn kleurgecodeerd. De legenda boven de grafiek toont de kleurcodering. 
Meer informatie over wat elke stap betekent, is te vinden in het Knowledge Base-artikel [Waterval timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="nl" >}}).

Een watervalgrafiek in een transactiecontroleregel toont [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}})- en [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}})-kengetallen voor elke navigatie in een transactiestap. De kengetallen worden boven de watervalgrafiek weergegeven. Wanneer een stap meerdere navigaties bevat, toont de grafiek de kengetallen voor alle navigaties door een verticale donkergroene lijn weer te geven. Wanneer u over de lijn hovert, wordt het exacte kengetal weergegeven. 

Onder de watervalgrafiek staat een overzicht van alle timings per request type. 

## Timing details

Om meer gedetailleerde informatie of achtergrondinformatie over de metingen van de pagina-elementen te krijgen kunt u hoveren over de metingen voor een element en er verschijnt een pop-up met de details voor dit specifieke element.

![screenshot waterfall timings popup](/img/content/scr_waterfall_chart-popup-detail.min.png)


## Het paneel request/response

Voor elk afzonderlijk element in de waterval kunt u op het **+**-symbool klikken om het request/response-paneel te openen. Dit paneel bevat informatie over de request die is gedaan om het element op te halen en de erop volgende response. 

Het bevat de volgende informatie:
- De gebruikte request URL, methode en protocol
- Een overzicht van de request headers die in de request zijn opgenomen
- Het IP-adres van de reagerende server
- Informatie over de (on)gecomprimeerde omvang van het element:
    - **Netwerkomvang**: het werkelijke aantal bytes dat is gedownload (gecomprimeerde omvang)
    - **Resource-omvang/ongecomprimeerde omvang**: omvang van het element na decompressie, indien van toepassing
- Alle response headers die in de response zijn opgenomen

Als u een [Full Page Check met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}) gebruikt, bevatten de request/response-panelen ook de relevante **TLS-informatie** voor dat element. Bovendien kunnen deze watervallen verdere elementdetails weergeven, zoals de request die wordt gecachet, vooraf wordt geladen of wordt afgebroken, en ze ondersteunen data-URI's (wanneer de HTML-pagina inline afbeeldingsdata bevat). Deze extra informatie is, waar van toepassing, beschikbaar in de request/response-panelen voor afzonderlijke elementen. 

![Request/response paneel](/img/content/scr-fpc-waterfall-requestresponse-panel.min.png)

## Andere opties om de informatie te verfijnen

De kolommen met het pagina-elementnummer (#), de elementnaam (URL) en de elementgrootte (Grootte) kunnen worden aangeklikt om de volledige watervalgrafiek te sorteren op basis van de waarden in die kolommen. 

Als u veel elementen op de pagina heeft, kan het nodig zijn om de grafiek te filteren op (een deel van) de naam van het pagina-element. Gebruik het veld **Filter** om uw term in te vullen waarop u wilt filteren.

## De watervalgrafiek exporteren

Het watervalgrafiek kan worden geëxporteerd als een pdf-bestand. Deze pdf's kunnen worden gebruikt als back-up van uw watervalmetingen. Soms kan een pdf handig zijn om watervaldiagrammen aan derden te tonen zonder dashboards te delen.

Klik op de knop **Exporteren als PDF** rechts boven de grafiek om een pdf-exemplaar van uw watervalgrafiek te genereren en op te slaan.
