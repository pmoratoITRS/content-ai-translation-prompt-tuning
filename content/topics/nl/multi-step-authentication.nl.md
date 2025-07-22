{
  "hero": {
    "title": "Multi-step monitoring authenticatie"
  },
  "title": "Multi-step monitoring authenticatie",
  "summary": "Leer meer over de beschikbare opties voor authenticatie bij gebruik van Multi-step API monitoring. ",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-authenticatie",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-authentication"
}

Veel API's vereisen dat de caller authenticatie-informatie opgeeft om hun identiteit te verifiëren, en mogelijk de toegangsrechten van die caller. Authenticatie-informatie kan doorgegeven worden met behulp van HTTP headers (Basic/NTLM/Digest authentication), door access tokens (OAuth) uit te wisselen, door te eisen dat de cliënt een cliëntcertificaat toevoegt aan de request, of een combinatie hiervan. 

In dit artikel worden de op HTTP header en token gebaseerde authenticatie-opties in Uptrends besproken. Meer informatie over het configureren van cliëntcertificaten vindt u in [het artikel over authenticatie van cliëntcertificaten](/support/kb/synthetic-monitoring/api-monitoring/multi-step-clientcertificaten-monitoren). 

## Standaardtypes authenticatie

Het gedeelte Authenticatie op het tabblad Request van een Multi-step API-controleregel biedt verschillende authenticatietypes. Ze gebruiken allemaal een gebruikersnaam/wachtwoord-combinatie, maar de manier waarop deze inloggegevens worden verwerkt en naar de API worden verzonden, is voor elk type verschillend:

-   **Basic authentication**: de gebruikersnaam en het wachtwoord zijn gecodeerd in een eenvoudig Base-64-gecodeerd formaat en worden verzonden naar de API-server.
-   **NTLM (Windows) authentication**: wanneer u dit type opgeeft, worden er verschillende requests naar de API verzonden om te onderhandelen over de authenticatie die moet worden gebruikt, voordat de laatste HTTP-request met de juiste authenticatie wordt verzonden. Deze reeks requests telt als één enkele stap. Als een Windows-domein moet worden opgegeven, neemt u dit op in de gebruikersnaam: YOURDOMAIN\\username.
-   **Digest authentication**: de gebruikersnaam en het wachtwoord worden gehasht met behulp van het MD5-hashing-algoritme, en de hash wordt naar de server verzonden. 
-   **None**: kies *None* als u geen gebruik wilt maken van authenticatie voor uw HTTP request.

### HTTP headers

De hierboven beschreven authenticatietypes zullen allemaal meerdere requests verzenden (hoewel ze allemaal nog steeds als één stap tellen). De eerste request bevat geen inloggegevens (gehasht/gecodeerd of anderszins). De client wacht dan tot de server een challenge verzendt, in de vorm van een 401 (Ongeautoriseerde) response code en een **WWW-Authenticate** header die de vereiste authenticatiemethode specificeert. Vervolgens zal de client de request opnieuw verzenden, maar deze keer met de juiste Authorization header.

Wanneer u een van deze authenticatietypes gebruikt, hoeft u doorgaans geen andere authenticatiespecifieke HTTP headers op te geven: de juiste Authorization header wordt automatisch gegenereerd. Als de challenge echter onvolledig is (omdat de server reageert met een andere statuscode dan 401, of omdat de WWW-Authenticate header ontbreekt), zal de controleregel een fout retourneren en moet u mogelijk handmatig de correcte Authorization header definiëren. 

Voor Basic authentication verwachten we bijvoorbeeld dat de server reageert met een challenge na de eerste request, met een header `WWW-Authenticate: Basic` en een statuscode van 401: Unauthorized. Als dit niet gebeurt, moet u mogelijk de header voor Basic authentication handmatig instellen, zodat de inloggegevens zelfs zonder een correcte challenge worden doorgegeven. 

Volgens het [Basic authentication scheme](https://datatracker.ietf.org/doc/html/rfc7617), moeten de inloggegevens worden doorgegeven in een Base64 gecodeerde string van *username:password*. Base64 gecodeerde string 'username:password' levert  `dXNlcm5hbWU6cGFzc3dvcmQ=` op, die vervolgens moet worden doorgegeven in een Authorization header. Door de header `Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=` toe te voegen aan de MSA-stap, kunt u de noodzaak van een challenge op effectieve wijze omzeilen.

### Ondersteuning van variabelen

De velden gebruikersnaam en wachtwoord ondersteunen variabelen. U kunt voorgedefinieerde variabelen (bijvoorbeeld: {{< Code/Symbol type="variable" >}}{{username}}{{< /Code/Symbol >}} en {{< Code/Symbol type="variable" >}}{{password}}{{< /Code/Symbol >}}) met de juiste waarden creëren en deze variabelennamen vervolgens gebruiken in de authenticatievelden. [Meer informatie over variabelen en voorgedefinieerde variabelen.](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variabelen)

## Aangepaste authenticatie

Wanneer uw API OAuth als authenticatieprotocol gebruikt, heeft u een meer uitgebreide set-up nodig. Afhankelijk van uw API heeft u wellicht iets nodig dat heel specifiek is voor uw situatie. OAuth 2.0 in het bijzonder gebruikt ten minste één afzonderlijk request voor alleen het authenticatieproces. Met deze request wordt toegang tot de API gevraagd (met behulp van een van de standaardtypes authenticatie, door in de URL inloggegevens op te geven of zelfs een webpagina log-in uit te voeren). Na succesvolle authenticatie wordt het OAuth access token vastgelegd en opgeslagen in een variabele, zodat het in volgende requests kan worden gebruikt.

Als u geen OAuth gebruikt, maar een ander protocol, werkt het mogelijk nog steeds op dezelfde manier: u moet eerst inloggegevens opgeven die uw identiteit aan de API "bewijzen". De API-server reageert dan door u een inlogtoken te geven dat een bepaalde tijd geldig is. Door dat token vast te leggen en op te slaan in een variabele, kunt u een reeks requests uitvoeren die het inlogtoken gebruiken om toegang te krijgen.

### OAuth 2.0-authenticatie instellen

In het volgende voorbeeld zullen we een eenvoudige vorm van OAuth 2.0-authenticatie instellen. Ons doel is om een toegangstoken te verkrijgen van de API, die we vervolgens in latere requests kunnen gebruiken.

Hiervoor sturen we eerst een request die de juiste OAuth-velden bevat. In dit geval vragen we om toegang op basis van een autorisatiecode, een client-id en een client secret. De client-id en het client secret zijn vaste waarden die we kunnen definiëren als voorgedefinieerde variabelen. In onze eenvoudige set-up zal de autorisatiecode ook een vaste waarde zijn, maar in uw set-up kan het nodig zijn om die autorisatiecode eerst met een afzonderlijke stap op te halen.

Eerst voegen we die waarden toe aan de voorgedefinieerde variabelen:

![Predefined variables](/img/content/scr-MSA-predefined-variables-auth.min.png)

Nu die variabelen gedefinieerd zijn, kunnen we nu een request naar onze API instellen door verwijzingen naar die variabelen erin op te nemen, samen met andere parameters die de API verwacht. Voeg in de eerste stap van onze multi-step set-up deze URL toe:

`GET https://myapi.com/oauth/token?grant_type=authorization_code&code={{authorizationcode}}&client_id={{clientid}}&client_secret={{clientsecret}}`

We verwachten dat de API een datastructuur retourneert die het toegangstoken bevat dat we nodig hebben, maar hoe wordt die datastructuur geformatteerd? Om ervoor te zorgen dat we gegevens in JSON-indeling krijgen, vertellen we de server dat we alleen het application/json formaat accepteren door dat in een HTTP-header te specificeren:

![MSA accept header](/img/content/scr-msa-header-example.min.png)

Nu deze header is gespecificeerd kunnen we verwachten dat de response er ongeveer zo uitziet:

`{    "access_token":"SGV5ISBZb3UgZm91bmQgdGhpcyB0ZXh0IQ==",    "token_type":"Bearer",    "expires_in":86400  } `

Het enige wat we nu hoeven te doen, is het veld access\_token vastleggen in de JSON response. Om dit te doen maken we een nieuwe variabele op het tabblad Response van onze stap:

-   De response zou JSON moeten bevatten, dus kies {{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} als de bron voor onze variabele.
-   Aangezien het kenmerk **access\_token** zich op het hoogste niveau in onze datastructuur bevindt, is onze JSON expressie simpelweg {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}}.
-   We kiezen {{< Code/Symbol type="variable" >}}accesstoken{{< /Code/Symbol >}} als onze variabelenaam. Dit is de naam waarnaar we in latere stappen zullen verwijzen.

![Access token variable](/img/content/scr-msa-auth-variable.min.png)

Hoewel het hoofddoel van deze eerste stap is om het access token vast te leggen, voert het ook al enige monitoring uit: als de API op dit punt een fout retourneert of als de response geen access token bevat, zal deze stap dit detecteren en een fout rapporteren.

Nu we een geldig access token hebben, kunnen we eindelijk toegang krijgen tot de feitelijke API-methode die we willen controleren (bijvoorbeeld voor het ophalen van een lijst met producten). Maak een nieuwe stap om deze API call te definiëren. Nadat we de methode en URL voor deze nieuwe request hebben opgegeven, gaan we het access token dat we zojuist hebben vastgelegd, doorgeven. OAuth 2.0-gebaseerde API's verwachten een HTTP header met de naam **Authorization**, met een waarde `Bearer {{accesstoken}}`

![Access token header](/img/content/scr-msa-auth-accesstoken-header.min.png)

We kunnen dit herhalen voor elke extra stap die dezelfde access token vereist.
