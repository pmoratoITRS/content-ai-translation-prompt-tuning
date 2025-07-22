{
  "hero": {
    "title": "Systeemvariabelen voor alerting"
  },
  "title": "Systeemvariabelen voor alerting",
  "summary": "Een overzicht van beschikbare systeemvariabelen voor gebruik in (aanpasbare) integraties",
  "url": "/support/kb/alerting/integraties/aangepaste-integraties/systeemvariabelen-voor-alerting",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/alerting-system-variables",
  "tableofcontents": false
}

Dit artikel bevat een overzicht van alle beschikbare **Systeemvariabelen** die kunnen worden gebruikt om het uitgaande alertbericht te vullen met relevante informatie over zaken als de controleregel die de alert heeft veroorzaakt, welke fout is opgetreden of de alert zelf. Meer informatie over het gebruik van deze systeemvariabelen vindt u in ons artikel over [het bouwen van de juiste berichtinhoud]({{< ref path="support/kb/alerting/integrations/custom-integrations/building-the-right-message-content" lang="nl" >}}).

Kort gezegd, om de hier vermelde variabelen te gebruiken moeten ze verpakt in dubbele accolades worden opgenomen in de berichtinhoud. Ter illustratie: `{{@alert.alertGuid}}`.

|  Variabele   | Beschrijving    |  Voorbeeldwaarde   |
| --- | --- | --- |
| `@account.accountId` | Uw Uptrends-account-ID. | `299840` |
| `@alert.alertGuid` | Unieke ID van deze alert. | `cbfc7769-edb2-46a7-89d0-1e1b1fb0815b` |
| `@alert.checkpointName` | Bevat de naam of locatie van het controlestation van waaruit de alert het laatst is gecontroleerd. | `Gent, Belgium` |
| `@alert.description` | Tekstbeschrijving van de fout die deze alert heeft getriggerd. Bevat stapnummer indien van toepassing. | `Stap 1: Navigeer naar https://www.galacticresorts.com is mislukt.` |
| `@alert.downtimeDuration` | De tijd tussen de eerste fout en het huidige (Ok-) alert-tijdstempel. | `48:03:21` |
| `@alert.errorTypeId` | {{< tableformatter >}} De fouttype-ID van de fout die deze alert heeft getriggerd, zie [Fouttypes]({{< ref path="/support/kb/alerting/errors/error-types" lang="nl" >}}) voor een lijst met fouttypes. {{< /tableformatter >}} | `5407` |
| `@alert.failureMessage` | De aangepaste foutmelding voor de specifieke actie in een transactiestap die de fout heeft veroorzaakt | `Login is mislukt` |
| `@alert.firstError` | Dezelfde datum en tijd als @alert.firstErrorUtc, maar in de tijdzone van uw account. Ook geformatteerd als ISO 8601. | `2018-11-08T10:21:58` |
| `@alert.firstErrorCheckId` | De ID van de fout die deze alert heeft getriggerd. | `30833627687` |
| `@alert.firstErrorCheckUrl` | De URL van een deep link die u naar de details van de fout leidt die deze alert heeft getriggerd. | `https://app.uptrends.com/Report/ProbeLog/Check/30833627687` |
| `@alert.firstErrorDescription` | De foutbeschrijving van de eerste controleregelcheck die de fout ontving. Bevat stapnummer indien van toepassing. | `Stap 1: Navigeer naar https://www.galacticresorts.com is mislukt.` |
| `@alert.firstErrorFormatted` | Dezelfde datum en tijd als @alert.firstErrorUtc, maar in de tijdzone en cultuur van uw account. | `8/28/2020 12:23 PM` |
| `@alert.firstErrorUtc` | De datum en tijd van de oorspronkelijke fout die deze alert heeft getriggerd, uitgedrukt in UTC-tijd en geformatteerd als ISO 8601. | `2018-11-08T16:21:58` |
| `@alert.firstErrorUtcFormatted` | De datum en tijd van de oorspronkelijke fout die deze alert heeft getriggerd, uitgedrukt in UTC-tijd en geformatteerd in de cultuur van uw account. | `8/28/2020 10:23 PM` |
| `@alert.numberOfConsecutiveErrors` | Bevat het totale aantal opeenvolgende fouten (bevestigde fouten) van de alert. | `2` |
| `@alert.resolvedIpAddress` | Het IP-adres dat werd gebruikt om de controle uit te voeren. Kan een IPv4- of een IPv6-adres zijn. | `178.217.84.4 OF 2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@alert.responseHeaders` | {{< tableformatter >}} Bevat de responsheaders van de alert in sleutel-waardeparen. Houd er rekening mee dat de waarde van deze variabele leeg kan zijn als [Gegevensbescherming van persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}) is ingeschakeld op een persoonlijke controlestationlocatie die de alertcontrole uitvoert. {{< /tableformatter >}} | `Content-Type": "text/html` |
| `@alert.responseBody` | {{< tableformatter >}} Bevat de ontvangen response body wanneer deze beschikbaar is. Merk op dat de response body tekens kan bevatten die moeten worden gecodeerd, bijv. [met @JsonEncode of @XmlEncode]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-formatting" lang="nl" >}}). De response body wordt afgekapt wanneer deze groter is dan 1 MB. {{< /tableformatter >}} | `{"Status": "error"}` |
| `@alert.serverIpv4` | Het IPv4-adres van de server waarop de controle werd uitgevoerd. | `178.217.84.4` |
| `@alert.serverIpv6` | Het IPv6-adres van de server waarop de controle werd uitgevoerd. | `2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@alert.sslValidUntil` | Bevat de datum en tijd waarop het SSL-certificaat verloopt voor SSL-controleregelalerts. | `2024-11-07T15:05:43` |
| `@alert.timestamp` | Dezelfde datum en tijd als @alert.timestampUtc, maar in de tijdzone van uw account. Ook geformatteerd als ISO 8601. | `2018-11-08T10:26:58` |
| `@alert.timestampFormatted` | Dezelfde datum en tijd als @alert.timestampUtc, maar in de tijdzone en cultuur van uw account. | `8/28/2020 12:23 PM` |
| `@alert.timestampUtc` | De datum en tijd van de alert, uitgedrukt in UTC-tijd en geformatteerd als ISO 8601. | `2018-11-08T16:26:58` |
| `@alert.timestampUtcFormatted` | De datum en tijd van de alert, uitgedrukt in UTC-tijd en geformatteerd in de cultuur van uw account. | `8/28/2020 10:23 PM` |
| `@alert.type` | Het type van dit alertbericht:<br><br>- Alert: er is een nieuwe fout gedetecteerd.<br>- Ok: de oorspronkelijke fout is opgelost.<br>- Herinnering: de oorspronkelijke fout duurt nog steeds voort. | `Alert` \| `Ok` \| `Herinnering` |
| `@alertDefinition.guid` | De unieke ID van de alertdefinitie die is gebruikt om deze alert te genereren. | `2C97E464-6112-435B-8C8D-6DEF1E18273A` |
| `@alertDefinition.name` | De naam van de alertdefinitie die is gebruikt om deze alert te genereren | `Standaardalert` |
| `@CustomField(customFieldReference)` | {{< tableformatter >}} Een verwijzing naar een [vrij veld]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#including-external-ids-or-custom-data" lang="nl" >}}), dat kan worden gebruikt om aangepaste data voor individuele controleregels op te nemen. {{< /tableformatter >}} | `Alert voor Ops team` |
| `@escalationLevel.id` | De ID van het escalatieniveau dat is gebruikt om deze alert te genereren. | `1` |
| `@escalationLevel.message` | Het aangepaste bericht dat is opgegeven in het escalatieniveau | `Gebruik checklist THX-1138 om dit probleem te onderzoeken.` |
| `@incident.key` | Unieke ID van het incident waartoe deze alert behoort. Een foutalert en een Ok-alert delen dezelfde incident-key. | `ba8ffcb7-5de0-489e-b649-f00f0b447e80-0-30099055746` |
| `@monitor.dashboardUrl` | De URL van een deep link die u naar het dashboard van deze controleregel brengt. | `https://app.uptrends.com/Probe/Dashboard?probeGuids=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.editUrl` | De URL van een deep link die u naar de instellingen van deze controleregel brengt. | `https://app.uptrends.com/Report/Probe?probeGuid=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.monitorGuid` | De unieke ID van de controleregel in uw account die deze alert heeft getriggerd. | `849b2046-213d-43ad-9efc-5af1faaeb222` |
| `@monitor.name` | De naam van de controleregel in uw account die deze alert heeft getriggerd. | `GalacticResorts.com - DNS` |
| `@monitor.notes` | Alle aangepaste notities die in de controleregelinstellingen zijn ingevuld | `Controleer Amazon Route53 DNS entries` |
| `@monitor.type` | Bevat het type van de controleregel | `Transactie` |
| `@monitor.url` | De URL of het netwerkadres dat deze controleregel aan het controleren is. | `https://galacticresorts.com` |