{
  "hero": {
    "title": "Onbevestigde en bevestigde fouten"
  },
  "title": "Onbevestigde en bevestigde fouten",
  "summary": "Wat zijn onbevestigde en bevestigde fouten en hoe tellen ze mee voor de berekende downtime?",
  "url": "[URL_BASE_TOPICS]alerting/fouten/onbevestigde-en-bevestigde-fouten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Een van de enorme voordelen van het gebruik van Uptrends voor server- en websitemonitoring is de mogelijkheid uw team op de hoogte te houden van aan downtime of performance gerelateerde gebeurtenissen. Maar wat is nu precies het verschil tussen een onbevestigde en bevestigde fout?

## Het verschil tussen een onbevestigde en een bevestigde fout

Een **onbevestigde fout** is een fout die is gerapporteerd na controle van een controleregel vanuit één controlestation, maar die nog geverifieerd moet worden door een tweede controlestationlocatie.

Een **bevestigde fout** is een fout die door twee controlestationlocaties is geverifieerd.

Deze **dubbele controle van downtime** helpt voorkomen dat er valse alerts worden gemaakt. Bevestigt de tweede controle een fout niet, dan wordt aangenomen dat de eerste onbevestigde fout een tijdelijk probleem was.

[SHORTCODE_1]
**Opmerking**: Onbevestigde fouten worden geel weergegeven in het dashboard Controleregel log. Bevestigde fouten worden rood weergegeven. Geen fouten worden groen weergegeven.
[SHORTCODE_2]

## Hoe fouten bijdragen aan downtime en alerting

Het is belangrijk te weten dat in de Uptrends-service alleen bevestigde (tweemaal gecontroleerde) fouten worden meegerekend in het downtime alertsysteem.

Om te bepalen wanneer een alert moet worden verstuurd kunt u de standaard alertdefinitie bewerken of er zelf een maken. Meer informatie over alertdefinities vindt u in het artikel [Alertdefinities]([LINK_URL_1]).
