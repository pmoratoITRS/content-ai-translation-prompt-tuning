{
  "hero": {
    "title": "Exclure des demandes de transaction les tests A/B"
  },
  "title": "Exclure des demandes de transaction les tests A/B",
  "summary": "Les A/B tests peuvent poser des problèmes et générer des alertes inutiles. Vous pouvez évitez les alertes non désirées en excluant vos outils d'A/B tests.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/exclure-des-demandes-de-transaction-les-tests-a-b",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les outils de test A/B divisent le trafic de votre page Web en deux flux en dirigeant un groupe d'utilisateurs vers la version A et l'autre groupe vers la version B de votre page web. Vos moniteurs de transactions pourraient générer des erreurs dues à vos tests A/B en raison des différents contenus des pages. Par exemple, si dans la version A vous avez appelé un bouton "Ajouter au panier" et dans la version B vous avez appelé le même bouton "Ajouter au panier d'achats", vous verrez des erreurs si le succès du script repose sur la recherche du texte "Ajouter au panier". Lorsque le script de surveillance des transactions repose sur la recherche d'un élément qui se trouve uniquement sur la version A de votre page, le script échouera si elle reçoit la version B. Vous pouvez éviter cette erreur en excluant l'URL de votre outil de test A/B des demandes que votre moniteur Uptrends effectue sur votre site.

[SHORTCODE_1]
**Remarque** : Bien sûr, cela vaut aussi pour le moniteur Full Page Check si vous effectuez une vérification de contenu spécifique et que le contenu change au cours d'un test A/B.
[SHORTCODE_2]

## Exclure les URLs des outils de tests A/B

Afin d'exclure des URLs des outils de tests A/B :

1.  Connectez-vous à votre compte Uptrends.
2.  Cliquez sur **Moniteurs** dans le menu déroulant **Moniteur** du menu principal.
3.  Cliquez sur le moniteur pour afficher ses détails.
4.  Cliquez sur l'onglet [SHORTCODE_5]Avancé[SHORTCODE_6].
5.  Cherchez le champ de texte étiqueté, "**Bloquer ces (parties de) URL**."
6.  Renseignez l'URL de votre outil de test dans le champ de texte. Placez chaque URL à exclure sur sa propre ligne.
7.  Cliquez sur [SHORTCODE_7]Enregistrer[SHORTCODE_8].

C'est tout ce qu'il faut faire. Une fois ces URL à exclure ajoutés, Uptrends n'enverra plus de requête sortante à votre outil de test A/B lors de la vérification de votre site. Sans la demande sortante, Uptrends ne déclenchera jamais le script de test A/B.

### Example

Dans le champ "**Bloquer ces (parties de) URL**", indiquez l'URL de votre outil de test A/B; par exemple, si vous utilisez Visual Website Optimizer pour votre test A/B, tapez visualwebsiteoptimizer.com dans le domaine. Si vous utilisez Optimizely, vous devez exclure optimizely.com.

![]([LINK_URL_1])

[SHORTCODE_3]
**Remarque** : Même si nous filtrons les demandes associées aux URLs exclues, nous l'indiquons dans le graphique en cascade par une en-tête de réponse "X-Bloqué par Uptrends: true."
[SHORTCODE_4]
