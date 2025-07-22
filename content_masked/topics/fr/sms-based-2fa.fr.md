{
  "hero": {
    "title": "Double authentification par SMS"
  },
  "title": "Appliquer la double authentification par SMS dans les transactions",
  "summary": "Découvrez comment configurer la double authentification par SMS pour vos moniteurs de transaction.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/transactions/double-authentification-sms",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dans un monde où la sécurité et la protection des données personnelles sont des préoccupations de plus en plus centrales, bon nombre d'entreprises ne veulent plus se contenter d'une connexion unique pour sécuriser l'accès aux applications web. Afin de renforcer l'authentification des utilisateurs lors de la connexion, les applications web utilisent désormais une authentification à facteurs multiples, souvent sous la forme d'une double authentification qui consiste à demander à l'utilisateur de prouver son identité à deux reprises.

En plus de la combinaison nom d'utilisateur/mot de passe habituelle, la méthode la plus courante pour obtenir une preuve d'identité consiste à envoyer un code unique par e-mail, SMS (message texte) ou via une application d'authentification sur mobile.

Cette interaction humaine représente une difficulté supplémentaire pour l'automatisation des tests d'application web. Dans cet article, vous comprendrez comment Uptrends prend en charge la double authentification dans le cadre de la surveillance de transactions.

[SHORTCODE_1] **Remarque** : Les méthodes d'authentification multi-facteurs qui s'appuient sur des applications sont [aussi prises en charge]([LINK_URL_1]). [SHORTCODE_2]

## Flux normal d'un scénario de double authentification par SMS
Le flux habituel d'une procédure d'authentification à deux facteurs dans une application web utilisant les messages SMS est le suivant :

1. Dans la page de connexion d'une application, un utilisateur saisit ses identifiants de connexion dans les champs textuels. Cette saisie est la première étape de la double authentification.
2. Cette tentative de connexion ordonne au système d'envoyer un SMS sur le numéro de téléphone qui a été préconfiguré pour l'utilisateur.
3. Pendant l'envoi du SMS, l'application web ouvre une seconde page qui contient un champ textuel, et attend la saisie de l'utilisateur.
4. Dans le SMS qui est envoyé sur son téléphone mobile, l'utilisateur trouve un code unique à saisir dans la nouvelle page web. Cette saisie est la seconde étape de la double authentification.
5. Si les données sont correctes, l'utilisateur est autorisé à entrer sur l'application web.
6. Une fois connecté, l'utilisateur réalise la tâche prévue dans l'application web.

## Présentation de la solution d'Uptrends pour la double authentification basée sur SMS
Plutôt que d'utiliser un téléphone mobile physique, Uptrends met en place un numéro de téléphone virtuel qui sera utilisé pour recevoir les SMS. Quelques étapes manuelles sont nécessaires pour permettre à Uptrends de créer le composant SMS du processus d'authentification.

L'une des actions du script de transaction consiste à attendre la saisie du SMS entrant. Une fois reçu, le code unique (généralement un code numérique à six chiffres, mais d'autres formats sont aussi possibles) est extrait puis saisi dans le champ textuel correspondant. Tout ce processus reproduit exactement ce que ferait un utilisateur normal, et représente donc une très bonne solution pour réaliser des tests orientés vers les utilisateurs finaux.

## Étapes à suivre pour configurer une double authentification par SMS dans une transaction
1. Dans la page de création et de configuration d'une transaction, il est nécessaire d'examiner certains points et de prendre quelques mesures préparatoires. [Contactez le support]([LINK_URL_2]) pour commencer la mise en place.
2. Aucun téléphone mobile physique n'est utilisé. Un numéro de téléphone virtuel sera demandé à notre partenaire, Twilio. Pour cela, nous devons savoir dans quel pays le numéro de téléphone doit être enregistré.
3. Une fois enregistré, le nouveau numéro de téléphone mobile doit être préconfiguré dans le profil utilisateur de l'application cible. De plus, le profil utilisateur peut devoir être paramétré comme nécessitant une double authentification par SMS.
4. Avant qu'Uptrends commence à créer la transaction, il est judicieux de réaliser un test manuel pour vérifier si la configuration fonctionne correctement et déclenche bien l'envoi d'un SMS qui pourra être reçu par le système d'Uptrends.
5. Une fois confirmé le bon fonctionnement de la communication par SMS, le support d'Uptrends crée une transaction (généralement en s'appuyant sur un enregistrement de transaction créé au moyen de notre [extension de navigateur Transaction Recorder]([LINK_URL_3])).

![Double authentification par SMS dans un script de transaction]([LINK_URL_4])

6. Une fois testée et mise en production, la transaction peut être modifiée et mise à jour librement sans l'aide du support d'Uptrends. Bien sûr, l'équipe de support reste à votre disposition pour toute question.

## Coût
Le [coût de transaction habituel]([LINK_URL_5]) s'applique. Ce coût dépend du nombre d'actions qui seront nécessaires pour que le navigateur ouvre une nouvelle page. En plus du coût habituel, un crédit de transaction supplémentaire sera déduit pour l'action d'attente du SMS.

## Mises en garde
Certains systèmes de double authentification n'envoient pas un SMS à chaque tentative de connexion. Nous vous conseillons d'utiliser une configuration qui déclenche toujours le même comportement à chaque vérification. Cela rendra le script de transaction plus prévisible, et cela augmentera grandement les chances de repérer rapidement un problème dans le système de double authentification.

L'enregistrement d'un numéro de téléphone dédié ne peut fonctionner que pour **une seule transaction**. Si la double authentification est nécessaire pour plusieurs transactions, un nouveau numéro de téléphone sera requis à chaque fois. En effet, comme les transactions seront exécutées en parallèle, voire simultanément, il est impossible de savoir quel SMS est lié à quelle transaction si tous les SMS sont envoyés au même numéro de téléphone.