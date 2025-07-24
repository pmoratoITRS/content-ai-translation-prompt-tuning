{
  "hero": {
    "title": "Protection des données dans les emplacements privés"
  },
  "title": "Protection des données dans les emplacements privés",
  "summary": "Comment sont protégées les données dans les emplacements privés ?",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/points-de-controle/emplacements-prives/protection-donnees-emplacements-prives",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cet article de notre base de connaissances vous explique comment protéger les données situées dans vos emplacements privés. L'une des mesures de protection liées aux emplacements privés d'Uptrends consiste à empêcher le chargement des captures d'écran sur le cloud. Vous pouvez aussi désactiver le contenu des pages, et masquer les en-têtes de requête et de réponse ainsi que les adresses IP résolues dans les résultats des vérifications.

## Modification du fichier Docker Compose

Si vous ne l'avez pas déjà fait, commencez par installer votre checkpoint en suivant les étapes présentées dans l'article [Installer un checkpoint Docker]([LINK_URL_1]).

1. Effectuez une copie de sauvegarde de l'extraction du fichier Docker Compose. Tout changement apporté au fichier Compose est effectué à vos propres risques. En cas de doute, contactez le [support]([LINK_URL_2]).
2. Ouvrez le fichier docker-compose.yml et retirez la balise de commentaire `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]- AllowScreenshotsInResults=false[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]- AllowScreenshotsInResults=false[INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10]- AllowHttpHeadersInResults=false[INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13]- AllowResolvedIpAddressesInResults=false[INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16]- AllowResolvedIpAddressesInResults=false` dans la liste des variables d'environnement du checkpoint. Enregistrez le fichier et redémarrez manuellement le conteneur Docker, comme décrit à la dernière étape des instructions de modification ci-dessus, afin de refléter les changements apportés aux paramètres de protection des données dans l'application d'Uptrends.

Si cette valeur est définie comme "false", l'exécution des moniteurs DNS sera bloquée sur les serveurs de checkpoints de votre emplacement privé.

[SHORTCODE_3] **Remarque** : Tous les paramètres ne sont pas disponibles pour tous les moniteurs. Par exemple, pour les moniteurs HTTP(S) de base, seules les captures d'écran des erreurs fonctionnent, et le paramétrage des adresses IP résolues n'est pas disponible pour ce type de moniteur.
[SHORTCODE_4]

## État des paramètres de protection des données

Dans l'application Uptrends, l'onglet [Santé du point de contrôle]([LINK_URL_9]) montre l'état des paramètres de protection des données. La présence d'une croix rouge signifie que les données ne s'affichent pas, et donc que la protection des données est activée. Notez que l'affichage est en lecture seule, et que les paramètres ne peuvent être ajustés que dans le fichier Docker.

![Paramètres de protection des données dans l'onglet Santé du point de contrôle]([LINK_URL_10])