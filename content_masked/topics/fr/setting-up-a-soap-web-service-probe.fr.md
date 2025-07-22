{
  "hero": {
    "title": "Configurer un moniteur de service web SOAP"
  },
  "title": "Configurer une surveillance SOAP",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/configurer-moniteur-service-web-soap",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Cet article vous explique comment ajouter un **moniteur SOAP** à votre compte Uptrends.

## Configuration d'un moniteur de service web SOAP

Pour tester un service SOAP, on appelle en général une méthode de ce service web avec des données d'entrée sous la forme d'une enveloppe SOAP, puis on vérifie que la réponse est correcte.

1. Ouvrez la page de configuration Ajouter un moniteur. (Si vous avez besoin d'aide, vous pouvez lire l'article [Ajouter un moniteur]([LINK_URL_1]).) Sélectionnez un moniteur Webservice HTTP ou Webservice HTTPS.

   [SHORTCODE_1]**Remarque :** L'utilisation de ce type de moniteur garantit que nos requêtes envoyées au serveur contiendront Content-Type: text/xml. Puisque les enveloppes SOAP sont au format XML, cela devrait fonctionner pour la plupart des services web.[SHORTCODE_2]
2. Saisissez un nom, l'intervalle de vérification, l'URL et l'information sur le port.
3. Accédez à l'onglet [SHORTCODE_5]Avancé[SHORTCODE_6] et définissez la méthode HTTP POST.
4. Définissez votre requête SOAP (l'enveloppe SOAP entière) dans le champ Requête body.

   En général, votre requête ressemblera à ceci :  
   *... Infos du message à mettre ici ...*
5. Votre serveur web s'attend probablement à recevoir un en-tête HTTP SOAPAction, qui lui indiquera quelle méthode doit être exécutée par votre service web.

   Dans le champ HTTP request headers, spécifiez l'en-tête au format suivant :

   [INLINE_CODE_1]

   [SHORTCODE_3]**Remarque** : Si votre serveur web attend un type de contenu différent, vous pouvez le spécifier ici. Par exemple : Content-Type: application/xml[SHORTCODE_4]
6. Il est probablement utile de vérifier que votre service web renvoie le contenu approprié.

   Vous pouvez rechercher un contenu spécifique en le spécifiant dans le champ *Recherche de correspondance de contenu* situé dans l'onglet [SHORTCODE_7]Conditions d'erreur[SHORTCODE_8].

   Le service Uptrends cherchera alors ce contenu dans la réponse HTTP à chaque fois qu'il effectuera une vérification.

## Votre moniteur SOAP ne fonctionne pas ?

Si vous n'arrivez pas à faire fonctionner votre moniteur SOAP, contactez notre support en soumettant un [ticket de support]([LINK_URL_2]).

Si possible, fournissez une capture d'écran d'une requête HTTP qui devrait marcher. Habituellement, vous aurez une configuration de travail avec des outils de test de service web, que vous pouvez utiliser pour fournir une capture avec Fiddler, ou une commande cURL qui contient toutes les données nécessaires (URL/POST data/en-têtes HTTP.)
