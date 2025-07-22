{
  "hero": {
    "title": "Moniteurs de Serveur E-mail"
  },
  "title": "Moniteurs de Serveur E-mail",
  "summary": "Avec les moniteurs SMTP et POP3 d'Uptrends, vous serez le premier au courant à propos des problèmes de serveur e-mail.",
  "url": "/support/kb/surveillance-synthetique/uptime-monitoring/moniteurs-de-serveur-e-mail",
  "translationKey": "https://www.uptrends.com/support/kb/mail-server-monitors",
  "tableofcontents": true
}

Vous avez entendu le vieux dicton : «Ni la neige, ni la pluie, ni la chaleur, ni l'obscurité de la nuit n'empêcheront ces courriers d'achever rapidement leurs rondes." Le courrier est important pour vous et votre entreprise, mais tout aussi importants sont le bon fonctionnement et la disponibilité de vos serveurs de messagerie. Si votre serveur de messagerie tombe en panne, même pour un court laps de temps, la panne pourrait porter préjudice  à votre entreprise, en productivité, en réputation et en perte de revenus. Avec Uptrends, vous pouvez surveiller les serveurs de messagerie SMTP, POP3 ou IMAP et vous assurer que votre équipe soit informée instantanément si un problème survient.

## Surveillance de la Disponibilité

Outre les pannes de serveur, les problèmes de DNS, ou d'autres problèmes de configuration, peuvent empêcher vos serveurs de messagerie de fonctionner correctement. Avec les moniteurs de serveur de messagerie vous saurez instantanément quand un problème survient.

## Surveillance de la Performance

Beaucoup de choses peuvent affecter la performance, dont le trafic réseau et le matériel défaillant. En mettant en place des alertes sur les temps de réponse, vous pourrez savoir exactement quand vos serveurs de messagerie commencent à rencontrer des problèmes.

## Configuration

La configuration de vos moniteurs de serveurs mail n'est pas très différente de la configuration d'autres types de moniteurs. Pour vous rafraîchir la mémoire sur la marche à suivre pour configurer un nouveau moniteur, vous pouvez lire l'article [Ajouter un moniteur]({{< ref path="support/kb/basics/adding-monitors" lang="fr" >}}). Pour configurer un moniteur de serveur mail :

1. Sélectionnez {{< AppElement type="button" >}}\+Ajouter moniteur{{< /AppElement >}} dans la section **Moniteurs** du {{< AppElement type="menuitem" >}}menu principal{{< /AppElement >}}.
2. Dans le champ **Type** choisissez SMTP, POP3 ou IMAP.
3. Donnez un **Nom** à votre moniteur.
4. Choisissez l'**intervalle de vérification**.
5. Cochez les cases **Activé** et **Générer alerte** si elles ne le sont pas déjà.
6. Fournissez soit l'adresse IP soit le nom de domaine de votre serveur mail dans le champ **Adresse réseau**.
7. Vérifiez que le numéro de **Port** est correct.
8. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.

Avec cette configuration de base, Uptrends vous enverra des alertes si votre serveur devient indisponible. Vous pouvez également utiliser l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}} pour définir les alertes pour le temps de réponse. Dans l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}}, vous pouvez fournir des informations d'authentification si vous voulez qu'Uptrends tente de se connecter au serveur (voici comment [Uptrends protège vos informations d'authentification]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="fr" >}})).
