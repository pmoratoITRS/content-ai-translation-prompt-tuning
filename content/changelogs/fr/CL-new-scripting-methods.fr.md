{
"title": "Ajout de nouvelles méthodes de script dans les moniteurs API multi-étapes",
"date": "2025-03-12",
"url": "/changelog/mars-2025-nouvelles-methodes-script",
"translationKey": "https://www.uptrends.com/changelog/march-2025-new-scripting-methods"
}

Les méthodes de script suivantes peuvent désormais être utilisées dans les onglets des [scripts de pré-requête et de post-réponse]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="fr" >}}) des moniteurs d'API multi-étapes :

- `ut.crypto.cert.parseCrl(bytes)` : analyse une liste de révocation de certificats et fournit ses métadonnées.
- `ut.crypto.md5(value)` : génère un hash MD5 de la valeur précisée.
- `ut.crypto.sha1(value)` : génère un hash SHA-1 de la valeur précisée.
- `ut.crypto.sha256(value)` : génère un hash SHA-256 de la valeur précisée.
- `ut.crypto.sha512(value)` : génère un hash SHA-512 de la valeur précisée.
- `ut.response.bytes` : fournit un tableau d'octets contenant le corps de la requête. Les réponses ne peuvent excéder 100 Mo.

Notez que la méthode `ut.response.bytes` est uniquement disponible dans l'onglet {{< AppElement type="tab" >}} Post-response {{< /AppElement >}} de votre moniteur multi-étapes. Les méthodes de script permettant de générer des hash MD5 et SHA vous permettent de stocker et d'envoyer des valeurs de façon sécurisée, en garantissant la protection des données au moyen du hachage.