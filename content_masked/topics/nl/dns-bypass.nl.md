{
  "hero": {
    "title": "DNS bypass"
  },
  "title": "DNS bypass",
  "summary": "Begrijp en leer hoe en of een DNS bypass moet worden ingesteld voor een controleregeltype transactie of Full Page Check. Deze bypass kan worden toegevoegd aan het browsertype 'Chrome met extra kengetallen'. De DNS bypass zorgt ervoor dat de webpagina wordt omgezet naar een opgegeven domeinnaam of IP-adres.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/dns-bypass",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De DNS bypass zorgt ervoor dat de webpagina wordt omgezet naar een opgegeven domeinnaam of IP-adres. 

U heeft dit misschien nodig om bijvoorbeeld de specifieke locatie van een website succesvol te monitoren en te controleren, als de site deel uitmaakt van een Content Delivery Network (CDN) of load-balancing-oplossing of in een van deze [DNS bypass-scenario's]([LINK_URL_1]). 

## Welke controleregels gebruiken DNS bypass

De Uptrends DNS bypass is geïmplementeerd in de controleregel [Full Page Check]([LINK_URL_2]) en in [transactie]([LINK_URL_3])-controleregels. Deze is alleen beschikbaar voor het browsertype _Chrome met extra kengetallen_. 

Voor andere controleregeltypes, zoals HTTPS, kunt u host headers gebruiken. Lees meer over deze soortgelijke functie in ons Knowledge Base-artikel [Andere websites dan de productieserver monitoren]([LINK_URL_4]).

## Waarom een DNS bypass gebruiken? 
Wanneer Uptrends een URL in de browser laadt voor een Full Page Check of een transactie, zal de browser een DNS-service op een externe server vragen om de gevraagde domeinnaam te vertalen naar een IP-adres. Het heeft dit adres nodig voor de feitelijke HTTP request. Een FPC bootst exact na wat de browser van een gewone eindgebruiker zou doen. 

Voor monitoring- of testdoeleinden is dit mogelijk niet voldoende. Wat als u nog steeds de URL van uw bedrijf wilt gebruiken, maar een specifieke server of IP-adres moet targeten in plaats van te vertrouwen op de reguliere DNS?

Met de DNS bypass kunt u precies dat doen. U kunt een vast IP-adres (of een andere CNAME-domeinnaam) opgeven dat moet worden gebruikt wanneer de browser verbinding moet maken met een bepaalde domeinnaam. Het omzeilt of overschrijft in wezen het normale DNS-systeem. Op deze manier werkt het zeer vergelijkbaar met het _hosts file_ op Windows of Linux.
## Een DNS bypass toevoegen

1.  Bij een Full Page Check-controleregel gaat u naar [SHORTCODE_3] Monitoring > Controleregels beheren [SHORTCODE_4].
2.  Klik op de naam van de controleregel om de instellingen van de controleregel te openen.
3.  Zorg ervoor dat _Browser type_ Chrome met extra kengetallen is geselecteerd.
4.  Ga naar het tabblad [SHORTCODE_5] Extra [SHORTCODE_6].
![]([LINK_URL_5])
5.  Klik onder _Verbinding_ op [SHORTCODE_7] DNS bypass toevoegen [SHORTCODE_8]
6.  Voer het _Brondomein_ en _Doeldomein_ in (houd er rekening mee dat om veiligheidsredenen niet alle doeldomeinen worden ondersteund).
7.  Klik op de knop [SHORTCODE_9]Opslaan[SHORTCODE_10] voordat u de pagina verlaat.

 [SHORTCODE_1]
**Opmerking**: U kunt jokertekens gebruiken in de naam van het _brondomein_, maar niet in het doeldomein. U kunt bijvoorbeeld een regel *acc.example.com naar www.example.com maken die requests naar server1-acc.example.com omleidt naar www.example.com.
[SHORTCODE_2]

## Wanneer een DNS bypass moet worden gebruikt  [ANCHOR_1]
Wanneer wilt u ervoor kiezen om de DNS-server die als standaard wordt gebruikt, te omzeilen? Dit zijn scenario's waarin dit nuttig of noodzakelijk kan zijn: 
### DTAP / UAT-server (User Acceptance Testing)
U wilt de performance van webpagina's testen en monitoren in een DTAP-omgeving of op een UAT-server (User Acceptance Testing). Deze pagina's geven u een actueel beeld van hoe ze er in productie uit zullen zien en daarom wellicht monitoring vereisen. Met een DNS bypass vertelt u Uptrends op de gewenste locatie te monitoren en controleren.
### Verschillende SSL-configuratie
Stel dat uw testomgeving dezelfde SSL-certificaten moet gebruiken als uw productieomgeving. Het webserveradres voor het controleren van certificaten moet identiek zijn aan het adres dat is gespecificeerd in het certificaat, anders resulteert de full page check in een fout. 
### Preproductie-website op een extern domein
Uw website wordt bijvoorbeeld opnieuw ontworpen door een derde partij. U wilt de nieuwe webpagina's testen en monitoren op hun huidige locatie op de webserver van de websiteontwikkelaars.
### Webpagina op één node in een webcluster
Gebruik een DNS bypass als u wilt verzekeren dat elke afzonderlijk node in het cluster goed werkt en deze afzonderlijk wilt monitoren.
### Webpagina op een CDN origin machine
Uw website bevindt zich bijvoorbeeld in een Content Delivery Network (CDN). Het is mogelijk dat u de website op de origin server wilt testen en controleren, niet de gecachete op de CDN edge servers. Configureer een DNS bypass om Uptrends te vertellen rechtstreeks op de origin server te controleren.
### Webpagina op een specifieke CDN-locatie 
Als uw website zich in een Content Delivery Network (CDN) bevindt, wilt u misschien een van de webpagina-instanties in de cache op een van de edge servers in het delivery network monitoren. Door een DNS bypass te configureren, kan Uptrends rechtstreeks naar deze server kijken. Maar er is eigenlijk een betere manier om die locaties te monitoren: stel een (FPC) controleregel in en laat die controles uitvoeren vanaf [controlestations]([LINK_URL_6]) in de betreffende regio. 
### Webpagina of website binnen een intern netwerk
Wanneer u persoonlijke controlestations binnen uw netwerk gebruikt, kan een FPC een interne netwerkroute gebruiken die ertoe leidt dat het adres van de pagina wordt omgezet via de interne server. Als u liever van buiten uw netwerk test, kunt u een DNS bypass gebruiken om de netwerkroute te wijzigen. Dit kan een rol spelen wanneer er verschillende pagina's en manieren zijn om intern en extern in te loggen. 