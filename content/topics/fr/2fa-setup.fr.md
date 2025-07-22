{
"hero": {
"title": "Configuration de l'authentification à deux facteurs"
},
"title": "Configuration de l'authentification à deux facteurs",
"summary": "Découvrez comment configurer l’authentification à deux facteurs avec des mots de passe à usage unique basés sur le temps pour Uptrends.",
"url": "/support/kb/account/parametres/configuration-authentification-deux-facteurs",
"translationKey": "https://www.uptrends.com/support/kb/account/2fa-setup"
}

Pour activer l’authentification à deux facteurs dans Uptrends, un compte administrateur doit d'abord configurer le paramètre par défaut applicable à tous les comptes. Après cela, les paramètres principaux de l'opérateur peuvent être modifiés individuellement selon le besoin. Une application d'authentification au choix peut être utilisée.

## Activation des options de connexion par défaut pour tous les comptes
Ce paramètre peut uniquement être configuré par les comptes administrateurs.

Dans Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Paramètres de compte {{< /AppElement >}} et cochez l'une des options dans la section **Authentification à deux facteurs**.

![Capture d'écran de la configuration de l'authentification à deux facteurs](/img/content/scr_2fa-authentication-setting.min.png)
- **Requise** : les [opérateurs de base]({{< ref path="/support/kb/account/users/operators/permissions#basic-operator" lang="fr" >}}) doivent utiliser l'authentification à deux facteurs au moyen d'un mot de passe à usage unique basé sur le temps.
- **Facultative** : les opérateurs de base peuvent choisir d'utiliser l'authentification à deux facteurs au moyen d'un mot de passe à usage unique basé sur le temps.
- **Désactivée** : l'authentification à deux facteurs au moyen d'un mot de passe à usage unique basé sur le temps n'est pas disponible pour ce compte.

## Paramétrage de l'authentification à deux facteurs pour les opérateurs
Après avoir défini les options de connexion par défaut des opérateurs, sélectionnez une option de connexion dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}} de la page de l'opérateur, dans la section **Options de connexion pour cet opérateur**. Le statut par défaut de l'authentification à deux facteurs dans votre compte est précisé dans cette section, où vous pouvez aussi modifier ce paramètre pour cet opérateur particulier. (À noter que ce paramètre ne peut être modifié que par les comptes administrateurs.)

![Capture d'écran des options de connexion avec authentification à deux facteurs pour les opérateurs](/img/content/scr_2fa-operator-login-options.min.png)
Dans la partie **Authentification à deux facteurs**, cochez la case **Remplacer la configuration de l'authentification à deux facteurs** si vous souhaitez modifier les paramètres.
- **Requise** : l'authentification à deux facteurs doit être utilisée. L'option sera activée lors de la prochaine connexion de l'opérateur.
- **Facultative** : l'authentification à deux facteurs peut être configurée manuellement sur cette page.
- **Désactivée** : l'authentification à deux facteurs n'est pas disponible.

Pour paramétrer à nouveau la configuration de l'authentification à deux facteurs, cliquez sur le bouton {{< AppElement type="deletebutton" >}} Réinitialiser l'authentification à deux facteurs {{< /AppElement >}}.

{{< callout >}}
**Remarque :** l'authentification à deux facteurs au moyen d'un mot de passe à usage unique basé sur le temps n'est pas compatible avec la fonctionnalité d'[authentification unique (Single Sign-on) dans Uptrends]({{< ref path="/support/kb/account/settings/single-sign-on-overview" lang="fr" >}}).
{{< /callout >}}

Les administrateurs et les opérateurs ont plusieurs possibilités pour activer l'authentification à deux facteurs.

### Dans les paramètres de l'opérateur
Dans Uptrends, ouvrez l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}} de la page de l'opérateur. Pour cela, il vous suffit de cliquer sur le nom de l'opérateur situé au bas du menu principal, puis de sélectionner {{< AppElement type="menuitem" >}} Paramètres utilisateur {{< /AppElement >}}. Cliquez ensuite sur le bouton {{< AppElement type="editbutton" >}} Scanner le code QR {{< /AppElement >}} pour configurer l'authentification à deux facteurs. Une fenêtre contextuelle s'ouvre.

Utilisez une application d'authentification de votre choix pour scanner le code QR. Si vous ne pouvez pas scanner le code, utilisez la fonctionnalité de saisie manuelle en cliquant sur le lien situé sous le code. Cliquez sur {{< AppElement type="buttonPrimary" >}} Suivant {{< /AppElement >}} et saisissez le code à six chiffres fourni. Cliquez sur {{< AppElement type="buttonPrimary" >}} Terminer {{< /AppElement >}} pour terminer la configuration de l'authentification à deux facteurs.

### Dans l'invitation envoyée à l'opérateur
Lorsqu'un opérateur devant utiliser l'authentification à deux facteurs est [invité à utiliser Uptrends]({{< ref path="support/kb/account/users/operators/add-or-delete-operator#by-invitation" lang="fr" >}}), le processus d'authentification à deux facteurs est inclus dans l'acceptation de l'invitation. Le processus est le même : une application d'authentification au choix fournit un mot de passe à usage unique basé sur le temps.

### Avec un lien envoyé par e-mail
Après s'être connecté, un opérateur devant utiliser l'authentification à deux facteurs verra s'afficher une page l'informant de la réception d'un e-mail. Cet e-mail contient un lien avec une page d'Uptrends où l'authentification à deux facteurs peut être activée. L'opérateur peut ainsi se connecter. Par la suite, l'opérateur devra se connecter au moyen d'un mot de passe à usage unique basé sur le temps.