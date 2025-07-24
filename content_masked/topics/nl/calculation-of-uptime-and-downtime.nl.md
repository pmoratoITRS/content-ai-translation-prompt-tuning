{
  "hero": {
    "title": "Berekening van uptime en downtime"
  },
  "title": "Berekening van uptime en downtime",
  "summary": "Hoe bereken je de uptime van uw controleregel op basis van controleresultaten en hoe beïnvloeden gepauzeerde controleregels of onderhoud deze berekening?",
  "url": "[URL_BASE_TOPICS]dashboards-en-rapportages/dashboards/berekening-van-uptime-en-downtime",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Berekeningen van uptime en downtime vormen de basis voor een aantal statistieken in datategels op uw dashboards en voor uw [service level agreements (SLA's))]([LINK_URL_1]). Laten we eens kijken hoe de berekening wordt gedaan en welke factoren van invloed zijn.
## Inleiding tot Uptrends' dubbele controle

Wanneer er een fout op uw website of server wordt gedetecteerd, voert Uptrends altijd een tweede controle uit bij een ander controlestation om de fout te bevestigen. Daarom ziet u gedurende downtime altijd een patroon van onbevestigde fouten en bevestigde fouten in uw [website monitoring]([LINK_URL_2]) dashboards.

Zo werkt standaard monitoring. Als u gelijktijdige monitoring gebruikt, zijn er geen dubbele controles. Bekijk het artikel [Fouten en alerting bij gelijktijdige controleregels]([LINK_URL_3]) om het verschil te begrijpen.

[SHORTCODE_1]
**Tip:** Voor een gedetailleerde analyse van de exacte metingen die worden uitgevoerd, en de gedetecteerde fouten, kunt u uw dashboard **Controleregel log**  bekijken via het menu [SHORTCODE_7] Monitoring > Controleregel log [SHORTCODE_8].
[SHORTCODE_2]

## Hoe wordt het uptimepercentage berekend?

De manier om uptime te berekenen is eenvoudig te begrijpen: neem het aantal seconden dat uw controleregel down was (in een bepaald tijdsbestek) en deel dit door het totale aantal seconden dat uw controleregel gemonitord werd gedurende dat tijdsbestek. De uitkomst hiervan is het downtimepercentage, dat vervolgens van 100% wordt afgetrokken om het uptime percentage te krijgen.

[SHORTCODE_3]
**Tip:** SLA's geven u een uptime als percentage, maar hoeveel tijd is dat eigenlijk? Gebruik de [gratis SLA & uptime calculator]([LINK_URL_4]) om downtime in seconden om te rekenen naar percentage en vice versa. 
[SHORTCODE_4]

### Voorbeeld

Stel dat u een website gedurende 24 uur heeft gemonitord (dus 86.400 seconden) en dat de website binnen dat tijdsbestek 10 minuten (600 seconden) down was. Om de uptime- and downtimepercentages te definiëren wordt de volgende berekening uitgevoerd:

Totale tijd dat uw website down was: 600 seconden  
Totale tijd dat uw website werd gemonitord: 86.400 seconden  
Downtimepercentage = 600 seconden / 86.400 seconden = 0,0069 = 0,69%  
Uptimepercentage = 100% - 0,69% = 99,31%  

[SHORTCODE_5]
**Tip:** Speel wat met de data in uw account om het feitelijke aantal seconden te achterhalen. Met de [aangepaste rapporttegels]([LINK_URL_5]) van het type _lijst_ en _grafiek_ kunt u het aantal seconden weergeven dat uw controleregels up of down waren. Ga naar een tegel en klik op het menupictogram met drie stippen [SHORTCODE_9][SHORTCODE_10] om de tegelinstellingen te openen, inclusief de verschillende kengetallen die u kunt selecteren.
[SHORTCODE_6]

## Impact van resultaten van controleregelchecks

Hoe markeert Uptrends de periode tussen verschillende resultaten van controleregelchecks (OK, onbevestigde fout en bevestigde fout)? Wordt de tijd tussen een onbevestigde fout en een bevestigde fout beschouwd als up of down? 

De onderstaande afbeelding toont de mogelijke sequenties van controleresultaten en hoe de perioden worden beschouwd. Bij het continu monitoren van een dienst of server zullen er natuurlijk veel controleresultaten achter elkaar zijn. Alle resultaten kunnen echter worden onderverdeeld in de volgende situaties:

![illustratie sequenties controleresultaten]([LINK_URL_6])

Op een gedetailleerd niveau kunnen de controleresultaten op de volgende manieren veranderen:   

**Onbevestigde fout -> bevestigde fout**  
De tijd tussen de twee metingen wordt als **down** beschouwd.

**Bevestigde fout -> onbevestigde fout**  
De tijd tussen de twee metingen wordt als **down** beschouwd, omdat de controleregel nog steeds in foutconditie verkeert. Een controleregel verkeert in foutconditie tot er een OK-indicatie is gedetecteerd.

**Bevestigde fout -> OK**  
De tijd tussen de twee metingen wordt als **down** beschouwd. Een controleregel wordt alleen als up beschouwd vanaf het moment dat er een OK-indicatie is gedetecteerd.

**OK -> onbevestigde fout**   
De tijd tussen de twee metingen wordt als **up** beschouwd, omdat het nog niet zeker is dat er echt een fout is.. 

**Onbevestigde fout -> OK**  
De tijd tussen de twee metingen wordt als **up** beschouwd. 

## Welke fouten dragen bij aan downtime?

Houd er rekening mee dat **alle fouten worden meegerekend** bij het berekenen van downtime. 

Als u bijvoorbeeld performancelimieten definieert in de foutcondities van een controleregel en die limiet wordt bereikt, wordt er een fout voor die conditie gegenereerd. Hoewel uw website feitelijk niet down is (maar onder uw limieten presteert), zal deze een uptime van minder dan 100% aangeven omdat de performanceconditie een fout genereerde.

## Hoe beïnvloeden gepauzeerde controleregels de uptime?

Als u een controleregel pauzeert, wordt deze tijd geregistreerd als 'onbekend'. Houd er rekening mee dat bij het berekenen van het uptimepercentage ook het totale aantal onbekende seconden wordt opgenomen en gemarkeerd als uptime. De formule voor het uptimepercentage is **(uptime + onbekend) / (uptime + downtime + onbekend)**, waarbij uptime, downtime en onbekend in seconden worden gegeven.

Hier is bewust voor gekozen, omdat heel veel klanten hierom vroegen. Wilt u de onbekende tijd uitsluiten van de uptimeberekening, dan kunt u het totaal aantal seconden uptime en downtime ophalen om dit zelf te berekenen. Voor het uptimepercentage gebruikt u de formule **uptime / (uptime + downtime)**, waarbij uptime en downtime in seconden worden gegeven.

## Hoe beïnvloedt onderhoud de uptime?

Fouten die tijdens een [onderhoudsperiode]([LINK_URL_7]) optreden, worden uitgesloten van de uptimeberekeningen, mits het *Onderhoudstype* van de onderhoudsperiode is ingesteld op **Zet monitoring helemaal uit** versus alleen notificaties uitzetten.  
