{
  "hero": {
    "title": "Moniteurs de certificat SSL"
  },
  "title": "Moniteurs de certificat SSL",
  "summary": "La fonctionnalité avancée de surveillance des certificats SSL d’Uptrends contrôle l’absence de faille de sécurité en surveillant les dates d’expiration et les modifications de vos certificats SSL. ",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/uptime-monitoring/moniteurs-de-certificats-ssl",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Votre certificat SSL (Secure Socket Layer) a plus d'importance qu'il n'y paraît. Des études ont montré que la plupart des utilisateurs suivent les conseils de leur navigateur et quittent le site en cours pour celui d'un concurrent s'ils sont avertis d'un certificat SSL invalide ou périmé. Les erreurs SSL sont courantes ; même Google a été victime d'un certificat périmé. À mesure que le personnel et les responsabilités évoluent, les certificats SSL sont vite oubliés. Heureusement, avec Uptrends, vous pouvez conserver vos informations SSL dans un seul endroit et recevoir des alertes à l'approche des dates d'expiration et en cas de modification de votre certificat.

## Qu’est-ce qui est surveillé ?

En plus d’anticiper l'expiration de votre certificat SSL, vous pouvez suivre une ou plusieurs des valeurs de certificat suivantes :

- Nom commun
- Organisation
- Unité organisationnelle
- Numéro de série
- Empreinte digitale
- Délivré par nom commun
- Délivré par organisation
- Délivré par unité organisationnelle

Si l'une de ces valeurs du certificat sur votre site change (ce qui peut indiquer un piratage), Uptrends émet une alerte.

#### Messages d’alerte et messages d’erreur

Voici les messages qui s’affichent lorsque votre certificat SSL est sur le point d’expirer :

- **Le certificat SSL expirera bientôt** : ce message d’erreur générique est basé sur le nombre de jours défini dans le champ [SHORTCODE_1] Délai d'alerte en jour [SHORTCODE_2] dans l’onglet [SHORTCODE_3] Principal [SHORTCODE_4] de votre moniteur SSL. Lorsque la date de votre certificat correspond à la valeur indiquée dans ce message, ce message s’affiche dans le dashboard *Vue d'ensemble des erreurs* ou dans les emplacements où les erreurs sont regroupées.

Vous pouvez voir le nombre de jours restants avant l’expiration de votre certificat dans les dashboards *Journal moniteurs* et *Historique d’alertes* spécifiques à vos moniteurs SSL :

- **Le certificat SSL expirera dans 1 jour.**
- **Le certificat SSL expirera dans moins d’1 jour.**
- **Le certificat SSL expirera dans *n* jours** : la valeur *n* représente le nombre effectif de jours restants avant l’expiration du certificat SSL, sous un format numérique. Par exemple, s’il reste *45* jours, le message d’alerte indiquera : *Le certificat SSL expirera dans 45 jours*.

Ces messages s’affichent aussi dans la section *Voir les détails* lorsque vous réalisez une action [SHORTCODE_5] Tester maintenant [SHORTCODE_6] sur les moniteurs SSL.

## Configurer un moniteur de certificat SSL :

La configuration d’un moniteur de certificat SSL est similaire à la configuration d'un moniteur de page web. Pour revoir les grandes étapes de configuration d’un moniteur, vous pouvez lire l'article de notre base de connaissances intitulé [Ajouter un moniteur]([LINK_URL_1]).

Pour configurer un moniteur de certificat SSL :

1. Dans le menu, cliquez sur [SHORTCODE_7] Surveillance > Configuration du moniteur [SHORTCODE_8], puis sur le bouton [SHORTCODE_9][SHORTCODE_10].
2. Dans la fenêtre contextuelle *Sélectionnez un type de moniteur*, cliquez sur *Certificat SSL*, puis sur le bouton [SHORTCODE_11] Choisir [SHORTCODE_12].
3. Configurez les [principaux paramètres du moniteur]([LINK_URL_2]).
4. Dans le champ *URL*, saisissez l’URL ou l’adresse de navigateur que vous voulez surveiller.
5. Remplissez soigneusement la section Certificat SSL. Ces informations sont généralement faciles à obtenir auprès de votre émetteur de certificat SSL.

![Section contenant les détails du certificat SSL]([LINK_URL_3])

6. Cliquez sur le bouton [SHORTCODE_13] Enregistrer [SHORTCODE_14] en bas de l'écran.

Uptrends surveillera désormais les détails de votre certificat SSL et vous avertira si les conditions définies dans les onglets [SHORTCODE_15]Conditions d'erreur[SHORTCODE_16] et [SHORTCODE_17]Avancé[SHORTCODE_18] sont remplies. Pour en savoir plus, veuillez consulter l’article de notre base de connaissances sur les [paramètres de moniteur]([LINK_URL_4]).