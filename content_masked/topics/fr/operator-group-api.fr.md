{
  "hero": {
    "title": "Commande Operator Group de l'API"
  },
  "title": "Commande Operator Group de l'API",
  "summary": "Présentation des méthodes de la commande d'API permettant de manipuler les groupes d'opérateurs.",
  "url": "[URL_BASE_TOPICS]api/api-du-groupe-operateurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cette page décrit les méthodes de la commande d'API permettant de manipuler des groupes d'opérateurs. Les groupes d'opérateurs servent à organiser les opérateurs (comptes d'utilisateur) dans votre compte. Cette commande de l'API fournit des méthodes pour gérer chaque groupe, et pour ajouter des opérateurs au groupe ou pour en supprimer.

## Description de l'objet OperatorGroup

L'objet OperatorGroup suivant est utilisé dans les méthodes de la commande d'API décrites ci-dessous :

| Nom | Description | Type de données |
|------------------------|-------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | Identifiant unique pour ce groupe d'opérateurs | Guid |
| [INLINE_CODE_2] | Chaîne contenant un nom descriptif | Chaîne |
| [INLINE_CODE_3] | Indique s'il s'agit du groupe système "Everyone" | Booléen |
| [INLINE_CODE_4] | Indique s'il s'agit du groupe système "Administrators" | Booléen |

Le groupe "Everyone" (Tout le monde) est un groupe créé automatiquement par le système. Ce groupe ne peut pas être modifié : chaque opérateur est automatiquement ajouté à ce groupe.

Le groupe "Administrators" (Administrateurs) est également un groupe créé par le système, mais vous pouvez y ajouter des opérateurs individuels ou les supprimer. Lorsqu'un opérateur est ajouté en tant que membre du groupe Administrators, tous les privilèges d'administration lui sont automatiquement attribués.

## Endpoints pour la commande d'API OperatorGroup

Les endpoints API suivants sont disponibles pour l'extraction, la création, la mise à jour et la suppression de groupes d'opérateurs :

| Type de requête | Endpoint | Utilisation |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET | [INLINE_CODE_5] | Obtenir tous les groupes d'opérateurs. |
| GET | [INLINE_CODE_6] | Obtenir les détails d'un groupe d'opérateurs |
| POST | [INLINE_CODE_7] | Créer un nouveau groupe d'opérateurs |
| PUT | [INLINE_CODE_8] | Mettre à jour un groupe d'opérateurs |
| DELETE | [INLINE_CODE_9] | Supprimer un groupe d'opérateurs |
| GET | [INLINE_CODE_10] | Obtenir les horaires de repos d'un opérateur |
| POST | [INLINE_CODE_11] | Ajouter un horaire de repos à tous les opérateurs du groupe spécifié |
| PUT | [INLINE_CODE_12] | Mettre à jour l'horaire de repos spécifié |
| DELETE | [INLINE_CODE_13] | Supprimer l'horaire de repos spécifié |

#### GET OperatorGroup

Cette requête GET renvoie une collection contenant tous les groupes d'opérateurs, y compris les groupes système spéciaux.

[CODE_BLOCK_1]

#### GET OperatorGroup/{operatorGroupGuid}

Cette requête GET renvoie les détails du groupe d'opérateurs identifié par le GUID du groupe d'opérateurs spécifié.

Exemple de sortie :

[CODE_BLOCK_2]

#### POST OperatorGroup

Cette méthode crée un nouveau groupe d'opérateurs avec les détails fournis.

Exemple d'entrée :

[CODE_BLOCK_3]

La réponse contient le groupe d'opérateurs créé, y compris le GUID attribué :

[CODE_BLOCK_4]


#### DELETE OperatorGroup/{operatorGroupGuid}

Cette méthode supprime le groupe d'opérateurs identifié par le GUID de l'opérateur spécifié, à l'aide des données fournies dans la demande.
