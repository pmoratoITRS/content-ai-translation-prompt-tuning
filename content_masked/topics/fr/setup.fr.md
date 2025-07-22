{
  "hero": {
    "title": "Configurer le Real User Monitoring (RUM)"
  },
  "title": "Configurer le Real User Monitoring (RUM)",
  "summary": "Découvrez comment configurer le Real User Monitoring en quelques étapes.",
  "url": "[URL_BASE_TOPICS]rum/configuration",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le **Real User Monitoring** (RUM) vous permet de collecter des données de performance auprès des utilisateurs réels de votre site web. Le monitoring synthétique standard d'Uptrends s'exécute dans un environnement prévisible et à des intervalles fixes. Ce type de surveillance fonctionne bien pour la surveillance de la disponibilité et la détection des changements dans les performances des pages web. Le RUM, quant à lui, fonctionne dans des environnements moins prévisibles (par exemple, les périphériques et les ordinateurs de l'utilisateur final) et consiste essentiellement à mesurer l'expérience réelle de vos utilisateurs. Les données tirées de la surveillance RUM sont accessibles depuis votre compte Uptrends, et vous pouvez les comparer aux données produites par le monitoring synthétique.

## Mise en place du RUM d'Uptrends

La mise en place du RUM nécessite deux actions :
- l'ajout d'une définition de site RUM à votre compte ;
- l'intégration du script sur votre site web.

### Ajouter votre premier site web RUM à votre compte

1. Connectez-vous à votre compte Uptrends. Si vous n'avez pas encore de compte, ouvrez la [page d'inscription]([LINK_URL_1]) et créez un compte d'essai gratuit.
2. Si vous n'utilisez pas encore la fonction RUM dans Uptrends, vous pouvez l'essayer gratuitement en lançant une version d'essai du RUM. Dans le menu Applications et extras, cliquez sur l'option *Essayer le Real User Monitoring*.
3. Sur la page d'*essai du RUM*, cliquez sur le bouton [SHORTCODE_7]Essayer le Real User Monitoring[SHORTCODE_8].
4. Saisissez l'URL du site web que vous souhaitez surveiller. Cliquez sur le bouton [SHORTCODE_9] Créer votre premier site web en RUM[SHORTCODE_10].
5. Votre essai RUM a maintenant commencé. Cliquez sur le bouton [SHORTCODE_11]Afficher les instructions[SHORTCODE_12] pour accéder aux paramètres de votre nouveau site web RUM.

### Ajouter d'autres sites web RUM

Une fois la configuration initiale effectuée, la section *RUM* du menu contiendra une sous-section *Véritables utilisateurs*, où vous pourrez trouver les dashboards liés au RUM et gérer vos sites web RUM. Pour ajouter d'autres sites web RUM :

1. Développez la section *RUM* dans le menu.
2. Cliquez sur l'icône *\+* à côté de *Sites web en RUM*.
   ![Ajouter un site web RUM]([LINK_URL_2])
3. Saisissez le *nom* du site web, et son *URL*.
4. Si votre site web est une application web monopage (AWM), cochez l'option *Utiliser le suivi des applications monopage*.
5. Si le site web utilise des fragments d'URL (par exemple [INLINE_CODE_1] à la fin), et que ceux-ci constituent une partie importante de vos URL, cochez l'option *Inclure le fragment d'URL*. Cela empêchera RUM de rejeter tout ce qui se trouve après le symbole #.
6. Après avoir défini toutes les options, cliquez sur le bouton [SHORTCODE_13]Enregistrer[SHORTCODE_14] en bas à gauche.
7. Le script apparaît maintenant dans l'onglet [SHORTCODE_15]Implémentation[SHORTCODE_16]. Le chapitre suivant traitera de l'implémentation du script.

### Intégrer le script sur votre site web

Contrairement à la surveillance standard d'un site web, le RUM nécessite quelques actions de votre part. Uptrends vous fournit un petit JavaScript que vous ajoutez aux pages web que vous souhaitez mesurer avec le RUM. Le script a été conçu de manière à ne pas interférer avec d'autres scripts sur votre site web et vos utilisateurs finaux ne remarqueront rien une fois le script RUM d'Uptrends ajouté à vos pages. L'[impact de la présence du script RUM sur votre site]([LINK_URL_3]) est pratiquement nul.

1. Assurez-vous d'avoir accès au code de votre site web afin que le contenu de vos pages puisse être modifié.
2. Ouvrez le menu [SHORTCODE_17] RUM > Véritables utilisateurs > Sites web en RUM [SHORTCODE_18].
3. Saisissez le site web qui vous intéresse.
4. Ouvrez l'onglet [SHORTCODE_19] Implémentation [SHORTCODE_20].
5. Sélectionnez et copiez le [script RUM]([LINK_URL_4]).
6. Placez le script à l'intérieur des balises [INLINE_CODE_2] des pages que vous souhaitez surveiller avec le RUM. Cette méthode permet de charger le script aussi tôt que possible. Le moniteur peut ainsi capturer le plus de données pertinentes possible.

- Si votre site web inclut un en-tête de réponse Content-Security-Policy (CSP), assurez-vous que le domaine RUM d’Uptrends [INLINE_CODE_3] est [ajouté et correctement configuré]([LINK_URL_5]) sur votre site web. Pour vérifier si le script RUM d’Uptrends fonctionne correctement, inspectez le source code de votre site pour vérifier l’existence du script RUM. Ouvrez la section *Outils de développement > onglet Réseau* de votre navigateur pour vérifier que les ressources RUM d’Uptrends s’ouvrent sans difficultés.

7. Relancez votre site web pour actualiser sa version avec le script.
8. Les données RUM seront capturées dès que des visiteurs accéderont à votre site mis à jour. Vous verrez alors les données dans le [dashboard Vue d'ensemble RUM]([LINK_URL_6]), et ce [en temps réel]([LINK_URL_7]).

[SHORTCODE_1]
**Remarque :** Si vous activez l'option *Utiliser le suivi des applications monopage* pour un site web RUM existant, gardez à l'esprit que le script sera modifié après l'enregistrement et devra donc être mis à jour de votre côté également.
[SHORTCODE_2]

## Licence

Uptrends met le script RUM et ses composants à votre disposition sous une licence BSD (Berkeley Software Distribution). Vous pouvez trouver le texte complet à l'adresse [HTML_TAG_1].

[SHORTCODE_3]
**La confidentialité vous inquiète ?** Notre [page de confidentialité]([LINK_URL_8]) explique comment Uptrends protège la confidentialité des utilisateurs, quelles mesures supplémentaires vous pouvez prendre pour améliorer cette confidentialité. Vous trouverez aussi une mention que vous pouvez ajouter à votre déclaration de confidentialité.
[SHORTCODE_4]

## Un script par site web

Gardez à l'esprit que chaque script est spécifiquement destiné à un seul site web puisqu'il contient un [INLINE_CODE_4] qui identifie de manière unique le site web RUM correspondant dans votre compte. Pour chaque vue de page enregistrée par Uptrends pour un site RUM particulier, nous vérifierons que la vue vient effectivement du domaine du site web que vous avez spécifié. Prenons un exemple :  
**Exemple** : Imaginons le site web [INLINE_CODE_5]. Par défaut nous autorisons les vues de pages provenant des domaines [INLINE_CODE_6] et [INLINE_CODE_7]. Si vous ajoutez ce même script sur un site web hébergé sur [INLINE_CODE_8] ou [INLINE_CODE_9], le RUM ne fonctionnera pas sur ces sites, car il n'enregistre pas les vues provenant d'autres domaines. Chaque site web a besoin de sa propre instance RUM afin de fonctionner correctement.

En substance, si vous voulez suivre les données RUM sur plus d'un site web, vous devez les traiter comme des sites web RUM distincts dans Uptrends également. Pour chaque domaine de site web que vous souhaitez surveiller, vous devrez configurer un site web RUM supplémentaire, car chaque domaine recevra un script différent.

La vérification du domaine signifie également que le RUM ne fonctionnera que dans votre environnement de production réel. Si vous avez des environnements de développement et de test distincts qui fonctionnent localement ou sous un domaine différent, le RUM n'enregistrera pas de vues pour ces sites.

[SHORTCODE_5]
**Remarque :** Dans certaines circonstances où le même site fonctionne sur plusieurs domaines, vous le traiterez comme un domaine unique. Dans ce cas, merci de [contacter le support]([LINK_URL_9]).
[SHORTCODE_6]
