{
  "hero": {
    "title": "Problèmes liés aux alertes SMS et vocales en Chine et en Inde"
  },
  "title": "Problèmes liés aux alertes SMS et vocales en Chine et en Inde",
  "summary": "En raison des filtres antispam et des listes de numéros de téléphone exclus, les messages d’alerte peuvent ne pas fonctionner dans certaines régions. Voici les autres options disponibles pour vos opérateurs situés en Chine et en Inde.  ",
  "url": "[URL_BASE_TOPICS]alerter/problemes-d-alerte-sms-et-vocaux-en-chine-et-en-inde",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Vos opérateurs situés en Chine ou en Inde rencontrent des problèmes pour recevoir les alertes ou ne reçoivent que certains alertes ? En effet, la réglementation chinoise et le registre indien des préférences des consommateurs (aussi connu sous le nom de "Do Not Disturb Registry") bloquent certains appels téléphoniques et SMS.

## Filtrage des spams en Chine

La Chine surveille les appels et les SMS provenant de l’extérieur du pays et bloque ceux qu’elle considère comme des spams. La plateforme d’API [Twilio]([LINK_URL_1]) résume ainsi la situation :

« Nos partenaires en charge des réseaux et des opérations doivent remplir des normes très strictes pour transmettre des appels en Chine. Ces normes rejettent les appels de moins de deux minutes ainsi que les volumes d’appels élevés, et les entités qui ne respectent pas ces règles risquent d’être interdites de façon complète et permanente, sans avertissement. Pour rester conforme à nos partenaires, Twilio ne peut plus passer des appels de courte durée en Chine. Ce problème s’applique à tous les appels internationaux vers la Chine et ne concerne pas uniquement notre plateforme. Pour de plus amples détails, veuillez consulter notre FAQ sur la limitation des appels vers la Chine. »

Plusieurs facteurs liés aux exigences strictes de la Chine concernant les appels et les SMS empêchent la distribution de nos messages d’alerte :

- Durée d’appel moyenne de deux minutes minimum : les messages vocaux d’Uptrends émis par téléphone ou par message vocal ne peuvent pas respecter ce critère.
- Des appels fréquents proviennent du même numéro.
- L’envoi de trois SMS contenant le même texte constitue un bloc. Selon vos paramètres d’escalade, les messages d’alerte peuvent être envoyés plus de trois fois.
- L’envoi vers la Chine de cinq messages différents depuis un même numéro déclenche une vérification manuelle et un blocage de 24 h applicable à tous les messages.

Comme indiqué ci-dessus, les **SMS envoyés à des numéros situés en Chine ne fonctionnent pas de façon fiable, voire pas du tout, et les messages vocaux et les alertes par téléphone ne fonctionnent pas du tout.** Nous vous recommandons vivement d’envisager d’adopter l’une des méthodes d’alerte décrites ci-dessous.

## Blocage d’appels et de SMS en Inde

Si votre opérateur situé en Inde ne reçoit pas les messages d’alerte vocaux ou SMS de la part d’Uptrends, il est probable que son numéro se trouve sur la liste [National Customer Preference Register]([LINK_URL_2]). Cette liste permet aux consommateurs de bloquer les appels et les SMS pour une partie ou l’intégralité des secteurs d’activité. Si le numéro de l’opérateur a été enregistré, il doit attendre trois mois pour le retirer de la liste de blocage.

## Solutions permettant de remplacer l’envoi de SMS et de messages vocaux vers la Chine et l’Inde

Uptrends propose plusieurs autres options pour envoyer des alertes à vos opérateurs situés en Chine et en Inde.

- **E-mail** : les e-mails constituent un outil efficace pour alerter les opérateurs pendant leurs horaires de service.
- [**Intégrations**]([LINK_URL_3]) : si vous utilisez Slack, PagerDuty, StatusHub, Splunk On-Call (anciennement VictorOps) ou ServiceNow, vous pouvez facilement les intégrer à votre compte Uptrends pour envoyer des messages à vos opérateurs situés en Chine et en Inde.
- [**Webhooks**]([LINK_URL_4]) : si votre application ou votre service tiers peut recevoir et traiter des requêtes d’API, vous pouvez envoyer des alertes d’Uptrends à travers ces services.
- **Notifications push depuis l’application Uptrends** : l’[application Uptrends]([LINK_URL_5]) pour iPhone et Android peut envoyer des notifications push à vos opérateurs.
