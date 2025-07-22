{
  "hero": {
    "title": "Variabelen bij Multi-step monitoring"
  },
  "title": "Variabelen bij Multi-step monitoring",
  "summary": "Hoe u variabelen gebruikt voor het opslaan van waarden uit uw API-responses voor gebruik in latere stappen.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-variabelen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-variables"
}

In een [multi-step API monitoring set-up]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}) worden variabelen meestal gebruikt om waarden uit uw HTTP-responses te extraheren en ze tijdelijk op te slaan, zodat u ze opnieuw kunt gebruiken in een latere stap. Hiermee kunt u in feite stappen aan elkaar koppelen: elke keer dat u een stukje informatie uit een HTTP-respons wilt halen en die informatie wilt gebruiken om de volgende HTTP-request uit te voeren, heeft u een variabele nodig. Simpel gezegd: stap 1 ontvangt een waarde van uw server en slaat deze op in een variabele. Stap 2 neemt dan de waarde die we zojuist hebben opgeslagen en gebruikt deze om een nieuwe request op te bouwen. U kunt zoveel variabelen gebruiken als u wilt en ze in zoveel stappen gebruiken als u nodig heeft.

Een tweede reden om variabelen te gebruiken, is om bepaalde waarden slechts eenmaal te definiëren en ze in verschillende stappen opnieuw te gebruiken. Normaal gesproken voegt u deze waarden toe in het gedeelte Voorgedefinieerde variabelen: die variabelen zijn in elke stap beschikbaar gedurende het gehele meerstapsscenario. Zie de sectie [Voorgedefinieerde variabelen](#predefined-variables) voor meer informatie.

Alle variabelen die u in een stap definieert worden geëvalueerd zodra de HTTP-request is uitgevoerd en de respons is verwerkt. Op dat moment, als een variabele al bestond (ofwel door een vorige stap, of omdat u deze vooraf heeft gedefinieerd), wordt de bestaande waarde ervan overschreven. Anders wordt een nieuwe variabele gemaakt en aan de lijst toegevoegd. Deze lijst met variabelen en bijbehorende waarden wordt vervolgens meegenomen naar de volgende stap.

## Variabelen definiëren

Als u variabelen wilt gebruiken, moet u ons vertellen welke waarde we in die variabele moeten opslaan. Vergelijkbaar met het patroon dat wordt gebruikt om assertions te definiëren, worden variabelen op de volgende manier gedefinieerd:

{{< Code/Symbol type="source" >}}Source{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}property{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}variable name{{< /Code/Symbol >}} 

bijvoorbeeld:

{{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}access\_token{{< /Code/Symbol >}} 

-   De **variable source**: dit veld definieert welk kenmerk van de HTTP respons u wilt extraheren. [Alle beschikbare opties worden in dit artikel beschreven]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="nl" >}}).
-   De **variable property**: sommige source-opties (met name de inhoudextractie en header-gerelateerde opties) vereisen dat u verder specificeert welke inhoud of header moet worden gecontroleerd. Dit wordt [uitgebreider uitgelegd]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="nl" >}})  voor elk geschikt sourcetype.
-   De **variable name**: dit is de identifier die in de volgende stappen zal worden gebruikt om terug te verwijzen naar deze variabele, met behulp van een speciale notatie.

Als er een probleem optreedt tijdens de evaluatie van een variabele (bijvoorbeeld omdat u probeert een waarde te extraheren die niet aanwezig is in de responsinhoud), zal de stap mislukken en een fout worden gerapporteerd.

## Verwijzen naar variabelen in andere stappen

Nadat een variabele met succes is geëvalueerd, kan zijn waarde opnieuw worden gebruikt in de requestdefinitie van volgende stappen en binnen assertions (responsinhoud-controles). Verwijs altijd naar een variabele door de variabelenaam tussen dubbele accolades te plaatsen: {{< Code/Symbol type="variable" >}}{{variable-name}}{{< /Code/Symbol >}}.

-   In de URL van een stap: `https://myapi.customer.com/ProductInfo/{{ProductId}}`

-   In een Request header: `"Authorization": Bearer {{access_token}}`

-   In Request Body inhoud:

    `{ "ProductId": "{{ProductId}}", "Code": "P123456" }`

-   In de doelwaarde van een assertion. Heeft u bijvoorbeeld een variabele {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}} (in een vorige stap ingevuld, of als een voorgedefinieerde variabele), dan kunt u die gebruiken om te verifiëren dat een respons de feitelijke waarde in die variabele bevat:

    {{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products\[0\].Id{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}

-   In de propertywaarde van een assertion. Als u een variabele {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}} heeft, kunt u naar die variabele verwijzen in een JSON-expressie of XPath-query om de inhoud te selecteren die u wilt verifiëren:

    {{< Code/Symbol type="source" >}}Response body as XML{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}//Product\[@Id="{{ProductId}}"\]/Name/text(){{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} `Chocolate chip cookie`

## Voorgedefinieerde variabelen

Onder de stap-editor vindt u een extra gedeelte waar u meer variabelen kunt specificeren. Deze variabelen zijn beschikbaar aan het begin van het hele scenario. Als u een bepaalde waarde meerdere keren nodig heeft, kunt u die waarde van tevoren definiëren en in verschillende stappen gebruiken. Dit kan een product-ID zijn die u in uw hele scenario wilt gebruiken, een API-key of andere speciale waarden die uw API nodig heeft. Eén speciaal geval is het gebruik van een variabele die de domeinnaam voor elke API bevat. Door die variabele als onderdeel van elke URL te gebruiken, hoeft u deze niet in elke stap te herhalen, waardoor u deze heel gemakkelijk voor het hele scenario kunt wijzigen. Om een voorgedefinieerde variabele toe te voegen klikt u op
 {{< AppElement type="button" >}}\+ Variabele toevoegen{{< /AppElement >}} in de controleregelinstellingen, onder het gedeelte *Voorgedefinieerde variabelen*. Maak dan een variabele genaamd `BaseUrl` met de waarde `https://test.yourapi.com`. Door een verwijzing naar die variabele te gebruiken, kan de URL voor elke API-stap de vorm `{{BaseURL}}/UserService/GetUserInfo` hebben. Met deze aanpak kunt u uw meerstapsscenario zo wijzigen dat die naar een andere omgeving verwijst (bijvoorbeeld een staging-omgeving versus een production-omgeving), zonder elke stap te hoeven wijzigen. 

Voorgedefinieerde variabelen kunnen ook worden gebruikt als op enig moment tijdens het uitvoeren van de controleregel gevoelige gegevens moeten worden verzonden. Als uw API bijvoorbeeld geauthenticeerde toegang vereist, moet u mogelijk inloggen of een toegangstoken ophalen door inloggegevens toe te voegen aan een van uw requests. Gevoelige gegevens worden opgeslagen [in de vault](/support/kb/vault). Om vault-inloggegevens in te stellen voor gebruik in een Multi-Step API-controleregel doet u het volgende:

1. Zorg er eerst voor dat u [de inloggegevens heeft toegevoegd aan de vault]({{< ref path="/support/kb/account/vault#een-nieuw-item-aan-de-vault-toevoegen" lang="nl" >}}).

2. Creëer de voorgedefinieerde variabele zoals u dat normaal zou doen, zoals hierboven beschreven. 
3. Om te verwijzen naar een vault-item klikt u op het pictogram [...] onder **waarde**, waardoor de waardekiezer wordt geopend.

![Waardekiezer MSA-vault](/img/content/scr_MSA_predefined_variables_1.min.png)

4. Selecteer de juiste set inloggegevens in de lijst en selecteer de waarde in het veld gebruikersnaam of het veld wachtwoord.
5. Geef uw variabele een geschikte **Naam**. Naar deze naam gaat u verwijzen tijdens het uitvoeren van de controleregel, zoals beschreven in dit artikel. In het onderstaande voorbeeld verwijzen we naar de variabele *examplePassword* als `{{examplePassword}}`. 

![Waardekiezer MSA-vault](/img/content/scr-MSA-predefined-variables-example.min.png)

In de controleregel-log worden waarden uit het veld *wachtwoord* in het vault-item weergegeven als sterretjes om de gevoelige gegevens verborgen te houden.

![Waardekiezer MSA-vault](/img/content/MSA_predefined_variables_result.png)

## Codering van waarden van variabelen

Afhankelijk van waar u uw variabelen gebruikt, is het soms nodig om de waarden te coderen. Coderen betekent dat we speciale tekens converteren naar een formaat dat geschikt is voor een HTTP-request. Doorgaans moeten variabelen die in een URL worden gebruikt, worden gecodeerd. Stel dat u een URL bouwt waarbij een naamparameter wordt gebruikt en dat u een variabele met de naam {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} wilt gebruiken om een waarde voor die parameter te specificeren. Zonder rekening te houden met codering, zou u die als volgt gebruiken:

`https://my.api.com/GetCompanyInfo?name={{CompanyName}}`

Stel nu dat de variabele {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} de waarde `Ben & Jerry's` bevat. Die waarde bevat spaties en een ampersand-teken (&), die een speciale betekenis hebben in een URL. Zonder enige codering toe te passen, komt de correcte waarde niet op de server terecht. Als u eerst codering toepast, wordt de waarde geconverteerd naar `Ben\+%26\+Jerry's`,  die door de server wordt geïnterpreteerd als de oorspronkelijke waarde. Gebruik de functie {{< Code/Symbol type="variable" >}}{{@UrlEncode(...)}}{{< /Code/Symbol >}} om codering toe te passen op uw variabelen. Vermeld binnen de haakjes de volledige naam van de variabele, bijvoorbeeld {{< Code/Symbol type="variable" >}}{{CompanyName}}{{< /Code/Symbol >}}. Gebruikt in een URL ziet het er als volgt uit:

`https://my.api.com/GetCompanyInfo?name={{@UrlEncode({{CompanyName}})}}`

Als een variabele nooit speciale tekens bevat (bijvoorbeeld alleen numerieke waarden), is het niet nodig om de @UrlEncode-functie te gebruiken. We URL-coderen automatisch variabelen die worden gebruikt in het veld Request Body van een stap, maar alleen als er een Content-Type header is gespecificeerd met de waarde application/x-www-form-urlencoded. Andere soorten inhoud vereisen meestal geen URL-codering.

## Automatische variabelen

Afgezien van de variabelen die u in uw controleregelinstellingen definieert, heeft u ook toegang tot een aantal automatische variabelen die wij voor u maken. De meeste daarvan zijn feitelijk functies die een waarde genereren die u kunt gebruiken in uw HTTP requests en tijdens de evaluatie van uw HTTP responses met behulp van assertions. Wilt u automatische variabelen gebruiken in uw Multi-Step API monitoring, raadpleeg dan onze [volledige lijst met beschikbare automatische variabelen]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}).

## Door de gebruiker gedefinieerde functies

In bepaalde gevallen moeten de waarden van de inkomende data getransformeerd of gemapt worden om ze inzichtelijker te maken. Met Uptrends kunt u gebruiker-gedefinieerde functies instellen die kunnen worden gebruikt om waarden van variabelen (uit een vorige stap of een systeemvariabele uit Uptrends) om te zetten naar een nieuwe waarde. Meer informatie over het instellen en gebruiken van door de gebruiker gedefinieerde functies vindt u in [dit knowledgebase-artikel]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="nl" >}}).

## Vrije kengetal-variabelen

Wanneer uw MSA-controleregel data van uw API's vastlegt, kunnen er gevallen zijn waarin u specifieke numerieke data wilt bijhouden die geen deel uitmaken van de standaard meetgegevens, zoals responsstatuscode en de responsduur, bij het evalueren van het gedrag van uw API.

In dergelijke gevallen kunt u met de Vrij kengetal-variabele een door de gebruiker gedefinieerde variabele creëren om alle numerieke data op te slaan die zijn vastgelegd in de respons van de API. Raadpleeg het knowledgebase-artikel [Vrije Kengetallen instellen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#how-to-set-up-custom-api-monitoring" lang="nl" >}}) voor meer informatie.