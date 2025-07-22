{
"hero": {
"title": "Configurer le Real User Monitoring (RUM)"
},
"title":"Configurer le Real User Monitoring (RUM)",
"summary": "Découvrez comment configurer le Real User Monitoring en quelques étapes.",
"url": "/support/kb/rum/configuration",
"translationKey": "https://www.uptrends.com/support/kb/rum/setup"
}

Le **Real User Monitoring** (RUM) vous permet de collecter des données de performance auprès des utilisateurs réels de votre site web. Le monitoring synthétique standard d'Uptrends s'exécute dans un environnement prévisible et à des intervalles fixes. Ce type de surveillance fonctionne bien pour la surveillance de la disponibilité et la détection des changements dans les performances des pages web. Le RUM, quant à lui, fonctionne dans des environnements moins prévisibles (par exemple, les périphériques et les ordinateurs de l'utilisateur final) et consiste essentiellement à mesurer l'expérience réelle de vos utilisateurs. Les données tirées de la surveillance RUM sont accessibles depuis votre compte Uptrends, et vous pouvez les comparer aux données produites par le monitoring synthétique.

## Mise en place du RUM d'Uptrends

La mise en place du RUM nécessite deux actions :
- l'ajout d'une définition de site RUM à votre compte ;
- l'intégration du script sur votre site web.

### Ajouter votre premier site web RUM à votre compte

1. Connectez-vous à votre compte Uptrends. Si vous n'avez pas encore de compte, ouvrez la [page d'inscription]({{< ref path="signup" lang="fr" >}}) et créez un compte d'essai gratuit.
2. Si vous n'utilisez pas encore la fonction RUM dans Uptrends, vous pouvez l'essayer gratuitement en lançant une version d'essai du RUM. Dans le menu Applications et extras, cliquez sur l'option *Essayer le Real User Monitoring*.
3. Sur la page d'*essai du RUM*, cliquez sur le bouton {{< AppElement type="button" >}}Essayer le Real User Monitoring{{< /AppElement >}}.
4. Saisissez l'URL du site web que vous souhaitez surveiller. Cliquez sur le bouton {{< AppElement type="button" >}} Créer votre premier site web en RUM{{< /AppElement >}}.
5. Votre essai RUM a maintenant commencé. Cliquez sur le bouton {{< AppElement type="button" >}}Afficher les instructions{{< /AppElement >}} pour accéder aux paramètres de votre nouveau site web RUM.

### Ajouter d'autres sites web RUM

Une fois la configuration initiale effectuée, la section *RUM* du menu contiendra une sous-section *Véritables utilisateurs*, où vous pourrez trouver les dashboards liés au RUM et gérer vos sites web RUM. Pour ajouter d'autres sites web RUM :

1. Développez la section *RUM* dans le menu.
2. Cliquez sur l'icône *\+* à côté de *Sites web en RUM*.
   ![Ajouter un site web RUM](/img/content/scr-RUM-adding_a_RUM_website.png)
3. Saisissez le *nom* du site web, et son *URL*.
4. Si votre site web est une application web monopage (AWM), cochez l'option *Utiliser le suivi des applications monopage*.
5. Si le site web utilise des fragments d'URL (par exemple `#fragment` à la fin), et que ceux-ci constituent une partie importante de vos URL, cochez l'option *Inclure le fragment d'URL*. Cela empêchera RUM de rejeter tout ce qui se trouve après le symbole #.
6. Après avoir défini toutes les options, cliquez sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} en bas à gauche.
7. Le script apparaît maintenant dans l'onglet {{< AppElement type="tab" >}}Implémentation{{< /AppElement >}}. Le chapitre suivant traitera de l'implémentation du script.

### Intégrer le script sur votre site web

Contrairement à la surveillance standard d'un site web, le RUM nécessite quelques actions de votre part. Uptrends vous fournit un petit JavaScript que vous ajoutez aux pages web que vous souhaitez mesurer avec le RUM. Le script a été conçu de manière à ne pas interférer avec d'autres scripts sur votre site web et vos utilisateurs finaux ne remarqueront rien une fois le script RUM d'Uptrends ajouté à vos pages. L'[impact de la présence du script RUM sur votre site]({{< ref path="support/kb/rum/impact-of-the-rum-script-on-your-website" lang="fr" >}}) est pratiquement nul.

1. Assurez-vous d'avoir accès au code de votre site web afin que le contenu de vos pages puisse être modifié.
2. Ouvrez le menu {{< AppElement type="menuitem" >}} RUM > Véritables utilisateurs > Sites web en RUM {{< /AppElement >}}.
3. Saisissez le site web qui vous intéresse.
4. Ouvrez l'onglet {{< AppElement type="tab" >}} Implémentation {{< /AppElement >}}.
5. Sélectionnez et copiez le [script RUM]({{< ref path="/support/kb/rum/understanding-real-user-monitoring#what-does-a-rum-script-look-like" lang="fr" >}}).
6. Placez le script à l'intérieur des balises `<head>` des pages que vous souhaitez surveiller avec le RUM. Cette méthode permet de charger le script aussi tôt que possible. Le moniteur peut ainsi capturer le plus de données pertinentes possible.

- Si votre site web inclut un en-tête de réponse Content-Security-Policy (CSP), assurez-vous que le domaine RUM d’Uptrends `https://hit.uptrendsdata.com` est [ajouté et correctement configuré](https://content-security-policy.com/) sur votre site web. Pour vérifier si le script RUM d’Uptrends fonctionne correctement, inspectez le source code de votre site pour vérifier l’existence du script RUM. Ouvrez la section *Outils de développement > onglet Réseau* de votre navigateur pour vérifier que les ressources RUM d’Uptrends s’ouvrent sans difficultés.

7. Relancez votre site web pour actualiser sa version avec le script.
8. Les données RUM seront capturées dès que des visiteurs accéderont à votre site mis à jour. Vous verrez alors les données dans le [dashboard Vue d'ensemble RUM]({{< AppUrl >}}/Report/RumOverview), et ce [en temps réel]({{< ref path="support/kb/rum/real-time-data" lang="fr" >}}).

{{< callout >}}
**Remarque :** Si vous activez l'option *Utiliser le suivi des applications monopage* pour un site web RUM existant, gardez à l'esprit que le script sera modifié après l'enregistrement et devra donc être mis à jour de votre côté également.
{{< /callout >}}

## Licence

Uptrends met le script RUM et ses composants à votre disposition sous une licence BSD (Berkeley Software Distribution). Vous pouvez trouver le texte complet à l'adresse <https://hit.uptrendsdata.com/license.txt>.

{{< callout >}}
**La confidentialité vous inquiète ?** Notre [page de confidentialité]({{< ref path="support/kb/rum/rum-and-user-privacy" lang="fr" >}}) explique comment Uptrends protège la confidentialité des utilisateurs, quelles mesures supplémentaires vous pouvez prendre pour améliorer cette confidentialité. Vous trouverez aussi une mention que vous pouvez ajouter à votre déclaration de confidentialité.
{{< /callout >}}

## Un script par site web

Gardez à l'esprit que chaque script est spécifiquement destiné à un seul site web puisqu'il contient un `sid` qui identifie de manière unique le site web RUM correspondant dans votre compte. Pour chaque vue de page enregistrée par Uptrends pour un site RUM particulier, nous vérifierons que la vue vient effectivement du domaine du site web que vous avez spécifié. Prenons un exemple :  
**Exemple** : Imaginons le site web `www.votre-domaine.com`. Par défaut nous autorisons les vues de pages provenant des domaines `www.votre-domaine.com` et `votre-domaine.com`. Si vous ajoutez ce même script sur un site web hébergé sur `test.votre-domaine.com` ou `www.votre-autre-domaine.com`, le RUM ne fonctionnera pas sur ces sites, car il n'enregistre pas les vues provenant d'autres domaines. Chaque site web a besoin de sa propre instance RUM afin de fonctionner correctement.

En substance, si vous voulez suivre les données RUM sur plus d'un site web, vous devez les traiter comme des sites web RUM distincts dans Uptrends également. Pour chaque domaine de site web que vous souhaitez surveiller, vous devrez configurer un site web RUM supplémentaire, car chaque domaine recevra un script différent.

La vérification du domaine signifie également que le RUM ne fonctionnera que dans votre environnement de production réel. Si vous avez des environnements de développement et de test distincts qui fonctionnent localement ou sous un domaine différent, le RUM n'enregistrera pas de vues pour ces sites.

{{< callout >}}
**Remarque :** Dans certaines circonstances où le même site fonctionne sur plusieurs domaines, vous le traiterez comme un domaine unique. Dans ce cas, merci de [contacter le support]({{< ref path="contact" lang="fr" >}}).
{{< /callout >}}
