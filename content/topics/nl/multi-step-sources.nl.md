{
  "hero": {
    "title": "Bronnen voor Multi-step monitoring"
  },
  "title": "Bronnen voor Multi-step monitoring",
  "summary": "Hoe u waarden extraheert voor assertions of variabeletoewijzing bij het instellen van Multi-step API Monitoring.",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-bronnen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-sources",
  "TableOfContents": true
}

Voor het instellen van een [inhoudcontrole-assertion]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}})  of het extraheren van een [waarde die als variabele moet worden opgeslagen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}) als onderdeel van uw multi-step API-controleregel, moet u specificeren naar welke waarde we moeten kijken. De volgende opties zijn beschikbaar als bronnen:

## Response body als JSON
Kies deze optie als de body content van uw response JSON-data bevat en u een bepaald element in de JSON-structuur wilt inspecteren of vastleggen. Specificeer in het propertyveld van de assertion of variabele welk JSON-element we moeten inspecteren.

### Voorbeelden
Stel dat uw JSON response de volgende inhoud heeft:

```json
{
  "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
  "token_type":"Bearer",
  "expires_in":86400
}
```
      

Om de waarde van het kenmerk **access\_token** vast te leggen, vult u {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}} in als de propertywaarde.

Als het object dat de **access_token**-sleutel bevat het **kind** van een ander JSON-object is, specificeert u het volledige 'path'. Bijvoorbeeld:

```json
{
   "response":{
      "access_token":"MjAxNy0xMC0wMlQxMDoxMDoyNy42NDkwOTEzWg==",
      "token_type":"Bearer",
      "expires_in":86400
   }
}
```

Hier kan de access token worden gepakt door {{< Code/Symbol type="property" >}}response.access\_token{{< /Code/Symbol >}} in te vulen als de property waarde.


Nog een JSON-voorbeeld: stel dat uw JSON-data een **array** bevat van een of meer elementen, in dit geval een array van drie produkten:

```json
[
  {
    "Name": "Alpha Cygnus IX",
    "Price": 20000,
  },
  {
    "Name": "Norcadia Prime",
    "Price": 25000,
  },
  {
    "Name": "Risa", 
    "Price": 37500,
  }
]
  ```

Om een kenmerk van een van deze produkten te krijgen, zullen we eerst naar één bepaald element in de array moeten verwijzen door middel van een index. De index van het eerste element in een JSON-array is altijd nul: `[0]`. Dus om het kenmerk Price van het eerste produkt in onze array vast te leggen, specificeren we {{< Code/Symbol type="property" >}}\[0\].Price{{< /Code/Symbol >}} wat resulteert in een waarde van "20000".

Als uw JSON een array bevat als het kind van een ander object, moet u elke 'stap' specificeren, inclusief de index voor het element in de array. Stel dat uw JSON iets bevat dat lijkt op:

```json
{
   "Destinations":[
      {
         "Name":"Alpha Cygnus IX",
         "Price":20000
      },
      {
         "Name":"Norcadia Prime",
         "Price":25000
      },
      {
         "Name":"Risa",
         "Price":37500
      }
   ]
}
```

In dit geval kan de waarde voor de eerste `Name` worden vastgelegd als {{< Code/Symbol type="property" >}}Destinations.\[0\].Name{{< /Code/Symbol >}} (de waarde voor **Name** in het eerste element in de **Destinations** array), wat "Alpha Cygnus IX" zou opleveren. 


{{< callout >}}**Opmerking**: Als de response body niet kan worden geparset als JSON, genereert deze functie een fout.{{< /callout >}} 

## Response body als XML
Als uw response een XML-document bevat, kies dan deze optie en specificeer een XPath query om te bepalen welk stukje inhoud moet worden geïnspecteerd of vastgelegd.

### Voorbeeld

Stel dat uw XML response de volgende inhoud bevat:

```xml
<AuthInfo> 
  <access_token>MjAxNy0xMC0wMlQxMDowOTo1My45MDUxNjEyWg==</access_token> 
  <expires_in>86400</expires_in> 
  <token_type>Bearer</token_type> 
</AuthInfo>
```

      

Om de innerlijke waarde van de **access\_token** node vast te leggen gebruikt u de XPath query {{< Code/Symbol type="property" >}}/AuthInfo/access\_token/text(){{< /Code/Symbol >}} als de property value.

Zie voor meer informatie [meer XPath-voorbeelden, waaronder SOAP XML]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="nl" >}}).

Als de response body niet als standalone XML-document kan worden geparset, als de XPath query ongeldig is of geen werkelijke waarde uit het document selecteert, wordt er een fout gegenereerd.

## Response body als tekst

Als uw response content geen JSON of XML is (bijvoorbeeld platte tekst, HTML of een eigen formaat), kunt u deze optie nog steeds gebruiken om die inhoud te doorzoeken. Standaard bekijken we de volledige inhoud van de response. Dit werkt prima als je alleen een simpele Contains-bewerking wilt uitvoeren (bijvoorbeeld: de response body moet de uitdrukking "Price" bevatten; aan die controle wordt voldaan zolang het woord Price ergens in de inhoud staat). Als u de volledige content voor uw assertion of variabeledefinitie wilt gebruiken, laat u het eigenschappenveld leeg.

Als u echter inhoud van een zeer specifieke locatie in het document wilt inspecteren of extraheren, heeft u een manier nodig om te definiëren welk deel van de inhoud we daarvoor moeten gebruiken. Hiertoe geeft u een reguliere expressie op in het eigenschappenveld. Gebruikmakend van de mogelijkheden voor het matchen van patronen van reguliere expressies, proberen we de regex te matchen en de eerste match te gebruiken om die waarde uit uw inhoud vast te leggen.

Als de reguliere expressie een zogenaamde capturing-groep bevat (waarmee u een intern patroon binnen in de reguliere expressie kunt definiëren), gebruiken we de eerste match voor die capturing-groep.

Houd er rekening mee dat deze opties alleen van toepassing zijn op tekstinhoud (hoewel ze ook kunnen worden toegepast op responses die JSON of XML bevatten, aangezien deze nog steeds alleen tekst zijn); zoeken naar binaire inhoud wordt niet ondersteund.

## Status code

Deze optie inspecteert de numerieke HTTP-statuscode die deel uitmaakt van elke HTTP-response. In de meeste gevallen wilt u alleen controleren of de status 200 is (wat OK betekent), of in ieder geval geen fout aangeeft. In feite doen we dit standaard voor u: als u geen Statuscode-assertion opgeeft, voeren we automatisch de volgende assertion uit, want 4xx- en 5xx-codes zijn meestal foutcodes:

`Status code` {{< Code/Symbol type="comparison" >}}Is less than{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}400{{< /Code/Symbol >}} 

Als u echter zelf een Statuscode-assertion definieert, zal deze onze standaardcontrole overrulen. Als u bijvoorbeeld het volgende definieert

`Status code` {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}200{{< /Code/Symbol >}} 

zullen we precies die toestand controleren.

{{< callout >}}**Opmerking**: Er is een speciaal geval wanneer u een statuscode assertion toevoegt voor code 301, 302, 303, 307 of 308 (d.w.z. een redirect code). Zie voor meer informatie het gedeelte [Redirects verwerken](/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects).{{< /callout >}} 

## Statusomschrijving

Deze optie kijkt naar de tekstuele beschrijving van de HTTP-statuscode (formeel de Reason-Phrase genoemd). Dit kan handig zijn als u het gedrag van bepaalde foutcondities in uw API controleert: misschien wilt u verifiëren dat wanneer u onjuiste invoer invoert in uw API, er een bruikbare statusbeschrijving wordt geretourneerd.

## Response compleet

Deze optie retourneert altijd een Booleaanse waarde die is gerelateerd aan het feit of de HTTP request met succes kon worden voltooid. Het retourneert false als we niet konden vaststellen met welke server er verbinding moest worden gemaakt, als er geen verbinding tot stand kon worden gebracht of als de server niet tijdig met een HTTP response reageerde. In alle andere gevallen wordt true geretourneerd.

In de meeste gevallen hoeft u deze optie niet te specificeren, omdat we dit automatisch voor u controleren: op basis van dit assertiontype zullen we een fout melden wanneer we geen HTTP response van uw server kunnen ophalen:

 `Response completed` {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}true{{< /Code/Symbol >}} 

Voor sommige speciale gevallen is het mogelijk om deze controle om te draaien: als u in plaats daarvan false opgeeft, controleren we of het verkrijgen van een succesvolle response NIET mogelijk is. Dit kan handig zijn als u een webapplicatie of API heeft die alleen binnen uw netwerk beschikbaar moet zijn, ook al is de bijbehorende domeinnaam openbaar beschikbaar. Met behulp van deze controle controleren we of we uw API of web-app niet kunnen bereiken.

## Response header 

Met deze optie kunt u een specifieke HTTP response header controleren. U moet de naam van die header opgeven in het eigenschappenveld.

## Cookie

Deze optie retourneert de huidige waarde van een cookie. U moet de naam van die cookie opgeven in het eigenschappenveld. Houd er rekening mee dat cookies die door uw server worden geretourneerd, behandeld worden als sessiecookies: cookiewaarden worden bewaard, bijgewerkt en teruggestuurd naar uw server tijdens de uitvoering van het volledige scenario, tot de laatste stap. Nadien worden alle cookies verwijderd, ongeacht eventuele richtlijnen voor het vervallen van de geldigheid. Dit betekent dat permanente cookies in essentie worden behandeld als sessiecookies.

## Content length

Deze optie retourneert de grootte (in bytes) van de response body. Houd er rekening mee dat dit de werkelijke lengte van de inhoud is nadat de response body is uitgepakt (als uw server deze eerder heeft gecomprimeerd).

## Duration
Deze optie retourneert de totale hoeveelheid tijd (in milliseconden) die nodig was om de request uit te voeren en de response te ontvangen. Hiermee kunt u de performancetijden van individuele stappen monitoren.
