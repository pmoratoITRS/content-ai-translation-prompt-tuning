{
  "hero": {
    "title": "Multi-step API monitoring configureren"
  },
  "title": "Multi-step API monitoring configureren",
  "summary": "Stapsgewijze instructies voor het configureren van Multi-step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Om uw API effectief te monitoren moet u vaak een reeks HTTP-requests creëren, waarbij elke request data ophaalt uit een eerdere request om de volgende reeks taken uit te voeren. Met de **Multi-step API-controleregel** kunt u meerdere HTTP-requests instellen, [variabelen]([LINK_URL_1]) definiëren, [door de gebruiker gedefinieerde functies]([LINK_URL_2]) maken, [aangepaste scripting]([LINK_URL_3]) instellen en nog veel meer.

Hier volgen enkele mogelijke scenario's waarom u een reeks HTTP-requests zou moeten uitvoeren:

- Uw API vereist geverifieerde toegang: een API-client moet eerst zijn inloggegevens verifiëren om toegang te krijgen tot HTTP-methoden (bijvoorbeeld met behulp van de OAuth-verificatie).
- U wilt een functioneel scenario in uw API testen dat bestaat uit meerdere stappen die meestal door uw eindgebruikers in een bepaalde volgorde worden uitgevoerd.
- Uw HTTP-request retourneert een redirect naar een andere URL en u wilt het gedrag van die respons inspecteren voordat u de redirect volgt.

## Functies van de Multi-step API-controleregel

De **Multi-step API-controleregel** geeft u volledige controle over de complete inhoud van de HTTP-request. De functies omvatten:

- Stel de HTTP method, URL, request headers en request body in voor iedere request.
- [Voeg authenticatie toe (Basic/NTLM/Digest/OAuth)]([LINK_URL_4]) of [voeg cliëntcertificaten toe]([LINK_URL_5]) om toegang te verkrijgen tot beveiligde API's.
- [Definieer assertions (controles) voor iedere response]([LINK_URL_6]) voor het verifiëren van de HTTP-statuscode, inhoudcontroles (gebaseerd op platte tekst, JSON- of XML-content), requestduur en meer.
- Extraheer inhoud uit de response body, response headers, cookies en [sla ze op in variabelen]([LINK_URL_7]). Dergelijke variabelen kunnen in latere stappen gebruikt worden om nieuwe URL's, request headers enzovoort te bouwen.
- Gebruik globale definities zoals [voorgedefinieerde variabelen]([LINK_URL_8]), [door de gebruiker gedefinieerde functies]([LINK_URL_9]), [vrije API-kengetallen]([LINK_URL_10]) en [hashing en codering]([LINK_URL_11]).

Deze functies helpen u ervoor te zorgen dat uw API correct functioneert en binnen de door u gespecificeerde limieten presteert. De stapsgewijze aanpak stelt u in staat om zeer krachtige scenario's op te zetten zonder complexiteit toe te voegen. Zolang u maar weet hoe uw API zich moet gedragen, hoeft u niet te kunnen programmeren om aan de slag te gaan met API-monitoring.

## Creëer een multi-step API-controleregel

Een multi-step API-controleregel toevoegen:

1. Ga naar [SHORTCODE_7] API > API-controleregels beheren [SHORTCODE_8] en klik op de [SHORTCODE_9][SHORTCODE_10] knop.
2. Klik in het pop-upvenster *Kies een controleregel type* op *Multi-step API* en klik op de knop [SHORTCODE_11] Kiezen [SHORTCODE_12].  
3. Zodra de controleregel is gecreëerd, geeft u uw controleregel een *Naam*.  
4. Stel het *Controle-interval* in. Uw [controle-interval]([LINK_URL_12]) is de tijd tussen het einde van de ene controle en het begin van de volgende.
5. Ga naar het tabblad [SHORTCODE_13] Stappen [SHORTCODE_14] om de details voor elke stap in te voeren.

Uw nieuwe controleregel begint met één (lege) stap. U kunt het volgende doen:
- Klik op [SHORTCODE_15] Request-stap toevoegen [SHORTCODE_16] om extra stappen toe te voegen.
- Klik op het **>**-pictogram naast een stap om stapdetails uit te vouwen en te bewerken.
- Klik op het pictogram **Stap dupliceren** om een kopie te maken van een bestaande stap. 
- Klik op het **X**-pictogram om een stap te verwijderen.
- Gebruik de knoppen *Verplaats stap omhoog* en *Verplaats stap omlaag* om de positie van de stappen te verplaatsen.

![Voorbeeld MSA-stappen]([LINK_URL_13])

## Configureer een Request-stap

Als u de visuele stap-editor bekijkt, ziet u het tabblad [SHORTCODE_17] Request [SHORTCODE_18]. Een stap in Multi-step API monitoring bestaat uit één round-trip call naar de API (bijvoorbeeld één request en één response). Binnen elke stap kunt u uw request definiëren en Uptrends vertellen hoe de response moet worden afgehandeld. Elke Multi-step API begint met één lege stap.

### Request

![Details tabblad Request]([LINK_URL_14])

Het tabblad **Request** bevat alle data die nodig zijn om de daadwerkelijke HTTP request in de stap uit te voeren. Doe ten minste het volgende:

1. Kies de juiste HTTP method: **GET**, **POST**, **PUT**, **PATCH**, **DELETE**, **HEAD** of **OPTIONS**. Als u een andere methode nodig heeft, [neem dan contact met ons op]([LINK_URL_15]).
2. Vul de URL in voor de request. Gebruik een volledig gekwalificeerde URL, inclusief het schema ("[URL_1] of "[URL_2]), de domeinnaam en het pad voor uw API, en eventuele query string parameters die u wilt opnemen.

#### Request body

Wanneer u een POST-, PUT-, PATCH-, HEAD-, OPTIONS- of DELETE-request opgeeft, kunt u met het veld **Request body** specifieke data (payload) verzenden als onderdeel van de requestdefinitie. Bijvoorbeeld door een specifieke gebruikersnaam en wachtwoord te versturen om een nieuw gebruikersaccount te maken.

Hieronder staan de data-indelingen voor de request body waaruit u kunt kiezen:

- Platte tekst — hiermee kunt u platte teksten zonder opmaak versturen.
- Bestand uploaden (als form-data) — hiermee kunt u een bestand (zoals afbeeldingen en documenten uit de [Vault]([LINK_URL_16])) versturen in form-data-formaat.
- Bestand uploaden (als binary) — hiermee kunt u een bestand (zoals afbeeldingen en documenten uit de [Vault]([LINK_URL_17])) versturen in een raw binary data-formaat.
- Multi-part form — hiermee kunt u meerdere types inhoud in verschillende formaten (zoals platte-tekstinvoer of bestanden die zijn opgehaald uit de [Vault]([LINK_URL_18])) tegelijk versturen.

In de meeste gevallen en afhankelijk van het gekozen dataformaat, wordt de juiste [INLINE_CODE_1]- request header-waarde automatisch ingesteld (zoals [INLINE_CODE_2]) zodat de server uw data correct kan identificeren, lezen en verwerken. U kunt ook de request header [INLINE_CODE_3] opgeven, die in het volgende gedeelte van dit artikel wordt besproken.

#### Request headers [ANCHOR_1]

Een HTTP request bevat meestal enkele request headers om het formaat van de data die worden verzonden te specificeren, of om verder te beschrijven wat voor soort respons verwacht wordt. Bij het configureren van een request stap zult u merken dat bepaalde headers automatisch worden toegevoegd. Deze headers bestaan uit een standaardset, afhankelijk van het type request dat u doet (GET-requests hebben bijvoorbeeld een andere set headers dan POST-requests). Om een standaard header te overschrijven voegt u simpelweg een nieuwe header toe met precies dezelfde naam als de bestaande, maar met een andere waarde.

[SHORTCODE_1] **Opmerking:** Voor optimalisatiedoeleinden is **Connection: Keep-Alive** verwijderd uit de lijst met standaard request headers. In het achtergrondproces is de request header al het standaardgedrag voor HTTP/1.1 en wordt niet langer ondersteund voor HTTP/2 en HTTP/3. [SHORTCODE_2]

U kunt ook nieuwe headers toevoegen door deze stappen te volgen:

1. Klik op de knop [SHORTCODE_19]Request header toevoegen[SHORTCODE_20] om een request header key en waarde toe te voegen.
2. Voer Content-Type in als de header key.
3. De juiste header waarde is afhankelijk van de data die u verzendt. De meest voorkomende content types zijn [INLINE_CODE_4] voor JSON-data, [INLINE_CODE_5] voor XML-data en [INLINE_CODE_6] voor webformulierendata.

Evenzo, als uw API vereist dat u authenticatie opneemt, voegt u een [INLINE_CODE_7] header toe samen met de juiste data in het veld Waarde.

![Voorbeelden van request headers]([LINK_URL_19])

De afbeelding hierboven toont een voorbeeld van een request stap. Let op het volgende:

- Het is een POST request naar [INLINE_CODE_8]
- De standaard headers die voor deze request zijn ingesteld, zijn:
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
- De waarden voor de header [INLINE_CODE_11] wordt bepaald bij het verzenden van de request.
- Handmatige headers [INLINE_CODE_12] en [INLINE_CODE_13] zijn toegevoegd om respectievelijk het dataformaat te specificeren en de benodigde inloggegevens te verstrekken.
- Standaard [INLINE_CODE_14] is overschreven.
- De request body bevat wat [INLINE_CODE_15]-inhoud, verwijzend naar enkele [variabelen]([LINK_URL_20]).

#### Authenticatie

Veel API’s zijn beveiligd en alleen toegankelijk door inloggegevens te verstrekken. Als uw API gebruikmaakt van authenticatie op het HTTP-protocolniveau, kies dan uw type authenticatie (Basic, NTLM or Digest) en vul de bijbehorende gebruikersnaam en wachtwoord in. Als alternatief kunt u een op OAuth gebaseerde authenticatie instellen met afzonderlijke stappen. [Meer informatie over het instellen van ingebouwde of aangepaste authenticatie]([LINK_URL_21]).

#### Gebruik inloggegevens uit de vault

Het is mogelijk om op elk punt verwijzingen naar [vault-inloggegevens]([LINK_URL_22]) te gebruiken als onderdeel van de request body, request headers of als de waarde voor uw gebruikersnaam/wachtwoord onder *Authenticatie*. Gebruik de volgende syntaxis om naar een vault-item te verwijzen: [INLINE_CODE_16] of [INLINE_CODE_17] afhankelijk van welke waarde vereist is. Om de [INLINE_CODE_18] te vinden navigeert u naar het vault-item met de inloggegevens en kopieert u vervolgens het laatste deel van de URL in de URL-balk van uw browser.

![Voorbeelden van verwijzingen naar vault-items]([LINK_URL_23])

#### Stel de TLS-versies in

De Transport Layer Security (TLS) is een beveiligingsprotocol dat verbindingen tussen websites en servers authenticeert, versleutelt en beschermt. Door het selectievakje *Alleen specifieke TLS-versies toestaan* aan te vinken in uw MSA-controleregel, kunt u specifieke TLS-versies selecteren tijdens de TLS-handshake voor HTTP-verbinding. U kunt het selectievakje ook uitschakelen als er geen beperkingen nodig zijn.

Alle [Uptrends-controlestations]([LINK_URL_24]) ondersteunen TLS 1.1 en TLS 1.2. Door de optie TLS 1.3 te selecteren, wordt de selectie van controlestations beperkt tot die met TLS 1.3-functionaliteit. Hoewel TLS 1.1 nog steeds beschikbaar is, wordt het niet aanbevolen.

![Selectievakje TLS-versies in MSA-controleregels]([LINK_URL_25])

#### Stel de HTTP-versie in

Met de optie **HTTP-versie** kunt u bepalen welke HTTP-versie de controlestationservers gebruiken bij het doen van requests. Gebruik deze optie om ervoor te zorgen dat de servers effectief communiceren met de API op het gebied van compatibiliteit, prestaties en beveiliging.

![HTTP-versie]([LINK_URL_26])

Standaard is de optie **HTTP-versie** niet aangevinkt, wat betekent dat de server automatisch de hoogste ondersteunde HTTP-versie gebruikt die beschikbaar is, met een fallback niet lager dan HTTP/1.1.

Momenteel is HTTP/3 beschikbaar op geselecteerde controlestationlocaties en de ondersteuning wordt binnenkort uitgebreid naar meer locaties.

[SHORTCODE_3] **Opmerking:** Met de HTTP-versie kunt u slechts één versie selecteren, terwijl de **TLS-versie(s)** de selectie van meerdere versies ondersteunen.
[SHORTCODE_4]

### Importeer cURL requests [ANCHOR_2]

Het is ook mogelijk om cURL requests rechtstreeks te importeren om uw stappen te creëren, zonder ze handmatig opnieuw te hoeven maken. Dit doet u als volgt:

1. In de **Visuele stap-editor** (in het tabblad [SHORTCODE_21]Stappen[SHORTCODE_22] van de controleregelinstellingen) van de Multi-step API-controleregel waarin u een stap wilt importeren op basis van een curl-opdracht, klikt u op de knop [SHORTCODE_23]cURL import[SHORTCODE_24] om de importwizard te openen.
2. Klik op de knop [SHORTCODE_25]Volgende[SHORTCODE_26].
3. Plak uw cURL-commandoregel statement(s). Stel dat we bijvoorbeeld een stap willen maken op basis van cURL-statement:

[CODE_BLOCK_1]

Dit is een request om een reservering te creëren op onze voorbeeldsite voor het testen van vakantieboekingen, [GalacticResorts.com]([LINK_URL_27]).

U kunt meerdere stappen tegelijk toevoegen door meerdere cURL-opdrachten te plakken.

4. Specificeer indien nodig het opdrachtformaat. In de meeste gevallen is 'Automatisch detecteren' echter voldoende.
5. Klik op de knop [SHORTCODE_27]Volgende[SHORTCODE_28].
6. Klik in de laatste stap van de wizard op de knop [SHORTCODE_29]Stappen genereren[SHORTCODE_30].

Het resultaat van de cURL-opdracht die in dit voorbeeld wordt genoemd, zou als volgt zijn:

![resultaat cURL import]([LINK_URL_28])

Het controleregeltype Multi-step API ondersteunt niet alle opties in de cURL-opdrachtregel. Niet-ondersteunde opties worden automatisch genegeerd, probeer de stap dus uit om te controleren of deze naar verwachting werkt.

### Response

Het tabblad Response bevat alle opties voor het uitvoeren van controles op responsdata (met behulp van Assertions) en het verwerken van die data ter voorbereiding op de volgende stap (met behulp van Variabelen).

![Tabblad Response]([LINK_URL_29])

#### Assertions

Het definiëren van uw stappen en het invoeren van de juiste data in deze stappen is de basis voor een bruikbare opzet. Het is echter ook belangrijk om naar de resultaten van elke stap te kijken. Alleen het aanroepen van een reeks URL’s is niet zinvol als ze niet de juiste resultaten terugsturen. Assertions helpen u bij deze gezondheidscontroles.

Assertions zijn controles die u kunt uitvoeren om te verifiëren dat de respons zich in een bepaalde stap gedraagt als verwacht, bijvoorbeeld, door zijn content te controleren of te verifiëren of het binnen een bepaalde hoeveelheid tijd is opgehaald. Net als bij variabelen, geeft u de bron voor de controle op, bijvoorbeeld een JSON property van de JSON response body, een XPath query op de XML response body, of zelfs alleen de statuscode van de response, de duur ervan of de lengte van de inhoud.

**Meer voorbeelden van Assertions**: lees onze [uitgebreide handleiding voor het definiëren van assertions]([LINK_URL_30]).

#### Variabelen

Wanneer u multi-step scenario’s aan het opzetten bent, is het waarschijnlijk dat ten minste één van die stappen afhankelijk is van invoer die tijdens een vorige stap is opgehaald. Door die invoer vast te leggen, tijdelijk op te slaan en mee te nemen naar de volgende stappen, creëert u een natuurlijke progressie van verbonden stappen, zonder dat u enige code hoeft te schrijven.

Dat is precies wat u met variabelen kunt doen! Elke stap kan nieuwe variabelen maken en heeft toegang tot variabelen die door andere stappen zijn gemaakt, zodat u data kunt hergebruiken die eerder in het scenario zijn vastgelegd.

U kunt definiëren waar een variabele vandaan moet komen: waarschijnlijk een bepaalde waarde uit JSON- of XML-data, maar het vastleggen van response headers of zelfs van data van een redirect is ook mogelijk. Nadat een variabele is gedefinieerd, kunt u deze eenvoudig overal in uw multi-step-opzet gebruiken door er met zijn naam naar te verwijzen: [SHORTCODE_37]{{my-variable}}[SHORTCODE_38].

**Meer voorbeelden van Variabelen**: [Variabelen definiëren en gebruiken]([LINK_URL_31]).

#### Maximaal aantal pogingen [ANCHOR_3]

In sommige gevallen kan het zijn dat uw API enige tijd nodig heeft om een binnenkomende request te verwerken voordat hij kan reageren met de melding dat het is gelukt. Stel dat u bijvoorbeeld een bestand voor verwerking uploadt naar uw API. Tijdens de verwerking reageert de API op requests over de status met [INLINE_CODE_19] in een JSON-body. Zodra de verwerking is voltooid, begint de API in plaats daarvan te reageren met [INLINE_CODE_20]. In dergelijke gevallen kunt u de controleregel configureren om de API te blijven peilen totdat deze met succes reageert door de instelling **Maximaal aantal pogingen** te gebruiken. 

Deze functie zorgt ervoor dat de controleregel de stap opnieuw doet als een of meer van de assertions (aannames) in de stap (zoals [SHORTCODE_39]Response body als JSON[SHORTCODE_40] [SHORTCODE_41]result[SHORTCODE_42] [SHORTCODE_43]Is gelijk aan[SHORTCODE_44] [SHORTCODE_45]success[SHORTCODE_46] voor het hierboven genoemde voorbeeld) mislukt. U kunt instellen hoeveel keer de controleregel het opnieuw moet proberen, met een maximum van 50 keer. Houd er rekening mee dat het minimum aantal pogingen twee is, aangezien de initiële request al als de eerste poging telt.

Naast het aantal pogingen kunt u de wachttijd tussen deze pogingen instellen. De wachttijd tussen pogingen moet tussen 500 en 30000 ms liggen en is standaard ingesteld op 1000 ms. 

Voor elke stap kunt u een maximum aantal pogingen configureren in combinatie met een minimale wachttijd ertussen.

De controleregel zal de stap opnieuw blijven proberen ofwel totdat het maximum aantal pogingen is bereikt ofwel totdat elke assertion is geslaagd. Vanaf dat punt zal de controleregel gewoon verdergaan en de rest van de stappen in volgorde uitvoeren. Als het maximum aantal pogingen is bereikt en er nog steeds ten minste één assertion mislukt, rapporteert de controleregel een fout in het controleregel-log.

De kosten van de MSA-controleregel blijven gelijk, ongeacht het aantal pogingen.

## Configureer bestandsuploads

Met Multi-step API-controleregels kunt u bestanden uploaden vanuit [uw vault]([LINK_URL_32]) als onderdeel van een van uw request-stappen. Elke HTTP-stap die u configureert in de Multi-step API-controleregel die een request body bevat, kan een form-data- of binaire bestandsupload zijn of een gewone request met platte tekst. Bestanden worden verzonden als [INLINE_CODE_21] of binaire inhoud. Volg deze stappen om een bestand als form-data toe te voegen:

1. [Upload het betreffende bestand]([LINK_URL_33]) naar uw vault. De maximale bestandsgrootte is 2 MB. 
2. Voeg in de instellingen van uw Multi-step API-controleregel een request-stap toe of gebruik een bestaande stap om het uploaden van het bestand uit te voeren. 
3. In het tabblad **Request** van de stap die het uploaden van het bestand moet uitvoeren, stelt u de request-methode in op *POST*, *PUT* of *PATCH* (afhankelijk van wat u nodig heeft) en vult u de request-URL in.
4. Selecteer onder **Request body** de optie *Bestand uploaden (als form-data)*. 
5. Klik op de knop [SHORTCODE_31]Bestand uit de vault toevoegen[SHORTCODE_32] die verschijnt.
6. Kies het juiste bestand uit de Vault-bestandsuploadlijst en klik op de knop [SHORTCODE_33]Selecteren[SHORTCODE_34].
![Bestandsuploadkiezer]([LINK_URL_34])
7. Het is niet nodig om specifieke request headers toe te voegen. We stellen automatisch een request header in voor [INLINE_CODE_22] en stellen [INLINE_CODE_23] in met de juiste boundary (grens).
![Voorbeeld headers voor bestandsupload]([LINK_URL_35])

Als u een bestand wilt uploaden zonder dat Uptrends [INLINE_CODE_24]-metadata toevoegt aan de request body, kunt u *Een bestand uploaden (als binair)* selecteren onder **Request body** bij stap 4 hierboven. We zullen nog steeds automatisch de juiste headers genereren die worden vermeld bij **Request headers**, maar zonder deze specifieke metadata aan de request toe te voegen. Op deze manier kunt u, als uw API bestanden verwacht die zijn geüpload als onbewerkte binaire data, deze nog steeds testen.

Houd er rekening mee dat uw API mogelijk een specifieke waarde voor de bestandsnaam verwacht. De request zal een automatisch geconstrueerde header **Content-Disposition** bevatten, die wat metadata bevat. De waarde voor deze header bevat een *name*-parameter. Standaard gebruiken we de bestandsnaam zoals die door u in de vault is gespecificeerd. Zorg ervoor dat de bestandsnaam die u specificeert wanneer u het bestand aan de vault toevoegt, overeenkomt met de waarde die wordt verwacht door uw API. Als uw API bijvoorbeeld verwacht dat het geüploade bestand de naam "afbeelding" heeft, moet u ervoor zorgen dat u "afbeelding" (zonder bestandsextensie) opgeeft als bestandsnaam in het juiste vault-item.

## Configureer een Wachtstap

Als u een reeks Request-stappen aan uw controleregel heeft toegevoegd, wordt elke stap uitgevoerd zodra de vorige stap is voltooid, zonder vertraging. Echter, deze onmiddellijke uitvoering kan voor sommige scenario’s iets te snel zijn.

Denk bijvoorbeeld aan een API-methode die vraagt een rapportbestand te genereren. De API start een backendproces dat het bestand genereert en de caller instrueert een tweede request te sturen om het nieuwe bestand te downloaden. Het genereren van het bestand kan zo’n twee seconden duren, dus de caller moet enkele seconden wachten voordat de tweede request wordt verstuurd. Wordt deze te snel verstuurd, dan zal de tweede request mislukken omdat het gegenereerde bestand nog niet gereed is.

Voor dit scenario is het belangrijk om te wachten voordat Multi-step API om de tweede request vraagt. Om een vertraging toe te voegen kunt u een afzonderlijke Wachtstap invoegen. Met een Wachtstap kunt u het aantal milliseconden opgeven dat moet worden vertraagd. Om bijvoorbeeld 3 seconden te wachten geeft u 3000 milliseconden op als de wachttijd. Het rapport bevat de extra wachttijd in de totale tijdsduur voor de controleregel.

Om een wachtstap toe te voegen klikt u gewoon op de knop [SHORTCODE_35] Wachtstap toevoegen [SHORTCODE_36] en specificeert dan het aantal milliseconden dat u wilt wachten. Zo nodig kunt u de wachtstap naar de juiste plek in uw scenario verplaatsen met de knoppen Verplaats stap omhoog/omlaag.

De wachttijd voor een wachtstap is beperkt tot 60 seconden: een wachtstap is niet bedoeld voor het monitoren van een langlopende taak die enkele minuten of uren duurt. Als de controleregel de maximale totale uitvoertijd overschrijdt, stopt de controle met uitvoeren en rapporteert een fout.

Het toevoegen van een wachtstap aan uw controleregel kost u niets. Uptrends baseert de kosten van een Multi-step API-controleregel alleen op het aantal Request-stappen.

[SHORTCODE_5] **Opmerking:** De duur van de uitvoering van alle stappen in uw controleregel mag in totaal niet langer zijn dan 4 minuten. Als het langer dan 4 minuten duurt om de controleregel van begin tot eind uit te voeren, is het resultaat van de controleregelcheck een fout. Overweeg in dergelijke gevallen om uw requests, indien mogelijk, over meerdere controleregels uit te spreiden. [SHORTCODE_6]

## Resultaten, fouten en alerts van een multi-step-controleregel

Multi-step API-controleregels gedragen zich hetzelfde als elke andere controleregel. Elke controle verschijnt in de controleregel log en geeft uitgebreide informatie weer over elke afzonderlijke stap. Voor elke stap bestaat deze informatie uit:

- **Totale duur** van de stap (in milliseconden).
- **URL** die werd uitgevoerd tijdens die stap.
- **HTTP status code** die is geretourneerd.
- Resultaat voor iedere **assertion** (slagen of mislukken).
- **Request headers en content** die we hebben verzonden.
- **Response headers en content** die we hebben ontvangen.

Als er tijdens een van de stappen een probleem optreedt, of als een van de assertions die u heeft gedefinieerd mislukt, zal de controleregel mislukken en een fout rapporteren. Zoals gewoonlijk kunnen deze fouten alerts genereren op basis van uw alertdefinities.