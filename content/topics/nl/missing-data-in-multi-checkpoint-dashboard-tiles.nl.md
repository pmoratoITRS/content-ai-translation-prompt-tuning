{
  "hero": {
    "title": "Ontbrekende data in tegels met meerdere controlestations"
  },
  "title": "Ontbrekende data in tegels met meerdere controlestations",
  "summary": "Leer waarom u soms geen data of onvolledige data hebt in uw Multicontrolestation dashboardtegels",
  "url": "/support/kb/dashboards-en-rapportages/dashboards/ontbrekende-data-in-tegels-met-meerdere-controlestations",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/missing-data-in-multi-checkpoint-dashboard-tiles"
}

De lijsten en grafieken van onze Multicontrolestation data tonen geselecteerde meetresultaten op basis van de controlestations die de tests hebben uitgevoerd. Deze datategels zijn geweldig voor het identificeren van latency en andere regionale problemen. Af en toe krijgen we een vraag over ontbrekende of onvolledige data in deze tegels. Er zijn verschillende oorzaken voor deze problemen.

## Conflict tussen geselecteerde controlestations in dashboard en controleregel

Toen u uw controleregel configureerde, selecteerde u welke controlestations u voor de controleregel wilde gebruiken; daarnaast hebt u, boven aan elk dashboard, de mogelijkheid om te selecteren welke controlestations worden gebruikt voor het berekenen van data voor het dashboard. Als de controlestations die zijn geselecteerd voor de controleregel of controleregels niet zijn opgenomen in de selectie van controlestations in het dashboard, krijgt u of geen data of onvolledige datasets. Pas de controlestations in het dashboard aan om de controleregel(s) die geselecteerd zijn voor de tegel op te nemen. Is dit niet het geval, dan hebt u misschien te veel controlestations geselecteerd voor de tegel (lees verder).

{{< callout >}}
**Opmerking**: U zult ook geen data zien in de Multicontrolestation lijst van controlestations die worden gebruikt door de controleregel die u niet in het dashboard hebt opgenomen.
{{< /callout >}}

## Er zijn te veel dashboardcontrolestations geselecteerd bij gebruik van de multicontrolestation grafiek.

Standaard geeft het dashboard data weer van alle controlestations, maar de tegel Multicontrolestation grafiek kan slechts tien controlestations tegelijk weergeven. Als u het dashboard op de standaardinstelling laat staan of een groot aantal controlestations hebt geselecteerd en uw controleregel er slechts enkele gebruikt, ziet u mogelijk geen data of alleen data van sommige controlestations. De tegel neemt de eerste tien controlestations op basis van de controlestations die voor het dashboard zijn geselecteerd en toont de gegevens van die controlestations. Als er geen data zijn voor de eerste 10 controlestations, verschijnt het bericht "Er zijn geen gegevens beschikbaar." Als een of meer voor uw controleregel geselecteerde controlestations toevallig in de eerste 10 voor het dashboard geselecteerde controlestations vallen, ziet u de data van die controlestations samen met de andere controlestations in de eerste tien – zelfs als er geen data voor zijn. Om alle gegevens in deze tegel te bekijken moet u de selectie van de controlestations voor het dashboard aanpassen om de controlestations op te nemen die door de controleregel worden gebruikt (maximaal tien controlestations).
