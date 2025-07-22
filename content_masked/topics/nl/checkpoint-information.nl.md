{
  "hero": {
    "title": "Controlestation informatie"
  },
  "title": "Controlestation informatie",
  "summary": "Wat is een controlestation en hoe kies je de juiste uit de vele controlestations voor monitoring die Uptrends biedt?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/controlestation-informatie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends biedt een omvangrijk netwerk van meer dan {{% Features/Variable variable="CheckpointCount" %}} mondiale controlestations, die u kunt configureren voor het monitoren van uw websites, servers en webservices om de oorsprong van een probleem te bepalen.

## Wat is een Controlestation?

Een controlestation is een geografische locatie waar de uptime en prestaties van uw controleregels periodiek worden gecontroleerd. Elk controlestation heeft een of meer servers in datacenters om tests uit te voeren. Deze controlestations gebruiken voornamelijk de Domain Name System (DNS)-servers van lokale Internet Service Providers (ISP), indien beschikbaar, om feitelijke metingen en resultaten te garanderen.

## Lijst met IP-adressen van Uptrends Controlestations

Bekijk de volledige en bijgewerkte [lijst met wereldwijde monitoring-controlestations van Uptrends]([LINK_URL_1]), inclusief IPv4- en IPv6-IP-adressen.

Zie de links [IPv4-adressen]([LINK_URL_2]) en [IPv6-adressen]([LINK_URL_3]) om de lijst te downloaden. Als u de IP-adressen in JSON- of XML-formaat wilt downloaden, raadpleegt u het knowledgebase-artikel [Krijg controlestationdata in JSON- of XML-formaat]([LINK_URL_4]).

## Meerdere Controlestations

Met het grote aantal controlestations dat beschikbaar is in Uptrends, kunt u flexibel verschillende locaties kiezen om tests uit te voeren en het gedrag van uw controleregelresultaten te verifiëren.

Controlestations kunnen ook een uitstekende tool zijn voor:

- Het testen van de Content Delivery Network (CDN) met veel eindpunten.
- Het testen van het mondiale DNS-netwerk. Veel van Uptrends' controlestations gebruiken een lokale DNS, zodat u kunt testen of uw DNS-wijzigingen op de juiste manier over de hele wereld worden doorgegeven.
- Het testen of vertraging die optreedt door afstand of backbone providers binnen aanvaardbare parameters blijft.

## De juiste set controlestations kiezen

Het selecteren van meerdere controlestations is al inbegrepen in uw abonnement en brengt geen extra kosten met zich mee. Uptrends raadt aan om zoveel mogelijk controlestations te selecteren, omdat dit de prestaties van uw controleregel beter zal evalueren en alternatieve locaties biedt tijdens controlestationonderhoud en downtime.

Standaard selecteert Uptrends controlestationlocaties wereldwijd, waaronder Europa, Noord-Amerika, Afrika, Azië, Australië, Zuid-Amerika en het Midden-Oosten. Het is handig om een controlestationselectie te hebben die zorgvuldig is gericht op een specifieke regio.

Het is verplicht om ten minste drie controlestations te selecteren. Als een van deze controlestations om welke reden dan ook voor onderhoud is, kunnen ten minste twee controlestations controles uitvoeren en fouten vanaf een ander controlestation verifiëren.

In het tabblad [SHORTCODE_5]Controlestations[SHORTCODE_6] van een controleregel kunt u individuele controlestations activeren, maar ook complete landen en continenten. Wanneer u een land of continent selecteert, profiteert u er meteen van wanneer we aan die regio nieuwe controlestations toevoegen. Zodra ons netwerk groeit, groeit uw dekking ook automatisch! Zelfs wanneer u individuele controlestations wilt overslaan, kunt u nog steeds profiteren van deze automatische groeifunctie: in plaats van individuele controlestations in een bepaald land te selecteren en er eentje uit te sluiten, kunt u de functie [Controlestations uitsluiten]([LINK_URL_5])  gebruiken om precieze controle te behouden over uw sets van controlestations.

[SHORTCODE_1]
**Opmerking:** De opties die u heeft verschillen per accounttype. Gebruikers van de versies Starter, Premium of Professional kunnen alleen vaste sets van controlestations selecteren. Gebruikers van de versies Business of Enterprise kunnen elk beschikbaar individueel controlestation selecteren.
[SHORTCODE_2]

## Downtime controlestation

Vanwege lokale netwerkproblemen of onderhoud kunnen controlestationlocaties tijdelijk buiten gebruik zijn. In scenario's waarin al uw controlestationselecties niet beschikbaar zijn, zorgt Uptrends ervoor dat controles nog steeds worden uitgevoerd op een uitwijklocatie buiten uw geconfigureerde controlestationselectie. Als slechts enkele van de geselecteerde controlestations niet beschikbaar zijn, controleert Uptrends uw controleregels nog steeds vanaf uw andere geselecteerde controlestations.

De uitwijklocatie is standaard ingeschakeld in de [SHORTCODE_7] Accountinstellingen [SHORTCODE_8] > **Uitwijken naar controlestations**. Dit zorgt ervoor dat tests nog steeds op andere locaties worden uitgevoerd en niet worden gecompromitteerd. Zodra controlestations weer beschikbaar zijn, schakelt Uptrends automatisch terug naar de controlestationinstellingen van uw controleregel.

Er zijn bepaalde scenario's waarin uitwijklocaties mogelijk niet goed werken. Bijvoorbeeld als u een whitelisting-beleid gebruikt waarbij alleen specifieke [Uptrends IP-adressen]([LINK_URL_6]) op de whitelist staan. In dit soort gevallen kunt u het probleem als volgt oplossen::

- Verhoog het aantal geselecteerde controlestations om de kans op monitoring vanaf niet-beschikbare controlestationlocaties te verkleinen.

- Ga naar [SHORTCODE_9] Accountinstellingen [SHORTCODE_10] en schakel de optie **Uitwijken naar controlestations** uit. Als u **Uitwijken naar controlestations** uitschakelt, zijn er geen alternatieve locaties beschikbaar om uw controleregel te checken. Als uw controleregel een test start en downtime van een controlestation detecteert, slaat de controleregel de huidige check automatisch over. Vervolgens start de controleregel een andere check bij het volgende controleregel-[interval]([LINK_URL_7]). Houd er rekening mee dat het uitschakelen van deze optie kan leiden tot gaten in uw monitoringresultaten.

## Problemen met controlestations?

Ondervindt u problemen met een bepaald controlestation? [Neem dan contact met ons op]([LINK_URL_8])!

[SHORTCODE_3]
**Opmerking:** Sommige IP-tools om de geografische locatie te vinden geven de fysieke locatie van onze datacenters onjuist aan. [Lees meer]([LINK_URL_9]). 
[SHORTCODE_4]
