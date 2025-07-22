{
"hero": {
"title": "Configuration d'une page de statut protégée"
},
"title": "Configuration d'une page de statut protégée",
"summary": "Cet article vous explique comment créer une nouvelle page de statut protégée et configurer les opérateurs.",
"url": "/support/kb/dashboards-et-rapports/pages-statut/configuration-page-statut-protegee",
"translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/protected-status-page-configuration"
}

Pour créer une page de statut protégée, vous devez configurer la page en veillant à accorder les autorisations nécessaires à l'opérateur ou aux opérateurs qui doivent pouvoir la consulter. Les autorisations du nouvel opérateur doivent être limitées pour l'empêcher d'accéder à d'autres éléments qu'à la page de statut protégée (par exemple, à des moniteurs). Veuillez noter que des droits d'administrateur sont nécessaires pour gérer les opérateurs et les autorisations.

## Création d'une page de statut protégée


1. Créez une page de statut publique en suivant les instructions figurant dans l'article [Configuration d’une page de statut publique]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration" lang="fr" >}}).
2. Puisque vous créez une page de statut protégée, vérifiez que la case à cocher **Publier** dans l'onglet {{< AppElement type="tab" >}} Général {{< /AppElement >}} n'est pas cochée. Si cette case est cochée, votre page sera accessible à tout le monde.
3. Ajoutez éventuellement un logo, et modifiez les couleurs, le titre et le pied de page. La marche à suivre est présentée dans la partie [Personnalisation d’une page de statut publique]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration#customize" lang="fr" >}}).
4. Enregistrez la page de statut.
5. Dans la vue d'ensemble des pages de statut publiques, vous remarquerez que le lien *Prévisualiser* apparaît pour la nouvelle page de statut. Ce lien contient l'URL que les utilisateurs autorisés peuvent utiliser pour accéder à la page de statut.

## Création d'opérateurs ayant accès à la page de statut protégée

Vous devez créer au moins un opérateur et définir les autorisations de telle sorte que cet opérateur puisse accéder uniquement à la page de statut protégée. Veuillez noter que le statut d'administrateur est nécessaire pour ajouter des opérateurs et gérer les autorisations. De plus, vous aurez besoin de l'aide d'Uptrends pour terminer le processus :

1. Ajoutez un [nouvel opérateur]({{< ref path="support/kb/account/users/operators/operator-groups" lang="fr" >}}). Nous vous recommandons fortement de ne pas partager les nouvelles informations de connexion avec des tiers avant la fin des étapes suivantes.
2. Retirez l'autorisation *Opérateur de base*[]({{< ref path="support/kb/account/users/operators/permissions" lang="fr" >}}) au nouvel opérateur, depuis les paramètres de l'opérateur. Dans l'onglet {{< AppElement type="tab" >}} Autorisations {{< /AppElement >}} de la section **Autorisations sur tout le système**, cliquez sur le bouton {{< AppElement type="deletebutton" >}} Éteindre {{< /AppElement >}} à côté de l'autorisation *Opérateur de base*.
3. Confirmez votre choix en cliquant sur {{< AppElement type="deletebutton" >}} Éteindre {{< /AppElement >}} dans la boîte de dialogue contextuelle.
4. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} en bas de l'écran des paramètres de l'opérateur.
5. Autorisez l'opérateur à accéder à la page de statut protégée. Cette étape est effectuée par le support d'Uptrends. Veuillez [créer un ticket de support]({{< ref path="contact" lang="fr" >}}) pour la page de statut protégée. Dans votre demande, précisez le nom de la page de statut protégée et le nom de l'opérateur ou des opérateurs qui doivent y avoir accès. L'équipe de support établira cette autorisation et vous informera dès que la demande aura été traitée.
