{
  "hero": {
    "title": "Overzicht Alerting"
  },
  "title": "Overzicht Alerting",
  "summary": "Hoe alerting werkt. De controleregelcheck genereert een fout, de fout leidt tot een alert die een bericht activeert via een alertdefinitie.",
  "url": "[URL_BASE_TOPICS]alerting/overzicht-alerting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In een real-world setting wordt verondersteld dat websites, servers en andere systemen 24 uur per dag draaien en ononderbroken beschikbaarheid van de service bieden. In scenario's als deze is alerting een krachtig hulpmiddel om u onmiddellijk op de hoogte te houden wanneer zich een probleem of iets ongewoons in uw systeem voordoet. Alerting zorgt ervoor dat uw systeem altijd operationeel is en helpt de downtime van het systeem te minimaliseren.

Een van de belangrijkste functies van Uptrends monitoringdienst is **Alerting**. Wanneer er fouten in uw controleregels worden gedetecteerd, wordt u via alertberichten onmiddellijk op de hoogte gesteld. De onderstaande illustratie toont de samenvatting van de Uptrends alertworkflow:

![Illustratie alertworkflow]([LINK_URL_1])

Eenvoudig gezegd: er wordt een alert gecreëerd wanneer deze vier definities bestaan: *Controleregelcheck, Foutconditie, Alertdefinitie en Integratie*. Nadat u uw controleregel en de bijbehorende instellingen heeft gecreëerd en gedefinieerd, voert uw controleregel verschillende checks uit zoals gedefinieerd in de controleregelinstellingen. Zodra een controleregelcheck resulteert in een [bevestigde fout]([LINK_URL_2]) wordt er een alert gegenereerd in de Uptrends webapplicatie. Deze alert triggert vervolgens het verzenden van een bericht naar een operator of een applicatie van een derde partij.


In dit artikel bespreken we stap voor stap hoe een controleregelcheck een bericht wordt.

## Controleregelchecks

Het begint allemaal met de controleregelchecks die met het door u gedefinieerde interval worden uitgevoerd. De controleregelchecks bevatten enkele standaardcontroles die afhankelijk zijn van het controleregeltype, zoals beschikbaarheid. Daarnaast kunt u uw eigen foutcondities definiëren, zoals een laadtijdlimiet of de pagina-inhoudmatch.

![Instellingen controleregelchecks]([LINK_URL_3])

In het knowledgebase-artikel [Foutcondities]([LINK_URL_4]) wordt uitgebreider uitgelegd hoe u foutcondities configureert.

Een fout wordt gesignaleerd zodra de controleregelcheck een probleem vindt als gevolg van een mislukte standaardcontrole of als aan een foutvoorwaarde is voldaan.

## Fouten

Alle fouten worden weergegeven in de sectie **Fouten overzicht**. U kunt filteren welke fouttypes u wilt zien (*OK, onbevestigd, bevestigd*) en instellen welke tijdsperioden u wilt bekijken. U kunt het [knowledgebase-artikel Dashboards]([LINK_URL_5]) raadplegen voor meer informatie over het filteren en aanpassen van dashboardinstellingen.

Het onderstaande voorbeeld Fouten overzicht toont onbevestigde (geel gemarkeerd) en bevestigde (rood gemarkeerd) fouten:

![Dashboard Fouten overzicht]([LINK_URL_6])

Zoals in de illustratie wordt getoond, wordt de eerste keer dat een fout optreedt een onbevestigde fout genoemd. Dit kan slechts een tijdelijke situatie zijn of een probleem met het controlestation. Daarom wordt een tweede controleregelcheck uitgevoerd vanaf een ander controlestation. Als er fouten worden gerapporteerd, is het resultaat een bevestigde fout, die een alert genereert.

Meer informatie over dit principe vindt u in het artikel [Onbevestigde en bevestigde fouten]([LINK_URL_7]).

### Reeksen van fouten

Er zijn verschillende scenario’s voor een reeks van fouten, deze worden weergegeven in de afbeelding hieronder:

-   Een onbevestigde fout gevolgd door een OK-resultaat. Dit leidt niet tot een alert.
-   Een onbevestigde fout gevolgd door een bevestigde fout en vervolgens een OK-resultaat. Dit resulteert in een alert als uw alertdefinitie is ingesteld op "Genereer een alert als er 1 of meer fouten opgetreden zijn".
-   Een aantal (n) onbevestigde/bevestigde fouten treden achter elkaar op. Dit resulteert in een alert als uw alertdefinitie is ingesteld op "Genereer een alert als er n of meer fouten opgetreden zijn". Als alternatief kunt u een tijdslimiet instellen voor fouten. Als de reeks van fouten die tijdslimiet bereikt, de fouten treden bijvoorbeeld langer dan 5 minuten op, wordt er een alert gecreëerd.

![]([LINK_URL_8])

## Alerts

De alertdefinitie regelt het genereren van alerts voor verschillende escalatieniveaus. De escalatieniveaus worden gebruikt om alerts in fasen te creëren en om de geselecteerde operators op de juiste manier op de hoogte te stellen, rekening houdend met de urgentie van het probleem en de toenemende urgentie, als het probleem blijft bestaan.

Voor elk niveau moet u instellen of er een alert wordt gecreëerd, welke operator(groepen) worden gewaarschuwd, wanneer een tijdslimiet wordt bereikt (fouten zijn langer dan x minuten opgetreden) of dat er een alert wordt gecreëerd nadat een aantal fouten is opgetreden (n of meer fouten zijn opgetreden). Alle fouten moeten bevestigde fouten zijn. Met onbevestigde fouten wordt bij deze condities geen rekening gehouden.

Naast de oorspronkelijke alert kunt u een of meer herinneringsalerts genereren. U moet het maximale aantal herinneringen instellen en het interval waarmee ze moeten worden gecreëerd. Deze optie is beschikbaar voor elk afzonderlijk escalatieniveau.

De knowledgebase-artikelen [Alertdefinities creëren]([LINK_URL_9]) en [Alert escalatieniveaus]([LINK_URL_10]) bevatten meer informatie over alertdefinities.

Merk op dat voor de controleregel de optie *Alerts genereren* moet zijn ingeschakeld om überhaupt alerts te genereren.

Wanneer de fout is opgelost (wat betekent dat dezelfde controle OK heeft geretourneerd in plaats van een fout), wordt er een herstelalert (OK-alert) gecreëerd.

Alle alerts worden weergegeven in de **Alerthistorie**. Foutalerts zijn rood gemarkeerd en OK-alerts zijn groen gemarkeerd. Zolang de fout niet is opgelost en er geen herstelalert wordt gegenereerd, blijft de alert een actieve alert. De actieve alerts worden vermeld in het dashboard **Huidige alertstatus**.

![]([LINK_URL_11])

Zoekt u een specifieke **Alertdefinitie** die u heeft gemaakt? U kunt Uptrends' [Zoeken]([LINK_URL_12]) gebruiken om die snel te vinden.

## Berichten

Met het dashboard **Alerthistorie** kunt u uw alerts van tijd tot tijd monitoren en ze op één plek bekijken. Het is echter ook handig om realtimeberichten over uw alertsituatie te ontvangen zonder naar de webapplicatie zelf te gaan. Uptrends biedt [Integraties]([LINK_URL_13]), waarmee u een volledig scala aan opties heeft voor het versturen van alertberichten naar uzelf, naar mensen of naar systemen van derden en meteen op de hoogte wordt gebracht.

Om een bericht te sturen wanneer er een alert is gegenereerd moet u eerst uw [Alertdefinitie]([LINK_URL_14]) instellen en vervolgens kiest u het type [integratie]([LINK_URL_15]) van uw voorkeur per escalatieniveau. Als u klaar bent, kunt u eenvoudig updates ontvangen op basis van uw favoriete integratie.

### Berichten testen

Aangezien u zo snel mogelijk alertberichten wilt ontvangen, zorgt u er eerst voor dat het verzenden van alertberichten ook echt werkt. Bekijk dit knowledgebase-artikel om te weten hoe u [alertberichten test]([LINK_URL_16]) voor verschillende integraties.

Ga naar de sectie [Problemen oplossen]([LINK_URL_17]) voor meer informatie!