{
  "hero": {
    "title": "API Opérateurs"
  },
  "title": "API Opérateurs",
  "summary": "Les méthodes d'API disponibles pour manipuler les opérateurs.",
  "url": "[URL_BASE_TOPICS]api/operator-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cette page décrit les méthodes d'API disponibles pour manipuler les opérateurs, c'est-à-dire les comptes de connexion spécifiques à l'utilisateur. Les méthodes permettant de manipuler l'horaire d'un opérateur en-dehors des heures de travail (horaire hors service) sont décrites dans une section distincte ci-dessous. La dernière section de cette page décrit l'API de fuseau horaire, dont vous pouvez avoir besoin pour mettre à jour le paramètre de fuseau horaire spécifique d'un opérateur.

## Description de l'objet opérateur

L'objet Opérateur suivant est utilisé dans les méthodes de l'API décrites ci-dessous :

| Nom | Description | Type de données |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | Identifiant unique pour cet opérateur. | Guid |
| [INLINE_CODE_2] | Adresse e-mail principale et nom de connexion de l'opérateur. | String |
| [INLINE_CODE_3] | Le mot de passe de l'opérateur. | String |
| [INLINE_CODE_4] | Le nom complet de cet opérateur. | String |
| [INLINE_CODE_5] | Le numéro de téléphone portable de l'opérateur. | String |
| [INLINE_CODE_6] | Le numéro de téléphone sortant de l'opérateur. | String |
| [INLINE_CODE_7] | Indique si l'opérateur est l'administrateur du compte. Ceci est un champ en lecture seule. | Boolean |
| [INLINE_CODE_8] | L'adresse e-mail de secours pour cet opérateur. | String |
| [INLINE_CODE_9] | Indique si cet opérateur est actuellement en service. | Boolean |
| [INLINE_CODE_10] | S'il est renseigné, définit la culture de cet opérateur. Valeurs possibles : en-US, en-GB, fr-FR, de-DE, nl-NL ou vide. Lorsque cette valeur est définie sur vide, la culture/langue générale du compte est utilisée | String |
| [INLINE_CODE_11] | Optionnel. Identifiant du paramètre de fuseau horaire de cet utilisateur. Reportez-vous à l'API de fuseau horaire mentionné ci-dessous pour connaître les valeurs disponibles. S'il n'est pas spécifié, le fuseau horaire du compte sera utilisé pour cet utilisateur. | Short |
| [INLINE_CODE_12] | Le fournisseur de SMS utilisé par l'opérateur. Valeurs possibles : UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational | String |
| [INLINE_CODE_13] | Si le fournisseur SMS est configuré spécifiquement pour cet opérateur, ce champ indique si un identifiant téléphonique numérique doit être utilisé. | Boolean |
| [INLINE_CODE_14] | Le fournisseur utilisé pour les alertes téléphoniques. | String |
| [INLINE_CODE_15] | Si la connexion native (nom d'utilisateur/mot de passe) est disponible et configurée pour votre compte, indique si cet opérateur est autorisé à se connecter à Uptrends à l'aide de son nom d'utilisateur et de son mot de passe Uptrends. Valeurs possibles : True, False ou non-spécifié pour utiliser le paramètre de compte général. | Boolean |
| [INLINE_CODE_16] | Si Single Signon est disponible et configuré pour votre compte, indique si cet opérateur est autorisé à utiliser Single Sign-On. Valeurs possibles : True, False ou non-spécifié pour utiliser le paramètre de compte général. | Boolean |

## Endpoints Operateur

Les points de terminaison API suivants sont disponibles pour extraire, créer, mettre à jour et supprimer des opérateurs :

| Type de requête | Endpoint | Utilisation |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET | [INLINE_CODE_17] | Liste tous les opérateurs. |
| GET | [INLINE_CODE_18] | Liste les détails d'un opérateur. |
| POST | [INLINE_CODE_19] | Crée un nouvel opérateur. |
| PUT | [INLINE_CODE_20] | Met à jour un opérateur existant. |
| DELETE | [INLINE_CODE_21] | Supprime un opérateur existant. Note: vous ne pouvez pas supprimer l'opérateur associé au compte API que vous utilisez. |
| GET | [INLINE_CODE_22] | Obtient les horaires de repos pour un opérateur existant. |
| POST | [INLINE_CODE_23] | Ajoute un horaire de repos pour un opérateur existant. |
| PUT | [INLINE_CODE_24] | Met à jour l'horaire de repos spécifié. |
| DELETE | [INLINE_CODE_25] | Supprime l'horaire de repos spécifié. |

#### GET Operator

Cette requête GET renverra une collection contenant tous les opérateurs, y compris l'administrateur du compte.

[INLINE_CODE_26]

#### GET Operator/{operatorGuid}

Cette requête GET renverra les détails de l'opérateur spécifique identifié par l'opérateur GUID spécifié.

Exemple :

[INLINE_CODE_27]

#### POST Operator

Créera un nouvel opérateur avec les détails fournis.

Exemple de données d'entrée :

[INLINE_CODE_28]

La réponse contiendra l'opérateur créé, y compris l'opérateur GUID attribué :

[INLINE_CODE_29]

#### PUT Operator/{operatorGuid}

Cette méthode met à jour l'opérateur identifié par l'opérateur GUID spécifié, à l'aide des données fournies dans la requête.

Exemple de données d'entrée :

[INLINE_CODE_30]

#### DELETE Operator/{operatorGuid}

Cette méthode supprimera l'opérateur identifié par le GUID opérateur spécifié, à l'aide des données fournies dans la demande.

## Description de l'objet Horaire de repos de l'opérateur

| Nom | Description | Type de données |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_31] | L'identifiant unique de cet horaire de repos. Ce champ est en lecture seule et sera généré automatiquement. | Guid |
| [INLINE_CODE_32] | Le mode de l'horaire. Possible values: OneTime, Daily, Weekly, Monthly | String |
| [INLINE_CODE_33] | La date et l'heure de début (pour un horaire unique) | DateTime |
| [INLINE_CODE_34] | La date et l'heure de fin (pour un horaire unique) | DateTime |
| [INLINE_CODE_35] | Le jour de la semaine (pour un horaire hebdomadaire). Valeurs possibles: Monday, Tuesday, ..., Sunday. | String |
| [INLINE_CODE_36] | Le jour du mois (pour un horaire mensuel) | Int |
| [INLINE_CODE_37] | L'heure de début (pour un horaire quotidien, hebdomadaire ou mensuel). Format: “HH: mm”, au format 24 heures. | String |
| [INLINE_CODE_38] | L'heure de fin (pour un horaire quotidien, hebdomadaire ou mensuel). Format: “HH: mm”, au format 24 heures. | String |

## Endpoints de l'horaire de repos de l'opérateur

Les endpoints d'API suivants sont disponibles pour l'extraction, la création, la mise à jour et la suppression des horaires hors service pour un opérateur spécifique :

#### GET Operator/{operatorGuid}/DutySchedule

Cette méthode renverra une collection contenant tous les horaires de repos (hors service) pour l'opérateur spécifié.

Exemple :

[INLINE_CODE_39]

#### POST Operator/{operatorGuid}/DutySchedule

Cette méthode créera un nouveau horaire de repos pour l'opérateur spécifié.

Exemple de données d'entrée (pour un horaire hebdomadaire):

[INLINE_CODE_40]

Comme vous pouvez le constater dans cet exemple, vous ne devez spécifier que les paramètres pertinents pour le type d'horaire que vous créez. Par exemple, MonthDay n'est pas pertinent pour un horaire hebdomadaire et StartDateTime et EndDateTime ne concernent que des planifications à usage unique.

De même, un horaire quotidien ne s’attend pas à une valeur de jour de la semaine, juste à un ScheduleMode «Daily», ainsi qu’une heure de début et une heure de fin. Et encore, un horaire mensuel n'attend que ScheduleMode «Monthly», le jour du mois, l'heure de début et l'heure de fin.

Lorsque vous créez un nouveau horaire hors service, la sortie contient l'identifiant du nouvel horaire. Exemple de sortie pour la création d'un horaire quotidien:

[INLINE_CODE_41]

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Cette méthode met à jour l'horaire de repos donné par l'ID spécifié, pour l'opérateur spécifié. Exemple de données d'entrée :

[INLINE_CODE_42]

#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

Cette méthode supprime l'horaire de repos donné par l'ID spécifié, pour l'opérateur spécifié.

## Description de l'objet Fuseau horaire

| Nom | Description | Type de données |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_43] | L'identifiant unique pour ce fuseau horaire | Short |
| [INLINE_CODE_44] | La description de ce fuseau horaire | String |
| [INLINE_CODE_45] | La différence avec l'UTC en minutes | Short |
| [INLINE_CODE_46] | Si ce fuseau horaire utilise ou non l'heure d'été | Boolean |
| [INLINE_CODE_47] | La différence en minutes pour l'heure d'été. Non spécifié lorsque HasDaylightSaving est faux. | Short |

## Timezone endpoints

Les méthodes suivantes peuvent être utilisées pour extraire des informations de fuseau horaire. Vous pouvez utiliser ces données pour identifier le timezoneId à utiliser lorsque vous souhaitez spécifier un timezoneId pour les paramètres d'un opérateur.

#### GET Timezone

Cette requête GET renverra une collection contenant tous les fuseaux horaires.

Exemple :

[INLINE_CODE_48]

#### GET Timezone/{timezoneId}

Cette méthode récupérera le fuseau horaire pour le fuseau horaire dont l'ID est spécifié.

Exemple :

[INLINE_CODE_49]
