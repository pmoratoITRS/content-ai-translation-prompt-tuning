{
  "hero": {
    "title": "Vue d'ensemble du Single Sign-on"
  },
  "title": "Vue d'ensemble du Single Sign-on",
  "summary": "Découvrez comment Uptrends et votre fournisseur SSO travaillent ensemble pour améliorer la gestion des utilisateurs et offrir aux utilisateurs des connexions plus rapides et sans problèmes.",
  "url": "[URL_BASE_TOPICS]compte/parametres/vue-densemble-du-single-sign-on",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lorsqu'un compte Uptrends est créé pour la première fois, l'administrateur du compte initial crée un identifiant pour lui-même avec son adresse e-mail et un mot de passe. Des opérateurs supplémentaires peuvent ensuite être ajoutés au fil du temps pour permettre à plus de personnes d'accéder au compte, et chaque opérateur se connecte en utilisant sa propre adresse e-mail et son propre mot de passe.

Cela fonctionne bien, mais au fur et à mesure que votre organisation évolue et que vos équipes commencent à utiliser davantage d'outils et de services en ligne, il est judicieux de prendre en compte quelques points :

- Les utilisateurs doivent se souvenir de leur mot de passe Uptrends, ainsi que des mots de passe de tous les autres outils en ligne qu'ils utilisent.
- Ils doivent effectuer une connexion manuelle chaque fois qu'ils veulent accéder à Uptrends.
- Du point de vue de la gestion des utilisateurs, il peut être de plus en plus difficile de contrôler quels utilisateurs ont accès à quels outils.

## Contrôle d'accès plus simple et plus sûr grâce au Single Sign-on

Pour rendre les choses plus faciles pour les utilisateurs finaux et les administrateurs, pour toutes les applications en ligne utilisées par vos équipes, vous pouvez utiliser une solution qui se situe à cheval entre vos utilisateurs et ces applications en ligne. De nombreux produits tiers proposent une solution SSO (Single Sign-On). Nous avons travaillé avec [Azure Active Directory]([LINK_URL_1]), Services de fédération Active Directory (ADFS), [Okta]([LINK_URL_2]), [OneLogin]([LINK_URL_3]), [SecureAuth]([LINK_URL_4]) et [Duo Access Gateway]([LINK_URL_5]), mais il y en a beaucoup d'autres. Tout produit pouvant supporter le [protocole SAML 2.0]([LINK_URL_6]) pour Single Sign-on devrait fonctionner.

## Le fonctionnement du Single Sign-on chez Uptrends

Comme déjà indiqué, vous aurez besoin d'un produit tiers faisant office de hub centralisé qui permet aux utilisateurs un accès aux applications, et à vos administrateurs un contrôle sur quels utilisateurs ont accès à quelles applications, Uptrends étant l'une d'entre elles. Dans cet article, nous appellerons ce produit **Fournisseur d'Identité (IdP)**, car sa fonction est de prouver l'identité de chaque utilisateur lors de la connexion à vos applications. Dans cette configuration, Uptrends est l'une de ces applications et joue le rôle de **Fournisseur de service (SP)**.

Une fois que vous disposez d'une configuration IdP opérationnelle, les fonctionnalités de connexion de l'IdP permettront à vos utilisateurs d'être authentifiés dans leur navigateur, sur leurs appareils mobiles, etc., souvent en fonction de leurs informations d'identification réseau. Ces fonctionnalités peuvent également inclure l'authentification à deux facteurs, des stratégies strictes de mot de passe, etc. Le principal avantage pour les utilisateurs finaux est qu'ils n'ont plus besoin de se souvenir de mots de passe différents pour les applications différentes, et qu'ils peuvent accéder à Uptrends et à d'autres applications avec un seul clic. La plupart des IdP offrent une galerie ou hub d'applications, affichant tous les outils et services disponibles pour l'utilisateur. Les outils sont immédiatement reconnaissables et accessibles, sans avoir à mettre les URL dans les favoris, ni à se souvenir des bons mots de passe ou à passer par les tracas habituels autour de la sécurité et de l'organisation.

Les administrateurs bénéficient d'une configuration SSO car ils peuvent contrôler les utilisateurs qui ont accès à Uptrends et révoquer facilement l'accès lorsque quelqu'un quitte l'entreprise ou change d'équipe.

## Vue d'ensemble de la configuration du Single Sign-on

Pour obtenir une configuration SSO fonctionnelle dans Uptrends, les étapes de base suivantes sont nécessaires :

- **Activez l'option SSO** dans vos paramètres de compte Uptrends. Notez que le Single Sign-on est disponible uniquement pour les comptes Entreprise.
- **Définissez une nouvelle application chez votre fournisseur d'identité**, en utilisant les données de configuration SAML fournies par Uptrends. Essentiellement, vous n'avez besoin de copier qu'une seule URL : il s'agit de l'URL Single Sign-on (du côté Uptrends) unique pour la configuration SSO de votre organisation ; votre IdP a besoin de cette URL pour savoir où envoyer vos utilisateurs quand ils se connectent
- Une fois définie, la nouvelle application Uptrends de votre IdP génère également des données de configuration SAML. Ces données contiennent deux informations : **l'URL de connexion de votre IdP** (pour qu'Uptrends sache d'où viennent vos utilisateurs) et **le certificat généré par votre IdP** qui permet de signer numériquement les requêtes SAML qu'il envoie à Uptrends. Cela permet à Uptrends d'être absolument certain que les connexions entrantes proviennent véritablement de votre fournisseur d'identité et non de quelqu'un d'autre. Ceci est cruciale pour la sécurité du Single Sign-on. Vous stockerez la clé publique pour SSO dans votre [coffre-fort d'Uptrends]([LINK_URL_7]).
- Assurez-vous que **vos utilisateurs sont définis des deux côtés** : votre IdP s'exécute dans votre propre environnement, donc il connaît déjà vos utilisateurs. Dans Uptrends, chaque utilisateur a besoin de son propre opérateur (s'il n'existe pas déjà). Lorsqu'un utilisateur est connecté grâce à l'IdP, nous examinons l'adresse e-mail. Il doit donc correspondre des deux côtés.
- Il n'est pas nécessaire de déployer SSO pour tous les utilisateurs à la fois : vous pouvez commencer par un seul, tandis que les utilisateurs restants peuvent continuer d'accéder à Uptrends en utilisant les connexions classiques jusqu'à ce que vous soyez prêt à les passer en SSO.

Pour des instructions d'installation détaillées, lisez le [Guide de configuration du Single Sign-on]([LINK_URL_8]).

## Comment les utilisateurs SSO peuvent-ils se connecter ? [ANCHOR_1]

Une fois la configuration SSO terminée, vous allez vouloir informer vos utilisateurs sur comment se connecter à Uptrends. Où pointer leur navigateur pour accéder à leur compte Uptrends ? Il existe deux approches :

1. SSO initiée par IdP. Cette méthode signifie que vos utilisateurs disposent d'un emplacement centralisé qu'ils peuvent visiter (souvent une page web hébergée par votre logiciel IdP sous la forme d'une galerie d'applications) afin de se connecter à Uptrends ou à d'autres services compatibles SSO. La galerie d'applications comprend un lien spécial vers Uptrends qui lancera la procédure de connexion SSO. Cette méthode se dit *initiée par IdP* car la séquence de connexion est démarrée du côté du fournisseur d'identité.
2. SSO initiée par SP. Cette méthode suppose que vous ne disposez pas d'une galerie d'applications centralisé ni d'un portail, mais que vos utilisateurs doivent eux-mêmes accéder aux services compatibles SSO. Ils devront spécifier le nom de votre organisation à l'écran de connexion Uptrends SSO afin de lancer la séquence de connexion vers votre fournisseur d'identité. Sinon, ils peuvent créer un signet vers le sous-domaine [INLINE_CODE_1]. Merci de [contacter notre service d'assistance]([LINK_URL_9]) si vous souhaitez utiliser la méthode de connexion initiée par SP. Ils s'assureront que votre sous-domaine sera créé.
