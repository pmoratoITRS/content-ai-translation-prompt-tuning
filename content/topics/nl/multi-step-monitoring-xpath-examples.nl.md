{
  "hero": {
    "title": "Multi-step monitoring XPath-voorbeelden"
  },
  "title": "Multi-step monitoring XPath-voorbeelden",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-voorbeelden",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-xpath-examples"
}

Dit artikel bevat verschillende voorbeelden voor het extraheren van inhoud van XML-responses met behulp van XPath. Met deze XPath-query's kunt u een XML-respons die terugkomt van uw API of webservice inspecteren als onderdeel van een [Multi-step API-controleregel](/support/kb/synthetic-monitoring/api-monitoring/multi-step). Een XPath-query definieert welk deel van de XML-respons u interesseert - meestal een waarde die is opgenomen in een van de XML-nodes. U kunt dan die geëxtraheerde waarde nemen en (gebruikmakend van assertions) controleren of deze [aan bepaalde voorwaarden voldoet](/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions) of [deze opslaan in een variabele](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variabelen) voor later gebruik.

De XPath-versie die in configuraties van Multi-step API-controleregels wordt gebruikt is XPath 1.0, wat betekent dat functies die in hogere XPath-versies zijn geïntroduceerd niet worden ondersteund.

## Voorbeeld 1: Gewone XML

Stel u een API of webservice voor die informatie over een productvoorraad kan retourneren. Als we een request naar die API sturen, retourneert deze data over een of meer producten. Stel dat de API dit heel eenvoudige XML-document retourneert wanneer we data opvragen over product P-12345:

    <?xml version="1.0" encoding="utf-8"?>
      <Products>
        <ProductInfo Id="P-12345">
          <Name>Product 12345</Name>
          <Price>99.90</Price>
        </ProductInfo>
      </Products>

De root node is **Products**, en erbinnen bevindt zich één enkele **ProductInfo** node die het door ons gevraagde product aanduidt. Daarbinnen bevinden zich vervolgens een **Name** node en een **Price** node, die beiden enige tekstinhoud bevatten.

Zodra we dit XML-document van de API ontvangen, kunnen we de inhoud ervan verifiëren om te controleren of de API correct werkt. We kunnen bijvoorbeeld door dit document 'navigeren', helemaal tot aan de **Name** node, om de naam van het product te extraheren. De volgende XPath-query haalt die waarde op:

`/Products/ProductInfo/Name/text()`

U ziet dat in dit voorbeeld elke node in de hiërarchie wordt vermeld om bij de **Name** node te komen, en dat ten slotte de functie **text()** wordt gebruikt om de inner text van die **Name** node op te halen.

Als we deze XPath-query in een Multi-step API Assertion gebruiken, kunnen we controleren of de waarde inderdaad bestaat in het XML-document, en of het de waarde is die we verwachtten:

![](/img/content/scr-MSA-xpath-assertion-example.min.png)

## Voorbeeld 2: Een SOAP Envelope met prefixen

Als uw API een SOAP-webservice is, kan de XML die deze retourneert er zo uitzien:

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

U ziet dat dit XML-document niet alleen de gebruikelijke *xmlns* namespace attributes bevat die u verwacht te zien in een SOAP XML, maar ook een prefixed namespace **xmlns:product** die de inner nodes beschrijft die de productinformatie bevatten. Als gevolg hiervan heeft elke node, vanaf de **Envelope** helemaal tot aan de productdata, een prefix. De SOAP **Envelope** en **Body** nodes gebruiken de prefix **soap:**, de **GetProductInfoResponse** node en al zijn inner nodes gebruiken de prefix **product:**.

Hiermee kunnen we een XPath-query definiëren die een volledig gekwalificeerde node selector heeft voor elke node in het pad dat we willen selecteren. De volgende XPath-query retourneert de waarde 99.90:

`/soap:Envelope/soap:Body/product:GetProductInfoResponse/product:GetProductInfoResult/product:ProductInfo/product:Price/text()`

U ziet dat we elke prefix voor elke node in onze query moeten opnemen. Als we er één weglaten, mislukt de XPath-query omdat XPath 1.0 vereist dat we verwijzen naar de volledige naam van elke node, inclusief zijn prefix. Toch kunnen we deze query nog verder vereenvoudigen omdat er maar één product in het document is en slechts één **Price** node. Aangezien hier geen dubbelzinnigheid bestaat, kunnen we meteen naar de **Price** node navigeren met behulp van de descendant operator //:

`//product:Price/text()`

U ziet dat we nog steeds de prefix **product:** moeten vermelden.

Tot dusver hebben we de inner text van een node geëxtraheerd. Wilt u in plaats daarvan de waarde van een attribute (zoals de Id attribute met waarde "P-12345") extraheren? Dan kunt u gewoon de XPath @ operator gebruiken. Deze XPath-query retourneert de waarde P-12345:

`//product:ProductInfo/@Id`

## Voorbeeld 3: SOAP-data met meerdere objecten

In ons vorige voorbeeld was er geen dubbelzinnigheid omdat alles een prefix had en er slechts één **product:ProductInfo** object in ons XML-document voorkwam. Maar wat als we nu een SOAP methode hebben die een lijst met objecten retourneert? Bekijk dit XML-document met meer dan één product (slechts twee om het kort te houden):

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
              <product:ProductInfo Id="P-24680">
                <product:Name>Product 24680</product:Name>
                <product:Price>45.99</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

Als we naar het allereerste product willen en de prijs ervan willen selecteren, kunnen we de volgende query gebruiken die 99.90 retourneert. Vergeet niet dat XPath arrays gebaseerd zijn op 1, dus gebruiken we een indexwaarde van 1:

`//product:ProductInfo[1]/product:Price/text()`

Op dezelfde manier kunnen we de prijs van het laatste product selecteren, die 45.99 retourneert:

`//product:ProductInfo[last()]/product:Price/text()`

We kunnen zelfs een product selecteren op basis van zijn Product **Id** attribute. Deze query vindt een product met een Id van P-24680 en selecteert zijn prijs - en retourneert 45.99:

`//product:ProductInfo[@Id="P-24680"]/product:Price/text()`

## Voorbeeld 4: XML-data met lege prefixen

Voor dit voorbeeld gebruiken we opnieuw SOAP data, maar het is van toepassing op elk XML-document met dezelfde kenmerken. In onze vorige SOAP-voorbeelden hadden we het geluk dat elke node een prefix had. Maar de XML-respons van uw API kan XML retourneren die niet overal een prefix bevat.

In XPath 1.0 moet elke node die afhankelijk is van een namespace inclusief zijn prefix worden gespecificeerd. Dit wordt moeilijk wanneer sommige nodes een lege prefix hebben. U kunt geen lege prefix specificeren in een XPath query, dus het selecteren van die nodes wordt lastig.

Bekijk de volgende XML, die prefixen heeft voor de SOAP Envelope en Body, maar niet voor de inner nodes. U ziet dat er geen extra namespace is gedefinieerd voor de product nodes:

`<?xml version="1.0" encoding="utf-8"?>  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">    <soap:Body>      <GetProductInfoResponse>        <GetProductInfoResult>          <ProductInfo Id="P-12345">            <Name>Product 12345</Name>            <Price>99.90</Price>          </ProductInfo>        </GetProductInfoResult>      </GetProductInfoResponse>    </soap:Body>  </soap:Envelope>`

Dit werkt nog steeds zoals verwacht, omdat de nodes zonder prefix niet afhankelijk zijn van een namespace. Deze XPath query retourneert 99.90:

`//Price/text()`

Nu kijken we naar een variant die een extra namespace heeft. U ziet dat de attribute xmlns="http://myproduct.com" op de root level geen prefix specificeert (dat wil zeggen dat het een lege prefix heeft):

`<?xml version="1.0" encoding="utf-8"?>  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"`

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
          <GetProductInfoResponse>
            <GetProductInfoResult>
              <ProductInfo Id="P-12345">
                <Name>Product 12345</Name>
                <Price>99.90</Price>
              </ProductInfo>
            </GetProductInfoResult>
          </GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

In dit geval zijn de inner nodes afhankelijk van die namespace, maar we kunnen ze niet op de gewone manier selecteren, omdat de prefix van hun namespace leeg is. Daarom werkt de volgende query niet en retourneert die eenvoudigweg een lege waarde:

`//Price/text()`

Helaas is het niet mogelijk om een lege prefix op te nemen in een XPath query. Maar gelukkig is er wel een manier om het probleem met de lege prefix te vermijden. We kunnen de XPath-functie **local-name()** gebruiken waarmee we een node kunnen selecteren door zijn naam te gebruiken, zonder de prefix te hoeven specificeren:

`//*[local-name()="Price"]/text()`

De structuur van deze query is:

// descendant operator: selecteer alle descendant nodes vanaf de root  
\* wildcard operator: elke node, ongeacht de naam van de node  
`[local-name()="Price"]`: selecteer alleen nodes die een lokale naam hebben (d.w.z. zonder prefix) die gelijk is aan Price  
`text()`: selecteer de inner text van de geselecteerde node(s)

Vergeleken met onze vorige voorbeelden die meerdere ProductInfo nodes in de XML hadden, kunnen we verschillende strategieën combineren voor het selecteren van de nodes waarin we geïnteresseerd zijn. Deze query selecteert de node ProductInfo met Id gelijk aan P-24680 en krijgt dan de inner text van zijn Price node:

`//*[local-name()="ProductInfo"][@Id="P-24680"]/*[local-name()="Price"]/text()`

## Voorbeeld 5: XPath-functies

In de vorige voorbeelden werden XPath query's gebruikt om het bestaan van een of meer nodes in een XML-document te verifiëren en de inhoud van een node of node attribute te retourneren. Naast het vinden van nodes en hun inhoud, laat XPath u ook bepaalde functies uitvoeren. Hieronder staan enkele voorbeelden waarin er rekening mee wordt gehouden dat alleen XPath 1.0-functies beschikbaar zijn:

| **Functie**                                                                                                                                                                                                                                                                                                                      | **Voorbeeldquery**                    | **Waarde** |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|------------|
| De functie **count()** telt hoeveel nodes er worden gevonden met behulp van het argument dat u specificeert. Deze retourneert een numerieke waarde die u kunt gebruiken in een assertion. U kunt bijvoorbeeld een assertion opstellen die controleert of het aantal geretourneerde producten groter is dan of gelijk is aan 100. | count(//ProductInfo)                  | 2          |
| De functie **contains()** controleert of de geselecteerde stringwaarde de substring bevat die u specificeert. Retourneert True of False.                                                                                                                                                                                         | contains(//ProductInfo/Name, "12345") | True       |
| De functie **contains()** controleert of de geselecteerde stringwaarde de substring bevat die u specificeert. Retourneert True of False.                                                                                                                                                                                         | sum(//ProductInfo/Price)              | 145.89     |
