{
"hero": {
"title": "Recevoir des alertes de surveillance dans Microsoft Teams"
},
"title": "Intégration à Microsoft Teams",
"summary": "Recevez les alertes de surveillance de site web d'Uptrends dans Microsoft Teams.",
"url": "/support/kb/alerter/integrations/microsoft-teams",
"translationKey": "https://www.uptrends.com/support/kb/integrations/microsoft-teams"
}

**Microsoft Teams** est le point central du travail d'équipe dans Microsoft 365. Dans Teams, vous pouvez communiquer (par messagerie instantanée, appel ou vidéo) et partager des informations (fichiers, agendas, etc.). L'intégration de Microsoft Teams permet de recevoir des notifications automatiques de la part d'Uptrends. La mise en place de l'intégration entre les deux systèmes s'effectue comme suit :

1. Configuration d’un *workflow* dans Microsoft Teams
2. Configuration de l'intégration dans Uptrends
3. Ajout de l'intégration à une définition d'alerte dans Uptrends

Vous vous demandez ce que cela donne une fois l'intégration configurée ? Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans Microsoft Teams.

![Exemple d'alerte dans Teams](/img/content/scr-teams-integration-alert-example.min.png)

Dans le canal Microsoft Teams pour lequel l'intégration a été définie, vous recevrez un message contenant des informations détaillées sur l'alerte générée. À partir de ce message, vous pouvez accéder directement au dashboard, à l'erreur ou au moniteur dans Uptrends pour obtenir plus de détails et approfondir la recherche. Il vous suffit d'appuyer sur l'un des boutons pour arriver au bon endroit dans l'application Uptrends.

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Configuration d’un workflow dans Microsoft Teams

1. Dans Microsoft Teams, ouvrez le canal sur lequel vous souhaitez recevoir des messages d'Uptrends. Passez la souris au-dessus du canal pour voir apparaître {{< AppElement type="menuitem" >}}Plus d'options{{< /AppElement >}} (…). Sélectionnez {{< AppElement type="menuitem" >}}Workflows{{< /AppElement >}}.  
   ![Ajout d'un worklow](/img/content/scr-teams-integration-add-workflow.min.png)
2. Sélectionnez l'option *Publier dans une conversation lors de la réception d’une demande de webhook*.
3. Saisissez un nom pour le workflow.
4. Cliquez sur *Suivant*.
5. Vérifiez les paramètres de **l'équipe Microsoft Teams** et du **canal Microsoft Teams**, et cliquez sur *Ajouter un workflow*.
5. Le workflow devrait être créé après quelques secondes. Une URL s'affiche au bas du formulaire :  
   ![URL du workflow dans Teams](/img/content/scr-teams-integration-workflow-added.min.png)
6. Copiez l'URL et enregistrez-la quelque part. Vous en aurez besoin plus tard pour configurer l'intégration dans Uptrends.
7. Cliquez sur {{< AppElement type="menuitem" >}}Terminé{{< /AppElement >}}.

La configuration de l'intégration dans Microsoft Teams est terminée.

## 2. Configuration de l'intégration dans Uptrends

Pour ajouter une nouvelle intégration Microsoft Teams dans Uptrends, procédez comme suit :

1. Ouvrez {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Cliquez sur {{< AppElement type="button" >}}Ajouter intégration{{< /AppElement >}} en haut à droite.
3. Choisissez Microsoft Teams comme type d'intégration.  
   ![](/img/content/9df05fe6-c315-4a7c-89d9-f4e2bf8344bf.png)
4. Donnez un nom à cette intégration.
5. Collez l'URL du webhook Microsoft Teams (que vous avez copiée précédemment) dans {{< AppElement type="menuitem" >}}Variables prédéfinies > WorkflowUrl{{< /AppElement >}}.
6. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour enregistrer vos paramètres. La nouvelle intégration Microsoft Teams apparaîtra sur la page Intégrations.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration dans vos définitions d'alerte.

{{< callout >}}
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous souhaitez désactiver temporairement la réception d'alertes.
{{< /callout >}}

## 3. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu {{< AppElement type="menuitem" >}} Alerte > Définitions d'alerte {{< /AppElement >}}, sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet {{< AppElement type="tab" >}}Niveau d'escalade{{< /AppElement >}} contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="fr" >}}).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, il s'agira de **l'intégration personnalisée** pour Microsoft Teams.
4. N'oubliez pas de cliquer sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration pour Microsoft Teams.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support](/contact).
