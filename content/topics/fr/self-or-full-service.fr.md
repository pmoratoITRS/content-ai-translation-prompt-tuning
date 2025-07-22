{
"hero": {
"title": "Options pour les scripts de transaction"
},
"title": "Options pour les scripts de transaction",
"summary": "Pour générer le script de transaction final, vous avez le choix entre plusieurs options : le service complet, le libre-service ou l'utilisation directe du script.",
"url": "/support/kb/surveillance-synthetique/transactions/service-complet-ou-libre-service",
"translationKey": "https://www.uptrends.com/support/kb/transactions/self-or-full-service"
}

Les moniteurs de transactions ont besoin d'un script pour reproduire les étapes à surveiller. Selon votre niveau d'aisance avec la création de scripts, plusieurs options sont disponibles.

- **Si vous savez que vous aurez besoin d'aide**, le support d'Uptrends peut gérer la création et le test du script dans le cadre de l'option [transactions en service complet](#full-service).
- **Si vous êtes assez à l'aise avec les langages web tels que ** HTML, CSS, JSON et XPath, l'option [transactions en libre-service](#self-service) est faite pour vous.
- **Si vous avez un niveau avancé**, vous pouvez passer directement à l'éditeur de scripts et copier coller votre script depuis vos outils habituels de scripts et de contrôle de version, et ainsi [créer votre script de A à Z](#script-from-scratch). Vous pouvez aussi gérer vos transactions et vos scripts avec l'[API]({{< ref path="support/kb/api" lang="fr" >}}) d'Uptrends.

Avant de créer les scripts de vos transactions, vous devez décider quelle méthode est la plus adaptée pour vous. Pour rappel, [l'équipe de support]({{< ref path="contact" lang="fr" >}}) est toujours là pour vous.

## Transactions en service complet {id="full-service"}

Avec cette option, vous enregistrez vos transactions, puis vous les chargez en choisissant l'option "service complet". Les spécialistes de script d'Uptrends prennent le relais et utilisent votre enregistrement pour modifier et tester vos scripts. Prévoyez environ une semaine entre l'envoi de votre enregistrement et la réception d'un moniteur prêt à l'emploi dans votre compte. Par ailleurs, cette option est encadrée par notre [politique de révision des scripts de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="fr" >}}).

### À qui s'adresse l'option des transactions en service complet ?

L'option service complet est accessible à tout le monde, et l'équipe de support se réjouit de vous aider à créer vos moniteurs opérationnels. Les transactions en service complet sont faites pour vous si :

- Vous n'êtes pas à l'aise avec les langages de script tels que HTML, CSS, JSON et XPath.
- Vous ne disposez pas du temps et des ressources nécessaires pour cette tâche.
- Vous ne voulez pas vous charger de cette tâche.

### Quelles sont les étapes de cette option ?

Si vous choisissez l'option service complet, vous devez :

1. Vous exercer à réaliser la transaction afin de produire un enregistrement exact et précis.
2. [Enregistrer la transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}})
3. Charger les enregistrements nécessaires à la création des scripts. Après avoir interrompu l'enregistrement, vous pouvez choisir l'option "transactions en service complet" pour soumettre l'enregistrement à l'équipe de support.

Le processus de chargement crée un moniteur en lecture seule dans votre compte. Cet état reste en vigueur pendant l'exécution du service complet. Une fois le script rédigé et testé, les spécialistes de script d'Uptrends vous informent de la disponibilité du moniteur et le débloquent dans votre compte. Veuillez lire notre [politique de révision des scripts de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="fr" >}}) qui contient des informations importantes sur les délais de réalisation du service complet et les limites applicables aux nombres d'enregistrement soumis simultanément.

{{< callout >}}
**Remarque** : Si vous avez des questions sur le monitoring des applications web ou si vous voulez définir une méthode pour maîtriser vos transactions, ces articles pourraient vous intéresser : [Comprendre le monitoring d'applications web]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="fr" >}}) et [Maîtriser vos transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="fr" >}}).
{{< /callout >}}

## Transactions en libre-service {id="self-service"}

Avec l'option transactions en libre-service, vous maîtrisez complètement vos scripts de transaction. Pour préparer votre script, vous avez deux possibilités :

- Utilisez [l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}) pour vous doter d'un script de base, puis affinez-le et testez-le à l'aide de [l'éditeur d'étapes]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}).
- Passez-vous de l'enregistreur de transaction et utilisez [l'éditeur d'étapes]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}) directement pour créer entièrement vos scripts dans l'éditeur visuel d'étapes.

Nous vous recommandons d'utiliser l'enregistreur, car il vous fera gagner un temps précieux.

### À qui s'adresse l'option des transactions en libre-service ?

Nous encourageons tous les utilisateurs à essayer les transactions en libre-service. Cela ne coûte rien d'essayer de modifier et de tester des scripts en mode développement. Vous pourriez même trouver cet exercice amusant. De plus, [l'équipe de support]({{< ref path="contact" lang="fr" >}}) est toujours là pour vous aider ou prendre la relève. Les transactions en libre-service sont faites pour vous si :

- Vous avez des bases avec les technologies web de base et vous apprenez assez rapidement.
- Vous connaissez bien les langages côté client tels que HTML, CSS, XPath et JSON.

### Quelles sont les étapes de cette option ?

1. Utiliser l'enregistreur de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="fr" >}}) pour plus d'efficacité.
2. Ouvrir votre nouveau moniteur dans votre compte Uptrends et [modifier et tester]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}) le script.

## Créer les scripts de A à Z {id="scripting-from-scratch"}

Les utilisateurs les plus chevronnés pourront aussi choisir cette option. Si c'est votre cas, vous pouvez vous passer de l'enregistreur de transaction et de l'éditeur d'étapes, et saisir votre script en utilisant l'éditeur textuel de script qui se trouve directement dans les paramètres de votre moniteur. Il vous suffit de cliquer sur le bouton {{< AppElement type="button" >}}Basculer vers le script{{< /AppElement >}} en haut de l'onglet {{< AppElement type="tab" >}}Étapes{{< /AppElement >}} de votre moniteur, puis d'y copier et coller votre script.

Vous pouvez aussi utiliser l'[API]({{< ref path="support/kb/api" lang="fr" >}}) pour créer de nouveaux moniteurs de transactions, puis les modifier et les tester.
