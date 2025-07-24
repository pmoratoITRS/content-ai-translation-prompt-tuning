{
  "hero": {
    "title": "Configuration des alertes téléphoniques (vocales)"
  },
  "title": "Configuration des alertes téléphoniques (vocales)",
  "summary": "Configuration des alertes téléphoniques Uptrends : configuration, messages d'exemples, tests et sélection du numéro de téléphone de réception. ",
  "url": "[URL_BASE_TOPICS]alerter/alertes-vocales",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Parfois, un simple e-mail, SMS ou message intégré en provenance de Slack ou PagerDuty ne peut pas faire l'affaire. Parfois, le téléphone doit sonner pour vous tirer d'un sommeil profond ou attirer votre attention captée par un match important. Les alertes téléphoniques sont là pour ça. Selon vos alertes, vos niveaux d'escalade et le planning de vos opérateurs, vous pouvez faire sonner le téléphone de l'opérateur de service afin de recevoir un message vocal automatisé concernant les conditions de l'alerte. Dans cet article de la base de connaissances, vous allez apprendre à :

- [Configurer vos alertes téléphoniques]([LINK_URL_1])
- [Configurer vos opérateurs pour les alertes téléphoniques]([LINK_URL_2])
- [Configurer vos définitions d'alertes avec alertes téléphoniques]([LINK_URL_3])
- [Utiliser les crédits SMS/téléphone]([LINK_URL_4])
- [Savoir à quoi vous attendre lorsque vous décrochez le téléphone]([LINK_URL_5])

## Configurer Uptrends pour l'intégration des alertes téléphoniques [ANCHOR_1]

Afin d'ajouter les alertes téléphoniques à votre arsenal d'outils de messagerie, vous devez en premier lieu avoir une formule Premium ou supérieure.

[SHORTCODE_1]
**Remarque :** Vous pouvez facilement mettre à niveau votre version Starter en appelant votre chargé de compte, ou vous pouvez simplement adresser un ticket à notre support et quelqu'un prendra contact avec vous rapidement. Visitez notre page [Contact]([LINK_URL_6]) pour plus d'informations.
[SHORTCODE_2]

Les alertes téléphoniques sont désactivées par défaut. Pour activer l'intégration téléphonique, vous devez vous rendre sur la page **Intégrations** dans le menu [SHORTCODE_9]Alerte[SHORTCODE_10]. Une fois l'intégration activée, vous pouvez ajouter des alertes téléphoniques à vos niveaux d'escalade. Pour activer les alertes téléphoniques :

1. Sélectionnez **Téléphone** dans la case **Type d'intégration**.
2. Utilisez le nom d'intégration par défaut ou modifiez-le dans la case **Nom d'intégration**.
3. Choisissez un **numéro de téléphone sortant** dans la case. Choisissez un numéro basé sur votre localisation. Si votre pays n'est pas sur la liste, choisissez le pays le plus proche de vous. Vous (et votre équipe) pouvez ajouter le numéro dans vos contacts pour l'identifier plus rapidement. Si vous laissez l'option **Par défaut**, Uptrends choisira le meilleur numéro d'après le code de pays des (opérateurs) receveurs.  
   [SHORTCODE_3]**Remarque :** Consultez la [liste des pays pris en charge]([LINK_URL_7]) et les codes de pays pour vérifier la compatibilité avec le numéro de téléphone de l'opérateur receveur. Si le pays et le code ne figurent pas dans la liste, l'opérateur ne recevra PAS les appels d'alerte. [SHORTCODE_4]
4. Si vous souhaitez modifier les paramètres de langue définis pour l'opérateur, sélectionnez la **langue** à utiliser pour l'alerte téléphonique.
5. Assurez-vous que le nom du moniteur peut être transcrit par la synthèse vocale. Autrement, cochez la case **Utiliser des noms de moniteurs alternatifs**. Pour en savoir plus, lisez l'article [Indiquer un nom de moniteur adapté aux alertes téléphoniques]([LINK_URL_8]).
6. Cochez la case **Actif** si elle n'est pas cochée.
7. Cliquez sur [SHORTCODE_11]Enregistrer[SHORTCODE_12].

![capture d'écran de l'intégration téléphonique]([LINK_URL_9])

## Configurer les opérateurs [ANCHOR_2]

Dans l'onglet [SHORTCODE_13]Principal[SHORTCODE_14] de la page de configuration de l'opérateur, vous pouvez ajouter un numéro de **téléphone mobile** et remplacer le **numéro de téléphone sortant** que vous avez défini lors de l'intégration téléphonique. Si vous utilisez déjà les SMS dans votre définition d'alerte, vous ne devriez pas avoir besoin d'ajuster les profils de vos opérateurs.

### Ajouter un numéro de téléphone mobile

Le système utilise le numéro de téléphone mobile de l'opérateur pour envoyer des alertes par SMS, et Uptrends utilise le même numéro pour les alertes téléphoniques. Pour ajouter un numéro de téléphone :

1. Tapez le signe (\+) suivi du code du pays suivi du numéro de téléphone.
2. N'utilisez pas d'autres caractères non numériques. En général, le numéro de téléphone ressemble à ça \+33634168796 pour un numéro français.
3. Cliquez sur [SHORTCODE_15]Enregistrer[SHORTCODE_16].

[SHORTCODE_5]
**Remarque :** Oui, vous pouvez utiliser un numéro de téléphone fixe dans le champ **Téléphone mobile** (est-ce que quelqu'un possède encore un téléphone fixe de nos jours ?), mais si vous utilisez les SMS, cet opérateur ne recevra pas les alertes SMS. Si vous avez besoin d'utiliser une ligne de téléphone fixe pour un numéro de téléphone mobile d'un opérateur, assurez-vous de ne pas inclure cet opérateur dans les niveaux d'escalade que vous avez définis pour les alertes par SMS.
[SHORTCODE_6]

### Remplacer le numéro de téléphone sortant par défaut

Si vous avez défini un **numéro de téléphone sortant** sur la page d'intégration des alertes par téléphone, vous aurez peut-être besoin de remplacer ce choix pour un opérateur donné. Si vous sélectionnez **Remplacer les paramètres d'intégration téléphone**, Uptrends utilisera le numéro alternatif que vous avez sélectionné dans le champ de sélection de téléphone.

![capture d'écran du paramétrage téléphonique de l'opérateur]([LINK_URL_10])
## Configurer Uptrends pour l'intégration des alertes téléphoniques [ANCHOR_3]

Maintenant que vous avez activé les alertes et que tous vos opérateurs ont leur numéro de téléphone mobile dans le système, il est temps de paramétrer vos niveaux d'escalade pour les alertes téléphoniques.

1. Sélectionnez **Définitions d'alerte** dans l'option **Alerte** du menu principal.
2. Cliquez pour choisir une définition existante, ou créez une nouvelle définition en cliquant sur [SHORTCODE_17]Ajouter une définition d'alerte[SHORTCODE_18] dans le menu d'action rapide.
3. Sélectionnez un onglet parmi les [SHORTCODE_19]niveaux d'escalade[SHORTCODE_20] .
4. Cochez la case **Téléphone** dans la section **Alertes par intégrations**. Si l'option Téléphone n'est pas proposée, vous devez activer l'intégration téléphonique ou cocher la case **Actif** sur la page d'intégration des alertes par téléphone (voir les instructions de [configuration]([LINK_URL_11]) ci-dessus).
5. Cliquez sur [SHORTCODE_21]Enregistrer[SHORTCODE_22].

![capture d'écran de la définition d'alerte pour l'intégration téléphonique]([LINK_URL_12])

C'est terminé ! Lorsqu'une erreur déclenchera une alerte pour cette définition et ce niveau d'escalade, Uptrends localisera le numéro de l'opérateur et appellera son téléphone mobile avec un message automatisé.

## Coûts liés à l'utilisation des alertes téléphoniques [ANCHOR_4]

Si vous utilisez déjà les SMS, vous connaissez probablement le système de crédits de message. Chaque niveau de compte est livré avec des crédits. Une fois ces crédits utilisés, vous devez les recharger pour continuer à recevoir les alertes par téléphone ou par SMS. Les alertes par téléphone et par SMS utilisent les mêmes crédits. Pour en savoir plus, consultez la page [Utilisation du crédit SMS]([LINK_URL_13]).

[SHORTCODE_7]
**Remarque :** Les alertes tests par téléphone et SMS sont GRATUITES. Uptrends n'utilise pas vos crédits de message pour les tests.
[SHORTCODE_8]

## À quoi s'attendre en décrochant le téléphone [ANCHOR_5]

Que va vous dire l'alerte téléphonique ? Si le système dispose de l'information d'erreur, vous devriez entendre quelque chose comme cela :

> "Bonjour, c'est Uptrends.  
> Nous avons détecté une erreur pour le moniteur Page d'accueil. L'erreur était "HTTP pattern matched", et cela a démarré il y a une minute.  
> Le code d'erreur HTTP était 500.  
> Le délai fixé à 12 a été dépassé.  
> Au revoir."

Bien entendu, ce message n'est qu'un exemple. Votre message contiendra les informations correspondant à votre situation d'alerte et à votre moniteur. Si l'information sur l'erreur n'est pas disponible, vous entendrez quelque chose comme cela :

> "Bonjour, c'est Uptrends.  
> Une erreur est survenue pour un ou plusieurs de vos moniteurs. Pour le moment, nous n'avons pas d'autres informations. Veuillez vérifier le statut de votre moniteur dans Uptrends.  
> Au revoir."

## Résoudre les problèmes liés aux alertes téléphoniques

Vous rencontrez des problèmes lors de la réception des alertes téléphoniques ? Nous avons rassemblé les [solutions de dépannage des alertes téléphoniques]([LINK_URL_14]).

## Vous avez des questions ?

Si vous avez besoin d'une aide plus détaillée pour configurer les opérateurs, définir les alertes et paramétrer les niveaux d'escalade, consultez la [base de connaissances]([LINK_URL_15]) d'Uptrends. Si vous ne trouvez pas l’information que vous cherchez, nous sommes là pour vous aider. Consultez la page [Contact]([LINK_URL_16]) pour trouver un numéro d'assistance ou créer un ticket support.
