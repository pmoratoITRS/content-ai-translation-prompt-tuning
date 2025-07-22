{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "De beschikbare API-methodes voor het manipuleren van operators.",
  "url": "/support/kb/api/operator-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-api"
}

Deze pagina beschrijft de beschikbare API-methodes voor het manipuleren van operators, d.w.z. gebruikersspecifieke inlogaccounts. Methodes voor het manipuleren van geen-dienstperiodes van een operator worden in een apart gedeelte hieronder beschreven. In het laatste gedeelte op deze pagina wordt de tijdzone-API beschreven die u mogelijk nodig hebt voor het bijwerken van de specifieke tijdzone-instelling van een operator.

## Objectbeschrijving operator

Het volgende Operator-object wordt gebruikt in de hieronder beschreven API-methodes:

| Naam                     | Beschrijving                                                                                                                                                                                                                                                                             | Datatype |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| `OperatorGuid`           | De unieke ID van deze operator.                                                                                                                                                                                                                                                | Guid      |
| `Email`                  | Het primaire e-mailadres en de inlognaam van de operator.                                                                                                                                                                                                                                    | String    |
| `Password`               | Het wachtwoord van de operator.                                                                                                                                                                                                                                                                | String    |
| `FullName`               | De volledige naam van deze operator.                                                                                                                                                                                                                                                        | String    |
| `MobilePhone`            | Mobiel telefoonnummer van de operator.                                                                                                                                                                                                                                                     | String    |
| `OutgoingPhoneNumber`    | Uitgaand telefoonnummer van de operator.                                                                                                                                                                                                                                                   | String    |
| `IsAccountAdministrator` | Geeft aan of de operator de administrator van het account is. Dit veld is alleen-lezen.                                                                                                                                                                                          | Boolean   |
| `BackupEmail`            | Het alternatieve e-mailadres van deze operator.                                                                                                                                                                                                                                             | String    |
| `IsOnDuty`               | Geeft aan of deze operator momenteel dienst heeft.                                                                                                                                                                                                                                   | Boolean   |
| `CultureName`            | Als deze is ingevuld, wordt de taal voor deze operator ingesteld. Mogelijke waarden: en-US, en-GB, fr-FR, de-DE, nl-NL of leeg. Wanneer deze waarde is ingesteld op leeg, wordt de algemene accountcultuur/-taal gebruikt.                                                                                     | String    |
| `TimeZoneId`             | Optioneel. De ID voor de tijdzone-instelling voor deze gebruiker. Raadpleeg de hieronder vermelde tijdzone-API voor beschikbare waarden. Als dit niet wordt opgegeven, wordt voor deze gebruiker de tijdzone van het account gebruikt.                                                                                  | Short     |
| `SmsProvider`            | De SMS-provider die door de operator wordt gebruikt. Mogelijke waarden: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| `UseNumericSender`       | Als de SMS-provider specifiek voor deze operator is geconfigureerd, geeft dit veld aan of een numerieke afzender moet worden gebruikt.                                                                                                                                                         | Boolean   |
| `PhoneProvider`          | De provider die wordt gebruikt voor telefonische alerts.                                                                                                                                                                                                                                                     | String    |
| `AllowNativeLogin`       | Als Native Login (gebruikersnaam/wachtwoord) beschikbaar en geconfigureerd is voor uw account, geeft dit aan of deze operator mag inloggen bij Uptrends met zijn Uptrends-gebruikersnaam en -wachtwoord. Mogelijke waarden: True, False of niet specificeren om de globale accountinstelling te gebruiken. | Boolean   |
| `AllowSingleSignon`      | Als Single Sign-on beschikbaar en geconfigureerd is voor uw account, geeft dit aan of deze operator toestemming heeft om Single Sign-on te gebruiken. Mogelijke waarden: True, False of niet specificeren om de globale accountinstelling te gebruiken.                                                               | Boolean   |

## Eindpunten operator

De volgende API-eindpunten zijn beschikbaar voor het ophalen, maken, bijwerken en verwijderen van operators:

| Type request | Eindpunt                                                 | Gebruik                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | `/Operator`                                              | Verkrijgt alle operators.                                                                                               |
| GET          | `/Operator/{operatorGuid}`                               | Verkrijgt de details van een operator.                                                                                  |
| POST         | `/Operator`                                              | Creëert een nieuwe operator.                                                                                           |
| PUT          | `/Operator/{operatorGuid}`                               | Werkt een bestaande operator bij.                                                                                     |
| DELETE       | `/Operator/{operatorGuid}`                               | Wist een bestaande operator. Opmerking: u kunt de operator die is gekoppeld aan het API-account dat u gebruikt niet verwijderen. |
| GET          | `/Operator/{operatorGuid}/DutySchedule`                  | Verkrijgt de geen-dienstperiodes voor een bestaande operator.                                                                 |
| POST         | `/Operator/{operatorGuid}/DutySchedule`                  | Voegt een dienstperiode toe voor een bestaande operator.                                                                    |
| PUT          | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Werkt een gespecificeerde dienstperiode bij.                                                                              |
| DELETE       | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Verwijdert een gespecificeerde dienstperiode.                                                                              |

#### GET Operator

Deze GET request retourneert een verzameling die alle operators bevat, inclusief de account administrator.

`[  {  "OperatorGuid": "36fad910-6e9f-4886-b1a7-9b4637362cb8",  "FullName": "First Operator",  "Email": "FirstOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": true,  "BackupEmail": " FirstOperator@gmail.com ",  "IsOnDuty": true,  "SmsProvider": "UseAccountSetting",  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  },  {  "OperatorGuid": "23a75d1f-0dec-4963-86d8-0cee21267db4",  "UserName": "SecondOperator@acme.com",  "FullName": "Second Operator",  "Email": "SecondOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "SmsProvider": "SmsProviderEurope",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  }  ] `

#### GET Operator/{operatorGuid}

Deze GET request retourneert de details van de specifieke operator die wordt geïdentificeerd door de gespecificeerde operator-GUID.

Voorbeeld uitvoer:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true  "AllowSingleSignon": false  } `

#### POST Operator

Hiermee wordt een nieuwe operator gemaakt met de verstrekte gegevens.

Voorbeeld invoer:

`{  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

De respons bevat de gecreëerde operator, inclusief de operator-GUID die is toegewezen:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### PUT Operator/{operatorGuid}

Deze methode werkt de operator bij die wordt geïdentificeerd door de opgegeven operator-GUID met behulp van de data die in de request zijn opgegeven.

Voorbeeld invoer:

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### DELETE Operator/{operatorGuid}

Deze methode verwijdert de operator geïdentificeerd door de gespecificeerde operator-GUID met behulp van de in de request verstrekte data.

## Objectbeschrijving geen-dienstperiode operator

| Naam            | Beschrijving                                                                                               | Datatype |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `Id`            | De unieke ID voor deze geen-dienstperiode. Dit veld is alleen-lezen en wordt automatisch gegenereerd. | Guid      |
| `ScheduleMode`  | De roostermodus. Mogelijke waarden: OneTime, Daily, Weekly, Monthly                                       | String    |
| `StartDateTime` | De begindatum en -tijd (voor een eenmalig rooster)                                                         | DateTime  |
| `EndDateTime`   | De einddatum en -tijd (voor een eenmalig rooster)                                                           | DateTime  |
| `WeekDay`       | De dag van de week (voor een wekelijks rooster). Mogelijke waarden: Monday, Tuesday, …, Sunday.               | String    |
| `MonthDay`      | De datum van de maand (voor een maandelijks rooster)                                                            | Int       |
| `StartTime`     | De begintijd (voor een dagelijks, wekelijks of maandelijks rooster). Formaat: “HH:mm”, in 24 uursformaat.             | String    |
| `EndTime`       | De eindtijd (voor een dagelijks, wekelijks of maandelijks rooster). Formaat: “HH:mm”, in 24 uursformaat.               | String    |

## Eindpunten geen-dienstperiode operator

De volgende API-eindpunten zijn beschikbaar voor het ophalen, creëren, bijwerken en verwijderen van geen-dienstperiodes voor een specifieke operator:

#### GET Operator/{operatorGuid}/DutySchedule

Deze methode retourneert een verzameling die alle geen-dienstperiodes voor de gespecificeerde operator bevat.

Voorbeeld uitvoer:

`[  {  "Id": 2272,  "ScheduleMode": "Weekly",  "WeekDay": "Monday",  "StartTime": "08:00",  "EndTime": "16:30"  },  {  "Id": 2267,  "ScheduleMode": "Monthly",  "MonthDay": 15  "StartTime": "08:00",  "EndTime": "16:30"  }  ] `

#### POST Operator/{operatorGuid}/DutySchedule

Deze methode creëert een nieuwe geen-dienstperiode voor de gespecificeerde operator.

Voorbeeld invoer (voor een wekelijks rooster):

`{  "ScheduleMode": "Weekly",  "WeekDay": "Thursday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

Zoals u in dit voorbeeld kunt zien, moet u alleen de parameters specificeren die relevant zijn voor het roostertype dat u aan het creëren bent. De MonthDay is bijvoorbeeld niet relevant bij een wekelijks rooster, en StartDateTime en EndDateTime zijn alleen voor eenmalige roosters.

Om hier iets dieper op in te gaan: in een dagelijks rooster is geen weekdagwaarde nodig, alleen ScheduleMode “Dagelijks” en een start- en eindtijd. En bij een maandelijks rooster alleen ScheduleMode “Maandelijks”, de dag van de maand, de starttijd en de eindtijd.

Wanneer u een nieuwe geen-dienstperiode maakt, bevat de uitvoer de ID van het nieuwe rooster. Voorbeeld uitvoer voor het maken van een dagelijks rooster:

`{  "Id": 2272,  "ScheduleMode": "Daily",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Deze methode werkt de geen-dienstperiode bij met de gespecificeerde geen-dienstperiode-ID voor de gespecificeerde operator.Voorbeeld invoer:

`{  "Id": 2273,  "ScheduleMode": "Weekly",  "WeekDay": "Wednesday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Deze methode verwijdert de geen-dienstperiode met de gespecificeerde geen-dienstperiode-ID voor de gespecificeerde operator.

## Objectbeschrijving tijdzone

| Naam                   | Beschrijving                                                                                      | Datatype |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| `TimeZoneId`           | De unieke ID voor deze tijdzone                                                         | Short     |
| `Description`          | De beschrijving voor deze tijdzone                                                               | String    |
| `OffsetFromUtc`        | De offset van UTC in minuten                                                                   | Short     |
| `HasDaylightSaving`    | Of deze tijdzone wel of geen zomertijd heeft                                            | Boolean   |
| `DaylightSavingOffset` | De offset, in minuten, voor zomertijd. Niet gespecificeerd wanneer HasDaylightSaving false is. | Short     |

## Eindpunten tijdzone

De volgende methodes kunnen worden gebruikt om tijdzone-informatie op te halen. U kunt deze data gebruiken om vast te stellen welke tijdzone-ID u moet gebruiken wanneer u een tijdzone-ID voor de instellingen van een operator wilt specificeren.

#### GET Timezone

Deze GET request retourneert een verzameling met alle tijdzones.

Voorbeeld uitvoer:

`[  {  "TimezoneId": 1,  "Description": "GMT-04:00# Brazil West, Chile, Paraguay",  "OffsetFromUtc": -240,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 2,  "Description": "GMT\+06:00# Cocos Islands",  "OffsetFromUtc": 360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 3,  "Description": "GMT\+01:00 West Central Africa",  "OffsetFromUtc": 60,  "HasDaylightSaving": false  }  // (there will be many more)  ]`

#### GET Timezone/{timezoneId}

Met deze methode worden de tijdzonedetails voor de tijdzone met de gespecificeerde ID verkregen.

Voorbeeld uitvoer:

`{  "TimezoneId": 56,  "Description": "GMT-06:00* Central time",  "OffsetFromUtc": -360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  }`
