{
  "hero": {
    "title": "Contournement DNS"
  },
  "title": "Contournement DNS",
  "summary": "Sachez comment et pourquoi configurer un contournement DNS pour un moniteur de transaction ou un moniteur Full Page Check. Ce contournement peut être ajouté au type de navigateur 'Chrome avec des métriques supplémentaires'. Il permet de s'assurer que la résolution d'une page web se fait dans un nom de domaine ou une adresse IP spécifique.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/contournement-dns",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le contournement DNS permet de s'assurer que la résolution de la page web se fait dans un nom de domaine ou une adresse IP spécifique.

Par exemple, vous pourriez en avoir besoin pour surveiller et vérifier l’emplacement spécifique d’un site web, si le site fait partie d’un réseau de diffusion de contenu (CDN) ou d'une solution à répartition de charge. Le contournement DNS vous sera aussi utile dans les [scénarios]([LINK_URL_1]) suivants.

## Moniteurs compatibles avec le contournement DNS

Le contournement DNS d'Uptrends s'exécute dans les moniteurs [Full Page Check]([LINK_URL_2]) et les moniteurs de [transactions]([LINK_URL_3]). Il est disponible uniquement pour le type de navigateur _Chrome avec des métriques supplémentaires_.

Pour d'autres types de navigateurs, tels que HTTPS, vous pouvez utiliser des en-têtes d’hôte. Pour en savoir plus sur cette fonction, lisez l'article [Surveillance de sites web autres que le serveur de production]([LINK_URL_4]) dans notre base de connaissances.

## Pourquoi utiliser un contournement DNS ?
Quand Uptrends charge une URL dans le navigateur pour un moniteur Full Page Check ou un moniteur de transaction, le navigateur demande à un service DNS situé sur un serveur externe de traduire le nom de domaine demandé en adresse IP. Cette adresse est nécessaire pour exécuter la requête HTTP. Un Full Page Check reproduit exactement le comportement du navigateur d'un utilisateur final.

Or, pour la surveillance et les tests, cela ne suffit pas toujours. Par exemple, vous pouvez vouloir utiliser l'URL de votre entreprise en ciblant un serveur ou une adresse IP spécifique, plutôt que d'utiliser le DNS traditionnel.

C'est dans ce type de situation que le contournement DNS vous est utile. Vous pouvez spécifier une adresse IP fixe (ou un autre nom de domaine CNAME) pour connecter le navigateur à un nom de domaine particulier. Concrètement, cela vous permet de contourner ou remplacer le système DNS classique. Ce fonctionnement est très similaire à celui du _fichier hosts_ dans Windows ou Linux. 
## Comment ajouter un contournement DNS

1. Pour le moniteur Full Page Check, ouvrez le menu [SHORTCODE_3] Surveillance > Configuration du moniteur [SHORTCODE_4].
2. Cliquez sur le nom du moniteur pour accéder à ses paramètres.
3. Vérifiez que le _Type de navigateur_ sélectionné est "Chrome avec des métriques supplémentaires".
4. Ouvrez l'onglet [SHORTCODE_5] Avancé [SHORTCODE_6].
   ![]([LINK_URL_5])
5. Dans la partie _Connexion_, cliquez sur [SHORTCODE_7] Ajouter un contournement DNS [SHORTCODE_8].
6. Précisez le _Domaine source_ et le _Domaine cible_ (pour des questions de sécurité, tous les domaines cibles ne sont pas acceptés).
7. Pensez à cliquer sur le bouton [SHORTCODE_9]Enregistrer[SHORTCODE_10] avant de quitter la page.

[SHORTCODE_1]
**Remarque** : Vous pouvez utiliser des caractères génériques pour le domaine _source_, mais pas pour le domaine cible. Par exemple, vous pouvez créer une règle *acc.exemple.com pour www\.exemple.com, afin de rediriger les requêtes de server1-acc.exemple.com vers www\.exemple.com.
[SHORTCODE_2]

## Quand utiliser un contournement DNS ? [ANCHOR_1]
Quand avez-vous intérêt à contourner le serveur DNS par défaut ? Voici quelques scénarios où le contournement DNS peut vous être utile ou nécessaire :
### Environnement DTAP / serveur UAT
Imaginons que vous souhaitiez tester et surveiller la performance de vos pages web dans un environnement DTAP ou sur un serveur servant aux tests de validation utilisateur (UAT). Ces pages vous donnent un aperçu réel de leur apparence lors de la production, et peuvent donc nécessiter une surveillance. Avec un contournement DNS, vous ordonnez à Uptrends de surveiller et de vérifier un emplacement spécifique.
### Configuration SSL différente
Imaginons que votre environnement de test doive utiliser les mêmes certificats SSL que votre environnement de production. L'adresse du serveur web de vérification du certificat doit être identique à l'adresse précisée sur le certificat, sous peine de générer une erreur lors du Full Page Check.
### Site web de pré-production situé sur un domaine externe
Imaginons maintenant que votre site web soit en cours de refonte auprès d'une partie tierce. Vous voudriez tester et surveiller les nouvelles pages web depuis leur emplacement actuel, sur le serveur web du développeur.
### Page web sur un nœud dans un cluster web
Le contournement DNS vous permet de vérifier que chaque nœud du cluster fonctionne correctement, et de surveiller les nœuds séparément.
### Page web sur un serveur d'origine du CDN
Dans cet exemple, votre site web est hébergé sur un réseau de diffusion de contenu (CDN). Il est possible que vous souhaitiez tester et surveiller le site web sur son serveur d'origine, mais pas les versions mises en cache sur les serveurs de périphérie. La configuration d'un contournement DNS vous permet de demander à Uptrends d'effectuer la vérification directement sur le serveur d'origine.
### Page web hébergée à un emplacement spécifique du CDN
Si votre site web est hébergé sur un CDN, il est possible que vous souhaitiez surveiller l'une des instances des pages web mises en cache sur l'un des serveurs de périphérie du réseau de diffusion de contenu. Vous pouvez configurer un contournement DNS pour ordonner à Uptrends de cibler ce serveur. Cela étant, il existe une solution plus simple pour surveiller ce type d'emplacement. Il suffit de configurer un moniteur Full Page Check et de le laisser effectuer ses vérifications depuis les [checkpoints]([LINK_URL_6]) de la région qui vous intéresse.
### Page web ou site web hébergé sur un réseau interne
Si vous avez configuré des checkpoints privés sur votre réseau, le moniteur Full Page Check peut emprunter un itinéraire sur le réseau interne pour que l'adresse de la page soit résolue dans le serveur interne. Si vous préférez réaliser le test en dehors de votre réseau, vous pouvez utiliser le contournement DNS pour modifier l'itinéraire réseau. Cela peut s'avérer utile quand il existe différentes pages et modalités de connexion interne et externe.