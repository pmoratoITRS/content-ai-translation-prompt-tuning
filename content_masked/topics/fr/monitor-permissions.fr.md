{
  "hero": {
    "title": "Autorisations de moniteurs"
  },
  "title": "Autorisations de moniteurs",
  "summary": "Comment configurer les autorisations des moniteurs pour vos opérateurs ou groupes d'opérateurs.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/autorisations-moniteurs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]Les autorisations de moniteurs ne sont disponibles que pour les abonnés **Enterprise**.[SHORTCODE_2]

Par défaut, tous les [opérateurs de base]([LINK_URL_1]) dans votre compte peuvent afficher les données de surveillance (dashboards, statistiques, résultats de vérification) pour tous vos moniteurs. Par contre, ils ne peuvent pas modifier ou supprimer les moniteurs existants, ni en créer de nouveaux. Ces actions ne sont, par défaut, disponibles que pour les [administrateurs]([LINK_URL_2]) (membres du groupe d'opérateurs *Administrateurs*).

Pour un contrôle plus précis sur les opérateurs et ce qu'ils sont autorisés à faire dans votre compte, les abonnés Enterprise peuvent mettre en place des **autorisations**. En bref, une autorisation de moniteur est une règle qui s'applique à un moniteur ou à un groupe de moniteurs, qui détermine le niveau d'accès d'un opérateur ou d'un groupe d'opérateurs pour ce moniteur ou ce groupe de moniteurs.

Ceci s'applique uniquement aux moniteurs de votre compte. Pour en savoir plus sur les **autorisations des opérateurs** comme la possibilité de passer des commandes, de consulter des factures, d'accéder à l'abonnement Uptrends Infra, etc., consultez notre article sur les [autorisations des opérateurs]([LINK_URL_3]).

## Configuration des autorisations de moniteurs

Les autorisations de moniteurs peuvent s'appliquer aux [groupes de moniteurs]([LINK_URL_4]) ou aux moniteurs individuels. Elles peuvent être définies dans les paramètres du moniteur ou du groupe de moniteurs, mais vous pouvez aussi les attribuer directement dans les paramètres des [groupes d'opérateurs]([LINK_URL_5]).

#### Pour configurer des autorisations dans les paramètres d'un groupe d'opérateurs :

1. Ouvrez la vue d'ensemble [Groupes d'opérateurs]([LINK_URL_6]) (en cliquant sur le lien ou via le menu *Configuration de compte > Opérateurs, groupes et sous-comptes*) et sélectionnez le groupe d'opérateurs auquel vous souhaitez attribuer des autorisations de moniteurs.
2. Le paramètre **Permissions de moniteur** est accessible dans l'onglet [SHORTCODE_3] Autorisations [SHORTCODE_4].
3. Si nécessaire, ajoutez le groupe de moniteurs ou le moniteur auquel vous souhaitez attribuer une autorisation.
4. Choisissez le niveau d'autorisation souhaité en déplaçant le curseur (les différents niveaux sont visibles dans l'image ci-dessous).
   ![Permissions de moniteur par groupe d'opérateurs]([LINK_URL_7])
5. N'oubliez pas de cliquer sur [SHORTCODE_5] Enregistrer [SHORTCODE_6] en bas à gauche de l'écran !

Dans l'exemple ci-dessus, les membres du groupe d'opérateurs peuvent créer et supprimer des moniteurs dans le *groupe de moniteurs A*, afficher les données de *tous les moniteurs* du compte, et modifier les paramètres d'un moniteur appelé *Example SSL Cert monitor*.

#### Pour définir des autorisations dans les paramètres d'un moniteur ou d'un groupe de moniteurs :

1. Affichez le [groupe de moniteurs]([LINK_URL_8]) ou le moniteur pour lequel vous souhaitez configurer des autorisations.
2. Cliquez sur l'onglet [SHORTCODE_7] Autorisations [SHORTCODE_8] pour voir les autorisations actuellement définies pour ce groupe ou ce moniteur. Le groupe d'opérateurs *Administrateurs* aura toujours l'autorisation **Créer et supprimer des moniteurs dans le groupe**, qui ne peut pas être supprimée. Par défaut, le groupe d'opérateurs *Tout le monde* aura l'autorisation **Afficher les données du moniteur dans le groupe**.
3. Pour supprimer une autorisation existante, cliquez sur le bouton Supprimer sur le côté droit. Ensuite, passez à l’étape 7.
4. Pour créer une nouvelle autorisation, cliquez sur **Ajouter une autorisation** dans le coin supérieur droit. Pour modifier une autorisation existante, cliquez sur le bouton **Éditer**.
5. Sélectionnez l’autorisation que vous souhaitez attribuer. Une présentation des types d’autorisations disponibles est donnée au-dessous. Si vous créez une nouvelle autorisation, sélectionnez d’abord l’opérateur individuel ou le groupe d’opérateurs auquel vous souhaitez accorder l’autorisation.
6. Cliquez sur **Ajouter** ou **Mettre à jour**, selon que vous ajoutez une nouvelle autorisation ou que vous mettez à jour une autorisation existante.
7. N'oubliez pas de cliquer sur [SHORTCODE_9] Enregistrer [SHORTCODE_10] en bas à gauche de l'écran !

### Application des autorisations de moniteurs au groupe "Tous les moniteurs"

Lorsqu'un nouveau moniteur est créé, il est automatiquement ajouté au groupe *Tous les moniteurs* (comme l'indique le nom de ce groupe). Cependant, par défaut, les opérateurs standard (non administrateurs) n'auront pas l'autorisation nécessaire pour créer ou supprimer des moniteurs dans le groupe *Tous les moniteurs*. Autrement dit, un opérateur qui n'aurait pas été expressément autorisé à créer des moniteurs dans le groupe *Tous les moniteurs* ne pourrait jamais rien créer. Pour éviter cela, lors de la création d'un nouveau moniteur, l'ajout au groupe *Tous les moniteurs* est ignoré dès lors que le moniteur est ajouté à un autre groupe au moins.

Par exemple, prenons le cas d'un opérateur qui n'aurait pas d'autorisation pour le groupe *Tous les moniteurs*, mais qui aurait une permission de création/suppression pour un *groupe de moniteurs A*. Cet opérateur pourra afficher et modifier les moniteurs existants dans un groupe A, et créer de nouveaux moniteurs dans ce groupe. En revanche, il ne pourra pas afficher ni modifier les moniteurs en dehors du *groupe de moniteurs A*.

Pour créer un nouveau moniteur, cet opérateur doit l'ajouter à l'un des groupes de moniteurs pour lesquels il dispose des autorisations nécessaires.

![Groupe Tous les moniteurs]([LINK_URL_9])

Le moniteur sera créé en tant que membre du *groupe de moniteurs A* et du groupe *Tous les moniteurs*, sans que cela nécessite d'attribuer expressément une autorisation de création/suppression pour ce dernier.

## Types d'autorisations [ANCHOR_1]

Les types d'autorisations suivants sont disponibles :

- **Afficher les données des moniteurs du groupe** : les opérateurs qui disposent de cette autorisation pourront seulement afficher les données de moniteur pour ce groupe de moniteurs. Les données de moniteurs comprennent les dashboards, les statistiques et les résultats des vérifications. Les paramètres du moniteur ne sont **pas** compris.
- **Afficher les paramètres des moniteurs du groupe** : cette autorisation concerne les données du moniteur, mais inclut également les paramètres du moniteur. Avec cette autorisation, les opérateurs peuvent consulter les paramètres du moniteur ou du groupe de moniteurs applicable. Ces paramètres comprennent l'intervalle de surveillance, le mode, la sélection du checkpoint, les périodes de maintenance, etc. Avec cette autorisation, ces paramètres sont en **lecture seule**, et ne peuvent pas être modifiés.
- **Modifier les paramètres des moniteurs du groupe** : permet aux opérateurs disposant de cette autorisation d'apporter des modifications aux moniteurs contenus dans le groupe de moniteurs pour lequel cette autorisation est définie. Avec cette autorisation, les opérateurs peuvent activer ou désactiver le moniteur, modifier l'intervalle, modifier le checkpoint, ajouter des périodes de maintenance, etc.
- **Créer et supprimer des moniteurs dans le groupe** : cette autorisation, qui est la plus élevée pouvant être attribuée, donne à un opérateur des privilèges administratifs pour des groupes de moniteurs spécifiques. Cet opérateur pourra créer de nouveaux moniteurs (mais uniquement dans le groupe de moniteurs assigné) ou supprimer des moniteurs existants. Cette autorisation n'est disponible que pour les groupes de moniteurs et ne peut pas être attribuée à des moniteurs individuels.

Il est à noter que ces autorisations sont cumulatives. Chaque nouveau niveau d'autorisation contient toutes les autorisations des niveaux précédents. Par exemple, un opérateur avec l'autorisation *Afficher les paramètres des moniteurs du groupe* peut également afficher automatiquement les données des moniteurs.

![Exemples d'autorisations]([LINK_URL_10])

Dans l'image ci-dessus (pour un *Exemple de groupe de moniteurs* ou Example monitor group), le groupe d'opérateurs *Tout le monde* (Everyone) ne peut afficher que les données des moniteurs, c'est-à-dire les dashboards, les statistiques et les résultats des vérifications individuelles. Le groupe d'opérateurs *Exemple de groupe d'opérateurs* peut afficher les données des moniteurs et modifier les paramètres des moniteurs existants au sein de ce groupe. Le groupe d'opérateurs *Administrateurs* (Administrators) dispose des autorisations CRUD complètes pour les moniteurs contenus dans le groupe de moniteurs *Exemple de groupe de moniteurs*.

## Groupe de moniteurs par défaut [ANCHOR_2]

Par définition, chaque moniteur de votre compte est membre du groupe *Tous les moniteurs*[]([LINK_URL_11]). Les moniteurs ne peuvent pas être retirés de ce groupe. Bien que généralement pertinent, ce paramètre n'est pas toujours idéal pour attribuer les autorisations dont vous avez besoin.

Toute autorisation que vous attribuez au groupe Tous les moniteurs s'applique à tous les moniteurs de votre compte. Cependant, vous pouvez avoir besoin d'appliquer une autorisation à *presque tous* les moniteurs de votre compte. Par exemple, si un [groupe d'opérateurs]([LINK_URL_12]) donné doit pouvoir modifier les paramètres de tous les moniteurs de votre compte à l'exception de quelques-uns, attribuer l'autorisation "Modifier les paramètres des moniteurs" au groupe "Tous les moniteurs" ne fonctionnerait pas (car le groupe d'opérateurs aurait la possibilité de modifier chaque moniteur, y compris ceux qu'il ne doit pas pouvoir modifier).

Pour remédier à cela, vous pouvez définir un **Groupe de moniteurs par défaut**. Ce groupe de moniteurs personnalisé est similaire au groupe Tous les moniteurs, sauf que des moniteurs peuvent être retirés de ce groupe. Une fois que vous avez configuré un groupe de moniteurs par défaut, chaque nouveau moniteur est automatiquement ajouté à ce groupe (en plus du groupe Tous les moniteurs) et reçoit donc les mêmes autorisations sans autre intervention manuelle.

Toute autorisation que vous souhaitez appliquer à presque tous les moniteurs peut être attribuée au groupe de moniteurs par défaut, plutôt qu'au groupe Tous les moniteurs.

Pour configurer un groupe de moniteurs par défaut :

1. Utilisez un groupe de moniteurs existant ou créez un nouveau groupe.
2. Assurez-vous que ce groupe contient tous les moniteurs concernés par votre autorisation. Notre [commande d'API MonitorGroup]([LINK_URL_13]) peut vous être utile pour ajouter des lots de moniteurs à ce groupe.
3. Ouvrez vos paramètres de compte en cliquant sur [SHORTCODE_11] Configuration de compte > Paramètres de compte [SHORTCODE_12] dans le menu.
4. Sélectionnez le groupe de moniteurs dans la liste déroulante, au niveau de l'option **Groupe de moniteurs par défaut**.
   ![Paramètres du groupe de moniteurs par défaut]([LINK_URL_14])
5. Cliquez sur [SHORTCODE_13] ENREGISTRER [SHORTCODE_14] pour enregistrer vos changements.

