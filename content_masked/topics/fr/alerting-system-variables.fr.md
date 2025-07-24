{
  "hero": {
    "title": "Variables système d'alerte"
  },
  "title": "Variables système d'alerte",
  "summary": "Vue d'ensemble des variables système disponibles pour les intégrations (personnalisées)",
  "url": "[URL_BASE_TOPICS]alerter/integrations/integrations-personnalisees/variables-systeme-alertes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Cet article présente toutes les **variables système** qui peuvent être utilisées pour compléter le message d'alerte sortant avec des informations pertinentes concernant le moniteur d'où provient l'alerte, le type d'erreur ou l'alerte elle-même. Pour plus d'informations sur l'utilisation de ces variables système, lisez notre article qui explique comment [créer le bon contenu de message]([LINK_URL_1]).

Les variables ci-dessous doivent être placées entre doubles accolades dans le contenu du message. Par exemple : [INLINE_CODE_1].

| Variable | Description | Exemple de valeur |
| --- | --- | --- |
| [INLINE_CODE_2] | Votre identifiant de compte Uptrends | [INLINE_CODE_3] |
| [INLINE_CODE_4] | Identifiant unique de cette alerte | [INLINE_CODE_5] |
| [INLINE_CODE_6] | Contient le nom ou l'emplacement du checkpoint où l'alerte a été vérifiée en dernier. | [INLINE_CODE_7] |
| [INLINE_CODE_8] | Description textuelle de l'erreur qui a déclenché cette alerte. Le numéro d'étape est inclus le cas échéant. | [INLINE_CODE_9] |
| [INLINE_CODE_10] | Temps écoulé entre la première erreur et l'alerte (OK) actuelle | [INLINE_CODE_11] |
| [INLINE_CODE_12] | [SHORTCODE_1] Identifiant du type de l'erreur qui a déclenché cette alerte. Pour consulter la liste de types d'erreur, reportez-vous à la page [Types d'erreurs]([LINK_URL_2]). [SHORTCODE_2] | [INLINE_CODE_13] |
| [INLINE_CODE_14] | Message d'échec personnalisé de l'action d'une étape de transaction d'où provient l'erreur | [INLINE_CODE_15] |
| [INLINE_CODE_16] | Même date et heure qu'avec la variable @alert.firstErrorUtc, mais d'après le fuseau horaire de votre compte. Également formaté en ISO 8601. | [INLINE_CODE_17] |
| [INLINE_CODE_18] | Identifiant de l'erreur qui a déclenché cette alerte | [INLINE_CODE_19] |
| [INLINE_CODE_20] | URL d'un lien profond qui fournit les détails de l'erreur ayant déclenché cette alerte | [INLINE_CODE_21] |
| [INLINE_CODE_22] | Description de l'erreur de la première vérification effectuée par le moniteur ayant reçu l'erreur. Le numéro d'étape est inclus le cas échéant. | [INLINE_CODE_23] |
| [INLINE_CODE_24] | Même date et heure qu'avec la variable @alert.firstErrorUtc, mais d'après le fuseau horaire et la localisation de votre compte | [INLINE_CODE_25] |
| [INLINE_CODE_26] | Date et heure de l'erreur d'origine qui a déclenché cette alerte, exprimées en heure UTC et présentées selon la norme ISO 8601 | [INLINE_CODE_27] |
| [INLINE_CODE_28] | Date et heure de l'erreur à l'origine de l'alerte, exprimées en heure UTC et présentées selon la localisation de votre compte | [INLINE_CODE_29] |
| [INLINE_CODE_30] | Contient le nombre total d'erreurs (confirmées) consécutives de l'alerte. | [INLINE_CODE_31] |
| [INLINE_CODE_32] | Adresse IP qui a été utilisée pour effectuer la vérification. Peut être une adresse IPv4 ou IPv6. | [INLINE_CODE_33] |
| [INLINE_CODE_34] | [SHORTCODE_3] Contient les en-têtes de réponse de l'alerte sous forme de paires clé-valeur. Notez que la valeur de cette variable peut être vide si la [protection des données des emplacements privés]([LINK_URL_3]) est activée sur le checkpoint privé vérifiant l'alerte. [SHORTCODE_4] | [INLINE_CODE_35] |
| [INLINE_CODE_36] | [SHORTCODE_5] Contient le corps de la réponse reçue lorsqu'il est disponible. Notez que le corps de la réponse peut contenir des caractères qui doivent être encodés, par exemple [en utilisant @JsonEncode ou @XmlEncode]([LINK_URL_4]). Le corps de la réponse sera tronqué si sa taille dépasse 1 Mo. [SHORTCODE_6] | [INLINE_CODE_37] |
| [INLINE_CODE_38] | Adresse IPv4 du serveur sur lequel la vérification a été effectuée | [INLINE_CODE_39] |
| [INLINE_CODE_40] | Adresse IPv6 du serveur sur lequel la vérification a été effectuée. | [INLINE_CODE_41] |
| [INLINE_CODE_42] | Contient la date et l'heure d'expiration du certificat SSL, qui seront prises en compte pour les alertes du moniteur SSL. | [INLINE_CODE_43] |
| [INLINE_CODE_44] | Même date et heure qu'avec la variable @alert.timestampUtc, mais d'après le fuseau horaire de votre compte. Également formaté en ISO 8601. | [INLINE_CODE_45] |
| [INLINE_CODE_46] | Même date et heure qu'avec la variable @alert.timestampUtc, mais d'après le fuseau horaire et la localisation de votre compte | [INLINE_CODE_47] |
| [INLINE_CODE_48] | Date et heure de l'alerte, exprimées en heure UTC et présentées selon la norme ISO 8601 | [INLINE_CODE_49] |
| [INLINE_CODE_50] | Date et heure de l'alerte, exprimées en heure UTC et présentées selon la localisation de votre compte | [INLINE_CODE_51] |
| [INLINE_CODE_52] | Type de ce message d'alerte : [HTML_TAG_1][HTML_TAG_2]- Alerte : une nouvelle erreur a été détectée.[HTML_TAG_3]- Ok : l'erreur d'origine a été résolue.[HTML_TAG_4]- Rappel : l'erreur d'origine n'a pas été résolue. | [INLINE_CODE_53] \| [INLINE_CODE_54] \| [INLINE_CODE_55] |
| [INLINE_CODE_56] | Identifiant unique de la définition d'alerte qui a été utilisée pour générer cette alerte | [INLINE_CODE_57] |
| [INLINE_CODE_58] | Le nom de la définition d'alerte qui a été utilisée pour générer cette alerte | [INLINE_CODE_59] |
| [INLINE_CODE_60] | [SHORTCODE_7] Référence à un [champ personnalisé]([LINK_URL_5]) qui peut servir à inclure des données personnalisées pour les moniteurs individuels. [SHORTCODE_8] | [INLINE_CODE_61] |
| [INLINE_CODE_62] | Identifiant du niveau d'escalade utilisé pour générer cette alerte | [INLINE_CODE_63] |
| [INLINE_CODE_64] | Message personnalisé qui a été configuré pour ce niveau d'escalade | [INLINE_CODE_65] |
| [INLINE_CODE_66] | Identifiant unique de l'incident associé à cette alerte. Une alerte d'erreur et une alerte Ok partagent la même clé d'incident. | [INLINE_CODE_67] |
| [INLINE_CODE_68] | URL d'un lien profond qui vous mène au dashboard de ce moniteur | [INLINE_CODE_69] |
| [INLINE_CODE_70] | URL d'un lien profond qui vous amène aux paramètres de ce moniteur | [INLINE_CODE_71] |
| [INLINE_CODE_72] | Identifiant unique du moniteur de votre compte qui a déclenché cette alerte | [INLINE_CODE_73] |
| [INLINE_CODE_74] | Nom du moniteur de votre compte qui a déclenché cette alerte | [INLINE_CODE_75] |
| [INLINE_CODE_76] | Notes personnalisées ayant été ajoutées dans les paramètres du moniteur | [INLINE_CODE_77] |
| [INLINE_CODE_78] | Type de moniteur | [INLINE_CODE_79] |
| [INLINE_CODE_80] | Adresse réseau ou URL vérifiée par ce moniteur | [INLINE_CODE_81] |