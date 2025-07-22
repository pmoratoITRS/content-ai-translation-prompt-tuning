{
"hero": {
"title": "Certificats clients pour le monitoring multi-étapes"
},
"title": "Certificats clients pour le monitoring multi-étapes",
"url": "/support/kb/synthetic-monitoring/surveillance-api/certificats-clients-pour-monitoring-multi-etapes",
"translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-client-certificate-authentication"
}

De nombreuses API exigent que l'appelant spécifie des informations d'authentification pour vérifier son identité, et parfois ses droits d'accès. Les informations d'authentification peuvent être transmises via des en-têtes HTTP (authentification basique/NTLM/Digest), en échangeant des jetons d'accès (OAuth), en demandant au client d'inclure un certificat client dans la requête, ou via une combinaison de ces méthodes.

Cet article présente les options relatives aux **certificats clients**. Pour configurer une méthode d'authentification traditionnelle, [lisez l'article sur les types d'authentification]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="fr" >}}).

## Types de certificats clients

La section Certificat client accessible dans l'onglet Requête des étapes du moniteur d'API multi-étapes propose les options présentées ci-dessous. Si vous utilisez plusieurs étapes dans votre définition, assurez-vous de définir les paramètres nécessaires pour chaque étape.

- **Certificat client Uptrends** : cette option est pertinente si vous demandez à vos utilisateurs d'API de générer et d'inclure leur propre certificat client pour prouver leur identité. Si vous choisissez cette option, un certificat appartenant à Uptrends sera fourni lors de l'envoi de la requête HTTP. Votre API peut vérifier cette requête entrante en utilisant la clé publique correspondante. S'il y a correspondance, alors c'est une preuve que la requête provient de quelqu'un qui possède le certificat d'origine (celui d'Uptrends), et de personne d'autre. Le certificat n'est pas disponible pour les [checkpoints privés]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="fr" >}}) (en conteneurs).
   Pour en savoir plus, vous pouvez lire l'article sur les [clés publiques des certificats clients d'Uptrends]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="fr" >}}).
- **Certificat client personnalisé** : utilisez cette option si vous possédez ou contrôlez le certificat client qui doit être inclus dans la requête. Une fois que vous avez envoyé le fichier de certificat à Uptrends, vous pouvez l'inclure dans vos moniteurs d'API multi-étapes. Puisque ce certificat vous appartient, votre API pourra vérifier les requêtes entrantes qui l'utilisent. La section suivante contient des informations sur la configuration.
- **Aucun** : choisissez *Aucun* si vous ne voulez pas inclure de certificat client dans votre requête HTTP.

## Création d'un certificat client défini par l'utilisateur ou personnalisé

Avant d'inclure un certificat client dans vos moniteurs d'API multi-étapes, vous devez d'abord le charger dans votre compte Uptrends. Les certificats (et autres informations sensibles) sont téléchargés et stockés dans votre coffre-fort. Une fois que vous avez placé un certificat dans votre coffre-fort, vous pouvez commencer à l'utiliser dans la configuration de votre moniteur.

### Chargement d'un certificat client

Lorsque vous choisissez l'option Certificat client personnalisé pour la première fois, vous remarquerez qu'il n'y a pas encore de certificats disponibles. Pour en ajouter un, choisissez *Ajouter un élément*. Vous serez ensuite dirigé vers le coffre-fort. Vous pouvez aussi passer par le menu {{< AppElement type="menuitem" >}}Configuration de compte > Coffre-fort{{< /AppElement >}}, ouvrir une section de coffre-fort et cliquer sur {{< AppElement type="button" >}}Ajouter un élément de coffre-fort{{< /AppElement >}}.

Dans la fenêtre *Nouvel élément de coffre-fort*, donnez un nom unique au certificat afin de pouvoir le reconnaître plus tard. Assurez-vous que le type du nouvel élément du coffre-fort est **Archive de certificat**. Ajoutez les informations que vous jugez utiles dans le champ *Description*.

Enfin, sélectionnez le fichier de certificat que vous voulez charger. Le fichier doit être de type PKCS\#12, ou un fichier d'archive de certificat, qui contient à la fois la clé privée et la clé publique. Les fichiers PKCS \#12 ont une extension .pfx ou .p12.

La plupart du temps, le fichier d'archive de certificat est crypté. Nous aurons donc besoin du mot de passe pour utiliser ce fichier. Saisissez le mot de passe dans le champ *Mot de passe d'archive* et cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}}.

### Utilisation des certificats clients dans les moniteurs multi-étapes

Une fois que vous avez enregistré le certificat client dans le coffre-fort, vous pouvez l'utiliser pour le monitoring d'API multi-étapes. Dans la section **Certificat client** d'une étape, cliquez sur **Rafraîchir** pour actualiser la liste des certificats disponibles. Choisissez ensuite le certificat correspondant pour chaque étape qui nécessite un certificat.
