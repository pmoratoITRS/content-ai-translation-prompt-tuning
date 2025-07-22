{
  "hero": {
    "title": "Monitor API"
  },
  "title": "Monitor API",
  "url": "/support/kb/api/monitor-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitor-api"
}

De eindpunten die deel uitmaken van de Monitor API helpen u bij het beheren van uw controleregelinstellingen in Uptrends. *Controleregels* zijn de dingen die u definieert in Uptrends om te beschrijven wat moet worden gemonitord. Doorgaans controleert een controleregel een enkele webpagina of een reeks API calls of een klikpad van een eindgebruiker op een website.

De Monitor API heeft verschillende eindpunten waarmee u controleregeldefinities kunt creëren, wijzigen, klonen of verwijderen. Deze eindpunten worden hieronder beschreven.

## Aan de slag gaan

-   Voor toegang tot de API hebt u een API-account nodig.
-   U kunt de Monitor API-eindpunten ontdekken/uitproberen in onze [Swagger environment](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor).
-   Elke API-methode wordt hieronder beschreven.
-   Voor de meeste van deze methoden werkt u met een monitorobject dat de instellingen voor een controleregel bevat. U kunt de juiste instellingen en velden bekijken in het artikel [monitor API velden](/support/kb/api/monitor-api-velden).

## GET /Monitor

Retourneert de lijst met controleregels die momenteel aanwezig zijn in de account.

`GET /Monitor`

Response body:

    [
    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // More fields here
    },
    // More monitors here
    ]

## GET /Monitor/{monitorGuid}

Retourneert een enkele controleregel, geïdentificeerd door de gespecificeerde monitorGuid.

`GET /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Response body:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // More fields here
    }

## PATCH /Monitor/{monitorGuid}

Werkt de definitie van de gespecificeerde controleregel bij. De request body van deze request bevat naar verwachting een gedeeltelijke lijst van velden die u wilt bijwerken. U gebruikt deze request meestal om slechts een of enkele velden bij te werken. Geef in de request body alleen de velden op die u wilt bijwerken. Het opnemen van het veld MonitorGuid is optioneel. Als u het specificeert, moet het overeenkomen met de MonitorGuid die u specificeert in de URL.

De volgende PATCH request wordt gebruikt om een controleregel te deactiveren door een nieuwe waarde voor zijn veld `IsActive` te specificeren.

`PATCH /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Request body:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "IsActive": false
    }

## PUT /Monitor/{monitorGuid}

Werkt de definitie van de gespecificeerde controleregel bij. De request body voor deze request bevat naar verwachting de volledige lijst met alle controleregelvelden. Doorgaans voert u eerst een GET-request uit om de bestaande definitie van de controleregel die u wilt bijwerken te verkrijgen, de nodige wijzigingen in die inhoud aan te brengen en terug te sturen met deze PUT-request.

De volgende PUT-request wordt gebruikt om de velden `Name` en `IsActive` van de controleregel te wijzigen, maar de andere velden moeten ook worden vermeld omdat we een PUT-request doen, geen gedeeltelijke PATCH-request.

`PUT /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

Request body:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts product page",
    "IsActive": false,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // Remaining fields here    
    }

## POST /Monitor

Creëert een nieuwe controleregel. De request body voor deze request bevat naar verwachting de volledige lijst met alle controleregelvelden die geschikt zijn voor het type controleregel dat u aan het maken bent.

Als u voor het eerst een API-request zoals deze creëert, kan het handig zijn om eerst een controleregel in de Uptrends-toepassing te creëren, de definitie voor die controleregel op te halen met een GET-request en de structuur van die controleregeldefinitie als een voorbeeld te inspecteren.

De volgende POST-request wordt gebruikt om een gewone HTTPS-controleregel te maken die op controlestations in Europa wordt uitgevoerd:

`POST /Monitor`

Request body:

    {
    "Name": "My new monitor",
    "IsActive": true,
    "GenerateAlert": true,
    "IsLocked": false,
    "CheckInterval": 5,
    "MonitorMode": "Production",
    "CustomFields": [],
    "SelectedCheckpoints": {
        "Regions": [
        1004
        ]
    },
    "UsePrimaryCheckpointsOnly": true,
    "MonitorType": "Https",
    "Notes": "Monitors uptime for the homepage",
    "AlertOnLoadTimeLimit1": true,
    "LoadTimeLimit1": 2500,
    "AlertOnLoadTimeLimit2": true,
    "LoadTimeLimit2": 5000,
    "RequestHeaders": [],
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
    "Username": "",
    "AuthenticationType": "None",
    "CheckCertificateErrors": true,
    "IpVersion": "IpV4",
    "AlertOnMinimumBytes": false,
    "MinimumBytes": 0,
    "HttpMethod": "Get",
    "CheckHttpStatusCode": false,
    "ExpectedHttpStatusCode": 401,
    "TlsVersion": "Tls12_Tls11_Tls10",
    "RequestBody": "",
    "Url": "https://galacticresorts.com"
    }

## DELETE /Monitor/{monitorGuid}

Verwijdert de gespecificeerde controleregel.

`DELETE /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e`

## POST /Monitor/{monitorGuid}/Clone

Maakt een kloon (duplicaat) van de gespecificeerde controleregel. De gekopieerde controleregel is in eerste instantie inactief, dus u kunt wijzigingen aanbrengen voordat u hem activeert.

### Optionele parameters

-   **includeMaintenancePeriods**: true of false (standaard: true). Geeft aan of de bestaande onderhoudsperioden van de broncontroleregel ook naar de kloon moeten worden gekopieerd.
-   **includeMonitorGroups**: true of false (standaard: true). Geeft aan of de leden van de controleregelgroep ook naar de kloon moeten worden gekopieerd. Als true is gespecificeerd, zal de nieuwe kopie deel uitmaken van dezelfde controleregelgroepen als de broncontroleregel. Als false is gespecificeerd, zal deze alleen deel uitmaken van de groep *Alle controleregels*.

De volgende POST-request creëert een kopie van een bestaande controleregel en specificeert dat de onderhoudsperioden niet moeten worden gekopieerd van de bron, maar dat de nieuwe controleregel wel deel moet uitmaken van dezelfde controleregelgroepen.

`POST /Monitor/1d2f5fac-730c-45b0-a077-4ab82aaee14e/Clone?includeMaintenancePeriods=false&includeMonitorGroups=true`

## Andere API's gerelateerd aan controleregels

-   Bent u op zoek naar controleregeldata (d.w.z. data van controleregelchecks geproduceerd door een controleregel), kijk dan op de [MonitorCheck API](/support/kb/api/monitorcheck-api).
-   Controleregels kunnen worden georganiseerd in groepen. Bekijk de [MonitorGroup API](/support/kb/api/monitorgroup-api).
-   Controleregels hebben geautomatiseerde aan/uit-schema's genaamd *Onderhoudsperioden*. Bekijk de [Onderhoudsperioden in de API](/support/kb/api/onderhoudsperioden-in-de-api).
