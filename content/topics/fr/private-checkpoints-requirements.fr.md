{
"hero": {
"title": "Exigences liées aux emplacements privés"
},
"title": "Exigences liées aux emplacements privés",
"summary": "Quelles sont les exigences techniques liées aux emplacements privés ?",
"url": "/support/kb/surveillance-synthetique/points-de-controle/emplacements-prives/exigences-checkpoints-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-requirements"
}

## Exigences et paramètres applicables

Certaines exigences s'appliquent au matériel et au réseau, et les paramètres réseau nécessitent quelques ajustements. Les exigences décrites ci-dessous sont basées sur des scénarios standard. Si vous avez des doutes sur vos besoins, veuillez contacter le [support d'Uptrends]({{< ref path="contact" lang="fr" >}}). Pensez à vérifier que les exigences et les paramètres sont respectés avant de procéder à l'installation du checkpoint.

## Capacité des emplacements privés

Vos emplacements privés sont utilisés seulement par vos moniteurs. La capacité requise dépend du type de monitoring que vous effectuez avec les checkpoints sur l'emplacement privé.

Le monitoring qui ne se base pas sur un navigateur, comme avec les moniteurs HTTPS, Connect, Ping et Multi-step API, influe principalement sur les capacités du réseau. Les moniteurs basés sur un navigateur influent principalement sur les capacités du serveur (processeur, mémoire, disque E/S).

### Calcul d'une capacité typique

Voici un exemple de capacité typique si vous suivez les recommandations concernant l'installation d'un emplacement privé, avec le [matériel]({{< ref path="#hardware-requirements" lang="fr" >}}) recommandé et deux checkpoints :

- 2 x 10 transactions à 5 minutes d'intervalle ;
- 2 x 10 vérifications Full Page Check à 5 minutes d'intervalle ;
- 100 vérifications de moniteurs de base à 1 minute d'intervalle.

La durée de la transaction influe sur la capacité.

Cette installation est suffisante pour :

- Confirmer les [erreurs non confirmées]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="fr" >}})
- Assurer la maintenance de l'un des checkpoints, par exemple pour mettre à niveau les conteneurs ou l'hôte Docker

### Redondance

La capacité décrite ci-dessus ne tient pas compte de la redondance des moniteurs. Avec certaines configurations, un emplacement privé peut assurer plus de tâches de monitoring qu'indiqué ci-dessus. C'est le cas lorsque vous établissez une redondance à différents niveaux, par exemple si vous utilisez plusieurs emplacements privés pour la surveillance.

## Exigences matérielles {id="hardware-requirements"}

Les spécifications matérielles suivantes doivent être respectées pour pouvoir ajouter un checkpoint. Pour plus de fiabilité, nous vous recommandons d'utiliser deux checkpoints. Pour des performances optimales, nous vous recommandons d'utiliser trois checkpoints, voire plus. Chaque checkpoint doit respecter les spécifications ci-dessous :

|   | Recommandé | Minimum |
| --- | --- | --- |
| **Processeur** | 4 cœurs | 2 cœurs |
| **RAM** | 8 Go | 4 Go |
| **Stockage** | 60 Go avec un type de stockage rapide (SSD) | 60 Go |
| **Système d'exploitation** | Windows Server 2022 LTSC Standard | Windows Server 2019 LTSC Standard* |

* Notez que Docker sur Windows Server 2019 présente des problèmes de résolution DNS.

## Exigences réseau

Les exigences réseau suivantes doivent être respectées :

**IPv4** : adresse IPv4 statique pour chaque serveur de checkpoints

**IPv6** : facultatif, dépend de votre utilisation d'IPv6 dans l'infrastructure surveillée

**Réseau** : nous recommandons 1 Gbit/s, mais l'utilisation réelle est largement inférieure (généralement 1 à 10 Mbit/s à 95 %) et constante.
Votre connexion Internet doit être capable de transférer les données des mesures à la plateforme d'Uptrends.


## Paramètres réseau

### Pare-feu

Il ne doit pas y avoir d'inspection SSL sur le trafic entre les checkpoints et les serveurs cloud d'Uptrends.

Assurez-vous qu'aucun objet de stratégie de groupe (GPO, ou Group Policy Objects) n'empêche Docker de créer un pare-feu local. Sur la machine qui exécute Docker, activez le paramètre de stratégie de groupe *Appliquer les règles de pare-feu locales*.

### Exigences liées à IPv6

Si le réseau interne fonctionne avec IPv6, indiquez une adresse IPv6 statique et une passerelle IPv6 pour chaque serveur de checkpoints. L'adresse IPv6 nous permet de surveiller votre infrastructure avec IPv6 (le pare-feu doit aussi être configuré correctement). Sans adresse IPv6 statique, Uptrends peut seulement surveiller avec IPv4.

### Serveurs DNS

Le checkpoint nécessite un ou plusieurs serveurs DNS pour être configuré sur un hôte Docker. Par défaut, les conteneurs utilisent la configuration DNS de l'hôte pour résoudre les noms d'hôte avec les applications testées et pour assurer la connectivité avec la plateforme cloud d'Uptrends.

### DNS inversé

Pour surveiller vos serveurs mail depuis un accès externe, configurez un DNS inversé en utilisant checkpoint\_name@uptrends.net pour accéder à l'adresse IP externe correspondante.

