{
  "hero": {
    "title": "Werken met meerdere SLA-definities"
  },
  "title": "Werken met meerdere SLA-definities",
  "summary": "U kunt meerdere SLA's monitoren met SLA-definities en aangepaste dashboards.",
  "url": "/support/kb/dashboards-en-rapportages/sla/werken-met-meerdere-sla-definities",
  "translationKey": "https://www.uptrends.com/support/kb/sla/working-with-multiple-SLA-definitions"
}

Voor de meeste gebruikers van Uptrends is één SLA-definitie genoeg, maar sommige bedrijven onderhouden of monitoren meerdere SLA’s met verschillende minimumpercentages, paginalaadtijden of operator responstijden. Om te leren hoe u extra SLA-definities instelt of de standaard SLA-definitie aanpast leest u het artikel [Een SLA instellen]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="nl" >}}). Als u uw SLA-definities heeft geconfigureerd en wilt leren hoe u meerdere SLA-definities gebruikt in uw Uptrends-account, dan bent u hier op de juiste plaats.

Uptrends berekent de SLA-nummers/naleving voor elke SLA-definitie voor elke controleregel in uw account. U hoeft bepaalde controleregels niet te koppelen aan bepaalde SLA-definities, want u kunt data bekijken van alle controleregels of controleregelgroepen, onafhankelijk van welke SLA-definitie is toegepast. U kunt in het standaard dashboard SLA-overzicht werken en schakelen tussen definities en controleregels of controleregelgroepen, en u kunt aangepaste SLA-overzichtdashboards creëren voor specifieke controleregels of controleregelgroepen en SLA-definities.

{{< callout >}}
**Opmerking:** Als u in uw SLA-overzicht streepjes en nullen ziet in plaats van data, dan hebben uw tegel-/dashboardinstellingen een conflict in de data veroorzaakt, wat resulteert in ongeldige data. Het knowledgebase-artikel [Ontbrekende gegevens SLA-overzicht]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="nl" >}}) bevat meer informatie over dit soort conflicten.
{{< /callout >}}

## Schakelen tussen SLA-definities in het dashboard SLA-overzicht

Nadat u aanvullende SLA-definities heeft gecreëerd, kunt u kiezen welke u in uw dashboard **SLA-overzicht** wilt weergeven. Om te schakelen tussen SLA-definities doet u het volgende:

1. Ga naar het menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics: SLA overzicht {{< /AppElement >}}.
2. Klik op het menupictogram met drie stippen van de tegel {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} om de tegelinstellingen te openen.
3. Kies een SLA-definitie in de lijst **SLA gebaseerd op**.
5. Klik op {{< AppElement type="button" >}}Instellen{{< /AppElement >}}.

Uw tegel ververst op basis van de gewijzigde SLA-definitie. Als de SLA-definitie nieuw is, ziet u waarschijnlijk streepjes (-) in plaats van data. Uptrends berekent en bewaart de SLA-data in realtime na het creëren van de definitie. Aangezien de SLA-definitie nieuw is, heeft het systeem nog geen complete dataset gebaseerd op deze nieuwe definitie en de datum- /tijdinstellingen, dus toont het rapport een streepje in plaats van percentages die gebaseerd zijn op een onvolledige dataset. Lees voor meer informatie het knowledgebase-artikel [Ontbrekende gegevens SLA-overzicht]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="nl" >}}).

## Aangepaste dashboards SLA-overzicht {id="custom-sla-overview-dashboard"}

Als u met meerdere SLA-definities werkt, kunt u in een aangepast dashboard afzonderlijke tegels creëren op basis van verschillende combinaties van SLA-definities en controleregels. Of u creëert verschillende aangepaste dashboards op basis van verschillende combinaties van SLA-definities en controleregels of controleregelgroepen.

Om een aangepast SLA-dashboard te maken moet u eerst een aangepast dashboard maken of een kopie opslaan van het dashboard **SLA-overzicht** om deze aan te passen.

### Creëer een aangepast dashboard SLA-overzicht

1. Ga naar het menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics: SLA overzicht {{< /AppElement >}}.
2. Klik op het menupictogram met drie stippen {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} om de instellingen te openen.
3. (Optioneel) Als u meerdere definities gebruikt, verandert u de SLA-definitie in **SLA gebaseerd op**.
4. Klik op het tabblad {{< AppElement type="tab" >}}Groepen en controleregels{{< /AppElement >}}.
5. Deselecteer **Gebruik de context van het dashboard** (als deze is geselecteerd) en selecteer de controleregel(s) of groep(en) om op te nemen in het aangepaste dashboard.
6. Klik op {{< AppElement type="button" >}}Instellen{{< /AppElement >}}.
7. Klik op het hamburgerpictogram {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
8. Selecteer {{< AppElement type="savebutton" >}}Opslaan als{{< /AppElement >}}.
9. Geef het nieuwe dashboard een beschrijvende naam.
10. Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

U heeft nu een aangepast dashboard dat toegankelijk is via het menu {{< AppElement type="menuitem" >}}Dashboards > Aangepaste dashboards{{< /AppElement >}}.  
  
### Creëer aanvullende SLA-tegels

In plaats van meerdere dashboards te maken, kunt u ook een multi-view dashboard creëren met tegels die gebaseerd zijn op verschillende combinaties van SLA-definities, controleregels of controleregelgroepen. Maak eerst een kopie van het standaard SLA-dashboard om dat aan te passen (zie de aanwijzingen hierboven vanaf stap 7). Om tegels toe te voegen doet u het volgende:

1. Open uw aangepaste dashboard door naar het menu {{< AppElement type="menuitem" >}}Dashboards > Aangepaste dashboards {{< /AppElement >}} te gaan en uw dashboard te selecteren.
2. Klik op het hamburgerpictogram {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
3. Selecteer *Tegel toevoegen*.
4. Selecteer **Controleregel lijst** in de Tegeltypes.
5. Klik op {{< AppElement type="button" >}}Volgende{{< /AppElement >}}.
6. Selecteer de controleregel(s) of controleregelgroep(en) die u voor deze tegel wilt gebruiken.
7. Klik op {{< AppElement type="button" >}}Voltooien{{< /AppElement >}} en de nieuwe tegel is gecreëerd.
8. Klik op het menupictogram met drie stippen van de tegel {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} om de tegelinstellingen te openen.
9. Selecteer een SLA-definitie in de lijst **SLA gebaseerd op**.
10. Klik op de vakjes bij de waarden die u wilt weergeven.
11. Wijzig desgewenst andere instellingen.
12. Klik op {{< AppElement type="button" >}}Instellen{{< /AppElement >}}.
13. Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} op het *Actiemenu*.

Voeg zoveel tegels toe als u nodig heeft.
