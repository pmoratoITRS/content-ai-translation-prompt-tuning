{
  "hero": {
    "title": "API changelog"
  },
  "title": "API changelog",
  "summary": "Bekijk de wijzigingen, updates en verbeteringen voor de Uptrends API",
  "url": "/support/kb/api/changelog",
  "translationKey": "https://www.uptrends.com/support/kb/api/changelog",
  "type": "story" 
}

{{< Features/Story >}}

Uptrends' API zal in de loop van de tijd worden verbeterd en uitgebreid. We zullen nieuwe eindpunten en methoden toevoegen voor nieuwe functionaliteit.

Bij het toevoegen van nieuwe functionaliteit streven wij ernaar achterwaarts compatibel te blijven. Soms is verandering echter onvermijdelijk en is een nieuwe versie van de API mogelijk niet compatibel met wat u tot nu toe heeft gecodeerd en gebruikt. Bekijk de API Changelog regelmatig om op de hoogte te blijven van alle wijzigingen en waar nodig op wijzigingen te reageren.

Als u de documentatie van de API zoekt, bekijk dan de artikelen in de categorie [Uptrends' API]({{< ref path="support/kb/api" lang="nl" >}}).

Bent u ook geïnteresseerd in de wijzigingen in de Uptrends-app, bekijk dan de [algemene changelog]({{< ref path="/changelog" lang="nl" >}}).

## Mei 2025

### Aankomende belangrijke wijziging: verwijdering van API-velden

Als onderdeel van onze voortdurende inspanningen om de Uptrends API te optimaliseren, worden specifieke velden in de volgende [Monitor](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor)-eindpunten met ingang van **27 augustus 2025** verwijderd:

- `GET` en `POST` `/Monitor`
- `GET`, `PUT` en `PATCH` `/Monitor/{monitorGuid}`
- `GET` en `POST` `/Monitor/MonitorGroup/{monitorGroupGuid}`

De volgende verouderde velden worden nu behandeld als [Types foutcondities]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview" lang="nl" >}}) onder de array `ErrorConditions`. Gerelateerde velden worden samengevoegd tot één entry, ter vervanging van hun eerdere gebruik als individuele velden:

| Verouderde velden | Vervangende velden |
|--|--|
| `AlertOnLoadTimeLimit1`, `LoadTimeLimit1`| {{< tableformatter >}} [LoadTimeLimit1]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}}) |
| `AlertOnLoadTimeLimit2`, `LoadTimeLimit2` | [LoadTimeLimit2]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}}) |
|`AlertOnMaximumBytes`, `MaximumBytes` | [TotalMaxBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="nl" >}}) |
|`AlertOnMinimumBytes`, `MinimumBytes` | [TotalMinBytes]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-the-sum-of-all-resources-together-full-page-check" lang="nl" >}}) | 
|`AlertOnMaximumSize`, `ElementMaximumSize` | [PageElementMaxSizeWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="nl" >}}) |
|`AlertOnPercentageFail`, `FailedObjectPercentage` | [PageElementFailedWithPercentage]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources#check-each-resource-individually-full-page-check" lang="nl" >}})
|`ExpectedHttpStatusCode`, `ExpectedHttpStatusCodeSpecified` | [HttpStatus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="nl" >}}) |

Hieronder ziet u een voorbeeld van de bijgewerkte API-respons. Het is raadzaam uw API-aanroepen aan te passen om de `ErrorConditions`-array te gebruiken. Dit is afgestemd op de nieuwste API-structuur en zorgt voor correcte API-functionaliteit.

```json
{
  ...
  "ErrorConditions": [
    {
      "ErrorConditionType": "LoadTimeLimit1",
      "Value": "2500",
      "Effect": "Indicate"
    },
    {
      "ErrorConditionType": "LoadTimeLimit2",
      "Value": "5000",
      "Effect": "Error"
    },
    {
      "ErrorConditionType": "TotalMaxBytes",
      "Value": "5000000"
    },
    {
      "ErrorConditionType": "TotalMinBytes",
      "Value": "5000"
    },
    {
      "ErrorConditionType": "PageElementMaxSizeWithPercentage",
      "Value": "200000",
      "Percentage": "10"
    },
    {
      "ErrorConditionType": "PageElementFailedWithPercentage",
      "Percentage": "10"
    },
    { "ErrorConditionType": "HttpStatus",       
      "Value": "200"     
    }
  ],
 ...
}
```

### Update Persoonlijk Controlestationstatus

Het eindpunt `GET /PrivateCheckpointHealth` retourneert nu het veld `Warnings`, dat alle waarschuwingsinformatie bevat die is gekoppeld aan het controlestation van de server. Raadpleeg voor meer informatie de Engelstalige [Uptrends API v4 Private location Checkpoint health-documentatie](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/PrivateLocation/PrivateLocation_GetSpecifiedPrivateCheckpointHealth).

## April 2025

### Introductie van de Persoonlijke locaties API

Er is een nieuwe set API-eindpunten toegevoegd om u te helpen uw Persoonlijke locaties-configuratie te beheren, inclusief status- en controlestationinformatie. Raadpleeg voor meer informatie de [Uptrends API v4 Persoonlijke locaties-documentatie](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json).

## Maart 2025

### Update Monitor Group API 

Het eindpunt `/MonitorGroup` retourneert nu het aantal gebruikte credits per [controleregeltype]({{< ref path="/support/kb/basics/monitor-types" lang="nl" >}}):
- `UsedBasicMonitorQuota` — retourneert het aantal credits dat wordt gebruikt voor [Uptime- of Basiscontroleregels]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}}).
- `UsedBrowserMonitorQuota` — retourneert het aantal credits dat wordt gebruikt voor [Browser- of Full Page Check (FPC)-controleregels]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="nl" >}}).
- `UsedTransactionMonitorQuota` — retourneert het aantal credits dat wordt gebruikt voor [Transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}).
- `UsedApiMonitorQuota` — retourneert het aantal credits dat wordt gebruikt voor [Multi-step API (MSA)-]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) en [Postman-]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="nl" >}})controleregels.

Voorheen retourneerde de MonitorGroup API alleen het totale aantal credits dat beschikbaar was voor de groep voor elke controleregelcategorie. Nu retourneert het ook het aantal credits dat in de groep wordt gebruikt voor elke controleregelcategorie.

## Februari 2025

### Update Cursor-parameterwaarde 

De API Cursor-parameter is een tekenreekswaarde die werkt als aanwijzer om data uit de API-respons te doorlopen.

Cursors zijn nu bijgewerkt naar een langere tekenreeksindeling om veiligere dataverwerking te garanderen. Alle nieuw gecreëerde cursors volgen nu het nieuwe formaat en de in het oude formaat gemaakte cursors blijven werken tot 1 april 2025. Na deze periode zijn oude cursors niet meer beschikbaar voor gebruik. Het wordt aanbevolen om nieuwe cursorwaarden te genereren om ze up-to-date te houden en te laten werken zoals verwacht.

Merk op dat de Cursor-parameter beschikbaar is in de eindpunten [MonitorCheck API]({{< ref path="/support/kb/api/monitorcheck-api" lang="nl" >}}) en Alert API.

## Januari 2025

### Update Monitor API

Het eindpunt `/Monitor` retourneert nu de `LastModifiedDate`, die de datum en tijd bevat waarop de controleregel voor het laatst is bijgewerkt. Voorheen kon alleen de `CreatedDate` worden opgehaald uit de Monitor API.

## November 2024

### Update VaultItem

De `POST/v4/VaultItem`, `PUT/v4/VaultItem/{vaultItemGuid}` en `PATCH/v4/VaultItem/{vaultItemGuid}` accepteren nu het veld `SecretEncodingMethod` bij het bijwerken of creëren van het vault-item [Configuratie eenmalig wachtwoord]({{< ref path="/support/kb/account/vault#one-time-password" lang="nl" >}}). Dit nieuwe veld accepteert *Hex* of *Base32* als tekenreekswaarden. De *Base32*-indeling is de standaard codeermethode als het veld `SecretEncodingMethod` niet is gespecificeerd.

## September 2024

### Update Vault-item

De `GET /v4/VaultItem` retourneert nu een extra data-item, `VaultItemUsedBy` dat details retourneert over welke items of controleregels elk vault-item gebruiken.

## Augustus 2024

### Checkpoint API

Het API-eindpunt `/Checkpoint/Server/{serverId}` retourneert nu ook persoonlijke-locatieservers.

### Update VaultItem 

Het eindpunt `GET /v4/VaultItem` kan nu voor elk vault-item dezelfde mate van details retourneren, vergelijkbaar met hoe details worden geretourneerd voor een enkel item in een `GET /v4/VaultItem/{GUID}`.

## Juni 2024

### Belangrijke wijziging: de /Register API voor SSO-only operators

De Uptrends API vereist [registratie]({{< ref path="/support/kb/api/authentication-v4" lang="nl" >}}) voordat deze kan worden gebruikt. Operators kunnen een set API-specifieke inloggegevens creëren, op basis van hun reguliere Uptrends-inloggegevens. Er zijn twee manieren om een set API-inloggegevens te registreren:

- Operators kunnen gebruikmaken van de reguliere Uptrends-interface en een API-gebruiker toevoegen via het tabblad {{< AppElement type="tab" >}}API management{{< /AppElement >}} in hun operatorinstellingen.
- Operators kunnen zich ook registreren voor inloggegevens in de API zelf, via een request `POST /Register` door hun reguliere Uptrends-inloggegevens te verstrekken.

Vanaf deze update kunnen operators die alleen [kunnen inloggen met Single sign-on (SSO)]({{< ref path="/support/kb/account/settings/single-sign-on-overview" lang="nl" >}}) niet langer proberen gebruik te maken van deze tweede optie voor het registreren van API-inloggegevens, aangezien ze geen 'reguliere' Uptrends-inloggegevens hebben om te gebruiken. 

In dergelijke gevallen raden we aan een apart operatoraccount aan te maken en dat te gebruiken om te registreren voor API-inloggegevens. 

## Oktober 2023

### Belangrijke wijziging: statistieken voor het laden van pagina's voor browsergebaseerde monitoring

**Opmerking:** Het volgende is een **belangrijke wijziging** in de *MonitorCheck* API. De wijziging gaat live op **woensdag 8 november**.

De Uptrends [MonitorCheck API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorCheck) kan worden gebruikt om gedetailleerde informatie op te halen over individuele controleregelchecks. Voor browsergebaseerde monitoring kan de [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}) worden opgehaald via de call `GET /MonitorCheck/{monitorCheckId}/Waterfall`, die alle watervalmetingen retourneert, inclusief [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) en [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}), als die aanwezig zijn in het controleresultaat. 

Momenteel retourneert de MonitorCheck API Core Web Vitals en W3C Navigatietijden in twee afzonderlijke JSON-objecten: `PageLoadMetrics` en `W3CNavigationTiming`. Voortaan zullen deze afzonderlijke objecten als volgt worden gecombineerd tot één enkele array, `PageLoadMetricsCollection`:

```json
  "Attributes": {
    "PageLoadMetricsCollection": [
      {
        "CumulativeLayoutShift": 0.029,
        "FirstContentfulPaint": 2914,
        "LargestContentfulPaint": 3014,
        "TotalBlockingTime": 819,
        "TimeToInteractive": 12516,
        "TimeToFirstByte": 2068,
        "SendStart": 2059,
        "LoadEventEnd": 6721,
        "DomInteractive": 2652,
        "DomComplete": 6719
      }
    ],
    ...
    }
```


### Variabelen in alertdefinities specificeren via de API

Bij het configureren van [alerting]({{< ref path="/support/kb/alerting" lang="nl" >}}) via een [aanpasbare integratie]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="nl" >}}) in Uptrends kunnen operators de gebruikersinterface gebruiken om bepaalde vereiste variabelen te specificeren [in het escalatieniveau van de alertdefinitie]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#specifying-variables-per-escalation-level" lang="nl" >}}) in plaats van in de integratieopties. Hierdoor kunnen gebruikers één enkele integratie voor verschillende scenario's gebruiken, zoals het versturen van alerts voor verschillende sets controleregels naar verschillende teams, maar met dezelfde berichtinhoud.

Wanneer de optie om variabelen te specificeren in het escalatieniveau is geselecteerd in de integratie-instellingen, moeten de variabelen in plaats daarvan worden geconfigureerd wanneer de integratie is ingesteld voor gebruik in de instellingen van de alertdefinitie. Om dit te doen verschijnt er een extra tekstveld in de integratieselectielijst in de alertdefinitie-instellingen. 

Tot nu toe was deze optie niet beschikbaar bij het configureren van alertdefinities via de API. We hebben een nieuwe optie toegevoegd aan het `/AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration` request (waar u configureert welke integraties zijn gekoppeld aan elk escalatieniveau in de alertdefinitie). De nieuwe eigenschap wordt:

```json
{
    ...
    "VariableValues": {
        "ApiUrl": "https://api.escalationlevel-specific-url.com/alerts"
    },
    ...
}
```

Deze eigenschap is het equivalent van deze optie in de gebruikersinterface van de applicatie:

![Integratievariabele configureren in alertdefinitie](/img/content/scr-api-cl-conf-variables-in-escalation-level.min.png)


## September 2023

### Wijziging in IPv6-adressen van controlestations

Wanneer voorheen de checkpoint API werd gebruikt om controlestationinformatie op te halen, werden de IPv4-adressen van het controlestation weergegeven als een eenvoudige lijst in een array, terwijl de IPv6-adressen (indien van toepassing) een lijst met objecten waren. Zo werden de IP-adressen van het Amsterdamse controlestation voorheen als volgt weergegeven:

```
     "Ipv4Addresses": [
        "178.217.84.4",
        "188.241.149.95",
        "66.212.22.2",
        "185.145.63.225",
        "5.182.210.227",
        "5.182.210.168"
    ],
    "IpV6Addresses": [
        {
            "IpAddress": "2a01:5cc0:1:2::4"
        },
        {
            "IpAddress": "2607:fcd0:cd40:1400::2"
        }
    ],
```

Uptrends heeft deze inconsistentie nu opgelost en retourneert de IPv6-adressen op dezelfde manier:

```json
    "IpV6Addresses": [
        "2a01:5cc0:1:2::4",
        "2607:fcd0:cd40:1400::2",
    ],
```

Houd er rekening mee dat als u het ophalen van IP-adressen van controlestations heeft geautomatiseerd, bijvoorbeeld voor whitelistdoeleinden, dit een **belangrijke wijziging** kan zijn.

## Januari 2023

Versie 3 van de API heeft per januari 2023 het einde van zijn levensduur bereikt en is uitgeschakeld. U kunt [de documentatie]({{< ref path="/support/kb/api" lang="nl" >}}) nog steeds vinden in onze knowledge base, maar versie 3 werkt niet meer. Als u bestaande scripts of procedures heeft die nog gebruikmaken van versie 3, zullen deze mislukken, en we raden u aan zo snel mogelijk over te stappen naar versie 4. Zie onze [upgradehandleiding]({{< ref path="/support/kb/api" lang="nl" >}}) voor meer informatie over het overstappen van API versie 3 naar versie 4.

**Update mei 2023:** De documentatie voor versie 3 van onze API is verwijderd en is niet meer toegankelijk. 

## December 2022

### Aanmaakdatuminformatie controleregel via de API

Het [/Monitor endpoint](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Monitor) kan onder andere worden gebruikt om definities van de controleregels in uw account op te halen (via *GET /Monitor/{monitorGuid}*). De response bevat nu ook een `CreatedDate`, die aangeeft wanneer de controleregel is gemaakt.


## November 2022

### Kleine wijzigingen in /Register endpoint

Zoals u misschien [in onze reguliere changelog]({{< ref path="/changelog" lang="nl" >}}) heeft gelezen, hebben we in deze release de optie toegevoegd om [Uptrends API-inloggegevens te maken en in te trekken via de gebruikersinterface]({{< ref path="/changelog#2022-11-manage-uptrends-api-credentials-via-ui" lang="nl" >}}). Om de Uptrends API v4 af te stemmen op de gebruikersinterface hebben we 2 nieuwe opties toegevoegd aan het /Register endpoint:

- Het is nu mogelijk om een optionele beschrijving op te geven bij het registreren van een nieuw API-account door het veld `omschrijving` te gebruiken.
- Het is nu mogelijk om een API-account te creëren voor een andere operator wanneer de aanroepende operator voldoende rechten heeft door het veld `operatorGuid` te gebruiken.

## September 2022

### Aankomende wijziging: tijdstempels in de API response

Momenteel worden tijdstempels die deel uitmaken van de response voor elke [API v4]({{< ref path="/support/kb/api" lang="nl" >}}) call op een van de volgende twee manieren geconverteerd naar JSON:

- Het aantal milliseconden is gelijk aan 0:  _2022-09-21T13:08:47_
- Het aantal milliseconden is niet gelijk aan 0: _2022-09-21T13:08:47<b>.682</b>_

Deze inconsistentie kan tot problemen leiden wanneer de data die deze tijdstempels bevatten automatisch worden geparseerd en verwerkt. Daarom brengen we een wijziging aan: het aantal milliseconden wordt niet langer weergegeven voor tijdstempels die zijn opgenomen in de API response. Voortaan hebben alle tijdstempels het formaat _2022-09-21T13:08:47_.

## Juni 2022

### Aankomende IP-adressen van controlestations 

De Uptrends API kan worden gebruikt om IP-adressen van controlestations op te halen, voor geautomatiseerde whitelisting. Voorheen waren responses op dergelijke requests aan onze [checkpoint API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Checkpoint) doorgaans een up-to-date lijst van huidige IP-adressen van controlestations. Uptrends' controlestationnetwerk is echter altijd in beweging. Nieuwe controlestations worden toegevoegd, bestaande controlestations worden verwijderd of verplaatst, of IP-adressen worden gewijzigd. Dat kan betekenen dat de lijst met IP-adressen die u gebruikte voor whitelisting, achterloopt tot de volgende synchronisatie, wat leidt tot onnodige fouten.

We registreren nu aankomende IP-adressen van controlestations en nemen deze op in de API-response. Op die manier is uw whitelist van te voren up-to-date.

### Relationships in statistics API

Responses van de [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics) (die kan worden gebruikt om statistische data voor uw controleregels of controleregelgroepen op te halen) bevatten nu enkele aanvullende metadata over de response. De nieuwe array `Relationships` bestaat al voor andere API-eindpunten en bevat aanvullende informatie over de request, zoals een link naar de Monitor of MonitorGroup API request om aanvullende informatie over de controleregel(groep) zelf op te halen.


```json
        "Relationships": [
            {
                "Id": "4c3a9529-7934-4978-9c36-c377b232g7hb",
                "Type": "Monitor",
                "Links": {
                    "Self": "/Monitor/4c3a9529-7934-4978-9c36-c377b232g7hb"
                }
            }  
        ]
```

## Mei 2022

### Oplossing voor start-/eindparameters in statistics API

Onze API ondersteunt het ophalen van statistische controleregeldata, met de [Statistics API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Statistics/Statistics_GetMonitorStatistics). U kunt een vooringestelde periode opgeven waarvoor de data moeten worden opgehaald (met beschikbare waarden zoals `Last24Hours`) of een aangepaste periode instellen met behulp van start- en eindparameters van de URL. Met `GET /Statistics/Monitor/{monitorGuid}?Start=2022-04-08&End=2022-04-09` haalt u bijvoorbeeld statistische data op voor een enkele controleregel, voor de opgegeven periode.

Er was een probleem waarbij de minutenindicator in de begin- en eindtijdstempels niet correct werd toegewezen, wat had kunnen leiden tot onvolledige (of zelfs lege) resultaten in de API-response. Dit probleem is opgelost.

## Februari 2022

### Update van status API

De [Status API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Status/Status_GetMonitorStatus) haalt statusinformatie op voor een specifieke controleregel, op basis van de meest recente controleregelcheck. Dit eindpunt kan worden gebruikt voor informatie over de huidige controleregelstatus. We hebben de response zo uitgebreid dat die nu ook een waarde voor `TotalTime` bevat - informatie over het [kengetal totale tijd]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="nl" >}}) voor de meest recente controleregelcheck.

## Januari 2022

### De juiste controleregeldata retourneren

Wanneer een niet-Administrator operator met [het gebruikersrecht **Gegevens bekijken**]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}}) voor een bepaalde controleregel die controleregeldefinitie ophaalde via de API (via `GET /Monitor/{monitorGuid}`), bevatte de response niet alle relevante data. Dat was onjuist, omdat dezelfde data al beschikbaar waren via de gebruikersinterface maar niet via de API, en dit is gecorrigeerd. Wanneer deze operators nu een controleregel ophalen, bevat de response waarden voor *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive* en *GenerateAlert*.

## Augustus 2021

### Aankondiging: beëindiging van versie 3 van onze API

De [Uptrends API](/support/kb/api) ondersteunt momenteel twee versies naast elkaar. Versie 3 is de oudere legacy-versie van onze API en versie 4 is de momenteel aanbevolen versie. Met een veel completere set functies ligt de focus van onze ontwikkeling al geruime tijd op versie 4. Daarom hebben we besloten te stoppen met versie 3 van onze API, deze wordt buiten gebruik gesteld en zal rond **december 2022** niet meer beschikbaar zijn. 

Voor klanten die momenteel nog actief gebruikmaken van versie 3 van onze API, moet worden opgemerkt dat deze tot die tijd nog ondersteund zal worden. We raden u echter aan om zo snel mogelijk over te stappen en versie 4 te gaan gebruiken. Om u hierbij te helpen hebben we een [API v3 naar v4 upgradehandleiding]({{< ref path="support/kb/api" lang="nl" >}}) geschreven, waarin wordt uitgelegd wat de belangrijkste verschillen tussen de twee API-versies zijn en hoe u deze kunt overbruggen in uw scripts en software. 

## Juli 2021

### Belangrijke wijziging: veranderingen in autorisatie-response OperatorGroup

Met de Uptrends API kunt u [gebruikersrechten voor operators en operatorgroepen]({{< ref path="/support/kb/account/users/operators/permissions" lang="nl" >}}) beheren, rollen toewijzen zoals **Beheerder**, **Financiële operator** of **Infra-toegang** toestaan. De [OperatorGroup API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/OperatorGroup) bevat verschillende opties voor het ophalen, toevoegen of verwijderen van dergelijke rechten. 

De manier waarop de gebruikersrechten worden gespecificeerd voor operatorgroepen in de API is gewijzigd, wat invloed kan hebben op het automatisch aanmaken, verwijderen of ophalen van informatie over operatorgroeprechten die u mogelijk heeft ingesteld. Momenteel werkt het ophalen van informatie over gebruikersrechten met de volgende request:

`GET /OperatorGroup/{operatorGroupGuid}/Authorization`

die een response van onderstaande strekking retourneert (afhankelijk van welke rechten zijn geconfigureerd voor die specifieke operatorgroep):

```json
[
      {
        "AuthorizationId": "{authIdGuid1}",
        "AuthorizationType": "FinancialOperator",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    {
        "AuthorizationId": "{authIdGuid2}",
        "AuthorizationType": "AllowInfra",
        "OperatorGroupGuid": "{operatorGroupGuid}"
    },
    ...
]
```

Vanaf nu zal diezelfde request zijn response vereenvoudigen, door alleen de verleende gebruikersrechten en geen andere informatie te vermelden. De response zal niet langer een `operatorGroupGuid` of `AuthorizationId` bevatten (de laatste zal volledig verdwijnen, wat betekent dat er aan gebruikersrechten geen individuele GUID meer wordt toegewezen). Het zal er als volgt uitzien:

```json
{
    "FinancialOperator",
    "AllowInfra",
    ...
}
```

Het toevoegen van een nieuw operatorgroepsrecht werkt momenteel door een POST-request te sturen naar:

 `/OperatorGroup/{operatorGroupGuid}/Authorization` 
 met een request body die een "AuthorizationType" specificeert. De momenteel beschikbare waarden voor AuthorizationType voor operatorgroepen zijn te vinden in de [Uptrends API Swagger UI](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/), onder **Models** (onderaan), en vervolgens **OperatorGroupAuthorizationType**.
 
 Vanaf nu kunnen nieuwe gebruikersrechten worden toegevoegd aan een operatorgroep door een POST-request te sturen naar: 

 `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}` 
 zonder een request body op te nemen. 

Het verwijderen van een recht uit een operatorgroep gebeurt momenteel door een DELETE-request te sturen naar `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationGuid}` - maar zoals hierboven opgemerkt, zal "authorizationGuid" volledig verdwijnen als een entiteit en kan niet meer worden gebruikt. In plaats daarvan kunt u gebruikersrechten verwijderen door rechtstreeks naar hun naam te verwijzen in de request-URL: `/OperatorGroup/{operatorGroupGuid}/Authorization/{authorizationType}`

## Februari 2021

### Belangrijke wijziging: gevoelige waarden in Multi-step API-controleregels

Met ons [controleregeltype Multi-step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="nl" >}}) kunt u meerdere opeenvolgende HTTP requests uitvoeren, waarbij elke nieuwe request een of meer stukjes data gebruikt die zijn opgehaald uit een eerdere request om zijn taak uit te voeren. Vaak behelst een van de stappen dat inloggegevens worden verstrekt om toegang te krijgen tot een bepaalde bron. In het verleden werden deze inloggegevens als voorgedefinieerde variabelen toegevoegd aan de controleregeldefinitie en vervolgens gemarkeerd als *Gevoelig*.

Om de veiligheid te verbeteren van de manier waarop we met dergelijke inloggegevens omgaan, gaan we die opzet niet meer gebruiken. In plaats daarvan worden de inloggegevens in de [vault]({{< ref path="support/kb/account/vault" lang="nl" >}}) geplaatst. Met die wijziging wordt de optie om voorgedefinieerde variabelen als gevoelig te markeren in Multi-step API-controleregels achterhaald en zal worden verwijderd.

Dit zal invloed hebben op de manier waarop u Multi-step API-controleregels kunt maken of ermee kunt interacteren via onze API. Momenteel bevat de controleregeldefinitie voor dit controleregeltype een reeks "PredefinedVariables", waarbij elk van de individuele variabelen een true/false booleaans "Sensitive" heeft. In de nabije toekomst zal deze booleaanse waarde uit de definitie worden verwijderd. Als u in uw account een nieuwe Multi-step API-controleregel wilt maken of een bestaande wilt bijwerken via de Uptrends API, moet dit veld niet langer worden opgenomen. 

### Wijziging: hernoemde routing
 
 Voor Uptrends' API v4 hebben we een inconsistente manier om routes te benoemen. In de meeste gevallen wordt enkelvoud gebruikt, maar een enkele keer meervoud. De route bevat nu alleen nog delen met enkelvoud, bijvoorbeeld `/MonitorGroup/{monitorGroupGuid}/Member` in plaats van `/MonitorGroup/{monitorGroupGuid}/Members`.

 We ondersteunen nog steeds de oude routes voor achterwaartse compatibiliteit.

{{< /Features/Story >}}
