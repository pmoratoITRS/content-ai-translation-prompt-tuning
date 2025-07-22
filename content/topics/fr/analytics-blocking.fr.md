{
 "hero": {
"title": "Blocage d'URL et de Google Analytics"
},
"title": "Blocage d'URL et de Google Analytics",
"summary": "Blocage d'URL et de Google Analytics dans vos moniteurs Full Page Check, Real Browser et Transactions.",
  "url": "/support/kb/surveillance-synthetique/parametres-moniteurs/blocage-des-url-et-des-analytics",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/analytics-blocking"
}

{{< callout >}}
**Remarque :** Le blocage d'URL et de Google analytics est seulement disponible pour les comptes [Enterprise et Business]({{< ref path="/pricing" lang="fr" >}}).
{{< /callout >}}

Les moniteurs de type Full Page Check (FPC) et Transactions chargent votre page web dans un navigateur avec tous les éléments de la page, y compris les scripts Google Analytics et d'autres éléments tiers. Le chargement de la page dans le navigateur du point de contrôle est comptabilisé comme une visite de page dans votre analyse d'audience. Si la surveillance de votre site web modifie trop votre analyse d'audience ou s'il existe une autre raison pour laquelle vous ne souhaitez pas que des éléments particuliers soient chargés dans le navigateur, vous avez deux options :

- Blocage de Google Analytics
- Blocage d'URL

{{< callout >}}
**Remarque :** Ne craignez pas que vos moniteurs HTTP(S) perturbent vos analyses ; les vérifications HTTP(S) ne chargent pas votre page dans un navigateur. Par conséquent, cette surveillance n'apparaîtra jamais dans vos analyses.
{{< /callout >}}

## Comment fonctionne le blocage des requêtes ?

Lorsque vous affichez le graphique en cascade, vous verrez toujours les requêtes d'éléments bloqués. Pourquoi ? Eh bien, nous ne pouvons pas simplement dire au navigateur de ne pas charger ces URL, alors nous ne traitons pas ces requêtes lorsque nous les voyons et nous les empêchons ainsi de sortir sur Internet. Google Analytics ne verra jamais ces requêtes, donc vos analyses ne seront pas perturbées. Le navigateur a néanmoins besoin d'une réponse pour ces requêtes afin de ne pas perturber le comportement HTTP normal attendu. C'est pourquoi nous lui renvoyons une réponse avec un en-tête normal de statut 200 OK et un contenu de 512 octets.

## Comment le blocage des requêtes affecte-t-il mes rapports ?

Le blocage affecte peu vos rapports. Nous vous indiquons toujours lorsque le navigateur a bloqué le téléchargement d'un élément et nous bloquons les requêtes générées par ces éléments. Pour indiquer que l'élément a été bloqué, le nom de l'élément apparaît barré dans votre graphique en cascade. Les noms barrés vous indiquent exactement quelles requêtes ont été interceptées en fonction des paramètres de blocage de votre moniteur.

![](/img/content/e13feb2b-6a95-479e-92aa-eea4deac6169.png)

## Lorsque vous bloquez Google Analytics, qu'est-ce qui est bloqué ?

Google propose une suite de services, pas seulement les analytics ; par conséquent, Uptrends bloque les éléments Google les plus courants. Lorsque vous choisissez de bloquer Google Analytics, Uptrends bloque :

- google-analytics.com
- stats.g.doubleclick.net
- googleadservices.com
- google.com/ads

Uptrends **ne bloque pas** googletagmanager.com, afin de ne pas perturber les pages qui en dépendent pour leur fonctionnement.

## Comment puis-je bloquer Google Analytics ?

Parce que beaucoup de sites utilisent Google Analytics, nous proposons une case à cocher dans les paramètres de votre moniteur.

1. Ouvrez les paramètres de votre moniteur.
2. Sélectionnez l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}} 
3. Cochez la case intitulée **Bloquer Google Analytics**.
4. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.

C'est tout ! Vous avez terminé. S'il existe d'autres éléments que vous devez bloquer, lisez la suite.

## Comment bloquer d'autres URL et d'autres éléments ?

Le blocage d'une URL peut s'avérer nécessaire pour diverses raisons, par exemple lors de l'exécution des tests A/B. Avec les moniteurs Uptrends, vous pouvez bloquer autant d'éléments que vous voulez.

1. Ouvrez les paramètres de votre moniteur
2. Sélectionnez l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}}.
3. Tapez l'URL complète ou partielle de l'élément que vous souhaitez bloquer dans la case intitulée **Bloquer cette (partie de l') URL**.
4. Placez chaque URL à bloquer sur sa propre ligne.
5. Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.

Lorsque le point de contrôle voit une requête sortante contenant des URL ou des chaînes de caractères trouvées dans cette zone, le point de contrôle bloque la requête. Pour obtenir une aide supplémentaire concernant le blocage d'éléments, [demandez à nos experts]({{< ref path="contact" lang="fr" >}}) !

{{< callout >}}
**Remarque :** Le blocage des URL peut parfois casser votre page et provoquer des alertes inutiles. Si vous avez besoin d'aide, [contactez-nous]({{< ref path="contact" lang="fr" >}}).
{{< /callout >}}
