{
"hero": {
"title": "Conditions d'erreur"
},
"title": "Conditions d'erreur",
"summary": "Cet article vous explique à quoi servent les conditions d'erreur et comment les utiliser. ",
"url": "/support/kb/surveillance-synthetique/parametres-moniteurs/conditions-erreur/apercu-des-conditions-derreur",
"translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
"tableofcontents": true,
"sectionlist": false
}

Les conditions d'erreur jouent un rôle essentiel dans la création de vos alertes de moniteur. La configuration d'une condition d'erreur est la première étape du [cycle du flux d'alertes et d'erreurs]({{< ref path="support/kb/alerting/alerting-overview" lang="fr" >}}) qui vous permet de recevoir des messages d'alerte.

Les **conditions d'erreur** vous permettent de définir un ensemble de critères pour informer votre moniteur des erreurs à surveiller sur votre site web, votre service web ou votre serveur. Elles indiquent à votre moniteur quel comportement de site web doit entraîner ou non une erreur.

Par exemple, si vous voulez vous assurer que le chargement de votre site web dure moins que trois secondes, vous pouvez définir une condition d'erreur en précisant les seuils applicables au temps de chargement de page. De même, si vous voulez vérifiez que les contenus, les plug-ins ou les scripts de votre site web se chargent correctement, vous pouvez définir des conditions d'erreur pour chacun de ces éléments.

Lorsqu'une condition d'erreur est remplie, une erreur est générée et une alerte est déclenchée. Si l'alerte a été configurée, vous recevez immédiatement un message d'alerte.

## Conditions d'erreur pour les types de moniteur {id="error-conditions-by-category"}

L'onglet {{< AppElement type="tab" >}} Conditions d'erreur {{< /AppElement >}} vous permet de configurer les différentes conditions d'erreur disponibles pour chaque type de moniteur. Notez que la disponibilité des conditions d'erreur varie selon la catégorie du moniteur et les données collectées :

![Capture d'écran de la configuration des conditions d'erreur du moniteur](/img/content/scr_monitor-setup-errorconditions.min.png)

### Moniteur de disponibilité

Les conditions d'erreur suivantes sont disponibles pour les [moniteurs de disponibilité]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}) :

| Type de moniteur | Conditions d'erreur |
|--|--|
| HTTPS, Webservice HTTP et HTTPS | {{< tableformatter >}}
- [Vérifier la disponibilité de la page]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="fr" >}})
- [Vérifier le contenu de la page]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="fr" >}})
- [Vérifier le temps de chargement de la page]({{< ref path="" lang="fr" >}})
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
   {{< /tableformatter >}} |
   | DNS, SSL, SFTP, FTP | {{< tableformatter >}}
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
- [Vérifier le temps de fonctionnement total]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}})
   {{< /tableformatter >}} |
   | SMTP, POP3, IMAP | {{< tableformatter >}}
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
- [Vérifier le temps de fonctionnement total]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}})
   {{< /tableformatter >}} |
   | Microsoft SQL Server, MySQL | {{< tableformatter >}}
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
- [Vérifier le temps de fonctionnement total]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}})
   {{< /tableformatter >}} |
   | Ping, Connect | {{< tableformatter >}}
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
- [Vérifier le temps de fonctionnement total]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}})
   {{< /tableformatter >}} |

### Moniteur de navigateur ou Full Page Check (FPC)

Les conditions d'erreur suivantes sont disponibles pour les [moniteurs de navigateur ou Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="fr" >}}) :

| Type de moniteur | Conditions d'erreur |
|--|--|
| Navigateur ou Full Page Check | {{< tableformatter >}}

- [Vérifier la disponibilité de la page]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="fr" >}})
- [Vérifier le contenu de la page]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="fr" >}})
- [Vérifier les URL chargées par la page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="fr" >}})
- [Vérifier le temps de chargement de la page]({{< ref path="" lang="fr" >}})
- [Vérifier les Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="fr" >}})
- [Vérifier les métriques W3C]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="fr" >}})
- [Vérifier le contenu de la console]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="fr" >}})
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
   {{< /tableformatter >}} |

### Moniteur de transaction

Les conditions d'erreur des [moniteurs de transactions]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="fr" >}}) sont aussi disponibles pour chaque étape. Selon la [configuration des étapes de transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}), les conditions d'erreur suivantes peuvent être ou non disponibles :

![Capture d'écran de la configuration des conditions d'erreur du moniteur](/img/content/scr-error-condition-transactions.min.png)

| Type de moniteur | Conditions d'erreur |
|--|--|
| Transaction ou Parcours utilisateur | {{< tableformatter >}}
- [Vérifications de contenu]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}})
- [Vérifier les ressources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="fr" >}})
- [Vérifier les URL chargées par la page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="fr" >}})
- [Vérifier les Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="fr" >}})
- [Vérifier les métriques W3C]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="fr" >}})
- [Vérifier le contenu de la console]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="fr" >}})
- [Vérifier la disponibilité du site]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="fr" >}})
- [Vérifier le temps de fonctionnement total]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="fr" >}})
   {{< /tableformatter >}} |

Notez que le [moniteur d'API multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="fr" >}}) détecte les erreurs selon une autre approche. Il utilise des **assertions** pour vous permettre de définir les vérifications à valider si la réponse de l'API répond à vos conditions. Pour en savoir plus, lisez notre article sur les [assertions pour la surveillance multi-étapes]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="fr" >}}).

## Configuration d'une condition d'erreur {id="configure-error-condition"}

Les conditions d'erreur peuvent être ajoutées lors de la [création d'un tout nouveau moniteur]({{< ref path="support/kb/basics/adding-monitors" lang="fr" >}}) ou de la modification d'un moniteur existant.

Pour configurer des conditions d'erreur :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Surveillance > Configuration du moniteur {{< /AppElement >}}.
2. Sélectionnez le moniteur auquel vous voulez ajouter une condition d'erreur.
3. Ouvrez l'onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}}.
4. Cliquez sur la condition d'erreur pour afficher toute la section et configurer les paramètres du moniteur.
5. (Facultatif) Pour ajouter de nouvelles vérifications à une condition d'erreur, cliquez sur le bouton {{< AppElement type="buttonSecondary" >}} \+ Nouvelle vérification {{< /AppElement >}}.
6. Poursuivez la configuration des conditions.
7. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.

Pour recevoir un message d'alerte lorsqu'une condition d'erreur est remplie, [créez une définition d'alerte]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="fr" >}}).

![Capture d'écran de la configuration des conditions d'erreur du moniteur](/img/content/gif-set-up-error-condition.gif)