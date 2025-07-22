{
  "hero": {
    "title": "Vereisten voor persoonlijke locaties"
  },
  "title": "Vereisten voor persoonlijke locaties",
  "summary": "Wat zijn de technische vereisten voor persoonlijke locaties?",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-controlestations-vereisten",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-requirements"
}

## Vereisten en noodzakelijke instellingen

Er zijn enkele vereisten voor hardware en netwerk, en noodzakelijke netwerkinstellingen. De vereisten zijn gebaseerd op algemene scenario's en als u twijfelt over wat u nodig heeft, kunt u dit altijd navragen bij [Uptrends' Support]({{< ref path="contact" lang="nl" >}}). Zorg ervoor dat u zich aan de vereisten houdt en dat de instellingen zijn geconfigureerd voordat u begint met het installeren van het controlestation.

### Capaciteit persoonlijke locatie

Uw persoonlijke locaties worden alleen gebruikt voor uw controleregels. De vereiste capaciteit hangt af van het soort monitoring dat op de controlestations in de persoonlijke locatie wordt uitgevoerd.

Niet-browsergebaseerde monitoring, zoals HTTPS, connect, ping en Multi-step API hebben vooral impact op de beschikbare netwerkcapaciteit. Browsergebaseerde controleregels hebben vooral impact op de servercapaciteit (CPU, geheugen, disk I/O).

### Berekening van een typische capaciteit 

De typische capaciteit voor een aanbevolen set-up van een persoonlijke locatie, bij gebruik van de aanbevolen [hardware]({{< ref path="#hardware-requirements" lang="nl" >}}) en met twee controlestations, zou zijn:

- 2 x 10 transacties met intervallen van 5 minuten
- 2 x 10 Full Page Checks met intervallen van 5 minuten
- 100 basiscontroleregels met intervallen van 1 minuut

De duur van de transactie is van invloed op de capaciteit.

De set-up laat ruimte voor:

- Bevestigen van [onbevestigde foute]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}})
- Onderhoud van een van de controlestations, bijv. om containers of de Docker host te upgraden

### Redundantie

De capaciteit zoals hierboven beschreven houdt geen rekening met redundantie van controleregels. Er zijn enkele mogelijke configuraties waarbij een persoonlijke locatie feitelijk meer monitoringtaken kan uitvoeren dan hierboven vermeld. Dit is het geval wanneer u redundantie op verschillende niveaus heeft, b.v. wanneer u meerdere persoonlijke locaties voor uw monitoring gebruikt.

## Hardwarevereisten {id="hardware-requirements"}

Controleer de volgende hardwarespecificaties voor het toevoegen van een controlestation. Voor betrouwbaarheid raden we aan om twee controlestations te gebruiken en voor de beste performance raden we aan om drie of meer controlestations te gebruiken. Elk controlestation moet voldoen aan de specificaties zoals hieronder gedefinieerd. 

|   | Aanbevolen | Minimum |
| --- | --- | --- |
| **CPU** | 4 cores | 2 cores |
| **RAM** | 8 GB | 4 GB |
| **Opslag** | 60 GB op snelle opslag (SSD) | 60 GB |
| **Besturingssysteem** | Windows Server 2022 LTSC Standard | Windows Server 2019 LTSC Standard* |

*Houd er rekening mee dat Docker op Windows Server 2019 bekende problemen heeft met DNS resolving*.

## Netwerkvereisten

U moet aan de volgende netwerkvereisten voldoen.

**IPv4** — Vast IPv4-adres voor elke controlestation-server  

**IPv6** — Optioneel, afhankelijk van of u IPv6 gebruikt in de gemonitorde infrastructuur. 

**Netwerk** — Hoewel we 1 Gbps aanbevelen, is het werkelijke gebruik van deze verbinding veel lager (meestal 1 tot 10 Mbps 95%) en zeer constant. 
Een verbinding met internet die goed is gedimensioneerd om de meetgegevens over te brengen naar het Uptrends-platform. 


## Netwerkinstellingen

### Firewall

Er mag geen SSL-inspectie plaatsvinden op het verkeer tussen de controlestations en de Uptrends-cloudservers.

Zorg ervoor dat u geen Group Policy Objects (GPOs) heeft geïnstalleerd die voorkomen dat Docker een lokale firewall creëert. Op de computer waarop Docker draait stelt u de group policy-instelling *Apply local firewall rules* in op 'Yes'.

### IPv6-vereisten

Als het interne netwerk IPv6-enabled is, geef dan een vast IPv6-adres en gateway op voor elke controlestationserver. Met het IPv6 IP-adres kunnen we uw infrastructuur monitoren via IPv6 (met de juiste firewallconfiguratie). Zonder het vaste IPv6-adres kan Uptrends alleen monitoren via IPv4.

### DNS-servers

Voor het controlestation moet(en) één of meer DNS-server(s) worden geconfigureerd op de Docker-host. Standaard gebruiken containers de DNS-configuratie van de host om hostnamen voor de geteste applicaties te resolven en voor connectiviteit met het Uptrends-cloudplatform. 

### FCrDNS

Als u mailservers via een externe route wilt monitoren, configureert u reverse DNS met: checkpoint\_name@uptrends.net om te converteren naar het bijbehorende externe IP-adres.
