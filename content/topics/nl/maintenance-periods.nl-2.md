{
  "hero": {
    "title": "Onderhoudsperioden in de API"
  },
  "title": "Onderhoudsperioden in de API",
  "url": "/support/kb/api/onderhoudsperioden-in-de-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/maintenance-periods"
}

Er is een specifieke set API-methoden voor het bewerken van onderhoudsperioden voor een controleregel of voor alle controleregels in een controleregelgroep.

## Objectbeschrijving onderhoudsperiode

Het volgende MaintenancePeriod object wordt gebruikt in de hieronder beschreven API-methoden:

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th><strong>Naam</strong></th><th><strong>Beschrijving</strong></th><th><strong>Datatype</strong></th></tr></thead><tbody><tr class="odd"><td>Id</td><td>De unieke identifier voor deze onderhoudsperiode</td><td>Integer</td></tr><tr class="even"><td>ScheduleMode</td><td>OneTime, Daily, Weekly of Monthly</td><td>Enum</td></tr><tr class="odd"><td>StartDateTime</td><td>Een begindatum en -tijd (alleen van toepassing op een eenmalige geplande periode)</td><td>DateTime</td></tr><tr class="even"><td>EndDateTime</td><td>De einddatum en -tijd van een eenmalige geplande onderhoudsperiode</td><td>DateTime</td></tr><tr class="odd"><td>StartTime</td><td>De begintijd (“HH:mm”, in 24-uursnotatie) voor een terugkerende (Daily, Weekly of Monthly) onderhoudsperiode</td><td>String (“HH:mm”)</td></tr><tr class="even"><td>EndTime</td><td>De eindtijd (“HH:mm”, in 24-uursnotatie) voor een terugkerende (Daily, Weekly of Monthly) onderhoudsperiode</td><td>String (“HH:mm”)</td></tr><tr class="odd"><td>WeekDay</td><td>De dag van de week voor een wekelijkse onderhoudsperiode<br />
(Sunday/Monday/[…]/Saturday)</td><td>Enum</td></tr><tr class="even"><td>MonthDay</td><td>Het nummer van de dag voor een maandelijkse onderhoudsperiode</td><td>Int (1-31)</td></tr><tr class="odd"><td>MaintenanceType</td><td>DisableMonitoring (om de controleregel helemaal uit te schakelen) of DisableNotifications (monitoring zal nog steeds plaatsvinden, maar kennisgevingen worden niet verzonden)</td><td>Enum</td></tr></tbody></table>

Wanneer een onderhoudsperiode via de API wordt geretourneerd, zijn alle eigenschappen aanwezig, maar afhankelijk van de ScheduleMode worden sommige velden met betrekking tot begin- en einddatums/-tijden niet gebruikt.

Voor een eenmalige onderhoudsperiode moeten we de begin- en einddatum *en* -tijd weten, zodat de eigenschappen StartDateTime en EndDateTime worden gebruikt. Voor terugkerende onderhoudsperioden zijn de velden begin- en eindtijd geschikt, en, afhankelijk van het type schema, de eigenschap WeekDay of MonthDay.

Een dagelijks schema ziet er bijvoorbeeld als volgt uit:

    {
    "Id": 123, 
    "ScheduleMode": "Daily", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

De eigenschappen die niet relevant zijn voor dit type schema (DateTime, WeekDay en MonthDay) worden weggelaten.

Een wekelijks schema ziet er als volgt uit:

    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }

Een maandelijks schema ziet er als volgt uit:

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Een eenmalig schema ziet er als volgt uit:

    {
    "Id": 124, 
    "ScheduleMode": "OneTime", 
    "StartDateTime": "2018-09-24T22:00",
    "EndDateTime": "2018-09-24T22:00", 
    "MaintenanceType": "DisableMonitoring" 
    }

De volgende API-eindpunten zijn beschikbaar:

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th><strong>Type request</strong></th><th><strong>Eindpunt</strong></th><th><strong>Gebruik</strong></th></tr></thead><tbody><tr class="odd"><td>GET</td><td>Monitor/{monitorGuid}/MaintenancePeriod</td><td>Vindt alle onderhoudsperioden voor een controleregel</td></tr><tr class="even"><td>POST</td><td>Monitor/{monitorGuid}/MaintenancePeriod</td><td>Slaat de nieuwe onderhoudsperiode op die is opgegeven voor de gespecificeerde controleregel</td></tr><tr class="odd"><td>PUT</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
{maintenancePeriodId}</td><td>Werkt het gespecificeerde onderhoudsschema bij voor de gespecificeerde controleregel</td></tr><tr class="even"><td>DELETE</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
{maintenancePeriodId}</td><td>Verwijdert de gespecificeerde onderhoudsperiode uit de gespecificeerde controleregel</td></tr><tr class="odd"><td>POST</td><td>Monitor/{monitorGuid}/MaintenancePeriod/<br />
Cleanup/{beforeDate}</td><td>Wist alle eenmalige onderhoudsperioden voor de gespecificeerde controleregel die ouder is dan de gespecificeerde datum</td></tr><tr class="even"><td>POST</td><td>MonitorGroup/{monitorGroupGuid}/<br />
MaintenancePeriod</td><td>Voegt de opgegeven onderhoudsperiode toe aan alle controleregels in de gespecificeerde groep</td></tr></tbody></table>

### GET Monitor

`GET Monitor/{monitorGuid}/MaintenancePeriod`

Deze GET request retourneert een verzameling met alle geplande onderhoudsperioden voor de controleregel met de verstrekte GUID.

Voorbeeld output:

    [
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }, 
    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
    ]

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod`

Deze methode creëert de onderhoudsperiode die is opgegeven in de request body en wijst deze toe aan de controleregel met de opgegeven GUID.

Een POST request verwacht een objectstructuur zoals verstrekt is in de voorbeelden onder “Objectbeschrijving onderhoudsperiode.” Zoals u daar kunt zien, is de structuur afhankelijk van het type onderhoudsperiode (OneTime, Daily, Weekly of Monthly). Verder moet het Id-veld niet worden opgegeven. Er wordt automatisch een nieuwe Id-waarde gegenereerd.

### PUT Monitor

`PUT Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Deze methode werkt de onderhoudsperiode met de verstrekte onderhoudsperiode-ID bij naar de waarden die zijn opgegeven in de request body.

Verwachte input (voorbeeld voor een maandelijkse onderhoudsperiode):

    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }

Merk op dat de Id van de onderhoudsperiode zowel in de body als in de parameter maintenancePeriodId moet worden opgegeven. Als de Id in de parameter niet overeenkomt met de Id van de onderhoudsperiode in de request body, wordt er een uitzondering geretourneerd.

### DELETE Monitor

`DELETE Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

Deze methode verwijdert de onderhoudsperiode met de in maintenancePeriodId opgegeven Id uit de controleregel met de verstrekte monitorGuid.

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate}`

Deze methode verwijdert alle **eenmalige** schema's met een StartDateTime vóór de datum die is verstrekt in beforeDate van de controleregel met de verstrekte monitorGuid.

### POST MonitorGroup

`POST MonitorGroup/{monitorGroupGuid}/MaintenancePeriod`

Deze methode voegt de in de request body verstrekte onderhoudsperiode toe aan alle controleregels in de controleregelgroep met de verstrekte controleregelgroep Guid.

Verwachte input (voorbeeld voor een wekelijkse onderhoudsperiode):

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
