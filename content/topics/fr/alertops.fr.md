{
   "hero": {
      "title": "Recevoir des alertes dans AlertOps"
   },
   "title": "AlertOps",
   "summary": "Découvrez comment intégrer vos alertes Uptrends dans AlertOps",
   "url": "/support/kb/alerter/integrations/alertops",
   "translationKey": "https://www.uptrends.com/support/kb/integrations/alertops"
}

**AlertOps** est un outil d'automatisation des opérations en temps réel. Cet outil vous permet de hiérarchiser vos incidents et d'automatiser vos processus. Les incidents majeurs peuvent être facilement gérés en mobilisant les équipes de garde et en leur fournissant les informations dont elles ont besoin.

1. Configuration de l'intégration entrante dans AlertOps
2. Configuration de l'intégration dans Uptrends
3. Ajout de l'intégration à une définition d'alerte dans Uptrends

Une fois que vous avez configuré cette intégration avec les paramètres d'alerte appropriés, vos alertes Uptrends généreront également des alertes dans AlertOps. Ci-dessous, vous pouvez voir à quoi ressemble une intégration dans AlertOps.![](/img/content/8f848598-92d3-4add-a9ca-3b483b0d0f14.png)

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Configuration de l'intégration entrante dans AlertOps

1. Dans l'interface d'AlertOps, accédez au menu *Inbound Integrations* (sous *Integrations* dans le menu de la barre latérale).
2. Ouvrez l'onglet **API**, puis cliquez sur le bouton *ADD API INTEGRATION*.
3. Dans la fenêtre suivante, cliquez sur *Uptrends* pour sélectionner l'intégration par défaut d'Uptrends.
4. Donnez à l'intégration un nom parlant et sélectionnez le ou les groupes ou utilisateurs destinataires dans les champs **Recipient Group(s)/User(s)**.

   ![](/img/content/84d3f6f8-493a-48fa-95ff-0b16acf5a634.png)
5. Cliquez sur le bouton *Save* pour enregistrer.
6. Notez **l'URL de l'API** qui est maintenant répertoriée dans l'interface d'AlertOps. Vous en aurez besoin lors de l'intégration du côté Uptrends.

Vous avez terminé la configuration de l'intégration du côté AlertOps.

{{< callout >}}
**Remarque** : AlertOps propose une intégration prédéfinie pour Uptrends, qui doit normalement être immédiatement utilisable. Cette intégration est largement personnalisable du côté d'AlertOps. À ce stade, nous vous recommandons toutefois de ne modifier aucun des paramètres avancés. Une fois que vous avez vérifié que l'intégration fonctionne, vous pourrez la personnaliser en fonction de vos besoins.
{{< /callout >}}

## 2. Configuration de l'intégration dans Uptrends

Pour ajouter une nouvelle intégration pour AlertOps dans Uptrends, procédez comme suit :

1. Ouvrez {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Cliquez sur {{< AppElement type="button" >}}Ajouter intégration{{< /AppElement >}} en haut à droite.
3. Choisissez AlertOps comme type d'intégration.
4. Donnez un nom à cette intégration.
5. Collez **l'URL d'API** d'AlertOps dans le champ correspondant dans les {{< AppElement type="menuitem" >}}variables prédéfinies{{< /AppElement >}}.
6. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour enregistrer vos paramètres. La nouvelle intégration AlertOps apparaîtra sur la page Intégrations.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration dans vos définitions d'alerte.

## 3. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu {{< AppElement type="menuitem" >}} Alerte > Définitions d'alerte {{< /AppElement >}}, sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet {{< AppElement type="tab" >}}Niveau d'escalade{{< /AppElement >}} contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="fr"  >}}).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, il s'agira de **l'intégration personnalisée** pour AlertOps.
4. N'oubliez pas de cliquer sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour ne pas perdre vos modifications.

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration pour AlertOps.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support](/contact).
