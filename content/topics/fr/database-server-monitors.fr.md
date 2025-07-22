{
  "hero": {
    "title": "Moniteurs base de données"
  },
  "title": "Moniteurs base de données",
  "summary": "Uptrends supports two types of Database server monitors: MySQL and Microsoft SQL Server.",
  "url": "/support/kb/surveillance-synthetique/uptime-monitoring/moniteurs-base-de-donnees",
  "translationKey": "https://www.uptrends.com/support/kb/database-server-monitors"
}

A moins que votre site Web ne fournisse qu'une brochure statique, votre site ou service web dépend d'une base de données pour récupérer le contenu, gérer les utilisateurs ou traiter les commandes. Connaître les temps de réponse de vos bases de données peut vous aider à éviter la catastrophe. L'utilisation des moniteurs de serveur de base de données d'Uptrends vous permet de toujours savoir si votre base de données est en difficulté.

Uptrends utilisera ses  {{% Features/Variable variable="CheckpointCount" %}} points de contrôle pour surveiller votre serveur de base de données depuis l'extérieur.

{{< callout >}}
**Remarque :** Si votre base de données n'est pas visible depuis Internet, vous ne pouvez pas utiliser ce type de moniteur. Toutefois vous pouvez, dans ce cas, surveiller les serveurs derrière votre pare-feu avec [Uptrends Infra](/produits/infra/surveillance-serveur).
{{< /callout >}}

## Comment ça marche ?

Avec la surveillance de la base de données d'Uptrends, vous pouvez surveiller les serveurs de type Microsoft SQL ou MySQL. Les points de contrôle Uptrends tenteront d'établir une connexion à l'adresse IP et à la base de données que vous spécifiez dans l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}} , et si vous fournissez les informations de login, le point de contrôle va tenter de se connecter. Outre pour les temps de réponse que vous spécifiez dans l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}} , Uptrends déclenchera une alerte pour les échecs ou pertes de connexion.

{{< callout >}}
**Remarque :** La sécurité et le partage des informations d'authentification de votre base de données vous préoccupe ? Renseignez-vous sur la façon dont Uptrends met en sécurité vos identifiants de connexion : [Cryptage et la sécurité de votre site]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security" lang="fr" >}}).
{{< /callout >}}


Le moniteur de base de données vous envoie des alertes relatives aux temps de réponse et aux problèmes de connectivité. Sa configuration est similaire à celle du moniteur HTTPS, avec seulement quelques champs spéciaux supplémentaires. Pour savoir comment configurer les moniteurs et les conditions d'erreur, veuillez consulter notre [base de connaissances]({{< ref path="support/kb" lang="fr" >}}). Pour configurer un moniteur de base de données, vous devrez connaître :

- le nom de la base de données ;
- l'URL ou l'adresse IP de la base de données ;
- les informations de connexion de la base de données (facultatif).

## Configuration du moniteur

Pour configurer un moniteur de base de données :

1. Cliquez sur {{< AppElement type="button" >}}\+ Ajouter moniteur{{< /AppElement >}} dans la section **Surveillance** du {{< AppElement type="menuitem" >}}menu principal{{< /AppElement >}}.
2. Sélectionnez **Microsoft SQL Server** ou **MySQL** dans la partie **Serveurs de bases de données** de la boîte de dialogue **Type**.
3. Saisissez le nom de domaine ou l'adresse IP du serveur de la base de données dans la section **Adresse réseau**.
4. Remplissez les autres champs dans l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}}.
5. Définissez les temps de réponse attendus dans l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}}.
6. Cliquez sur l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}}.
7. Indiquez le **nom d'utilisateur** et le **mot de passe**, si nécessaire.
8. Indiquez le **nom de la base de données**.
9. Sélectionnez vos checkpoints dans l'onglet {{< AppElement type="tab" >}}Checkpoints{{< /AppElement >}}.
10. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.
