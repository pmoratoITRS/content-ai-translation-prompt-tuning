{
"hero": {
"title": "Variables système d'alerte"
},
"title": "Variables système d'alerte",
"summary": "Vue d'ensemble des variables système disponibles pour les intégrations (personnalisées)",
"url": "/support/kb/alerter/integrations/integrations-personnalisees/variables-systeme-alertes",
"translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/alerting-system-variables",
"tableofcontents": false
}

Cet article présente toutes les **variables système** qui peuvent être utilisées pour compléter le message d'alerte sortant avec des informations pertinentes concernant le moniteur d'où provient l'alerte, le type d'erreur ou l'alerte elle-même. Pour plus d'informations sur l'utilisation de ces variables système, lisez notre article qui explique comment [créer le bon contenu de message]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content" lang="fr" >}}).

Les variables ci-dessous doivent être placées entre doubles accolades dans le contenu du message. Par exemple : `{{@alert.alertGuid}}`.

| Variable | Description | Exemple de valeur |
| --- | --- | --- |
| `@account.accountId` | Votre identifiant de compte Uptrends | `299840` |
| `@alert.alertGuid` | Identifiant unique de cette alerte | `cbfc7769-edb2-46a7-89d0-1e1b1fb0815b` |
| `@alert.checkpointName` | Contient le nom ou l'emplacement du checkpoint où l'alerte a été vérifiée en dernier. | `Ghent, Belgium` |
| `@alert.description` | Description textuelle de l'erreur qui a déclenché cette alerte. Le numéro d'étape est inclus le cas échéant. | `Étape 1 : La navigation vers https://www.galacticresorts.com a échoué.` |
| `@alert.downtimeDuration` | Temps écoulé entre la première erreur et l'alerte (OK) actuelle | `48:03:21` |
| `@alert.errorTypeId` | {{< tableformatter >}} Identifiant du type de l'erreur qui a déclenché cette alerte. Pour consulter la liste de types d'erreur, reportez-vous à la page [Types d'erreurs]({{< ref path="/support/kb/alerting/errors/error-types" lang="fr" >}}). {{< /tableformatter >}} | `5407` |
| `@alert.failureMessage` | Message d'échec personnalisé de l'action d'une étape de transaction d'où provient l'erreur | `Échec de connexion` |
| `@alert.firstError` | Même date et heure qu'avec la variable @alert.firstErrorUtc, mais d'après le fuseau horaire de votre compte. Également formaté en ISO 8601. | `2018-11-08T10:21:58` |
| `@alert.firstErrorCheckId` | Identifiant de l'erreur qui a déclenché cette alerte | `30833627687` |
| `@alert.firstErrorCheckUrl` | URL d'un lien profond qui fournit les détails de l'erreur ayant déclenché cette alerte | `https://app.uptrends.com/Report/ProbeLog/Check/30833627687` |
| `@alert.firstErrorDescription` | Description de l'erreur de la première vérification effectuée par le moniteur ayant reçu l'erreur. Le numéro d'étape est inclus le cas échéant. | `Étape 1 : La navigation vers https://www.galacticresorts.com a échoué.` |
| `@alert.firstErrorFormatted` | Même date et heure qu'avec la variable @alert.firstErrorUtc, mais d'après le fuseau horaire et la localisation de votre compte | `8/28/2020 12:23 PM` |
| `@alert.firstErrorUtc` | Date et heure de l'erreur d'origine qui a déclenché cette alerte, exprimées en heure UTC et présentées selon la norme ISO 8601 | `2018-11-08T16:21:58` |
| `@alert.firstErrorUtcFormatted` | Date et heure de l'erreur à l'origine de l'alerte, exprimées en heure UTC et présentées selon la localisation de votre compte | `8/28/2020 10:23 PM` |
| `@alert.numberOfConsecutiveErrors` | Contient le nombre total d'erreurs (confirmées) consécutives de l'alerte. | `2` |
| `@alert.resolvedIpAddress` | Adresse IP qui a été utilisée pour effectuer la vérification. Peut être une adresse IPv4 ou IPv6. | `178.217.84.4 OR 2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@‌alert.responseHeaders` | {{< tableformatter >}} Contient les en-têtes de réponse de l'alerte sous forme de paires clé-valeur. Notez que la valeur de cette variable peut être vide si la [protection des données des emplacements privés]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="fr" >}}) est activée sur le checkpoint privé vérifiant l'alerte. {{< /tableformatter >}} | `Content-Type": "text/html` |
| `@alert.responseBody` | {{< tableformatter >}} Contient le corps de la réponse reçue lorsqu'il est disponible. Notez que le corps de la réponse peut contenir des caractères qui doivent être encodés, par exemple [en utilisant @JsonEncode ou @XmlEncode]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-formatting" lang="fr" >}}). Le corps de la réponse sera tronqué si sa taille dépasse 1 Mo. {{< /tableformatter >}} | `{"Status": "error"}` |
| `@alert.serverIpv4` | Adresse IPv4 du serveur sur lequel la vérification a été effectuée | `178.217.84.4` |
| `@alert.serverIpv6` | Adresse IPv6 du serveur sur lequel la vérification a été effectuée. | `2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@alert.sslValidUntil` | Contient la date et l'heure d'expiration du certificat SSL, qui seront prises en compte pour les alertes du moniteur SSL. | `2024-11-07T15:05:43` |
| `@alert.timestamp` | Même date et heure qu'avec la variable @alert.timestampUtc, mais d'après le fuseau horaire de votre compte. Également formaté en ISO 8601. | `2018-11-08T10:26:58` |
| `@alert.timestampFormatted` | Même date et heure qu'avec la variable @alert.timestampUtc, mais d'après le fuseau horaire et la localisation de votre compte | `8/28/2020 12:23 PM` |
| `@alert.timestampUtc` | Date et heure de l'alerte, exprimées en heure UTC et présentées selon la norme ISO 8601 | `2018-11-08T16:26:58` |
| `@alert.timestampUtcFormatted` | Date et heure de l'alerte, exprimées en heure UTC et présentées selon la localisation de votre compte | `8/28/2020 10:23 PM` |
| `@alert.type` | Type de ce message d'alerte : <br><br>- Alerte : une nouvelle erreur a été détectée.<br>- Ok : l'erreur d'origine a été résolue.<br>- Rappel : l'erreur d'origine n'a pas été résolue. | `Alerte` \| `Ok` \| `Rappel` |
| `@alertDefinition.guid` | Identifiant unique de la définition d'alerte qui a été utilisée pour générer cette alerte | `2C97E464-6112-435B-8C8D-6DEF1E18273A` |
| `@alertDefinition.name` | Le nom de la définition d'alerte qui a été utilisée pour générer cette alerte | `Alerte par défaut` |
| `@CustomField(customFieldReference)` | {{< tableformatter >}} Référence à un [champ personnalisé]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#including-external-ids-or-custom-data" lang="fr" >}}) qui peut servir à inclure des données personnalisées pour les moniteurs individuels. {{< /tableformatter >}} | `Alerte pour l'équipe Ops` |
| `@escalationLevel.id` | Identifiant du niveau d'escalade utilisé pour générer cette alerte | `1` |
| `@escalationLevel.message` | Message personnalisé qui a été configuré pour ce niveau d'escalade | `Consultez la checklist THX-1138 pour étudier ce problème.` |
| `@incident.key` | Identifiant unique de l'incident associé à cette alerte. Une alerte d'erreur et une alerte Ok partagent la même clé d'incident. | `ba8ffcb7-5de0-489e-b649-f00f0b447e80-0-30099055746` |
| `@monitor.dashboardUrl` | URL d'un lien profond qui vous mène au dashboard de ce moniteur | `https://app.uptrends.com/Probe/Dashboard?probeGuids=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.editUrl` | URL d'un lien profond qui vous amène aux paramètres de ce moniteur | `https://app.uptrends.com/Report/Probe?probeGuid=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.monitorGuid` | Identifiant unique du moniteur de votre compte qui a déclenché cette alerte | `849b2046-213d-43ad-9efc-5af1faaeb222` |
| `@monitor.name` | Nom du moniteur de votre compte qui a déclenché cette alerte | `GalacticResorts.com - DNS` |
| `@monitor.notes` | Notes personnalisées ayant été ajoutées dans les paramètres du moniteur | `Il faut vérifier les entrées DNS d'Amazon Route53` |
| `@monitor.type` | Type de moniteur | `Transaction` |
| `@monitor.url` | Adresse réseau ou URL vérifiée par ce moniteur | `https://galacticresorts.com` |