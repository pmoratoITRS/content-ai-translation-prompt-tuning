{
  "hero": {
    "title": "Source de la page et journal de la console"
  },
  "title": "Source de la page et journal de la console",
  "summary": "Où trouver la source de la page et les informations du journal de la console dans les FPC et les moniteurs de transactions",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/resultats-surveillance/source-page-journal-console",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Pour les [moniteurs de transactions]([LINK_URL_1]) et les [moniteurs Full Page Check (FPC)]([LINK_URL_2]), vous avez la possibilité d'afficher la **source de la page** (c'est-à-dire le document HTML tel que reçu par le point de contrôle), ainsi que le **journal de la console** qui a été généré lorsque nous avons chargé la page.


## Dans les FPC

Pour les FPC, les informations sur la source de la page et le journal de la console se trouvent dans chaque résultat de vérification, sous le [graphique en cascade]([LINK_URL_3]). Les informations sur la source de la page sont toujours présentes, mais le journal de la console ne sera disponible que s'il y avait vraiment des entrées de journal de la console dans le navigateur lorsque la page a été chargée. En règle générale, le navigateur génère des entrées pour le journal de la console lorsque quelque chose ne va pas - par exemple, si un certain élément ne peut pas être chargé correctement ou si une erreur javascript est rencontrée.

![Exemple de journal de console affichant une erreur]([LINK_URL_4])

## Dans les moniteurs de transactions

Pour les moniteurs de transactions, ces options de source de la page et de journal de la console devront être explicitement activées.

### Configuration de la capture de la source de la page et du journal de la console dans une transaction

Pour afficher la source de la page et les données du journal de la console pour une étape spécifique d'une transaction, vous devez d'abord activer l'option **Cascade** pour cette étape (voir notre guide sur [travailler avec des cascades de transactions]([LINK_URL_5])). L'option **Source de la page** devient disponible. La sélection de cette option signifie que les résultats de la vérification du moniteur contiendront à la fois les informations sur la source de la page et toutes les données de journal de la console qui ont été générées pendant l'exécution de cette étape.

![Sélection de la source de la page dans l'éditeur de transactions]([LINK_URL_6])

### Où trouver la source de la page et des informations du journal de la console dans une transaction

Après avoir activé l'option de source de page pour une étape de transaction, vous trouverez les informations dans les résultats de la vérification générés à partir de ce moment-là. Allez à la transaction dans votre [Journal moniteurs]([LINK_URL_7]) ou accédez au tableau de bord des transactions et cliquez sur n'importe quel résultat de contrôle de surveillance généré après avoir activé l'option Source de la page.


![Icônes pour la source de la page et le journal de la console dans la transaction]([LINK_URL_8])

Pour accéder aux informations de la source de la page pour cette étape particulière, cliquez sur la troisième icône [SHORTCODE_1][SHORTCODE_2] dans le résultat de la vérification du moniteur. Vous trouverez le journal de la console en cliquant sur la dernière icône [SHORTCODE_3][SHORTCODE_4] mais il peut ne pas toujours exister.

