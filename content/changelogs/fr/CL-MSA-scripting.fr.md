{
"title": "Personnalisation des scripts de pré-requête et de post-réponse dans les moniteurs d'API multi-étapes",
"date": "2024-07-03",
"url": "/changelog/juillet-2024-scripts-msa",
"translationKey": "https://www.uptrends.com/changelog/july-2024-msa-scripting"
}

Vous pouvez désormais [personnaliser les scripts de pré-requête et de post-réponse]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}}) pour chaque étape dans les [moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="fr" >}}). Les moniteurs d'API multi-étapes incluent plusieurs options permettant de configurer les requêtes et de traiter les réponses. Toutefois, certains cas clients nécessitent une plus grande flexibilité ou des fonctionnalités supplémentaires. Grâce aux nouveaux onglets de création de scripts, les utilisateurs peuvent appliquer du code Javascript à la requête et à la réponse de chaque étape, voire intégrer des fonctions spéciales pour interagir avec le reste des paramètres du moniteur.

![Exemple de script de pré-requête dans un moniteur MSA](/img/content/scr-msa-prerequest-script.min.png)

Cette fonctionnalité de script offre une flexibilité maximale pour configurer le traitement des requêtes et des réponses d’une façon qui répond à vos besoins.