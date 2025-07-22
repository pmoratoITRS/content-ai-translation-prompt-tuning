{
  "hero": {
    "title": "Controlestationstatus"
  },
  "title": "Controlestationstatus",
  "summary": "Krijg een overzicht van hoe de controlestations van uw persoonlijke locatie het doen. Werken ze goed of hebben ze aandacht nodig?",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-locaties-gezondheid-controlestation",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-checkpoint-health"
}

Uw controlestations in [persoonlijke locaties]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="nl" >}}) kunnen hun monitoringwerk alleen doen als ze in goede staat verkeren. Het tabblad {{< AppElement type="tab" >}} Controlestationstatus {{< /AppElement >}} geeft u inzicht in de belangrijke feiten die van invloed zijn op de toestand van het controlestation. Dit omvat informatie over de geïnstalleerde software en enkele statistieken over de host. Hieronder vindt u meer details over de verstrekte informatie.

## Hoe kom ik bij de gezondheidsinformatie van het controlestation?

1. Ga naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Vouw in de lijst met persoonlijke locaties de locatie uit met het controlestation dat u wilt bekijken.
3. Klik op het controlestation en selecteer het tabblad {{< AppElement type="tab" >}} Controlestationstatus {{< /AppElement >}}.

![screenshot van het tabblad Controlestationstatus](/img/content/scr_private-location-checkpoint-health.min.png)

Houd er rekening mee dat u dit tabblad alleen ziet als het controlestation volledig is geïnstalleerd. Anders ziet u alleen het tabblad {{< AppElement type="tab" >}} Installatie {{< /AppElement >}} en moet u eerst uw controlestation installeren. Volg de instructies in [Een Docker controlestation installeren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}) om uw controlestation operationeel te maken.

## Uptrends-software

In dit gedeelte ziet u of de Uptrends-software correct is geïnstalleerd en of de verschillende services die nodig zijn om monitoring beschikbaar te maken, operationeel zijn. Elk onderdeel van het gedeelte **Uptrends-software** kan de status actief of inactief hebben. Deze moeten allemaal de status 'actief' tonen zodat het controlestation monitoringtaken kan uitvoeren.

De controlestationcontainer wordt gebruikt om alle niet-browsergebaseerde controles uit te voeren. 
De transactieprocessorcontainer wordt gebruikt om de echte browserchecks uit te voeren ([Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}), [transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="en" >}})). 
De relay container wordt gebruikt als communicatierelais tussen de andere containers en de Uptrends-clouddiensten.

Houd er rekening mee dat Uptrends container images met overeenkomende versienummers uitbrengt en alleen die combinatie van releases test. Het wordt niet aanbevolen om niet-overeenkomende versies samen te gebruiken. 

## Browsers

Op het controlestation moeten de browsers zijn geïnstalleerd die u wilt gebruiken voor het uitvoeren van echte browsercontroles ([Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}), [transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="en" >}})). 

In dit gedeelte kunt u de geïnstalleerde browsers met hun versies bekijken en deze vergelijken met de nieuwste versies. 
Uptrends levert container images met de meest recente browsers. Zorg ervoor dat u uw containers altijd updatet wanneer deze beschikbaar zijn. 

## Hostgegevens

De (virtuele) machine die uw controlestation host, moet in goede staat verkeren en over voldoende geheugen beschikken om monitoringtaken uit te voeren.

Controleer hier de informatie over uw systeem om mogelijke knelpunten te detecteren.

## Hostconfiguratie

In dit gedeelte vindt u de configuratiedetails van de host van de persoonlijke locatie, zoals DNS-servers, tijdzone en taalinstellingen.

## Instellingen voor gegevensbescherming

In dit gedeelte is te zien of gegevensbescherming is ingeschakeld. Een groen vinkje betekent dat er gegevens worden weergegeven, dus dat gegevensbescherming niet is ingeschakeld. Meer informatie over hoe u gegevensbescherming op uw persoonlijke controlestations implementeert vindt u in dit artikel over [Gegevensbescherming]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}).

