{
  "hero": {
    "title": "Vue d'ensemble du DNS"
  },
  "title": "Vue d'ensemble du DNS",
  "summary": "Toutes les infos sur le paramétrage de la surveilance de DNS avec le monitoring d'Uptrends.",
  "url": "/support/kb/surveillance-synthetique/uptime-monitoring/dns/vue-densemble-du-dns",
  "translationKey": "https://www.uptrends.com/support/kb/dns/dns-overview",
  "sectionlist": false
}

La surveillance de votre serveur DNS est un excellent moyen de vous assurer que vos utilisateurs peuvent accéder à votre site web et à vos services web facilement, rapidement et en toute sécurité.

Les étapes à suivre pour ajouter un moniteur sont décrites dans notre article [Ajouter un moniteur]({{< ref path="support/kb/basics/adding-monitors" lang="fr" >}}). Le présent article vous apporte des précisions relatives aux moniteurs DNS.

## Pourquoi utiliser un moniteur DNS ?

Ce moniteur vous permet d'effectuer différentes requêtes sur un serveur de noms DNS. La vérification la plus courante consiste à savoir si votre nom de domaine (www\.yourcompany.com) pointe toujours sur l'adresse IP de votre serveur web. Le serveur de nom de votre fournisseur est la source principale de cette information. En surveillant cette requête DNS directement, nous détectons les éventuels problèmes de DNS, avant même que votre site ne devienne indisponible pour vos visiteurs et vos clients.

Le moniteur DNS d'Uptrends vous permet de faire de nombreux contrôles concernant le bon fonctionnement du serveur DNS : vérifiez vos noms de domaine (enregistrements A et CNAME), les noms de domaine des serveurs de messagerie (enregistrements MX), les délégués de zone DNS (enregistrements NS), les informations faisant autorité sur les zones DNS (enregistrements SOA) et d'autres informations DNS contenues dans des enregistrements au format TXT (y compris les informations SPF pour l'authentification par e-mail).

## Mise en place d'un moniteur DNS

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}} et cliquez sur le bouton + (Ajouter).
2. Sélectionnez le type de moniteur **DNS**.
3. Ensuite, entrez le **nom**, et l'**intervalle de vérification** qui convient le mieux à vos besoins de surveillance de DNS.
4. Sélectionnez votre **version d'IP**. Si vous effectuez vos tests avec IPv6, vous pouvez choisir d'utiliser seulement les checkpoints qui ne prennent en charge qu’IPv6 en natif. Si cette case est décochée, les vérifications seront effectuées à partir des checkpoints qui utilisent IPv6 en natif, et avec une simulation IPv6 pour les checkpoints qui utilisent IPv4.
5. Entrez les informations relatives au **serveur DNS**, en précisant *le nom de domaine* ou *l'adresse IP* du serveur DNS à tester. Par exemple : `n1s.yourprovider.com`
6. Il est aussi important de vérifier le **port** de votre serveur DNS, pour confirmer l'utilisation de la valeur par défaut de 53.
7. Sélectionnez ensuite le type de **requête DNS**. Vous avez le choix entre : *A Record*, *AAAA Record*, *CNAME Record*, *MX Record*, *NS Record*, *SOA Record*, *TXT Record* ou *Root Server*.
8. Spécifiez le nom de domaine que vous souhaitez interroger dans le champ **Valeur test**. Par exemple : `www.yourdomain.com`
9. Indiquez le **Résultat attendu** dans le champ du même nom.
   Par exemple, si vous testez le nom de domaine de votre site web (une requête A Record), indiquez l'adresse IP de votre domaine. Le service Uptrends vérifiera ensuite que la réponse de la requête DNS correspond à l'adresse IP.

   {{< callout >}}**Astuce** : Si votre nom de domaine a plusieurs adresses IP, vous pouvez utiliser une expression régulière pour faire correspondre plusieurs valeurs.
   Exemple : 1.2.3.4 \| 5.6.7.8{{< /callout >}}
10. Cliquez sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} lorsque vous avez terminé.
