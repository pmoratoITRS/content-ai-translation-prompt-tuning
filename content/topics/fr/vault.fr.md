{
"hero": {
"title": "Coffre-fort"
},
"title": "Coffre-fort",
"url": "/support/kb/compte/coffre-fort",
"translationKey": "https://www.uptrends.com/support/kb/account/vault"
}

Le **coffre-fort** d'Uptrends est un espace centralisé qui vous aide à gérer les noms d'utilisateur, les mots de passe, les certificats et d'autres informations sensibles dont vous avez besoin pour configurer votre moniteur.

Cette fonctionnalité vous permet de stocker vos identifiants en tant qu'**éléments de coffre-fort**, pour ensuite les utiliser avec plusieurs moniteurs. Par exemple, si vous avez besoin d'utiliser un `nom d'utilisateur` et un `mot de passe` pour les moniteurs d'API multi-étapes et les moniteurs de transactions, vous pouvez les enregistrer comme des éléments de coffre-fort et les appliquer aux deux moniteurs. Si des changements sont apportés à vos éléments de coffre-fort, le **coffre-fort** applique automatiquement ces changements à tous les moniteurs qui les utilisent. Ainsi, vous pouvez facilement organiser et suivre toutes vos données depuis un même endroit.

Le **coffre-fort** est fourni avec tous les forfaits, sans coût supplémentaire.

{{< callout >}}
**Rappel utile :** dans un objectif de sécurité et de respect des bonnes pratiques, le coffre-fort d'Uptrends doit vous servir uniquement pour gérer toutes vos informations sensibles dans Uptrends. Il est déconseillé de l'utiliser comme emplacement principal pour stocker des secrets ou gérer vos mots de passe.
{{< /callout >}}

## Fonctionnalités du coffre-fort

Le **coffre-fort** propose plusieurs fonctionnalités pour stocker vos informations de façon sécurisée. Vous pouvez notamment définir vos **éléments de coffre-fort**, les regrouper dans une **section de coffre-fort** et contrôler les droits d'accès au moyen d'**autorisations**.

Pour voir et utiliser facilement les fonctionnalités du **coffre-fort**, passez par le menu {{< AppElement type="menuitem" >}} Configuration de compte > Coffre-fort {{< /AppElement >}}.

## Sections du coffre-fort

Tous les éléments stockés dans le coffre-fort sont organisés en **sections de coffre-fort**. Ces sections sont comme le conteneur ou le parent de vos éléments de coffre-fort. Par défaut, tous les comptes Uptrends sont équipés d'une section de coffre-fort, et chaque élément de coffre-fort que vous enregistrez doit appartenir à une seule section.

Comme les éléments stockés dans la section par défaut sont réservés aux membres du groupe Administrateurs, tous les administrateurs peuvent afficher et modifier chaque élément du coffre-fort.

Pour créer une **section de coffre-fort** :

1. Dans le coin supérieur droit, cliquez sur le bouton {{< AppElement type="buttonCta" >}} Ajouter une section de coffre-fort {{< /AppElement >}}.
2. Dans les **détails de la section du coffre-fort**, précisez le **nom** de la section de coffre-fort. Il est recommandé de donner un nom qui définit clairement le but et le contenu des éléments stockés.
3. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.

Une fois la section de coffre-fort créée, vous pouvez ajouter des [éléments de coffre-fort]({{< ref path="/support/kb/account/vault#vault-item-types" lang="fr" >}}) et accorder des [autorisations]({{< ref path="/support/kb/account/vault#vault-permissions" lang="fr" >}}).

Pour supprimer une **section de coffre-fort** :

1. Cliquez sur le bouton {{< AppElement type="deletebutton" >}} Supprimer cette section de coffre-fort {{< /AppElement >}}.
2. Dans la **fenêtre de confirmation** qui s'affiche, cliquez sur {{< AppElement type="deletebutton" >}} Supprimer {{< /AppElement >}} pour confirmer le changement.

## Types d'éléments de coffre-fort

Une fois que vous avez créé votre section de coffre-fort, vous pouvez catégoriser et ajouter vos éléments de coffre-fort.

Pour ajouter un **élément de coffre-fort** :

1. Dans le coin supérieur droit, cliquez sur le bouton {{< AppElement type="buttonCta" >}} Ajouter un élément de coffre-fort {{< /AppElement >}}.
2. Dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}, remplissez la section **Détails** :

- Nom ; précisez un nom unique pour l'élément de coffre-fort.
- Section : choisissez la section de coffre-fort qui vous intéresse dans la liste déroulante.
- Description : décrivez ou annotez l'élément de coffre-fort.
- Type : faites votre choix parmi les différents types d'élément de coffre-fort dans la liste déroulante. Le **coffre-fort** permet de stocker différents types de données. Les types d'élément de coffre-fort disponibles sont les suivants :

### Références d'identification {id="credential-set"}

Ce type d'élément de coffre-fort correspond à la combinaison d'un nom d'utilisateur et d'un mot de passe. Vous pouvez l'utiliser avec les types de moniteurs qui attendent un nom d'utilisateur et un mot de passe pour l'authentification, notamment avec l'authentification de base, NTLM, Digest pour les moniteurs d'API multi-étapes, comme identifiants de connexion pour les moniteurs SMTP, POP3, IMAP, SQL, FTP et SFTP, et comme noms d'utilisateur et mots de passe dans les scripts de transaction.

### Archive de certificat

Ce type d'élément de coffre-fort peut stocker un certificat de sécurité, sous la forme d'une archive de certificat PKCS \#12 (habituellement un fichier .p12 ou .pfx) qui contient la clé privée d'un certificat ainsi que sa clé publique. Une fois téléchargé dans le coffre-fort, vous pouvez utiliser le certificat en tant que certificat client dans les moniteurs API multi-étapes.

Si vous avez un fichier d'archive de certificat (un fichier .p12 ou .pfx) contenant vos clés privées et publiques, sélectionnez ce fichier dans le champ **Importer une nouvelle archive**. Le fichier d'archive est généralement chiffré. Dans ce cas, spécifiez le mot de passe correspondant dans le champ **Mot de passe d'archive**.

### Clé publique de certificat

Ce type d'élément de coffre-fort sera utilisé pour la configuration de l'authentification unique (SSO) avec Uptrends. Il stockera la clé publique générée par votre fournisseur d'identité (IdP). Lorsque votre IdP envoie les demandes de connexion SAML à Uptrends, il signe ces demandes à l'aide d'un certificat. Uptrends utilise votre clé publique pour vérifier que la demande entrante provient véritablement de votre IdP.

Si vous voulez ajouter une clé publique au coffre-fort, vous avez probablement déjà un fichier de clé publique (généralement un fichier .pem ou .cer). Copiez le contenu du fichier dans le champ **Clé publique**. Il devrait s'agir d'un contenu codé Base64 qui peut être lu en tant que certificat X.509.

### Fichier {id="file"}

Ce type d'élément peut être utilisé pour stocker des fichiers, qui peuvent ensuite être téléchargés par le biais d'un flux du [moniteur de transaction en libre-service]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}). Pour plus d'informations sur la configuration des téléchargements de fichiers dans vos transactions, consultez notre [documentation sur les interactions de page]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#file-upload" lang="fr" >}}) dans les moniteurs de transactions. Tout type de fichier ou extension est pris en charge, et nous définissons automatiquement le type MIME correct (une manière universelle de spécifier la nature et le format du fichier sur Internet), le cas échéant. La taille maximale du fichier est 2 Mo.

Les fichiers peuvent être téléchargés en cliquant sur le bouton **Choisir le fichier** qui apparaît lorsque le type d'élément du coffre-fort de fichiers est sélectionné. Les propriétés Name et Type MIME seront automatiquement renseignées. Nous vous recommandons de donner à l'élément de coffre-fort un nom parlant, afin que vous puissiez facilement vous y référer lors de la configuration du [téléchargement de fichiers]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#file-upload" lang="fr" >}}) dans votre transaction ou dans le [moniteur API multi-étapes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}).

### Configuration du mot de passe à usage unique ou du mot de passe à usage unique basé sur le temps {id="one-time-password"}

Cet élément de coffre-fort stocke une valeur *secrète* qui est utilisée pour générer un mot de passe à usage unique. Il vous offre une autre façon de [configurer une double authentification basée sur un mot de passe à usage unique]({{< ref path="support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="fr" >}}) pour surveiller une [application web]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="fr" >}}) dont les utilisateurs doivent vérifier leur connexion au moyen d'un code.

Les champs suivants peuvent être configurés selon vos préférences :

- Méthode de codage du secret : ce champ désigne la méthode de codage utilisée pour les valeurs secrètes. Choisissez *Hex* si la valeur secrète est encodée en hexadécimal (soit avec des caractères allant de 0 à 9 et de A à F). Autrement, choisissez le format par défaut d'Uptrends, *Base32*, si votre valeur secrète est encodée en Base32 (soit avec des caractères allant de A à Z et de 2 à 7).
- Chiffres : la longueur du code de mot de passe à usage unique généré. Le code comprend *6, 7 ou 8* chiffres.
- Délai d'expiration (s) : la durée de validité du mot de passe à usage unique. Le délai est compris entre *1 et 120* secondes.
- Algorithme : le type d'algorithme de hachage sécurisé (SHA) utilisé. Les algorithmes peuvent être de type *SHA512* (64 octets), *SHA256* (32 octets) ou *SHA1* (20 octets).

## Autorisations liées au coffre-fort

### Restreindre l'accès au coffre-fort à des personnes spécifiques
Dans certains cas, il est utile d'avoir un contrôle plus fin : les différents opérateurs ou groupes peuvent avoir des responsabilités différentes, et c'est généralement une bonne idée de limiter autant que possible l'accès aux données sensibles.

Les règles d'accès au coffre-fort peuvent être définies au niveau de la section : vous pouvez modifier les autorisations initialement définies pour la section par défaut, et vous pouvez créer des sections supplémentaires et accorder l'accès à des groupes d'opérateurs spécifiques ainsi qu'à des opérateurs individuels.

Deux niveaux d'accès sont disponibles pour les sections du coffre-fort :

- **Contrôle complet** : les opérateurs ou groupes qui ont ce niveau d'accès pour une section de coffre-fort peuvent ajouter ou supprimer des éléments dans cette section, mettre à jour les éléments stockés dans cette section et gérer les droits d'accès pour cette section.
- **Voir seulement** : ce niveau d'accès est nécessaire pour voir les éléments du coffre-fort stockés dans une section et pour pouvoir utiliser un élément de coffre-fort (comme un certificat ou des références d'identification dans les paramètres du moniteur, ou bien comme une clé publique de certificat dans les paramètres de Single Sign-on). Important : dès qu'un élément de coffre-fort est configuré en tant qu'élément d'un moniteur, les droits d'édition pour ce moniteur sont limités aux opérateurs disposant des droits d'affichage pour la section de coffre-fort correspondante. Les droits d'édition seront restreints afin d'empêcher l'accès non autorisé au contenu de l'élément de coffre-fort.

## Gestion des éléments de coffre-fort avec l'API Uptrends

L'un des avantages de la configuration d'un élément de coffre-fort est que toute modification de cet élément sera automatiquement appliquée à tous les moniteurs qui l'utilisent. C'est utile si vous souhaitez appliquer une politique d'expiration de mot de passe pour les informations d'identification utilisées dans vos moniteurs. Supposons que ces informations d'identification expirent tous les x jours dans votre environnement réseau. Il suffit alors de changer le contenu de l'élément du coffre-fort qui détient ces informations d'identification dans Uptrends : les moniteurs correspondants commenceront automatiquement à utiliser les informations d'identification mises à jour.

Vous pouvez aller plus loin en automatisant la mise à jour de l'élément de coffre-fort. Vous pouvez appeler l'[API Coffre-fort]({{< ref path="/support/kb/api/vault-api" lang="fr" >}}) d'Uptrends à partir de votre propre backend pour mettre à jour les informations d'identification dans un élément existant du coffre-fort. Pour en savoir plus, lisez la [documentation de l'API]({{< ref path="support/kb/api/v4" lang="fr" >}}).
