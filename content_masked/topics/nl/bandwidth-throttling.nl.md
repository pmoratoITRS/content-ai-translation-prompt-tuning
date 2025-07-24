{
  "hero": {
    "title": "Bandbreedte begrenzen"
  },
  "title": "Bandbreedte begrenzen",
  "summary": "FPC's en transactiecontroleregels bieden twee verschillende methodes voor het begrenzen van uw verbindingssnelheden: gesimuleerde en browsergebaseerde begrenzing met Chrome.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/bandbreedte-begrenzen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Om uw synthetic monitoring nauwkeuriger af te stemmen op de werkelijke verbindingssnelheden van uw gebruikers raden we u aan bandbreedtebegrenzing te gebruiken met uw Full page check (FPC)- en transactiecontroleregels.

## Waarom zou u bandbreedtebegrenzing gebruiken?

Uptrends' controlestationcomputers werken binnen datacenters. Hun native snelheden weerspiegelen die van een doorsnee gebruiker die via een hogesnelheidsnetwerk werkt, net zoals het netwerk dat u op uw kantoor gebruikt. Als uw gebruikers voornamelijk bestaan uit desktopgebruikers, vindt u waarschijnlijk dat onze native snelheden op Uptrends' controlestations uw gebruikers prima weergeven. Maar als uw gebruikers uw site of dienst gebruiken met mobiele apparaten of tragere DSL-verbindingen gebruiken, moet u overwegen een controleregel te configureren die de ervaringen van deze gebruikers weerspiegelt. Daarbij komt bandbreedtebegrenzing van pas.

## Types bandbreedtebegrenzing

Uptrends biedt twee types bandbreedtebegrenzing: gesimuleerde en browsergebaseerde begrenzing. U heeft bij beide types dezelfde opties voor verbindingssnelheid. Browsergebaseerde begrenzing is alleen beschikbaar voor Chrome en gesimuleerde bandbreedtebegrenzing is beschikbaar voor andere browsertypes.

### Browsergebaseerd

U kunt browsergebaseerde bandbreedtebegrenzing gebruiken als u een Chrome-browser kiest bij uw FPC-controleregel. Meestal wordt bij browsergebaseerde bandbreedtebegrenzing gebruikgemaakt van dezelfde bandbreedtebegrenzingsopties die beschikbaar zijn in de Chrome-ontwikkelaarstools. Chrome verschilt van de gesimuleerde begrenzing doordat Chrome latentie toepast naast het simuleren van een lagere bandbreedte. Browsergebaseerde begrenzing geeft een nauwkeuriger meting, vooral op webpagina’s die heel weinig of heel veel verbindingen gebruiken. Bovendien houdt Chrome het aantal verbindingen bij en voegt ze samen, wat nauwkeuriger is op websites met een lager of hoger aantal bronnen dan gemiddeld. 

Om browsergebaseerde begrenzing in te schakelen doet u het volgende:

1.  Maak een nieuwe FPC-controleregel of open een bestaande.
2.  Open het tabblad [SHORTCODE_1]Extra[SHORTCODE_2].
3.  Selecteer **Browser** in het gedeelte [SHORTCODE_3]Bandbreedte begrenzen[SHORTCODE_4] samen met de verbindingssnelheid die u wilt gebruiken (zie hieronder).
4.  Klik op [SHORTCODE_5]Opslaan[SHORTCODE_6].

### Gesimuleerd

U kunt gesimuleerde begrenzing configureren met een browser naar keuze, behalve Chrome. Gesimuleerde begrenzing gebruikt een proxy om u een redelijke simulatie te geven van de verschillende verbindingssnelheden die uw gebruikers kunnen hebben.

Het controlestation begrenst elke verbinding die de browser maakt, waarbij de gemiddelde hoeveelheid bandbreedte die beschikbaar is voor het gekozen verbindingstype wordt gesimuleerd. Het controlestation houdt geen rekening met netwerklatentie en maakt berekeningen op basis van een gemiddeld aantal verbindingen.

1.  Maak een nieuwe FPC-controleregel of open een bestaande.
2.  Open het tabblad [SHORTCODE_7]Extra[SHORTCODE_8].
3.  Selecteer uw [SHORTCODE_9]Browser type[SHORTCODE_10].
![Gesimuleerde bandbreedtebegrenzing]([LINK_URL_1])
4.  Selecteer **Gesimuleerd** in het gedeelte [SHORTCODE_11]Bandbreedte begrenzen[SHORTCODE_12] samen met de verbindingssnelheid die u wilt gebruiken (zie hieronder).
5.  Klik op [SHORTCODE_13]Opslaan[SHORTCODE_14].


## Verbindingstypes

We baseren de verschillende verbindingstypes waaruit u kunt kiezen bij het toepassen van bandbreedtebegrenzing op werkelijke gebruiksscenario’s en niet op de theoretische maximale snelheden die deze technologieën kunnen bieden. Browsergebaseerde begrenzing past netwerklatentie toe op uw resultaten.

**ADSL**: 4 Mbit down, 0,5 Mbit up, 80 ms round trip time  
**Kabel**: 5 Mbit down, 1 Mbit up, 50 ms round trip time  
**Glasvezel**: 15 Mbit down, 3 Mbit up, 10 ms round trip time  

**2G**: 200 Kbit down, 200 Kbit up, 1000 ms round trip time  
**3G**: 1 Mbit down, 500 Kbit up, 300 ms round trip time  
**4G**: 4 Mbit down, 4 Mbit up, 230 ms round trip time
