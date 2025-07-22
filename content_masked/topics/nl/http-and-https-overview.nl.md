{
  "hero": {
    "title": "Overzicht HTTP- en HTTPS-controleregels"
  },
  "title": "Overzicht HTTP- en HTTPS-controleregels",
  "summary": "Hoe uptime monitoring werkt voor HTTP- en HTTPS-controleregels en hoe u de geavanceerde HTTP-monitoringopties leert kennen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/http-en-https/overzicht-http-en-https",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

[SHORTCODE_1] **Opmerking:** Het controleregeltype **HTTP** is niet langer beschikbaar voor nieuwe gebruikers. Uptrends heeft de functionaliteit van **HTTPS**-controleregels uitgebreid om de beschikbaarheid van HTTP-websites te kunnen blijven controleren. [SHORTCODE_2]

De controleregels Hypertext Transfer Protocol (HTTP) en Hypertext Transfer Protocol Secure (HTTPS) behoren tot de uptime [controleregeltypes]([LINK_URL_1]) die u in een mum van tijd eenvoudig kunt instellen. Deze controleregels gedragen zich op dezelfde manier, zodat u de beschikbaarheid van websites kunt controleren op basis van HTTP- en HTTPS-requests.

Deze controleregels voeren basiscontroles uit op uw [INLINE_CODE_1] en [INLINE_CODE_2] websites vanaf aangewezen [Controlestations]([LINK_URL_2]) wereldwijd. Deze basiscontroles omvatten het verifiëren van de responsstatuscodes van de website, de paginalaadtijd en het laden van inhoudsbronnen. Dat gezegd hebbende, de HTTP- en HTTPS-controleregels halen eenvoudigweg de gevraagde bronnen op van de website. Hun voornaamste zorg is om een foutloze respons van de webserver te krijgen en te bevestigen dat uw pagina operationeel is. Zie voor meer informatie [Hoe een HTTP-controleregel werkt]([LINK_URL_3]).

Als u diepgaande controleregelchecks wilt om de prestaties en systeemuptime van uw website nauwkeurig te meten, raadt Uptrends aan een [Full Page Check]([LINK_URL_4]) te gebruiken. Raadpleeg voor meer informatie het knowledgebase-artikel [Basiscontroles versus Full Page Checks of Real Browser Checks]([LINK_URL_5]).

## Een HTTP- of HTTPS-controleregel instellen

Er is een minimaal verschil tussen het instellen van de Uptime HTTP-controleregel en HTTPS-controleregels. Aangezien de HTTPS-controleregel een uitgebreide en beveiligde versie van HTTP is, bevat deze controleregel een extra check om SSL-certificaatfouten te verifiëren. Om deze instelling te configureren gaat u naar het tabblad [SHORTCODE_3] Extra [SHORTCODE_4] van het configuratiescherm van uw controleregel en vinkt u het selectievakje **Check SSL-certificaatfouten** aan.

Door deze optie in te schakelen, kan uw HTTPS-controleregel valideren dat het SSL-certificaat geen fouten genereert. Schakel deze optie alleen uit om problemen te negeren die door uw SSL-certificaat worden gegenereerd. Als u uw SSL-certificaten uitgebreid wilt monitoren, raadpleeg dan [SSL Certificaat-controleregels]([LINK_URL_6]) om aanvullende controles uit te voeren.

Als u uw eigen HTTP- of HTTPS-controleregel wilt creëren, raadpleeg dan het knowledgebase-artikel [Een HTTP- of HTTPS-controleregel toevoegen]([LINK_URL_7]).

## Geavanceerde HTTP-instellingen

Om uw controleregelinstellingen verder aan te passen gaat u naar het tabblad [SHORTCODE_5] Extra [SHORTCODE_6] van uw HTTP- of HTTPS-controleregel en configureert u het volgende:

- [User agent]([LINK_URL_8]) 
- Authenticatie — als de HTTP-bron die u monitort authenticatie vereist als onderdeel van de HTTP-request, kiest u het juiste type Authenticatie (Geen, Basisauthenticatie, NTLM (Windows)-authenticatie en Digest-authenticatie). Voer uw inloggegevens in de velden **Gebruikersnaam** en **Wachtwoord** in. Houd er rekening mee dat Uptrends uw data altijd [versleutelt]([LINK_URL_9]) ter bescherming.
- Aangepaste HTTP request-velden — configureer de opties **HTTP method** (GET/POST), **HTTP request headers**, **Check SSL-certificaatfouten** en **TLS-versie(s)**. Raadpleeg dit [knowledgebase-artikel]([LINK_URL_10]) voor meer informatie.
