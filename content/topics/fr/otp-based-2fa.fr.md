{
"hero": {
"title": "Double authentification basée sur un mot de passe à usage unique"
},
"title": "Utiliser la double authentification basée sur un mot de passe à usage unique dans les transactions",
"summary": "Découvrez comment configurer la double authentification basée sur un mot de passe à usage unique dans vos moniteurs de transactions.",
"url": "/support/kb/surveillance-synthetique/transactions/double-authentification-mot-passe-usage-unique",
"translationKey": "https://www.uptrends.com/support/kb/transactions/otp-based-2fa"
}

Dans un monde où la sécurité et la protection des données personnelles sont des préoccupations de plus en plus centrales, bon nombre d'entreprises ne veulent plus se contenter d'une connexion unique pour sécuriser l'accès aux applications web. Afin de renforcer l'authentification des utilisateurs lors de la connexion, des applications web utilisent désormais une authentification à facteurs multiples, souvent sous la forme d'une double authentification qui consiste à demander à l'utilisateur de prouver son identité à deux reprises.

En plus de [la double authentification par SMS]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="fr" >}}), Uptrends prend aussi en charge la méthode qui consiste à demander aux utilisateurs normaux de saisir un code reçu sur une application mobile. On parle aussi d'authentification multi-facteurs par **mot de passe à usage unique basé sur le temps**.

Ces mots de passe à usage unique sont généralement valides pendant une durée limitée (généralement 30 secondes) et doivent être saisis dans l'application web demandant l'authentification. Ces codes sont générés de façon algorithmique d'après l'horodatage et une **clé secrète**, qui est une valeur connue par l'application d'authentification et l'application web, pour qu'elles puissent calculer toutes deux les mêmes valeurs. Ainsi, si la valeur saisie par l'utilisateur correspond à la valeur attendue par l'application web, celle-ci sait que l'utilisateur a accès à la même clé secrète et doit pouvoir accéder aussi à l'application.

## Flux normal d'un scénario de double authentification par mot de passe à usage unique

Le flux habituel d'une procédure d'authentification à deux facteurs dans une application web utilisant les mots de passe à usage unique est le suivant :

1. Dans la page de connexion de l'application, l'utilisateur saisit ses identifiants de connexion dans les champs textuels. Cette saisie est la première étape de la double authentification.
2. Une fois les identifiants saisis, l'application web ouvre une seconde page qui contient un champ textuel, où le mot de passe à usage unique doit être saisi.
3. L'utilisateur ouvre son application mobile d'authentification qui doit présenter un code (généralement à 6 chiffres) ainsi qu'un décompte avant l'expiration du code.
4. L'utilisateur saisit ce code dans l'application web, ce qui lui permet de se connecter (à condition que le code réponde aux attentes de l'application web et n'ait pas expiré !).

## Solution d'Uptrends pour la double authentification basée sur un mot de passe à usage unique

Comme les codes des mots de passe à usage unique sont généralement générés par un algorithme, seule la connaissance de la *clé secrète* est nécessaire pour les calculer. En ajoutant cette clé secrète à votre [coffre-fort]({{< ref path="/support/kb/account/vault" lang="fr" >}}), nous pouvons calculer la valeur correcte, qui peut ensuite être utilisée de la même façon qu'un nom d'utilisateur ou mot de passe [stocké dans le coffre-fort]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="fr" >}}).

Contrairement à la double authentification par SMS, vous pouvez configurer vous-même la double authentification basée sur un mot de passe à usage unique. Il vous faudra néanmoins disposer de la *clé secrète*, qui peut se trouver dans votre configuration de la double authentification ou vous être remise par vos administrateurs. Si votre organisation utilise les codes QR pour enregistrer le mot de passe à usage unique dans les applications mobiles, il est aussi possible que la clé secrète figure dans ces codes. Si vous avez besoin d'aide, n'hésitez pas à contacter notre [équipe de support]({{< ref path="contact" lang="fr" >}}).

## Étapes à suivre pour configurer une double authentification par mot de passe à usage unique dans une transaction

1. En plus des informations de connexion habituelles (que vous pouvez [stocker et utiliser depuis le coffre-fort]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="fr" >}}), vous devez connaître la **clé secrète** nécessaire pour mettre en place l'authentification par mot de passe à usage unique. La clé secrète prend généralement la forme d'un code alphanumérique que vous devriez trouver dans la configuration de votre mot de passe à usage unique. Autrement, si votre organisation utilise les codes QR pour configurer les applications mobiles d'authentification, il est aussi possible que la clé secrète figure dans ces codes (scannez le code pour ouvrir une URL qui contient la clé secrète).
2. Quand vous disposez de la clé secrète, vous devez [l'ajouter au coffre-fort]({{< ref path="/support/kb/account/vault#adding-a-new-item-to-the-vault" lang="fr" >}}). Dans la section appropriée du coffre-fort, créez un élément de coffre-fort du type **Configuration du mot de passe à usage unique**.
3. Nommez l'élément de coffre-fort (et ajoutez une description si vous le souhaitez), puis saisissez la clé secrète dans le champ **Secret**. Si nécessaire, vous pouvez modifier l'algorithme de hachage, le nombre de chiffres ou le délai d'expiration pour les codes à usage unique qui seront générés. Toutefois, les valeurs par défaut devraient fonctionner dans la plupart des cas.
4. Enregistrez l'élément de coffre-fort.
5. La configuration de mot de passe à usage unique peut désormais être utilisée dans vos scripts de transaction, [de la même façon qu'un nom d'utilisateur ou mot de passe stocké dans le coffre-fort]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="fr" >}}).
6. À l'endroit indiqué dans le script de transaction, ajoutez une [action Définir]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="fr" >}}).
7. Ajoutez le bon sélecteur CSS ou Xpath pour pointer le script vers le champ textuel qui attend le mot de passe à usage unique sur la page.
8. Pour définir sa valeur, cliquez sur l'icône {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} et sélectionnez **Mot de passe à usage unique**.
9. Sélectionnez la bonne configuration de mot de passe à usage unique dans le coffre-fort et cliquez sur {{< AppElement type="button" >}} Sélectionner {{< /AppElement >}} pour l'appliquer à cette action.

![Sélection de la configuration de mot de passe à usage unique dans la transaction](/img/content/scr-otp-selection-transaction-nm.min.png)

10. La transaction est désormais configurée pour générer le bon mot de passe à usage unique et le saisir dans le champ textuel. Vous pouvez maintenant continuer à créer la transaction comme vous le feriez normalement.

## Coût

La configuration d'une double authentification basée sur un mot de passe à usage unique pour votre transaction ne suscite aucun coût supplémentaire. C'est le [coût habituel d'une transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}) qui s'applique.
