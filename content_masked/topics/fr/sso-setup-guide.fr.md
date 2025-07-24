{
  "hero": {
    "title": "Guide de configuration du Single Sign-on"
  },
  "title": "Guide de configuration du Single Sign-on",
  "url": "[URL_BASE_TOPICS]compte/parametres/sso-guide-de-configuration",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cet article vous présente les étapes de configuration du [Single Sign-on (SSO) dans Uptrends]([LINK_URL_1]). Avant d'envisager l'utilisation du Single Sign-on, merci de consulter les points suivants :

-   Vous devez avoir un fournisseur d'identité (IdP) tiers qui permet à votre organisation d'utiliser le Single Sign-on. Cet IdP sera le hub central pour l'accès de vos utilisateurs à Uptrends et à d'autres applications. Uptrends utilise le [protocole SAML 2.0]([LINK_URL_2]) pour le Single Sign-on, donc tout IdP qui prend en charge SAML 2.0 devrait fonctionner. Pensez à consulter la documentation de votre IdP qui décrit la procédure d'ajout d'une nouvelle application (ou fournisseur de service) à votre configuration.
-   Dans Uptrends, vous devez avoir un [abonnement Entreprise]([LINK_URL_3]) afin de pouvoir utiliser le SSO. Si vous avez actuellement un abonnement différent ou si vous avez un doute, [demandez à notre équipe de support]([LINK_URL_4]) de vous aider à évaluer vos options.

## Activation du Single Sign-on dans Uptrends

1.  Dans Uptrends, accédez aux paramètres de votre compte (Compte&gt; Paramètres du compte) et cochez l'option **Activer Single Sign-on (SSO)** . Si vous ne voyez pas cette option, vous devrez peut-être effectuer une mise à niveau vers Uptrends Enterprise.  
    Lorsque vous activez le SSO dans les options de votre compte, vous remarquerez une nouvelle section pour les options de connexion par défaut pour les opérateurs (voir ci-dessous) ainsi qu'une section contenant vos paramètres SSO.

2.  Dans les paramètres SSO, regardez le champ **Single Sign-on URL**. C'est une URL prédéfinie qu'il faudrait copier dans votre configuration IdP lors d'une prochaine étape.

3.  Connectez-vous à votre fournisseur d'identité en utilisant les privilèges administratifs. **Démarrer l'installation d'une nouvelle application basée sur SAML**, donnez-lui un nom approprié (par ex. *Uptrends*) et ajoutez éventuellement le logo Uptrends.

4.  Si votre IdP le demande, choisissez la **configuration initiée par IdP**, plutôt qu'une configuration initiée par SP. En outre, si vous devez spécifier la plate-forme web du fournisseur de services, choisissez Microsoft IIS.

5.  Votre IdP demandera l'**URL du Single Sign-on du fournisseur de services**, ou point de terminaison SAML. Merci d'utiliser l'URL de connexion unique mentionnée à l'étape 2.

6.  Certains IdP demandent un **URI d'audience ou ID d'entité** : merci d'utiliser la même URL que celle de l'étape précédente. En fait, certains IdP spécifient leur propre URI d'audience ou ID d'entité. Dans ce cas, copiez cette valeur et collez-la dans le champ Audience URI/Entity ID dans vos paramètres SSO Uptrends.

7.  Votre IdP vous permet probablement de spécifier quel champ doit être utilisé pour que le fournisseur de services puisse identifier l'utilisateur qui tente de se connecter. Cette option est souvent appelée **Name ID Format**. Uptrends utilise l'adresse e-mail de l'utilisateur, veuillez donc choisir *Email* ou *EmailAddress* pour cette valeur.

8.  Terminez la procédure d'installation dans votre IdP. À la fin de la procédure, votre IdP vous donne les données de configuration dont Uptrends a besoin pour finaliser la configuration SSO. En fonction de votre IdP, soit il vous donnera l' **URL Single Sign-on de l'IdP** et les **données de certificat** (qui est une clé publique X.509), ou il vous permettra de télécharger un fichier XML qui contient ces mêmes informations.

    Si votre IdP vous fournit un fichier de métadonnées XML, alors dans ce cas vous pouvez ouvrir le fichier sous la forme d'un fichier texte standard et rechercher les informations appropriées. Si vous n'êtes pas sûr, demandez à notre équipe de support de vous aider. 

    Cherchez un nœud XML qui ressemble à :

    [INLINE_CODE_1]

    L'URL de l'attribut **Location** est la valeur dont vous avez besoin à l'étape suivante.

    Cherchez également le nœud XML de nom :

    [INLINE_CODE_2]

    Les données codées en Base64 à l'intérieur de ce nœud sont les données de certificat dont vous aurez bientôt besoin.

9.  De retour dans vos paramètres de compte Uptrends, copiez l'URL du Single Sign-on du fournisseur d'identité dans le **Champ URL de connexion**. 

10.  L'étape suivante consiste à stocker les données de certificat générées par votre IdP dans votre [coffre-fort Uptrends]([LINK_URL_5]).   
    Cliquez sur le lien *Ajouter un item* à côté du champ Certificat. Un nouvel onglet de navigateur s'ouvre pour vous permettre de créer un nouvel élément dans le coffre-fort afin d'y stocker vos données de clé publique. Donnez-lui un nom reconnaissable (par exemple *Certificat SSO*), et assurez-vous qu'il a le type **Certificat clé publique**.   
    Dans le champ **Clé publique** copiez les données codées en Base64 que vous avez localisées plus tôt.  Enregistrez le nouvel élément de coffre-fort. 

11. Revenez aux paramètres du compte dans l'onglet précédent du navigateur. Cliquez sur *Actualiser* pour recharger la liste des éléments disponibles, qui devraient désormais contenir l'élément de coffre-fort que vous venez de créer. Enfin, sélectionnez le certificat SSO. Dans les cas où vous avez besoin de changer de certificat (par exemple, si un certificat précédemment téléchargé doit expirer et que vous avez besoin d'une transition transparente vers le suivant), vous pouvez choisir d'utiliser tous les éléments existant dans une section de coffre-fort. Pour ce faire, sélectionnez l'option « Analyser toute cette section pour trouver le certificat approprié » dans le menu déroulant Certificat. Cliquez sur [SHORTCODE_1]Enregistrer[SHORTCODE_2] pour terminer votre configuration SSO.

12.  Votre Single Sign-on est maintenant prêt. 

## Gérer les options de connexion 

Une fois le Single Sign-on configuré avec succès dans votre compte, vous pouvez décider d'activer ou non les connexions SSO pour tous les opérateurs. 

Dans les paramètres du compte, vous pouvez définir le comportement par défaut pour tous les opérateurs. Vous pouvez activer ou désactiver les connexions classiques - basées sur le nom d'utilisateur/mot de passe - et les connexions basées sur le Single Sign-on. Évidemment, vous ne devriez pas désactiver les deux, car cela bloque tous les opérateurs. 

Le scénario typique consiste à maintenir les connexions basées sur le nom d'utilisateur/mot de passe, tester les connexions SSO avec quelques utilisateurs seulement et enfin désactiver les connexions utilisateur/mot de passe pour tous les opérateurs afin d'imposer le Single Sign-on à tout le monde. 

En plus de ce comportement par défaut, vous pouvez créer des exceptions pour des opérateurs individuels. Lorsque vous passez en revue les paramètres d'un opérateur, vous remarquerez que les paramètres de connexion nom d'utilisateur/mot de passe et les paramètres de connexion SSO sont initialement définis comme "Compte par défaut". Cela signifie que le comportement par défaut que vous avez spécifié dans les paramètres du compte s'appliquera à cet opérateur. 

Pour chaque opérateur, vous pouvez faire un réglage différent pour autoriser ou interdire ces options de connexion. Par exemple, ceci est utile si vous demandez à tous vos opérateurs habituels d'utiliser le Single Sign-on à l'exception d'un ou de plusieurs opérateurs spéciaux que vous avez créés pour autoriser des personnes extérieures à votre entreprise à accéder à certains rapports. Ils n'ont peut-être pas accès à votre fournisseur d'identité, mais vous pouvez toujours leur permettre d'accéder à Uptrends en utilisant une connexion normale avec nom d'utilisateur/mot de passe.
