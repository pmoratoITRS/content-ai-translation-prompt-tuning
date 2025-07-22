{
  "hero": {
    "title": "Variabelen bij Multi-step monitoring"
  },
  "title": "Variabelen bij Multi-step monitoring",
  "summary": "Hoe u variabelen gebruikt voor het opslaan van waarden uit uw API-responses voor gebruik in latere stappen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-variabelen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In een [multi-step API monitoring set-up]([LINK_URL_1]) worden variabelen meestal gebruikt om waarden uit uw HTTP-responses te extraheren en ze tijdelijk op te slaan, zodat u ze opnieuw kunt gebruiken in een latere stap. Hiermee kunt u in feite stappen aan elkaar koppelen: elke keer dat u een stukje informatie uit een HTTP-respons wilt halen en die informatie wilt gebruiken om de volgende HTTP-request uit te voeren, heeft u een variabele nodig. Simpel gezegd: stap 1 ontvangt een waarde van uw server en slaat deze op in een variabele. Stap 2 neemt dan de waarde die we zojuist hebben opgeslagen en gebruikt deze om een nieuwe request op te bouwen. U kunt zoveel variabelen gebruiken als u wilt en ze in zoveel stappen gebruiken als u nodig heeft.

Een tweede reden om variabelen te gebruiken, is om bepaalde waarden slechts eenmaal te definiëren en ze in verschillende stappen opnieuw te gebruiken. Normaal gesproken voegt u deze waarden toe in het gedeelte Voorgedefinieerde variabelen: die variabelen zijn in elke stap beschikbaar gedurende het gehele meerstapsscenario. Zie de sectie [Voorgedefinieerde variabelen]([LINK_URL_2]) voor meer informatie.

Alle variabelen die u in een stap definieert worden geëvalueerd zodra de HTTP-request is uitgevoerd en de respons is verwerkt. Op dat moment, als een variabele al bestond (ofwel door een vorige stap, of omdat u deze vooraf heeft gedefinieerd), wordt de bestaande waarde ervan overschreven. Anders wordt een nieuwe variabele gemaakt en aan de lijst toegevoegd. Deze lijst met variabelen en bijbehorende waarden wordt vervolgens meegenomen naar de volgende stap.

## Variabelen definiëren

Als u variabelen wilt gebruiken, moet u ons vertellen welke waarde we in die variabele moeten opslaan. Vergelijkbaar met het patroon dat wordt gebruikt om assertions te definiëren, worden variabelen op de volgende manier gedefinieerd:

[SHORTCODE_3]Source[SHORTCODE_4] [SHORTCODE_5]property[SHORTCODE_6] [SHORTCODE_7]variable name[SHORTCODE_8] 

bijvoorbeeld:

[SHORTCODE_9]Response body as JSON[SHORTCODE_10] [SHORTCODE_11]access\_token[SHORTCODE_12] [SHORTCODE_13]access\_token[SHORTCODE_14] 

-   De **variable source**: dit veld definieert welk kenmerk van de HTTP respons u wilt extraheren. [Alle beschikbare opties worden in dit artikel beschreven]([LINK_URL_3]).
-   De **variable property**: sommige source-opties (met name de inhoudextractie en header-gerelateerde opties) vereisen dat u verder specificeert welke inhoud of header moet worden gecontroleerd. Dit wordt [uitgebreider uitgelegd]([LINK_URL_4])  voor elk geschikt sourcetype.
-   De **variable name**: dit is de identifier die in de volgende stappen zal worden gebruikt om terug te verwijzen naar deze variabele, met behulp van een speciale notatie.

Als er een probleem optreedt tijdens de evaluatie van een variabele (bijvoorbeeld omdat u probeert een waarde te extraheren die niet aanwezig is in de responsinhoud), zal de stap mislukken en een fout worden gerapporteerd.

## Verwijzen naar variabelen in andere stappen

Nadat een variabele met succes is geëvalueerd, kan zijn waarde opnieuw worden gebruikt in de requestdefinitie van volgende stappen en binnen assertions (responsinhoud-controles). Verwijs altijd naar een variabele door de variabelenaam tussen dubbele accolades te plaatsen: [SHORTCODE_15]{{variable-name}}[SHORTCODE_16].

-   In de URL van een stap: [INLINE_CODE_1]

-   In een Request header: [INLINE_CODE_2]

-   In Request Body inhoud:

    [INLINE_CODE_3]

-   In de doelwaarde van een assertion. Heeft u bijvoorbeeld een variabele [SHORTCODE_17]{{ProductId}}[SHORTCODE_18] (in een vorige stap ingevuld, of als een voorgedefinieerde variabele), dan kunt u die gebruiken om te verifiëren dat een respons de feitelijke waarde in die variabele bevat:

    [SHORTCODE_19]Response body as JSON[SHORTCODE_20] [SHORTCODE_21]Products\[0\].Id[SHORTCODE_22] [SHORTCODE_23]Equals[SHORTCODE_24] [SHORTCODE_25]{{ProductId}}[SHORTCODE_26]

-   In de propertywaarde van een assertion. Als u een variabele [SHORTCODE_27]{{ProductId}}[SHORTCODE_28] heeft, kunt u naar die variabele verwijzen in een JSON-expressie of XPath-query om de inhoud te selecteren die u wilt verifiëren:

    [SHORTCODE_29]Response body as XML[SHORTCODE_30] [SHORTCODE_31]//Product\[@Id="{{ProductId}}"\]/Name/text()[SHORTCODE_32] [SHORTCODE_33]Equals[SHORTCODE_34] [INLINE_CODE_4]

## Voorgedefinieerde variabelen

Onder de stap-editor vindt u een extra gedeelte waar u meer variabelen kunt specificeren. Deze variabelen zijn beschikbaar aan het begin van het hele scenario. Als u een bepaalde waarde meerdere keren nodig heeft, kunt u die waarde van tevoren definiëren en in verschillende stappen gebruiken. Dit kan een product-ID zijn die u in uw hele scenario wilt gebruiken, een API-key of andere speciale waarden die uw API nodig heeft. Eén speciaal geval is het gebruik van een variabele die de domeinnaam voor elke API bevat. Door die variabele als onderdeel van elke URL te gebruiken, hoeft u deze niet in elke stap te herhalen, waardoor u deze heel gemakkelijk voor het hele scenario kunt wijzigen. Om een voorgedefinieerde variabele toe te voegen klikt u op
 [SHORTCODE_1]\+ Variabele toevoegen[SHORTCODE_2] in de controleregelinstellingen, onder het gedeelte *Voorgedefinieerde variabelen*. Maak dan een variabele genaamd [INLINE_CODE_5] met de waarde [INLINE_CODE_6]. Door een verwijzing naar die variabele te gebruiken, kan de URL voor elke API-stap de vorm [INLINE_CODE_7] hebben. Met deze aanpak kunt u uw meerstapsscenario zo wijzigen dat die naar een andere omgeving verwijst (bijvoorbeeld een staging-omgeving versus een production-omgeving), zonder elke stap te hoeven wijzigen. 

Voorgedefinieerde variabelen kunnen ook worden gebruikt als op enig moment tijdens het uitvoeren van de controleregel gevoelige gegevens moeten worden verzonden. Als uw API bijvoorbeeld geauthenticeerde toegang vereist, moet u mogelijk inloggen of een toegangstoken ophalen door inloggegevens toe te voegen aan een van uw requests. Gevoelige gegevens worden opgeslagen [in de vault]([LINK_URL_5]). Om vault-inloggegevens in te stellen voor gebruik in een Multi-Step API-controleregel doet u het volgende:

1. Zorg er eerst voor dat u [de inloggegevens heeft toegevoegd aan de vault]([LINK_URL_6]).

2. Creëer de voorgedefinieerde variabele zoals u dat normaal zou doen, zoals hierboven beschreven. 
3. Om te verwijzen naar een vault-item klikt u op het pictogram [...] onder **waarde**, waardoor de waardekiezer wordt geopend.

![Waardekiezer MSA-vault]([LINK_URL_7])

4. Selecteer de juiste set inloggegevens in de lijst en selecteer de waarde in het veld gebruikersnaam of het veld wachtwoord.
5. Geef uw variabele een geschikte **Naam**. Naar deze naam gaat u verwijzen tijdens het uitvoeren van de controleregel, zoals beschreven in dit artikel. In het onderstaande voorbeeld verwijzen we naar de variabele *examplePassword* als [INLINE_CODE_8]. 

![Waardekiezer MSA-vault]([LINK_URL_8])

In de controleregel-log worden waarden uit het veld *wachtwoord* in het vault-item weergegeven als sterretjes om de gevoelige gegevens verborgen te houden.

![Waardekiezer MSA-vault]([LINK_URL_9])

## Codering van waarden van variabelen

Afhankelijk van waar u uw variabelen gebruikt, is het soms nodig om de waarden te coderen. Coderen betekent dat we speciale tekens converteren naar een formaat dat geschikt is voor een HTTP-request. Doorgaans moeten variabelen die in een URL worden gebruikt, worden gecodeerd. Stel dat u een URL bouwt waarbij een naamparameter wordt gebruikt en dat u een variabele met de naam [SHORTCODE_35]CompanyName[SHORTCODE_36] wilt gebruiken om een waarde voor die parameter te specificeren. Zonder rekening te houden met codering, zou u die als volgt gebruiken:

[INLINE_CODE_9]

Stel nu dat de variabele [SHORTCODE_37]CompanyName[SHORTCODE_38] de waarde [INLINE_CODE_10] bevat. Die waarde bevat spaties en een ampersand-teken (&), die een speciale betekenis hebben in een URL. Zonder enige codering toe te passen, komt de correcte waarde niet op de server terecht. Als u eerst codering toepast, wordt de waarde geconverteerd naar [INLINE_CODE_11],  die door de server wordt geïnterpreteerd als de oorspronkelijke waarde. Gebruik de functie [SHORTCODE_39][SYSTEM_VAR_1][SHORTCODE_40] om codering toe te passen op uw variabelen. Vermeld binnen de haakjes de volledige naam van de variabele, bijvoorbeeld [SHORTCODE_41]{{CompanyName}}[SHORTCODE_42]. Gebruikt in een URL ziet het er als volgt uit:

[INLINE_CODE_12]

Als een variabele nooit speciale tekens bevat (bijvoorbeeld alleen numerieke waarden), is het niet nodig om de @UrlEncode-functie te gebruiken. We URL-coderen automatisch variabelen die worden gebruikt in het veld Request Body van een stap, maar alleen als er een Content-Type header is gespecificeerd met de waarde application/x-www-form-urlencoded. Andere soorten inhoud vereisen meestal geen URL-codering.

## Automatische variabelen

Afgezien van de variabelen die u in uw controleregelinstellingen definieert, heeft u ook toegang tot een aantal automatische variabelen die wij voor u maken. De meeste daarvan zijn feitelijk functies die een waarde genereren die u kunt gebruiken in uw HTTP requests en tijdens de evaluatie van uw HTTP responses met behulp van assertions. Wilt u automatische variabelen gebruiken in uw Multi-Step API monitoring, raadpleeg dan onze [volledige lijst met beschikbare automatische variabelen]([LINK_URL_10]).

## Door de gebruiker gedefinieerde functies

In bepaalde gevallen moeten de waarden van de inkomende data getransformeerd of gemapt worden om ze inzichtelijker te maken. Met Uptrends kunt u gebruiker-gedefinieerde functies instellen die kunnen worden gebruikt om waarden van variabelen (uit een vorige stap of een systeemvariabele uit Uptrends) om te zetten naar een nieuwe waarde. Meer informatie over het instellen en gebruiken van door de gebruiker gedefinieerde functies vindt u in [dit knowledgebase-artikel]([LINK_URL_11]).

## Vrije kengetal-variabelen

Wanneer uw MSA-controleregel data van uw API's vastlegt, kunnen er gevallen zijn waarin u specifieke numerieke data wilt bijhouden die geen deel uitmaken van de standaard meetgegevens, zoals responsstatuscode en de responsduur, bij het evalueren van het gedrag van uw API.

In dergelijke gevallen kunt u met de Vrij kengetal-variabele een door de gebruiker gedefinieerde variabele creëren om alle numerieke data op te slaan die zijn vastgelegd in de respons van de API. Raadpleeg het knowledgebase-artikel [Vrije Kengetallen instellen]([LINK_URL_12]) voor meer informatie.