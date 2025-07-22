{
  "hero": {
    "title": "Controleregelgroepen"
  },
  "title": "Controleregelgroepen",
  "summary": "Als u uw controleregels in controleregelgroepen organiseert, is het configureren van rapportage en alerts eenvoudiger.",
  "url": "/support/kb/synthetic-monitoring/controleregelbeheer/controleregelgroepen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-groups"
}

Controleregelgroepen hebben alles te maken met organiseren en dingen eenvoudiger maken. Nadat u uw controleregelgroepen heeft ingesteld, kunt u hiermee gemakkelijker en sneller [sjablonen toepassen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="nl" >}}), controleregels toevoegen aan [alertdefinities]({{< ref path="support/kb/alerting/create-alert-definitions" lang="nl" >}}) en dashboards en rapporten configureren.

## Beslissen over controleregelgroepen

Hoewel uw groep *Alle controleregels* niet bewerkbaar is, is elke andere groep die u maakt wel bewerkbaar, en een controleregel kan tot meerdere controleregelgroepen behoren. U kunt uw controleregelgroepen op verschillende manieren instellen. Hier volgen een paar voorbeelden van veelvoorkomende manieren waarop andere gebruikers hun controleregelgroepen hebben ingesteld.

**Controleregeltype**: Het kan handig zijn controleregelgroepen in te stellen op basis van [controleregeltype]({{< ref path="support/kb/basics/monitor-types" lang="nl" >}}) zoals controleregels voor websiteperformance, voor mobiele performance, voor uptime, voor API, voor transacties en voor certificaten. Dit soort groeperen is vooral handig bij het instellen van rapporten.

**Locatiespecifiek**: Als u rapportages op basis van geografische locaties wilt ontvangen, is het handig om uw controleregelgroepen op regio of land in te stellen. Meestal zullen deze geografisch specifieke controleregels dezelfde controlestations delen, waardoor het eenvoudig is deze te beheren met controleregelsjablonen.

**Data Center**: Als u sites heeft die door verschillende datacenters worden ondersteund, wilt u misschien groepen instellen op basis van het datacenter. U kunt snel controleren op performance en uptime op basis van het datacenter. Groeperen op datacenter kan van pas komen bij het instellen van onderhoudsperiodes met behulp van controleregelsjablonen.

**Belang**: Misschien wilt u controleregels groeperen op basis van het belang van de controleregel. De beschikbaarheid van uw blog zal bijvoorbeeld niet dezelfde prioriteit hebben als uw inlogpagina; het instellen van controleregelgroepen op basis van het belang van de URL is dus een prima manier om controleregels te organiseren en prioriteiten aan uw rapporten te stellen.

**Domein**: U kunt verschillende domeinen of subdomeinen onderhouden. Organiseren op basis van domein maakt het eenvoudig om alerts dienovereenkomstig te escaleren.

**Paginadoel**: Er zijn ook verschillende gebruikers die hun controleregels groeperen op basis van het doel van de URL, zoals de inlogpagina’s, startpagina’s en ondersteuningspagina’s.

## Overzicht controleregelgroepen

De pagina **Controleregelgroepen** geeft u een overzicht van de controleregelgroepen in uw account. Open deze door naar {{< AppElement type="menuitem" >}} Accountinstellingen > Controleregelgroepen {{< /AppElement >}} te gaan.

![screenshot dashboard "Controleregelgroepen"](/img/content/scr-monitor-groups-overview.min.png)

U ziet alle controleregelgroepen waarvoor u ten minste het *Gebruikersrecht bekijken* heeft. Lees meer over deze en andere [types gebruikersrechten]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#permission-types" lang="nl" >}}) voor controleregels en controleregelgroepen.

De groep *Alle controleregels* is standaard aanwezig in elk Uptrends-account. Deze bevat alle controleregels in uw account en u kunt deze niet wijzigen of verwijderen. Mogelijk heeft u een groep nodig die lijkt op de groep * Alle controleregels* die (bijna) alle controleregels bevat, maar met de optie om gebruikersrechten te bewerken en er controleregels uit te verwijderen. Bekijk het instellen van een [standaard controleregelgroep]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#default-monitor-group" lang="nl" >}}) om dit te bereiken.

Het overzicht toont informatie over *Controleregels in gebruik* die verwijst naar het maximale aantal controleregels (per type) dat is ingesteld in uw controleregelgroepen. U kunt er ook voor kiezen om een onbeperkt aantal controleregels toe te staan en geen limieten per controleregeltype in te stellen.

**Voorbeelden**

- Als er geen limiet is ingesteld en er worden 4 basiscontroleregels gebruikt, ziet u ‘Basiscontroleregels: 4’. 
- Als de limiet is ingesteld op 10 basiscontroleregels en er 4 worden gebruikt, ziet u ‘Basiscontroleregels: 4/10’.

## Een nieuwe controleregelgroep creëren

Om een nieuwe controleregelgroep te creëren:

1. Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Controleregelgroepen {{< /AppElement >}} .
2. Klik rechtsboven op de knop {{< AppElement type="button" >}} Controleregelgroep toevoegen {{< /AppElement >}}.
   U kunt ook op het + teken klikken in het menu {{< AppElement type="menuitem" >}}  Accountinstellingen > Controleregelgroepen {{< /AppElement >}}. 
   
   De pagina *Nieuwe controleregelgroep* verschijnt.

   ![screenshot](/img/content/scr_monitor-group-settings.min.png)

3. Vul bij **Omschrijving** een beschrijvende naam in.
4. Beslis of u het aantal controleregels dat aan deze groep mag worden toegevoegd, wilt beperken. Kies *Een onbeperkt aantal controleregels toestaan* als u dit niet wilt beperken. Onthoud dat het totale aantal controleregels in alle groepen nooit hoger kan zijn dan het aantal controleregels in uw account.
5. Voeg controleregels toe die lid moeten zijn van deze groep: klik op de bestaande controleregelgroep in het gedeelte *Controleregels in deze groep* om deze uit te vouwen en selecteer vervolgens de controleregelnamen. Overigens kunt u ook vanaf de controleregel zelf een controleregel aan een controleregelgroep toevoegen. Open het tabblad {{< AppElement type="tab" >}} Lid van {{< /AppElement >}} om die wijzigingen aan te brengen.
6. Voeg op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} de operator(groepen) met hun bijbehorende toegangsrechten toe aan deze controleregelgroep. Het Knowledge Base-artikel [Gebruikersrechten voor controleregels]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}}) bevat meer informatie over de opties hier.
7. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} onder aan de pagina.


Controleregelgroepen spelen een belangrijke rol bij het instellen van een team en het geven van de benodigde toegangsrechten aan elk lid (operator). Het artikel [Een team instellen in uw account]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="nl" >}}) bevat gedetailleerde stappen voor deze taak.