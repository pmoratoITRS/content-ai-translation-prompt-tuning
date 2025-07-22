{
  "hero": {
    "title": "Overgang van User-Agent naar Client hints"
  },
  "title": "Overgang van User-Agent naar Client hints",
  "summary": "Uptrends' Real User Monitoring gebruikt een user agent request header voor het verzamelen van gebruikersdata. Google zet deze user agent string om naar client hints in toekomstige versies van Chromium-gebaseerde browsers.",
  "url": "/support/kb/rum/client-hints",
  "translationKey": "https://www.uptrends.com/support/kb/rum/client-hints"
}
## Wat is de User-Agent?
De User-Agent (UA) is een HTTP request header die wordt gebruikt om de webpagina aan te passen aan de specificaties van de browser. Wanneer een webserver een request voor een webpagina ontvangt van de browser van een client, stuurt de browser een request header die de user agent string bevat. Dit vertelt de server welk browsertype zich aan de andere kant bevindt. Alvorens te reageren door de pagina te verzenden, zal de webserver de webpagina afstemmen zodat de inhoud wordt aangepast voor dit specifieke browsertype. 

De user agent string voor een Chrome request header kan er ongeveer zo uitzien:  
`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36`

Bij gebruik van Uptrends' [Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="nl" >}}) wordt een klein script toegevoegd op de pagina's die u met RUM volgt. Wanneer uw gebruikers een webpagina openen die een RUM-script bevat, legt dit via de HTTP User-Agent request header informatie vast over de browser, het platform waarop het draait en de mogelijkheden ervan. Nadat de pagina volledig is geladen, bundelt het script de verzamelde data met informatie over de browser en de locatie van de bezoeker en stuurt deze naar uw Uptrends-dashboard. 
## Waarom client hints en wat verandert er?
Op dit moment verzamelt Uptrends data over de browser van de gebruiker, de besturingssystemen van het apparaat en versies via de user agent string. Google Chrome is nu bezig deze string over te zetten naar User-Agent Client Hints (UA-CH) voor alle Chrome-apparaten en Chromium-gebaseerde browsers, inclusief Microsoft Edge. Met client hints wordt deze informatie verdeeld in kleinere afzonderlijke secties, niet meer in een lange string met data. 

Er zijn twee redenen waarom Google dit doet; het is een betere manier om de privacy van de webbezoeker te beschermen en een methode om de data te retourneren in een voor ontwikkelaars gebruiksvriendelijker formaat.
## Welke invloed heeft dit op RUM monitoring?
Uptrends is voorbereid op deze wijziging en zal het script dienovereenkomstig bijwerken. Er is **geen actie vereist** aan de kant van de klant.

De informatie die met de huidige user agent wordt verzameld, zal geleidelijk worden verminderd. Dit betekent dat er in de toekomst mogelijk minder nauwkeurige gebruikersinformatie beschikbaar is voor monitoring. Zodra dit verandert en onze scriptinstellingen aan de kant van de klant moeten worden aangepast, zullen we u hiervan op de hoogte stellen.

Als startpunt voor meer achtergrondinformatie over deze overgang en de fasen van de UA-reductie met Chromium M101, [kijkt u op User-Agent Reduction op The Chromium Projects](https://www.chromium.org/updates/ua-reduction/).

{{< callout >}} **Opmerking**: Als u zich zorgen maakt over het RUM-script en gebruikersprivacy, vertelt ons Knowledge Base-artikel u meer over [Real User Monitoring en privacy]({{< ref path="/support/kb/rum/rum-and-user-privacy" lang="nl" >}}) {{< /callout >}}
