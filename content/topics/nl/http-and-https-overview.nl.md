{
  "hero": {
    "title": "Overzicht HTTP- en HTTPS-controleregels"
  },
  "title": "Overzicht HTTP- en HTTPS-controleregels",
  "summary": "Hoe uptime monitoring werkt voor HTTP- en HTTPS-controleregels en hoe u de geavanceerde HTTP-monitoringopties leert kennen",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/http-en-https/overzicht-http-en-https",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/http-and-https-overview",
  "sectionlist": false
}

{{< callout >}} **Opmerking:** Het controleregeltype **HTTP** is niet langer beschikbaar voor nieuwe gebruikers. Uptrends heeft de functionaliteit van **HTTPS**-controleregels uitgebreid om de beschikbaarheid van HTTP-websites te kunnen blijven controleren. {{< /callout >}}

De controleregels Hypertext Transfer Protocol (HTTP) en Hypertext Transfer Protocol Secure (HTTPS) behoren tot de uptime [controleregeltypes]({{< ref path="support/kb/basics/monitor-types" lang="nl" >}}) die u in een mum van tijd eenvoudig kunt instellen. Deze controleregels gedragen zich op dezelfde manier, zodat u de beschikbaarheid van websites kunt controleren op basis van HTTP- en HTTPS-requests.

Deze controleregels voeren basiscontroles uit op uw `http://` en `https://` websites vanaf aangewezen [Controlestations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="nl" >}}) wereldwijd. Deze basiscontroles omvatten het verifiëren van de responsstatuscodes van de website, de paginalaadtijd en het laden van inhoudsbronnen. Dat gezegd hebbende, de HTTP- en HTTPS-controleregels halen eenvoudigweg de gevraagde bronnen op van de website. Hun voornaamste zorg is om een foutloze respons van de webserver te krijgen en te bevestigen dat uw pagina operationeel is. Zie voor meer informatie [Hoe een HTTP-controleregel werkt]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/how-an-http-monitor-works" lang="nl" >}}).

Als u diepgaande controleregelchecks wilt om de prestaties en systeemuptime van uw website nauwkeurig te meten, raadt Uptrends aan een [Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) te gebruiken. Raadpleeg voor meer informatie het knowledgebase-artikel [Basiscontroles versus Full Page Checks of Real Browser Checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="nl" >}}).

## Een HTTP- of HTTPS-controleregel instellen

Er is een minimaal verschil tussen het instellen van de Uptime HTTP-controleregel en HTTPS-controleregels. Aangezien de HTTPS-controleregel een uitgebreide en beveiligde versie van HTTP is, bevat deze controleregel een extra check om SSL-certificaatfouten te verifiëren. Om deze instelling te configureren gaat u naar het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van het configuratiescherm van uw controleregel en vinkt u het selectievakje **Check SSL-certificaatfouten** aan.

Door deze optie in te schakelen, kan uw HTTPS-controleregel valideren dat het SSL-certificaat geen fouten genereert. Schakel deze optie alleen uit om problemen te negeren die door uw SSL-certificaat worden gegenereerd. Als u uw SSL-certificaten uitgebreid wilt monitoren, raadpleeg dan [SSL Certificaat-controleregels]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="nl" >}}) om aanvullende controles uit te voeren.

Als u uw eigen HTTP- of HTTPS-controleregel wilt creëren, raadpleeg dan het knowledgebase-artikel [Een HTTP- of HTTPS-controleregel toevoegen]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="nl" >}}).

## Geavanceerde HTTP-instellingen

Om uw controleregelinstellingen verder aan te passen gaat u naar het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van uw HTTP- of HTTPS-controleregel en configureert u het volgende:

- [User agent]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks#what-is-a-user-agent" lang="nl" >}}) 
- Authenticatie — als de HTTP-bron die u monitort authenticatie vereist als onderdeel van de HTTP-request, kiest u het juiste type Authenticatie (Geen, Basisauthenticatie, NTLM (Windows)-authenticatie en Digest-authenticatie). Voer uw inloggegevens in de velden **Gebruikersnaam** en **Wachtwoord** in. Houd er rekening mee dat Uptrends uw data altijd [versleutelt]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="nl" >}}) ter bescherming.
- Aangepaste HTTP request-velden — configureer de opties **HTTP method** (GET/POST), **HTTP request headers**, **Check SSL-certificaatfouten** en **TLS-versie(s)**. Raadpleeg dit [knowledgebase-artikel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/monitoring-websites-other-than-the-production-server" lang="nl" >}}) voor meer informatie.
