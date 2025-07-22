{
  "hero": {
    "title": "Overzicht machtigingen"
  },
  "title": "Overzicht machtigingen",
  "url": "/support/kb/account/gebruikersrechten/overzicht-machtigingen",
  "translationKey": "https://www.uptrends.com/support/kb/permissions/permissions-overview",
  "sectionlist": false
}

De Uptrends-app werkt met een gebruikersrechtensysteem om operators toegangsrechten te geven, zodat operators de items die relevant zijn voor hun rol kunnen bekijken, bewerken of maken.

In principe zijn er twee soorten gebruikersrechten: **algemene systeemrechten** worden toegewezen aan een operator(groep), terwijl **contextrechten** worden ingesteld op een item dat de operator(groep) toegang geeft tot dat specifieke item. Beide typen worden hieronder uitvoeriger beschreven.

 {{< callout >}} De algemene systeemrechten zijn beschikbaar voor alle accounts, terwijl contextrechten alleen beschikbaar zijn voor Enterprise-accounts. {{< /callout >}}


## Wie kan gebruikersrechten bewerken (toekennen/intrekken)?

Administrators (leden van de operatorgroep **Administrators**) kunnen altijd gebruikersrechten bewerken.

Wat betreft de contextrechten is de situatie iets anders, aangezien ook niet-administrators het recht kunnen hebben om gebruikersrechten te bewerken. In feite hangt dit af van welk niveau van contextrecht aan hen is verleend, in combinatie met een algemeen systeemrecht.
Bekijk de informatie over de individuele [contextrechten]({{< ref path="#context-permissions" lang="nl" >}}) om te zien hoe dit werkt.

## Algemene systeemrechten

De algemene systeemrechten worden uitgebreid uitgelegd in het Knowledge Base-artikel [Gebruikersrechten]({{< ref path="support/kb/account/users/operators/permissions" lang="nl" >}}).

Over het algemeen wordt aangeraden om de gebruikersrechten voor operatorgroepen in te stellen in plaats van individuele operators. Hierdoor is het makkelijker om overzicht te houden. In de meeste gevallen zult u te maken hebben met teams (operatorgroepen) waarbij elk lid dezelfde rechten moet hebben als alle andere leden van het team.

## Contextrechten {id="context-permissions"}

Met de volgende items in Uptrends kunt u gebruikersrechten per item instellen (zoals *bekijken*, *bewerken*, *gebruiken*, *maken*) door de operatorgroep met gebruikersrechten aan het item te koppelen. Raadpleeg de volgende Knowledge Base-artikelen waarin wordt beschreven hoe u gebruikersrechten instelt:

- [Alertdefinities]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="nl" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="nl" >}})
- [Integraties]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="nl" >}})
- [Controleregels]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="nl" >}})

## Handleiding

De handleiding bevat stapsgewijze instructies voor het instellen van gebruikersrechten voor een nieuw team in uw account.

- [Een team in uw account instellen]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="nl" >}})