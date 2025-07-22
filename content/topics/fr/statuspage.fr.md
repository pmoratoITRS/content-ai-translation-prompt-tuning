{
"hero": {
"title": "Recevoir des alertes dans Statuspage"
},
"title": "Statuspage",
"summary": "Découvrez les étapes à suivre pour configurer l'envoi de notifications d'alerte d'Uptrends vers Statuspage. ",
"url": "/support/kb/alerter/integrations/statuspage",
"translationKey": "https://www.uptrends.com/support/kb/integrations/statuspage"
}

**Statuspage** est l'outil de communication des statuts et des incidents d'Atlassian. Cet outil vous permet de communiquer en temps réel le statut de vos pages et sites web à vos utilisateurs.  
Intégrer les alertes Uptrends dans votre environnement Statuspage, c'est très simple ! La mise en place de l'intégration entre les deux systèmes s'effectue comme suit :

1. Configuration d'un composant dans Statuspage
2. Création d'une clé API Statuspage
3. Configuration de l'intégration dans Uptrends
4. Ajout de l'intégration à une définition d'alerte dans Uptrends

Une fois que l'intégration a été configurée avec les paramètres d'alerte appropriés, votre page de statut affiche immédiatement l'état en temps réel de votre page ou ressource pour vos utilisateurs.

![](/img/content/f3be08ae-f844-41eb-be59-67b5de6b9901.png)

Dans la suite de cet article, vous trouverez des instructions détaillées sur la configuration de l'intégration.

## 1. Ajout d'un composant dans Statuspage

1. Dans votre environnement Statuspage, ajoutez un nouveau *composant* sous le menu **Components** (Composants). Donnez au nouveau composant un nom parlant et éventuellement une description. Enregistrez le composant.
2. Ouvrez le composant nouvellement créé et notez l'URL. L'URL se présente sous la forme manage.Statuspage.io/pages/{page\_id}/components/{component\_id}/edit. Nous aurons besoin du *{page\_id}* et du *{component\_id}* plus tard, alors notez-les bien.

{{< callout >}}
**Astuce :** Il est préférable de créer un composant par domaine surveillé avec Uptrends. Ainsi, vous pourrez mieux suivre les domaines qui sont opérationnels ou non à un moment donné.
{{< /callout >}}

## 2. Création d'une clé API dans Statuspage

1. En bas à gauche de l'écran, cliquez sur l'icône de l'utilisateur, et ouvrez **API info**. ![](/img/content/564d3038-8587-414a-8ebf-b863fd0cefad.png)
2. Créez une nouvelle clé API ici en cliquant sur le bouton *Create key* (Créer une clé). Donnez un nom qui convient et confirmez.
3. La clé API nouvellement créée apparaît immédiatement. N'oubliez pas de noter cette clé, car nous en aurons besoin plus tard.

Vous avez terminé la configuration de l'intégration du côté Statuspage.

## 3. Configuration de l'intégration dans Uptrends

Pour ajouter une nouvelle intégration pour Statuspage dans Uptrends, suivez ces étapes :

1. Ouvrez {{< AppElement type="menuitem" >}} Alerte > Intégrations {{< /AppElement >}}.
2. Cliquez sur {{< AppElement type="button" >}}Ajouter intégration{{< /AppElement >}} en haut à droite.
3. Choisissez Statuspage comme type d'intégration.
4. Donnez un nom à cette intégration.
5. Collez la clé API Statuspage, le Page\_Id et le Component\_Id dans les champs correspondants des {{< AppElement type="menuitem" >}}variables prédéfinies{{< /AppElement >}}.
6. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour enregistrer vos paramètres. La nouvelle intégration Statuspage apparaîtra sur la page Intégrations.

La configuration de l'intégration dans Uptrends est terminée. Vous pouvez désormais utiliser cette intégration dans vos définitions d'alerte.

{{< callout >}}
**Astuce :** La désactivation d'une définition d'intégration signifie que l'intégration ne sera pas utilisée pour les alertes. Cela peut être utile si vous souhaitez désactiver temporairement la réception d'alertes.
{{< /callout >}}

## 4. Ajout de l'intégration à une définition d'alerte dans Uptrends

En soi, une définition d'intégration ne fait rien. Pour recevoir des messages au moyen d'une intégration, vous devez la rattacher à un niveau d'escalade dans une définition d'alerte.

1. Dans le menu {{< AppElement type="menuitem" >}} Alerte > Définitions d'alerte {{< /AppElement >}}, sélectionnez l'alerte à laquelle vous souhaitez rattacher l'intégration.
2. Chaque onglet {{< AppElement type="tab" >}}Niveau d'escalade{{< /AppElement >}} contient une section **Alertes par intégrations** avec une liste des types d'intégrations disponibles. Pour comprendre comment fonctionnent les niveaux d'escalade, lisez l'article de la base de connaissances intitulé [Niveaux d'escalade des alertes]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="fr" >}}).
3. Sélectionnez la ou les intégrations à rattacher à ce niveau d'escalade. Dans ce cas-ci, sélectionnez **l'intégration personnalisée** pour Statuspage.
4. N'oubliez pas de cliquer sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour ne pas perdre vos modifications.

{{< callout >}}
**Astuce :** Chaque intégration Statuspage que vous créez affecte un seul composant Statuspage. Par conséquent, nous vous recommandons de faire correspondre chaque composant Statuspage à une intégration et à une définition d'alerte dans Uptrends.
{{< /callout >}}

**Et voilà, c'est fait !** Vous avez correctement configuré l'intégration de Statuspage.

Comme toujours, si vous avez la moindre question, n’hésitez pas à [contacter notre équipe de support](/contact).
