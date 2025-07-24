{
  "hero": {
    "title": "Passer de la chaîne d'agent utilisateur aux indications du client"
  },
  "title": "Passer de la chaîne d'agent utilisateur aux indications du client",
  "summary": "Pour collecter des données sur les utilisateurs, le Real User Monitoring d'Uptrends utilise un request header de type agent utilisateur. Or, Google va progressivement remplacer cette chaîne user-agent par des indications client dans les prochaines versions des navigateurs basés sur Chromium.",
  "url": "[URL_BASE_TOPICS]rum/indications-client",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Qu'est-ce que la chaîne d'agent utilisateur ?
La chaîne d'agent utilisateur (aussi appelée chaîne user-agent, ou UA) est un en-tête de requête HTTP utilisé pour adapter la page web aux spécifications du navigateur. Lorsqu'un serveur web reçoit une requête de page web depuis le navigateur d'un client, le navigateur envoie un request header (ou en-tête de requête) qui contient la chaîne d'agent utilisateur. Cette information indique au serveur quel type de navigateur se trouve à l'autre bout. Avant d'envoyer la page en réponse, le serveur web ajuste la page web pour que le contenu soit adapté au type de navigateur concerné.

La chaîne d'agent utilisateur pour un request header de Chrome peut ressembler à ceci :  
[INLINE_CODE_1]

Avec le [Real User Monitoring]([LINK_URL_1]) d'Uptrends, un petit script est ajouté aux pages que vous suivez avec le RUM. Quand vos utilisateurs ouvrent une page web contenant un script RUM, celui-ci utilise le request header HTTP d'agent utilisateur pour enregistrer les informations sur le navigateur, sa plateforme et ses capacités. Une fois la page chargée, le script regroupe les données collectées avec les informations concernant le navigateur et l'emplacement du visiteur, et envoie le tout à votre dashboard Uptrends.
## Quelles sont les raisons et les conséquences de la transition vers les indications du client ?
Actuellement, Uptrends utilise la chaîne d'agent utilisateur pour collecter les données sur le navigateur de l'utilisateur, les systèmes d'exploitation des appareils et les versions. Google Chrome se prépare à remplacer cette chaîne par la fonction User-Agent Client Hints (UA-CH) pour tous les appareils Chrome et les navigateurs basés sur Chromium, y compris Microsoft Edge. Avec les indications du client, ces informations sont fournies dans plusieurs sections plus petites et distinctes, et non plus sous la forme d'une longue chaîne de données.

Il y a deux raisons pour lesquelles Google réalise cette transition : la protection de la confidentialité de l'internaute est renforcée, et les données sont renvoyées sous un format plus facile à utiliser pour les développeurs.
## Quelles sont les conséquences pour le RUM ?
Uptrends se prépare pour ce changement et modifiera le script en conséquence. **Aucune mesure n'est nécessaire** de la part de nos clients.

Les informations collectées avec l'agent utilisateur actuel seront progressivement réduites. Par conséquent, la quantité d'informations sur les utilisateurs récupérées aux fins de monitoring va diminuer. Nous vous informerons dès que ce changement surviendra et qu'il faudra adapter les paramètres de scripts côté client.

Pour en savoir plus sur la transition et les phases de réduction de l'utilisation de la chaîne d'agent utilisateur avec Chromium M101, [lisez cet article sur la réduction de l'agent utilisateur pour les projets Chromium]([LINK_URL_2]) (en anglais).

[SHORTCODE_1] **Remarque** : Si vous avez des questions sur le script RUM et le respect de la confidentialité des utilisateurs, lisez cet article de notre base de connaissances [RUM et la confidentialité des utilisateurs]([LINK_URL_3]) [SHORTCODE_2]