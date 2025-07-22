{
"hero": {
"title": "Adresses IP à mettre sur liste blanche"
},
"title": "Adresses IP à mettre sur liste blanche",
"summary": "Tous les services d'Uptrends, y compris le portail de l'application, les sites www, l'API d'Uptrends et tous les autres services liés à Uptrends, Uptrends Infra et Uptrends RUM, sont fournis depuis plusieurs emplacements ayant différentes adresses IP.",
"url": "/support/kb/compte/addresses-ip-pour-listeblanche",
"translationKey": "https://www.uptrends.com/support/kb/account/ip-addresses-for-whitelisting"
}

{{< callout >}}
**Remarque :** Vous cherchez les **adresses IP des checkpoints** pour les ajouter à la liste blanche et assurer le bon fonctionnement de vos moniteurs ? Consultez la [liste complète]({{< ref path="/checkpoints" lang="fr" >}}) des adresses IP de nos checkpoints.
{{< /callout >}}

Plusieurs services sont utilisés par Uptrends Synthetics, Uptrends Infra et Uptrends Real User Monitoring. C'est notamment le cas du portail de l'application, des sites www et de l'API d'Uptrends. Ces services sont accessibles depuis plusieurs emplacements ayant des adresses IP différentes. Par exemple, l'adresse IP du domaine api.uptrends.com peut changer toutes les cinq minutes. C'est aussi le cas pour tous les sous-domaines du domaine uptrends.com.

{{< callout >}}
**Astuce :** Si vous avez besoin de mettre nos applications sur liste blanche, nous vous conseillons de placer sur liste blanche les domaines et sous-domaines uptrends.com (pour HTTPS uniquement et pour IPv4 et IPv6) afin d'éviter tout impact lié aux modifications de nos adresses IP.
{{< /callout >}}

Les adresses IPv6 suivantes peuvent être mises sur liste blanche :

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64

Les tableaux ci-dessous indiquent quelles adresses IPv4/IPv6 doivent être ajoutées à la liste blanche pour certains services.

## Uptrends Synthetics
| URL | Adresse ou plage IP | Utilisé pour |
|-----|--------------------|-------------------|
| `api.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.211
- 95.211.70.211 {{< /tableformatter >}}  | Communication avec l'API (Synthetics) |
   | `app.uptrends.com`          | {{< tableformatter >}}
- 178.162.179.213
- 95.211.70.213 {{< /tableformatter >}}  | Application Uptrends |
   | `customername.uptrends.com` | {{< tableformatter >}}
- 178.162.179.205
- 95.211.70.205 {{< /tableformatter >}} | {{< tableformatter >}}
   SSO initié par le prestataire de service
   Pour en savoir plus, vous pouvez lire l'article [Vue d'ensemble du Single Sign-on]({{< ref path="support/kb/account/settings/single-sign-on-overview#how-sso-users-log-in" lang="fr" >}}), et plus précisément l'option 2 de la section *Comment les utilisateurs SSO peuvent-ils se connecter ?*. {{< /tableformatter >}} |
   | `status.uptrends.com`       | {{< tableformatter >}}
- 178.162.179.217
- 95.211.70.217  {{< /tableformatter >}} | Pages de statut publiques |
   | `www.uptrends.com`          | {{< tableformatter >}}
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  {{< /tableformatter >}}| Téléchargements |

## Uptrends Infra
| URL | Adresse ou plage IP | Utilisé pour |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| `api.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.210
- 95.211.70.210 {{< /tableformatter >}} |  Communication avec l'API (Infra) |
   |  `app.uptrendsinfra.com` | {{< tableformatter >}}
- 178.162.179.208
- 95.211.70.208 {{< /tableformatter >}} |  Application Uptrends Infra |
   |  `collector.uptrends.com` | {{< tableformatter >}}
- 178.162.179.209
- 95.211.70.209 {{< /tableformatter >}} |  {{< tableformatter >}}
   Données envoyées par les agents
   La machine sur laquelle l'agent est installé doit pouvoir y accéder. {{< /tableformatter >}} |
   | `www.uptrends.com` | {{< tableformatter >}}
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5{{< /tableformatter >}} |  Téléchargements, par exemple les mises à jour des agents |

## Uptrends RUM

| URL | Utilisé pour |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `code.highcharts.com` | Nécessaire pour afficher les cartes sur votre vue d'ensemble RUM. La machine qui affiche le dashboard doit avoir accès à ce domaine. |

## Alertes

| Adresse ou plage IP | Utilisé pour |
|----------------------------------------------------------------------------|-------------------|
| {{< tableformatter >}} 
- 168.245.61.22
- 178.162.179.193
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 {{< /tableformatter >}} | Alertes par e-mail |
   | {{< tableformatter >}}
- 95.211.70.193
- 178.162.179.193{{< /tableformatter >}} | Alertes par intégrations personnalisées |