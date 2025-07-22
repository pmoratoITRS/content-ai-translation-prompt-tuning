{
  "title": "Clés publiques des certificats clients d'Uptrends",
  "summary": "Cet article explique comment utiliser les clés publiques d’Uptrends avec vos moniteurs d'API multi-étapes pour vérifier que les vérifications d'API proviennent d'Uptrends.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/cles-publiques-des-certificats-clients-uptrends",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Le certificat client d'Uptrends peut être utilisé dans les moniteurs d'API multi-étapes afin de garantir l'authenticité des requêtes HTTP créées par vos moniteurs : votre serveur API peut vérifier l'identité des serveurs de checkpoints d'Uptrends, d'où sont envoyées les requêtes HTTP.

Les serveurs de checkpoints utiliseront la clé privée du certificat pour signer les requêtes. Personne d'autre n'a accès à cette clé privée, donc personne ne peut signer une demande de la même manière en se faisant passer pour Uptrends. Cela signifie que vous, en tant que destinataire, pouvez être sûr que ces requêtes proviennent réellement des serveurs d'Uptrends. Cette vérification se fait en vérifiant l'identité des requêtes entrantes à l'aide de la clé publique d'Uptrends. Les informations relatives à la clé publique sont listées ci-dessous.

[SHORTCODE_1]
**Remarque** : Le certificat client d'Uptrends n'est pas disponible pour les [checkpoints privés]([LINK_URL_1]) (en conteneurs).
[SHORTCODE_2]


## Comment puis-je être sûr que cette clé publique est authentique ?

Lors de l'établissement de l'identité et de l'authenticité, il est important de vérifier que vous disposez d'informations correctes.

### Fiabilité de la connexion et du transport

- Nous avons fait en sorte que vous lisiez toujours le contenu de cette page à l'aide d'une connexion HTTPS. Cette connexion sécurisée signifie que le contenu ne peut jamais être falsifié (et que son contenu ne peut pas être détourné) pendant le transport depuis notre serveur web jusqu'à votre navigateur.
- Même si une personne malveillante parvenait à vous présenter un lien HTTP (c'est-à-dire, non sécurisé) vers le site web d'Uptrends avec l'intention de l'intercepter et d'en modifier le contenu (on parle d'attaque par repli), votre navigateur rejetterait ce lien. Les navigateurs refusent de contacter Uptrends via une connexion non sécurisée pour les raisons suivantes :
   - Le site web d'Uptrends et le portail d'applications clients imposent une politique de sécurité de transport HTTP strict (HSTS). Cela signifie que les navigateurs ont comme consigne de ne jamais suivre un lien HTTP non sécurisé vers le domaine uptrends.com. À la place, ils doivent toujours utiliser le HTTPS.
   - Le domaine uptrends.com figurait parmi les 1 000 premiers domaines répertoriés dans la liste préchargée HSTS. Cette liste de préchargement est codée en dur dans les navigateurs grand public tels que Chrome, Edge, Opera et Safari, ce qui signifie que ces navigateurs vont toujours utiliser HTTPS pour uptrends.com et ses sous-domaines.

### Identité de confiance

Si vous consultez le certificat TLS pour ce site, vous remarquerez que ce site web appartient à Uptrends B.V. Le certificat est signé par Sectigo, une autorité de certification reconnue dans le monde entier. Votre navigateur ne fera jamais confiance à la connexion sans la signature d'une autorité de certification. C'est la meilleure façon de prouver que le domaine que vous visitez actuellement est effectivement la propriété d'Uptrends, et de confirmer que son contenu provient d'Uptrends.

## Informations relatives à la clé publique

Les informations suivantes décrivent les propriétés de la clé publique associée au certificat client utilisé par les serveurs de checkpoints d'Uptrends, lorsqu'ils sont invités à le faire. Ce certificat client, tout comme les certificats relatifs à nos sites web, a été signé par une autorité de certification.

[HTML_TAG_1]

  [HTML_TAG_2]
    [HTML_TAG_3]
      [HTML_TAG_4][HTML_TAG_5]
      [HTML_TAG_6][HTML_TAG_7]
    [HTML_TAG_8]

  [HTML_TAG_9]

  [HTML_TAG_10]
    [HTML_TAG_11]
      [HTML_TAG_12]Émetteur[HTML_TAG_13]
      [HTML_TAG_14]CN = Sectigo RSA Client Authentication and Secure Email CA[HTML_TAG_15]O = Sectigo Limited[HTML_TAG_16]L = Salford[HTML_TAG_17]S = Greater Manchester[HTML_TAG_18]C = GB[HTML_TAG_19]
    [HTML_TAG_20]
    [HTML_TAG_21]
      [HTML_TAG_22]Sujet[HTML_TAG_23]
      [HTML_TAG_24]E = certificates@uptrends.com[HTML_TAG_25]
    [HTML_TAG_26]
    [HTML_TAG_27]
      [HTML_TAG_28]Nom commun[HTML_TAG_29]
      [HTML_TAG_30]Uptrends[HTML_TAG_31]
    [HTML_TAG_32]
    [HTML_TAG_33]
      [HTML_TAG_34]Numéro de série[HTML_TAG_35]
      [HTML_TAG_36]1a223e5481b066dfda30e5f35cdb3a81[HTML_TAG_37]
    [HTML_TAG_38]
    [HTML_TAG_39]
      [HTML_TAG_40]Date d'expiration[HTML_TAG_41]
      [HTML_TAG_42]Sunday, 27 July 2025 01:59:59[HTML_TAG_43]
    [HTML_TAG_44]
    [HTML_TAG_45]
      [HTML_TAG_46]Clé publique complète (Base64)[HTML_TAG_47]
      [HTML_TAG_48]—–BEGIN CERTIFICATE—– [HTML_TAG_49]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[HTML_TAG_50]—–END CERTIFICATE—–[HTML_TAG_51][HTML_TAG_52]
    [HTML_TAG_53]
  [HTML_TAG_54]

[HTML_TAG_55]