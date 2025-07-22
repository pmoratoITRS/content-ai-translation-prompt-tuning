{
  "hero": {
    "title": "API du coffre-fort"
  },
  "title": "API du coffre-fort",
  "url": "[URL_BASE_TOPICS]api/api-du-coffre-fort",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le coffre-fort est utilisé pour stocker des données réutilisables, qui sont souvent des données sensibles telles que des certificats, des clés publiques et des combinaisons de nom d’utilisateur et mot de passe. Chaque élément enregistré dans le coffre-fort est appelé un *élément de coffre-fort*, et les éléments de coffre-fort sont organisés en *sections de coffre-fort*. Organiser les éléments dans des sections différentes permet aussi d’en réserver l’accès à des opérateurs et à des groupes particuliers.

Cet article décrit les méthodes API disponibles pour gérer les éléments, les sections et les autorisations liées aux sections de coffre-fort. Pour connaître les scénarios d’usage du coffre-fort, veuillez lire notre [introduction sur les coffres-forts]([LINK_URL_1]). Pour savoir comment accéder à l’API, consultez notre [introduction sur l’API v4]([LINK_URL_2]).

## Éléments de coffre-fort

Cet ensemble d’endpoints vous permet de récupérer, créer, mettre à jour et supprimer des éléments individuels du coffre-fort. En raison de la nature sensible de certains types d’éléments de coffre-fort, les données sensibles elles-mêmes ne sont jamais renvoyées.

### Description de l’objet Élément de coffre-fort

L’objet VaultItem est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|------|-----------------------------|
| [INLINE_CODE_1] | Identifiant unique de l’élément de coffre-fort |
| [INLINE_CODE_2] | Nom d’affichage de l’élément de coffre-fort |
| [INLINE_CODE_3] | Identifiant unique de la section de coffre-fort dans laquelle cet élément de coffre-fort est stocké |
| [INLINE_CODE_4] | Indique quels éléments ou moniteurs utilisent l’élément de coffre-fort. |
| [INLINE_CODE_5] | Définit le type d’élément de coffre-fort. Actuellement, les types pris en charge sont les suivants : [SHORTCODE_1] 

- [INLINE_CODE_6] : pour les fichiers d’archivage de certificats (c.-à-d. fichiers pfx), utilisés pour les certificats clients dans les moniteurs d’API multi-étapes.
- [INLINE_CODE_7] : pour les clés publiques, utilisées pour la configuration de l’authentification unique (Single Sign-On).
- [INLINE_CODE_8] : pour les combinaisons nom d’utilisateur/mot de passe, utilisées pour les paramètres d’authentification dans les moniteurs.
- [INLINE_CODE_9] : pour le stockage de fichiers, utilisé par les moniteurs de transaction en libre-service. Tous les formats de fichiers sont pris en charge. Le fichier ne doit pas dépasser 2 Mo.
- [INLINE_CODE_10] : pour la configuration d’un mot de passe à usage unique, contient une valeur secrète et permet l’authentification à deux facteurs.[SHORTCODE_2] |
   | [INLINE_CODE_11] | La valeur stockée dans l’élément de coffre-fort. Le contenu de ce champ dépend du type d’élément de coffre-fort : [SHORTCODE_3]
- Pour le type [INLINE_CODE_12] : spécifiez un encodage Base-64 de votre fichier binaire .pfx lorsque vous créez ou mettez à jour un élément de coffre-fort de ce type. Lorsque vous récupérez l’élément à nouveau, le champ Value est toujours vide (car il s’agit d’informations sensibles).
- Pour le type [INLINE_CODE_13] : spécifiez le contenu texte de votre clé publique lorsque vous créez ou mettez à jour un élément de coffre-fort de ce type. Lorsque vous récupérez l’élément à nouveau, le champ Value contient les données de la clé publique d’origine.
- Pour le type [INLINE_CODE_14] : ce champ n’est pas utilisé. À la place, utilisez les champs UserName et Password.
   [SHORTCODE_4] |
   | [INLINE_CODE_15] | Indique si la valeur stockée dans l’élément de coffre-fort est chiffrée. Si cet attribut est configuré comme vrai (true), la ou les valeurs stockées ne sont pas visibles par l’application web ou par l’API. Cette valeur ne doit pas être spécifiée lors de la création d’un nouvel élément : les éléments [INLINE_CODE_16] et [INLINE_CODE_17] sont toujours chiffrés (car ils contiennent par définition des données sensibles) alors qu’un [INLINE_CODE_18] de clé publique est par nature une information publique et peut être stockée comme du texte en clair. |
   | [INLINE_CODE_19] | Une note ou une description se rapportant à cet élément de coffre-fort
   | [INLINE_CODE_20] | La partie nom d’utilisateur d’un jeu d'identification |
   | [INLINE_CODE_21] | La partie mot de passe d’un jeu d’identification |

### Endpoints des éléments de coffre-fort

Les méthodes API suivantes sont disponibles :

| Type de requête | Endpoint | Utilisation |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET | [INLINE_CODE_22] | Renvoie tous les éléments de coffre-fort des sections auxquelles l’utilisateur a accès. |
| GET | [INLINE_CODE_23] | Renvoie l’élément de coffre-fort spécifié. |
| POST | [INLINE_CODE_24] | Crée un nouvel élément de coffre-fort avec les valeurs spécifiées. |
| PUT | [INLINE_CODE_25] | Met à jour l’élément de coffre-fort spécifié. |
| PATCH | [INLINE_CODE_26] | Met à jour certaines parties de l’élément de coffre-fort spécifié. Les valeurs [INLINE_CODE_27] et [INLINE_CODE_28] ne peuvent pas être modifiées et restent inchangées pendant cette opération. |
| DELETE | [INLINE_CODE_29] | Supprime l’élément de coffre-fort spécifié. |

#### GET /VaultItem

La requête GET [INLINE_CODE_30] n’est pas paramétrable. Elle renvoie une liste contenant tous les éléments de coffre-fort des sections que vous pouvez consulter.

Exemple de contenu :

[CODE_BLOCK_1]

#### GET /VaultItem/{VaultItemGuid}

La requête GET [INLINE_CODE_31] renvoie l’élément de coffre-fort identifié par son Guid.

Exemple d’un élément de coffre-fort renvoyé dans le contenu d’une réponse 200 :
[CODE_BLOCK_2]

Remarquez que les valeurs qui contiennent des informations sensibles sont renvoyées sous forme de chaîne vide.

#### PUT /VaultItem/{VaultItemGuid}

La requête PUT pour l’endpoint [INLINE_CODE_32] met à jour l’élément du coffre-fort identifié par son guid. Dès que vous mettez à jour un élément de coffre-fort, tout moniteur qui contient une référence à cet élément de coffre-fort est également mis à jour pour que votre modification soit prise en compte immédiatement.

Cette requête nécessite une autorisation ChangeVaultSection.

Une requête PUT exige la structure d’objet suivante :
[CODE_BLOCK_3]

Dans l’exemple ci-dessus, s’il y avait eu une valeur dans le champ Notes de l’élément de coffre-fort original, le champ Notes aurait été vide. [INLINE_CODE_33] Les seules valeurs qui n’ont pas besoin d’être fournies sont les valeurs sensibles. Si, par exemple, vous omettez le champ Value ou Password, ou la totalité de l’objet CertificateArchive, ceux-ci resteront inchangés. De plus, les attributs IsSensitive et VaultSectionGuid ne peuvent pas être modifiés.

#### DELETE /VaultItem/{VaultItemGuid}

La requête DELETE pour l’endpoint [INLINE_CODE_34] efface l’élément indiqué.

Si l’élément de coffre-fort est en cours d’utilisation (par exemple, un moniteur y fait référence), alors le service renvoie le code d’état 400 avec un message d’explication. Cette requête nécessite une autorisation ChangeVaultSection.

#### POST /VaultItem

La requête POST pour l’endpoint [INLINE_CODE_35] créera un nouvel objet VaultItem. Lorsque vous indiquez les données pour le VaultItem, omettez le VaultItemGuid : le nouveau GUID pour cet article sera renvoyé dans la réponse. Cette requête nécessite une autorisation ChangeVaultSection.

Exemple de contenu :
[CODE_BLOCK_4]

## Sections du coffre-fort

Cette API fournit plusieurs endpoints pour gérer vos sections de coffre-fort. Chaque objet de coffre-fort appartient à une seule section de coffre-fort. Si vous n’avez besoin que de quelques éléments de coffre-fort pour tout votre compte, vous pouvez simplement les conserver dans une seule section de coffre-fort.  En revanche, si le nombre d’éléments de coffre-fort liés à votre compte commence à augmenter, il peut être judicieux de commencer à les organiser en sections distinctes.

Par défaut, chaque compte Uptrends compte une seule section de coffre-fort. Le groupe Administrateurs dispose d’un accès complet à cette section, ce qui signifie que les administrateurs peuvent modifier la section et tous les éléments de coffre-fort qu’elle contient.

Lorsqu’une nouvelle section de coffre-fort est créée, l’utilisateur (opérateur) associé au compte API à l’origine de cette création obtient automatiquement l’autorisation ChangeVaultSection pour la nouvelle section. Aucune autre autorisation n’est créée.

### Description de l’objet Section de coffre-fort

L’objet VaultSection est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|--------------------|--------------------------------------------|
| [INLINE_CODE_36] | Identifiant unique de la section de coffre-fort |
| [INLINE_CODE_37] | Nom de la section de coffre-fort |

### Endpoints des sections de coffre-fort

| Type de requête | Endpoint | Utilisation |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET | [INLINE_CODE_38] | Renvoie toutes les sections de coffre-fort auxquelles l’utilisateur a accès. |
| GET | [INLINE_CODE_39] | Renvoie la section de coffre-fort indiquée. |
| POST | [INLINE_CODE_40] | Crée un nouvel élément de coffre-fort avec le nom indiqué. |
| PUT | [INLINE_CODE_41] | Met à jour la section de coffre-fort indiquée. |
| DELETE | [INLINE_CODE_42] | Supprime la section de coffre-fort indiquée. |

#### GET /VaultSection

La requête GET [INLINE_CODE_43] n’est pas paramétrable. Elle renvoie une liste contenant toutes les sections de coffre-fort que vous pouvez consulter.

Exemple de contenu :
[CODE_BLOCK_5]

#### GET /VaultSection/{VaultSectionGuid}

La requête GET [INLINE_CODE_44] renvoie la section de coffre-fort identifiée par son GUID.

Exemple de contenu :
[CODE_BLOCK_6]


#### POST /VaultSection

La requête POST pour l’endpoint [INLINE_CODE_45] crée un nouvel objet VaultSection. L’opérateur dans le contexte duquel la requête a été émise recevra les autorisations ViewVaultSection et ChangeVaultSection pour cette nouvelle section. Aucune autre autorisation n’est créée. Lorsque vous fournissez les données pour l’objet VaultSection, omettez le VaultSectionGuid : le nouveau GUID pour cette section sera renvoyé dans la réponse.
[CODE_BLOCK_7]

#### PUT /VaultSection/{VaultSectionGuid}

La requête PUT pour l’endpoint [INLINE_CODE_46] met à jour la section de coffre-fort identifiée par le GUID de l’élément de coffre-fort. En règle générale, le seul but de cette opération est de modifier le nom de la section du coffre-fort. Cette requête nécessite une autorisation ChangeVaultSection.

[CODE_BLOCK_8]

#### DELETE /VaultSection/{VaultSectionGuid}

La requête DELETE pour l’endpoint [INLINE_CODE_47] supprime la section de coffre-fort demandée.

Si la section de coffre-fort est en cours d’utilisation (par exemple, des éléments de coffre-fort y sont stockés), alors le service renvoie le code d’état 400 avec un message d’explication. Si tel est le cas, vous devrez supprimer les éléments du coffre-fort avant de pouvoir supprimer la section. Gardez à l’esprit que vous ne pouvez pas supprimer un élément de coffre-fort si celui-ci est utilisé (par exemple, lorsqu’un moniteur est configuré pour utiliser cet élément de coffre-fort). Cette requête nécessite une autorisation ChangeVaultSection.

## Autorisations liées aux sections de coffre-fort

En plus de séparer les éléments du coffre-fort, les sections du coffre-fort vous permettent de contrôler qui a accès à quoi. Si vous souhaitez qu’un groupe d’opérateurs spécifique dispose d’un accès réservé à certains éléments du coffre-fort, placez ces éléments dans une section distincte. Seules les personnes ayant accès à cette section de coffre-fort peuvent voir les éléments de coffre-fort contenus dans cette section.

Lorsque vous créez une nouvelle section de coffre-fort (via l’API ou l’application en ligne), cette section n’est visible que par vous dans un premier temps. Si vous y avez ajouté des éléments de coffre-fort, les autres opérateurs ne peuvent ni modifier ni utiliser ces éléments.

Afin de permettre aux autres utilisateurs d’utiliser la nouvelle section du coffre-fort, d’y ajouter des éléments et/ou de sélectionner ces éléments dans les paramètres d’un moniteur, vous devez leur en donner l’accès. Pour cela, vous pouvez utiliser les méthodes API suivantes.

Il existe deux types d’autorisations : [INLINE_CODE_48] et [INLINE_CODE_49]. Ces types d’autorisation peuvent être accordés aux opérateurs et aux groupes d’opérateurs.

### Description de l’objet Autorisation

L’objet Authorization est utilisé dans les méthodes API décrites ci-dessous :

| Nom | Description |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_50] | Identifiant unique de l’autorisation |
| [INLINE_CODE_51] | Identifiant unique du contexte pour lequel l’autorisation est créée. Dans le cas d’une autorisation de section de coffre-fort, il s’agit du GUID de la section. |
| [INLINE_CODE_52] | [INLINE_CODE_53] ou [INLINE_CODE_54]. |
| [INLINE_CODE_55] | Si l’autorisation doit être accordée à un seul opérateur, cela fournit le GUID de l’opérateur. La valeur [INLINE_CODE_56] s’applique pour les autorisations de groupe d’opérateurs. |
| [INLINE_CODE_57] | Si l’autorisation doit être accordée à un groupe d’opérateurs, cela fournit l’ID du groupe d’opérateurs. La valeur [INLINE_CODE_58] s’applique pour les autorisations de groupe d’opérateurs. |

### Endpoints pour les autorisations liées aux sections de coffre-fort

| Type de requête | Endpoint | Utilisation |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET | [INLINE_CODE_59] | Renvoie une liste de toutes les autorisations pour la section de coffre-fort indiquée. |
| POST | [INLINE_CODE_60] | Crée une nouvelle autorisation pour la section de coffre-fort indiquée, en utilisant les valeurs fournies. |
| DELETE | [INLINE_CODE_61] | Supprime l’autorisation indiquée. |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

La requête GET pour l’endpoint [INLINE_CODE_62] renvoie une liste de toutes les autorisations pour la section de coffre-fort spécifiée par VaultSectionGuid.

Exemple de contenu :
[CODE_BLOCK_9]


Une autorisation s’applique soit à un opérateur, soit à un groupe d’opérateurs. L’autorisation pour un opérateur fournit une valeur pour l’OperatorGuid et aucune valeur pour l’OperatorGroupID. Dans le cas de l’autorisation pour un groupe d’opérateurs, c’est le contraire qui s’applique.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

La requête POST pour l’endpoint [INLINE_CODE_63] crée une nouvelle autorisation pour la section de coffre-fort indiquée.

Exemple de contenu :

[CODE_BLOCK_10]

Si vous créez une autorisation de type ChangeVaultSection, l’autorisation supplémentaire de ViewVaultSection pour le même opérateur ou groupe d’opérateurs est ajoutée automatiquement. Si un opérateur ou un groupe d'opérateurs dispose des autorisations "Changer + Voir", l’autorisation affichera *Contrôle complet* dans l’application Uptrends.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

La requête DELETE pour l’endpoint [INLINE_CODE_64] supprime l’autorisation existante.
