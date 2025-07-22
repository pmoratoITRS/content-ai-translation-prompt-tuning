{
"hero": {
"title": "FAQ sur les checkpoints privés"
},
"title": "FAQ sur les checkpoints privés",
"summary": "Questions fréquentes sur les checkpoints privés d'Uptrends",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/faq-checkpoints-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-faq"
}

## Puis-je avoir plusieurs checkpoints privés ?

Oui, tout à fait. Par exemple, si votre entreprise possède plusieurs sites d'hébergement, vous pouvez installer un [checkpoint privé]({{< ref path="support/kb/synthetic-monitoring/checkpoints/#user-managed" lang="fr" >}}) dans chaque emplacement concerné.

## Puis-je utiliser mon checkpoint privé dans plusieurs comptes Uptrends ?

Oui, tout à fait. Il suffit de nous dire avec quels comptes vous voulez utiliser votre checkpoint privé. En revanche, votre checkpoint privé ne sera accessible que par vous.

## Pourquoi y a-t-il deux checkpoints privés par défaut ? {id="two-default-private-checkpoints"}

Lorsque vous créez un nouvel [emplacement privé]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}), deux checkpoints privés sont ajoutés à l'emplacement par défaut.

En effet, conformément aux recommandations de configuration, deux checkpoints sont nécessaires pour assurer la disponibilité de votre emplacement privé. Avec deux checkpoints redondants, un checkpoint peut être mis à jour tandis que l'autre assure la surveillance. De même, si l'un de ces checkpoints venait à tomber en panne, l'autre pourrait continuer de surveiller vos sites web, services ou serveurs.

## Puis-je exécuter des moniteurs de transactions dans mon application métier interne ?

Oui, tout à fait. Cette fonctionnalité d'Uptrends est disponible. Vous pouvez donc surveiller les transactions sur vos applications hébergées en interne.

## Dois-je créer mes propres scripts de transaction ?

Non, ce n'est pas nécessaire. Comme habituellement, vous pouvez enregistrer vos [transactions]({{< ref path="features/transaction-recorder" lang="fr" >}}) avec l'extension Chrome Transaction Recorder (Enregistreur de transaction). Ensuite, libre à vous de décider si vous souhaitez transformer vous-même votre enregistrement en une transaction stable et exploitable, ou si vous préférez confier cette tâche à un spécialiste des transactions d'Uptrends.

## Quels types de navigateurs de moniteurs sont pris en charge ?

Les moniteurs Full Page Check et de transactions qui utilisent des [types de navigateurs avec des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}}) sont pris en charge dans les emplacements privés. Veuillez noter que les moniteurs hérités ne fournissant pas de métriques supplémentaires ne sont pas pris en charge.

## Comment empêcher le chargement des captures d'écran et des pellicules sur le cloud ?

Suivez les instructions relatives à la [protection des données]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}) pour désactiver la création de captures d'écran, de captures d'écran chronologiques et de captures d'écran d'erreurs pour le moniteur HTTP(S) sur les checkpoints privés.

## Comment résoudre les problèmes ?

Consultez le [guide de résolution des problèmes]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting" lang="fr" >}}) dans la base de connaissances d'Uptrends.

## Je voudrais en savoir plus. Qui puis-je appeler ?

Votre consultant en monitoring Uptrends est toujours là pour vous. Si vous connaissez son numéro ou son adresse e-mail, veuillez le contacter directement. Si vous ne savez pas qui est votre consultant en monitoring ou si vous n'avez pas ses coordonnées, veuillez utiliser notre [page de contact]({{< ref path="contact" lang="fr" >}}) pour ouvrir un ticket de support. Vous pouvez aussi téléphoner à l'un de nos bureaux internationaux.

## Si vous avez des doutes ou des questions…

À toute étape de la configuration, si vous avez un doute ou une question, n'hésitez pas à solliciter Uptrends en ouvrant un [ticket de support]({{< ref path="contact" lang="fr" >}}). Nous vous recontacterons rapidement.