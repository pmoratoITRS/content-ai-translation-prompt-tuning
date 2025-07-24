{
  "hero": {
    "title": "Multi-step monitoring - Gestion des redirections"
  },
  "title": "Multi-step monitoring",
  "summary": "Découvrez comment utiliser les redirections dans vos moniteurs API multi-étapes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/surveillance-api/multi-step-redirects",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Les redirections HTTP permettent à un serveur web de rediriger l'appelant (le client HTTP) vers une autre URL que celle initialement demandée. Cela se fait en retournant un code d'état dans la plage 3xx, ainsi que la nouvelle URL qui doit être appelée par le client. Cette nouvelle URL, renvoyée dans l'en-tête de réponse HTTP, est nommé Location.

Requête initiale et réponse :  

[INLINE_CODE_1] [INLINE_CODE_2]  

Requête vers le nouvel emplacement :  

[INLINE_CODE_3] [INLINE_CODE_4]

## Vérification des redirections dans un moniteur multi-étapes

Dans un [moniteur API multi-étapes]([LINK_URL_1]), les redirections comme celles-ci sont exécutées automatiquement. Vous n'avez pas à vous soucier du fonctionnement interne de la gestion, par votre application web ou API, des requêtes entrantes : vous pouvez vous concentrer sur la vérification du résultat. Cela signifie que si une étape demande une URL qui est redirigée par votre serveur, nous exécuterons la deuxième requête dans le cadre de cette même étape, et vous pourrez travailler avec le résultat de la deuxième requête comme s'il n'y avait pas de redirection au milieu. Si la deuxième requête renvoie aussi une redirection, nous suivrons celle-ci également, dans la limite de 50 redirections consécutives. Dans chaque cas, vous obtiendrez le contenu et les en-têtes de la réponse correspondant à la dernière requête.

Dans certains cas, ce comportement automatique des redirections consécutives peut ne pas correspondre à votre besoin. Par exemple, si vous souhaitez surveiller le comportement de la redirection elle-même (en vérifiant le code d'état, le contenu de l'en-tête Location, si un cookie est renvoyé ou toute autre valeur), vous aurez besoin d'accéder à ces valeurs plutôt que d'exécuter la seconde requête tout de suite.

Si vous ajoutez une assertion et spécifiez que le code d'état HTTP doit être égal à 301, 302, 303, 307 ou 308, alors nous n'exécuterons pas cette redirection. À la place, vous aurez un accès direct à cette réponse. Vous pouvez ensuite utiliser des assertions et des variables supplémentaires, dans la même étape, afin de traiter cette réponse. Par exemple :

### Les assertions

[SHORTCODE_1]Status code[SHORTCODE_2] [SHORTCODE_3]Is equal to[SHORTCODE_4] [SHORTCODE_5]302[SHORTCODE_6]

[SHORTCODE_7]Response header[SHORTCODE_8] [SHORTCODE_9]Location[SHORTCODE_10] [SHORTCODE_11]Contains[SHORTCODE_12] [SHORTCODE_13]productId=P12345[SHORTCODE_14]

![Redirection MSA]([LINK_URL_2])

## Suivre la redirection manuellement

Comme nous travaillons dans une configuration à plusieurs étapes, nous pouvons continuer à exécuter la redirection manuellement après avoir vérifié la redirection et éventuellement capturé des valeurs à partir de la réponse. Ajoutez simplement une nouvelle étape et spécifiez ce nouvel emplacement en tant qu'URL.

Pour ce faire, vous pouvez capturer la valeur de l'en-tête Location, la stocker dans une variable (par exemple, [SHORTCODE_15]{{location-value}}[SHORTCODE_16]) et utiliser cette variable dans l'URL de l'étape suivante. Cependant il faut faire attention : la valeur de l'en-tête Location est susceptible d'être une URL relative, c'est-à-dire sans nom de domaine. Si vous êtes en configuration manuelle, vous aurez à compenser en incluant le nom de domaine dans la nouvelle URL :

[INLINE_CODE_5]

Ça va marcher, mais nous pouvons vous faciliter la tâche : chaque fois que nous détectons un en-tête Location dans une réponse HTTP, nous convertissons cette valeur en une URL absolue (y compris le nom de domaine de la requête d'origine) et la plaçons dans un variable appelée [SHORTCODE_17][SYSTEM_VAR_1][SHORTCODE_18]. Cette variable est prête à être utilisée à l'étape suivante:

[INLINE_CODE_6]

## Capture de paramètres à partir d'une URL de redirection

Dans certains scénarios, vous pouvez ne pas vouloir suivre l'URL de redirection, mais en capturer une valeur de paramètre à la place. Supposons que la réponse d'origine contenait cet en-tête :

[INLINE_CODE_7]

Et si vous ne vouliez pas vraiment suivre cette URL, mais simplement utiliser cette valeur de paramètre de code qui a été renvoyée par votre serveur ? Pas de problème: nous capturons automatiquement les paramètres d'URL que nous trouvons dans les en-têtes Location, et les plaçons dans des variables automatiques que vous pouvez utiliser ailleurs. La convention de nommage pour ces variables automatiques est la suivante : [SHORTCODE_19][SYSTEM_VAR_3][SHORTCODE_20]. Dans ce cas, vous aurez accès à [SHORTCODE_21][SYSTEM_VAR_4][SHORTCODE_22] et [SHORTCODE_23][SYSTEM_VAR_5][SHORTCODE_24].
