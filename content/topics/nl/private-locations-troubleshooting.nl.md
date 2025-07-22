{
  "hero": {
    "title": "Persoonlijke locaties - problemen oplossen"
  },
  "title": "Persoonlijke locaties - problemen oplossen",
  "summary": "Richtlijnen en voorbeelden voor het oplossen van problemen met uw persoonlijke locaties.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/persoonlijke-locaties-problemen-oplossen",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting"
}

De installatie van een persoonlijke locatie is volledig geautomatiseerd waarna u beschikt over een actief containercontrolestation dat zichzelf up-to-date houdt en metingen kan uitvoeren voor controleregels. Deze handleiding biedt stappen om u te helpen [de installatie van uw persoonlijke locatie te verifiëren](#verify-private-location-installation), [een smoke test uit te voeren op uw set-up](#smoke-test-your-setup) en [problemen op te lossen](#how-to-troubleshoot) tijdens of na de installatie van een persoonlijke locatie. 

## Verifieer de installatie van de persoonlijke locatie
Als eerste stap controleert u of uw persoonlijke locatie correct is [geïnstalleerd en ingesteld]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="nl" >}}). Het geautomatiseerde installatiepakket is voorgeconfigureerd en bestaat uit drie stappen.

- Installatie van vereisten (inclusief opnieuw opstarten indien nodig).
- De Uptrends-containerimages ophalen uit Azure.
- Installatie van de taken automatisch uitvoeren en automatisch bijwerken.


### Installatie van vereisten
Er zijn drie vereisten voor het uitvoeren van de Uptrends-containerimages geïnstalleerd: de Windows-functie 'Containers', de Docker-engine en Docker Compose. Voor de installatie van de Windows-functie Containers moet mogelijk opnieuw worden opgestart, waarvoor een melding zal verschijnen. De installatie wordt na deze herstart automatisch voortgezet (met behulp van een Scheduled Task, taakplanner).

Als u wilt controleren of deze drie items correct zijn geïnstalleerd, zijn er drie opdrachten die u moet uitvoeren. 

Maak eerst een lijst van alle Windows-functies en controleer of deze lijst 'Containers' bevat:
1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het docker-compose.yml bestand zich bevindt en voer de volgende opdracht uit ``Get-WindowsFeature | Where-Object {$_. installstate -eq "installed"}``. 
3. Controleer of deze lijst 'Containers' bevat.

Controleer ten tweede de uitvoer van de versie van Docker:
1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het docker-compose.yml bestand zich bevindt en voer de volgende opdracht uit ``Docker -v``. 
3. Het resultaat zou iets als 'Docker version 23.0.3, build 3e7cbfd' moeten zijn.

Controleer ten derde de uitvoer van de versie van Docker Compose:
1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het bestand docker-compose.yml zich bevindt en voer de volgende opdracht uit ``Docker-compose -v``. 
3. Het resultaat zou iets als 'Docker Compose version v2.17.2' moeten zijn.

Als u denkt dat er iets niet in orde is, kunt u het installatiescript, install-checkpoint.ps1, raadplegen en handmatig de afzonderlijke onderdelen voor de bovenstaande componenten uitvoeren en de uitvoer bekijken.
 
### Container images
Als aan alle drie de bovenstaande vereisten is voldaan, begint het [installatiescript]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="nl" >}}) met het ophalen van de Uptrends-containerimages uit Azure. Deze images zijn groot omdat ze allemaal een gecomprimeerde installatie van Windows Server bevatten. Het downloaden kan minstens enkele minuten duren (20 minuten is gebruikelijk), afhankelijk van de netwerkdoorvoer. Delen van de images worden hergebruikt bij het updaten, zodat volgende downloads sneller zullen zijn. Zodra het downloaden is voltooid, kunt u dit verifiëren door het [uitvoeren](#managing-running-containers) van: ``docker images`` en u zult drie vermeldingen zien.

Het ophalen van de images is afhankelijk van de interne werking van Docker en is een robuust proces dat het wegvallen van verbindingen aankan. Als het downloaden helemaal mislukt, is de meest waarschijnlijke oorzaak een (lokale) firewall die verhindert dat Docker toegang krijgt tot de Azure Container Repository via azurecr.io, gehost door Microsoft.

Om te authenticeren bij het ophalen van de images, registreert het installatiescript inloggegevens via Docker-login. In geval van problemen met authenticatie kunt u naar de installatiemap navigeren (de map die install-checkpoint.ps1 bevat) en deze opdrachten in powershell uitvoeren om:

Bestaande inloggegevens te wissen, gebruik de volgende opdracht:
``Docker logout``

registry-login.ps1 opnieuw uit te voeren en de uitvoer van deze opdracht te bekijken, gebruik de volgende opdracht:
``.\registry-login.ps1``

### Automatisch uitvoeren en automatische updates
Om de containercontrolestations draaiende te houden, wordt er een geplande taak gecreëerd om het script start-containers.ps1 uit te voeren na het opstarten van de server. Om de Docker-images van het containercontrolestation [up-to-date]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-update-containers" lang="nl" >}}) te houden wordt er een tweede Scheduled Task gecreëerd om regelmatig te controleren op image-updates. Controleer de uitvoer van de powershell-opdracht ``Get-ScheduledTask`` om te verifiëren of deze taken bestaan. Ze heten 'Start Checkpoint Containers' en 'Update Checkpoint Images'. 

U kunt de Windows Scheduled Task-gebruikersinterface gebruiken om de taken verder te onderzoeken, de historie en fouten uit te voeren of de taak handmatig te activeren om problemen op te lossen. Nogmaals, gebruik in geval van problemen het installatiescript (install-checkpoint.ps1) om dit deel van de installatie indien nodig handmatig opnieuw uit te voeren.

### Configuratie
Alle serverspecifieke configuraties bevinden zich in het configuratiebestand Docker-compose.yml. Dit bestand bevat alle drie de containerimages en hun individuele instellingen. Dit configuratiebestand wordt vooraf gevuld met alle benodigde instellingen wanneer het wordt gedownload. Het belangrijkste is de combinatie ``ServerId/Password`` die moet worden geconfigureerd voor alle drie de containerimages die in het bestand worden vermeld (wat betekent dat dezelfde combinatie van inloggegevens driemaal in het yml-bestand zal voorkomen met dezelfde waarden). 

{{< callout >}} De *ServerId* en *Password* zijn uniek voor het containercontrolestation. Meerdere containercontrolestationservers mogen nooit dezelfde *ServerId* hebben.
{{< /callout >}} 

Het Docker Compose-bestand kan worden gebruikt voor het configureren van controlestationspecifieke [gegevensbescherming]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}), beleid en [omgevingsspecifieke DNS-regels](#dns-issues).
 
### Huidige status
Na installatie worden de containers voor alle drie de images gestart en deze containers zullen naar verwachting altijd draaien. U kunt hun status verifiëren met de opdracht ``docker ps`` en in de meest rechtse kolom is te zien of de containers inderdaad actief zijn. Gebruik in geval van problemen deze opdrachten om logbestanden te verkrijgen voor verdere diagnose:

- Krijg de huidige status voor alle containers
``Docker ps``

- Krijg de logs voor de controlestation Agent-container en schrijf naar bestand
``Docker logs Checkpoint | Out-File Docker_CS.txt``

- Krijg de logs voor de transactieprocessorcontainer en schrijf naar bestand
``Docker logs TransactionProcessor | Out-File Docker_TP.txt``

- U kunt ook gecombineerde logs voor alle containers krijgen
``Docker-compose logs -t -n 5000 | Out-File Docker.txt``

## Een smoke test uitvoeren op uw set-up

Zodra de containercontrolestations zijn geïnstalleerd, zijn deze direct klaar om metingen uit te voeren. Uptrends' interne processen zullen automatisch de onderhoudsstatus van een containercontrolestation wijzigen op basis van de status ervan. Een gezond controlestation wordt omgeschakeld naar actief, een ongezond controlestation naar onderhoud. 

Controlestations updaten hun status elke minuut. U kunt controlestations ook activeren of [deactiveren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use#disable-a-private-checkpoint" lang="nl" >}}) (bijvoorbeeld bij het uitvoeren van onderhoud of het testen van de set-up ervan) vanuit de gebruikersinterface van persoonlijke locaties in de Uptrends-webapplicatie. De standaardstatus is 'ingeschakeld'. 

Om een smoke test op een containercontrolestation uit te voeren is het gebruik van de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}} het handigst. Idealiter zou u dit doen voor elk controleregeltype dat u erop wilt uitvoeren. 

U kunt de [Controlestationstatus]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="nl" >}}) van de persoonlijke locaties gebruiken om de status van ongezonde controlestations te diagnosticeren. 

Houd er rekening mee dat alle metingen 'binnen' een container worden uitgevoerd. U zult niet zien dat er een browser wordt gestart op de hostcomputer wanneer u de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}} gebruikt voor een FPC of transactie.

Houd er ook rekening mee dat wanneer u een controlestation toevoegt aan een bestaande persoonlijke locatie die deel uitmaakt van de controlestationselectie van actieve controleregels, het nieuwe controlestation metingen zal gaan uitvoeren nadat de installatie is voltooid. Als dat ongewenst is (bijvoorbeeld als u eerst wilt testen), moet u het controlestation in het gedeelte persoonlijke locaties van Uptrends uitschakelen.

## Hoe u problemen oplost

### Stop, start of herstart een set containers
Herstart containers die zijn gekoppeld aan het bestand Docker-compose.yaml in de huidige directory. Dit is vaak de map C:\uptrends\ :

1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het bestand docker-compose.yml zich bevindt en voer een of meerdere van de volgende opdrachten uit.
- Om te starten typt u `docker-compose up -d` op de opdrachtregel. 
- Om te stoppen typt u `docker-compose down` op de opdrachtregel. 
- Om te herstarten typt u `docker-compose restart` op de opdrachtregel.


{{< callout >}} **Tip** Gebruik de Docker-help. Over elk van de opdrachten kunt u meer te weten komen door de opdracht *docker - -help* te gebruiken. Met deze opdracht worden alle opdrachten weergegeven met algemene hulp voor alle verschillende opdrachten. U kunt ook om hulp vragen over een bepaalde opdracht door *docker image - -help* te typen.{{< /callout >}}


### Actieve containers beheren
Om een lijst met actieve containers te krijgen, voert u de opdracht ``docker ps`` uit. Hier wordt een containerId vermeld die kan worden gebruikt in andere opdrachten met betrekking tot deze container. 

Om een lijst met alle lokale images te krijgen, voert u de opdracht ``docker images`` uit. Let op het meervoud images, alle opdrachten die op een image zijn gericht, worden uitgevoerd met image (enkelvoud).

Images kunnen behoorlijk groot worden, om wat ruimte vrij te maken kunt u ``docker image prune`` gebruiken om images te verwijderen die niet langer door actieve containers worden gebruikt. Of gebruik ``docker image rm <containerid>`` om een specifieke container te verwijderen.

### Ongebruikte Docker-objecten verwijderen

Het [Uptrends-installatiescript voor Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="nl" >}}) bevat geen set-up voor het automatisch opschonen van ongebruikte Docker-objecten. Om ongebruikte Docker-objecten te verwijderen raadpleegt u de (Engelstalige) documentatie [Prune unused Docker objects](https://docs.docker.com/engine/manage-resources/pruning). Als u andere platforms gebruikt, zoals Kubernetes, raadpleeg dan de officiële documentatie daarvan.

### Cmd/shell-toegang verkrijgen binnen een container
Voer deze opdracht uit om een powershell- of cmd-proces binnen de container te starten. Dit kan worden gebruikt om snel het bestandssysteem binnen de containers te lezen. Gebruik de opdracht ```Docker exec -i checkpoint powershell``` of ```Docker exec -i checkpoint cmd```.

Weet u niet zeker of u zich binnen of buiten een container bevindt? Typ ``winver`` in de Windows-opdrachtprompt. Als u zich in een container bevindt, ziet het er zo uit: 

```winver : The term 'winver' is not recognized``` 

Als u zich op de host bevindt, wordt de pop-up **Over Windows** weergegeven.
Als u de powershell- of cmd-sessie in de container wilt afsluiten en terug wilt gaan naar de host, gebruikt u Ctrl+C.

### Loguitvoer lezen

1. Open een PowerShell-console in beheerdersmodus. 
2. Ga naar de map waar het bestand docker-compose.yml zich bevindt en voer een van de volgende opdrachten uit.
- Loguitvoer, typ `Docker-compose logs -t -n 5000` op de opdrachtregel. 
- Of als u dit naar een bestand containerlogs.log wilt uitvoeren, typt u ``Docker-compose logs -t -n 5000 > containerlogs.log``.

### Netwerk
Bij het opstarten zal Docker op de host een virtueel netwerk creëren waaraan de containers zijn gekoppeld en een IP-adres krijgen. 
U kunt bestaande netwerken in powershell bekijken met ``docker network ls`` en een specifiek netwerk met ``docker network inspect <<network name>>``. Om het netwerk te vinden waarin een container zich bevindt, gebruikt u ``docker inspect <<container name>>`` (en ``docker ps`` om containernamen te vinden).

Alle drie de Uptrends Docker-containers (Checkpoint, CheckpointRelay, TransactionProcessor) moeten verbinding kunnen maken met Uptrends via probemaster1.uptrends.com en probemaster2.uptrends.com. Zowel de Checkpoint- als de CheckpointRelay-containers moeten verbinding kunnen maken met de te testen applicaties van de klant.

### DNS-problemen

Een veel voorkomende oorzaak van verbindingsproblemen is het resolven van DNS. Voor het oplossen van problemen kunt u deze stappen volgen:

1. Op de host zou ``nslookup probemaster1.uptrends.com`` 95.211.70.204 moeten retourneren. Als dit niet het geval is, kunnen de containers geen verbinding maken met Uptrends.

2. Gegeven dat de containers actief zijn (controleer dit met ``docker ps``), voer dan in een powershell-sessie een container in: ``docker exec -i Checkpoint powershell.exe``.

3. Eenmaal in de container zou ``nslookup probemaster1.uptrends.com`` opnieuw 95.211.70.204 moeten retourneren. Als dat lukt, moet de container het Uptrends-cloudplatform kunnen bereiken.

4. Probeer hetzelfde voor een hostnaam van een interne applicatie, zoals ``nslookup <<name application>>`` en verifieer het geretourneerde IP-adres. Als er een time-out optreedt, is de applicatie niet bereikbaar vanaf de container (en kan deze dus niet worden gemonitord).

Als een van deze stappen mislukt, kunt u het volgende proberen:

- Vergelijk ipconfig vanaf de host en vanuit een container (``docker exec -i Checkpoint powershell.exe`` om een powershell-sessie binnen de Checkpoint-container te krijgen) en verifieer de geconfigureerde DNS-server(s).

Probeer een publieke DNS zoals 8.8.8.8 (Google) op te geven wanneer u een nslookup als volgt uitvoert: ``nslookup probemaster1.uptrends.com 8.8.8.8``, als deze correct functioneert wanneer u het IP-adres van de publieke DNS niet gebruikt, maar problemen ondervindt als deze afwezig is, kan er een probleem zijn met het resolven van DNS. Houd er rekening mee dat het gebruik van 8.8.8.8 als DNS-server in production niet wenselijk is, omdat dit de interne applicaties niet kan resolven.

Geef specifieke DNS-server(s) op in het composebestand, zoals te zien is in de onderstaande code. Vergeet niet om dit voor beide containers in het yaml-bestand te doen.

```yaml
TransactionProcessor:
    container_name: TransactionProcessor
    image: uptrends.azurecr.io/win2022/transaction-processor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: local
    environment:
      - ServerId=
      - Password=
    dns:
      - 1.2.3.4
      - 2.3.4.5
```

Vul de IP-adressen in van de DNS-servers die u wilt gebruiken. U kunt deze testen tegen probemaster1.uptrends.com en de hostnaam met nslookup. Vergeet niet om dit vanuit een container te doen.

Mogelijk moet u DNS-requests toestaan die afkomstig zijn van de Docker-containers als uw DNS-servers gebruikmaken van een toelatingslijst. Als u containercontrolestations uitvoert op een cloudplatform zoals Google Cloud, AWS of Azure, kan aanvullende configuratie nodig zijn om connectiviteit vanuit de Docker-containers te garanderen. 

## Nog steeds problemen? 

Als u op enig moment tijdens het probleemoplossingsproces iets niet begrijpt of een vraag heeft, communiceer dan uw vragen of zorgen aan Uptrends door [een support ticket te openen]({{< ref path="contact" lang="nl" >}}). We nemen snel contact met u op. 