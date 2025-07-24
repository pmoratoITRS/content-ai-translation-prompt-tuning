{
  "hero": {
    "title": "Adresses IP à mettre sur liste blanche"
  },
  "title": "Adresses IP à mettre sur liste blanche",
  "summary": "Tous les services d'Uptrends, y compris le portail de l'application, les sites www, l'API d'Uptrends et tous les autres services liés à Uptrends, Uptrends Infra et Uptrends RUM, sont fournis depuis plusieurs emplacements ayant différentes adresses IP.",
  "url": "[URL_BASE_TOPICS]compte/addresses-ip-pour-listeblanche",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_27]
**Remarque :** Vous cherchez les **adresses IP des checkpoints** pour les ajouter à la liste blanche et assurer le bon fonctionnement de vos moniteurs ? Consultez la [liste complète]([LINK_URL_1]) des adresses IP de nos checkpoints.
[SHORTCODE_28]

Plusieurs services sont utilisés par Uptrends Synthetics, Uptrends Infra et Uptrends Real User Monitoring. C'est notamment le cas du portail de l'application, des sites www et de l'API d'Uptrends. Ces services sont accessibles depuis plusieurs emplacements ayant des adresses IP différentes. Par exemple, l'adresse IP du domaine api.uptrends.com peut changer toutes les cinq minutes. C'est aussi le cas pour tous les sous-domaines du domaine uptrends.com.

[SHORTCODE_29]
**Astuce :** Si vous avez besoin de mettre nos applications sur liste blanche, nous vous conseillons de placer sur liste blanche les domaines et sous-domaines uptrends.com (pour HTTPS uniquement et pour IPv4 et IPv6) afin d'éviter tout impact lié aux modifications de nos adresses IP.
[SHORTCODE_30]

Les adresses IPv6 suivantes peuvent être mises sur liste blanche :

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64

Les tableaux ci-dessous indiquent quelles adresses IPv4/IPv6 doivent être ajoutées à la liste blanche pour certains services.

## Uptrends Synthetics
| URL | Adresse ou plage IP | Utilisé pour |
|-----|--------------------|-------------------|
| [INLINE_CODE_1] | [SHORTCODE_1] 
- 178.162.179.211
- 95.211.70.211 [SHORTCODE_2]  | Communication avec l'API (Synthetics) |
   | [INLINE_CODE_2]          | [SHORTCODE_3]
- 178.162.179.213
- 95.211.70.213 [SHORTCODE_4]  | Application Uptrends |
   | [INLINE_CODE_3] | [SHORTCODE_5]
- 178.162.179.205
- 95.211.70.205 [SHORTCODE_6] | [SHORTCODE_7]
   SSO initié par le prestataire de service
   Pour en savoir plus, vous pouvez lire l'article [Vue d'ensemble du Single Sign-on]([LINK_URL_2]), et plus précisément l'option 2 de la section *Comment les utilisateurs SSO peuvent-ils se connecter ?*. [SHORTCODE_8] |
   | [INLINE_CODE_4]       | [SHORTCODE_9]
- 178.162.179.217
- 95.211.70.217  [SHORTCODE_10] | Pages de statut publiques |
   | [INLINE_CODE_5]          | [SHORTCODE_11]
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  [SHORTCODE_12]| Téléchargements |

## Uptrends Infra
| URL | Adresse ou plage IP | Utilisé pour |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| [INLINE_CODE_6] | [SHORTCODE_13] 
- 178.162.179.210
- 95.211.70.210 [SHORTCODE_14] |  Communication avec l'API (Infra) |
   |  [INLINE_CODE_7] | [SHORTCODE_15]
- 178.162.179.208
- 95.211.70.208 [SHORTCODE_16] |  Application Uptrends Infra |
   |  [INLINE_CODE_8] | [SHORTCODE_17]
- 178.162.179.209
- 95.211.70.209 [SHORTCODE_18] |  [SHORTCODE_19]
   Données envoyées par les agents
   La machine sur laquelle l'agent est installé doit pouvoir y accéder. [SHORTCODE_20] |
   | [INLINE_CODE_9] | [SHORTCODE_21]
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5[SHORTCODE_22] |  Téléchargements, par exemple les mises à jour des agents |

## Uptrends RUM

| URL | Utilisé pour |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_10] | Nécessaire pour afficher les cartes sur votre vue d'ensemble RUM. La machine qui affiche le dashboard doit avoir accès à ce domaine. |

## Alertes

| Adresse ou plage IP | Utilisé pour |
|----------------------------------------------------------------------------|-------------------|
| [SHORTCODE_23] 
- 168.245.61.22
- 178.162.179.193
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 [SHORTCODE_24] | Alertes par e-mail |
   | [SHORTCODE_25]
- 95.211.70.193
- 178.162.179.193[SHORTCODE_26] | Alertes par intégrations personnalisées |