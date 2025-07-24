{
  "hero": {
    "title": "Krijg controlestationdata in JSON- of XML-formaat"
  },
  "title": "Krijg controlestationdata in JSON- of XML-formaat",
  "summary": "Wanneer u de Uptrends API gebruikt om controlestation informatie op te vragen, kunt u die informatie in verschillende formaten krijgen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controlestations/haal-controlestationdata-op-in-de-formaten-json-csv-xml",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

JSON- of XML-downloads van controlestationdata zijn beschikbaar via onze API. De volledige documentatie over de API kunt u bekijken op [deze pagina]([LINK_URL_1])).

U kunt onze API gebruiken om de lijsten met IPv4- of IPv6-adressen voor al Uptrends' controlestations op te vragen, inclusief de aankomende adressen van gewijzigde of nieuwe controlestations. Responses zijn beschikbaar in zowel JSON als XML, afhankelijk van uw [INLINE_CODE_1] header. 

We bieden ook eenvoudige lijsten met [IPv4-adressen]([LINK_URL_2]) en [IPv6-adressen]([LINK_URL_3]) om te downloaden.

Alle methoden en koppelingen die op deze pagina worden vermeld, leveren een lijst op met IP-adressen van controlestations, waaronder **aanstaande adressen** (zoals aangekondigd in onze maandelijkse controlestation-nieuwsbrief). 

#### Voor een lijst met IPv4-adressen:
Stuur een GET request naar [INLINE_CODE_2] met header [INLINE_CODE_3]. Er is geen authenticatie vereist. 

Als u *curl* gebruikt, is dit een voorbeeld: 
[CODE_BLOCK_1]

Vervang *application/json* door *application/xml* als u een XML response nodig heeft.

#### Voor een lijst met IPv6-adressen: 
Hetzelfde als voor IPv4, behalve dat de request naar [INLINE_CODE_4] moet worden gestuurd.


[SHORTCODE_1]
**Tip:** In plaats van *curl* kunt u een powershell Invoke-Webrequest gebruiken.
[SHORTCODE_2]
