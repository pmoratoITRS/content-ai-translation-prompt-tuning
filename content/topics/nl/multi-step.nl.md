{
  "hero": {
    "title": "Multi-step API monitoring configureren"
  },
  "title": "Multi-step API monitoring configureren",
  "summary": "Stapsgewijze instructies voor het configureren van Multi-step API Monitoring.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step"
}

Om uw API effectief te monitoren moet u vaak een reeks HTTP-requests creëren, waarbij elke request data ophaalt uit een eerdere request om de volgende reeks taken uit te voeren. Met de **Multi-step API-controleregel** kunt u meerdere HTTP-requests instellen, [variabelen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined" lang="nl" >}}) definiëren, [door de gebruiker gedefinieerde functies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="nl" >}}) maken, [aangepaste scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="nl" >}}) instellen en nog veel meer.

Hier volgen enkele mogelijke scenario's waarom u een reeks HTTP-requests zou moeten uitvoeren:

- Uw API vereist geverifieerde toegang: een API-client moet eerst zijn inloggegevens verifiëren om toegang te krijgen tot HTTP-methoden (bijvoorbeeld met behulp van de OAuth-verificatie).
- U wilt een functioneel scenario in uw API testen dat bestaat uit meerdere stappen die meestal door uw eindgebruikers in een bepaalde volgorde worden uitgevoerd.
- Uw HTTP-request retourneert een redirect naar een andere URL en u wilt het gedrag van die respons inspecteren voordat u de redirect volgt.

## Functies van de Multi-step API-controleregel

De **Multi-step API-controleregel** geeft u volledige controle over de complete inhoud van de HTTP-request. De functies omvatten:

- Stel de HTTP method, URL, request headers en request body in voor iedere request.
- [Voeg authenticatie toe (Basic/NTLM/Digest/OAuth)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="nl" >}}) of [voeg cliëntcertificaten toe]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="nl" >}}) om toegang te verkrijgen tot beveiligde API's.
- [Definieer assertions (controles) voor iedere response]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}}) voor het verifiëren van de HTTP-statuscode, inhoudcontroles (gebaseerd op platte tekst, JSON- of XML-content), requestduur en meer.
- Extraheer inhoud uit de response body, response headers, cookies en [sla ze op in variabelen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}). Dergelijke variabelen kunnen in latere stappen gebruikt worden om nieuwe URL's, request headers enzovoort te bouwen.
- Gebruik globale definities zoals [voorgedefinieerde variabelen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined" lang="nl" >}}), [door de gebruiker gedefinieerde functies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="nl" >}}), [vrije API-kengetallen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="nl" >}}) en [hashing en codering]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/hashing-and-encoding" lang="nl" >}}).

Deze functies helpen u ervoor te zorgen dat uw API correct functioneert en binnen de door u gespecificeerde limieten presteert. De stapsgewijze aanpak stelt u in staat om zeer krachtige scenario's op te zetten zonder complexiteit toe te voegen. Zolang u maar weet hoe uw API zich moet gedragen, hoeft u niet te kunnen programmeren om aan de slag te gaan met API-monitoring.

## Creëer een multi-step API-controleregel

Een multi-step API-controleregel toevoegen:

1. Ga naar {{< AppElement type="menuitem" >}} API > API-controleregels beheren {{< /AppElement >}} en klik op de {{< AppElement type="iconAdd" >}}{{< /AppElement >}} knop.
2. Klik in het pop-upvenster *Kies een controleregel type* op *Multi-step API* en klik op de knop {{< AppElement type="button" >}} Kiezen {{< /AppElement >}}.  
3. Zodra de controleregel is gecreëerd, geeft u uw controleregel een *Naam*.  
4. Stel het *Controle-interval* in. Uw [controle-interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="nl" >}}) is de tijd tussen het einde van de ene controle en het begin van de volgende.
5. Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}} om de details voor elke stap in te voeren.

Uw nieuwe controleregel begint met één (lege) stap. U kunt het volgende doen:
- Klik op {{< AppElement type="buttonPrimary" >}} Request-stap toevoegen {{< /AppElement >}} om extra stappen toe te voegen.
- Klik op het **>**-pictogram naast een stap om stapdetails uit te vouwen en te bewerken.
- Klik op het pictogram **Stap dupliceren** om een kopie te maken van een bestaande stap. 
- Klik op het **X**-pictogram om een stap te verwijderen.
- Gebruik de knoppen *Verplaats stap omhoog* en *Verplaats stap omlaag* om de positie van de stappen te verplaatsen.

![Voorbeeld MSA-stappen](/img/content/scr-msa-example-steps.min.png)

## Configureer een Request-stap

Als u de visuele stap-editor bekijkt, ziet u het tabblad {{< AppElement type="tab" >}} Request {{< /AppElement >}}. Een stap in Multi-step API monitoring bestaat uit één round-trip call naar de API (bijvoorbeeld één request en één response). Binnen elke stap kunt u uw request definiëren en Uptrends vertellen hoe de response moet worden afgehandeld. Elke Multi-step API begint met één lege stap.

### Request

![Details tabblad Request](/img/content/scr-msa-editor-request-tab.min.png)

Het tabblad **Request** bevat alle data die nodig zijn om de daadwerkelijke HTTP request in de stap uit te voeren. Doe ten minste het volgende:

1. Kies de juiste HTTP method: **GET**, **POST**, **PUT**, **PATCH**, **DELETE**, **HEAD** of **OPTIONS**. Als u een andere methode nodig heeft, [neem dan contact met ons op]({{< ref path="contact" lang="nl" >}}).
2. Vul de URL in voor de request. Gebruik een volledig gekwalificeerde URL, inclusief het schema ("https://" of "http://"), de domeinnaam en het pad voor uw API, en eventuele query string parameters die u wilt opnemen.

#### Request body

Wanneer u een POST-, PUT-, PATCH-, HEAD-, OPTIONS- of DELETE-request opgeeft, kunt u met het veld **Request body** specifieke data (payload) verzenden als onderdeel van de requestdefinitie. Bijvoorbeeld door een specifieke gebruikersnaam en wachtwoord te versturen om een nieuw gebruikersaccount te maken.

Hieronder staan de data-indelingen voor de request body waaruit u kunt kiezen:

- Platte tekst — hiermee kunt u platte teksten zonder opmaak versturen.
- Bestand uploaden (als form-data) — hiermee kunt u een bestand (zoals afbeeldingen en documenten uit de [Vault]({{< ref path="/support/kb/api/vault-api" lang="nl" >}})) versturen in form-data-formaat.
- Bestand uploaden (als binary) — hiermee kunt u een bestand (zoals afbeeldingen en documenten uit de [Vault]({{< ref path="/support/kb/api/vault-api" lang="nl" >}})) versturen in een raw binary data-formaat.
- Multi-part form — hiermee kunt u meerdere types inhoud in verschillende formaten (zoals platte-tekstinvoer of bestanden die zijn opgehaald uit de [Vault]({{< ref path="/support/kb/api/vault-api" lang="nl" >}})) tegelijk versturen.

In de meeste gevallen en afhankelijk van het gekozen dataformaat, wordt de juiste `Content-Type`- request header-waarde automatisch ingesteld (zoals `multipart/form-data`) zodat de server uw data correct kan identificeren, lezen en verwerken. U kunt ook de request header `Content-Type` opgeven, die in het volgende gedeelte van dit artikel wordt besproken.

#### Request headers {id="request-headers"}

Een HTTP request bevat meestal enkele request headers om het formaat van de data die worden verzonden te specificeren, of om verder te beschrijven wat voor soort respons verwacht wordt. Bij het configureren van een request stap zult u merken dat bepaalde headers automatisch worden toegevoegd. Deze headers bestaan uit een standaardset, afhankelijk van het type request dat u doet (GET-requests hebben bijvoorbeeld een andere set headers dan POST-requests). Om een standaard header te overschrijven voegt u simpelweg een nieuwe header toe met precies dezelfde naam als de bestaande, maar met een andere waarde.

{{< callout >}} **Opmerking:** Voor optimalisatiedoeleinden is **Connection: Keep-Alive** verwijderd uit de lijst met standaard request headers. In het achtergrondproces is de request header al het standaardgedrag voor HTTP/1.1 en wordt niet langer ondersteund voor HTTP/2 en HTTP/3. {{< /callout >}}

U kunt ook nieuwe headers toevoegen door deze stappen te volgen:

1. Klik op de knop {{< AppElement type="buttonSecondary" >}}Request header toevoegen{{< /AppElement >}} om een request header key en waarde toe te voegen.
2. Voer Content-Type in als de header key.
3. De juiste header waarde is afhankelijk van de data die u verzendt. De meest voorkomende content types zijn `application/json` voor JSON-data, `text/xml` voor XML-data en `application/x-www-form-urlencoded` voor webformulierendata.

Evenzo, als uw API vereist dat u authenticatie opneemt, voegt u een `Authorization` header toe samen met de juiste data in het veld Waarde.

![Voorbeelden van request headers](/img/content/scr-MSA-headers-default_override_auth.min.png)

De afbeelding hierboven toont een voorbeeld van een request stap. Let op het volgende:

- Het is een POST request naar `https://www.galacticresorts.com/api/Reservation`
- De standaard headers die voor deze request zijn ingesteld, zijn:
  - `Host`
  - `Accept-Encoding`
- De waarden voor de header `Host` wordt bepaald bij het verzenden van de request.
- Handmatige headers `Content-Type` en `Authorization` zijn toegevoegd om respectievelijk het dataformaat te specificeren en de benodigde inloggegevens te verstrekken.
- Standaard `Accept-Encoding` is overschreven.
- De request body bevat wat `x-www-form-urlencoded`-inhoud, verwijzend naar enkele [variabelen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}).

#### Authenticatie

Veel API’s zijn beveiligd en alleen toegankelijk door inloggegevens te verstrekken. Als uw API gebruikmaakt van authenticatie op het HTTP-protocolniveau, kies dan uw type authenticatie (Basic, NTLM or Digest) en vul de bijbehorende gebruikersnaam en wachtwoord in. Als alternatief kunt u een op OAuth gebaseerde authenticatie instellen met afzonderlijke stappen. [Meer informatie over het instellen van ingebouwde of aangepaste authenticatie]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="nl" >}}).

#### Gebruik inloggegevens uit de vault

Het is mogelijk om op elk punt verwijzingen naar [vault-inloggegevens]({{< ref path="support/kb/account/vault#credential-set" lang="nl" >}}) te gebruiken als onderdeel van de request body, request headers of als de waarde voor uw gebruikersnaam/wachtwoord onder *Authenticatie*. Gebruik de volgende syntaxis om naar een vault-item te verwijzen: `{{@VaultItem.<itemGuid>.Password}}` of `{{@VaultItem.<itemGuid>.Username}}` afhankelijk van welke waarde vereist is. Om de `itemGuid` te vinden navigeert u naar het vault-item met de inloggegevens en kopieert u vervolgens het laatste deel van de URL in de URL-balk van uw browser.

![Voorbeelden van verwijzingen naar vault-items](/img/content/scr-MSA-vault-creds-references.min.png)

#### Stel de TLS-versies in

De Transport Layer Security (TLS) is een beveiligingsprotocol dat verbindingen tussen websites en servers authenticeert, versleutelt en beschermt. Door het selectievakje *Alleen specifieke TLS-versies toestaan* aan te vinken in uw MSA-controleregel, kunt u specifieke TLS-versies selecteren tijdens de TLS-handshake voor HTTP-verbinding. U kunt het selectievakje ook uitschakelen als er geen beperkingen nodig zijn.

Alle [Uptrends-controlestations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="nl" >}}) ondersteunen TLS 1.1 en TLS 1.2. Door de optie TLS 1.3 te selecteren, wordt de selectie van controlestations beperkt tot die met TLS 1.3-functionaliteit. Hoewel TLS 1.1 nog steeds beschikbaar is, wordt het niet aanbevolen.

![Selectievakje TLS-versies in MSA-controleregels](/img/content/scr-tls-versions-option-checkbox.min.png)

#### Stel de HTTP-versie in

Met de optie **HTTP-versie** kunt u bepalen welke HTTP-versie de controlestationservers gebruiken bij het doen van requests. Gebruik deze optie om ervoor te zorgen dat de servers effectief communiceren met de API op het gebied van compatibiliteit, prestaties en beveiliging.

![HTTP-versie](/img/content/scr-msa-step-http-version.min.png)

Standaard is de optie **HTTP-versie** niet aangevinkt, wat betekent dat de server automatisch de hoogste ondersteunde HTTP-versie gebruikt die beschikbaar is, met een fallback niet lager dan HTTP/1.1.

Momenteel is HTTP/3 beschikbaar op geselecteerde controlestationlocaties en de ondersteuning wordt binnenkort uitgebreid naar meer locaties.

{{< callout >}} **Opmerking:** Met de HTTP-versie kunt u slechts één versie selecteren, terwijl de **TLS-versie(s)** de selectie van meerdere versies ondersteunen.
{{< /callout >}}

### Importeer cURL requests {id="import-curl"}

Het is ook mogelijk om cURL requests rechtstreeks te importeren om uw stappen te creëren, zonder ze handmatig opnieuw te hoeven maken. Dit doet u als volgt:

1. In de **Visuele stap-editor** (in het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}} van de controleregelinstellingen) van de Multi-step API-controleregel waarin u een stap wilt importeren op basis van een curl-opdracht, klikt u op de knop {{< AppElement type="buttonSecondary" >}}cURL import{{< /AppElement >}} om de importwizard te openen.
2. Klik op de knop {{< AppElement type="buttonPrimary" >}}Volgende{{< /AppElement >}}.
3. Plak uw cURL-commandoregel statement(s). Stel dat we bijvoorbeeld een stap willen maken op basis van cURL-statement:

```
curl -X POST https://www.galacticresorts.com/api/Reservation -H "Content-Type: application/x-www-form-urlencoded" -u username:password -d "name=Joe&productId=97f8fcc9-11b5-4d86-b208-ccb6d2be35e3&sols=5"
```

Dit is een request om een reservering te creëren op onze voorbeeldsite voor het testen van vakantieboekingen, [GalacticResorts.com](https://www.galacticresorts.com).

U kunt meerdere stappen tegelijk toevoegen door meerdere cURL-opdrachten te plakken.

4. Specificeer indien nodig het opdrachtformaat. In de meeste gevallen is 'Automatisch detecteren' echter voldoende.
5. Klik op de knop {{< AppElement type="buttonPrimary" >}}Volgende{{< /AppElement >}}.
6. Klik in de laatste stap van de wizard op de knop {{< AppElement type="button" >}}Stappen genereren{{< /AppElement >}}.

Het resultaat van de cURL-opdracht die in dit voorbeeld wordt genoemd, zou als volgt zijn:

![resultaat cURL import](/img/content/scr-msa-curl-import-result.min.png)

Het controleregeltype Multi-step API ondersteunt niet alle opties in de cURL-opdrachtregel. Niet-ondersteunde opties worden automatisch genegeerd, probeer de stap dus uit om te controleren of deze naar verwachting werkt.

### Response

Het tabblad Response bevat alle opties voor het uitvoeren van controles op responsdata (met behulp van Assertions) en het verwerken van die data ter voorbereiding op de volgende stap (met behulp van Variabelen).

![Tabblad Response](/img/content/scr-MSA-editor-response-tab.min.png)

#### Assertions

Het definiëren van uw stappen en het invoeren van de juiste data in deze stappen is de basis voor een bruikbare opzet. Het is echter ook belangrijk om naar de resultaten van elke stap te kijken. Alleen het aanroepen van een reeks URL’s is niet zinvol als ze niet de juiste resultaten terugsturen. Assertions helpen u bij deze gezondheidscontroles.

Assertions zijn controles die u kunt uitvoeren om te verifiëren dat de respons zich in een bepaalde stap gedraagt als verwacht, bijvoorbeeld, door zijn content te controleren of te verifiëren of het binnen een bepaalde hoeveelheid tijd is opgehaald. Net als bij variabelen, geeft u de bron voor de controle op, bijvoorbeeld een JSON property van de JSON response body, een XPath query op de XML response body, of zelfs alleen de statuscode van de response, de duur ervan of de lengte van de inhoud.

**Meer voorbeelden van Assertions**: lees onze [uitgebreide handleiding voor het definiëren van assertions]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}}).

#### Variabelen

Wanneer u multi-step scenario’s aan het opzetten bent, is het waarschijnlijk dat ten minste één van die stappen afhankelijk is van invoer die tijdens een vorige stap is opgehaald. Door die invoer vast te leggen, tijdelijk op te slaan en mee te nemen naar de volgende stappen, creëert u een natuurlijke progressie van verbonden stappen, zonder dat u enige code hoeft te schrijven.

Dat is precies wat u met variabelen kunt doen! Elke stap kan nieuwe variabelen maken en heeft toegang tot variabelen die door andere stappen zijn gemaakt, zodat u data kunt hergebruiken die eerder in het scenario zijn vastgelegd.

U kunt definiëren waar een variabele vandaan moet komen: waarschijnlijk een bepaalde waarde uit JSON- of XML-data, maar het vastleggen van response headers of zelfs van data van een redirect is ook mogelijk. Nadat een variabele is gedefinieerd, kunt u deze eenvoudig overal in uw multi-step-opzet gebruiken door er met zijn naam naar te verwijzen: {{< Code/Symbol type="variable" >}}{{my-variable}}{{< /Code/Symbol >}}.

**Meer voorbeelden van Variabelen**: [Variabelen definiëren en gebruiken]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}).

#### Maximaal aantal pogingen {id="msaretry"}

In sommige gevallen kan het zijn dat uw API enige tijd nodig heeft om een binnenkomende request te verwerken voordat hij kan reageren met de melding dat het is gelukt. Stel dat u bijvoorbeeld een bestand voor verwerking uploadt naar uw API. Tijdens de verwerking reageert de API op requests over de status met `{"result":"processing"}` in een JSON-body. Zodra de verwerking is voltooid, begint de API in plaats daarvan te reageren met `{"result":"success"}`. In dergelijke gevallen kunt u de controleregel configureren om de API te blijven peilen totdat deze met succes reageert door de instelling **Maximaal aantal pogingen** te gebruiken. 

Deze functie zorgt ervoor dat de controleregel de stap opnieuw doet als een of meer van de assertions (aannames) in de stap (zoals {{< Code/Symbol type="source" >}}Response body als JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}result{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is gelijk aan{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}success{{< /Code/Symbol >}} voor het hierboven genoemde voorbeeld) mislukt. U kunt instellen hoeveel keer de controleregel het opnieuw moet proberen, met een maximum van 50 keer. Houd er rekening mee dat het minimum aantal pogingen twee is, aangezien de initiële request al als de eerste poging telt.

Naast het aantal pogingen kunt u de wachttijd tussen deze pogingen instellen. De wachttijd tussen pogingen moet tussen 500 en 30000 ms liggen en is standaard ingesteld op 1000 ms. 

Voor elke stap kunt u een maximum aantal pogingen configureren in combinatie met een minimale wachttijd ertussen.

De controleregel zal de stap opnieuw blijven proberen ofwel totdat het maximum aantal pogingen is bereikt ofwel totdat elke assertion is geslaagd. Vanaf dat punt zal de controleregel gewoon verdergaan en de rest van de stappen in volgorde uitvoeren. Als het maximum aantal pogingen is bereikt en er nog steeds ten minste één assertion mislukt, rapporteert de controleregel een fout in het controleregel-log.

De kosten van de MSA-controleregel blijven gelijk, ongeacht het aantal pogingen.

## Configureer bestandsuploads

Met Multi-step API-controleregels kunt u bestanden uploaden vanuit [uw vault]({{< ref path="support/kb/account/vault" lang="nl" >}}) als onderdeel van een van uw request-stappen. Elke HTTP-stap die u configureert in de Multi-step API-controleregel die een request body bevat, kan een form-data- of binaire bestandsupload zijn of een gewone request met platte tekst. Bestanden worden verzonden als `multipart/form-data` of binaire inhoud. Volg deze stappen om een bestand als form-data toe te voegen:

1. [Upload het betreffende bestand]({{< ref path="support/kb/account/vault#file" lang="nl" >}}) naar uw vault. De maximale bestandsgrootte is 2 MB. 
2. Voeg in de instellingen van uw Multi-step API-controleregel een request-stap toe of gebruik een bestaande stap om het uploaden van het bestand uit te voeren. 
3. In het tabblad **Request** van de stap die het uploaden van het bestand moet uitvoeren, stelt u de request-methode in op *POST*, *PUT* of *PATCH* (afhankelijk van wat u nodig heeft) en vult u de request-URL in.
4. Selecteer onder **Request body** de optie *Bestand uploaden (als form-data)*. 
5. Klik op de knop {{< AppElement type="buttonSecondary" >}}Bestand uit de vault toevoegen{{< /AppElement >}} die verschijnt.
6. Kies het juiste bestand uit de Vault-bestandsuploadlijst en klik op de knop {{< AppElement type="button" >}}Selecteren{{< /AppElement >}}.
![Bestandsuploadkiezer](/img/content/scr_MSA_file-upload-picker.png)
7. Het is niet nodig om specifieke request headers toe te voegen. We stellen automatisch een request header in voor `Content-Length` en stellen `Content-Type: multipart/form-data` in met de juiste boundary (grens).
![Voorbeeld headers voor bestandsupload](/img/content/scr_MSA_file-upload-headers-example.png)

Als u een bestand wilt uploaden zonder dat Uptrends `Content-Disposition`-metadata toevoegt aan de request body, kunt u *Een bestand uploaden (als binair)* selecteren onder **Request body** bij stap 4 hierboven. We zullen nog steeds automatisch de juiste headers genereren die worden vermeld bij **Request headers**, maar zonder deze specifieke metadata aan de request toe te voegen. Op deze manier kunt u, als uw API bestanden verwacht die zijn geüpload als onbewerkte binaire data, deze nog steeds testen.

Houd er rekening mee dat uw API mogelijk een specifieke waarde voor de bestandsnaam verwacht. De request zal een automatisch geconstrueerde header **Content-Disposition** bevatten, die wat metadata bevat. De waarde voor deze header bevat een *name*-parameter. Standaard gebruiken we de bestandsnaam zoals die door u in de vault is gespecificeerd. Zorg ervoor dat de bestandsnaam die u specificeert wanneer u het bestand aan de vault toevoegt, overeenkomt met de waarde die wordt verwacht door uw API. Als uw API bijvoorbeeld verwacht dat het geüploade bestand de naam "afbeelding" heeft, moet u ervoor zorgen dat u "afbeelding" (zonder bestandsextensie) opgeeft als bestandsnaam in het juiste vault-item.

## Configureer een Wachtstap

Als u een reeks Request-stappen aan uw controleregel heeft toegevoegd, wordt elke stap uitgevoerd zodra de vorige stap is voltooid, zonder vertraging. Echter, deze onmiddellijke uitvoering kan voor sommige scenario’s iets te snel zijn.

Denk bijvoorbeeld aan een API-methode die vraagt een rapportbestand te genereren. De API start een backendproces dat het bestand genereert en de caller instrueert een tweede request te sturen om het nieuwe bestand te downloaden. Het genereren van het bestand kan zo’n twee seconden duren, dus de caller moet enkele seconden wachten voordat de tweede request wordt verstuurd. Wordt deze te snel verstuurd, dan zal de tweede request mislukken omdat het gegenereerde bestand nog niet gereed is.

Voor dit scenario is het belangrijk om te wachten voordat Multi-step API om de tweede request vraagt. Om een vertraging toe te voegen kunt u een afzonderlijke Wachtstap invoegen. Met een Wachtstap kunt u het aantal milliseconden opgeven dat moet worden vertraagd. Om bijvoorbeeld 3 seconden te wachten geeft u 3000 milliseconden op als de wachttijd. Het rapport bevat de extra wachttijd in de totale tijdsduur voor de controleregel.

Om een wachtstap toe te voegen klikt u gewoon op de knop {{< AppElement type="buttonSecondary" >}} Wachtstap toevoegen {{< /AppElement >}} en specificeert dan het aantal milliseconden dat u wilt wachten. Zo nodig kunt u de wachtstap naar de juiste plek in uw scenario verplaatsen met de knoppen Verplaats stap omhoog/omlaag.

De wachttijd voor een wachtstap is beperkt tot 60 seconden: een wachtstap is niet bedoeld voor het monitoren van een langlopende taak die enkele minuten of uren duurt. Als de controleregel de maximale totale uitvoertijd overschrijdt, stopt de controle met uitvoeren en rapporteert een fout.

Het toevoegen van een wachtstap aan uw controleregel kost u niets. Uptrends baseert de kosten van een Multi-step API-controleregel alleen op het aantal Request-stappen.

{{< callout >}} **Opmerking:** De duur van de uitvoering van alle stappen in uw controleregel mag in totaal niet langer zijn dan 4 minuten. Als het langer dan 4 minuten duurt om de controleregel van begin tot eind uit te voeren, is het resultaat van de controleregelcheck een fout. Overweeg in dergelijke gevallen om uw requests, indien mogelijk, over meerdere controleregels uit te spreiden. {{< /callout >}}

## Resultaten, fouten en alerts van een multi-step-controleregel

Multi-step API-controleregels gedragen zich hetzelfde als elke andere controleregel. Elke controle verschijnt in de controleregel log en geeft uitgebreide informatie weer over elke afzonderlijke stap. Voor elke stap bestaat deze informatie uit:

- **Totale duur** van de stap (in milliseconden).
- **URL** die werd uitgevoerd tijdens die stap.
- **HTTP status code** die is geretourneerd.
- Resultaat voor iedere **assertion** (slagen of mislukken).
- **Request headers en content** die we hebben verzonden.
- **Response headers en content** die we hebben ontvangen.

Als er tijdens een van de stappen een probleem optreedt, of als een van de assertions die u heeft gedefinieerd mislukt, zal de controleregel mislukken en een fout rapporteren. Zoals gewoonlijk kunnen deze fouten alerts genereren op basis van uw alertdefinities.