{
  "hero": {
    "title": "Le fonctionnement d'un moniteur HTTP"
  },
  "title": "Le fonctionnement d'un moniteur HTTP",
  "summary": "Apprenez comment Uptrends effectue un test HTTP(S) et comment le système réagit lorsqu'il rencontre et d'erreur.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/uptime-monitoring/http-et-https/le-fonctionnement-dun-moniteur-http",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Vous êtes-vous déjà demandé ce qui se passe quand Uptrends lance une vérification HTTP ou HTTPS  sur votre site ? De nombreux scénarios différents peuvent se produire en fonction des circonstances; nous allons examiner quelques-uns d'entre eux.

1.  Uptrends choisit au hasard un de vos points de contrôle désignés pour le test.
2.  Uptrends tente de résoudre le nom de domaine spécifié.   
    [SHORTCODE_1]**Remarque:** Vous pouvez spécifier l'adresse IP au lieu du nom de domaine pour passer outre le test de résolution d'adresse, mais vous ne recevrez pas d'alerte si votre site a des problèmes de résolution d'adresse.[SHORTCODE_2] 
3.  Avec l'adresse IP, Uptrends tente alors une connexion bas niveau TCP sur le port 80 pour HTTP, 443 pour HTTPS, ou le port que vous avez spécifié.
4.  Après le test de base décrit à l'étape 3, nous ouvrons une nouvelle connexion TCP pour envoyer la requête HTTP(S), et nous attendons la réponse.

## Qu'est-ce qui se passe quand Uptrends trouve un problème ?

Des erreurs peuvent se produire à chaque étape dans le processus de test, et en fonction de l'erreur, Uptrends essaie immédiatement différentes choses avant d'émettre une alerte. Avec la plupart des erreurs, Uptrends tentera d'obtenir une connexion sans erreur en utilisant un point de contrôle différent. Si Uptrends duplique l'erreur à partir d'un point de contrôle différent, Uptrends sonne l'alarme. Uptrends fait quelques exceptions basées sur des erreurs spécifiques.

### Échecs HTTPS

Si, avec le type de moniteur HTTPS, la requête échoue (étape 3), Uptrends peut essayer plusieurs fois avec des protocoles de sécurité différents avant de déclarer l'échec du test.

### HTTP(S) avec des informations d'authentification fournies

Pour des requêtes HTTP et HTTPS qui contiennent des informations d'authentification de l'utilisateur, Uptrends peut refaire un test précédemment échoué avant de déclarer la tentative un échec.

### Erreurs réseau

Si la requête HTTP ou HTTPS échoue en raison d'un problème de réseau, Uptrends tente d'effectuer un traceroute à l'adresse IP. Le traceroute envoie une série de paquets Ping (= ICMP).
