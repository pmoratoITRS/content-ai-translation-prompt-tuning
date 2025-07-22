{
"hero": {
"title": "Vérification d'un numéro de série dans un enregistrement SOA"
},
"title": "Vérification d'un numéro de série dans un enregistrement SOA",
"summary": "Cet article vous explique comment utiliser un moniteur DNS pour vérifier un numéro de série dans un enregistrement SOA. ",
"url": "/support/kb/surveillance-synthetique/uptime-monitoring/dns/verification-d-un-numero-de-serie-dans-un-enregistrement-soa",
"translationKey": "https://www.uptrends.com/support/kb/dns/checking-a-serial-number-in-an-soa-record"
}

Il est possible que vous ayez besoin d'utiliser un moniteur DNS pour vérifier le numéro de série signalé par un serveur de noms pour un domaine. Le numéro de série est une propriété spécifique d'un nom de domaine, que le serveur de noms stocke dans l'enregistrement SOA (Start of Authority). Le serveur de noms incrémente le numéro de série chaque fois que les paramètres DNS d'un domaine sont modifiés. Le numéro de série vous indique le moment où vos entrées DNS changent et vous permet de recevoir une alerte en cas de falsification. Cet article vous décrit comment obtenir le numéro de série et comment configurer un moniteur DNS pour tester la valeur.

## Obtention du numéro de série actuel

Pour obtenir le numéro de série actuel, vous devez effectuer une requête SOA.

1. Ouvrez une fenêtre de commande.
2. Tapez  `nslookup` et appuyez sur \[Entrée\].
3. Passez à l'interrogation des enregistrements SOA en tapant `set type=soa` et appuyez sur \[Entrée\].
4. Tapez le nom du nom de domaine en question et appuyez sur \[Entrée\].

Si le serveur de noms actuel peut répondre à cette requête, il vous donnera le contenu des enregistrements SOA. Le numéro de série figure parmi les valeurs renvoyées. Dans l'exemple ci-dessous, le numéro de série est 162337499.

![](/img/content/4a94bdaf-0a6c-41ac-8d4b-5b2d941b37e1.png)

## Configuration d'un moniteur DNS pour vérifier l'enregistrement SOA

Maintenant que vous connaissez le numéro de série, vous devez configurer un moniteur DNS pour vérifier l'enregistrement SOA. Si vous avez besoin d'aide pour configurer un moniteur DNS, vous pouvez lire l'article [Configurer un moniteur DNS]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="fr" >}}).

1. Ouvrez un moniteur DNS existant ou créez un nouveau moniteur DNS.
2. Sélectionnez **SOA Record** dans le menu déroulant **Requête DNS.**
3. Fournissez l'adresse IP ou le nom de domaine pour le serveur de noms que vous souhaitez tester dans le champ **Serveur DNS**. Laissez cette case vide pour utiliser le serveur de noms local sur le checkpoint.
4. Remplissez le nom de domaine pour lequel vous souhaitez vérifier l'enregistrement SOA dans le champ **Valeur Test**.
5. Entrez le numéro de série que vous souhaitez tester dans le champ **Résultat attendu**.

{{< callout >}}
**Remarque** : Si le serveur de noms renvoie un résultat, ce dernier contiendra toutes les valeurs de l'enregistrement SOA, et pas seulement la valeur du numéro de série. Il existe une astuce pour extraire tout le contenu de l'enregistrement SOA. Cette astuce consiste à forcer le moniteur à échouer en fournissant un résultat attendu invalide. Par exemple, saisissez "valeur de test factice" dans la zone **Résultat attendu**. Lorsque le moniteur retournera une erreur, vous obtiendrez tout le contenu de l'enregistrement SOA dans les détails de la vérification (voir l'exemple ci-dessous).
{{< /callout >}}

![](/img/content/99d458d1-7366-4722-9ca6-27201259d8f1.png)
