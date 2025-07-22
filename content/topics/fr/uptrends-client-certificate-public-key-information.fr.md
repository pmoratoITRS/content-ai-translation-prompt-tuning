{
"title": "Clés publiques des certificats clients d'Uptrends",
"summary": "Cet article explique comment utiliser les clés publiques d’Uptrends avec vos moniteurs d'API multi-étapes pour vérifier que les vérifications d'API proviennent d'Uptrends.",
"url": "/support/kb/synthetic-monitoring/surveillance-api/cles-publiques-des-certificats-clients-uptrends",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/uptrends-client-certificate-public-key-information"
}

Le certificat client d'Uptrends peut être utilisé dans les moniteurs d'API multi-étapes afin de garantir l'authenticité des requêtes HTTP créées par vos moniteurs : votre serveur API peut vérifier l'identité des serveurs de checkpoints d'Uptrends, d'où sont envoyées les requêtes HTTP.

Les serveurs de checkpoints utiliseront la clé privée du certificat pour signer les requêtes. Personne d'autre n'a accès à cette clé privée, donc personne ne peut signer une demande de la même manière en se faisant passer pour Uptrends. Cela signifie que vous, en tant que destinataire, pouvez être sûr que ces requêtes proviennent réellement des serveurs d'Uptrends. Cette vérification se fait en vérifiant l'identité des requêtes entrantes à l'aide de la clé publique d'Uptrends. Les informations relatives à la clé publique sont listées ci-dessous.

{{< callout >}}
**Remarque** : Le certificat client d'Uptrends n'est pas disponible pour les [checkpoints privés]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="fr" >}}) (en conteneurs).
{{< /callout >}}


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

<table>

  <thead>
    <tr>
      <th class="cell-small"></th>
      <th class="cell-extralarge"></th>
    </tr>

  </thead>

  <tbody>
    <tr>
      <td class="bold">Émetteur</td>
      <td>CN = Sectigo RSA Client Authentication and Secure Email CA<br>O = Sectigo Limited<br>L = Salford<br>S = Greater Manchester<br>C = GB</td>
    </tr>
    <tr>
      <td class="bold">Sujet</td>
      <td>E = certificates@uptrends.com</td>
    </tr>
    <tr>
      <td class="bold">Nom commun</td>
      <td>Uptrends</td>
    </tr>
    <tr>
      <td class="bold">Numéro de série</td>
      <td>1a223e5481b066dfda30e5f35cdb3a81</td>
    </tr>
    <tr>
      <td class="bold">Date d'expiration</td>
      <td>Sunday, 27 July 2025 01:59:59</td>
    </tr>
    <tr>
      <td class="bold">Clé publique complète (Base64)</td>
      <td>—–BEGIN CERTIFICATE—– <br>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<br>—–END CERTIFICATE—–<br></td>
    </tr>
  </tbody>

</table>