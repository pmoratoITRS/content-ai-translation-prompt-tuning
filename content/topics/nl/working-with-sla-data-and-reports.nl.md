{
  "hero": {
    "title": "Werken met SLA-data en -rapporten"
  },
  "title": "Werken met SLA-data en -rapporten",
  "summary": "Leer hoe u uw SLA-data leest en beheert. ",
  "url": "/support/kb/dashboards-en-rapportages/sla/werken-met-sla-data-en-rapporten",
  "translationKey": "https://www.uptrends.com/support/kb/sla/working-with-sla-data-and-reports"
}

Uptrends bevat een standaard dashboards **SLA overzicht** dat toegankelijk is via het menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics > SLA overzicht {{< /AppElement >}}. Als u [aangepaste dashboards SLA overzicht]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-multiple-SLA-definitions#custom-sla-overview-dashboard" lang="nl" >}}) heeft gemaakt, vindt u deze onder {{< AppElement type="menuitem" >}} Dashboards > Aangepaste dashboards {{< /AppElement >}}. 

Uw dashboard SLA-overzicht is waar u uw SLA-naleving controleert, PDF’s en Excelbestanden van uw SLA-data downloadt en periodieke SLA-rapporten plant.

## Het SLA-overzicht

Standaard toont het **SLA-overzicht** uw SLA-doelen en werkelijke waarden in kolomparen op basis van de periode die is gekozen in het actiemenu.

- **SLA doel uptime en SLA uptime** – Het uptime percentage van uw SLA-doel is uw gedefinieerde uptime-doel. De SLA uptime is het werkelijke uptime percentage, rekening houdend met eventuele uitgesloten dagen of tijden die u in uw SLA-definitie heeft ingesteld.
- **SLA doel totale tijd en SLA totale tijd** – De totale tijd van uw SLA-doel is de maximum paginalaadtijd in seconden die binnen de SLA-naleving blijft. De totale SLA-tijd zijn de werkelijke gemiddelde laadtijden voor de periode in seconden.
- **SLA doel operator responstijd en SLA operator responstijd** — De doelresponstijd van de SLA-operator is de maximale hoeveelheid toegestane tijd voor een operator om een probleem in Uptrends te bevestigen. Responstijd van de SLA-operator is de werkelijke hoeveelheid tijd die dit duurde.
- **Bevestigde fouten** – Het aantal bevestigde fouten voor de periode.
- **Downtime** – De som van alle downtime voor de periode weergegeven in seconden.
- **Downtime percentage** - Alle downtime voor de periode weergegeven als een percentage.

{{< callout >}}
**Opmerking:** Als u in uw **SLA-overzicht** streepjes en nullen ziet in plaats van data, dan hebben uw tegel-/dashboardinstellingen een conflict in de data veroorzaakt, wat resulteert in ongeldige data. [Lees meer]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="nl" >}}).
{{< /callout >}}

## SLA-data herberekenen

We vergeten allemaal weleens onderhoudschema’s en tijdelijke uitsluitingen in te stellen in onze SLA-definities. Hierdoor kunnen uw SLA-rapporten een rommeltje worden, maar u zit niet helemaal vast aan de slechte data.

### Dezelfde dag

Als u uw fout meteen opmerkt, kunt u [de fouten wissen]({{< ref path="support/kb/alerting/errors/clearing-errors#clear-individual-errors" lang="nl" >}}) in uw controleregel logs.

### Vorige dagen (maximaal 90)

Het is iets ingewikkelder om fouten te wissen voor SLA-rapporten van gisteren en elke dag ervoor. Uptrends bewaart SLA-data apart van uw reguliere monitoringdata. Aan het eind van elke dag worden uw SLA-data geëxtraheerd, dus door fouten te wissen in uw controleregel logs van gisteren zal er niets veranderen in uw SLA-rapporten. 

U kunt echter hulp krijgen van Uptrends om dit probleem op te lossen. Volg de stappen in [Grote hoeveelheden fouten tegelijk wissen]({{< ref path="support/kb/alerting/errors/clearing-errors#bulk-error-clearance" lang="nl" >}}) om een verzoekformulier in te vullen met de benodigde informatie. Op basis van die informatie wordt een ticket aangemaakt in Uptrends' ticketsysteem. Houd er rekening mee dat het enige tijd kan duren om de fouten te wissen en de SLA-data opnieuw te berekenen. U wordt op de hoogte gebracht door het ticketsysteem zodra het proces is voltooid.

## SLA-overzichtrapporten downloaden of delen

U kunt op meerdere manieren SLA-rapportdata downloaden als een bestand of uw SLA-overzichtsdata delen door e-mails te versturen.

### Downloaden

U kunt de inhoud van uw dashboard SLA-overzicht op elk gewenst moment downloaden in PDF- en Excel-formaat.

Vanuit uw standaard of aangepaste dashboard **SLA-overzicht**:

1.  Stel de datumparameters en controleregels die u wilt downloaden in in het actiemenu.
2.  Klik op het hamburgerpictogram {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
3.  Klik in het menu op een van de knoppen {{< AppElement type="menuitem" >}}PDF export{{< /AppElement >}} of {{< AppElement type="menuitem" >}}Excel export{{< /AppElement >}}.
4.  Wacht tot Uptrends het rapport heeft gegenereerd (dit kan even duren als u veel data heeft). U vindt het bestand in uw downloadsmap.

### Een eenmalige e-mail verzenden

U kunt data van uw SLA-dashboards via e-mail verzenden en kiezen tussen data in PDF-, Excel- of HTML-formaat. 

1. Open het SLA-dashboard waarvan u data wilt versturen.
2. Klik op het hamburgerpictogram {{< AppElement type="iconFeather" >}}{{< /AppElement >}} en klik op {{< AppElement type="menuitem" >}}Verzenden als e-mail{{< /AppElement >}}.
3. Vul de e-mailadressen van de ontvangers in, kies het type bestand en voeg desgewenst notities toe.
4. Klik op de knop {{< AppElement type="button" >}} Rapport versturen {{< /AppElement >}}.

### E-mails periodiek verzenden door rapporten te plannen {id="scheduling-reports"}

U kunt regelmatig geplande rapporten instellen die naar uzelf en andere operators in uw account worden gemaild met **Rapportdefinities**. Uw rapport wordt verstuurd naar uw lijst met ontvangers vanuit uw dashboard **SLA-overzicht** (standaard of aangepast):

1.  Klik op het hamburgerpictogram {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
2.  Klik op {{< AppElement type="menuitem" >}}Rapport inplannen{{< /AppElement >}} om de geplande-rapportdefinitie te openen.
3.  Vul de velden in op de tabbladen {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}} en {{< AppElement type="tab" >}}Ontvangers{{< /AppElement >}}.
4.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}
5.  Beheer uw geplande-rapportdefinities door naar het menu {{< AppElement type="menuitem" >}} Accountinstellingen > Geplande rapporten {{< /AppElement >}} te gaan.
