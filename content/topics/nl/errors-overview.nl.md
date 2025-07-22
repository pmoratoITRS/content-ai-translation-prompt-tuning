{
  "hero": {
    "title": "Overzicht van fouten"
  },
  "title": "Overzicht van fouten",
  "summary": "Wanneer een controleregelcheck een probleem tegenkomt (zoals gedefinieerd in foutcondities), wordt er een fout gesignaleerd.",
  "url": "/support/kb/alerting/fouten/overzicht-van-fouten",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/errors-overview",
  "sectionlist": false,
  "tableofcontents": false
}

Wanneer er iets mis is met uw website of services, resulteert een controleregelcheck in een fout. U moet de details definiëren van wat 'er is iets mis' betekent door [foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}) in te stellen voor uw controleregels.

Houd er rekening mee dat een fout niet hetzelfde is als een alert. Bekijk dit [Overzicht alerting]({{< ref path="support/kb/alerting/alerting-overview" lang="nl" >}}) om de verschillen beter te begrijpen en hoe deze zich tot elkaar verhouden.

Fouten worden altijd dubbel gecontroleerd om verkeerd-positieven te voorkomen. Lees meer hierover in het knowledgebase-artikel [Onbevestigde en bevestigde fouten]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}}).

Zodra er een fout is opgetreden, verschijnt deze op het dashboard *Foutenoverzicht*. Navigeer naar {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Fouten overzicht {{< /AppElement >}} om dit dashboard te openen. Er zal meer informatie staan over een fout in de [details van de controle]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="nl" >}}) gerelateerd aan de controleregelcheck die de fout heeft veroorzaakt.

Afhankelijk van de controleregel en de foutsituatie zal er een [fout snapshot]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="nl" >}}) zijn die u kan helpen bij het oplossen van de situatie.

Er zijn veel verschillende soorten fouten. Als u informatie over de fout nodig heeft, kunt u deze opzoeken op de pagina [fouttypes]({{< ref path="support/kb/alerting/errors/error-types" lang="nl" >}}) door te zoeken naar de foutcode of andere kenmerken.

Als er fouten zijn waarvan u denkt dat ze niet correct zijn of uit de lijst met fouten moeten worden verwijderd, heeft u de mogelijkheid om [fouten te wissen]({{< ref path="support/kb/alerting/errors/clearing-errors" lang="nl" >}}).
