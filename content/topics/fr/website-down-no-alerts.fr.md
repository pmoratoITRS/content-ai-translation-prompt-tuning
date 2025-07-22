{
  "hero": {
    "title": "Mon site web est en panne mais je ne reçois pas d'alertes"
  },
  "title": "Mon site est en panne",
"summary": "Votre site web est en panne mais vous n'avez pas reçu d'alerte ? Voici ce que vous devez faire.",
  "url": "/support/kb/alerter/site-en-panne-pas-d-alertes",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/website-down-no-alerts"
}

Votre site web, votre serveur ou votre service web est tombé en panne, mais vous n'avez reçu ni alerte ni message. Alors, que se passe-t-il ? L'absence d'alerte ou de message peut avoir plusieurs causes.

Souvenez-vous que l'envoi d'alertes repose sur plusieurs étapes. Tout d'abord, le moniteur signale une erreur. Si l'erreur est confirmée, cela peut générer une alerte, qui peut à son tour déclencher l'envoi d'un message (défini dans une intégration). Pour approfondir la question, reportez-vous à l'article [Présentation des alertes]({{< ref path="support/kb/alerting/alerting-overview" lang="fr" >}}) En résumé, le problème peut provenir du moment où l'alerte doit être générée ou du moment où le message doit être envoyé.

Si vous n'avez pas vu d'alerte ni reçu de message, et que cela vous semble anormal, nous vous invitons à vérifier les différents points ci-dessous.

## Vérifiez votre moniteur

- **Votre moniteur est-il actif ?**  
   Si un moniteur est désactivé, vous ne recevez aucune alerte, car le moniteur n'effectue pas de surveillance.
- **Les alertes sont-elles activées ?**  
   L'état d'activation du moniteur et celui des alertes se trouvent dans le dashboard Statut moniteurs :

   ![Capture d'écran du dashboard Statut moniteurs](/img/content/scr_monitor-status-dashboard-alerting.min.png)

- **Vous reste-t-il des crédits de message ?**  
   L'envoi de messages téléphoniques ou SMS consomme des crédits de message. Si votre stock de crédits est épuisé, vous ne recevrez pas de messages tant que vous n'aurez pas acheté de nouveaux crédits de message. Pour en savoir plus, lisez l'article [Utilisation du crédit SMS]({{< ref path="support/kb/alerting/sms-credit-usage" lang="fr" >}}).
- **L'erreur s'est-elle produite pendant la période de maintenance du moniteur ?**  
   Les alertes ne sont pas envoyées au cours des [périodes de maintenance]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="fr" >}}) programmées des moniteurs. Ce paramètre se trouve dans l'onglet {{< AppElement type="tab" >}}Périodes de maintenance{{< /AppElement >}} du moniteur.
- **Avez-vous configuré une vérification de contenu dans vos conditions d'erreur ?**  
   Si vous avez configuré une *recherche de correspondance de contenu*, une partie ou l'ensemble du contenu vérifié doit correspondre exactement au mot ou à la phrase que vous recherchez.

## Vérifiez l'historique de vos alertes

L'application Uptrends conserve un journal des alertes. Cet historique des alertes est l'un des outils les plus importants pour vérifier si des messages ont été envoyés. Dans le cas contraire, c'est là qu'il faut regarder.

Pour vérifier si des alertes ont été générées et des messages envoyés, procédez comme suit :  
Dans l'application Uptrends, ouvrez le menu {{< AppElement type="menuitem" >}}Alertes > Historique des alertes{{< /AppElement >}}.   
Cette page affiche un journal d'activité de toutes les alertes qui ont été envoyées, y compris la date et l'heure, le niveau d'escalade et les paramètres des rappels.

Cliquez sur une alerte pour obtenir des informations détaillées la concernant. Une fenêtre s'affiche avec deux onglets : {{< AppElement type="tab" >}}Détails{{< /AppElement >}} et {{< AppElement type="tab" >}}Messages{{< /AppElement >}}.

![Capture d'écran du dashboard Historique des alertes présentant les détails de l'alerte](/img/content/scr_alert-history-with-detail.min.png)

Plusieurs situations sont possibles :

- **L'historique d'alertes ne contient aucune entrée.**  
   Dans ce cas, vérifiez les paramètres de votre moniteur, puis les définitions des alertes.
- **L'alerte est là, mais aucun message n'a été envoyé.**  
   Dans l'onglet Messages, vous pouvez voir quels messages ont été envoyés et à qui.
- **Aucun message n'a été envoyé d'après votre intégration personnalisée.**  
   Vérifiez dans l'onglet Messages pour voir si une erreur a été renvoyée par le service tiers. Dans l'exemple ci-dessus, si Slack n'a pas reçu le message correctement, l'entrée "Slack to Master operator" sera marquée en rouge et la réponse de l'API Slack (avec les codes d'erreur et les informations) s'affichera lorsque vous cliquez dessus.

## Vérifiez les paramètres de l'opérateur

{{< callout >}}
**Remarque** : Il faut disposer de droits d'administrateur pour accéder aux informations de compte des opérateurs. Sans droits d'administrateur, vous ne pouvez vérifier que votre propre compte.
{{< /callout >}}

Pour afficher les paramètres d'un opérateur, ouvrez le menu {{< AppElement type="menuitem" >}}Configuration de compte > Opérateurs{{< /AppElement >}} puis, dans la liste, sélectionnez l'opérateur qui ne reçoit pas de messages.

Effectuez les vérifications suivantes :

- Le numéro de téléphone et l'adresse e-mail de l'opérateur en question sont-ils corrects ?  
   {{< callout >}}**Remarque** : Pour le numéro de téléphone, assurez-vous que le code de pays et l'indicatif régional sont correctement renseignés.{{< /callout >}}
- L'opérateur en question est-il répertorié comme en service ?  
   ![](/img/content/94102310-1e38-4f93-af1d-01a1fdeeb418.png)
- Essayez d'envoyer un SMS de test à partir des paramètres de l'opérateur ( {{< AppElement type="menuitem" >}}Configuration de compte > Opérateurs{{< /AppElement >}}) pour vérifier que tout fonctionne. Si le SMS n'est pas reçu dans les 10 minutes, essayez de modifier la passerelle SMS.  
   Cela peut se faire au moyen d'un paramètre général (valable pour tous les opérateurs) qui est disponible dans l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}} de l'intégration SMS, où vous pouvez sélectionner un autre *Opérateur SMS*.  
   Vous pouvez aussi modifier les paramètres d'un opérateur individuel dans les *Paramètres téléphone* dans l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}} de l'opérateur. Lorsque l'opérateur se trouve dans un autre endroit, il est parfois nécessaire de modifier la passerelle séparément.  
   Modifiez la passerelle et refaites le test.  
   {{< callout >}}**Remarque** : Les alertes SMS et vocales envoyées aux numéros de téléphone des opérateurs situés en Chine et en Inde peuvent être bloquées en raison des filtres anti-spam nationaux ou des registres de numéros exclus. [En savoir plus.]({{< ref path="support/kb/alerting/china-india-sms-voice-alert-issues" lang="fr" >}}) {{< /callout >}}
- Essayez d'envoyer un e-mail de test à partir des paramètres de l'opérateur pour vérifier le bon fonctionnement.  {{< callout >}}**Remarque** : Si vous ne recevez pas d'e-mails, vérifiez la liste noire et le dossier spam dans votre messagerie, car les messages y sont parfois redirigés. Des recommandations concernant l'établissement d'une [liste blanche](#check-your-ip-whitelist) sont fournies à la fin de cet article.{{< /callout >}}

Pour en savoir plus sur l'envoi de messages de test, lisez notre article [Tester les messages d’alerte]({{< ref path="support/kb/alerting/testing-alert-configurations" lang="fr" >}}).

## Vérifiez vos définitions d'alertes et vos niveaux d'escalade

Pour générer des alertes, une définition d'alerte doit exister et un moniteur doit lui être affecté. Pour que des messages soient envoyés, au moins un niveau d'escalade doit être défini et actif.

- **La définition de l'alerte est-elle activée ?**  
   Le paramètre se trouve dans l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}} de la définition d'alerte.
- **Le service surveillé est-il affecté à une définition d'alerte ?**  
   Vérifiez toutes vos définitions d'alerte pour savoir à quels moniteurs elles sont attachées. Si vous avez de nombreuses définitions d'alerte et que vous ne trouvez pas les informations que vous recherchez, ouvrez un [ticket de support]({{< ref path="contact" lang="fr" >}}) pour obtenir de l'aide.
- **Les niveaux d'escalade sont-ils actifs ?**  
   Vérifiez ce paramètre dans l'onglet {{< AppElement type="tab" >}} Niveau d'escalade {{< /AppElement >}} correspondant.
- **Comment la génération d'alerte est-elle configurée ?**  
   Il est important de noter que ces paramètres déterminent comment et quand les alertes sont envoyées en cas d'erreurs confirmées ou non confirmées.  
   **Par exemple :**  
   La règle *Générer une alerte quand 1 erreur ou plus se sont produites* signifie que nous envoyons une alerte uniquement lorsqu'une erreur a été confirmée. Cette erreur confirmée affiche alors une barre rouge dans le journal de votre moniteur.  
   La règle *Générer une alerte quand 2 erreurs ou plus se sont produites* signifie que nous envoyons une alerte uniquement lorsque 2 erreurs se sont produites consécutivement (sans vérification OK entre elles).

## Vérifiez votre liste blanche des IP et vos paramètres d'e-mail {id="check-your-ip-whitelist"}

- Il se peut que vos serveurs de messagerie bloquent les e-mails d'alerte ou les classent comme spam. Pour éviter cela, ajoutez à la liste blanche les adresses IP des serveurs Uptrends de messagerie. Pour connaître les adresses IP utilisées pour l'envoi des alertes par e-mail, lisez notre article [Adresses IP à mettre sur liste blanche]({{< ref path="support/kb/account/ip-addresses-for-whitelisting" lang="fr" >}}).
- Uptrends utilise les **signatures DKIM** pour l'authentification des e-mails. Cette méthode vise à lutter contre l'usurpation d'identité et le hameçonnage en ajoutant une signature aux messages sortants, tels que les e-mails d'alerte. Si le dispositif DKIM échoue pour une raison ou pour une autre, l'e-mail est marqué comme spam.
