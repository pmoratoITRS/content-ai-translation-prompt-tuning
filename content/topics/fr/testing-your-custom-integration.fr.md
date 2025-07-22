{
"hero": {
"title": "Tester votre intégration personnalisée"
},
"title": "Tester votre intégration personnalisée",
"summary": "Intégrations personnalisées - comment tester votre nouvelle intégration",
"url": "/support/kb/alerter/integrations/integrations-personnalisees/tester-votre-integration-personnalisee",
"translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/testing-your-custom-integration"
}

Une fois que vous avez créé ou modifié une intégration personnalisée, il est recommandé de la tester avant de l'utiliser en production. Cet article montrera deux façons de tester l'intégration nouvellement mise en place. En règle générale, si les données d'alerte ont été correctement analysées ou traitées, vous les verrez dans le système tiers auquel vous vous connectez, ce qui signifie que le test a réussi.

## Vérification d'une intégration à l'aide de messages de test

Il est possible de tester de nouvelles intégrations en générant des données fictives du côté Uptrends, et de les envoyer au système tiers. L'onglet {{< AppElement type="tab" >}}Personnalisations{{< /AppElement >}} dans l'éditeur d'intégration comporte un bouton intitulé **Envoyer un message de test** qui vous permet d'envoyer un message de test au système tiers à l'aide des étapes HTTPS que vous avez créées. Lorsque vous utilisez cette fonction de test, vous pouvez sélectionner le type d'alerte (une alerte d'erreur, une alerte OK ou une alerte de rappel) qu'Uptrends doit utiliser pour ce message de test particulier. Vous pouvez remplir les autres valeurs si nécessaire, et les données restantes (qui seraient normalement des données de surveillance pertinentes et des données d'alerte) seront remplies de valeurs fictives.

Une fois qu'Uptrends génère le message et l'envoie au système tiers ou à l'API, le contenu complet du message, le code de réponse du serveur et le contenu s'affichent. Vous pouvez développer les en-têtes et le contenu des requêtes et des réponses pour inspecter le trafic sortant et entrant associés à ce message de test.

## Vérification d'une intégration à l'aide de données en direct

Bien qu'un test statique décrit dans la section précédente soit utile pour tester le fonctionnement de votre message et vos variables et établir que le canal de communication vers le système externe fonctionne correctement, il est bon d'avoir aussi la possibilité de vérifier que l'intégration fonctionne correctement dans une situation réelle.

Tout d'abord, vérifiez que l'une de vos définitions d'alerte utilise réellement votre intégration. Sinon, Uptrends ne déclenche jamais l'intégration pour envoyer des messages. Pour plus d'informations sur l'activation des intégrations dans votre configuration d'alerte, lisez l'article sur les [niveaux d'escalade](/support/kb/alerter).

Ensuite, une situation d'erreur doit se produire pour que votre surveillance génère une véritable alerte. Dès que vous voyez une alerte dans le status des alertes ou dans le tableau de bord du journal des alertes, cliquez dessus pour révéler les détails de cette alerte. L'onglet {{< AppElement type="tab" >}}Détails{{< /AppElement >}} liste toutes les propriétés clés de l'alerte ; l'onglet {{< AppElement type="tab" >}}Messages{{< /AppElement >}} contient les informations dont vous avez besoin pour inspecter le trafic de messages entre Uptrends et le système externe.

Dans l'onglet {{< AppElement type="tab" >}}Messages{{< /AppElement >}}, repérez l'intégration que vous souhaitez inspecter ; il se peut qu'il y ait d'autres intégrations qui ont également été déclenchées par cette alerte. Développez le panneau d'intégration contenant les requêtes et réponses. Vous verrez le contenu complet du ou des messages sortants, les réponses renvoyées par le système externe et éventuellement des messages d'erreur qui se sont produits en cas de problème lors de l'envoi du message d'alerte.
