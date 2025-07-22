{
  "hero": {
    "title": "Tool voor website snelheidstest: PageSpeed Insights"
  },
  "title": "Tool voor website snelheidstest: PageSpeed Insights",
  "summary": "Met Uptrends' gratis testtool voor websitesnelheid krijgt u uw score van Google PageSpeed Insights bij uw gedetailleerde watervalrapport. Lees meer over PageSpeed Insights en hoe Google de paginascore berekent.",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/tool-voor-website-snelheidstest-pagespeed-insights",
  "translationKey": "https://www.uptrends.com/support/kb/full-page-check/website-speed-test-tool-pagespeed-insights"
}

Uw gratis [website snelheidstest](/tools/website-speed-test) bevat een paginascore en aanbevelingen voor performanceverbeteringen van [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/). We hebben de informatie van Google opgenomen bij de resultaten van de Uptrends-testen om u alle informatie te verstrekken die u nodig hebt om de gebruikerservaring van uw pagina te verbeteren. Uptrends geeft u de paginadetails op elementniveau om u te helpen bij het vinden van problematische pagina-elementen en toont u de voortgang van het laden van uw pagina met behulp van een makkelijk te lezen watervalrapport. 

## Wat is PageSpeed Insights?

PageSpeed Insights is een tool van Google voor webontwikkelaars (en voor iedereen die leergierig is) die een overzicht van hun paginaperformance willen zoals die door Google wordt gezien. Google bevat ook aanbevelingen voor performanceverbeteringen om u te helpen bij uw pogingen de snelheid te optimaliseren.

## Waarom is mijn PageSpeed Insights-score veranderd?

Als u in het verleden onze gratis snelheidstesttool hebt gebruikt, kan uw score zijn gewijzigd. Uptrends haalt de PageSpeed Insight-score en de daaruit voortvloeiende aanbevelingen van Google. Uw score is gewijzigd omdat Google de manier heeft gewijzigd waarop de score wordt berekend in de [fifth version of the PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/about).

Voorheen was de PageSpeed Insights-score primair gebaseerd op de conventies die werden gebruikt om de paginagrootte te verkleinen en het renderingproces te versnellen. De nieuwe versie houdt hier rekening mee, maar past de score ook aan op basis van andere factoren die afkomstig zijn van de diagnostische tools van Lighthouse (labgegevens) en veldgegevens (daadwerkelijke ervaringen).

## Hoe berekent Google mijn paginascore?

PageSpeed Insights verzamelt data uit meerdere bronnen voor mobiele en desktopsnelheden die resulteren in een paginascore en aanbevelingen voor het verbeteren van de pagina.

### Labgegevens

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) verzamelt en analyseert data over de paginalaadtijden en wijst ze een [score](https://developers.google.com/web/tools/lighthouse/v3/scoring) toe: ≥90 snel, 50-89 gemiddeld, ≤ 50 traag. Lighthouse baseert de score op:

-   [Eerste weergave met content (FCP)](https://developers.google.com/web/tools/lighthouse/audits/first-contentful-paint): Het moment dat de browser DOM-inhoud voor het eerst genereert.
-   [Eerste nuttige weergave (FMP)](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint): Het moment waarop een gebruiker merkt dat de primaire inhoud is geladen.
-   [Snelheidsindex](https://developers.google.com/web/tools/lighthouse/audits/speed-index): Hoe snel een pagina zichtbaar is geladen.
-   [Eerste keer dat CPU inactief was](https://developers.google.com/web/tools/lighthouse/audits/first-cpu-idle): Wanneer de meeste UI-elementen interactief worden.
-   [Tijd tot interactief](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive): Pagina heeft nuttige inhoud weergegeven, event-handlers zijn geregistreerd en de pagina reageert binnen 50 milliseconden op gebruikersinteracties.
-   [Geschatte invoerwachttijd](https://developers.google.com/web/tools/lighthouse/audits/estimated-input-latency): Input responsiviteit.

### Veldgegevens

Gebruikers van de Chrome-browser van Google kunnen kiezen om de Chrome-browser data te laten verzamelen over de paginaperformance terwijl ze op internet surfen. Wanneer Google de sitescore berekent, gebruikt het deze gegevens om te zien hoe echte gebruikers uw pagina hebben ervaren op basis van:

-   Eerste weergave met content (FCP): Het moment dat de browser DOM-inhoud voor het eerst genereert.
-   [First Input Delay](https://developers.google.com/web/updates/2018/05/first-input-delay): De verstreken tijd tussen de tussen de eerste pagina-interactie van een gebruiker en de respons van de pagina.

Google vergelijkt ook uw paginasnelheden met die van concurrerende pagina's en past de paginascore daarop aan.

### Pagina-audits

Google onderzoekt de huidige pagina en geeft u een lijst met items die goed presteren op uw pagina en items die extra aandacht nodig hebben. In de pagina-audits vindt u informatie over:

-   **Aanbevelingen** of manieren waarop u uw pagina sneller kunt maken,
-   **Diagnostische gegevens** over hoe goed de pagina de best practices in webontwikkeling gebruikt, en
-   **Geslaagde controles** inclusief de lijst met audits die uw pagina met succes heeft voltooid.

Meer discussie over Google PageSpeed Insights vindt u op [Stack Overflow](https://stackoverflow.com/questions/tagged/pagespeed-insights).

## Waarom is uw PageSpeed Insights-score van belang?

Google rangschikt pagina's met hoge scores voor mobiele prestaties hoger, dus u hebt een hoge score nodig om de SEO van uw pagina te verbeteren. Studies hebben bevestigd dat gebruikers snelheid het allerbelangrijkst vinden, en paginaperformance is direct gerelateerd aan bouncepercentages, gebruikerstevredenheid, succespercentages en inkomsten.
