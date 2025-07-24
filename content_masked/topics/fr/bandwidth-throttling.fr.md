{
  "hero": {
    "title": "Limitation de la bande passante"
  },
  "title": "Limitation de la bande passante",
  "summary": "Le FPC et les moniteurs de transactions proposent deux méthodes différentes pour brider vos vitesses de connexion : par simulation et en utilisant Chrome.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/limitation-de-la-bande-passante",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Pour affiner votre surveillance synthétique afin qu'elle corresponde mieux aux vitesses de connexion réelles de vos utilisateurs, nous vous recommandons d'utiliser la limitation de bande passante avec vos moniteurs Full Page Check (FPC) et vos moniteurs de transactions.

## Pourquoi utiliser la limitation de bande passante ?

Les ordinateurs de checkpoints d'Uptrends fonctionnent dans des centres de données. Leur vitesse native est proche de celle d'un utilisateur typique travaillant sur un réseau à grande vitesse, et sûrement très semblable à celle que vous utilisez dans votre entreprise. Si votre base d'utilisateurs se compose principalement d'utilisateurs d'ordinateurs de bureau, il est probable que les vitesses des checkpoints d'Uptrends représentent correctement celles de vos utilisateurs. Si vos utilisateurs accèdent à votre site ou service à l'aide d'appareils mobiles ou utilisent des connexions DSL plus lentes, il est judicieux de configurer un moniteur qui reflète leur expérience. C'est là qu'intervient la limitation de la bande passante.

## Types de limitations de bande passante

Uptrends vous propose deux types de limitations de bande passante : par simulation et par navigateur. Les deux types offrent les mêmes options de vitesse de connexion. La version basée sur navigateur est seulement disponible pour Chrome, et la version par simulation est disponible pour tous les autres types de navigateurs.

### Limitation basée sur un navigateur

Vous pouvez utiliser la limitation de bande passante basée sur un navigateur lorsque vous choisissez d'utiliser un navigateur Chrome pour votre moniteur FPC. Cette méthode, qui est la plus populaire, utilise la même limitation de bande passante que celle disponible dans les outils de développement Chrome. Elle diffère de la limitation simulée en ce que Chrome applique une latence en plus de simuler une bande passante inférieure. La limitation basée sur le navigateur donne une mesure plus précise, en particulier sur les pages web qui utilisent très peu ou beaucoup de connexions. En outre, Chrome surveille le nombre de connexions et applique la limitation à l'ensemble, ce qui donne un meilleur résultat pour les sites web dont la quantité de ressources est inférieure ou supérieure à la moyenne.

Pour activer la limitation par navigateur :

1. Créez un nouveau moniteur FPC ou ouvrez-en un existant.
2. Ouvrez l'onglet [SHORTCODE_1] Avancé [SHORTCODE_2].
3. Sélectionnez **Navigateur** dans la section [SHORTCODE_3]Limitation de bande passante[SHORTCODE_4], et précisez la vitesse de connexion que vous souhaitez utiliser (voir ci-dessous).
4. Cliquez sur [SHORTCODE_5]Enregistrer[SHORTCODE_6].

### Limitation de bande passante par simulation

Vous pouvez configurer une limitation simulée avec le navigateur de votre choix, à l'exception de Chrome. La limitation simulée utilise un proxy pour vous fournir une simulation raisonnable des différentes vitesses de connexion que vos utilisateurs peuvent avoir.

Le checkpoint limite chaque connexion créée par le navigateur, en simulant la quantité moyenne de bande passante disponible pour le type de connexion choisi. Le checkpoint ne prend pas en compte la latence du réseau et effectue des calculs basés sur un nombre moyen de connexions.

1. Créez un nouveau moniteur FPC ou ouvrez-en un existant.
2. Ouvrez l'onglet [SHORTCODE_7] Avancé [SHORTCODE_8].
3. Sélectionnez votre [SHORTCODE_9]Type de navigateur[SHORTCODE_10].
   ![Simulation de limitation de bande passante]([LINK_URL_1])
4. Dans la section [SHORTCODE_11]Limitation de bande passante[SHORTCODE_12], sélectionnez **Simulé**, et précisez la vitesse de connexion que vous souhaitez utiliser (voir ci-dessous).
5. Cliquez sur [SHORTCODE_13]Enregistrer[SHORTCODE_14].


## Types de connexions

Lors de l'application de la limitation de bande passante, nous vous proposons différents types de connexions basés sur des scénarios d'utilisation réelle et non sur les vitesses maximales théoriques que ces technologies peuvent fournir. La limitation de bande passante basée sur le navigateur applique la latence réseau à vos résultats.

**ADSL** : 4 Mbit descendant, 0,5 Mbit montant, 80 ms aller-retour  
**Câble** : 54 Mbit descendant, 1 Mbit montant, 50 ms aller-retour  
**Fibre** : 15 Mbit descendant, 3 Mbit montant, 10 ms aller-retour

**2G** : 200 kbit descendant, 200 kbit montant, 1000 ms aller-retour  
**3G** : 1 Mbit descendant, 500 kbit montant, 300 ms aller-retour  
**4G** : 4 Mbit descendant, 4 Mbit montant, 230 ms aller-retour
