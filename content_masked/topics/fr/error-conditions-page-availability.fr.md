{
  "hero": {
    "title": "Conditions d'erreur liées à la disponibilité"
  },
  "title": "Conditions d'erreur liées à la disponibilité",
  "summary": "Présentation des conditions d'erreur de la catégorie *Disponibilité*. ",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/conditions-erreur/conditions-erreur-disponibilite-page",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les conditions d'erreur disponibles dans la configuration du moniteur vous permettent de définir les situations qui doivent générer une erreur. Pour obtenir de plus amples informations, lisez l'article de notre base de connaissances [Conditions d'erreur]([LINK_URL_1]). Cet article vous explique notamment comment [configurer une condition d'erreur]([LINK_URL_2]).

La condition d'erreur **Disponibilité** vérifiera la disponibilité de la page (avec un moniteur HTTP/S ou webservice), du site (avec un moniteur de transaction) ou d'une ressource (avec d'autres moniteurs). Selon le type de moniteur, la condition d'erreur proposera des options distinctes. Pour en savoir plus, reportez-vous au tableau [Quelles conditions d’erreur sont disponibles ?]([LINK_URL_3]).

Par exemple, voici à quoi ressemble la vérification de disponibilité d'un moniteur HTTP(S) ou Webservice HTTP(S) :

![Capture d'écran de la section Vérifier la disponibilité de la page]([LINK_URL_4])

## Vérification de la disponibilité générale

Par défaut, tous les types de moniteurs vérifient la disponibilité du site web, de la page ou de la ressource sous surveillance.

Avec certains moniteurs, comme les moniteurs HTTP(S) ou Webservice HTTP(S), une réponse contenant un code de statut égal ou supérieur à 400 entraînera une erreur. Les autres types de moniteurs, tels que les moniteurs DNS, (S)FTP, serveurs mails ou serveurs de bases de données, ne vérifieront pas le code de statut de la réponse HTTP, mais la possibilité d'atteindre le serveur ou le service.

## Vérification du code de statut HTTP

Les types de moniteurs qui renvoient un code de statut HTTP permettent aussi de vérifier un code de statut spécifique.

Il peut arriver que vous ayez besoin de surveiller un code indiquant une erreur ou un dysfonctionnement. Par exemple, si vous mettez en place une redirection d'une ancienne page web vers une nouvelle page, vous avez besoin de savoir si la redirection fonctionne ou non. Si vous voulez surveiller une réponse spécifique, sélectionnez l'option **Vérifiez que le code de statut HTTP de la réponse correspond à…** et choisissez un code de statut dans la liste.

Pour consulter la liste complète des codes de statut, vous pouvez consulter la page [HTTP Status Code Registry]([LINK_URL_5]) (en anglais) de l'Internet AssignedNumbers Authority's (IANA), ou cette page en français.