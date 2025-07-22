{
  "hero": {
    "title": "Berichtopmaak"
  },
  "title": "Berichtopmaak",
  "summary": "Aanpasbare integraties - Hoe u uw bericht correct opmaakt",
  "url": "/support/kb/alerting/integraties/aangepaste-integraties/berichtopmaak",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/message-formatting" 
}

Aangezien het uitgaande alertbericht meestal in JSON zal zijn opgemaakt, moeten we regels volgen zodat deze JSON geldig blijft. Daarvoor moeten bepaalde tekens (zoals regeleinden of aanhalingstekens) worden gecodeerd voordat ze kunnen worden opgenomen in het uitgaande, JSON-geformatteerde alertbericht. Gebeurt dit niet, dan maken ze de JSON-structuur van het uitgaande bericht ongeldig, wat ertoe kan leiden dat het ontvangende eindpunt een fout genereert en de binnenkomende alert niet correct verwerkt. Dit artikel gaat over de ingebouwde functies voor automatische berichtopmaak.

## Automatische opmaak toepassen {id="applying-automatic-formatting"}

Als bijvoorbeeld het ‘Notities’-veld van een controleregel (die u aan het alertbericht kunt toevoegen met de systeemvariabele @monitor.notes) dergelijke tekens bevat (regeleinden, aanhalingstekens, ...), wordt dit op zodanige wijze afgehandeld dat de JSON-structuur van het uitgaande bericht zou worden verbroken.  
  
Een voorbeeld:  
`{ "notes": "{{@monitor.notes}}" }`  

Zou afgehandeld kunnen worden tot:  
```json
{ "notes": "Monitor notes that include 
 a line break or "a quote"" }
 ```
  
Dit verbreekt geldige JSON-structuur en zal waarschijnlijk leiden tot onjuiste afhandeling van de alert aan de ontvangende kant. Om dit probleem op te lossen hebben we de optie opgenomen om stukjes tekst te coderen (of te decoderen) om correct in een JSON- of XML-geformatteerd bericht te passen. Wordt deze functie gebruikt, dan worden alle tekens die moeten worden voorzien van escape-tekens om de JSON geldig te houden, automatisch gecodeerd.  
  
Om deze functie te gebruiken verpakt u de gewenste systeemvariabele of tekst in de volgende syntax:  
`{{@JsonEncode(your-variable-here)}}`  
  
Zo moet bijvoorbeeld de eerder genoemde systeemvariabele van de controleregelnotities als volgt worden verpakt:  
`{ "Notes": "{{@JsonEncode({{@monitor.notes}})}}"}`  
  
Met de functie @JsonEncode, wordt het eerder genoemde stukje JSON dat de verwijzing naar de controleregelnotities bevat, afgehandeld tot:  
`{ "notes": "Monitor notes that include\na line break or \"a quote\"" }`  
  
Zoals u ziet, hebben we de controleregelnotities nu correct opgenomen, zodanig gecodeerd dat de JSON-structuur niet wordt verbroken.  
  
Gebruikt u XML in plaats van JSON, dan hoeft u niet bang te zijn – we ondersteunen een vergelijkbare functie voor XML-codering! U kunt deze functie gebruiken door uw gewenste systeemvariabelen te verpakken in `{{@XmlEncode()}}`.
