{
  "hero": {
    "title": "API changelog"
  },
  "title": "API changelog",
  "summary": "Bekijk de wijzigingen, updates en verbeteringen voor de Uptrends API",
  "url": "[URL_BASE_TOPICS]api/changelog",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "type": "[FRONTMATTER_TYPE]"
}

{{[HTML_TAG_1]}}

Uptrends' API zal in de loop van de tijd worden verbeterd en uitgebreid. We zullen nieuwe eindpunten en methoden toevoegen voor nieuwe functionaliteit.

Bij het toevoegen van nieuwe functionaliteit streven wij ernaar achterwaarts compatibel te blijven. Soms is verandering echter onvermijdelijk en is een nieuwe versie van de API mogelijk niet compatibel met wat u tot nu toe heeft gecodeerd en gebruikt. Bekijk de API Changelog regelmatig om op de hoogte te blijven van alle wijzigingen en waar nodig op wijzigingen te reageren.

Als u de documentatie van de API zoekt, bekijk dan de artikelen in de categorie [Uptrends' API]([LINK_URL_1]).

Bent u ook geïnteresseerd in de wijzigingen in de Uptrends-app, bekijk dan de [algemene changelog]([LINK_URL_2]).

## Mei 2025

### Aankomende belangrijke wijziging: verwijdering van API-velden

Als onderdeel van onze voortdurende inspanningen om de Uptrends API te optimaliseren, worden specifieke velden in de volgende [Monitor]([LINK_URL_3])-eindpunten met ingang van **27 augustus 2025** verwijderd:

- [INLINE_CODE_1] en [INLINE_CODE_2] [INLINE_CODE_3]
- [INLINE_CODE_4], [INLINE_CODE_5] en [INLINE_CODE_6] [INLINE_CODE_7]
- [INLINE_CODE_8] en [INLINE_CODE_9] [INLINE_CODE_10]

De volgende verouderde velden worden nu behandeld als [Types foutcondities]([LINK_URL_4]) onder de array [INLINE_CODE_11]. Gerelateerde velden worden samengevoegd tot één entry, ter vervanging van hun eerdere gebruik als individuele velden:

| Verouderde velden | Vervangende velden |
|--|--|
| [INLINE_CODE_12], [INLINE_CODE_13]| [SHORTCODE_1] [LoadTimeLimit1]([LINK_URL_5]) |
| [INLINE_CODE_14], [INLINE_CODE_15] | [LoadTimeLimit2]([LINK_URL_6]) |
|[INLINE_CODE_16], [INLINE_CODE_17] | [TotalMaxBytes]([LINK_URL_7]) |
|[INLINE_CODE_18], [INLINE_CODE_19] | [TotalMinBytes]([LINK_URL_8]) | 
|[INLINE_CODE_20], [INLINE_CODE_21] | [PageElementMaxSizeWithPercentage]([LINK_URL_9]) |
|[INLINE_CODE_22], [INLINE_CODE_23] | [PageElementFailedWithPercentage]([LINK_URL_10])
|[INLINE_CODE_24], [INLINE_CODE_25] | [HttpStatus]([LINK_URL_11]) |

Hieronder ziet u een voorbeeld van de bijgewerkte API-respons. Het is raadzaam uw API-aanroepen aan te passen om de [INLINE_CODE_26]-array te gebruiken. Dit is afgestemd op de nieuwste API-structuur en zorgt voor correcte API-functionaliteit.

[CODE_BLOCK_1]

### Update Persoonlijk Controlestationstatus

Het eindpunt [INLINE_CODE_27] retourneert nu het veld [INLINE_CODE_28], dat alle waarschuwingsinformatie bevat die is gekoppeld aan het controlestation van de server. Raadpleeg voor meer informatie de Engelstalige [Uptrends API v4 Private location Checkpoint health-documentatie]([LINK_URL_12]).

## April 2025

### Introductie van de Persoonlijke locaties API

Er is een nieuwe set API-eindpunten toegevoegd om u te helpen uw Persoonlijke locaties-configuratie te beheren, inclusief status- en controlestationinformatie. Raadpleeg voor meer informatie de [Uptrends API v4 Persoonlijke locaties-documentatie]([LINK_URL_13]).

## Maart 2025

### Update Monitor Group API 

Het eindpunt [INLINE_CODE_29] retourneert nu het aantal gebruikte credits per [controleregeltype]([LINK_URL_14]):
- [INLINE_CODE_30] — retourneert het aantal credits dat wordt gebruikt voor [Uptime- of Basiscontroleregels]([LINK_URL_15]).
- [INLINE_CODE_31] — retourneert het aantal credits dat wordt gebruikt voor [Browser- of Full Page Check (FPC)-controleregels]([LINK_URL_16]).
- [INLINE_CODE_32] — retourneert het aantal credits dat wordt gebruikt voor [Transactiecontroleregels]([LINK_URL_17]).
- [INLINE_CODE_33] — retourneert het aantal credits dat wordt gebruikt voor [Multi-step API (MSA)-]([LINK_URL_18]) en [Postman-]([LINK_URL_19])controleregels.

Voorheen retourneerde de MonitorGroup API alleen het totale aantal credits dat beschikbaar was voor de groep voor elke controleregelcategorie. Nu retourneert het ook het aantal credits dat in de groep wordt gebruikt voor elke controleregelcategorie.

## Februari 2025

### Update Cursor-parameterwaarde 

De API Cursor-parameter is een tekenreekswaarde die werkt als aanwijzer om data uit de API-respons te doorlopen.

Cursors zijn nu bijgewerkt naar een langere tekenreeksindeling om veiligere dataverwerking te garanderen. Alle nieuw gecreëerde cursors volgen nu het nieuwe formaat en de in het oude formaat gemaakte cursors blijven werken tot 1 april 2025. Na deze periode zijn oude cursors niet meer beschikbaar voor gebruik. Het wordt aanbevolen om nieuwe cursorwaarden te genereren om ze up-to-date te houden en te laten werken zoals verwacht.

Merk op dat de Cursor-parameter beschikbaar is in de eindpunten [MonitorCheck API]([LINK_URL_20]) en Alert API.

## Januari 2025

### Update Monitor API

Het eindpunt [INLINE_CODE_34] retourneert nu de [INLINE_CODE_35], die de datum en tijd bevat waarop de controleregel voor het laatst is bijgewerkt. Voorheen kon alleen de [INLINE_CODE_36] worden opgehaald uit de Monitor API.

## November 2024

### Update VaultItem

De [INLINE_CODE_37], [INLINE_CODE_38] en [INLINE_CODE_39] accepteren nu het veld [INLINE_CODE_40] bij het bijwerken of creëren van het vault-item [Configuratie eenmalig wachtwoord]([LINK_URL_21]). Dit nieuwe veld accepteert *Hex* of *Base32* als tekenreekswaarden. De *Base32*-indeling is de standaard codeermethode als het veld [INLINE_CODE_41] niet is gespecificeerd.

## September 2024

### Update Vault-item

De [INLINE_CODE_42] retourneert nu een extra data-item, [INLINE_CODE_43] dat details retourneert over welke items of controleregels elk vault-item gebruiken.

## Augustus 2024

### Checkpoint API

Het API-eindpunt [INLINE_CODE_44] retourneert nu ook persoonlijke-locatieservers.

### Update VaultItem 

Het eindpunt [INLINE_CODE_45] kan nu voor elk vault-item dezelfde mate van details retourneren, vergelijkbaar met hoe details worden geretourneerd voor een enkel item in een [INLINE_CODE_46].

## Juni 2024

### Belangrijke wijziging: de /Register API voor SSO-only operators

De Uptrends API vereist [registratie]([LINK_URL_22]) voordat deze kan worden gebruikt. Operators kunnen een set API-specifieke inloggegevens creëren, op basis van hun reguliere Uptrends-inloggegevens. Er zijn twee manieren om een set API-inloggegevens te registreren:

- Operators kunnen gebruikmaken van de reguliere Uptrends-interface en een API-gebruiker toevoegen via het tabblad [SHORTCODE_2]API management[SHORTCODE_3] in hun operatorinstellingen.
- Operators kunnen zich ook registreren voor inloggegevens in de API zelf, via een request [INLINE_CODE_47] door hun reguliere Uptrends-inloggegevens te verstrekken.

Vanaf deze update kunnen operators die alleen [kunnen inloggen met Single sign-on (SSO)]([LINK_URL_23]) niet langer proberen gebruik te maken van deze tweede optie voor het registreren van API-inloggegevens, aangezien ze geen 'reguliere' Uptrends-inloggegevens hebben om te gebruiken. 

In dergelijke gevallen raden we aan een apart operatoraccount aan te maken en dat te gebruiken om te registreren voor API-inloggegevens. 

## Oktober 2023

### Belangrijke wijziging: statistieken voor het laden van pagina's voor browsergebaseerde monitoring

**Opmerking:** Het volgende is een **belangrijke wijziging** in de *MonitorCheck* API. De wijziging gaat live op **woensdag 8 november**.

De Uptrends [MonitorCheck API]([LINK_URL_24]) kan worden gebruikt om gedetailleerde informatie op te halen over individuele controleregelchecks. Voor browsergebaseerde monitoring kan de [watervalgrafiek]([LINK_URL_25]) worden opgehaald via de call [INLINE_CODE_48], die alle watervalmetingen retourneert, inclusief [Core Web Vitals]([LINK_URL_26]) en [W3C Navigatietijden]([LINK_URL_27]), als die aanwezig zijn in het controleresultaat. 

Momenteel retourneert de MonitorCheck API Core Web Vitals en W3C Navigatietijden in twee afzonderlijke JSON-objecten: [INLINE_CODE_49] en [INLINE_CODE_50]. Voortaan zullen deze afzonderlijke objecten als volgt worden gecombineerd tot één enkele array, [INLINE_CODE_51]:

[CODE_BLOCK_2]


### Variabelen in alertdefinities specificeren via de API

Bij het configureren van [alerting]([LINK_URL_28]) via een [aanpasbare integratie]([LINK_URL_29]) in Uptrends kunnen operators de gebruikersinterface gebruiken om bepaalde vereiste variabelen te specificeren [in het escalatieniveau van de alertdefinitie]([LINK_URL_30]) in plaats van in de integratieopties. Hierdoor kunnen gebruikers één enkele integratie voor verschillende scenario's gebruiken, zoals het versturen van alerts voor verschillende sets controleregels naar verschillende teams, maar met dezelfde berichtinhoud.

Wanneer de optie om variabelen te specificeren in het escalatieniveau is geselecteerd in de integratie-instellingen, moeten de variabelen in plaats daarvan worden geconfigureerd wanneer de integratie is ingesteld voor gebruik in de instellingen van de alertdefinitie. Om dit te doen verschijnt er een extra tekstveld in de integratieselectielijst in de alertdefinitie-instellingen. 

Tot nu toe was deze optie niet beschikbaar bij het configureren van alertdefinities via de API. We hebben een nieuwe optie toegevoegd aan het [INLINE_CODE_52] request (waar u configureert welke integraties zijn gekoppeld aan elk escalatieniveau in de alertdefinitie). De nieuwe eigenschap wordt:

[CODE_BLOCK_3]

Deze eigenschap is het equivalent van deze optie in de gebruikersinterface van de applicatie:

![Integratievariabele configureren in alertdefinitie]([LINK_URL_31])


## September 2023

### Wijziging in IPv6-adressen van controlestations

Wanneer voorheen de checkpoint API werd gebruikt om controlestationinformatie op te halen, werden de IPv4-adressen van het controlestation weergegeven als een eenvoudige lijst in een array, terwijl de IPv6-adressen (indien van toepassing) een lijst met objecten waren. Zo werden de IP-adressen van het Amsterdamse controlestation voorheen als volgt weergegeven:

[CODE_BLOCK_4]

Uptrends heeft deze inconsistentie nu opgelost en retourneert de IPv6-adressen op dezelfde manier:

[CODE_BLOCK_5]

Houd er rekening mee dat als u het ophalen van IP-adressen van controlestations heeft geautomatiseerd, bijvoorbeeld voor whitelistdoeleinden, dit een **belangrijke wijziging** kan zijn.

## Januari 2023

Versie 3 van de API heeft per januari 2023 het einde van zijn levensduur bereikt en is uitgeschakeld. U kunt [de documentatie]([LINK_URL_32]) nog steeds vinden in onze knowledge base, maar versie 3 werkt niet meer. Als u bestaande scripts of procedures heeft die nog gebruikmaken van versie 3, zullen deze mislukken, en we raden u aan zo snel mogelijk over te stappen naar versie 4. Zie onze [upgradehandleiding]([LINK_URL_33]) voor meer informatie over het overstappen van API versie 3 naar versie 4.

**Update mei 2023:** De documentatie voor versie 3 van onze API is verwijderd en is niet meer toegankelijk. 

## December 2022

### Aanmaakdatuminformatie controleregel via de API

Het [/Monitor endpoint]([LINK_URL_34]) kan onder andere worden gebruikt om definities van de controleregels in uw account op te halen (via *GET /Monitor/{monitorGuid}*). De response bevat nu ook een [INLINE_CODE_53], die aangeeft wanneer de controleregel is gemaakt.


## November 2022

### Kleine wijzigingen in /Register endpoint

Zoals u misschien [in onze reguliere changelog]([LINK_URL_35]) heeft gelezen, hebben we in deze release de optie toegevoegd om [Uptrends API-inloggegevens te maken en in te trekken via de gebruikersinterface]([LINK_URL_36]). Om de Uptrends API v4 af te stemmen op de gebruikersinterface hebben we 2 nieuwe opties toegevoegd aan het /Register endpoint:

- Het is nu mogelijk om een optionele beschrijving op te geven bij het registreren van een nieuw API-account door het veld [INLINE_CODE_54] te gebruiken.
- Het is nu mogelijk om een API-account te creëren voor een andere operator wanneer de aanroepende operator voldoende rechten heeft door het veld [INLINE_CODE_55] te gebruiken.

## September 2022

### Aankomende wijziging: tijdstempels in de API response

Momenteel worden tijdstempels die deel uitmaken van de response voor elke [API v4]([LINK_URL_37]) call op een van de volgende twee manieren geconverteerd naar JSON:

- Het aantal milliseconden is gelijk aan 0:  _2022-09-21T13:08:47_
- Het aantal milliseconden is niet gelijk aan 0: _2022-09-21T13:08:47[HTML_TAG_2].682[HTML_TAG_3]_

Deze inconsistentie kan tot problemen leiden wanneer de data die deze tijdstempels bevatten automatisch worden geparseerd en verwerkt. Daarom brengen we een wijziging aan: het aantal milliseconden wordt niet langer weergegeven voor tijdstempels die zijn opgenomen in de API response. Voortaan hebben alle tijdstempels het formaat _2022-09-21T13:08:47_.

## Juni 2022

### Aankomende IP-adressen van controlestations 

De Uptrends API kan worden gebruikt om IP-adressen van controlestations op te halen, voor geautomatiseerde whitelisting. Voorheen waren responses op dergelijke requests aan onze [checkpoint API]([LINK_URL_38]) doorgaans een up-to-date lijst van huidige IP-adressen van controlestations. Uptrends' controlestationnetwerk is echter altijd in beweging. Nieuwe controlestations worden toegevoegd, bestaande controlestations worden verwijderd of verplaatst, of IP-adressen worden gewijzigd. Dat kan betekenen dat de lijst met IP-adressen die u gebruikte voor whitelisting, achterloopt tot de volgende synchronisatie, wat leidt tot onnodige fouten.

We registreren nu aankomende IP-adressen van controlestations en nemen deze op in de API-response. Op die manier is uw whitelist van te voren up-to-date.

### Relationships in statistics API

Responses van de [Statistics API]([LINK_URL_39]) (die kan worden gebruikt om statistische data voor uw controleregels of controleregelgroepen op te halen) bevatten nu enkele aanvullende metadata over de response. De nieuwe array [INLINE_CODE_56] bestaat al voor andere API-eindpunten en bevat aanvullende informatie over de request, zoals een link naar de Monitor of MonitorGroup API request om aanvullende informatie over de controleregel(groep) zelf op te halen.


[CODE_BLOCK_6]

## Mei 2022

### Oplossing voor start-/eindparameters in statistics API

Onze API ondersteunt het ophalen van statistische controleregeldata, met de [Statistics API]([LINK_URL_40]). U kunt een vooringestelde periode opgeven waarvoor de data moeten worden opgehaald (met beschikbare waarden zoals [INLINE_CODE_57]) of een aangepaste periode instellen met behulp van start- en eindparameters van de URL. Met [INLINE_CODE_58] haalt u bijvoorbeeld statistische data op voor een enkele controleregel, voor de opgegeven periode.

Er was een probleem waarbij de minutenindicator in de begin- en eindtijdstempels niet correct werd toegewezen, wat had kunnen leiden tot onvolledige (of zelfs lege) resultaten in de API-response. Dit probleem is opgelost.

## Februari 2022

### Update van status API

De [Status API]([LINK_URL_41]) haalt statusinformatie op voor een specifieke controleregel, op basis van de meest recente controleregelcheck. Dit eindpunt kan worden gebruikt voor informatie over de huidige controleregelstatus. We hebben de response zo uitgebreid dat die nu ook een waarde voor [INLINE_CODE_59] bevat - informatie over het [kengetal totale tijd]([LINK_URL_42]) voor de meest recente controleregelcheck.

## Januari 2022

### De juiste controleregeldata retourneren

Wanneer een niet-Administrator operator met [het gebruikersrecht **Gegevens bekijken**]([LINK_URL_43]) voor een bepaalde controleregel die controleregeldefinitie ophaalde via de API (via [INLINE_CODE_60]), bevatte de response niet alle relevante data. Dat was onjuist, omdat dezelfde data al beschikbaar waren via de gebruikersinterface maar niet via de API, en dit is gecorrigeerd. Wanneer deze operators nu een controleregel ophalen, bevat de response waarden voor *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive* en *GenerateAlert*.

## Augustus 2021

### Aankondiging: beëindiging van versie 3 van onze API

De [Uptrends API]([LINK_URL_44]) ondersteunt momenteel twee versies naast elkaar. Versie 3 is de oudere legacy-versie van onze API en versie 4 is de momenteel aanbevolen versie. Met een veel completere set functies ligt de focus van onze ontwikkeling al geruime tijd op versie 4. Daarom hebben we besloten te stoppen met versie 3 van onze API, deze wordt buiten gebruik gesteld en zal rond **december 2022** niet meer beschikbaar zijn. 

Voor klanten die momenteel nog actief gebruikmaken van versie 3 van onze API, moet worden opgemerkt dat deze tot die tijd nog ondersteund zal worden. We raden u echter aan om zo snel mogelijk over te stappen en versie 4 te gaan gebruiken. Om u hierbij te helpen hebben we een [API v3 naar v4 upgradehandleiding]([LINK_URL_45]) geschreven, waarin wordt uitgelegd wat de belangrijkste verschillen tussen de twee API-versies zijn en hoe u deze kunt overbruggen in uw scripts en software. 

## Juli 2021

### Belangrijke wijziging: veranderingen in autorisatie-response OperatorGroup

Met de Uptrends API kunt u [gebruikersrechten voor operators en operatorgroepen]([LINK_URL_46]) beheren, rollen toewijzen zoals **Beheerder**, **Financiële operator** of **Infra-toegang** toestaan. De [OperatorGroup API]([LINK_URL_47]) bevat verschillende opties voor het ophalen, toevoegen of verwijderen van dergelijke rechten. 

De manier waarop de gebruikersrechten worden gespecificeerd voor operatorgroepen in de API is gewijzigd, wat invloed kan hebben op het automatisch aanmaken, verwijderen of ophalen van informatie over operatorgroeprechten die u mogelijk heeft ingesteld. Momenteel werkt het ophalen van informatie over gebruikersrechten met de volgende request:

[INLINE_CODE_61]

die een response van onderstaande strekking retourneert (afhankelijk van welke rechten zijn geconfigureerd voor die specifieke operatorgroep):

[CODE_BLOCK_7]

Vanaf nu zal diezelfde request zijn response vereenvoudigen, door alleen de verleende gebruikersrechten en geen andere informatie te vermelden. De response zal niet langer een [INLINE_CODE_62] of [INLINE_CODE_63] bevatten (de laatste zal volledig verdwijnen, wat betekent dat er aan gebruikersrechten geen individuele GUID meer wordt toegewezen). Het zal er als volgt uitzien:

[CODE_BLOCK_8]

Het toevoegen van een nieuw operatorgroepsrecht werkt momenteel door een POST-request te sturen naar:

 [INLINE_CODE_64] 
 met een request body die een "AuthorizationType" specificeert. De momenteel beschikbare waarden voor AuthorizationType voor operatorgroepen zijn te vinden in de [Uptrends API Swagger UI]([LINK_URL_48]), onder **Models** (onderaan), en vervolgens **OperatorGroupAuthorizationType**.
 
 Vanaf nu kunnen nieuwe gebruikersrechten worden toegevoegd aan een operatorgroep door een POST-request te sturen naar: 

 [INLINE_CODE_65] 
 zonder een request body op te nemen. 

Het verwijderen van een recht uit een operatorgroep gebeurt momenteel door een DELETE-request te sturen naar [INLINE_CODE_66] - maar zoals hierboven opgemerkt, zal "authorizationGuid" volledig verdwijnen als een entiteit en kan niet meer worden gebruikt. In plaats daarvan kunt u gebruikersrechten verwijderen door rechtstreeks naar hun naam te verwijzen in de request-URL: [INLINE_CODE_67]

## Februari 2021

### Belangrijke wijziging: gevoelige waarden in Multi-step API-controleregels

Met ons [controleregeltype Multi-step API]([LINK_URL_49]) kunt u meerdere opeenvolgende HTTP requests uitvoeren, waarbij elke nieuwe request een of meer stukjes data gebruikt die zijn opgehaald uit een eerdere request om zijn taak uit te voeren. Vaak behelst een van de stappen dat inloggegevens worden verstrekt om toegang te krijgen tot een bepaalde bron. In het verleden werden deze inloggegevens als voorgedefinieerde variabelen toegevoegd aan de controleregeldefinitie en vervolgens gemarkeerd als *Gevoelig*.

Om de veiligheid te verbeteren van de manier waarop we met dergelijke inloggegevens omgaan, gaan we die opzet niet meer gebruiken. In plaats daarvan worden de inloggegevens in de [vault]([LINK_URL_50]) geplaatst. Met die wijziging wordt de optie om voorgedefinieerde variabelen als gevoelig te markeren in Multi-step API-controleregels achterhaald en zal worden verwijderd.

Dit zal invloed hebben op de manier waarop u Multi-step API-controleregels kunt maken of ermee kunt interacteren via onze API. Momenteel bevat de controleregeldefinitie voor dit controleregeltype een reeks "PredefinedVariables", waarbij elk van de individuele variabelen een true/false booleaans "Sensitive" heeft. In de nabije toekomst zal deze booleaanse waarde uit de definitie worden verwijderd. Als u in uw account een nieuwe Multi-step API-controleregel wilt maken of een bestaande wilt bijwerken via de Uptrends API, moet dit veld niet langer worden opgenomen. 

### Wijziging: hernoemde routing
 
 Voor Uptrends' API v4 hebben we een inconsistente manier om routes te benoemen. In de meeste gevallen wordt enkelvoud gebruikt, maar een enkele keer meervoud. De route bevat nu alleen nog delen met enkelvoud, bijvoorbeeld [INLINE_CODE_68] in plaats van [INLINE_CODE_69].

 We ondersteunen nog steeds de oude routes voor achterwaartse compatibiliteit.

{{[HTML_TAG_4]}}
