{
  "hero": {
    "title": "Périodes de maintenance"
  },
  "title": "Périodes de maintenance",
  "summary": "Les périodes de maintenance vous permettent de désactiver temporairement vos alertes ou vos moniteurs pour ne plus recevoir les alertes.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/gestion-moniteurs/periodes-de-maintenance",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Il est probable que vous ne vouliez pas recevoir d'alerte lorsque vos serveurs, sites web ou services web sont hors service en raison d'une maintenance planifiée. Par exemple, cela peut être le cas lorsque votre équipe effectue une maintenance de routine sur le site web, les serveurs web ou le service web de votre entreprise. Pendant cette période, la fluctuation de la disponibilité et des performances risque de déclencher l'envoi d'alertes par vos moniteurs.

## Périodes de maintenance

En définissant une période de maintenance pour vos moniteurs, vous pouvez configurer à l'avance des dates et des heures spécifiques, et décider si vous souhaitez désactiver temporairement vos alertes ou vos moniteurs pour éviter de recevoir des erreurs :

![Périodes de maintenance pour un moniteur]([LINK_URL_1])


Lors de la configuration d'une période de maintenance, vous pouvez définir la récurrence dont vous avez besoin. La récurrence peut se configurer une seule fois, une fois par jour, une fois par semaine ou une fois par mois. Si vos serveurs sont programmés pour être hors ligne le dernier jour du mois, vous pouvez aussi gérer le nombre d'alertes que vous recevez à cette date. Pour en savoir plus, lisez le paragraphe sur la configuration d'une [récurrence le dernier jour du mois]([LINK_URL_2]).

Lors de la configuration d'une période de maintenance, Uptrends utilise l'heure et la date de votre compte principal. La date et l'heure de l'ordinateur local (sur lequel vous modifiez la période de maintenance) ne sont pas prises en compte. Ce fonctionnement simplifie la collaboration entre les opérateurs situés sur différents fuseaux horaires, car les périodes de maintenance dépendent d'un seul système de date et d'heure, à savoir celui du compte Uptrends.

### Créer une période de maintenance

Les périodes de maintenance sont propres à chaque moniteur. Pour définir votre maintenance planifiée :

1. Ouvrez le menu [SHORTCODE_5] Surveillance > Configuration du moniteur [SHORTCODE_6].
2. Cliquez pour sélectionner et ouvrir les paramètres du moniteur pour lequel la maintenance doit être programmée.
3. Ouvrez l'onglet [SHORTCODE_7]Périodes de maintenance[SHORTCODE_8].
4. Cliquez sur le bouton [SHORTCODE_9]Ajouter une nouvelle période de maintenance[SHORTCODE_10].

![Configuration d'une période de maintenance]([LINK_URL_3])

5. Ajoutez éventuellement une description de votre période de maintenance.
6. Définissez le type de **Récurrence** (*une fois, journalière, hebdomadaire, mensuelle*).
7. Renseignez les champs **Du** et **Jusqu'au**. Ces options dépendent de votre choix de **Récurrence** à l'étape précédente.
8. Indiquez si vous voulez désactiver uniquement les alertes ou désactiver complètement le moniteur dans la liste **Type de maintenance**.
9. Cliquez sur le bouton [SHORTCODE_11] Définir [SHORTCODE_12].
10. Cliquez sur le bouton [SHORTCODE_13]Enregistrer[SHORTCODE_14] en bas à gauche pour enregistrer les modifications que vous venez d'apporter aux paramètres du moniteur.

### Désactiver les alertes ou toute la surveillance

La fenêtre **Ajouter une période de maintenance** vous permet de choisir un **type de maintenance** : **Désactiver seulement les notifications** ou **Entièrement désactiver la surveillance**.

- Si vous choisissez de désactiver toutes les notifications, la surveillance se poursuivra et les erreurs survenues seront toujours affichées dans le journal des événements, mais aucune alerte ne sera envoyée.
- Si vous choisissez de désactiver entièrement la surveillance, aucune surveillance n'aura lieu et, par conséquent, aucune erreur ne sera enregistrée ni aucune alerte générée.

### Récurrence le dernier jour du mois [ANCHOR_1]

Pour configurer une période de maintenance pour le dernier jour du mois, procédez comme suit :
![Configuration d'une période de maintenance pour le dernier jour du mois]([LINK_URL_4])
1. Créez une nouvelle période de maintenance comme décrit ci-dessus.
2. Sélectionnez l'option Mensuelle dans le menu déroulant **Récurrence**.
3. Dans le champ **Le jour**, sélectionnez 31, puis cliquez sur [SHORTCODE_15]Définir[SHORTCODE_16]
4. Cliquez sur le bouton [SHORTCODE_17]Enregistrer[SHORTCODE_18] pour enregistrer les modifications que vous venez d'apporter aux paramètres du moniteur.

[SHORTCODE_1] **Remarque** : Même si un mois contient moins de 31 jours, la maintenance aura lieu le dernier jour de chaque mois.   [SHORTCODE_2]

#### Configuration efficace des périodes de maintenance à l'aide de modèles de moniteur

Si vous souhaitiez planifier la maintenance de plusieurs moniteurs à la fois, vous pouvez utiliser un [modèle de moniteur]([LINK_URL_5]).

## Vue d'ensemble des périodes de maintenance

Si vous souhaitez revoir les périodes de maintenance créées par vous ou un collègue, ouvrez dans le menu *Configuration de compte > Périodes de maintenance*, ou cliquez sur **Sélectionner toutes les périodes similaires** dans l'onglet [SHORTCODE_19] Périodes de maintenance [SHORTCODE_20] du moniteur.

La liste **Périodes de maintenance** montre toutes les périodes de maintenance dans votre compte. Vous pouvez ainsi vérifier et supprimer les périodes indésirables et faire du tri. Par défaut, cette liste affiche les périodes de maintenance pour tous vos moniteurs. Vous pouvez utiliser le filtre de moniteur [SHORTCODE_21] Tous les moniteurs [SHORTCODE_22] pour rendre votre sélection plus spécifique.

![Vue d'ensemble des périodes de maintenance]([LINK_URL_6])

Les périodes de maintenance peuvent être facilement filtrées au moyen d'un menu déroulant. Vous avez le choix entre plusieurs filtres : **Toutes les périodes**, **Périodes uniques** et **Périodes récurrentes**. Vous pouvez aussi filtrer les périodes en saisissant leur description dans la barre de recherche prévue à cet effet. D'autres [tuiles]([LINK_URL_7]) peuvent être paramétrées en cliquant sur le bouton [SHORTCODE_23] ... [SHORTCODE_24] en haut à droite.

[SHORTCODE_3] **Remarque** : Les administrateurs et les opérateurs disposant de [droits de modification des paramètres]([LINK_URL_8]) pour au moins un moniteur ont accès à la vue d'ensemble des **périodes de maintenance**. Ces opérateurs peuvent consulter les périodes de maintenance, mais aussi [supprimer les périodes de maintenance passées]([LINK_URL_9]) ou [toutes les périodes de maintenance]([LINK_URL_10]) pour les moniteurs pour lesquels ils disposent de **droits de modification**. [SHORTCODE_4]

### Supprimer les périodes de maintenance passées

1. Sélectionnez *Périodes uniques* ou *Périodes récurrentes* en cliquant sur le bouton des paramètres [SHORTCODE_25] … [SHORTCODE_26] dans le coin supérieur droit, puis cliquez sur [SHORTCODE_27] Définir [SHORTCODE_28].
   ![Choix des périodes à afficher]([LINK_URL_11])
2. Cliquez sur le bouton [SHORTCODE_29]Nettoyer[SHORTCODE_30].
3. La fenêtre de dialogue **Nettoyer** affichera le nombre de périodes révolues.
4. Cliquez sur [SHORTCODE_31]Ok[SHORTCODE_32] pour supprimer toutes les périodes passées sélectionnées.

### Supprimer toutes les périodes de maintenance

Voici comment supprimer toutes les périodes de maintenance en cours :

1. Sélectionnez *Périodes uniques* ou *Périodes récurrentes* en cliquant sur le bouton des paramètres [SHORTCODE_33] … [SHORTCODE_34] dans le coin supérieur droit, puis cliquez sur [SHORTCODE_35] Définir [SHORTCODE_36].
2. Cliquez sur le bouton [SHORTCODE_37]Supprimer tout[SHORTCODE_38].
3. La fenêtre de dialogue **Supprimer tout** affiche le nombre de périodes sélectionnées qui seront supprimées (toutes les périodes sont sélectionnées et seront supprimées).
4. Cliquez sur [SHORTCODE_39]Ok[SHORTCODE_40] pour supprimer toutes les périodes de maintenance.
