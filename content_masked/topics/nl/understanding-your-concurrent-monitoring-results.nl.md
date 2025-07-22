{
  "hero": {
    "title": "De resultaten van uw gelijktijdige monitoring begrijpen"
  },
  "title": "De resultaten van uw gelijktijdige monitoring begrijpen",
  "summary": "Waar u de resultaten van gelijktijdige monitoring kunt vinden en hoe u deze interpreteert.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/gelijktijdige-monitoring/resultaten-gelijktijdige-monitoring-begrijpen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bij gelijktijdige monitoring zijn de controleresultaten anders opgebouwd dan bij standaard controleregels. Er zijn verschillende aspecten aan de resultaten van gelijktijdige controles die ze onderscheiden van de resultaten van standaard controleregels. Het resultaat van een gelijktijdige controleregel bestaat uit verschillende afzonderlijke controles, elk met hun eigen statistieken en resultaten. In dit artikel bespreken we hoe u de controledetails interpreteert om uw gelijktijdige controleregels optimaal te benutten. Als u aan de slag wilt met gelijktijdige monitoring, hebben we  [hier een handleiding voor het configureren ervan.]([LINK_URL_1])

## Resultaten van gelijktijdige controleregels identificeren

In de Controleregel log kunt u de resultaten van gelijktijdige controleregelchecks herkennen aan het ![]([LINK_URL_2]) pictogram. Deze resultaten vermelden geen controlestation in de kolom **Controlestation**, in plaats daarvan staat er *Meerdere locaties*. Daarnaast heeft elke gelijktijdige controleregel zijn eigen speciale dashboard dat relevante informatie weergeeft, ongeacht het controleregeltype. Om het dashboard Gelijktijdige controleregel te openen hovert u over het infolabel van het resultaat van een controleregelcheck en klikt u op *Dashboard*.

![]([LINK_URL_3])

## De resultaten van gelijktijdige monitoring interpreteren

Om de algehele controleregelcheck te openen klikt u gewoon op zijn vermelding in de controleregel log.

![screenshot monitor details concurrent monitoring]([LINK_URL_4])

Zoals u ziet, geeft het venster Details van de controle de controlestations weer die de controle hebben uitgevoerd. De weergegeven **Laadtijd**-meting is het gemiddelde van de laadtijden van de afzonderlijke controles, van elk afzonderlijk controlestation. Het weergegeven **Resultaat** is het algehele controleresultaat – als de algehele controle voldoet aan de voorwaarden van de controleregelinstellingen, rapporteren we een resultaatcode *0 – OK*. Anders rapporteren we een fout. Fouten werken iets anders voor gelijktijdige monitoring – [we hebben hier een volledige uitleg geschreven]([LINK_URL_5]).

Voor meer details over de afzonderlijke metingen die we hebben uitgevoerd om tot dit algehele resultaat te komen, kunt u het gedetailleerde overzicht van de afzonderlijke metingen vinden door op de controlestationnamen te klikken. Als we bijvoorbeeld in het vorige screenshot op *Birmingham - 2* klikken, kunnen we de details van de controle bekijken die zijn uitgevoerd vanaf het controlestation Birmingham-2.

![screenshot concurrent monitoring individual checkpoint details]([LINK_URL_6])

Dit overzicht bevat informatie zoals de gedetailleerde [uitsplitsing van de totale tijd]([LINK_URL_7]) voor de controle die vanaf dat specifieke controlestation is uitgevoerd. Zoals u ziet, bevat het ook een koppeling die u terugbrengt naar de algehele controle (*Alle controles bekijken)*).

## Afzonderlijke controles weergeven in de controleregel log

Standaard worden in de controleregel alleen de algehele controles weergegeven. De details van de afzonderlijke metingen vindt u door de eerder beschreven pop-upvensters van algehele controle te doorzoeken. U kunt uw controleregel log echter zo instellen dat zowel de algehele controles als alle afzonderlijke controles worden weergegeven. Om dit in te stellen stelt u het dashboardfilter rechtsboven in op *Deelmetingen tonen*.![]([LINK_URL_8])

U kunt ook op het tandwielpictogram rechtsboven in de controleregel log klikken (beweeg de muisaanwijzer boven de tegel om dit pictogram te laten verschijnen) en de optie **Deelmetingen tonen** aanvinken. Sla de configuratie op door rechtsonder op de knop [SHORTCODE_1]INstellen[SHORTCODE_2] te klikken.

![]([LINK_URL_9])

Zoals u ziet, bevat de controleregel log nu zowel de algehele metingen (aangegeven door het ![]([LINK_URL_10]) pictogram), die *Meerdere locaties* vermeldt, en alle afzonderlijke controles met hun respectieve controlestations. Dezelfde informatie wordt weergegeven in de beschikbare tegels met foutuitsplitsing.
