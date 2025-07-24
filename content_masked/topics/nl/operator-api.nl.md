{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "De beschikbare API-methodes voor het manipuleren van operators.",
  "url": "[URL_BASE_TOPICS]api/operator-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Deze pagina beschrijft de beschikbare API-methodes voor het manipuleren van operators, d.w.z. gebruikersspecifieke inlogaccounts. Methodes voor het manipuleren van geen-dienstperiodes van een operator worden in een apart gedeelte hieronder beschreven. In het laatste gedeelte op deze pagina wordt de tijdzone-API beschreven die u mogelijk nodig hebt voor het bijwerken van de specifieke tijdzone-instelling van een operator.

## Objectbeschrijving operator

Het volgende Operator-object wordt gebruikt in de hieronder beschreven API-methodes:

| Naam                     | Beschrijving                                                                                                                                                                                                                                                                             | Datatype |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1]           | De unieke ID van deze operator.                                                                                                                                                                                                                                                | Guid      |
| [INLINE_CODE_2]                  | Het primaire e-mailadres en de inlognaam van de operator.                                                                                                                                                                                                                                    | String    |
| [INLINE_CODE_3]               | Het wachtwoord van de operator.                                                                                                                                                                                                                                                                | String    |
| [INLINE_CODE_4]               | De volledige naam van deze operator.                                                                                                                                                                                                                                                        | String    |
| [INLINE_CODE_5]            | Mobiel telefoonnummer van de operator.                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_6]    | Uitgaand telefoonnummer van de operator.                                                                                                                                                                                                                                                   | String    |
| [INLINE_CODE_7] | Geeft aan of de operator de administrator van het account is. Dit veld is alleen-lezen.                                                                                                                                                                                          | Boolean   |
| [INLINE_CODE_8]            | Het alternatieve e-mailadres van deze operator.                                                                                                                                                                                                                                             | String    |
| [INLINE_CODE_9]               | Geeft aan of deze operator momenteel dienst heeft.                                                                                                                                                                                                                                   | Boolean   |
| [INLINE_CODE_10]            | Als deze is ingevuld, wordt de taal voor deze operator ingesteld. Mogelijke waarden: en-US, en-GB, fr-FR, de-DE, nl-NL of leeg. Wanneer deze waarde is ingesteld op leeg, wordt de algemene accountcultuur/-taal gebruikt.                                                                                     | String    |
| [INLINE_CODE_11]             | Optioneel. De ID voor de tijdzone-instelling voor deze gebruiker. Raadpleeg de hieronder vermelde tijdzone-API voor beschikbare waarden. Als dit niet wordt opgegeven, wordt voor deze gebruiker de tijdzone van het account gebruikt.                                                                                  | Short     |
| [INLINE_CODE_12]            | De SMS-provider die door de operator wordt gebruikt. Mogelijke waarden: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| [INLINE_CODE_13]       | Als de SMS-provider specifiek voor deze operator is geconfigureerd, geeft dit veld aan of een numerieke afzender moet worden gebruikt.                                                                                                                                                         | Boolean   |
| [INLINE_CODE_14]          | De provider die wordt gebruikt voor telefonische alerts.                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_15]       | Als Native Login (gebruikersnaam/wachtwoord) beschikbaar en geconfigureerd is voor uw account, geeft dit aan of deze operator mag inloggen bij Uptrends met zijn Uptrends-gebruikersnaam en -wachtwoord. Mogelijke waarden: True, False of niet specificeren om de globale accountinstelling te gebruiken. | Boolean   |
| [INLINE_CODE_16]      | Als Single Sign-on beschikbaar en geconfigureerd is voor uw account, geeft dit aan of deze operator toestemming heeft om Single Sign-on te gebruiken. Mogelijke waarden: True, False of niet specificeren om de globale accountinstelling te gebruiken.                                                               | Boolean   |

## Eindpunten operator

De volgende API-eindpunten zijn beschikbaar voor het ophalen, maken, bijwerken en verwijderen van operators:

| Type request | Eindpunt                                                 | Gebruik                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_17]                                              | Verkrijgt alle operators.                                                                                               |
| GET          | [INLINE_CODE_18]                               | Verkrijgt de details van een operator.                                                                                  |
| POST         | [INLINE_CODE_19]                                              | Creëert een nieuwe operator.                                                                                           |
| PUT          | [INLINE_CODE_20]                               | Werkt een bestaande operator bij.                                                                                     |
| DELETE       | [INLINE_CODE_21]                               | Wist een bestaande operator. Opmerking: u kunt de operator die is gekoppeld aan het API-account dat u gebruikt niet verwijderen. |
| GET          | [INLINE_CODE_22]                  | Verkrijgt de geen-dienstperiodes voor een bestaande operator.                                                                 |
| POST         | [INLINE_CODE_23]                  | Voegt een dienstperiode toe voor een bestaande operator.                                                                    |
| PUT          | [INLINE_CODE_24] | Werkt een gespecificeerde dienstperiode bij.                                                                              |
| DELETE       | [INLINE_CODE_25] | Verwijdert een gespecificeerde dienstperiode.                                                                              |

#### GET Operator

Deze GET request retourneert een verzameling die alle operators bevat, inclusief de account administrator.

[INLINE_CODE_26]

#### GET Operator/{operatorGuid}

Deze GET request retourneert de details van de specifieke operator die wordt geïdentificeerd door de gespecificeerde operator-GUID.

Voorbeeld uitvoer:

[INLINE_CODE_27]

#### POST Operator

Hiermee wordt een nieuwe operator gemaakt met de verstrekte gegevens.

Voorbeeld invoer:

[INLINE_CODE_28]

De respons bevat de gecreëerde operator, inclusief de operator-GUID die is toegewezen:

[INLINE_CODE_29]

#### PUT Operator/{operatorGuid}

Deze methode werkt de operator bij die wordt geïdentificeerd door de opgegeven operator-GUID met behulp van de data die in de request zijn opgegeven.

Voorbeeld invoer:

[INLINE_CODE_30]

#### DELETE Operator/{operatorGuid}

Deze methode verwijdert de operator geïdentificeerd door de gespecificeerde operator-GUID met behulp van de in de request verstrekte data.

## Objectbeschrijving geen-dienstperiode operator

| Naam            | Beschrijving                                                                                               | Datatype |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_31]            | De unieke ID voor deze geen-dienstperiode. Dit veld is alleen-lezen en wordt automatisch gegenereerd. | Guid      |
| [INLINE_CODE_32]  | De roostermodus. Mogelijke waarden: OneTime, Daily, Weekly, Monthly                                       | String    |
| [INLINE_CODE_33] | De begindatum en -tijd (voor een eenmalig rooster)                                                         | DateTime  |
| [INLINE_CODE_34]   | De einddatum en -tijd (voor een eenmalig rooster)                                                           | DateTime  |
| [INLINE_CODE_35]       | De dag van de week (voor een wekelijks rooster). Mogelijke waarden: Monday, Tuesday, …, Sunday.               | String    |
| [INLINE_CODE_36]      | De datum van de maand (voor een maandelijks rooster)                                                            | Int       |
| [INLINE_CODE_37]     | De begintijd (voor een dagelijks, wekelijks of maandelijks rooster). Formaat: “HH:mm”, in 24 uursformaat.             | String    |
| [INLINE_CODE_38]       | De eindtijd (voor een dagelijks, wekelijks of maandelijks rooster). Formaat: “HH:mm”, in 24 uursformaat.               | String    |

## Eindpunten geen-dienstperiode operator

De volgende API-eindpunten zijn beschikbaar voor het ophalen, creëren, bijwerken en verwijderen van geen-dienstperiodes voor een specifieke operator:

#### GET Operator/{operatorGuid}/DutySchedule

Deze methode retourneert een verzameling die alle geen-dienstperiodes voor de gespecificeerde operator bevat.

Voorbeeld uitvoer:

[INLINE_CODE_39]

#### POST Operator/{operatorGuid}/DutySchedule

Deze methode creëert een nieuwe geen-dienstperiode voor de gespecificeerde operator.

Voorbeeld invoer (voor een wekelijks rooster):

[INLINE_CODE_40]

Zoals u in dit voorbeeld kunt zien, moet u alleen de parameters specificeren die relevant zijn voor het roostertype dat u aan het creëren bent. De MonthDay is bijvoorbeeld niet relevant bij een wekelijks rooster, en StartDateTime en EndDateTime zijn alleen voor eenmalige roosters.

Om hier iets dieper op in te gaan: in een dagelijks rooster is geen weekdagwaarde nodig, alleen ScheduleMode “Dagelijks” en een start- en eindtijd. En bij een maandelijks rooster alleen ScheduleMode “Maandelijks”, de dag van de maand, de starttijd en de eindtijd.

Wanneer u een nieuwe geen-dienstperiode maakt, bevat de uitvoer de ID van het nieuwe rooster. Voorbeeld uitvoer voor het maken van een dagelijks rooster:

[INLINE_CODE_41]

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Deze methode werkt de geen-dienstperiode bij met de gespecificeerde geen-dienstperiode-ID voor de gespecificeerde operator.Voorbeeld invoer:

[INLINE_CODE_42]

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Deze methode verwijdert de geen-dienstperiode met de gespecificeerde geen-dienstperiode-ID voor de gespecificeerde operator.

## Objectbeschrijving tijdzone

| Naam                   | Beschrijving                                                                                      | Datatype |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_43]           | De unieke ID voor deze tijdzone                                                         | Short     |
| [INLINE_CODE_44]          | De beschrijving voor deze tijdzone                                                               | String    |
| [INLINE_CODE_45]        | De offset van UTC in minuten                                                                   | Short     |
| [INLINE_CODE_46]    | Of deze tijdzone wel of geen zomertijd heeft                                            | Boolean   |
| [INLINE_CODE_47] | De offset, in minuten, voor zomertijd. Niet gespecificeerd wanneer HasDaylightSaving false is. | Short     |

## Eindpunten tijdzone

De volgende methodes kunnen worden gebruikt om tijdzone-informatie op te halen. U kunt deze data gebruiken om vast te stellen welke tijdzone-ID u moet gebruiken wanneer u een tijdzone-ID voor de instellingen van een operator wilt specificeren.

#### GET Timezone

Deze GET request retourneert een verzameling met alle tijdzones.

Voorbeeld uitvoer:

[INLINE_CODE_48]

#### GET Timezone/{timezoneId}

Met deze methode worden de tijdzonedetails voor de tijdzone met de gespecificeerde ID verkregen.

Voorbeeld uitvoer:

[INLINE_CODE_49]
