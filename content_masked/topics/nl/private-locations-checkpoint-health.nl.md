{
  "hero": {
    "title": "Controlestationstatus"
  },
  "title": "Controlestationstatus",
  "summary": "Krijg een overzicht van hoe de controlestations van uw persoonlijke locatie het doen. Werken ze goed of hebben ze aandacht nodig?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-locaties-gezondheid-controlestation",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uw controlestations in [persoonlijke locaties]([LINK_URL_1]) kunnen hun monitoringwerk alleen doen als ze in goede staat verkeren. Het tabblad [SHORTCODE_1] Controlestationstatus [SHORTCODE_2] geeft u inzicht in de belangrijke feiten die van invloed zijn op de toestand van het controlestation. Dit omvat informatie over de geïnstalleerde software en enkele statistieken over de host. Hieronder vindt u meer details over de verstrekte informatie.

## Hoe kom ik bij de gezondheidsinformatie van het controlestation?

1. Ga naar [SHORTCODE_3] Persoonlijke locaties [SHORTCODE_4].
2. Vouw in de lijst met persoonlijke locaties de locatie uit met het controlestation dat u wilt bekijken.
3. Klik op het controlestation en selecteer het tabblad [SHORTCODE_5] Controlestationstatus [SHORTCODE_6].

![screenshot van het tabblad Controlestationstatus]([LINK_URL_2])

Houd er rekening mee dat u dit tabblad alleen ziet als het controlestation volledig is geïnstalleerd. Anders ziet u alleen het tabblad [SHORTCODE_7] Installatie [SHORTCODE_8] en moet u eerst uw controlestation installeren. Volg de instructies in [Een Docker controlestation installeren]([LINK_URL_3]) om uw controlestation operationeel te maken.

## Uptrends-software

In dit gedeelte ziet u of de Uptrends-software correct is geïnstalleerd en of de verschillende services die nodig zijn om monitoring beschikbaar te maken, operationeel zijn. Elk onderdeel van het gedeelte **Uptrends-software** kan de status actief of inactief hebben. Deze moeten allemaal de status 'actief' tonen zodat het controlestation monitoringtaken kan uitvoeren.

De controlestationcontainer wordt gebruikt om alle niet-browsergebaseerde controles uit te voeren. 
De transactieprocessorcontainer wordt gebruikt om de echte browserchecks uit te voeren ([Full Page Checks]([LINK_URL_4]), [transactiecontroleregels]([LINK_URL_5])). 
De relay container wordt gebruikt als communicatierelais tussen de andere containers en de Uptrends-clouddiensten.

Houd er rekening mee dat Uptrends container images met overeenkomende versienummers uitbrengt en alleen die combinatie van releases test. Het wordt niet aanbevolen om niet-overeenkomende versies samen te gebruiken. 

## Browsers

Op het controlestation moeten de browsers zijn geïnstalleerd die u wilt gebruiken voor het uitvoeren van echte browsercontroles ([Full Page Checks]([LINK_URL_6]), [transactiecontroleregels]([LINK_URL_7])). 

In dit gedeelte kunt u de geïnstalleerde browsers met hun versies bekijken en deze vergelijken met de nieuwste versies. 
Uptrends levert container images met de meest recente browsers. Zorg ervoor dat u uw containers altijd updatet wanneer deze beschikbaar zijn. 

## Hostgegevens

De (virtuele) machine die uw controlestation host, moet in goede staat verkeren en over voldoende geheugen beschikken om monitoringtaken uit te voeren.

Controleer hier de informatie over uw systeem om mogelijke knelpunten te detecteren.

## Hostconfiguratie

In dit gedeelte vindt u de configuratiedetails van de host van de persoonlijke locatie, zoals DNS-servers, tijdzone en taalinstellingen.

## Instellingen voor gegevensbescherming

In dit gedeelte is te zien of gegevensbescherming is ingeschakeld. Een groen vinkje betekent dat er gegevens worden weergegeven, dus dat gegevensbescherming niet is ingeschakeld. Meer informatie over hoe u gegevensbescherming op uw persoonlijke controlestations implementeert vindt u in dit artikel over [Gegevensbescherming]([LINK_URL_8]).

