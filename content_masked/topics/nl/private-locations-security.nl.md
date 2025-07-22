{
  "hero": {
    "title": "Persoonlijke locaties en beveiliging"
  },
  "title": "Persoonlijke locaties en beveiliging",
  "summary": "Waar moet rekening mee worden gehouden om de veilige werking van controlestations op persoonlijke locaties te garanderen?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/persoonlijke-locaties-beveiliging",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u zich afvraagt hoe veilig de installatie van controlestations op persoonlijke locaties is en wat u zelf moet doen om uw data te beschermen, lees dan verder. In dit artikel worden de belangrijkste beveiligingsmaatregelen uitgelegd die door Uptrends worden genomen of die uw verantwoordelijkheid zijn. 

## Containers 

De installatie van een controlestation voor een persoonlijke locatie is gebaseerd op Docker-containers. Er zijn enkele 'ingebouwde' beveiligingsfuncties en enkele maatregelen uitgevoerd door Uptrends:

- Uptrends gebruikt een eigen containerrepository op Microsoft Azure. Hierdoor kunt u werken met een kleine repository, die alleen de vertrouwde containers bevat die u zoekt. 
- Docker verzorgt de containerverificatie.
- Uptrends scant de inhoud van de containerimages met behulp van beveiligingsscansoftware voordat ze worden geüpload naar de containerrepository. Dit helpt ervoor te zorgen dat Uptrends bekende kwetsbaarheden opspoort voordat nieuwe versies van gecontaineriseerde software worden verzonden. Daarnaast raden wij aan dat u ook de containerpakketten (updates) scant nadat u ze hebt gedownload en voordat u ze installeert.
- Docker-containers zijn door hun ontwerp beperkt in de inkomende communicatie van de buitenwereld en de communicatie op de host waar ze zich bevinden. U hoeft geen inkomende firewallpoorten te openen. 
- Bij de standaardinstallatie op een persoonlijke locatie wordt een script geïnstalleerd dat de Docker-containers automatisch bijwerkt. Dit zorgt ervoor dat de persoonlijke locaties altijd draaien op basis van de nieuwste beveiligingsupdates. 

## Software (anders dan installatie van Docker-containers)

De werking van controlestations vereist de controlestationsoftware, maar er is ook wat ondersteunende software bij betrokken. Denk aan de volgende onderwerpen:

- [Updates]([LINK_URL_1]) van Windows, browsers, enz. zijn nodig om bugfixes te krijgen zodra ze beschikbaar zijn en op die manier mogelijke beveiligingsproblemen op te lossen.
- Uptrends is ISO 27001 gecertificeerd. Deze certificering behandelt informatiebeveiliging en ontwikkelingspraktijken zoals:
  - Wijzigingen in Uptrends' software worden door vakgenoten beoordeeld.
  - Er zijn tools en procedures ter verdediging tegen kwetsbaarheden in softwareafhankelijkheden.
  - Er is een formele beveiligingsfunctionaris en Uptrends heeft over procedures voor beveiligingsincidenten. 
  - Bekijk Uptrends' [ISO 27001 certificaat]([LINK_URL_2]).
- Voor een Windows-host is een antivirusscanner op de host voldoende. De meeste antivirusscanners kunnen de processen en het verkeer in de container scannen. Controleer dit echter wel voor de antivirusscanner die u gebruikt.

## Netwerkverkeer 

Bij de controleregelchecks is enig netwerkverkeer betrokken waarbij data en requests binnen en soms buiten uw netwerk reizen. Bekijk de volgende situaties:

- Beperk de netwerktoegang altijd tot het noodzakelijke minimum. 
- De persoonlijke locaties hebben geen inkomende verbindingen nodig, en we raden aan deze volledig uit te schakelen. Alle verbindingen naar buiten zijn uitgaand en worden altijd geïnitieerd door de host. 
- De instructies die een controlestation ontvangt van de Uptrends Cloud worden ondertekend met een geheime sleutel. Het controlestation valideert binnenkomende instructies met de bijbehorende public key (bekend bij het controlestation) en garandeert op die manier dat de instructie echt door Uptrends is verzonden.

## Gegevensprivacy/-bescherming

Bij monitoring gaat het om gegevens variërend van eenvoudige informatie of een controle "OK" was of een fout opleverde, tot meer diepgaande informatie zoals screenshots van uw website bij een bepaalde transactiestap. Mogelijk wilt u weten welke soort informatie naar de Uptrends-cloudomgeving wordt verzonden en welke informatie u kunt verhinderen uw site te verlaten.

- Statusdata van het controlestation worden naar de Uptrends-cloudapplicatie gestuurd. Dit is nodig om te bepalen of het controlestation functioneert en correct werkt. Aan de hand van de statusinformatie kan een verouderd of incompatibel controlestation worden opgemerkt. Een niet-werkend controlestation kan leiden tot verkeerde monitoringresultaten. 
- De statusdata zijn zichtbaar op het tabblad Controlestationstatus van de persoonlijke locaties.
- Afgezien van de informatie over de controlestationstatus wordt alleen de meetinformatie naar de Uptrends-cloud verzonden.
- Als u zich zorgen maakt over het versturen van meetinformatie buiten uw bedrijf, raadpleeg dan het knowledgebase-artikel [Gegevensbescherming]([LINK_URL_3]) om te weten te komen hoe u het verzamelen van bepaalde informatie kunt uitschakelen, bijvoorbeeld screenshots, IP-adressen, enz.

Een ander onderwerp waar goed over nagedacht moet worden als het gaat om gegevens en privacy zijn inloggegevens. Uptrends raadt u ten zeerste aan voorzichtig te zijn met welke inloggegevens u gebruikt als onderdeel van uw monitoring. Gebruik nooit een really powerful gebruiker in een systeem om basistaken uit te voeren. Beperk de gebruikersrechten die aan een gebruiker zijn toegewezen tot het minimum dat nodig is om zijn of haar taken uit te voeren. Alle gebruikersrechten die verder gaan, kunnen toegang geven tot assets of taken waartoe de gebruiker geen toegang zou moeten hebben. Zie [Inloggegevens]([LINK_URL_4]) voor meer informatie over dit onderwerp. 
