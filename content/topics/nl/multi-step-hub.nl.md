{
  "hero": {
    "title": "Multi-step API-controleregel hub"
  },
  "title": "Multi-step API-controleregel hub",
  "summary": "Uw startpunt bij het verkennen van Multi-step API monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-hub",
  "tableofcontents": false
}

De **Multi-step API (MSA) hub** biedt een algemeen overzicht van MSA's en uw MSA-monitoringset-up. Om deze pagina te openen, gaat u naar het menu {{< AppElement type="menuitem" >}} API > {{< /AppElement >}} [API-monitoring verkennen](https://app.uptrends.com/Hubs/Api). In het zijbalkmenu vindt u links naar relevante knowledgebase-artikelen:

![MSA Hub](/img/content/scr-msa-hub.min.png)

De volgende kaarten tonen uw API-controleregelset-up:

- De kaart **API-controleregels** toont het aantal van uw controleregelset-ups. Als u op de knop {{< AppElement type="buttonPrimary" >}} Alle API-controleregels bekijken {{< /AppElement >}} klikt, wordt het overzicht van API-controleregels of het menu {{< AppElement type="menuitem" >}}  API-controleregelset-up {{< /AppElement >}} geopend.

- De kaart **Status API-controleregel** toont het aantal controleregels met [bevestigde fouten]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}}) en actieve alerts. Door op de knop {{< AppElement type="buttonPrimary" >}} Controleregelstatus bekijken {{< /AppElement >}} te klikken wordt de pagina **Controleregelstatus** geopend. Door op de knop {{< AppElement type="buttonPrimary" >}} Lopende alerts bekijken {{< /AppElement >}} te klikken wordt de pagina **Huidige alertstatus** geopend.

- De kaart Actieve controleregels toont de API-controleregels in [Staging- en Productionmodus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}}).

- De kaart API-credits toont het saldo van uw API-credits. Om meer credits te kopen, raadpleegt u [Extra controleregels en credits toevoegen]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="nl" >}}).

De hub biedt ook een manier om automatisch uw bestaande controleregels te scannen en te identificeren welke controleregels kunnen worden omgezet naar [API-controleregels]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}). Als de hub HTTP- of HTTPS-controleregels detecteert die een API-eindpunt lijken te controleren, biedt de hub de mogelijkheid om automatisch een nieuwe API-controleregel voor u te creëren.

Deze functionaliteit werkt elke [Uptime-controleregel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}}) direct bij naar een volledig geconfigureerde API-controleregel zonder de oorspronkelijke controleregel te verwijderen of te wijzigen. U kunt de actie op elk gewenst moment ongedaan maken. Bovendien hoeft u niet alles handmatig opnieuw te maken; Uptrends verzorgt de volledige configuratie en kopieert dezelfde instellingen van uw bestaande controleregels.

Als u op de knop **Details bekijken** klikt, wordt er een pop-up geopend waarmee u uw bestaande controleregel kunt omzetten naar een API-controleregel. Na de conversie verschijnt er een andere pop-up waarin u de configuratie kunt bekijken en de nieuw gecreëerde controleregel kunt inschakelen voor gebruik.