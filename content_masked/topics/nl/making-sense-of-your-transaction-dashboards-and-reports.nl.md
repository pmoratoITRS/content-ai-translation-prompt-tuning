{
  "hero": {
    "title": "Uw transactiedata begrijpen"
  },
  "title": "Uw transactiedata begrijpen",
  "summary": "Zodra uw transactiecontroleregel in production gaat, begint u rapporten met controledetails te genereren en vullen uw dashboards zich met data. In deze oefening leert u hoe u dit allemaal kunt begrijpen. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/tutorial-record-user-journey-in-shop/uw-transactie-dashboards-en-rapporten-begrijpen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De data die tijdens monitoring worden verzameld, kunnen worden bekeken in het [dashboard]([LINK_URL_1]) *Transactieoverzicht*. Zoals de naam al zegt is dit een overzicht en kan het informatie bevatten over meerdere transactiecontroleregels. Als u de details van een specifieke transactiecontroleregel wilt weten, opent u de [Details van de controle]([LINK_URL_2]) van die controleregel. 

## Dashboard Transactieoverzicht

Uw dashboard *Transactieoverzicht* bevat tegels met de huidige status, een log met recente controles, informatie over uptime en performance en een grafiek van de uptime en performance voor uw transacties. 
Er zijn in principe twee [types dashboardtegels]([LINK_URL_3]): grafiek en lijst. In een lijst worden de monitoringdata als een tabel weergegeven, terwijl een grafiek een grafische weergave van de gegevens toont.

Houd er rekening mee dat het dashboard *Transactieoverzicht* geen informatie bevat over uw transactiecontroleregels in [development mode]([LINK_URL_4]).

Om toegang te krijgen tot het dashboard *Transactieoverzicht* gaat u naar het menu [SHORTCODE_3] Transacties > Transactieoverzicht [SHORTCODE_4].

![screenshot dashboard transactieoverzicht]([LINK_URL_5])

### Account status

In de tegel *Account status* ziet u de huidige status van uw transactiecontroleregels in zowel staging mode als production mode. Vanuit deze tabel kunt u uw controleregels snel schakelen tussen actief en uitgeschakeld, en kunt u alerting in- en uitschakelen voor uw transacties in production mode.

![screenshot tegel account status]([LINK_URL_6])

### Laatste controles

De tabel *Laatste controles* is een chronologische log van recente controles. U kunt de tegel *Laatste controles* gebruiken om op een specifieke controle te klikken (klik op de datum) en het rapport [*Details van de controle*]([LINK_URL_7]) bekijken. Het camerapictogram in de kolom **Status** geeft aan dat het rapport *Details van de controle* een of meer screenshots bevat.

![screenshot tegel laatste controles]([LINK_URL_8])

### Totale tijd, uptime en bevestigde fouten

Deze lijst toont de gemiddelde totale tijd, het uptime-percentage en het aantal bevestigde fouten voor de rapportageperiode. U kunt natuurlijk ook andere metingen opnemen door het menu met drie stippen [SHORTCODE_5][SHORTCODE_6] te openen om toegang te krijgen tot de tegelinstellingen. 

![screenshot transactietegel uptime en fouten]([LINK_URL_9])

[SHORTCODE_1]**Opmerking:** Transacties in staging mode worden niet gevolgd voor uptime en rapporteren altijd 100% uptime. [SHORTCODE_2]

### Uptime en bevestigde fouten

De tegel *Uptime & bevestigde fouten* geeft u een grafische weergave van de gemiddelde uptime en fouten die tijdens de rapportageperiode zijn opgetreden voor al uw transactiecontroleregels in production mode. 

![screenshot transactietegel uptime en bevestigde fouten]([LINK_URL_10])

### Ingezoomd transactierapport [ANCHOR_1]

Het *Transactieoverzicht* bevat standaard data van alle transactiecontroleregels of de transactiecontroleregels die u voor dit dashboard heeft gekozen. Als u de details van één controleregel wilt bekijken, doet u het volgende:

Op de tegels van het dashboard worden op verschillende plaatsen de controleregelnamen weergegeven met een stippellijn eronder. Hover over de naam van de controleregel die u verder wilt inspecteren. Er verschijnt een pop-upvenster voor snelle toegang:

![screenshot controleregel snelle toegang]([LINK_URL_11])

Klik op de link **Dashboard** in dit pop-upvenster om een ander dashboard te openen dat specifiek is voor de controleregel. Dit dashboard bevat veel informatie die u alleen per controleregel kunt krijgen.

![screenshot dashboard één transactie controleregel]([LINK_URL_12])
### Timinglijsten en -grafieken voor transactiestappen

De hoeveelheid tijd die elke actie duurt, is net zo belangrijk als de initiële laadtijd van een pagina wanneer een gebruiker een site bezoekt. Lange wachttijden tussen gebruikersinteracties tasten het vertrouwen van de gebruiker in uw product en merk aan. De lijsten en grafieken van *Transactiestaptijden* zijn ontworpen om u te helpen potentiële problemen te identificeren en trends te ontdekken.

De dashboardtegel met de *Timing transactiestappen*-grafiek toont de duur van elke stap in de transactie zoals gemeten voor elke controleregelcheck in de loop van de tijd.

![screenshot tegel timing transactiestap]([LINK_URL_13])

Een andere manier om te kijken hoe de transactie presteert, is door de gemiddelde tijd te controleren die nodig is voor elke stap. Afhankelijk van wat er van een stap mag worden verwacht, kunnen lange gemiddelde staptijden een aanwijzing zijn dat iets niet optimaal werkt. 

![screenshot gemiddelde transactiestaptijd]([LINK_URL_14])

In de lijst *Timing transactiestappen* ziet u de staptijden voor elke test in cijfers. 

![screenshot lijst timing transactiestappen]([LINK_URL_15])

### Fouttypelijst en -grafiek

Uw lijst en grafiek *Fouttype* geven u een overzicht van de bevestigde fouten die uw controleregel tijdens de rapportageperiode heeft aangetroffen.

![screenshot tegels fouttypes ]([LINK_URL_16])

## Details van de controle [ANCHOR_2]

U kunt de resultaten van een individuele controle bekijken door te klikken op de betreffende vermelding in de tegel *Laatste controles* op uw dashboard *Transactieoverzicht* of op de tegel *Controleregel log* op het [eigen dashboard van de controleregel]([LINK_URL_17]). U ziet dat alle informatie aanwezig is: datum/tijd, resultaat, controlestation, laadtijd, browsertype en -versie, besturingssysteem en de resultaten per stap.

![screenshot transaction check details]([LINK_URL_18])

Gewoonlijk verwijst de **Laadtijd** (zie rapport hierboven) naar de tijd om één pagina op te vragen en te laden in de browser. Voor transacties is laadtijd echter de totale hoeveelheid tijd die de transactie nodig had om te voltooien vanaf de eerste request tot de laatste actie (de som van alle staptijden).

### Resultaten per stap

Uw **Resultaten per stap** moeten u bekend voorkomen. De sectie is een weerspiegeling van uw script, opgesplitst per stap met het resultaat van elke ondernomen actie. U krijgt de duur per stap en de uitkomst van elke actie. Als een actie mislukt, wordt de test afgebroken en wordt de stap rood gemarkeerd in het rapport. Als u een Business- of Enterprise-account heeft, heeft u vanuit het rapport *Details van de controle* toegang tot uw watervalgrafieken en screenshots, door bijvoorbeeld te klikken op het watervalpictogram [SHORTCODE_7] [SHORTCODE_8] (naast de stapnaam) wordt de waterval geopend die bij de stap hoort.

![]([LINK_URL_19])
