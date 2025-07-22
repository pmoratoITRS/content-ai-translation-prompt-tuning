{
"hero": {
"title": "Paramètres principaux des opérateurs"
},
"title": "Paramètres principaux des opérateurs",
"summary": "Chaque opérateur doit être configuré correctement, c'est-à-dire avec ses coordonnées, ses informations de connexion et ses droits d'accès, mais aussi ses paramètres de fuseau horaire et de langue.",
"url": "/support/kb/compte/utilisateurs/operateurs/parametres-principaux",
"translationKey": "https://www.uptrends.com/support/kb/account/users/operators/main-settings"
}

Après avoir [ajouté un opérateur]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="fr" >}}), vous devez configurer un certain nombre de paramètres, à commencer par ceux qui se trouvent dans l'onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}} de la page de l'opérateur. Les options de paramétrage sont décrites dans cet article. Vous devez avoir des droits d'administrateur pour ajouter et configurer des opérateurs.

## Informations de connexion {id="logininfo"}
Les informations de connexion sont indiquées lors de la configuration de l'opérateur. Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Ajouter ou supprimer un opérateur]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="fr" >}}).

## Paramètres de langue {id="langsettings"}
La **langue** est définie lors de la configuration du compte. La langue définie dans les paramètres de compte qui servira à l'affichage et sera utilisée par défaut. Pour modifier la langue du compte, cliquez sur **Remplacer la langue du compte** et sélectionnez une autre langue dans le menu déroulant.

## Rôle de l'opérateur {id="operatorrole"}
Le paramètre **Rôle de l'opérateur** permet d'indiquer le rôle que des opérateurs spécifiques ont dans l'entreprise, à titre de référence interne. Le rôle spécial *Utilisateur pour la gestion des alertes* peut être utilisé pour indiquer qu'un opérateur particulier doit être utilisé uniquement pour la réception, l'analyse et le traitement des e-mails d'alerte.

## Paramètres d'abonnement à la newsletter {id="newslettersub"}
Les options d'**abonnement à la newsletter** permettent aux opérateurs (et aux administrateurs) d'indiquer quels types d'e-mails ils souhaitent recevoir. Les options permettent de s'abonner aux *mises à jour sur les fonctionnalités*, qui sont des messages d'ordre général sur les fonctionnalités récentes ou récemment actualisées, et aux *mises à jour sur les checkpoints*, qui contiennent des informations concernant notre [réseau de checkpoints]({{< ref path="/checkpoints" lang="fr" >}}) (ajout de nouveaux checkpoints, suppression d'anciens checkpoints, modification des adresses IP, etc.).

Par défaut, les opérateurs reçoivent des e-mails contenant les mises à jour sur les fonctionnalités. Les mises à jour sur les checkpoints sont uniquement envoyées aux [administrateurs de compte]({{< ref path="/support/kb/account/users/operators/giving-an-operator-administrator-rights" lang="fr" >}}). Les opérateurs sont alors considérés comme des [contacts techniques]({{< ref path="/support/kb/account/users/operators/permissions#technical-contact" lang="fr" >}}).

## Dashboard par défaut {id="defaultdash"}
Le **dashboard par défaut** est configuré sur l'option {{< AppElement type="dropdown" >}} tel que spécifié par votre administrateur {{< /AppElement >}} lors de la configuration du compte. Toutefois, il est ensuite possible de sélectionner un autre dashboard dans le menu déroulant.

Pour en savoir plus sur les dashboards, référez-vous à l'article de notre base de connaissances intitulé [Dashboards et pages de statut publiques]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/" lang="fr" >}}).

## Paramètres du fuseau horaire {id="timezone"}
Lors de la configuration du compte Uptrends (à la première connexion), le [fuseau horaire]({{< ref path="support/kb/account/settings/timezones" lang="fr" >}}) est appliqué au compte dans son intégralité. Ce paramètre s'applique donc à tous les opérateurs qui sont ajoutés au compte Uptrends. Vous pouvez les retrouver dans le menu {{< AppElement type="menuitem" >}} Configuration de compte > Paramètres de compte {{< /AppElement >}}.


Si vous avez un [compte Enterprise]({{< ref path="/pricing#plans" lang="fr" >}}), vous pouvez définir un autre fuseau horaire pour les opérateurs. Cette option peut s'avérer utile lorsque vos opérateurs travaillent dans un autre fuseau horaire que celui défini par défaut pour votre compte Uptrends.

Dans la section **Paramètres du fuseau horaire**, choisissez l'option *Fuseau horaire supplémentaire* et sélectionnez le fuseau applicable dans la liste. Cliquez ensuite sur le bouton {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour activer cette option.

L'opérateur dispose désormais d'un plus grand nombre d'informations au niveau des horodatages :

- Les détails de la vérification du moniteur indiquent les horodatages basés sur le fuseau horaire par défaut et le fuseau horaire personnalisé.
- Dans le dashboard **Journal moniteurs** (accessible depuis le menu {{< AppElement type="menuitem" >}} Surveillance > Journal moniteurs {{< /AppElement >}}), le fuseau horaire personnalisé s'affiche lorsque l'on survole l'horodatage d'une ligne du journal.

## Paramètres de téléphone {id="phonesettings"}
Un numéro de téléphone mobile est indiqué lors de la configuration de l'opérateur. Pour en savoir plus, lisez l'article de notre base de connaissances intitulé [Ajouter ou supprimer un opérateur]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="fr" >}}).