{
"hero": {
"title": "API du coffre-fort"
},
"title": "API du coffre-fort",
"url": "/support/kb/api/api-du-coffre-fort",
"translationKey": "https://www.uptrends.com/support/kb/api/vault-api"
}

Le coffre-fort est utilisé pour stocker des données réutilisables, qui sont souvent des données sensibles telles que des certificats, des clés publiques et des combinaisons de nom d’utilisateur et mot de passe. Chaque élément enregistré dans le coffre-fort est appelé un *élément de coffre-fort*, et les éléments de coffre-fort sont organisés en *sections de coffre-fort*. Organiser les éléments dans des sections différentes permet aussi d’en réserver l’accès à des opérateurs et à des groupes particuliers.

Cet article décrit les méthodes API disponibles pour gérer les éléments, les sections et les autorisations liées aux sections de coffre-fort. Pour connaître les scénarios d’usage du coffre-fort, veuillez lire notre [introduction sur les coffres-forts]({{< ref path="/support/kb/account/vault" lang="fr" >}}). Pour savoir comment accéder à l’API, consultez notre [introduction sur l’API v4]({{< ref path="/support/kb/api/v4" lang="fr" >}}).

## Éléments de coffre-fort

Cet ensemble d’endpoints vous permet de récupérer, créer, mettre à jour et supprimer des éléments individuels du coffre-fort. En raison de la nature sensible de certains types d’éléments de coffre-fort, les données sensibles elles-mêmes ne sont jamais renvoyées.

### Description de l’objet Élément de coffre-fort

L’objet VaultItem est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|------|-----------------------------|
| `VaultItemGuid` | Identifiant unique de l’élément de coffre-fort |
| `Name` | Nom d’affichage de l’élément de coffre-fort |
| `VaultSectionGuid	` | Identifiant unique de la section de coffre-fort dans laquelle cet élément de coffre-fort est stocké |
| `VaultItemUsedBy` | Indique quels éléments ou moniteurs utilisent l’élément de coffre-fort. |
| `VaultItemType` | Définit le type d’élément de coffre-fort. Actuellement, les types pris en charge sont les suivants : {{< tableformatter >}} 

- `CertificateArchive` : pour les fichiers d’archivage de certificats (c.-à-d. fichiers pfx), utilisés pour les certificats clients dans les moniteurs d’API multi-étapes.
- `Certificate` : pour les clés publiques, utilisées pour la configuration de l’authentification unique (Single Sign-On).
- `CredentialSet` : pour les combinaisons nom d’utilisateur/mot de passe, utilisées pour les paramètres d’authentification dans les moniteurs.
- `File` : pour le stockage de fichiers, utilisé par les moniteurs de transaction en libre-service. Tous les formats de fichiers sont pris en charge. Le fichier ne doit pas dépasser 2 Mo.
- `OneTimePassword` : pour la configuration d’un mot de passe à usage unique, contient une valeur secrète et permet l’authentification à deux facteurs.{{< /tableformatter >}} |
   | `Value` | La valeur stockée dans l’élément de coffre-fort. Le contenu de ce champ dépend du type d’élément de coffre-fort : {{< tableformatter >}}
- Pour le type `CertificateArchive` : spécifiez un encodage Base-64 de votre fichier binaire .pfx lorsque vous créez ou mettez à jour un élément de coffre-fort de ce type. Lorsque vous récupérez l’élément à nouveau, le champ Value est toujours vide (car il s’agit d’informations sensibles).
- Pour le type `Certificate` : spécifiez le contenu texte de votre clé publique lorsque vous créez ou mettez à jour un élément de coffre-fort de ce type. Lorsque vous récupérez l’élément à nouveau, le champ Value contient les données de la clé publique d’origine.
- Pour le type `CredentialSet` : ce champ n’est pas utilisé. À la place, utilisez les champs UserName et Password.
   {{< /tableformatter >}} |
   | `IsSensitive` | Indique si la valeur stockée dans l’élément de coffre-fort est chiffrée. Si cet attribut est configuré comme vrai (true), la ou les valeurs stockées ne sont pas visibles par l’application web ou par l’API. Cette valeur ne doit pas être spécifiée lors de la création d’un nouvel élément : les éléments `CertificateArchive` et `CredentialSet` sont toujours chiffrés (car ils contiennent par définition des données sensibles) alors qu’un `certificat` de clé publique est par nature une information publique et peut être stockée comme du texte en clair. |
   | `Notes` | Une note ou une description se rapportant à cet élément de coffre-fort
   | `UserName` | La partie nom d’utilisateur d’un jeu d'identification |
   | `Password` | La partie mot de passe d’un jeu d’identification |

### Endpoints des éléments de coffre-fort

Les méthodes API suivantes sont disponibles :

| Type de requête | Endpoint | Utilisation |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET | `VaultItem` | Renvoie tous les éléments de coffre-fort des sections auxquelles l’utilisateur a accès. |
| GET | `VaultItem/{VaultItemGuid}` | Renvoie l’élément de coffre-fort spécifié. |
| POST | `VaultItem` | Crée un nouvel élément de coffre-fort avec les valeurs spécifiées. |
| PUT | `VaultItem/{VaultItemGuid}` | Met à jour l’élément de coffre-fort spécifié. |
| PATCH | `VaultItem/{VaultItemGuid}` | Met à jour certaines parties de l’élément de coffre-fort spécifié. Les valeurs `VaultItemType` et `VaultItemUsedBy` ne peuvent pas être modifiées et restent inchangées pendant cette opération. |
| DELETE | `VaultItem/{VaultItemGuid}` | Supprime l’élément de coffre-fort spécifié. |

#### GET /VaultItem

La requête GET `VaultItem` n’est pas paramétrable. Elle renvoie une liste contenant tous les éléments de coffre-fort des sections que vous pouvez consulter.

Exemple de contenu :

```json
[
  {
    "VaultItemGuid": " FE1656C1-A606-43BB-BD61-1EEE9715EE9E ",
    "Name": "Web shop test login",
    "Value": "",
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "test@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
    "VaultItemUsedBy": "1 monitor"
  },
  {
    "VaultItemGuid": "A9CB1BE3-1715-4C31-9040-51CBBFAE23CB",
    "Name": "Marketing web site login",
    "Value": "",
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F ",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "testmarketing@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
  "VaultItemUsedBy": "-"
  }
]
```

#### GET /VaultItem/{VaultItemGuid}

La requête GET `VaultItem/{VaultItemGuid}` renvoie l’élément de coffre-fort identifié par son Guid.

Exemple d’un élément de coffre-fort renvoyé dans le contenu d’une réponse 200 :
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "IsSensitive": true,
  "Notes": "Certificate archive test",
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Issuer": "Acme Corp, Inc.",
    "NotBefore": "2018-06-12T14:10:50.489Z",
    "NotAfter": "2020-06-12T14:10:50.489Z",
    "Password": "",
    "ArchiveData": ""
  },
  "VaultItemUsedBy": "1 monitor"
}
```

Remarquez que les valeurs qui contiennent des informations sensibles sont renvoyées sous forme de chaîne vide.

#### PUT /VaultItem/{VaultItemGuid}

La requête PUT pour l’endpoint `VaultItem/{VaultItemGuid}` met à jour l’élément du coffre-fort identifié par son guid. Dès que vous mettez à jour un élément de coffre-fort, tout moniteur qui contient une référence à cet élément de coffre-fort est également mis à jour pour que votre modification soit prise en compte immédiatement.

Cette requête nécessite une autorisation ChangeVaultSection.

Une requête PUT exige la structure d’objet suivante :
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CredentialSet",
  "IsSensitive": true,
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

Dans l’exemple ci-dessus, s’il y avait eu une valeur dans le champ Notes de l’élément de coffre-fort original, le champ Notes aurait été vide. `Si vous omettez un paramètre, il ne restera pas inchangé, mais sera considéré comme vide.` Les seules valeurs qui n’ont pas besoin d’être fournies sont les valeurs sensibles. Si, par exemple, vous omettez le champ Value ou Password, ou la totalité de l’objet CertificateArchive, ceux-ci resteront inchangés. De plus, les attributs IsSensitive et VaultSectionGuid ne peuvent pas être modifiés.

#### DELETE /VaultItem/{VaultItemGuid}

La requête DELETE pour l’endpoint `VaultItem/{VaultItemGuid}` efface l’élément indiqué.

Si l’élément de coffre-fort est en cours d’utilisation (par exemple, un moniteur y fait référence), alors le service renvoie le code d’état 400 avec un message d’explication. Cette requête nécessite une autorisation ChangeVaultSection.

#### POST /VaultItem

La requête POST pour l’endpoint `VaultItem` créera un nouvel objet VaultItem. Lorsque vous indiquez les données pour le VaultItem, omettez le VaultItemGuid : le nouveau GUID pour cet article sera renvoyé dans la réponse. Cette requête nécessite une autorisation ChangeVaultSection.

Exemple de contenu :
```json
{
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "Notes": "Certificate archive test",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

## Sections du coffre-fort

Cette API fournit plusieurs endpoints pour gérer vos sections de coffre-fort. Chaque objet de coffre-fort appartient à une seule section de coffre-fort. Si vous n’avez besoin que de quelques éléments de coffre-fort pour tout votre compte, vous pouvez simplement les conserver dans une seule section de coffre-fort.  En revanche, si le nombre d’éléments de coffre-fort liés à votre compte commence à augmenter, il peut être judicieux de commencer à les organiser en sections distinctes.

Par défaut, chaque compte Uptrends compte une seule section de coffre-fort. Le groupe Administrateurs dispose d’un accès complet à cette section, ce qui signifie que les administrateurs peuvent modifier la section et tous les éléments de coffre-fort qu’elle contient.

Lorsqu’une nouvelle section de coffre-fort est créée, l’utilisateur (opérateur) associé au compte API à l’origine de cette création obtient automatiquement l’autorisation ChangeVaultSection pour la nouvelle section. Aucune autre autorisation n’est créée.

### Description de l’objet Section de coffre-fort

L’objet VaultSection est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|--------------------|--------------------------------------------|
| `VaultSectionGuid` | Identifiant unique de la section de coffre-fort |
| `Name` | Nom de la section de coffre-fort |

### Endpoints des sections de coffre-fort

| Type de requête | Endpoint | Utilisation |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET | `VaultSection` | Renvoie toutes les sections de coffre-fort auxquelles l’utilisateur a accès. |
| GET | `VaultSection/{VaultSectionGuid}` | Renvoie la section de coffre-fort indiquée. |
| POST | `VaultSection` | Crée un nouvel élément de coffre-fort avec le nom indiqué. |
| PUT | `VaultSection/{VaultSectionGuid}` | Met à jour la section de coffre-fort indiquée. |
| DELETE | `VaultSection/{VaultSectionGuid}` | Supprime la section de coffre-fort indiquée. |

#### GET /VaultSection

La requête GET `VaultSection` n’est pas paramétrable. Elle renvoie une liste contenant toutes les sections de coffre-fort que vous pouvez consulter.

Exemple de contenu :
```json
[
  {
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "Name": "Vault items"
  },
  {
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F",
    "Name": "Marketing web site vault items"
  }
]
```

#### GET /VaultSection/{VaultSectionGuid}

La requête GET `VaultSection/{VaultSectionGuid}` renvoie la section de coffre-fort identifiée par son GUID.

Exemple de contenu :
```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Vault items"
}
```


#### POST /VaultSection

La requête POST pour l’endpoint `VaultSection` crée un nouvel objet VaultSection. L’opérateur dans le contexte duquel la requête a été émise recevra les autorisations ViewVaultSection et ChangeVaultSection pour cette nouvelle section. Aucune autre autorisation n’est créée. Lorsque vous fournissez les données pour l’objet VaultSection, omettez le VaultSectionGuid : le nouveau GUID pour cette section sera renvoyé dans la réponse.
```json
{
  "Name": "Development vault items"
}
```

#### PUT /VaultSection/{VaultSectionGuid}

La requête PUT pour l’endpoint `VaultSection/{VaultSectionGuid}` met à jour la section de coffre-fort identifiée par le GUID de l’élément de coffre-fort. En règle générale, le seul but de cette opération est de modifier le nom de la section du coffre-fort. Cette requête nécessite une autorisation ChangeVaultSection.

```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Web shop vault items"
}
```

#### DELETE /VaultSection/{VaultSectionGuid}

La requête DELETE pour l’endpoint `VaultSection/{VaultSectionGuid}` supprime la section de coffre-fort demandée.

Si la section de coffre-fort est en cours d’utilisation (par exemple, des éléments de coffre-fort y sont stockés), alors le service renvoie le code d’état 400 avec un message d’explication. Si tel est le cas, vous devrez supprimer les éléments du coffre-fort avant de pouvoir supprimer la section. Gardez à l’esprit que vous ne pouvez pas supprimer un élément de coffre-fort si celui-ci est utilisé (par exemple, lorsqu’un moniteur est configuré pour utiliser cet élément de coffre-fort). Cette requête nécessite une autorisation ChangeVaultSection.

## Autorisations liées aux sections de coffre-fort

En plus de séparer les éléments du coffre-fort, les sections du coffre-fort vous permettent de contrôler qui a accès à quoi. Si vous souhaitez qu’un groupe d’opérateurs spécifique dispose d’un accès réservé à certains éléments du coffre-fort, placez ces éléments dans une section distincte. Seules les personnes ayant accès à cette section de coffre-fort peuvent voir les éléments de coffre-fort contenus dans cette section.

Lorsque vous créez une nouvelle section de coffre-fort (via l’API ou l’application en ligne), cette section n’est visible que par vous dans un premier temps. Si vous y avez ajouté des éléments de coffre-fort, les autres opérateurs ne peuvent ni modifier ni utiliser ces éléments.

Afin de permettre aux autres utilisateurs d’utiliser la nouvelle section du coffre-fort, d’y ajouter des éléments et/ou de sélectionner ces éléments dans les paramètres d’un moniteur, vous devez leur en donner l’accès. Pour cela, vous pouvez utiliser les méthodes API suivantes.

Il existe deux types d’autorisations : `ViewVaultSection` et `ChangeVaultSection`. Ces types d’autorisation peuvent être accordés aux opérateurs et aux groupes d’opérateurs.

### Description de l’objet Autorisation

L’objet Authorization est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AuthorizationId` | Identifiant unique de l’autorisation |
| `ContextId` | Identifiant unique du contexte pour lequel l’autorisation est créée. Dans le cas d’une autorisation de section de coffre-fort, il s’agit du GUID de la section. |
| `AuthorizationType` | `ViewVaultSection` ou `ChangeVaultSection`. |
| `OperatorGuid` | Si l’autorisation doit être accordée à un seul opérateur, cela fournit le GUID de l’opérateur. La valeur `null` s’applique pour les autorisations de groupe d’opérateurs. |
| `OperatorGroupId` | Si l’autorisation doit être accordée à un groupe d’opérateurs, cela fournit l’ID du groupe d’opérateurs. La valeur `null` s’applique pour les autorisations de groupe d’opérateurs. |

### Endpoints pour les autorisations liées aux sections de coffre-fort

| Type de requête | Endpoint | Utilisation |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET | `VaultSection/{VaultSectionGuid}/Authorization` | Renvoie une liste de toutes les autorisations pour la section de coffre-fort indiquée. |
| POST | `VaultSection/{VaultSectionGuid}/Authorization` | Crée une nouvelle autorisation pour la section de coffre-fort indiquée, en utilisant les valeurs fournies. |
| DELETE | `VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}` | Supprime l’autorisation indiquée. |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

La requête GET pour l’endpoint `VaultSection/{VaultSectionGuid}/Authorization` renvoie une liste de toutes les autorisations pour la section de coffre-fort spécifiée par VaultSectionGuid.

Exemple de contenu :
```json
[
  {
    "AuthorizationId": "7210DD2D-3AAE-4F89-A2A8-000060F118F1 ",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ChangeVaultSection",
    "OperatorGuid": "5F71AFD7-8BEE-4C8D-9827-A107308473BE",
    "OperatorGroupId": ""
  },
  {
    "AuthorizationId": "0BACEE61-0582-40FD-B1A2-00034401421A",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ViewVaultSection",
    "OperatorGuid": "",
    "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
  }
]
```


Une autorisation s’applique soit à un opérateur, soit à un groupe d’opérateurs. L’autorisation pour un opérateur fournit une valeur pour l’OperatorGuid et aucune valeur pour l’OperatorGroupID. Dans le cas de l’autorisation pour un groupe d’opérateurs, c’est le contraire qui s’applique.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

La requête POST pour l’endpoint `VaultSection/{VaultSectionGuid}/Authorization` crée une nouvelle autorisation pour la section de coffre-fort indiquée.

Exemple de contenu :

```json
{
  "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "AuthorizationType": "ViewVaultSection",
  "OperatorGuid": "",
  "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
}
```

Si vous créez une autorisation de type ChangeVaultSection, l’autorisation supplémentaire de ViewVaultSection pour le même opérateur ou groupe d’opérateurs est ajoutée automatiquement. Si un opérateur ou un groupe d'opérateurs dispose des autorisations "Changer + Voir", l’autorisation affichera *Contrôle complet* dans l’application Uptrends.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

La requête DELETE pour l’endpoint `VaultSection/{VaultSectionGuid}/ Authorization/AuthorizationGuid` supprime l’autorisation existante.
