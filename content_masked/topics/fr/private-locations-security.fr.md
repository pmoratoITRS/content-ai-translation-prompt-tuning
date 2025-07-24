{
  "hero": {
    "title": "Mesures de sécurité liées aux emplacements privés"
  },
  "title": "Mesures de sécurité liées aux emplacements privés",
  "summary": "Quelles sont les mesures à prendre pour garantir la sécurité des opérations de checkpoints dans vos emplacements privés ?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/securite-emplacements-prives",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Si vous avez des questions sur la sécurité de l'installation des checkpoints de vos emplacements privés et sur ce que vous devez mettre en place pour protéger vos données, cet article est fait pour vous. Vous y trouverez les principales mesures de sécurité qui relèvent de la responsabilité d'Uptrends ou de celle de votre entreprise.

## Conteneurs

L'installation d'un checkpoint privé repose sur des conteneurs Docker. Certaines fonctionnalités de sécurité sont intégrées dans la technologie des conteneurs, tandis que d'autres sont assurées par Uptrends :

- Uptrends utilise son propre référentiel de conteneurs sur Microsoft Azure. Vous pouvez ainsi travailler avec un référentiel de taille réduite, qui contient uniquement les conteneurs sécurisés dont vous avez besoin.
- Docker se charge de la vérification des conteneurs.
- Uptrends contrôle le contenu des images de conteneurs au moyen d'un logiciel d'analyse de la sécurité, avant de les charger dans le référentiel de conteneurs. Cela permet à Uptrends de déceler les vulnérabilités connues avant de mettre à disposition de nouvelles versions du logiciel conteneurisé. En complément, nous vous recommandons d'analyser aussi les ensembles de conteneurs (lors des mises à jour) après les avoir téléchargés et avant de les installer.
- Par définition, les conteneurs Docker ne peuvent pas intervenir dans les communications externes entrantes et dans les communications survenant sur l'hôte où ils sont installés. Il n'est pas nécessaire d'ouvrir des ports de pare-feu entrants.
- Lors de l'installation standard d'un emplacement privé, un script de mise à jour automatique des conteneurs Docker est installé. Ainsi, les emplacements privés tiennent toujours compte des dernières mises à jour de sécurité.

## Logiciels (autres que l'installation des conteneurs Docker)

Le fonctionnement des checkpoints repose sur le logiciel de checkpoints mais aussi d'autres logiciels de soutien. Prêtez attention aux points suivants :

- Les [mises à jour]([LINK_URL_1]) de Windows, des navigateurs, etc., doivent être effectuées pour récupérer les correctifs de bugs dès qu'ils sont disponibles et ainsi corriger les problèmes de sécurité.
- Uptrends est titulaire de la certification ISO 27001. Cette certification régit les pratiques de développement et de sécurité informatique comme les suivantes :
   - Les changements apportés au logiciel Uptrends sont vérifiés par des pairs.
   - Des outils et des procédures sont en place pour assurer la protection contre les vulnérabilités dans les dépendances logicielles.
   - Un responsable de la sécurité est nommé et Uptrends a défini des procédures applicables en cas d'incident de sécurité.
   - La [certification ISO 27001]([LINK_URL_2]) d'Uptrends est consultable.
- Sur un hôte Windows, la présence d'un outil d'analyse anti-virus est suffisante. La plupart des anti-virus peuvent contrôler les processus et le trafic à l'intérieur des conteneurs. Vérifiez toutefois que c'est bien le cas avec votre outil.

## Trafic réseau

Les vérifications du moniteur s'intéressent aussi au trafic sur votre réseau, et plus précisément aux données et aux requêtes qui circulent à l'intérieur et parfois à l'extérieur de votre réseau. Prêtez attention aux points suivants :

- Limitez toujours l'accès à votre réseau au strict minimum.
- Les emplacements privés n'ont pas besoin de connexions entrantes, et nous recommandons de les désactiver complètement. Toute connexion avec l'extérieur doit être sortante, et toujours initiée par l'hôte.
- Les instructions que la plateforme cloud d'Uptrends envoie aux points de contrôle sont toujours protégées par une clé secrète. Le point de contrôle valide les instructions entrantes en utilisant la clé publique correspondante (qui est connue du checkpoint), ce qui confirme que l'instruction a bien été envoyée par Uptrends.

## Confidentialité et protection des données

La surveillance est avant tout une affaire de données. Ces données peuvent être simples, comme une vérification donnant lieu à un résultat "OK" ou à une erreur, ou plus complexes, comme des captures d'écran de votre site web lors d'une étape de transaction spécifique. Peut-être vous demandez-vous quels types d'informations sont envoyés vers l'environnement cloud d'Uptrends, et quelles informations vous pouvez empêcher de sortir de votre site web.

- Les données relatives à la santé du point de contrôle sont envoyées à l'application cloud d'Uptrends. Ces données permettent de vérifier si le checkpoint fonctionne, et s'il fonctionne correctement. Par exemple, elles permettent de repérer un checkpoint obsolète ou incompatible. Lorsqu'un checkpoint est dysfonctionnel, cela peut affecter la validité des résultats de monitoring.
- Les données relatives à l'état du checkpoint sont visibles dans l'onglet Santé, dans les emplacements privés.
- En dehors des informations relatives à la santé du point de contrôle, seules les informations sur les mesures sont envoyées vers la plateforme cloud d'Uptrends.
- Si vous avez des doutes quant à l'envoi d'informations sur les mesures en dehors de votre entreprise, veuillez lire l'article de la base de connaissances sur la [protection des données]([LINK_URL_3]). Vous y trouverez des explications pour désactiver la collecte de certaines informations, telles que les captures d'écran, les adresses IP, etc.

En matière de données et de confidentialité, les informations de connexion doivent aussi faire l'objet d'une attention particulière. Uptrends vous recommande vivement de réfléchir aux identifiants que vous utilisez dans le cadre du monitoring. N'utilisez jamais un profil d'utilisateur intensif pour effectuer des tâches de base. Octroyez uniquement les autorisations et les droits dont chaque utilisateur a besoin pour effectuer ses tâches. Tout autre droit peut donner accès à des ressources ou à des tâches auxquelles l'utilisateur ne devrait pas avoir accès. Pour en savoir plus à ce sujet, lisez les informations relatives aux [identifiants de connexion]([LINK_URL_4]).
