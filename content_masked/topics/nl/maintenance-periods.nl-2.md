{
  "hero": {
    "title": "Onderhoudsperioden in de API"
  },
  "title": "Onderhoudsperioden in de API",
  "url": "[URL_BASE_TOPICS]api/onderhoudsperioden-in-de-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Er is een specifieke set API-methoden voor het bewerken van onderhoudsperioden voor een controleregel of voor alle controleregels in een controleregelgroep.

## Objectbeschrijving onderhoudsperiode

Het volgende MaintenancePeriod object wordt gebruikt in de hieronder beschreven API-methoden:

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8][HTML_TAG_9][HTML_TAG_10]Naam[HTML_TAG_11][HTML_TAG_12][HTML_TAG_13][HTML_TAG_14]Beschrijving[HTML_TAG_15][HTML_TAG_16][HTML_TAG_17][HTML_TAG_18]Datatype[HTML_TAG_19][HTML_TAG_20][HTML_TAG_21][HTML_TAG_22][HTML_TAG_23][HTML_TAG_24][HTML_TAG_25]Id[HTML_TAG_26][HTML_TAG_27]De unieke identifier voor deze onderhoudsperiode[HTML_TAG_28][HTML_TAG_29]Integer[HTML_TAG_30][HTML_TAG_31][HTML_TAG_32][HTML_TAG_33]ScheduleMode[HTML_TAG_34][HTML_TAG_35]OneTime, Daily, Weekly of Monthly[HTML_TAG_36][HTML_TAG_37]Enum[HTML_TAG_38][HTML_TAG_39][HTML_TAG_40][HTML_TAG_41]StartDateTime[HTML_TAG_42][HTML_TAG_43]Een begindatum en -tijd (alleen van toepassing op een eenmalige geplande periode)[HTML_TAG_44][HTML_TAG_45]DateTime[HTML_TAG_46][HTML_TAG_47][HTML_TAG_48][HTML_TAG_49]EndDateTime[HTML_TAG_50][HTML_TAG_51]De einddatum en -tijd van een eenmalige geplande onderhoudsperiode[HTML_TAG_52][HTML_TAG_53]DateTime[HTML_TAG_54][HTML_TAG_55][HTML_TAG_56][HTML_TAG_57]StartTime[HTML_TAG_58][HTML_TAG_59]De begintijd (“HH:mm”, in 24-uursnotatie) voor een terugkerende (Daily, Weekly of Monthly) onderhoudsperiode[HTML_TAG_60][HTML_TAG_61]String (“HH:mm”)[HTML_TAG_62][HTML_TAG_63][HTML_TAG_64][HTML_TAG_65]EndTime[HTML_TAG_66][HTML_TAG_67]De eindtijd (“HH:mm”, in 24-uursnotatie) voor een terugkerende (Daily, Weekly of Monthly) onderhoudsperiode[HTML_TAG_68][HTML_TAG_69]String (“HH:mm”)[HTML_TAG_70][HTML_TAG_71][HTML_TAG_72][HTML_TAG_73]WeekDay[HTML_TAG_74][HTML_TAG_75]De dag van de week voor een wekelijkse onderhoudsperiode[HTML_TAG_76]
(Sunday/Monday/[…]/Saturday)[HTML_TAG_77][HTML_TAG_78]Enum[HTML_TAG_79][HTML_TAG_80][HTML_TAG_81][HTML_TAG_82]MonthDay[HTML_TAG_83][HTML_TAG_84]Het nummer van de dag voor een maandelijkse onderhoudsperiode[HTML_TAG_85][HTML_TAG_86]Int (1-31)[HTML_TAG_87][HTML_TAG_88][HTML_TAG_89][HTML_TAG_90]MaintenanceType[HTML_TAG_91][HTML_TAG_92]DisableMonitoring (om de controleregel helemaal uit te schakelen) of DisableNotifications (monitoring zal nog steeds plaatsvinden, maar kennisgevingen worden niet verzonden)[HTML_TAG_93][HTML_TAG_94]Enum[HTML_TAG_95][HTML_TAG_96][HTML_TAG_97][HTML_TAG_98]

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

[HTML_TAG_99][HTML_TAG_100][HTML_TAG_101][HTML_TAG_102][HTML_TAG_103][HTML_TAG_104][HTML_TAG_105][HTML_TAG_106][HTML_TAG_107][HTML_TAG_108]Type request[HTML_TAG_109][HTML_TAG_110][HTML_TAG_111][HTML_TAG_112]Eindpunt[HTML_TAG_113][HTML_TAG_114][HTML_TAG_115][HTML_TAG_116]Gebruik[HTML_TAG_117][HTML_TAG_118][HTML_TAG_119][HTML_TAG_120][HTML_TAG_121][HTML_TAG_122][HTML_TAG_123]GET[HTML_TAG_124][HTML_TAG_125]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_126][HTML_TAG_127]Vindt alle onderhoudsperioden voor een controleregel[HTML_TAG_128][HTML_TAG_129][HTML_TAG_130][HTML_TAG_131]POST[HTML_TAG_132][HTML_TAG_133]Monitor/{monitorGuid}/MaintenancePeriod[HTML_TAG_134][HTML_TAG_135]Slaat de nieuwe onderhoudsperiode op die is opgegeven voor de gespecificeerde controleregel[HTML_TAG_136][HTML_TAG_137][HTML_TAG_138][HTML_TAG_139]PUT[HTML_TAG_140][HTML_TAG_141]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_142]
{maintenancePeriodId}[HTML_TAG_143][HTML_TAG_144]Werkt het gespecificeerde onderhoudsschema bij voor de gespecificeerde controleregel[HTML_TAG_145][HTML_TAG_146][HTML_TAG_147][HTML_TAG_148]DELETE[HTML_TAG_149][HTML_TAG_150]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_151]
{maintenancePeriodId}[HTML_TAG_152][HTML_TAG_153]Verwijdert de gespecificeerde onderhoudsperiode uit de gespecificeerde controleregel[HTML_TAG_154][HTML_TAG_155][HTML_TAG_156][HTML_TAG_157]POST[HTML_TAG_158][HTML_TAG_159]Monitor/{monitorGuid}/MaintenancePeriod/[HTML_TAG_160]
Cleanup/{beforeDate}[HTML_TAG_161][HTML_TAG_162]Wist alle eenmalige onderhoudsperioden voor de gespecificeerde controleregel die ouder is dan de gespecificeerde datum[HTML_TAG_163][HTML_TAG_164][HTML_TAG_165][HTML_TAG_166]POST[HTML_TAG_167][HTML_TAG_168]MonitorGroup/{monitorGroupGuid}/[HTML_TAG_169]
MaintenancePeriod[HTML_TAG_170][HTML_TAG_171]Voegt de opgegeven onderhoudsperiode toe aan alle controleregels in de gespecificeerde groep[HTML_TAG_172][HTML_TAG_173][HTML_TAG_174][HTML_TAG_175]

### GET Monitor

[INLINE_CODE_1]

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

[INLINE_CODE_2]

Deze methode creëert de onderhoudsperiode die is opgegeven in de request body en wijst deze toe aan de controleregel met de opgegeven GUID.

Een POST request verwacht een objectstructuur zoals verstrekt is in de voorbeelden onder “Objectbeschrijving onderhoudsperiode.” Zoals u daar kunt zien, is de structuur afhankelijk van het type onderhoudsperiode (OneTime, Daily, Weekly of Monthly). Verder moet het Id-veld niet worden opgegeven. Er wordt automatisch een nieuwe Id-waarde gegenereerd.

### PUT Monitor

[INLINE_CODE_3]

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

[INLINE_CODE_4]

Deze methode verwijdert de onderhoudsperiode met de in maintenancePeriodId opgegeven Id uit de controleregel met de verstrekte monitorGuid.

### POST Monitor

[INLINE_CODE_5]

Deze methode verwijdert alle **eenmalige** schema's met een StartDateTime vóór de datum die is verstrekt in beforeDate van de controleregel met de verstrekte monitorGuid.

### POST MonitorGroup

[INLINE_CODE_6]

Deze methode voegt de in de request body verstrekte onderhoudsperiode toe aan alle controleregels in de controleregelgroep met de verstrekte controleregelgroep Guid.

Verwachte input (voorbeeld voor een wekelijkse onderhoudsperiode):

    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
