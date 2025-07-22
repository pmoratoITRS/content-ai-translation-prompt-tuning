{
  "hero": {
    "title": "Surveillance des transactions avec configuration mobile"
  },
  "title": "Surveillance des transactions avec configuration mobile",
  "summary": "L'enregistreur de transaction d'Uptrends vous permet également de tester les transactions pour votre site mobile. Cet article vous explique comment.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/surveillance-des-transactions-avec-configuration-mobile",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Compte tenu de la grande popularité des applications mobiles, il est insuffisant de tester uniquement le fonctionnement des transactions pour les ordinateurs de bureau. Heureusement, l'enregistreur de transaction d'Uptrends peut configurer des scripts pour surveiller la version mobile ou responsive de votre site web en simulant la fenêtre d'affichage d'un appareil. Pour simuler la fenêtre d'affichage de l'appareil, vous devez utiliser le mode de simulation mobile dans les outils de développement de Chrome. Voici comment faire.

## Utiliser le mode appareil (Device mode) de Chrome lors de l'enregistrement de la transaction.

1. [Lancez l'enregistreur de transaction d'Uptrends (extension Chrome)]([LINK_URL_1]) comme vous le feriez normalement. Une nouvelle fenêtre de navigateur s'ouvre.
2. Appuyez sur la touche F12 pour ouvrir les outils de développement Chrome.
3. Repérez l'icône de la barre d'outils qui représente le changement d'appareil et cliquez dessus pour activer le mode de simulation d'appareil.  
   ![Capture d'écran de la barre d'outils présentant le changement d'appareil]([LINK_URL_2])
4. Ajustez les paramètres de l'appareil si nécessaire.
5. Ouvrez la version mobile de votre site.
6. Parcourez votre transaction en cliquant.
7. Téléchargez-la sur votre compte pour créer le script et le tester, ou envoyer le script au support technique d'Uptrends qui s'en occupera.
8. Ajustez les paramètres de surveillance mobile dans votre nouveau moniteur de transactions.

Pour en savoir plus, vous pouvez consulter [cette page (en anglais) sur le mode Device]([LINK_URL_3]) du navigateur Chrome.

## Ajuster les paramètres du moniteur pour la surveillance mobile

Maintenant que vous avez enregistré votre transaction à l'aide du mode Device des outils de développement de Chrome, vous devez finaliser la configuration pour mobile dans les paramètres de votre moniteur.

1. Ouvrez le menu [SHORTCODE_1] Transactions > Gérer les transactions [SHORTCODE_2] et sélectionnez le nouveau moniteur de transaction.
2. Cliquez sur l'onglet [SHORTCODE_3] Avancé [SHORTCODE_4].
3. Dans la section *Navigateur*, à la ligne *Appareil / écran*, ajustez votre **taille d'écran** et choisissez un **agent utilisateur** (qui peut être personnalisé) ou sélectionnez l'option **Simulation mobile** et choisissez l'un des appareils les plus courants.
   ![Capture d'écran de l'onglet Avancé du moniteur de transaction]([LINK_URL_4])
4. Configurez le paramètre **Limitation de bande passante** pour simuler entièrement l'expérience de l'utilisateur final. Vous trouverez plus d'informations sur la [simulation de bande passante]([LINK_URL_5]) dans notre base de connaissances.
5. Cliquez sur le bouton [SHORTCODE_5] Enregistrer [SHORTCODE_6] pour enregistrer vos changements.
