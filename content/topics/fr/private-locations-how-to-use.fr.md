{
"hero": {
"title": "Comment utiliser les checkpoints des emplacements privés"
},
"title": "Comment utiliser les checkpoints des emplacements privés",
"summary": "Découvrez comment configurer la surveillance et tenir à jour vos emplacements privés et vos checkpoints privés après l'installation.",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/protection-donnees-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-how-to-use"
}

Lorsque vous ajoutez un [emplacement privé]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="fr" >}}), deux points de contrôle sont créés par défaut. Vous pouvez sélectionner les checkpoints de votre emplacement privé depuis l'application Uptrends, afin de les inclure dans votre système de surveillance quotidien. Vous devrez attribuer le checkpoint à vos nouveaux moniteurs ou aux moniteurs existants sur la page Configuration du moniteur.

Pour modifier les paramètres d'un checkpoint ou de l'emplacement privé, vous passerez par la page Emplacement privé. L'emplacement privé contient vos checkpoints. Lorsque vous retirez un checkpoint, cela ne supprime pas l'emplacement privé. Si vous supprimez un emplacement privé, cela supprime tout l'emplacement et ses checkpoints.

## Commencer à utiliser un checkpoint
Les checkpoints ne sont pas utilisés par défaut ou automatiquement. Si vous voulez utiliser un ou des checkpoints sur votre emplacement privé, vous devez d'abord les ajouter à la liste de sélection de checkpoints de votre moniteur.

Pour associer un checkpoint à un moniteur :
1. Dans l'application Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Trouvez le nom du checkpoint que vous souhaitez utiliser et cliquez sur le lien correspondant dans la colonne *Nom de moniteur*. (Notez qu'il n'est pas nécessaire de sélectionner les nouveaux moniteurs d'API multi-étapes à cette étape, car ces derniers sont liés à votre checkpoint privé.)
3. La page de configuration du moniteur s'ouvre, avec tous les onglets de paramétrage du moniteur. Dans l'onglet {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}}, sélectionnez tous les checkpoints de votre emplacement privé ou l'un de vos checkpoints privés. (Vous pouvez sélectionner ce checkpoint pour tous les moniteurs que vous créez.)
   ![capture d'écran des checkpoints privés d'un moniteur](/img/content/scr_private-location-checkpoints-tab-monitor.min.png)
4. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour conserver tous les changements apportés au moniteur.

## Gérer les emplacements privés

Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}. Sur cette page, vous pouvez gérer les checkpoints de votre emplacement privé.

### Renommer un emplacement privé

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur l'icône de modification (en forme de crayon).
3. Saisissez le nouveau nom et pressez la touche Entrée.

### Supprimer un emplacement privé

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton de suppression (corbeille).
3. Vérifiez que l'emplacement privé sélectionné et les checkpoints liés ont été supprimés.
4. Facultatif : vous pouvez aussi supprimer la machine virtuelle (dédiée) avec les checkpoints sélectionnés.

### Supprimer un checkpoint

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} et sélectionnez *Supprimer le point de contrôle*. Vous pouvez aussi cliquer sur le nom du checkpoint, l'ouvrir et cliquer sur le bouton gris *Supprimer le point de contrôle*.
3. Vérifiez que le checkpoint sélectionné a bien été supprimé.

### Désactiver un checkpoint

Lorsque vous désactivez un checkpoint privé, ce dernier n'est plus disponible pour effectuer des vérifications.

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} et sélectionnez *Désactiver le point de contrôle*. Vous pouvez aussi cliquer sur le nom du checkpoint, l'ouvrir et cliquer sur le bouton gris *Désactiver le point de contrôle*.
3. Indiquez pourquoi vous désactivez ce checkpoint.
4. Confirmez la désactivation en cliquant sur {{< AppElement type="deletebutton" >}} Désactiver {{< /AppElement >}} .

### Activer un checkpoint privé

1. Dans l'application Uptrends, ouvrez {{< AppElement type="menuitem" >}} Emplacements privés {{< /AppElement >}}.
2. Cliquez sur le bouton {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} et sélectionnez *Activer le point de contrôle*. Vous pouvez aussi cliquer sur le nom du checkpoint, l'ouvrir et cliquer sur le bouton gris *Activer le point de contrôle*.
3. Confirmez l'activation du checkpoint sélectionné en cliquant sur {{< AppElement type="savebutton" >}} Activer {{< /AppElement >}} .

## Onglets relatifs aux checkpoints privés

### Santé du point de contrôle
Si vous souhaitez suivre l'état de votre checkpoint, l'onglet [Santé du point de contrôle]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="fr" >}}) vous donne un aperçu des principales métriques le concernant. Il contient des informations sur le logiciel installé, les paramètres de [protection des données]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}) et des métriques relatives à l'hôte.

### Installation du checkpoint

Utilisez le guide d'installation pour configurer vos points de contrôle privés dans Docker. Pour plus d'informations, listez l'article sur [l'installation d'un checkpoint géré par l'utilisateur]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}).

### Comment utiliser ce point de contrôle

L'onglet {{< AppElement type="tab" >}} Comment utiliser ce point de contrôle {{< /AppElement >}} vous explique rapidement comment utiliser la page de configuration pour configurer vos moniteurs. Il ne s'affiche que si aucun contrôle n'a encore été effectué par ce checkpoint.


## Gérer votre propre emplacement privé
### Ajouter des moniteurs à votre compte

Il est important de vérifier qu'un point de contrôle privé est toujours disponible dans votre compte pour effectuer les vérifications sur votre emplacement privé. En l'absence de point de contrôle, Uptrends n'est pas capable de détecter les problèmes sur vos sites. Si aucune vérification n'est effectuée, aucune erreur n'est repérée et aucune alerte n'est envoyée.

Pour recevoir des alertes sur les perturbations touchant votre réseau de checkpoints privés, les moniteurs suivants devront être créés. La [création d'une définition d'alerte ]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}) vous permet de vous assurer que les bonnes personnes sont informées lorsqu'un checkpoint privé ne fonctionne pas.

| **Nom du moniteur** | **Type** |
|-------------------------------------------------------|----------------|
| "checkpoint `<nom du premier checkpoint>` health" | Multi-step API |
| "checkpoint `<nom du deuxième checkpoint>` health" | Multi-step API |
| "region `<nom de l'emplacement privé>` health" | Multi-step API |

### Ajouter de nouveaux moniteurs

Lorsque vous ajoutez de nouveaux moniteurs à votre compte Uptrends, pensez à les configurer dans votre pare-feu.