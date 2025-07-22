{
  "hero": {
    "title": "Uptrends en Cloudflare samen gebruiken voor maximale beveiliging"
  },
  "title": "Uptrends en Cloudflare samen gebruiken voor maximale beveiliging",
  "summary": "Ontdek hoe Cloudflare en Uptrends in het algemeen werken en waar u op moet letten als u beide gebruikt.",
  "url": "/support/kb/synthetic-monitoring/controlestations/cloudflare",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/cloudflare"
}

Mogelijk gebruikt u de diensten van Cloudflare om uw websites en API's te beveiligen en te beschermen. Als onderdeel van die diensten blokkeert Cloudflare elk inkomend verkeer van kwaadwillende gebruikers die geautomatiseerde tools of bots (soms als onderdeel van een botnetwerk) gebruiken om toegang te krijgen tot bronnen die door uw sites en API's worden geleverd. 

Cloudflare gebruikt verschillende technologieën, zoals Rate Limiting, IP- en Country blocking, anti-DDoS-technologie en CAPTCHA om requests van legitieme gebruikers te verifiëren en die van geautomatiseerde bots te blokkeren. 

Cloudflare biedt ook een Verified Bot-dienst waarmee u specifieke bots kunt aanwijzen waaraan toegang moet worden verleend tot uw websites en API's. Deze dienst zorgt ervoor dat requests van de aangewezen bots worden geverifieerd en doorgelaten, terwijl alle andere bots worden geblokkeerd, waardoor uw sites extra worden beveiligd.

## Uptrends is een geverifieerde bot

De monitoringactiviteiten die door Uptrends worden uitgevoerd om de beschikbaarheid en performance van uw webpagina's, gebruikerstrajecten en API's te testen, zijn feitelijk botactiviteit: er worden geautomatiseerde processen gebruikt om voortdurend toegang te krijgen tot uw webservers. 

Uptrends is een van de geverifieerde botpartners van Cloudflare. Cloudflare is op de hoogte van Uptrends’ publieke monitoringlocaties – het controlestationnetwerk – en ze vernieuwen regelmatig de lijst met IP-adressen (IPv4 en IPv6) van waaruit monitoring op uw sites plaatsvindt.

Dit betekent dat door Cloudflare en Uptrends samen te configureren, uw website en API-bronnen worden beschermd tegen kwaadwillende bots, terwijl het monitoren van verkeer van Uptrends is toegestaan via de Cloudflare-firewall.

## Lijst met geverifieerde bots

Als onderdeel van Cloudflare Radar wordt een lijst met speciaal geselecteerde bots gepubliceerd als de [Verified bots list](https://radar.cloudflare.com/traffic/verified-bots). Alle legitieme diensten kunnen verzoeken om te worden opgenomen in de lijst met bots die worden vertrouwd door Cloudflare. 

Uptrends heeft het aanvraagproces doorlopen en Cloudflare heeft bevestigd dat Uptrends een volledig geverifieerde bot is. Helaas publiceert Cloudflare slechts een deel van hun geverifieerde bots op hun lijst met geverifieerde bots en hoewel Uptrends een volledig geverifieerde bot is, zult u het niet op die lijst vinden.

## Problemen oplossen

Ondanks de bevestiging van Cloudflare dat Uptrends een geverifieerde bot is en dat de IP-adressen van de controlestationservers op de witte lijst staan bij Cloudflare, melden sommige Uptrends-gebruikers nog steeds af en toe problemen. 

Wanneer Cloudflare inkomend verkeer blokkeert dat afkomstig is van een van de controlestationlocaties, zal het lijken alsof uw site niet beschikbaar is – vanuit een monitoringperspectief. 

Wanneer u onverwachte storingen ondervindt die mogelijk worden veroorzaakt doordat Cloudflare inkomend verkeer van Uptrends blokkeert, volg dan deze stappen:

- Raadpleeg de (Engelstalige) Cloudflare-documentatie over [How to manage good bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/). In dit artikel wordt uitgelegd wat allowlists en blocklists zijn en hoe u regels instelt voor bots die toegang hebben tot een website of applicatie.

- Noteer welke controlestationlocaties problemen hebben met toegang tot uw site of API, en welke niet. Dien vervolgens een ticket in bij [Uptrends Support]({{< ref path="contact" lang="nl" >}}) met deze informatie. Dit helpt ons te achterhalen of het probleem te maken heeft met de whitelisting van Cloudflare of met een andere oorzaak.

- Neem contact op met [Cloudflare Support](https://dash.cloudflare.com/support) als u probeert wijzigingen aan te brengen in de configuratie van uw Cloudflare-firewallregels. Zorg ervoor dat u de (Engelstalige) Cloudflare-documentatie over [Firewall rules actions](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/) leest.

We werken actief samen met Cloudflare om deze problemen op te lossen, en uw input is nodig om de oorzaak beter te begrijpen.