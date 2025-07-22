{
  "hero": {
    "title": "Les Modes Moniteurs"
  },
  "title": "Les Modes Moniteurs",
  "summary": "Uptrends offers three new monitoring modes: development, staging, and production.",
  "url": "/support/kb/surveillance-synthetique/parametres-moniteurs/les-modes-moniteurs",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-mode"
}

La plupart du temps, lorsque vous créez un nouveau moniteur, vous voulez que ce moniteur devienne actif dans votre compte immédiatement. Une fois activé le moniteur commence à produire des mesures toutes les minutes (si l'intervalle du moniteur est ainsi configuré). Vous pouvez inspecter les résultats de ces mesures dans le journal du moniteur et Uptrends génère des alertes lorsque des erreurs commencent à se produire. Dans de nombreux cas, l'activation immédiate de votre moniteur fonctionne très bien. Cependant, cette immédiateté n'est pas toujours optimale. 

## Fonctionner en mode production ou pas

Lorsque vous créez une nouvelle transaction par exemple, vous passerez probablement un certain temps sur sa mise au point avant de l'exécuter en production. En attendant, vous souhaiterez peut-être laisser la transaction s'exécuter pendant un certain temps pour voir à quel point elle est stable sans courir le risque de générer des faux positifs (alertes d'erreur). Les faux positifs ont un effet indésirable sur vos SLA et d'autres indicateurs de disponibilité.

De même, si vous avez une transaction existante qui doit être remplacée par un nouveau script dès que vous lancez votre site web mis à jour, vous voudrez préparer cette nouvelle transaction pour qu'elle soit prête. Cependant, tant que le nouveau script de transaction reste inactif, le moniteur utilise de précieux crédits de transaction qui comptent dans votre quota de transactions disponibles. Vous pouvez acheter des crédits supplémentaires, mais il y a un moyen plus efficace d'organiser vos moniteurs.

## Gérer le cycle de vie du moniteur à l'aide des modes moniteur

Nous avons trois modes moniteurs différents : développement, mise en scène et production. Vous pouvez basculer entre ces modes pour tous les types de moniteurs (pas seulement les moniteurs de transactions) si vous avez un compte Professional, Business ou Entreprise. Pour les autres plans tarifaires, le mode moniteur est toujours en mode production.

Alors, dans quels cas ces différents modes de moniteur seront-ils utiles ?

### Mode de développement

Les moniteurs en mode développement sont toujours inactifs. Les moniteurs en mode développement ne peuvent pas être planifiés (pour une exécution), et donc ils ne génèrent aucun résultat dans leurs journaux. Cela signifie également qu'ils sont gratuits ! Vous pouvez en avoir autant que vous le voulez, sans frais supplémentaires. Mais toutes les données attachées à un moniteur disparaissent dès que vous remettez un moniteur en mode développement.

Le mode développement est utile pour créer et tester des versions préliminaires. Supposons que vous créez un nouveau moniteur de transaction ou un moniteur d'API multi-étapes et que vous exécutez des tests manuels dessus dans l'éditeur. Sur la base des résultats du test, vous pouvez le peaufiner jusqu'à ce que vous soyez satisfait de ces résultats de test initiaux. Tant que vous restez en mode développement, cela ne vous coûte rien et le moniteur n'a aucun impact négatif sur votre disponibilité.

Par conséquent, ce mode de développement vous permet de conserver plusieurs copies (inactives) sans avoir à acheter d'autres moniteurs, étapes de transaction ou étapes API. Vous pouvez garder les moniteurs en mode développement pendant longtemps. Cependant, lorsque vous êtes prêt à passer votre moniteur en mode de développement inactif vers le mode mise en scène ou production, vous aurez besoin d'un crédit moniteur disponible dans votre compte pour l'activer ou sinon l'échanger avec un autre moniteur.

### Mode de mise en scène

Le mode de mise en scène est généralement la prochaine étape du cycle de vie d'un nouveau moniteur. Contrairement au mode de développement, le mode mise en scène vous permet de planifier un moniteur pour une exécution normale. Une fois activé, le moniteur génère de nouvelles mesures comme n'importe quel autre moniteur, et les résultats sont visibles dans le journal du moniteur comme d'habitude. Ce qui est bien avec ce mode mise en scène, c'est que même si vous pouvez observer les résultats de la surveillance, ils n'affectent pas votre disponibilité, n'ont aucun impact sur vos SLA et ne génèrent pas d'alertes. C'est comme si vos moniteurs fonctionnaient dans un environnement bac à sable ; les mesures sont réelles, mais le temps de disponibilité, les SLA, les statistiques historiques et le pipeline d'alerte restent correctes ([en savoir plus](/support/kb/surveillance-synthetique/parametres-moniteurs/Les-effets-du-mode-mise-en-scene-sur-les-rapports-et-les-donnees-sla)).

Une fois en mode mise en scène, le moniteur compte dans le nombre total de moniteurs/crédits qui existent dans votre compte. En règle générale, il faudrait promouvoir un moniteur mise en scène vers le mode production dès que vous êtes certain que le moniteur est stable. Sinon, vous ne profitez pas de la gamme complète de fonctionnalités alors que le coût est le même que pour un moniteur de production.

### Mode de production {id="monitormodeproduction"}

C'est le mode par défaut. En mode production un moniteur est disponible pour une exécution régulière, la disponibilité du moniteur affecte la disponibilité globale du compte, les résultats du moniteur sont pris en compte pour les calculs de SLA et des alertes sont disponibles.
