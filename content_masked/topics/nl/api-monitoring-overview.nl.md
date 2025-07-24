{
  "hero": {
    "title": "Overzicht API-monitoring"
  },
  "title": "Overzicht API-monitoring",
  "summary": "Wat is API Monitoring en hoe kunt u het gebruiken?",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Een API (Application Programming Interface) is software die de communicatie tussen applicaties mogelijk maakt. Misschien gebruikt u uw eigen API's en/of vertrouwt u op API's van derden. Hoe dan ook, het correct functioneren van de API's is cruciaal voor de werking van uw website en diensten, daarom moet u ze monitoren.

API Monitoring controleert of de API's waarop u vertrouwt beschikbaar zijn, correct functioneren en goed presteren. Meer informatie is te vinden in het artikel [Wat is API Monitoring?]([LINK_URL_1]).

Uptrends API Monitoring biedt verschillende types controleregels om API Monitoring te configureren. Welk type u kiest, hangt af van of u te maken heeft met een enkele stap of met een keten van requests die uit meerdere stappen bestaat. De eenstaps-controleregel wordt gedefinieerd met het controleregeltype Webservice HTTP of Webservice HTTPS. De controleregel voor een reeks stappen wordt gedefinieerd met het controleregeltype Multi-step API (MSA-controleregel.

De Uptrends-app heeft een [Multi-step API-controleregel hub]([LINK_URL_2]) waar informatie over deze controleregels en de huidige status op één plek zijn te vinden.

## API-controleregels instellen

Het instellen van de verschillende types controleregels wordt beschreven in deze artikelen:

-   [Web Services Monitoring instellen]([LINK_URL_3])
-   [Web Services Monitoring (SOAP) instellen]([LINK_URL_4])
-   [Multi-step API Monitoring instellen]([LINK_URL_5])
-   [Postman API Monitoring instellen]([LINK_URL_6])

## Multi-step API-controleregelstappen definiëren

Bij het instellen van een Multi-step API-controleregel definieert u een stap voor elke HTTP-request die deel uitmaakt van het scenario dat u wilt monitoren. Voor elke stap bekijkt u twee onderdelen: eerst specificeert u de details voor het Request-gedeelte en definieert u wat er moet worden uitgevoerd en naar uw API moet worden verzonden. En ten tweede specificeert u het Response-gedeelte en definieert u wat er moet worden gecontroleerd in de response van onze API. 

Zowel het Request- als Response-gedeelte voor elke stap kan optioneel worden uitgebreid met [Aangepaste scripting]([LINK_URL_7]), geschreven in Javascript. U kunt uw aangepaste scripts toevoegen voor authenticatie en berekeningen en aangepaste logica uitvoeren om de correcte functionaliteit en inhoud van uw API-stappen te verifiëren.

Er zijn ook enkele definities voor [door de gebruiker gedefinieerde functies]([LINK_URL_8]), [variabelen]([LINK_URL_9]) en [vrije kengetallen]([LINK_URL_10]). Deze worden globaal ingesteld (beschikbaar voor alle stappen). Bekijk de artikelen in de onderstaande secties voor meer informatie over het instellen van de HTTP-stappen.

### Request

De HTTP-staprequest wordt ingesteld door een methode en URL en de requestbody te verstrekken, en vervolgens verdere details zoals de authenticatie te specificeren. De Request-definitie kan ook verder worden gewijzigd met aangepaste scripting. Zie de onderstaande artikelen voor meer informatie.

-   [Authenticatie]([LINK_URL_11])
-   [Clientcertificaten]([LINK_URL_12])
-   [Uptrends' clientcertificaat]([LINK_URL_13])
-   [Bestandsuploads in Multi-Step API]([LINK_URL_14])
- [Aangepaste scripting]([LINK_URL_15])

### Response

Binnen de response van de stap moet u assertions definiëren. Assertions zijn controles die één stap verder gaan dan de vraag of er een response op de request is. Een assertion controleert ook of de response geldig is of op tijd arriveert. Voor elke stap kunt u een aantal assertions definiëren. Naast het definiëren van Assertions op het tabblad Response, is het mogelijk om volledig aangepaste controles en logica in te stellen met de functie Aangepaste scripting. Meer informatie over assertions vindt u in deze artikelen:

-   [Assertions - Inleiding]([LINK_URL_16])
-   [Assertions - Bronnen]([LINK_URL_17])
-   [Assertions - Vergelijkingsoperatoren]([LINK_URL_18])
-   [Assertions - Voorbeelden met XPath]([LINK_URL_19])
-   [Variabelen]([LINK_URL_20])
-   [Redirects afhandelen]([LINK_URL_21])
- [Aangepaste scripting]([LINK_URL_22])

### Globale definities

Er zijn een aantal dingen die u kunt definiëren voor alle stappen en zowel het request- als het responsegedeelte ervan. Dit is handig als u een bepaalde waarde of functie in verschillende stappen wilt gebruiken. Lees verder in de volgende artikelen voor meer informatie:

-   [Voorgedefinieerde variabelen]([LINK_URL_23])
-   [Door de gebruiker gedefinieerde functies]([LINK_URL_24])
-   [Vrije kengetallen]([LINK_URL_25])
-   [Hashing en codering]([LINK_URL_26])

### Scriptweergave

U kunt de stapdefinities van Multi-step API-controleregels ook rechtstreeks in de *scriptweergave* bewerken. Dit script bevat de volledige definitie van uw Multi-step API-definitie, die u kunt kopiëren en plakken naar andere plaatsen. Zie ons artikel over de [MSA-scripteditor]([LINK_URL_27]) voor meer informatie.

Merk op dat de *scriptweergave* niet hetzelfde is als de functie [Aangepaste scripting]([LINK_URL_28]) waarmee u aangepaste logica aan uw scripts kunt toevoegen.

## Credits

API-controleregels gebruiken API-credits om u controleregels te laten creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]([LINK_URL_29]) voor meer informatie.