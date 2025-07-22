{
  "hero": {
    "title": "API Opérateurs"
},
"title": "API Opérateurs",
  "summary": "Les méthodes d'API disponibles pour manipuler les opérateurs.",
  "url": "/support/kb/api/operator-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-api"
}

Cette page décrit les méthodes d'API disponibles pour manipuler les opérateurs, c'est-à-dire les comptes de connexion spécifiques à l'utilisateur. Les méthodes permettant de manipuler l'horaire d'un opérateur en-dehors des heures de travail (horaire hors service) sont décrites dans une section distincte ci-dessous. La dernière section de cette page décrit l'API de fuseau horaire, dont vous pouvez avoir besoin pour mettre à jour le paramètre de fuseau horaire spécifique d'un opérateur.

## Description de l'objet opérateur

L'objet Opérateur suivant est utilisé dans les méthodes de l'API décrites ci-dessous :

| Nom | Description | Type de données |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| `OperatorGuid` | Identifiant unique pour cet opérateur. | Guid |
| `Email` | Adresse e-mail principale et nom de connexion de l'opérateur. | String |
| `Password` | Le mot de passe de l'opérateur. | String |
| `FullName` | Le nom complet de cet opérateur. | String |
| `MobilePhone` | Le numéro de téléphone portable de l'opérateur. | String |
| `OutgoingPhoneNumber` | Le numéro de téléphone sortant de l'opérateur. | String |
| `IsAccountAdministrator` | Indique si l'opérateur est l'administrateur du compte. Ceci est un champ en lecture seule. | Boolean |
| `BackupEmail` | L'adresse e-mail de secours pour cet opérateur. | String |
| `IsOnDuty` | Indique si cet opérateur est actuellement en service. | Boolean |
| `CultureName` | S'il est renseigné, définit la culture de cet opérateur. Valeurs possibles : en-US, en-GB, fr-FR, de-DE, nl-NL ou vide. Lorsque cette valeur est définie sur vide, la culture/langue générale du compte est utilisée | String |
| `TimeZoneId` | Optionnel. Identifiant du paramètre de fuseau horaire de cet utilisateur. Reportez-vous à l'API de fuseau horaire mentionné ci-dessous pour connaître les valeurs disponibles. S'il n'est pas spécifié, le fuseau horaire du compte sera utilisé pour cet utilisateur. | Short |
| `SmsProvider` | Le fournisseur de SMS utilisé par l'opérateur. Valeurs possibles : UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational | String |
| `UseNumericSender` | Si le fournisseur SMS est configuré spécifiquement pour cet opérateur, ce champ indique si un identifiant téléphonique numérique doit être utilisé. | Boolean |
| `PhoneProvider` | Le fournisseur utilisé pour les alertes téléphoniques. | String |
| `AllowNativeLogin` | Si la connexion native (nom d'utilisateur/mot de passe) est disponible et configurée pour votre compte, indique si cet opérateur est autorisé à se connecter à Uptrends à l'aide de son nom d'utilisateur et de son mot de passe Uptrends. Valeurs possibles : True, False ou non-spécifié pour utiliser le paramètre de compte général. | Boolean |
| `AllowSingleSignon` | Si Single Signon est disponible et configuré pour votre compte, indique si cet opérateur est autorisé à utiliser Single Sign-On. Valeurs possibles : True, False ou non-spécifié pour utiliser le paramètre de compte général. | Boolean |

## Endpoints Operateur

Les points de terminaison API suivants sont disponibles pour extraire, créer, mettre à jour et supprimer des opérateurs :

| Type de requête | Endpoint | Utilisation |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET | `/Operator` | Liste tous les opérateurs. |
| GET | `/Operator/{operatorGuid}` | Liste les détails d'un opérateur. |
| POST | `/Operator` | Crée un nouvel opérateur. |
| PUT | `/Operator/{operatorGuid}` | Met à jour un opérateur existant. |
| DELETE | `/Operator/{operatorGuid}` | Supprime un opérateur existant. Note: vous ne pouvez pas supprimer l'opérateur associé au compte API que vous utilisez. |
| GET | `/Operator/{operatorGuid}/DutySchedule` | Obtient les horaires de repos pour un opérateur existant. |
| POST | `/Operator/{operatorGuid}/DutySchedule` | Ajoute un horaire de repos pour un opérateur existant. |
| PUT | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Met à jour l'horaire de repos spécifié. |
| DELETE | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Supprime l'horaire de repos spécifié. |

#### GET Operator

Cette requête GET renverra une collection contenant tous les opérateurs, y compris l'administrateur du compte.

`[  {  "OperatorGuid": "36fad910-6e9f-4886-b1a7-9b4637362cb8",  "FullName": "First Operator",  "Email": "FirstOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": true,  "BackupEmail": " FirstOperator@gmail.com ",  "IsOnDuty": true,  "SmsProvider": "UseAccountSetting",  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  },  {  "OperatorGuid": "23a75d1f-0dec-4963-86d8-0cee21267db4",  "UserName": "SecondOperator@acme.com",  "FullName": "Second Operator",  "Email": "SecondOperator@acme.com",  "MobilePhone": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "SmsProvider": "SmsProviderEurope",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  }  ] `

#### GET Operator/{operatorGuid}

Cette requête GET renverra les détails de l'opérateur spécifique identifié par l'opérateur GUID spécifié.

Exemple :

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true  "AllowSingleSignon": false  } `

#### POST Operator

Créera un nouvel opérateur avec les détails fournis.

Exemple de données d'entrée :

`{  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

La réponse contiendra l'opérateur créé, y compris l'opérateur GUID attribué :

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### PUT Operator/{operatorGuid}

Cette méthode met à jour l'opérateur identifié par l'opérateur GUID spécifié, à l'aide des données fournies dans la requête.

Exemple de données d'entrée :

`{  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",  "FullName": "Third Operator",  "Email": "ThirdOperator@acme.com",  "MobilePhone": "\+31612345678",  "OutgoingPhoneNumber": "",  "IsAccountAdministrator": false,  "BackupEmail": "",  "IsOnDuty": false,  "CultureName": "",  "TimeZoneId": 56,  "SmsProvider": "SmsProviderUSA",  "UseNumericSender": false,  "PhoneProvider": "UseAccountSetting",  "AllowNativeLogin": true,  "AllowSingleSignon": false  } `

#### DELETE Operator/{operatorGuid}

Cette méthode supprimera l'opérateur identifié par le GUID opérateur spécifié, à l'aide des données fournies dans la demande.

## Description de l'objet Horaire de repos de l'opérateur

| Nom | Description | Type de données |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `Id` | L'identifiant unique de cet horaire de repos. Ce champ est en lecture seule et sera généré automatiquement. | Guid |
| `ScheduleMode` | Le mode de l'horaire. Possible values: OneTime, Daily, Weekly, Monthly | String |
| `StartDateTime` | La date et l'heure de début (pour un horaire unique) | DateTime |
| `EndDateTime` | La date et l'heure de fin (pour un horaire unique) | DateTime |
| `WeekDay` | Le jour de la semaine (pour un horaire hebdomadaire). Valeurs possibles: Monday, Tuesday, ..., Sunday. | String |
| `MonthDay` | Le jour du mois (pour un horaire mensuel) | Int |
| `StartTime` | L'heure de début (pour un horaire quotidien, hebdomadaire ou mensuel). Format: “HH: mm”, au format 24 heures. | String |
| `EndTime` | L'heure de fin (pour un horaire quotidien, hebdomadaire ou mensuel). Format: “HH: mm”, au format 24 heures. | String |

## Endpoints de l'horaire de repos de l'opérateur

Les endpoints d'API suivants sont disponibles pour l'extraction, la création, la mise à jour et la suppression des horaires hors service pour un opérateur spécifique :

#### GET Operator/{operatorGuid}/DutySchedule

Cette méthode renverra une collection contenant tous les horaires de repos (hors service) pour l'opérateur spécifié.

Exemple :

`[  {  "Id": 2272,  "ScheduleMode": "Weekly",  "WeekDay": "Monday",  "StartTime": "08:00",  "EndTime": "16:30"  },  {  "Id": 2267,  "ScheduleMode": "Monthly",  "MonthDay": 15  "StartTime": "08:00",  "EndTime": "16:30"  }  ] `

#### POST Operator/{operatorGuid}/DutySchedule

Cette méthode créera un nouveau horaire de repos pour l'opérateur spécifié.

Exemple de données d'entrée (pour un horaire hebdomadaire):

`{  "ScheduleMode": "Weekly",  "WeekDay": "Thursday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

Comme vous pouvez le constater dans cet exemple, vous ne devez spécifier que les paramètres pertinents pour le type d'horaire que vous créez. Par exemple, MonthDay n'est pas pertinent pour un horaire hebdomadaire et StartDateTime et EndDateTime ne concernent que des planifications à usage unique.

De même, un horaire quotidien ne s’attend pas à une valeur de jour de la semaine, juste à un ScheduleMode «Daily», ainsi qu’une heure de début et une heure de fin. Et encore, un horaire mensuel n'attend que ScheduleMode «Monthly», le jour du mois, l'heure de début et l'heure de fin.

Lorsque vous créez un nouveau horaire hors service, la sortie contient l'identifiant du nouvel horaire. Exemple de sortie pour la création d'un horaire quotidien:

`{  "Id": 2272,  "ScheduleMode": "Daily",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Cette méthode met à jour l'horaire de repos donné par l'ID spécifié, pour l'opérateur spécifié. Exemple de données d'entrée :

`{  "Id": 2273,  "ScheduleMode": "Weekly",  "WeekDay": "Wednesday",  "StartTime": "08:00",  "EndTime": "16:30"  }`

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Cette méthode supprime l'horaire de repos donné par l'ID spécifié, pour l'opérateur spécifié.

## Description de l'objet Fuseau horaire

| Nom | Description | Type de données |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| `TimeZoneId` | L'identifiant unique pour ce fuseau horaire | Short |
| `Description` | La description de ce fuseau horaire | String |
| `OffsetFromUtc` | La différence avec l'UTC en minutes | Short |
| `HasDaylightSaving` | Si ce fuseau horaire utilise ou non l'heure d'été | Boolean |
| `DaylightSavingOffset` | La différence en minutes pour l'heure d'été. Non spécifié lorsque HasDaylightSaving est faux. | Short |

## Timezone endpoints

Les méthodes suivantes peuvent être utilisées pour extraire des informations de fuseau horaire. Vous pouvez utiliser ces données pour identifier le timezoneId à utiliser lorsque vous souhaitez spécifier un timezoneId pour les paramètres d'un opérateur.

#### GET Timezone

Cette requête GET renverra une collection contenant tous les fuseaux horaires.

Exemple :

`[  {  "TimezoneId": 1,  "Description": "GMT-04:00# Brazil West, Chile, Paraguay",  "OffsetFromUtc": -240,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 2,  "Description": "GMT\+06:00# Cocos Islands",  "OffsetFromUtc": 360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  },  {  "TimezoneId": 3,  "Description": "GMT\+01:00 West Central Africa",  "OffsetFromUtc": 60,  "HasDaylightSaving": false  }  // (et plein d'autres)  ]`

#### GET Timezone/{timezoneId}

Cette méthode récupérera le fuseau horaire pour le fuseau horaire dont l'ID est spécifié.

Exemple :

`{  "TimezoneId": 56,  "Description": "GMT-06:00* Central time",  "OffsetFromUtc": -360,  "HasDaylightSaving": true,  "DaylightSavingOffset": 60  }`
