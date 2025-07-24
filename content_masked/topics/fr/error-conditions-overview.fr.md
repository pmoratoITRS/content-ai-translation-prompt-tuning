{
  "hero": {
    "title": "Conditions d'erreur"
  },
  "title": "Conditions d'erreur",
  "summary": "Cet article vous explique à quoi servent les conditions d'erreur et comment les utiliser. ",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/conditions-erreur/apercu-des-conditions-derreur",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": false
}

Les conditions d'erreur jouent un rôle essentiel dans la création de vos alertes de moniteur. La configuration d'une condition d'erreur est la première étape du [cycle du flux d'alertes et d'erreurs]([LINK_URL_1]) qui vous permet de recevoir des messages d'alerte.

Les **conditions d'erreur** vous permettent de définir un ensemble de critères pour informer votre moniteur des erreurs à surveiller sur votre site web, votre service web ou votre serveur. Elles indiquent à votre moniteur quel comportement de site web doit entraîner ou non une erreur.

Par exemple, si vous voulez vous assurer que le chargement de votre site web dure moins que trois secondes, vous pouvez définir une condition d'erreur en précisant les seuils applicables au temps de chargement de page. De même, si vous voulez vérifiez que les contenus, les plug-ins ou les scripts de votre site web se chargent correctement, vous pouvez définir des conditions d'erreur pour chacun de ces éléments.

Lorsqu'une condition d'erreur est remplie, une erreur est générée et une alerte est déclenchée. Si l'alerte a été configurée, vous recevez immédiatement un message d'alerte.

## Conditions d'erreur pour les types de moniteur [ANCHOR_1]

L'onglet [SHORTCODE_15] Conditions d'erreur [SHORTCODE_16] vous permet de configurer les différentes conditions d'erreur disponibles pour chaque type de moniteur. Notez que la disponibilité des conditions d'erreur varie selon la catégorie du moniteur et les données collectées :

![Capture d'écran de la configuration des conditions d'erreur du moniteur]([LINK_URL_2])

### Moniteur de disponibilité

Les conditions d'erreur suivantes sont disponibles pour les [moniteurs de disponibilité]([LINK_URL_3]) :

| Type de moniteur | Conditions d'erreur |
|--|--|
| HTTPS, Webservice HTTP et HTTPS | [SHORTCODE_1]
- [Vérifier la disponibilité de la page]([LINK_URL_4])
- [Vérifier le contenu de la page]([LINK_URL_5])
- [Vérifier le temps de chargement de la page]([LINK_URL_6])
- [Vérifier les ressources]([LINK_URL_7])
   [SHORTCODE_2] |
   | DNS, SSL, SFTP, FTP | [SHORTCODE_3]
- [Vérifier les ressources]([LINK_URL_8])
- [Vérifier le temps de fonctionnement total]([LINK_URL_9])
   [SHORTCODE_4] |
   | SMTP, POP3, IMAP | [SHORTCODE_5]
- [Vérifier les ressources]([LINK_URL_10])
- [Vérifier le temps de fonctionnement total]([LINK_URL_11])
   [SHORTCODE_6] |
   | Microsoft SQL Server, MySQL | [SHORTCODE_7]
- [Vérifier les ressources]([LINK_URL_12])
- [Vérifier le temps de fonctionnement total]([LINK_URL_13])
   [SHORTCODE_8] |
   | Ping, Connect | [SHORTCODE_9]
- [Vérifier les ressources]([LINK_URL_14])
- [Vérifier le temps de fonctionnement total]([LINK_URL_15])
   [SHORTCODE_10] |

### Moniteur de navigateur ou Full Page Check (FPC)

Les conditions d'erreur suivantes sont disponibles pour les [moniteurs de navigateur ou Full Page Check]([LINK_URL_16]) :

| Type de moniteur | Conditions d'erreur |
|--|--|
| Navigateur ou Full Page Check | [SHORTCODE_11]

- [Vérifier la disponibilité de la page]([LINK_URL_17])
- [Vérifier le contenu de la page]([LINK_URL_18])
- [Vérifier les URL chargées par la page]([LINK_URL_19])
- [Vérifier le temps de chargement de la page]([LINK_URL_20])
- [Vérifier les Core Web Vitals]([LINK_URL_21])
- [Vérifier les métriques W3C]([LINK_URL_22])
- [Vérifier le contenu de la console]([LINK_URL_23])
- [Vérifier les ressources]([LINK_URL_24])
   [SHORTCODE_12] |

### Moniteur de transaction

Les conditions d'erreur des [moniteurs de transactions]([LINK_URL_25]) sont aussi disponibles pour chaque étape. Selon la [configuration des étapes de transaction]([LINK_URL_26]), les conditions d'erreur suivantes peuvent être ou non disponibles :

![Capture d'écran de la configuration des conditions d'erreur du moniteur]([LINK_URL_27])

| Type de moniteur | Conditions d'erreur |
|--|--|
| Transaction ou Parcours utilisateur | [SHORTCODE_13]
- [Vérifications de contenu]([LINK_URL_28])
- [Vérifier les ressources]([LINK_URL_29])
- [Vérifier les URL chargées par la page]([LINK_URL_30])
- [Vérifier les Core Web Vitals]([LINK_URL_31])
- [Vérifier les métriques W3C]([LINK_URL_32])
- [Vérifier le contenu de la console]([LINK_URL_33])
- [Vérifier la disponibilité du site]([LINK_URL_34])
- [Vérifier le temps de fonctionnement total]([LINK_URL_35])
   [SHORTCODE_14] |

Notez que le [moniteur d'API multi-étapes]([LINK_URL_36]) détecte les erreurs selon une autre approche. Il utilise des **assertions** pour vous permettre de définir les vérifications à valider si la réponse de l'API répond à vos conditions. Pour en savoir plus, lisez notre article sur les [assertions pour la surveillance multi-étapes]([LINK_URL_37]).

## Configuration d'une condition d'erreur [ANCHOR_2]

Les conditions d'erreur peuvent être ajoutées lors de la [création d'un tout nouveau moniteur]([LINK_URL_38]) ou de la modification d'un moniteur existant.

Pour configurer des conditions d'erreur :

1. Ouvrez le menu [SHORTCODE_17] Surveillance > Configuration du moniteur [SHORTCODE_18].
2. Sélectionnez le moniteur auquel vous voulez ajouter une condition d'erreur.
3. Ouvrez l'onglet [SHORTCODE_19]Conditions d'erreur[SHORTCODE_20].
4. Cliquez sur la condition d'erreur pour afficher toute la section et configurer les paramètres du moniteur.
5. (Facultatif) Pour ajouter de nouvelles vérifications à une condition d'erreur, cliquez sur le bouton [SHORTCODE_21] \+ Nouvelle vérification [SHORTCODE_22].
6. Poursuivez la configuration des conditions.
7. Cliquez sur [SHORTCODE_23] Enregistrer [SHORTCODE_24] pour confirmer les changements.

Pour recevoir un message d'alerte lorsqu'une condition d'erreur est remplie, [créez une définition d'alerte]([LINK_URL_39]).

![Capture d'écran de la configuration des conditions d'erreur du moniteur]([LINK_URL_40])