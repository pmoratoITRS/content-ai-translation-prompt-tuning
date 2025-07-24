{
  "hero": {
    "title": "Hashing en codering"
  },
  "title": "Hashing- en/of coderingswaarden",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In bepaalde gebruikssituaties van [API monitoring]([LINK_URL_1]) kan het nodig zijn om variabelen of waarden te hashen of te coderen. Autorisatie-instellingen kunnen bijvoorbeeld Base64-codering of HMAC-SHA256-hashing vereisen om correct te werken, of u moet mogelijk gecodeerde JSON opnemen in uw request body. Hiertoe biedt Uptrends verschillende opties voor codering en hashing, die in dit artikel worden beschreven.

## Coderen en decoderen

Coderen is een proces om te verzekeren dat data op een betrouwbare manier, in een bepaalde vorm, kunnen worden verzonden. Een string of bestand kan worden gecodeerd om ervoor te zorgen dat de ontvangende kant het formaat begrijpt, waarna het weer kan worden gedecodeerd.

### Base64 
Base64 is een coderingsschema dat doorgaans wordt gebruikt om binaire data als tekst te transporteren. Het wordt vaak gebruikt in protocollen zoals [Basic Authentication]([LINK_URL_2]). Om Base64-codering toe te passen binnen uw Multi-step API-controleregel gebruikt u de functie [INLINE_CODE_1]. 

De Base64Encode-functie accepteert ook [(voorgedefinieerde) variabelen]([LINK_URL_3]), door simpelweg de variabele referentie (verpakt tussen accolades) in te vullen in de functie: [INLINE_CODE_2].

Decodering wordt ook ondersteund, door de functie [INLINE_CODE_3] te gebruiken. 

De Base64Encode- en -Decode-functies kunnen op elk punt in de Multi-step API-controleregelconfiguratie worden gebruikt. Dit betekent dat u er rechtstreeks naar kunt verwijzen, bijvoorbeeld bij het creëren van een request header, of in de inhoud van uw request body. 

![Base64Encode-functie gebruikt in een Auth header]([LINK_URL_4])

### JSON en XML

JSON en XML zijn gangbare formaten voor gegevensuitwisseling, die zich doorgaans aan een nogal strikte opmaak houden om geldig te blijven. In sommige gevallen moet JSON- of XML-inhoud worden gecodeerd voordat die kan worden verzonden. JSON kan bijvoorbeeld niet in zichzelf worden ingebed (u kunt geen JSON-geformatteerde inhoud binnen JSON-geformatteerde inhoud verzenden) zonder zijn structuur te verbreken, tenzij die gecodeerd is. Nog een voorbeeld: als uw inhoud in platte tekst aanhalingstekens bevat, hebben deze een specifieke betekenis in het JSON-formaat en kunnen ze niet in een JSON-gestructureerd bericht worden verzonden zonder ze eerst te coderen. 

Vergelijkbaar met de hierboven beschreven Base64Encoding- en -Decoding-functionaliteit, zijn er de functies JsonEncode(), JsonDecode(), XmlEncode() en XmlDecode(). Meer informatie over hun implementatie vindt u in onze documentatie over [berichtopmaak toepassen in een aanpasbare integratie]([LINK_URL_5]).

## Hashing [ANCHOR_1]

In tegenstelling tot codering, die kan worden gedecodeerd, is hashing een eenrichtingsproces waarbij een algoritme een bericht van elke lengte neemt en dit met behulp van een wiskundige functie toewijst aan een waarde met een vaste lengte. Een gehashte waarde kan praktisch niet worden teruggedraaid, en elke gegeven invoer moet altijd tot hetzelfde resultaat leiden. Hashing wordt vaak gebruikt bij authenticatie, omdat het een veilige methode is om geheime informatie, zoals wachtwoorden of handtekeningen, uit te wisselen en te vergelijken. 

Uptrends ondersteunt de volgende hashing-algoritmen:

- MD5
- SHA1
- SHA256
- SHA512
- HMAC-SHA1
- HMAC-SHA256
- HMAC-SHA512

Hashing-functies worden geïmplementeerd via het systeem van de [Gebruiker-gedefinieerde functies]([LINK_URL_6]), en de implementatie van een hashing-functie volgt dezelfde stappen als beschreven in dat artikel. U kunt een hashing-functie toepassen op elke tekenreeks zonder opmaak, op alle [variabelen]([LINK_URL_7]) die zijn gecreëerd als resultaat van een van de stappen in uw controleregel, of op alle [voorgedefinieerde variabelen]([LINK_URL_8]).

De op HMAC gebaseerde hashing-functies vereisen dat u een **geheime sleutel** opgeeft als een statische invoer, die zij zullen combineren met het bericht om een veilige, consistente uitvoer te genereren. Dit kan ook een waarde zijn van een set [vault]([LINK_URL_9])-inloggegevens.

![Voorbeeld van een hashing-functie]([LINK_URL_10])

### Base64-codering voor gehashte data

Voor bepaalde authenticatiemethoden is mogelijk een gehashte waarde vereist, die dan Base64-gecodeerd moet zijn. De hierboven genoemde functie [INLINE_CODE_4] is bedoeld om het datatype *string* te coderen. Deze hashing-functies resulteren echter in *hexadecimale* data. Dat betekent dat het coderen ervan met de standaard Base64-functie tot onjuiste resultaten kan leiden, omdat we met verschillende datatypes werken. 

Om de *hexadecimale* waarde die het resultaat is van een hashing-functie correct te coderen, gebruikt u de functie [INLINE_CODE_5] in plaats van de standaardfunctie [INLINE_CODE_6].