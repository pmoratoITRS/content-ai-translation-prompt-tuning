{
  "hero": {
    "title": "Ontbrekende gegevens SLA-overzicht"
  },
  "title": "Ontbrekende gegevens SLA-overzicht",
   "summary": "Het SLA-overzicht bevat geen data. Wat kan hiervan de reden zijn?",
  "url": "/support/kb/dashboards-en-rapportages/sla/ontbrekende-gegevens-sla-overzicht",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/sla/missing-sla-overview-data"
}

U heeft veel moeite gedaan om een SLA-controleregel (Service Level Agreement) in te stellen of u heeft gekozen om de standaard SLA-controleregel te gebruiken die gemaakt is toen u uw account opende. Maar als u het SLA-overzicht bekijkt, bestaat de data uit een heleboel streepjes (bjivoorbeeld '-') of nullen. Waarom? Omdat uw rapportopties hebben geresulteerd in ongeldige data. In plaats van onvolledige of ongeldige datasets te tonen, geeft Uptrends nullen en streepjes weer.

## De mogelijke scenario’s

We hebben twee mogelijke scenario’s gevonden voor het probleem van de ontbrekende data in het SLA-overzicht: u heeft tijd opgenomen van vóór de aanmaakdatum en -tijd van de SLA-definitie of controleregel, of u heeft **Controleregelgroepen** geselecteerd bij de optie **Regels tonen voor** in het tegelmenu.

### U heeft tijd opgenomen van vóór de aanmaakdatum en -tijd van de SLA-definitie of controleregel

Wanneer u een rapportageperiode selecteert, is het belangrijk op te letten of de SLA-definitie of -controleregel werd gemaakt na de startdatum en -tijd van de rapportageperiode. Zelfs als het gaat om slechts enkele seconden zullen uw resultaten voor de controleregel worden weergegeven met allemaal streepjes (nieuwere SLA-definitie) of met nullen (nieuwere controleregels). Zelfs als u uw SLA-definitie op 1 januari 2016 hebt gemaakt en het is nu 31 december 2016 ontvangt u geen data als u 'Dit jaar' selecteert voor uw rapportageperiode. U ontvangt geen data omdat er tijd is op 1 januari waarvan het systeem geen data heeft, dus geeft het rapport streepjes weer. Als u een geldig rapport wilt, kiest u eerst de optie {{< AppElement type="menuitem" >}}Aangepast{{< /AppElement >}} in het menu {{< AppElement type="menuitem" >}}Voorgedefinieerde periode{{< /AppElement >}} en dan een datum en uur nadat u de account of SLA-definitie hebt gecreëerd, bijvoorbeeld 2/1/2016 tot en met 31/12/2016.

### U heeft "Controleregelgroepen" geselecteerd bij de optie "Regels tonen voor" in het tegelmenu

Als u klikt op het menupictogram met drie stippen {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} om de tegelinstellingen te openen, ziet u veel opties voor de data die in deze tegel worden weergegeven. Als u **Controleregelgroepen** selecteert in het menu bij **Regels tonen voor**, zult u geen SLA-data ontvangen. De tegel zal de andere velden zoals Totale tijd, Controles, Bevestigde fouten, Uptime percentage en Downtime voor de controleregelgroepen weergeven, maar u krijgt geen waarden in de SLA-velden omdat SLA-data geen data zijn die we van meerdere controleregels kunnen samenvoegen. U kunt data weergeven van specifieke controleregels of controleregelgroepen door deze in het actiemenu of in de tegelinstellingen te selecteren, maar uw data zullen nog steeds in rijen van individuele controleregels in deze groepen worden weergegeven.
