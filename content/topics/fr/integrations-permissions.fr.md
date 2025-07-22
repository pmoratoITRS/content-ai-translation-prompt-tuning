{
"hero": {
"title": "Autorisations liées aux intégrations"
},
"title": "Autorisations liées aux intégrations",
"summary": "Gérer les autorisations accordées aux opérateurs pour les intégrations",
"url": "/support/kb/alerter/integrations/autorisations-integrations",
"translationKey": "https://www.uptrends.com/support/kb/integrations/integrations-permissions"
}

{{< callout >}} Les autorisations liées aux intégrations sont disponibles uniquement pour les comptes **Enterprise**.{{< /callout >}}

Les intégrations permettent de définir les canaux de communication à utiliser pour envoyer les messages d'alerte. Leur configuration se fait dans les niveaux d'escalade des définitions d'alerte.
Les autorisations liées aux intégrations vous permettent de décider quels opérateurs ont le droit de créer, modifier ou utiliser les intégrations dans les alertes de définition.

## Qui peut gérer les autorisations ?

Les administrateurs (membres du groupe d'opérateurs Administrateurs) peuvent toujours créer, utiliser et modifier les intégrations. Ils peuvent aussi configurer et modifier les autorisations liées aux intégrations.

Par ailleurs, un opérateur disposant à la fois de l'autorisation **Créer des intégrations** (attribuée à un opérateur ou un groupe d'opérateurs) et de l'autorisation **Modifier l'intégration** (attribuée au niveau de l'intégration) peut aussi gérer les autorisations des intégrations qu'il a créées.
## Types d'autorisations

Les autorisations sont gérées au niveau de l'opérateur ou du groupe d'opérateurs, au niveau de l'intégration elle-même.

### Créer une intégration

L'autorisation **Créer des intégrations** s'applique à un opérateur ou à un groupe d'opérateurs. Pour comprendre le fonctionnement de ces autorisations, consultez l'article de la base de connaissances [Autorisations]({{< ref path="support/kb/account/users/operators/permissions#create-integration" lang="fr" >}}).

### Utiliser l'intégration

L'autorisation **Utiliser l'intégration** permet à l'opérateur d'utiliser l'intégration dans les niveaux d'escalade d'une définition d'alerte. Dans la liste d'intégrations figurant dans les onglets des niveaux d'escalade (d'une définition d'alerte), vous verrez toutes les intégrations pour lesquelles vous avez l'autorisation **Utiliser l'intégration**.

Cette autorisation ne donne pas accès à l'intégration elle-même. Vous ne la verrez pas dans la liste des intégrations accessibles via le menu ({{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}).

L'intégration **Alertes par e-mail** est accessible à tous les membres du groupe d'opérateurs **Tout le monde**. Ainsi, vous pouvez choisir au moins une intégration, si vous avez le droit d'accès à une définition d'alerte mais pas de droit d'accès aux intégrations. L'intégration **Alertes par e-mail** est disponible sans coût supplémentaire, tandis que les intégrations Alertes par SMS utilisent des [crédits SMS]({{< ref path="support/kb/alerting/sms-credit-usage" lang="fr" >}}).

Vous utilisez des appels d'API pour obtenir des informations sur les intégrations ? Une requête GET vous donnera toutes les intégrations pour lesquelles vous avez l'autorisation **Utiliser l'intégration**. Ainsi, vous pouvez récupérer l'identifiant `GUID` de l'intégration, qui est nécessaire pour ajouter l'intégration à une définition d'alerte au moyen d'une API. La requête renvoie le nom, le type et l'identifiant `GUID` de l'intégration.

### Modifier l'intégration {id="edit-integration"}

Cette autorisation est plus avancée que l'option **Utiliser l'intégration**, car elle vous donne le droit de modifier l'intégration. De fait, l'autorisation **Modifier l'intégration** inclut l'autorisation **Utiliser l'intégration**. Il n'est donc pas nécessaire d'attribuer les deux autorisations.

Si vous avez l'autorisation **Modifier l'intégration** pour une intégration, celle-ci s'affichera dans la liste d'intégrations accessible via le menu ({{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}).

Cette autorisation inclut le droit de supprimer l'intégration

## Gérer les autorisations

Pour définir ou modifier des autorisations :

1. Ouvrez {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Dans la liste des intégrations, cliquez sur l'intégration à modifier.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}}.
4. Cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter une autorisation {{< /AppElement >}}.
5. Dans la boîte de dialogue contextuelle, sélectionnez le groupe d'opérateurs (ou l'opérateur) et le type d'autorisation, puis cliquez sur le bouton {{< AppElement type="buttonPrimary" >}} Ajouter {{< /AppElement >}}.
6. Pour supprimer une autorisation, cliquez sur {{< AppElement type="deletebutton" >}} Supprimer {{< /AppElement >}} dans la liste **Autorisations**.
7. Cliquez sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de la page avant de quitter.