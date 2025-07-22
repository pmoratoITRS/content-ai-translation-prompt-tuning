{
  "title": "MonitorCheck API",
  "url": "/support/kb/api/monitorcheck-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorcheck-api"
}

Les données de vérification du moniteur peuvent être récupérées depuis les endpoints de l'API **MonitorCheck** qui font partie de [API v4](/support/kb/api/v4). Les Monitor checks (vérifications de moniteur) sont les mesures individuelles que nous recueillons pour chaque moniteur, et le MonitorCheck API donne accès à ces données brutes. Une fois téléchargées, ces données peuvent être stockées dans une base de données soit pour une analyse hors ligne, soit pour un audit ou à des fins de sauvegarde. Les trois endpoints suivants sont disponibles :

| MonitorCheck endpoint      | **Utilisation**                                                   |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Retourne toutes les données du compte.                            |
| /MonitorCheck/Monitor      | Retourne les données de vérification pour un moniteur spécifique. |
| /MonitorCheck/MonitorGroup | Retourne les données de vérification pour un groupe de moniteurs. |

Un scénario typique consiste à télécharger vos données (pour tous les moniteurs, pour un groupe ou un moniteur spécifique) pour une période particulière (pour le mois précédent, par exemple). En fonction du nombre de vos moniteurs et l'intervalle de surveillance, cela peut représenter une grande quantité de données. Une bonne façon de faire des appels API rapides et réactifs, c'est de télécharger et traiter des données en paquets, par exemple 100 éléments à la fois. Les méthodes API du MonitorCheck sont optimisées pour le téléchargement des données en paquets.

Tous les endpoints MonitorCheck prennent les paramètres suivants :

|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Période à filtrer (par défaut : les dernières 24 heures). <br>Laissez ce champ vide si vous souhaitez spécifier une période personnalisée <br>en utilisant *start* et *end*. |
| **start**      | Le début d'une période personnalisée. <br>Laissez ce champ vide si vous utilisez le paramètre *period*.                                                                  |
| **end**        | La fin d'une période personnalisée. <br>Laissez ce champ vide si vous utilisez le paramètre *period*.                                                                    |
| **errorLevel** | Le niveau d'erreur minimum à retourner <br>(par défaut : NoError, ce qui signifie qu'aucun filtre n'est appliqué)                                                        |
| **cursor**     | Paramètre permettant de parcourir les données, voir ci-dessous.                                                                                                      |
| **take**       | Le nombre de lignes à renvoyer (par défaut : 100; c'est aussi le maximum).                                                                                           |
| **sorting**    | Spécifie si les données doivent être triées par date <br>en ordre Ascending ou Descending (par défaut : Descending)                                                      |

## Parcourir vos données à l'aide d'un curseur

Un curseur est une valeur de chaîne qui sert de pointeur dans vos données. Lorsque vous demandez une grande quantité de données (par exemple, toutes les données de surveillance du mois dernier), l'API renvoie le premier bloc de 100 éléments. Avec ces données, vous obtenez également une valeur de curseur que vous pouvez utiliser pour accéder facilement au deuxième bloc de données, etc. Vous pouvez répéter ce processus jusqu'à ce que vous ayez téléchargé toutes les données pour la période que vous avez demandée. Un curseur vide indique que vous avez atteint la fin de la séquence et qu’il n'y a plus de données à télécharger.

## En avant ou en arrière dans le temps

Vous pouvez décider si vous souhaitez commencer par des données récentes et remonter dans le temps (sorting=Descending), ou commencer au début d'une période et se déplacer vers l'heure actuelle (sorting=Ascending).  
  
Ce dernier est particulièrement utile et efficace si vous utilisez un processus automatisé qui reçoit des mises à jour régulières pour des données courantes. Par exemple, vous pouvez accéder à l’API toutes les 5 minutes en demandant Last24Hours, Ascending, et en spécifiant la valeur du curseur à partir de la réponse précédente : l'API ne retournera que les données générées depuis votre dernière demande d'API. Le résultat peut contenir une liste vide si aucune nouvelle donnée n'est encore disponible, mais si la réponse de l'API contient une valeur de curseur non vide, de nouvelles données peuvent être extraites dans une requête ultérieure.

## Récupérer les détails du MonitorCheck

Lorsque vous récupérez une liste de MonitorChecks, chaque entrée MonitorCheck contient les métriques de base pour cette vérification, comme décrit ci-dessous. Cependant, selon le type de moniteur, des données plus détaillées peuvent être disponibles. Ces détails peuvent être récupérés en utilisant des appels API distincts. Les liens entre le MonitorCheck principal et tous les détails connexes sont représentés par des relations. Lorsqu'un MonitorCheck a en effet un ou plusieurs détails qui lui sont liés, ils sont présentés dans le membre 'Relationships' (voir ci-dessous) : il contiendra un lien vers chaque bloc de détails donnant ainsi accès à ces données. Les détails suivants sont actuellement disponibles :

| Detail endpoint                            | Usage                                                                                                  |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------|
| /MonitorCheck/{monitorCheckId}/Http        | Retourne des détails d'une vérification HTTP, y compris le contenu HTML et les informations d'en-tête. |
| /MonitorCheck/{monitorCheckId}/Waterfall   | Retourne la graphique en cascade complète d'un Full Page Check ou d'une étape de transaction.          |
| /MonitorCheck/{monitorCheckId}/Transaction | Retourne les résultats de chaque étape de la transaction, y compris les durées des étapes.             |

## Structure de données générique

Une réponse MonitorCheck utilise le format suivant pour séparer les données réelles des métadonnées fournies :

### Root

Root contient les membres suivants :

|            |                                                                                                   |
|------------|---------------------------------------------------------------------------------------------------|
| **Data**   | Un tableau ou un objet unique contenant les données demandées <br>ou un sous-ensemble de ces données. |
| **Links**  | Des liens vers cet ensemble et vers le prochain ensemble de données.                              |
| **Cursor** | Contient les valeurs de curseur à utiliser pour parcourir l'ensemble de données.                  |

### Data

Ce membre peut contenir un tableau d'objets ou un objet unique. De toute façon, l'objet MonitorCheck ou les objets MonitorCheck à l'intérieur du tableau auront les membres suivants :

<table>
<thead>
  <tr>
    <th class="cell-small"></th>
    <th class="cell-large"></th>
    <th class="cell-large"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="bold">Id</td>
    <td>L’identifiant unique du monitor check. Cet ID correspond à l’identifiant du monitor check que vous voyez dans la barre d’adresse lorsque vous affichez les détails d’une vérification dans Uptrends.</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Type</td>
    <td>Le type d’objet (une valeur fixe “MonitorCheck" pour ces méthodes API).</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Attributes</td>
    <td>Les attributs de l’objet qui contient les données réelles. Ces attributs incluent :</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">MonitorGuid</td>
    <td>Le GUID du moniteur qui correspond à ce monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">Timestamp</td>
    <td>Date et heure auxquelles la vérification du moniteur a été effectuée en fonction de l’heure locale de l’opérateur connecté.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorCode</td>
    <td>Le code d’erreur numérique d’Uptrends en cas de résultat d’erreur ou 0 en cas de résultat OK.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalTime</td>
    <td>Le nombre de millisecondes nécessaires pour effectuer la vérification du moniteur.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolveTime</td>
    <td>Le nombre de millisecondes nécessaires pour exécuter la requête DNS pour cette vérification, le cas échéant.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ConnectionTime</td>
    <td>Le nombre de millisecondes nécessaires pour établir une connexion.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">DownloadTime</td>
    <td>Le nombre de millisecondes nécessaires pour télécharger les données de la réponse.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalBytes</td>
    <td>Le nombre d’octets téléchargés pour cette vérification.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolvedIpAddress</td>
    <td>L’adresse IP du nom de domaine spécifié lors de cette vérification du moniteur.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorLevel</td>
    <td>Une valeur qui représente l’état OK/Error pour cette vérification : NoError si le résultat était OK, Unconfirmed si une erreur a été trouvée, Confirmed si une erreur a été trouvée suite à une double vérification, juste après une erreur non confirmée.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorDescription</td>
    <td>Un texte décrivant l’erreur qui a été trouvée, ou OK si aucune erreur n’a été trouvée.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorMessage</td>
    <td>Toute information d’erreur supplémentaire, si elle existe.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ServerId</td>
    <td>L’ID du serveur de point de contrôle Uptrends qui a effectué cette vérification.</td>
  </tr>
   <tr>
    <td></td>
    <td class="bold">HttpStatusCode</td>
    <td>Le code de statut HTTP renvoyé (le cas échéant).</td>
  </tr>
  <tr>
    <td class="bold">Relationships</td>
    <td>Ce tableau contient une liste de données ou objets liés aux données actuelles. Cette liste peut contenir des liens pour récupérer les données associées. Les données de relation ont la même structure, en ce sens que ces entrées contiennent également les membres Id, Type et Links.</td>
    <td></td>
  </tr>
</tbody>
</table>