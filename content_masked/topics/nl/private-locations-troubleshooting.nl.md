{
  "hero": {
    "title": "Persoonlijke locaties - problemen oplossen"
  },
  "title": "Persoonlijke locaties - problemen oplossen",
  "summary": "Richtlijnen en voorbeelden voor het oplossen van problemen met uw persoonlijke locaties.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/persoonlijke-locaties-problemen-oplossen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De installatie van een persoonlijke locatie is volledig geautomatiseerd waarna u beschikt over een actief containercontrolestation dat zichzelf up-to-date houdt en metingen kan uitvoeren voor controleregels. Deze handleiding biedt stappen om u te helpen [de installatie van uw persoonlijke locatie te verifiëren]([LINK_URL_1]), [een smoke test uit te voeren op uw set-up]([LINK_URL_2]) en [problemen op te lossen]([LINK_URL_3]) tijdens of na de installatie van een persoonlijke locatie. 

## Verifieer de installatie van de persoonlijke locatie
Als eerste stap controleert u of uw persoonlijke locatie correct is [geïnstalleerd en ingesteld]([LINK_URL_4]). Het geautomatiseerde installatiepakket is voorgeconfigureerd en bestaat uit drie stappen.

- Installatie van vereisten (inclusief opnieuw opstarten indien nodig).
- De Uptrends-containerimages ophalen uit Azure.
- Installatie van de taken automatisch uitvoeren en automatisch bijwerken.


### Installatie van vereisten
Er zijn drie vereisten voor het uitvoeren van de Uptrends-containerimages geïnstalleerd: de Windows-functie 'Containers', de Docker-engine en Docker Compose. Voor de installatie van de Windows-functie Containers moet mogelijk opnieuw worden opgestart, waarvoor een melding zal verschijnen. De installatie wordt na deze herstart automatisch voortgezet (met behulp van een Scheduled Task, taakplanner).

Als u wilt controleren of deze drie items correct zijn geïnstalleerd, zijn er drie opdrachten die u moet uitvoeren. 

Maak eerst een lijst van alle Windows-functies en controleer of deze lijst 'Containers' bevat:
1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het docker-compose.yml bestand zich bevindt en voer de volgende opdracht uit `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4][INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7][INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10][INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13][INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16][INLINE_CODE_17][INLINE_CODE_18][INLINE_CODE_19][INLINE_CODE_20][INLINE_CODE_21][INLINE_CODE_22][INLINE_CODE_23][INLINE_CODE_24][INLINE_CODE_25][INLINE_CODE_26]docker-compose up -d[INLINE_CODE_27]docker-compose down[INLINE_CODE_28]docker-compose restart[INLINE_CODE_29][INLINE_CODE_30][INLINE_CODE_31][INLINE_CODE_32][INLINE_CODE_33][INLINE_CODE_34][INLINE_CODE_35][INLINE_CODE_36][INLINE_CODE_37][INLINE_CODE_38][INLINE_CODE_39]Docker-compose logs -t -n 5000[INLINE_CODE_40][INLINE_CODE_41][INLINE_CODE_42][INLINE_CODE_43][INLINE_CODE_44][INLINE_CODE_45][INLINE_CODE_46][INLINE_CODE_47][INLINE_CODE_48][INLINE_CODE_49][INLINE_CODE_50][INLINE_CODE_51][INLINE_CODE_52][INLINE_CODE_53][INLINE_CODE_54][INLINE_CODE_55][INLINE_CODE_56][INLINE_CODE_57][INLINE_CODE_58][INLINE_CODE_59][INLINE_CODE_60][INLINE_CODE_61][INLINE_CODE_62][INLINE_CODE_63]`, als deze correct functioneert wanneer u het IP-adres van de publieke DNS niet gebruikt, maar problemen ondervindt als deze afwezig is, kan er een probleem zijn met het resolven van DNS. Houd er rekening mee dat het gebruik van 8.8.8.8 als DNS-server in production niet wenselijk is, omdat dit de interne applicaties niet kan resolven.

Geef specifieke DNS-server(s) op in het composebestand, zoals te zien is in de onderstaande code. Vergeet niet om dit voor beide containers in het yaml-bestand te doen.

[CODE_BLOCK_4]

Vul de IP-adressen in van de DNS-servers die u wilt gebruiken. U kunt deze testen tegen probemaster1.uptrends.com en de hostnaam met nslookup. Vergeet niet om dit vanuit een container te doen.

Mogelijk moet u DNS-requests toestaan die afkomstig zijn van de Docker-containers als uw DNS-servers gebruikmaken van een toelatingslijst. Als u containercontrolestations uitvoert op een cloudplatform zoals Google Cloud, AWS of Azure, kan aanvullende configuratie nodig zijn om connectiviteit vanuit de Docker-containers te garanderen. 

## Nog steeds problemen? 

Als u op enig moment tijdens het probleemoplossingsproces iets niet begrijpt of een vraag heeft, communiceer dan uw vragen of zorgen aan Uptrends door [een support ticket te openen]([LINK_URL_14]). We nemen snel contact met u op. 