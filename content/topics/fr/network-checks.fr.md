{
  "hero": {
    "title": "Vérification de réseau"
  },
  "title": "Vérification de réseau",
  "summary": "Une vérification du réseau par des moniteurs permet de savoir que votre réseau est actif et accessible et vous avertit en cas de panne.",
  "url": "/support/kb/surveillance-synthetique/uptime-monitoring/verification-de-reseau",
  "translationKey": "https://www.uptrends.com/support/kb/network-checks"
}

Uptrends a conçu ses moniteurs HTTP(S) pour surveiller la disponibilité et la rapidité de votre site web. Mais pour vérifier d'autres appareils en réseau depuis l'autre côté de votre pare-feu, c'est de la vérification de réseau dont vous avez besoin. En cas d'erreur avec l'URL ou l'adresse IP que vous avez fourni, Uptrends vous envoie une notification. Selon l'erreur, vous recevez un traceroute pour vous aider à résoudre le problème. Avec la vérification de réseau, vous avez deux options : ping ou connect.

## Ping

Lorsque vous sélectionnez la vérification de réseau par Ping, les points de contrôle Uptrends utilisent le protocole ICMP (Internet Control Message Protocol) pour envoyer une demande d'écho. Uptrends s'occupe de collecter et de notifier les temps de réponse, et émet des alertes en cas d'erreur dans la réponse.

{{< callout >}}
**Remarque** : Vous devez activer ICMP sur votre appareil pour éviter les alertes inutiles ; il faut également savoir qu'en cas de trafic réseau intense, certains appareils ignorent les requêtes ICMP.
{{< /callout >}}

## Connect

Si vous sélectionnez la vérification réseau par **Connect**, Uptrends tente de se connecter au numéro de port que vous avez désigné. Vous pouvez fournir n'importe quel numéro de port. Par exemple, pour une connexion en SSH (Secure Shell) à un système Linux, vous indiquerez le port 22.

## Caractéristiques

Ping et Connect vous offrent tous les deux de nombreuses options de surveillance.

### Fréquence

Le réglage par défaut pour la fréquence est de cinq minutes, mais vous pouvez régler la fréquence entre une minute et une fois par heure.

{{< callout >}}
**Remarque** : L'intervalle de vérification est la durée entre la fin d'une vérification et le début de la suivante. [En savoir plus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="fr" >}})
{{< /callout >}}

### Version d'IP

IPv4 a longtemps été la norme, mais la nouvelle version IPv6 se fait progressivement accepter. La plupart des points de contrôle Uptrends supportent déjà IPv6 et la liste s’agrandit.

{{< callout >}}
**Remarque** : Nous vous recommandons de paramétrer vos vérifications de façon à surveiller à la fois IPv4 et IPv6. Le routage pour les deux versions se fait différemment, donc les tests pourraient échouer avec l'une des versions et réussir avec l'autre.
{{< /callout >}}

### Performance

Des connect ou ping lents peuvent indiquer d'autres problèmes de réseau ou de matériel. Dans l'onglet {{< AppElement type="tab" >}}Conditions d'alerte{{< /AppElement >}}, vous pouvez définir des limites de performance pour vous avertir lorsque votre réseau a une baisse de performance.

## Traceroute

Uptrends effectue des diagnostics avec Traceroute dans plusieurs cas :

1. Dans le cadre d'une vérification de moniteur, lorsque le moniteur suspecte un problème de connectivité ou de réseau. Par exemple, quand un moniteur HTTPS essaie de contacter le serveur web, mais qu'aucune connexion TCP ne peut être créée avec l'adresse IP du serveur, un traceroute est effectué pour collecter des données de diagnostic supplémentaires sur la connectivité entre l'emplacement du point de contrôle d'Uptrends et votre serveur.
2. Lorsque vous utilisez l'outil gratuit Traceroute pour effectuer manuellement un traceroute sur l'un des serveurs de points de contrôle d'Uptrends.

Il est important de comprendre le type de trafic auquel vous pouvez vous attendre lorsque ces traceroutes sont effectués. Les implémentations de Traceroute se comportent différemment sur les différentes plates-formes : certaines utilisent des paquets UDP, d'autres des paquets TCP et d'autres utilisent des requêtes d'écho ICMP (ping). Les traceroutes exécutés par Uptrends, toujours effectués sur des serveurs Windows, utilisent des paquets ICMP. Par conséquent, effectuer des traceroutes sur votre environnement réseau avec Uptrends ne fonctionnera que si votre réseau autorise les paquets ICMP. Aucun trafic TCP ou UDP n'est généré.

La configuration d'un moniteur pour surveiller un serveur ou réseau externe est assez simple et généralement très rapide. Ce qui est important c'est de vous assurer que vous avez une adresse IP ou un nom de domaine de serveur fonctionnel.

1. Cliquez sur le bouton + dans le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Dans la fenêtre contextuelle *Sélectionnez un type de moniteur*, cliquez sur le type de moniteur *Ping* ou *Connect*, puis sur le bouton {{< AppElement type="button" >}} Choisir {{< /AppElement >}}.  
   Le nouveau moniteur est créé et la page de configuration s'affiche.
3. Donnez un **Nom** à votre moniteur.
4. Choisissez l'**intervalle de vérification**. [L'intervalle de vérification]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="en" >}}) correspond au temps écoulé entre la fin d'une vérification et le début de la suivante.
5. Saisissez l'adresse du serveur à surveiller dans le champ **Adresse réseau** de la section *Détails*, en veillant à inclure l'adresse IP ou le nom de domaine approprié.
6. Une fois que vous avez terminé la configuration de votre nouveau moniteur, cliquez sur le bouton {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}. Vous avez désormais ajouté votre nouveau moniteur de serveur externe.

   {{< callout >}}**Remarque** : Vous pouvez aussi vérifier les autres [paramètres de moniteur]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="en" >}}) dans les onglets en haut de la page d'ajout de moniteur.{{< /callout >}}