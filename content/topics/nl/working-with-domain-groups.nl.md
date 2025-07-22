{
  "hero": {
    "title": "Werken met domeingroepen"
  },
  "title": "Werken met domeingroepen",
  "summary": "Begrijp en leer hoe je een Full Page Check instelt.",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/werken-met-domeingroepen",
  "translationKey": "https://www.uptrends.com/support/kb/full-page-check/working-with-domain-groups"
}

Met de controleregel Full page check\+ (FPC\+) kunt u snel de bron van pagina-elementen vinden. Meestal heeft een pagina veel elementen die van verschillende providers komen. U kunt bijvoorbeeld inhoud hebben die van een CDN komt, advertenties die van Google komen en plug-ins voor sociale media die uw meest recente posts op uw pagina plaatsen. Met domeingroepen zult u merken dat u snel de probleembronnen kunt vinden. Voor het beheren van domeingroepen kunt u het beste de **Standaard set** bekijken.

{{< callout >}}
**Opmerking:** Meer informatie over het bekijken van uw pagina-elementen per domeingroep is te vinden in de Knowledge Base: [De resultaten van het watervalrapport interpreteren]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="nl" >}}).
{{< /callout >}}

## De Standaard set

Uptrends heeft een set standaarddomeinen gecreëerd. Deze set bevat de meestgebruikte domeinen, zodat u verder misschien niets hoeft te doen. Maar we leven natuurlijk niet in een standaardwereld, en de standaard set past misschien niet bij uw behoeften. Daarom biedt Uptrends verschillende opties, u kunt:

-   de standaard set rechtstreeks wijzigen (niet aanbevolen);
-   de standaard set kopiëren en de kopie wijzigen;
-   een geheel nieuwe domeingroep van de grond af aan creëren.

Voordat u aan de slag gaat met de instellingen voor domeingroepen, is het belangrijk dat u de delen begrijpt die een domeingroep definiëren.

{{< callout >}}
**Opmerking:** Wanneer u de Standaard set opent (in de volgende stap), ziet u rechtsboven op de pagina de knop {{< AppElement type="button" >}}Deze domeingroep kopiëren{{< /AppElement >}}. We raden u aan deze optie te gebruiken om de Standaard set te dupliceren en deze niet rechtstreeks te bewerken.
{{< /callout >}}

## Domeingroepen en de Standaard set openen

Wanneer u Domeingroepen voor het eerst opent, staat er één domeingroep in de lijst, de Standaard set.  
Om de pagina Domeingroepen te openen doet u het volgende:

1.  Ga naar het menu Account op het hoofdmenu.
2.  Klik op Domeingroepen onder Accountopties.
3.  Klik op Standaard set om de editor te openen.

![](/img/content/8ca9e73e-26ae-42fd-a052-d909d5eac792.png)

### De gedefinieerde groepen

Nadat u de Standaard set hebt geopend, ziet u in het gedeelte **Groepen** vijf domeingroepen die zijn gedefinieerd. Bij elk van de domeingroepen kunt u extra domeinen toevoegen met de knop {{< AppElement type="button" >}}Regel toevoegen{{< /AppElement >}}. U kunt een regel ook uitsluiten of verwijderen door 'Uitsluiten' te kiezen bij de definitie van de regel of door op de minknop rechts van de regel te klikken om de regel te verwijderen.

#### 1st party

Als u de groep uitvouwt (klik op het driehoekje naast **Naam**), ziet u dat de ontwikkelaars standaard de selectievakjes **Automatisch alle requests van de URL van de controleregel meenemen** en **Dit is first party content** hebben geselecteerd. Als deze selectievakjes zijn geselecteerd, weet het systeem dat het alle content moet opnemen die van de URL komt en deze aan de controleregel moet leveren. First party content is uw inhoud; dat wil zeggen dat u de content bepaalt. Mogelijk hebt u nog andere domeinen die u bepaalt die bijdragen aan de inhoud op de pagina. Zorg er dan voor dat u deze toevoegt met de knop {{< AppElement type="button" >}}Regel toevoegen{{< /AppElement >}}.  

#### Statistics

Analytische content runt op de achtergrond en analytische services dragen vaak bij aan slechte performance op pagina's. U kunt de URL's toevoegen van elke analytische tool van derde partijen die u gebruikt. Als u Google Analytics wilt monitoren, selecteer dan niet het selectievakje **Google Analytics blokkeren** op de pagina waar u de controleregel definieert.

#### CDN

Soms falen content delivery networks (CDN) of hebben zij performanceproblemen. Door de URL's en regels van uw CDN's te definiëren, kunt u de performance van uw CDN's in de gaten houden.

#### Social

Hoewel plug-ins van sociale-media goed werken, kunnen uw sociale-mediacontent en actieknoppen een verwoestend effect hebben op uw webperformance. Neem de URL's van uw sociale-mediaelementen hier op. Uptrends heeft alvast URL's van de zes meest gebruikte sociale media opgenomen.

#### Ads

We hebben allemaal de clickbait-sites gezien die zoveel advertenties op de pagina hebben dat je te lang moet wachten op de top 5 kattenfoto's op internet en het opgeeft. Zorg ervoor dat uw advertentieproviders uw pagina's niet traag maken; monitor uw advertentieproviders door de URL's op te nemen in het gedeelte **Ads**.

#### Voeg uw eigen domeingroepen toe

U kunt natuurlijk regels toevoegen aan de reeds gedefinieerde domeingroepen, maar u kunt onder de standaard set nog drie groepen toevoegen op de pagina. Vergeet niet op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} te klikken voordat u de pagina verlaat.
