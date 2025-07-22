{
  "title": "MonitorCheck API",
  "url": "[URL_BASE_TOPICS]api/monitorcheck-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les données de vérification du moniteur peuvent être récupérées depuis les endpoints de l'API **MonitorCheck** qui font partie de [API v4]([LINK_URL_1]). Les Monitor checks (vérifications de moniteur) sont les mesures individuelles que nous recueillons pour chaque moniteur, et le MonitorCheck API donne accès à ces données brutes. Une fois téléchargées, ces données peuvent être stockées dans une base de données soit pour une analyse hors ligne, soit pour un audit ou à des fins de sauvegarde. Les trois endpoints suivants sont disponibles :

| MonitorCheck endpoint      | **Utilisation**                                                   |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Retourne toutes les données du compte.                            |
| /MonitorCheck/Monitor      | Retourne les données de vérification pour un moniteur spécifique. |
| /MonitorCheck/MonitorGroup | Retourne les données de vérification pour un groupe de moniteurs. |

Un scénario typique consiste à télécharger vos données (pour tous les moniteurs, pour un groupe ou un moniteur spécifique) pour une période particulière (pour le mois précédent, par exemple). En fonction du nombre de vos moniteurs et l'intervalle de surveillance, cela peut représenter une grande quantité de données. Une bonne façon de faire des appels API rapides et réactifs, c'est de télécharger et traiter des données en paquets, par exemple 100 éléments à la fois. Les méthodes API du MonitorCheck sont optimisées pour le téléchargement des données en paquets.

Tous les endpoints MonitorCheck prennent les paramètres suivants :

|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Période à filtrer (par défaut : les dernières 24 heures). [HTML_TAG_1]Laissez ce champ vide si vous souhaitez spécifier une période personnalisée [HTML_TAG_2]en utilisant *start* et *end*. |
| **start**      | Le début d'une période personnalisée. [HTML_TAG_3]Laissez ce champ vide si vous utilisez le paramètre *period*.                                                                  |
| **end**        | La fin d'une période personnalisée. [HTML_TAG_4]Laissez ce champ vide si vous utilisez le paramètre *period*.                                                                    |
| **errorLevel** | Le niveau d'erreur minimum à retourner [HTML_TAG_5](par défaut : NoError, ce qui signifie qu'aucun filtre n'est appliqué)                                                        |
| **cursor**     | Paramètre permettant de parcourir les données, voir ci-dessous.                                                                                                      |
| **take**       | Le nombre de lignes à renvoyer (par défaut : 100; c'est aussi le maximum).                                                                                           |
| **sorting**    | Spécifie si les données doivent être triées par date [HTML_TAG_6]en ordre Ascending ou Descending (par défaut : Descending)                                                      |

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
| **Data**   | Un tableau ou un objet unique contenant les données demandées [HTML_TAG_7]ou un sous-ensemble de ces données. |
| **Links**  | Des liens vers cet ensemble et vers le prochain ensemble de données.                              |
| **Cursor** | Contient les valeurs de curseur à utiliser pour parcourir l'ensemble de données.                  |

### Data

Ce membre peut contenir un tableau d'objets ou un objet unique. De toute façon, l'objet MonitorCheck ou les objets MonitorCheck à l'intérieur du tableau auront les membres suivants :

[HTML_TAG_8]
[HTML_TAG_9]
  [HTML_TAG_10]
    [HTML_TAG_11][HTML_TAG_12]
    [HTML_TAG_13][HTML_TAG_14]
    [HTML_TAG_15][HTML_TAG_16]
  [HTML_TAG_17]
[HTML_TAG_18]
[HTML_TAG_19]
  [HTML_TAG_20]
    [HTML_TAG_21]Id[HTML_TAG_22]
    [HTML_TAG_23]L’identifiant unique du monitor check. Cet ID correspond à l’identifiant du monitor check que vous voyez dans la barre d’adresse lorsque vous affichez les détails d’une vérification dans Uptrends.[HTML_TAG_24]
    [HTML_TAG_25][HTML_TAG_26]
  [HTML_TAG_27]
  [HTML_TAG_28]
    [HTML_TAG_29]Type[HTML_TAG_30]
    [HTML_TAG_31]Le type d’objet (une valeur fixe “MonitorCheck" pour ces méthodes API).[HTML_TAG_32]
    [HTML_TAG_33][HTML_TAG_34]
  [HTML_TAG_35]
  [HTML_TAG_36]
    [HTML_TAG_37]Attributes[HTML_TAG_38]
    [HTML_TAG_39]Les attributs de l’objet qui contient les données réelles. Ces attributs incluent :[HTML_TAG_40]
    [HTML_TAG_41][HTML_TAG_42]
  [HTML_TAG_43]
  [HTML_TAG_44]
    [HTML_TAG_45][HTML_TAG_46]
    [HTML_TAG_47]MonitorGuid[HTML_TAG_48]
    [HTML_TAG_49]Le GUID du moniteur qui correspond à ce monitor check.[HTML_TAG_50]
  [HTML_TAG_51]
  [HTML_TAG_52]
    [HTML_TAG_53][HTML_TAG_54]
    [HTML_TAG_55]Timestamp[HTML_TAG_56]
    [HTML_TAG_57]Date et heure auxquelles la vérification du moniteur a été effectuée en fonction de l’heure locale de l’opérateur connecté.[HTML_TAG_58]
  [HTML_TAG_59]
  [HTML_TAG_60]
    [HTML_TAG_61][HTML_TAG_62]
    [HTML_TAG_63]ErrorCode[HTML_TAG_64]
    [HTML_TAG_65]Le code d’erreur numérique d’Uptrends en cas de résultat d’erreur ou 0 en cas de résultat OK.[HTML_TAG_66]
  [HTML_TAG_67]
  [HTML_TAG_68]
    [HTML_TAG_69][HTML_TAG_70]
    [HTML_TAG_71]TotalTime[HTML_TAG_72]
    [HTML_TAG_73]Le nombre de millisecondes nécessaires pour effectuer la vérification du moniteur.[HTML_TAG_74]
  [HTML_TAG_75]
  [HTML_TAG_76]
    [HTML_TAG_77][HTML_TAG_78]
    [HTML_TAG_79]ResolveTime[HTML_TAG_80]
    [HTML_TAG_81]Le nombre de millisecondes nécessaires pour exécuter la requête DNS pour cette vérification, le cas échéant.[HTML_TAG_82]
  [HTML_TAG_83]
  [HTML_TAG_84]
    [HTML_TAG_85][HTML_TAG_86]
    [HTML_TAG_87]ConnectionTime[HTML_TAG_88]
    [HTML_TAG_89]Le nombre de millisecondes nécessaires pour établir une connexion.[HTML_TAG_90]
  [HTML_TAG_91]
  [HTML_TAG_92]
    [HTML_TAG_93][HTML_TAG_94]
    [HTML_TAG_95]DownloadTime[HTML_TAG_96]
    [HTML_TAG_97]Le nombre de millisecondes nécessaires pour télécharger les données de la réponse.[HTML_TAG_98]
  [HTML_TAG_99]
  [HTML_TAG_100]
    [HTML_TAG_101][HTML_TAG_102]
    [HTML_TAG_103]TotalBytes[HTML_TAG_104]
    [HTML_TAG_105]Le nombre d’octets téléchargés pour cette vérification.[HTML_TAG_106]
  [HTML_TAG_107]
  [HTML_TAG_108]
    [HTML_TAG_109][HTML_TAG_110]
    [HTML_TAG_111]ResolvedIpAddress[HTML_TAG_112]
    [HTML_TAG_113]L’adresse IP du nom de domaine spécifié lors de cette vérification du moniteur.[HTML_TAG_114]
  [HTML_TAG_115]
  [HTML_TAG_116]
    [HTML_TAG_117][HTML_TAG_118]
    [HTML_TAG_119]ErrorLevel[HTML_TAG_120]
    [HTML_TAG_121]Une valeur qui représente l’état OK/Error pour cette vérification : NoError si le résultat était OK, Unconfirmed si une erreur a été trouvée, Confirmed si une erreur a été trouvée suite à une double vérification, juste après une erreur non confirmée.[HTML_TAG_122]
  [HTML_TAG_123]
  [HTML_TAG_124]
    [HTML_TAG_125][HTML_TAG_126]
    [HTML_TAG_127]ErrorDescription[HTML_TAG_128]
    [HTML_TAG_129]Un texte décrivant l’erreur qui a été trouvée, ou OK si aucune erreur n’a été trouvée.[HTML_TAG_130]
  [HTML_TAG_131]
  [HTML_TAG_132]
    [HTML_TAG_133][HTML_TAG_134]
    [HTML_TAG_135]ErrorMessage[HTML_TAG_136]
    [HTML_TAG_137]Toute information d’erreur supplémentaire, si elle existe.[HTML_TAG_138]
  [HTML_TAG_139]
  [HTML_TAG_140]
    [HTML_TAG_141][HTML_TAG_142]
    [HTML_TAG_143]ServerId[HTML_TAG_144]
    [HTML_TAG_145]L’ID du serveur de point de contrôle Uptrends qui a effectué cette vérification.[HTML_TAG_146]
  [HTML_TAG_147]
   [HTML_TAG_148]
    [HTML_TAG_149][HTML_TAG_150]
    [HTML_TAG_151]HttpStatusCode[HTML_TAG_152]
    [HTML_TAG_153]Le code de statut HTTP renvoyé (le cas échéant).[HTML_TAG_154]
  [HTML_TAG_155]
  [HTML_TAG_156]
    [HTML_TAG_157]Relationships[HTML_TAG_158]
    [HTML_TAG_159]Ce tableau contient une liste de données ou objets liés aux données actuelles. Cette liste peut contenir des liens pour récupérer les données associées. Les données de relation ont la même structure, en ce sens que ces entrées contiennent également les membres Id, Type et Links.[HTML_TAG_160]
    [HTML_TAG_161][HTML_TAG_162]
  [HTML_TAG_163]
[HTML_TAG_164]
[HTML_TAG_165]