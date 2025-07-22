{
  "hero": {
    "title": "Krijg controlestationdata in JSON- of XML-formaat"
  },
  "title": "Krijg controlestationdata in JSON- of XML-formaat",
  "summary": "Wanneer u de Uptrends API gebruikt om controlestation informatie op te vragen, kunt u die informatie in verschillende formaten krijgen.",
  "url": "/support/kb/synthetic-monitoring/controlestations/haal-controlestationdata-op-in-de-formaten-json-csv-xml",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/get-checkpoint-data-in-json-and-xml-format",
  "TableOfContents": false
}

JSON- of XML-downloads van controlestationdata zijn beschikbaar via onze API. De volledige documentatie over de API kunt u bekijken op [deze pagina]({{< ref path="support/kb/api" lang="nl" >}})).

U kunt onze API gebruiken om de lijsten met IPv4- of IPv6-adressen voor al Uptrends' controlestations op te vragen, inclusief de aankomende adressen van gewijzigde of nieuwe controlestations. Responses zijn beschikbaar in zowel JSON als XML, afhankelijk van uw `Accept` header. 

We bieden ook eenvoudige lijsten met [IPv4-adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv4) en [IPv6-adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv6) om te downloaden.

Alle methoden en koppelingen die op deze pagina worden vermeld, leveren een lijst op met IP-adressen van controlestations, waaronder **aanstaande adressen** (zoals aangekondigd in onze maandelijkse controlestation-nieuwsbrief). 

#### Voor een lijst met IPv4-adressen:
Stuur een GET request naar `https://api.uptrends.com/v4/Checkpoint/Server/Ipv4` met header `Accept: application/json`. Er is geen authenticatie vereist. 

Als u *curl* gebruikt, is dit een voorbeeld: 
```
curl -X GET -H "accept: application/json" https://api.uptrends.com/v4/Checkpoint/Server/Ipv4
```

Vervang *application/json* door *application/xml* als u een XML response nodig heeft.

#### Voor een lijst met IPv6-adressen: 
Hetzelfde als voor IPv4, behalve dat de request naar `https://api.uptrends.com/v4/Checkpoint/Server/Ipv6` moet worden gestuurd.


{{< callout >}}
**Tip:** In plaats van *curl* kunt u een powershell Invoke-Webrequest gebruiken.
{{< /callout >}}
