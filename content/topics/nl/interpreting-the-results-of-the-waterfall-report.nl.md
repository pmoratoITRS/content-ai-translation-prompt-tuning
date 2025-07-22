{
  "hero": {
    "title": "De resultaten van het watervalrapport interpreteren"
  },
  "title": "De resultaten van het watervalrapport interpreteren",
  "summary": "Once you have opened the report, how do you interpret the results of the waterfall report.",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/de-resultaten-van-het-watervalrapport-interpreteren",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/interpreting-the-results-of-the-waterfall-report"
}

Wanneer u het watervalrapport hebt geopend (zie [Het watervalrapport openen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart#where-is-the-waterfall-chart-located" lang="nl" >}})), ontvangt u een grote hoeveelheid gegevens over uw pagina en de elementen ervan. Elk pagina-element vereist een request, TCP Connect, HTTPS Handshake, verzend-, wacht- en ontvangsttijd. Nadat de ontvangsttijd is voltooid, verwerkt de browser het element. Eén enkele pagina kan meer dan honderd elementen bevatten die door de browser moeten worden verwerkt. De totale laadtijd van de elementen of van slechts enkele trage elementen kan ervoor zorgen dat uw pagina uw verwachte maximale laadtijden overschrijdt. In het voorbeeld hieronder ziet u dat deze Full page check de maximale laadtijd van 2,5 seconden heeft overschreden.

In de rapportheader staat algemene informatie over de controle, met inbegrip van het gebruikte controlestation, de URL en welke browser bij de test is gebruikt. Bij Resultaat wordt de specifieke oorzaak van de fout weergegeven. Deze specifieke test mislukte vanwege het overschrijden van de maximale laadtijd met errorcode 6000. Uitleg over andere mogelijke foutcodes zijn te vinden op de pagina [Fouttypes](/support/kb/alerting/fouten/fouttypes).

![](/img/content/e219780e-36db-4aa0-bdd9-a6f7898ecdb0.png)

## Waardoor werd de fout precies veroorzaakt?

Als u omlaag scrolt op deze pagina ziet u een lijst met de pagina-elementen. Deze verschijnen in de volgorde waarin ze laden in de browser. Sommige delen laden asynchroon, en andere elementen zijn onderling afhankelijk en laden pas nadat andere elementen op de pagina zijn geladen. Rechts van elk element ziet u een staafdiagram. Elke kleur op het staafdiagram geeft een andere verbindingsstatus weer. Door de elementen op een tijdlijn te plaatsen, worden ze in een watervalperspectief weergegeven. Gekleurde delen in de staven geven aan hoe lang elk element erover deed om te laden. Door het rapport te bekijken, kunt u snel zien welke pagina-elementen er het langst over deden voordat de browser ze ontving.

In dit voorbeeldrapport duurde het laden bij meerdere handshakes (de goudkleurige staven) te lang. De elementen die de buitensporig lange handshake- en wachttijden veroorzaken, zijn een analytische applicatie van een derde partij en en een trage request om een JavaScript-bestand. Hoewel deze bestanden er het langst over deden, ziet u in de rest van het watervalrapport er dat andere elementen zijn met handshake- en wachttijden die, hoewel korter, cumulatief uw totale laadtijd kunnen beïnvloeden.

![](/img/content/2fc286e2-26d2-4b40-96f8-462734d4c509.png)

## De request- en responsheaders bekijken

Uw request- en responsheaders laten het volledige verhaal zien. Door de request- en responsheaders te bekijken, kunt u precies zien waar de browser om vroeg en wat het resultaat is van de request. Om de request- en responsheaders van een element te openen klikt u op het plusteken (\+) rechts van de naam van het element in de lijst. In onderstaand voorbeeld vroeg de browser om een Javacript-bestand, maar resulteerde de request in een langdurige vertraging van de handshake- en responstijd.

![](/img/content/68f3ff2b-15a3-4f5d-b1be-233bd9ca55e2.png)

## Samenvatting van het rapport

Onder aan het watervalrapport ziet u de samenvatting. De eerste kolom bevat de kleurlegenda voor de gekleurde staven in het watervalgedeelte van het rapport. Rechts daarvan ziet u de totale tijd en de gemiddelde tijd van elk van de verbindingsstatussen. De rest van de samenvatting bevat tellingen van elementtypes en paginatotalen.

![](/img/content/eed630d9-4882-441f-a303-8bdc9fefbfc1.png)

## Zoek de elementbron door domeingroepen te gebruiken 

Als uw controleregel een FPC\+ is, kunt u snel de bron zien van uw elementen die problemen veroorzaken.

1.  Onthoud het elementnummer uit het watervalrapport dat u wilt onderzoeken.
2.  Klik op de knop Domeingroepen rechts boven de waterval.  
       
    ![](/img/content/eabecf5d-acd3-437a-bba0-73ed862213e4.png)  
      
3.  Zoek het elementnummer in de lijst om de domeingroep te bekijken.  
    ![](/img/content/fa083053-33a5-489f-a1e2-d6c92241164c.png)
