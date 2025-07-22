{
  "hero": {
    "title": "API MonitorGroup"
  },
  "title": "API MonitorGroup",
  "summary": "Présentation des méthodes disponibles pour manipuler les groupes de moniteurs via l’API.",
  "url": "[URL_BASE_TOPICS]api/monitorgroup-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cette page décrit les méthodes de l’API permettant de manipuler les groupes de moniteurs. Pour en savoir plus, consultez la [documentation de l'API MonitorGroup d'Uptrends]([LINK_URL_1]).

## Description de l'objet MonitorGroup

L'objet MonitorGroup suivant est utilisé dans les points de terminaison de l'API MonitorGroup :

| Nom | Description | Type de données |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | Identifiant unique du groupe de moniteurs | Chaîne |
| [INLINE_CODE_2] | Nom du groupe de moniteurs | Chaîne |
| [INLINE_CODE_3] | [SHORTCODE_1] |
Indique si le groupe de moniteurs correspond à l'option par défaut [Tous les moniteurs]([LINK_URL_2]). [SHORTCODE_2] | Booléen |
| [INLINE_CODE_4] | Indique si le nombre de crédits pour le groupe de moniteurs est illimité ou non.  |  Booléen |
| [INLINE_CODE_5] |[SHORTCODE_3]
Fournit le nombre de crédits utilisés par les [moniteurs de disponibilité]([LINK_URL_3]). [SHORTCODE_4] | Nombre entier |
| [INLINE_CODE_6]            | [SHORTCODE_5]
Fournit le nombre de crédits utilisés par les [moniteurs de navigateur (Full Page Check)]([LINK_URL_4]). [SHORTCODE_6] | Nombre entier |
| [INLINE_CODE_7]            | [SHORTCODE_7]
Fournit le nombre de crédits utilisés par les [moniteurs de transactions]([LINK_URL_5]).  [SHORTCODE_8] | Nombre entier |
| [INLINE_CODE_8]            | [SHORTCODE_9]
Fournit le nombre de crédits utilisés par les [moniteurs d'API multi-étapes]([LINK_URL_6]) et les moniteurs [Postman]([LINK_URL_7]). [SHORTCODE_10] | Nombre entier |
| [INLINE_CODE_9]            | Fournit le nombre de crédits utilisés par les comptes qui sont abonnés au forfait incluant une seule réserve de crédit. | Nombre entier |

### Groupe Tous les moniteurs

Le groupe **Tous les moniteurs** est un groupe de systèmes ou de moniteurs qui contient tous les moniteurs par défaut. Utilisez l'identifiant GUID de ce groupe pour gérer les opérations qui concernent tous les moniteurs. Par exemple, l'activation ou l'interruption de tous les moniteurs ou de toutes les alertes.
Notez que vous ne pouvez pas modifier la composition de ce groupe.


## Points de terminaison permettant de gérer le groupe de moniteurs

Les endpoints d'API suivants sont disponibles pour créer, modifier et supprimer des groupes de moniteurs, ainsi que les moniteurs qui font partie de ces groupes.

| Type de requête | Endpoint | Utilisation |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET | [INLINE_CODE_10] | Obtenir tous les groupes de moniteurs |
| POST | [INLINE_CODE_11] | Créer un nouveau groupe de moniteurs |
| GET | [INLINE_CODE_12] | Obtenir les détails d'un groupe de moniteurs |
| PUT | [INLINE_CODE_13] | Mettre à jour un groupe de moniteurs |
| DELETE | [INLINE_CODE_14] | Supprimer un groupe de moniteurs |
| GET | [INLINE_CODE_15] | Obtenir une liste de tous les moniteurs faisant partie d'un groupe de moniteurs |
| POST | [INLINE_CODE_16] | Ajouter le moniteur spécifié à un groupe de moniteurs |
| DELETE | [INLINE_CODE_17] | Retirer le moniteur spécifié du groupe de moniteurs |

## Autres opérations liées aux groupes de moniteurs

Les endpoints d'API suivants permettent d'effectuer des opérations impliquant tous les moniteurs faisant partie d'un groupe :

| Type de requête | Endpoint | Utilisation |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST | [INLINE_CODE_18] | Désactiver tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | [INLINE_CODE_19] | Activer tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | [INLINE_CODE_20] | Désactiver les alertes de tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | [INLINE_CODE_21] | Activer les alertes de tous les moniteurs d'un groupe de moniteurs spécifié |
| POST | [INLINE_CODE_22] | Ajouter les périodes de maintenance indiquées à tous les moniteurs d'un groupe spécifié |
