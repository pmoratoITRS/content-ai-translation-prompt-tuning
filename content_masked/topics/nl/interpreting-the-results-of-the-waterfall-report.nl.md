{
  "hero": {
    "title": "De resultaten van het watervalrapport interpreteren"
  },
  "title": "De resultaten van het watervalrapport interpreteren",
  "summary": "Once you have opened the report, how do you interpret the results of the waterfall report.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-resultaten/de-resultaten-van-het-watervalrapport-interpreteren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wanneer u het watervalrapport hebt geopend (zie [Het watervalrapport openen]([LINK_URL_1])), ontvangt u een grote hoeveelheid gegevens over uw pagina en de elementen ervan. Elk pagina-element vereist een request, TCP Connect, HTTPS Handshake, verzend-, wacht- en ontvangsttijd. Nadat de ontvangsttijd is voltooid, verwerkt de browser het element. Eén enkele pagina kan meer dan honderd elementen bevatten die door de browser moeten worden verwerkt. De totale laadtijd van de elementen of van slechts enkele trage elementen kan ervoor zorgen dat uw pagina uw verwachte maximale laadtijden overschrijdt. In het voorbeeld hieronder ziet u dat deze Full page check de maximale laadtijd van 2,5 seconden heeft overschreden.

In de rapportheader staat algemene informatie over de controle, met inbegrip van het gebruikte controlestation, de URL en welke browser bij de test is gebruikt. Bij Resultaat wordt de specifieke oorzaak van de fout weergegeven. Deze specifieke test mislukte vanwege het overschrijden van de maximale laadtijd met errorcode 6000. Uitleg over andere mogelijke foutcodes zijn te vinden op de pagina [Fouttypes]([LINK_URL_2]).

![]([LINK_URL_3])

## Waardoor werd de fout precies veroorzaakt?

Als u omlaag scrolt op deze pagina ziet u een lijst met de pagina-elementen. Deze verschijnen in de volgorde waarin ze laden in de browser. Sommige delen laden asynchroon, en andere elementen zijn onderling afhankelijk en laden pas nadat andere elementen op de pagina zijn geladen. Rechts van elk element ziet u een staafdiagram. Elke kleur op het staafdiagram geeft een andere verbindingsstatus weer. Door de elementen op een tijdlijn te plaatsen, worden ze in een watervalperspectief weergegeven. Gekleurde delen in de staven geven aan hoe lang elk element erover deed om te laden. Door het rapport te bekijken, kunt u snel zien welke pagina-elementen er het langst over deden voordat de browser ze ontving.

In dit voorbeeldrapport duurde het laden bij meerdere handshakes (de goudkleurige staven) te lang. De elementen die de buitensporig lange handshake- en wachttijden veroorzaken, zijn een analytische applicatie van een derde partij en en een trage request om een JavaScript-bestand. Hoewel deze bestanden er het langst over deden, ziet u in de rest van het watervalrapport er dat andere elementen zijn met handshake- en wachttijden die, hoewel korter, cumulatief uw totale laadtijd kunnen beïnvloeden.

![]([LINK_URL_4])

## De request- en responsheaders bekijken

Uw request- en responsheaders laten het volledige verhaal zien. Door de request- en responsheaders te bekijken, kunt u precies zien waar de browser om vroeg en wat het resultaat is van de request. Om de request- en responsheaders van een element te openen klikt u op het plusteken (\+) rechts van de naam van het element in de lijst. In onderstaand voorbeeld vroeg de browser om een Javacript-bestand, maar resulteerde de request in een langdurige vertraging van de handshake- en responstijd.

![]([LINK_URL_5])

## Samenvatting van het rapport

Onder aan het watervalrapport ziet u de samenvatting. De eerste kolom bevat de kleurlegenda voor de gekleurde staven in het watervalgedeelte van het rapport. Rechts daarvan ziet u de totale tijd en de gemiddelde tijd van elk van de verbindingsstatussen. De rest van de samenvatting bevat tellingen van elementtypes en paginatotalen.

![]([LINK_URL_6])

## Zoek de elementbron door domeingroepen te gebruiken 

Als uw controleregel een FPC\+ is, kunt u snel de bron zien van uw elementen die problemen veroorzaken.

1.  Onthoud het elementnummer uit het watervalrapport dat u wilt onderzoeken.
2.  Klik op de knop Domeingroepen rechts boven de waterval.  
       
    ![]([LINK_URL_7])  
      
3.  Zoek het elementnummer in de lijst om de domeingroep te bekijken.  
    ![]([LINK_URL_8])
