{
  "hero": {
    "title": "Hoe werkt Gelijktijdige monitoring?"
  },
  "title": "Hoe werkt Gelijktijdige monitoring?",
  "summary": "Een overzicht van Gelijktijdige monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/gelijktijdige-monitoring/hoe-werkt-gelijktijdige-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Er zijn in Uptrends twee manieren om de uptime, performance en correct gedrag van uw websites, webdiensten en servers te monitoren: Standaard monitoring en Gelijktijdige monitoring.

## Standaard monitoring

Een controleregelcheck wordt vanaf één controlestation uitgevoerd. Als er een fout optreedt, wordt deze beschouwd als onbevestigde fout. Direct daarna wordt dezelfde controleregelcheck uitgevoerd vanaf een ander controlestation. Wordt dezelfde fout opnieuw ontvangen, dan is het resultaat een bevestigde fout. Alleen bevestigde fouten kunnen leiden tot alerts en berichten (sms, e-mail, Slack, andere systemen van derden).

## Gelijktijdige monitoring

Een aantal controleregelchecks wordt tegelijkertijd (gelijktijdig) uitgevoerd in plaats van na elkaar. U definieert hoeveel controles gelijktijdig worden uitgevoerd en vanaf welke controlestations.

Er zijn ook twee limieten die een percentage zijn van de controlestations die een fout retourneren: een limiet voor wanneer een fout als onbevestigde fout wordt beschouwd en een andere limiet voor wanneer een fout als bevestigde fout wordt beschouwd. Het is aan u om te beslissen welk percentage voldoende is om een fout te signaleren. Als het eerste niveau (bijvoorbeeld 30%) wordt bereikt, wordt de fout geclassificeerd als onbevestigde fout. Als het tweede niveau wordt bereikt (bijvoorbeeld 60%), ziet u in plaats daarvan een bevestigde fout.

Wanneer een aanzienlijk (door de gebruiker gedefinieerd) percentage controles een fout heeft geretourneerd, is het resultaat onmiddellijk een bevestigde fout. Er kan een alert worden gegenereerd en snel een bericht worden verstuurd.

## Scope

Gelijktijdige monitoring werkt binnen de volgende scope:

-   Het is beschikbaar voor alle controleregeltypes.
-   De controleregelchecks moeten met de gebruikelijke monitoringfrequenties worden uitgevoerd, namelijk 1 minuut voor basiscontroleregels en 5 tot 15 minuten voor browsercontroleregels.
-   Bij Gelijktijdige monitoring gelden speciale regels voor het selecteren van controlestations: kies uit alle controlestations (minstens 5) of kies uit controlestations die zijn gemarkeerd als *hoge beschikbaarheid* (minstens 3). Controlestations met *hoge beschikbaarheid* zijn over het algemeen die locaties waar meer dan één server beschikbaar is.
-   In alle gevallen is het maximale aantal geselecteerde controlestations 50.

## Monitoring output

Op basis van gelijktijdige controles berekent Uptrends één totale meting (met basisgegevens). De data kunnen op dezelfde manier worden gebruikt als andere controleregels, bijvoorbeeld in dashboards, alerts of SLA-berekeningen.

De individuele metingen zijn op de volgende plaatsen beschikbaar:

- De *Controleregel-log* 
- Als u de totale meting opent vanuit de *Controleregel-log*, krijgt u een pop-up met details die naar de deelmetingen verwijst.
- Per individuele meting leggen we de gebruikelijke debug-informatie vast (screenshots, waterval, traceroute, etc.).

## Voor- en nadelen

De voordelen zijn dat Gelijktijdige monitoring een fout sneller detecteert en een hogere betrouwbaarheid heeft. Let wel, dit laatste hangt af van het aantal gebruikte controlestations.

Een nadeel kan zijn dat we geen transactiestappen samenvoegen of een gemiddelde van de waterval berekenen voor rapportagedoeleinden (voor transacties, full page checks, etc.).

Gelijktijdige monitoring heeft een hogere prijs. U krijgt er echter snellere detectie en hogere betrouwbaarheid voor terug. Zie onderstaande voorbeelden om een indruk te krijgen van de prijsstelling.

## Abonnementen

De functie zal worden opgenomen in de volgende abonnementen: Business en Enterprise.  
Om Gelijktijdige monitoring te kunnen gebruiken moet u de controlestations die in de controles worden opgenomen afzonderlijk kiezen. Dit is alleen mogelijk in de abonnementen Business en Enterprise. Andere abonnementen hebben deze mogelijkheid niet en zijn daarom niet geschikt voor Gelijktijdige monitoring.

De berekening van credits die worden gebruikt voor gelijktijdige controleregels wordt uitgelegd in het KB-artikel [Prijzen voor Gelijktijdige monitoring]([LINK_URL_1]).