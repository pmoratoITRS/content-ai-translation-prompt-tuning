{
"hero": {
"title": "Installation de certificats dans des emplacements privés"
},
"title": "Installation de certificats dans des emplacements privés",
"summary": "Ce guide vous explique comment installer des certificats dans des emplacements privés pour effectuer une surveillance interne de votre infrastructure réseau.",
"url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/installation-certificats-emplacements-prives",
"translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-certificates-private-locations"
}


Lors de la configuration de votre [emplacement privé basé sur Docker]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="fr" >}}), il est possible que vous ayez besoin d'installer des certificats pour garantir la fiabilité et authentifier les connexions avec le site web ou le service web que vous surveillez.

Les types de certificats suivants peuvent être installés :

- Certificats clients (PKCS #12)
- Certificats intermédiaires de l'autorité de certification (PKCS #7)
- Certificats racines de l'autorité de certification (PKCS #7)

Notez que le [fichier compressé d'installation sur Docker d'Uptrends]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="fr" >}}) contient un dossier **Certificates**. Dans ce dossier, vous trouverez des sous-dossiers pour chaque type de certificat pris en charge. Pour les installer, suivez les instructions ci-dessous.

## Installer des certificats sur un emplacement privé basé sur Docker

Le guide d'installation facultatif ci-dessous concerne les certificats applicables aux emplacements privés basés sur Docker. Ces étapes sont à suivre uniquement si une ou plusieurs des applications testées nécessitent l'installation d'un certificat.

Avant d'installer les certificats, assurez-vous d'avoir suivi les étapes d'installation des [emplacements privés basés sur Docker]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="fr" >}}).

### Installer des certificats d'une autorité de certification (CA)

**Pour installer les certificats CA :**

1. Ouvrez le dossier contenant votre installation d'emplacement privé. Plusieurs fichiers sont inclus par défaut, comme le fichier YAML `docker-compose` et les scripts Windows PowerShell. Ces fichiers sont indispensables pour le processus d'installation.

2. Ouvrez le dossier **Certificates**. Ce dernier contient trois sous-dossiers et un fichier `README` au format Markdown.

3. Placez vos certificats CA dans les sous-dossiers **Certificates** correspondants :

- Dossier **Intermediate** : pour tous les fichiers de certificats intermédiaires de l'autorité de certification (PKCS #7).
- Dossier **Root** : pour tous les fichiers racines de l'autorité de certification (PKCS #7).

4. Relancez le logiciel de checkpoints d'Uptrends en exécutant le script `update-images.ps1` depuis le répertoire d'installation racine.

### Installer des certificats clients

Notez que les [certificats clients utilisés dans les moniteurs d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="fr" >}}) et les certificats clients utilisés pour les emplacements privés sont deux types de certificats distincts, qui remplissent des fonctions différentes.

**Pour installer des certificats clients :**

1. Ouvrez le dossier contenant votre installation d'emplacement privé. Plusieurs fichiers sont inclus par défaut, comme le fichier YAML `docker-compose` et les scripts Windows PowerShell. Ces fichiers sont indispensables pour le processus d'installation.

2. Ouvrez le dossier **Certificates**. Ce dernier contient trois sous-dossiers et un fichier `README` au format Markdown.

3. Placez votre certificat client dans le dossier **Client**.

4. Dans le dossier **Client**, créez un fichier JSON appelé `clientCertificates.json`. Ce fichier JSON doit lister tous vos certificats clients. Autrement, passez à l'étape suivante.

- Commencez par copier et modifier le modèle JSON :

```json
[
    {
        "File": "my-first-client-cert.p12",
        "Password": "letmein",
        "UrlPatterns": ["https://fake.sub.domain.example.com"]
    },
    {
        "File": "AcmeCert.pfx",
        "Password": "anvil123",
        "UrlPatterns": ["https://client.acmecorp.fake:1234", "[*.]acmecorp.real"]
    }
]
```

Vous remarquerez que cet extrait de code JSON contient deux certificats clients. Chaque certificat client est représenté par un objet JSON contenant trois paires clé-valeur. Le premier certificat, `my-first-client-cert.p12`, doit être utilisé avec un sous-domaine spécifique. Le deuxième certificat, `AcmeCert.pfx`, doit être utilisé avec le sous-domaine du client `acmecorp.fake` lors de la connexion au port HTTPS 1234 ou de l'accès à `acmecorp.real` ou à un de ses sous-domaines.

Modifiez les valeurs suivantes selon vos besoins :

- `File` : le nom de fichier et l'extension de fichier de votre certificat client.
- `Password` : le mot de passe requis pour accéder aux données dans l'archive de certificat, comme la clé privée.
- `UrlPatterns` : la liste de domaines ou sous-domaines URL pouvant utiliser le certificat client. Cette liste peut contenir plusieurs types d'URL qui peuvent représenter un domaine unique, un sous-domaine ou un caractère générique représentant un domaine et tous ses sous-domaines. Pour en savoir plus, consultez la page [Format des URL des règles Enterprise](https://chromeenterprise.google/policies/url-patterns/).

5. Relancez le logiciel de checkpoints d'Uptrends en exécutant le script `update-images.ps1` depuis le répertoire d'installation racine.

6. Vérifiez que les anciens et nouveaux certificats sont reconnus et installés correctement. En cas de problème, envisagez les cas de figure les plus courants :

- Vérifiez que le nom de fichier JSON est correct.
- Vérifiez que toutes les paires clé-valeur JSON respectent la syntaxe JSON.
- Vérifiez l'absence de tout problème de configuration ou d'autorisation.
