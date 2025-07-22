{
  "hero": {
    "title": "Autorisations liées aux définitions d'alerte"
  },
  "title": "Autorisations liées aux définitions d'alerte",
  "summary": "",
  "url": "[URL_BASE_TOPICS]alerter/autorisations-definitions-alerte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans l'application Uptrends, les définitions d'alerte permettent d'indiquer quand les alertes doivent être générées, quel niveau d'escalade doit être appliqué et quels messages doivent être envoyés aux opérateurs ou aux systèmes au moyen des intégrations. Les définitions d'alerte jouent un rôle essentiel pour la surveillance et l'envoi d'alertes, et vous devez donc pouvoir décider qui peut les modifier. C'est exactement ce à quoi servent les autorisations liées aux définitions d'alerte.

Ces autorisations peuvent être définies de deux façons. Par exemple, l'autorisation **Modifier la définition d'alerte** est attribuée au niveau de la définition d'alerte, tandis que l'autorisation **Créer des définitions d'alerte** est attribuée à un opérateur ou à un groupe d'opérateurs. C'est ainsi que fonctionne le système d'autorisations d'Uptrends. Certaines autorisations sont liées à un élément (comme un moniteur ou une définition d'alerte) et certaines sont définies pour des opérateurs ou des groupes d'opérateurs.

Les autorisations attribuées dans la définition d'alerte sont décrites dans la suite de cet article. Pour en savoir plus sur l'autorisation **Créer des définitions d'alerte**, reportez-vous à l'article de la base de connaissances sur les [autorisations]([LINK_URL_1]) applicables aux opérateurs.

## Qui peut gérer les autorisations ?

D'une manière générale, les autorisations liées aux définitions d'alerte peuvent être définies et modifiées par les administrateurs.
Par ailleurs, un opérateur disposant à la fois de l'autorisation **Créer des définitions d'alerte** (attribuée à un opérateur ou un groupe d'opérateurs) et de l'autorisation **Modifier la définition d'alerte** (attribuée au niveau de la définition d'alerte) peut aussi gérer les autorisations pour cette définition spécifique.

## Types d'autorisations

### Modifier la définition d'alerte

Cette autorisation permet à l'opérateur ou au groupe d'opérateurs de modifier une définition d'alerte.

Quelques précisions :

- L'opérateur peut changer la définition d'alerte et ajouter ou supprimer des moniteurs ou des groupes de moniteurs dans cette définition d'alerte. Cette possibilité s'applique à tous les moniteurs dont l'opérateur peut afficher les données, comme cela a été défini dans les [autorisations de moniteurs]([LINK_URL_2]). Si l'opérateur n'a pas l'autorisation d'afficher des données pour un moniteur ou groupe de moniteurs donné, il ne peut pas le sélectionner dans la définition d'alerte.

- L'opérateur peut changer la définition d'alerte et ajouter ou supprimer des opérateurs ou des groupes d'opérateurs. L'opérateur ne peut apporter ces changements que pour les opérateurs ou groupes d'opérateurs dont il a le droit d'afficher les données.

- Il est possible que d'autres opérateurs ajoutent des moniteurs ou des groupes de moniteurs que vous ne pourrez pas voir car vous n'avez pas l'autorisation de consulter ces données. C'est aussi le cas pour les opérateurs ou groupes d'opérateurs. Si la définition d'alerte contient des éléments cachés, une note s'affiche pour le signaler.

- L'autorisation Modifier la définition d'alerte permet de supprimer la définition. La suppression est possible uniquement si la définition ne contient aucun élément caché (moniteurs/groupes de moniteurs ou opérateurs/groupes d'opérateurs), c'est-à-dire des éléments que vous n'avez pas l'autorisation de consulter.

## Gérer les autorisations

Les autorisations relatives aux définitions d'alerte peuvent être configurées dans la définition d'alerte ou dans le groupe d'opérateurs. Tout changement effectué à l'un de ces emplacements est répercuté sur l'autre.
### Configurer des autorisations dans un groupe d'opérateurs

1. Ouvrez le menu [SHORTCODE_1] Configuration de compte > Opérateurs, groupes et sous-comptes [SHORTCODE_2].
2. Cliquez ensuite sur [SHORTCODE_3] Afficher tous les groupes d'opérateurs [SHORTCODE_4] pour obtenir la liste des groupes d'opérateurs configurés pour votre compte.
3. Sélectionnez le groupe pour lequel vous souhaitez ajouter des autorisations et ouvrez l'onglet [SHORTCODE_5] Autorisations [SHORTCODE_6].
   ![capture d'écran de l'onglet des autorisations du groupe d'opérateurs]([LINK_URL_3])
4. Dans la section **Autorisations de définition d'alerte**, ajoutez une définition d'alerte en la sélectionnant dans la liste déroulante. Pour supprimer une définition d'alerte du groupe d'opérateurs, cliquez sur la croix à droite de son nom.
5. Cliquez sur le bouton [SHORTCODE_7] Enregistrer [SHORTCODE_8] en bas de l'écran.

### Définir ou modifier des autorisations dans la définition d'alerte

1. Ouvrez [SHORTCODE_9] Alertes > Définitions d'alerte [SHORTCODE_10].
2. Dans la liste des définitions d'alerte, cliquez sur la définition à modifier.
3. Ouvrez l'onglet [SHORTCODE_11] Autorisations [SHORTCODE_12].
4. Cliquez sur le bouton [SHORTCODE_13] Ajouter une autorisation [SHORTCODE_14].
5. Dans la boîte de dialogue contextuelle, sélectionnez le groupe d'opérateurs et l'autorisation, puis cliquez sur le bouton [SHORTCODE_15] Ajouter [SHORTCODE_16].
6. Pour supprimer une autorisation, cliquez sur [SHORTCODE_17] Supprimer [SHORTCODE_18] dans la liste **Autorisations**.
7. Cliquez sur [SHORTCODE_19] Enregistrer [SHORTCODE_20] avant de quitter la page.