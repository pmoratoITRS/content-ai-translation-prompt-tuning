{
  "hero": {
    "title": "Door de klant beheerde controlestations (Docker-containers)"
  },
  "title": "Door de gebruiker beheerde controlestations (Docker-containers)",
  "summary": "Wat is een door de gebruiker beheerd controlestation en hoe implementeert u Uptrends monitoring achter de firewall van uw bedrijf in Docker-containers.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-controlestations-docker",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends biedt een Docker-container om een Uptrends-controlestation op uw netwerk uit te voeren (achter uw firewall). U krijgt volledige Uptrends-functionaliteit op het persoonlijke controlestation en kunt tests van uw eigen infrastructuur uitvoeren. Met de Uptrends-applicatie kiest u waar de tests van uw controleregels worden uitgevoerd: intern op uw persoonlijke controlestation, extern via Uptrends' [wereldwijde netwerk van controlestations]([LINK_URL_1]), of op beide.

![]([LINK_URL_2])

Hoewel de tests op uw netwerk plaatsvinden, gebeuren alle andere activiteiten zoals planning, alerting en rapportage in de Uptrends cloud-applicatie, en Uptrends slaat uw controleregeldefinities en testdata op in zijn datacenters.

Uw persoonlijke controlestation is exclusief voor uw Uptrends-account en uitsluitend voor uw gebruik. U kunt controleregels intern uitvoeren om uw niet-internetgerichte infrastructuur te controleren, zoals:

- Intranet
- Interne web-enabled bedrijfsapplicaties
- Webservices (API's)
- Acceptatie- en andere preproductie-omgevingen
- Basisinfrastructuur uptime monitoring voor servers, inclusief databaseservers, e-mailservers en SFTP-servers

## Hoe werkt een persoonlijk controlestation?

De set-up werkt als volgt: de persoonlijke controlestation-software van Uptrends is verpakt in Docker-containers. Deze containers worden gehost in uw eigen netwerk op een containerplatform. Het platform kan uw eigen host of virtuele machine zijn en ook andere opties zoals Azure zijn beschikbaar. De instructies in [Een Docker persoonlijk controlestation installeren]([LINK_URL_3]) zijn gericht op de set-up met een virtuele machine.

Een persoonlijk controlestation gebruikt minimaal twee Windows Docker-container instances die draaien op uw containerplatform dat is verbonden met uw netwerk. Deze instances hebben alleen toegang tot de gemonitorde infrastructuur op uw netwerk en u moet de Docker-apps isoleren van de rest van uw netwerk. Uptrends levert de software die draait op deze containerized controlestations, terwijl u de ondersteunende hardware en infrastructuur draaiende houdt.

Uptrends' monitoringsysteem maakt gebruik van een centraal besturings- en controlesysteem, het cloudplatform. Het cloudplatform heeft uw monitoringdefinities en bepaalt op basis van uw controlestationselectie waar en wanneer de volgende controleregelcheck moet plaatsvinden. Wanneer u een controleregel configureert om een persoonlijk controlestation te gebruiken, kiest Uptrends een van de container instances om de controleregelcheck uit te voeren. De container instance voert de tests uit en rapporteert terug aan Uptrends. Uptrends verwerkt en bewaart de data van de test die is uitgevoerd op uw persoonlijke controlestation. Als Uptrends een fout detecteert, test het onmiddellijk opnieuw op de andere container instance. Als de controleregel de tweede keer een fout detecteert, geeft Uptrends een alert vanuit de cloud, zie "Persoonlijke controlestation-architectuur" hieronder.

Als uw controlestation om welke reden dan ook helemaal niet meer beschikbaar is, geeft Uptrends een foutmelding om u te laten weten dat uw persoonlijke controlestation is uitgevallen. Enkele redenen waarom downtime kan optreden, zijn:

- Het persoonlijke controlestation verliest zijn internetverbinding.
- Al uw container instances gebruiken hetzelfde hostingplatform en dat platform ondervindt een storing.

![]([LINK_URL_4])

1. Uitgaande HTTPS (inclusief WebSockets)-connectiviteit met het Uptrends-cloudplatform voor besturing en controle, om controleregeldefinities op te halen en resultaten terug te sturen. De uitgaande WebSockets-verbinding wordt gebruikt om opdrachten te ontvangen en zal voor een lange periode open zijn. Op de whitelist voor vier Uptrends-locaties.
2. Uitgaande HTTPS-connectiviteit om containerupdates op te halen met controlestation- en browserupdates
3. Uitgaande internetconnectiviteit om de intrekkingsstatus van gebruikte certificaten te valideren
4. Connectiviteit van het Uptrends Persoonlijke Controlestation naar de gemonitorde infrastructuur, met geblokkeerde connectiviteit naar alle andere delen van het platform

## Hoe krijg ik een persoonlijk controlestation? 

Nadat u heeft besloten uw interne infrastructuur te monitoren met een Docker persoonlijk controlestation moet u de infrastructuur voorbereiden: stel (bij voorkeur 2) Windows Server-gebaseerde hosts in zoals wordt uitgelegd in de installatiestappen in [Een Docker persoonlijk controlestation installeren]([LINK_URL_5]).

Mocht u gaandeweg nog vragen hebben, aarzel dan niet om deze te stellen door gebruik te maken van Uptrends' [ticketsysteem]([LINK_URL_6]). Gesprekken met u en de genomen beslissingen worden vastgelegd in ons ticketsysteem. U kunt de besprekingen doornemen, opmerkingen maken en rechtstreeks vragen stellen aan de Support engineer die aan uw ticket is toegewezen.

## Beveiligingsoverwegingen

Hoewel Uptrends best practices uit de branche en due diligence toepast op beveiligingskwesties, ligt de verantwoordelijkheid voor de impact van het persoonlijke controlestation op het netwerk van de klant bij de klant. Hieronder vindt u meer informatie over wie verantwoordelijk is voor welk onderdeel.

### Verantwoordelijkheden van Uptrends

- Persoonlijke controlestation-containers voorzien van up-to-date software
- Alle softwarecomponenten die in de containers worden gebruikt up-to-date houden (d.w.z. de basis van de images en de webbrowsers)
- Al het verkeer van en naar het platform van de klant versleutelen
- Informatie voor whitelisting verstrekken

### Verantwoordelijkheden van de gebruiker

- Firewallregels toepassen om toegang te verlenen tot alleen de infrastructuur die moet worden gemonitord
- Accounts voor hun monitoring gebruiken met beperkte blootstelling aan het platform
- Waar van toepassing virusscanning enzovoort gebruiken
- Indien nodig extra waarborgen toepassen (bijvoorbeeld wanneer een transactie een herhaalde geldoverdracht uitvoert)
- De Docker-host en containers bij voorkeur elke dag updaten, maar ten minste elke twee weken om te verzekeren dat de meest recente browserversies in gebruik zijn en de nieuwste beveiligingspatches zijn toegepast
- Het host-besturingssysteem up-to-date houden
- [Het uitschakelen van snapshots, screenshots en filmstrips]([LINK_URL_7]) overwegen in basis- en browsercontroleregeltypes 

[SHORTCODE_1] Ga voor meer informatie naar [Persoonlijke controlestations - veelgestelde vragen]([LINK_URL_8]). [SHORTCODE_2]}
