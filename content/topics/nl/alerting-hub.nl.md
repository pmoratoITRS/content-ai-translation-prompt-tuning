{
  "hero": {
    "title": "Alerting hub"
  },
  "title": "Alerting hub",
  "summary": "De plek om te beginnen bij het verkennen van Alerting",
  "url": "/support/kb/alerting/alerting-hub",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alerting-hub",
  "tableofcontents": false
}

Alerting is een complex onderwerp en vereist dat veel instellingen soepel samenspelen om het verwachte resultaat te krijgen. Het hangt af van de juiste configuratie van foutcondities, alertdefinities, escalatieniveaus en integraties. Er zijn veel parameters om af te stemmen en de hub is er om u daarbij te helpen.

De hub biedt informatie over de theorie van alerting door u te wijzen op de belangrijkste concepten en andere relevante onderwerpen in de knowledge base. Vanuit de hub kunt u direct naar relevante instellingen in de Uptrends-app springen. U vindt er ook informatie over de feitelijke situatie: zijn er actieve alerts en zijn de dingen waarop u vertrouwt, zoals alertdefinities en integraties, actief? Tot slot kunt u zien of u nog berichtcredits heeft.

Open de Alerting Hub door in het hoofdmenu {{< AppElement type="menuitem" >}}Alerting > Alerting verkennen{{< /AppElement >}} te kiezen.

![](/img/content/scr-alerting-hub.min.png)

Het bovenste deel van de hub en de zijbalk bevatten koppelingen naar de belangrijkste concepten en waar en hoe u alerting kunt instellen. Er zijn een aantal koppelingen die verwijzen naar artikelen in de knowledge base. Andere koppelingen brengen u rechtstreeks naar het gedeelte van de app waar u definities kunt instellen die nodig zijn voor het functioneren van alerts.

In het onderste deel van de hub vindt u informatie over de feitelijke situatie van uw alerting, zoals hoeveel controleregels op dit moment alerts hebben. Dit overzicht is gepersonaliseerd en daarbij geldt het volgende:

- Er worden alleen controleregels of alertdefinities weergegeven waarvoor u het [gebruikersrecht om controleregel te bekijken]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}}) of [gebruikersrecht om alertdefinitie te wijzigen]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="nl" >}}) heeft. 
- Alleen de integraties waarvoor u het gebruikersrecht **Integratie bewerken** heeft, worden weergegeven. Andere integraties worden hier buiten beschouwing gelaten.

Vanaf hier kunt u direct springen naar:

-   De controleregels die boven aan de lijst met alerts staan.
-   Lopende alerts, waarmee u naar het dashboard *Alertstatus* gaat.
-   Volledige alertgeschiedenis, die u naar het dashboard *Alerthistorie* brengt.

Er zijn ook enkele statistieken over uw alertinginstellingen die u snel een overzicht van de situatie geven en u helpen bij het oplossen van problemen. De statistieken tonen u het aantal: 

- Actieve integraties 
- [Controleregels dat is gedekt door een alertdefinitie]({{< ref path="support/kb/alerting/monitor-alerting-coverage" lang="nl" >}}) (alleen controleregels in [production mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode#monitormodeproduction" lang="nl" >}}))
- Actieve alertdefinities
- Beschikbare berichtcredits

Wanneer u de statistieken bij **Alertdefinities actief** bekijkt, moet u er rekening mee houden dat alleen definities die actief zijn en ten minste één actief escalatieniveau hebben, meetellen bij dit aantal. Het is prima om een alertdefinitie te hebben die actief is zonder actieve escalatieniveaus. Er worden alerts gegenereerd (indien van toepassing) die kunnen worden bekeken in de Uptrends-app, bijvoorbeeld in de Alert-log, maar er worden geen alertberichten naar operators gestuurd en deze definitie wordt niet meegeteld bij het aantal **actieve alertdefinities**.

Er moet ook ten minste één integratie zijn in een escalatieniveau van de alertdefinitie waarbij het gebruikersrecht **Integratie gebruiken** (of hoger) is ingesteld voor de huidige operator. Anders wordt de alertdefinitie niet weergegeven als actief.
