{
  "hero": {
    "title": "RUM et la confidentialité des utilisateurs"
  },
  "title": "RUM et la confidentialité des utilisateurs",
  "summary": "Découvrez comment Uptrends protège la confidentialité des utilisateurs et ce que vous devez savoir sur le RUM.",
  "url": "/support/kb/rum/rum-et-la-confidentialite-des-utilisateurs",
  "translationKey": "https://www.uptrends.com/support/kb/rum/rum-and-user-privacy"
}

Garantir la confidentialité des utilisateurs est importante. Dans cet article, nous expliquons comment Uptrends utilise les informations des utilisateurs de votre site et nous décrivons les autres mesures que vous pouvez prendre pour protéger votre marque et la confidentialité des utilisateurs.

## La confidentialité, les données personnelles et la Loi sur la Protection des Données

Quand un utilisateur accède à votre site, le script RUM dans vos pages envoie une requête à Uptrends. C'est dans la nature même d'Internet que nous recevons également l'adresse IP du visiteur avec la demande. Ce sont des données sensibles puisque l'adresse IP peut servir à identifier et suivre des utilisateurs individuels. Nous avons conçu RUM de A à Z afin de vous garantir un contrôle complet sur la façon dont les adresses IP de vos visiteurs soient traitées. Les deux principaux aspects sont les suivants :

-   Nous proposons une anonymisation d'adresses IP à deux-niveaux

<!-- -->

-   Nous ne stockons pas d'adresses IP à long terme

### Anonymisation de l'adresse IP multi-niveaux

Afin de vous fournir le pays d'origine de vos visiteurs (et, dans certains cas, des informations de l'état pour l'Australie, le Canada et les États-Unis), Uptrends utilise l'adresse IP. Uptrends n'identifie pas, ne collecte pas des données personnelles, ni ne piste les visiteurs de votre site. Toutefois, si la politique de confidentialité de votre application n'autorise pas Uptrends à utiliser l'adresse IP complète de vos visiteurs de quelque manière que ce soit, nous proposons deux niveaux d'anonymisation :

-   **Niveau 0 :** l'adresse IP complète est utilisée. C'est la valeur par défaut.
-   **Niveau 1 :** Nous mettons le dernier octet (le plus identifiant) de l'adresse IP à zéro avant l'inspection.
-   **Niveau 2 :** Nous mettons les deux derniers octets de l'adresse IP à zéro avant l'inspection.

**Exemple :** en utilisant le niveau 1, l'adresse IP d'origine de l'utilisateur final `123.123.123.123` devient `123.123.123.0`. De même, l'utilisation de l'anonymisation au niveau 2 donne `123.123.0.0`.

{{< callout >}}
**Remarque :** Uptrends ne stocke pas l'adresse IP originale ou anonyme à long terme (voir ci-dessous).
{{< /callout >}}

En supprimant les parties les plus importantes de l'adresse IP (à propos de l'identification unique d'une adresse réseau), nous n'avons qu'une idée très générale de l'emplacement de chaque visiteur. Par conséquent, plus le niveau d'anonymisation est élevé, moins les informations sur le pays et l'état sont précises.

### Spécifier le niveau d'anonymisation

Si vous n'avez pas besoin d'une anonymisation IP, vous pouvez utiliser le script RUM normal tel quel sans aucune configuration supplémentaire. Les niveaux 1 ou 2 ne nécessitent qu'une petite modification dans le script.

Dans le script RUM inclus dans vos pages web, vous remarquerez que le paramètre aip est par défaut à 0. Mettez **sa valeur à 1 pour l'anonymisation de niveau 1** et **à 2 pour l'anonymisation de niveau 2**.

**Par exemple :**

`var _urconfig = { sid: "9acad2af-b1f5-4438-8de6-5047a02a7ecf", aip: 1 };`

Le script envoie la valeur d'anonymisation avec chaque requête RUM exécutée sur vos pages web et votre niveau d'anonymat spécifié prend effet immédiatement.

### Pas de stockage à long terme des adresses IP

Si vous décidez d'utiliser l'anonymisation IP, nous vous garantissons que nous ne regarderons pas les adresses IP d'origine, et nous ne les stockerons ni en mémoire, ni sur disque ni sur n'importe quelle autre périphérique de stockage. La toute première étape de notre procédure de traitement consiste à anonymiser les adresses IP avant de les examiner de quelque façon que ce soit.

En outre, **nous ne conservons les informations de l'adresse IP que temporairement**, jusqu'à ce que nous ayons complètement terminé le traitement de la demande initiale. Après ça nous purgeons l'information. La purge comprend toute combinaison d'informations de : adresse IP, données d'agent utilisateur, URL, dates, heures et informations de fuseau horaire.

## Real User Monitoring et votre déclaration de confidentialité

Parfois, les clients qui utilisent Real User Monitoring demandent ce qu'ils doivent ajouter à leur déclaration de confidentialité sur leur site web. Même si nous ne sommes pas des avocats, nous vous conseillons néanmoins de copier et coller le paragraphe suivant dans votre politique de confidentialité.

*&lt;Votre nom de marque ici&gt; utilise Real User Monitoring d'Uptrends pour surveiller l'expérience des utilisateurs lorsqu'ils visitent notre site. Uptrends n'utilise pas de cookies pour collecter des données ou suivre les utilisateurs de notre site; plutôt, Uptrends utilise un petit fichier de script sur nos pages qui envoie des données de performance sur les visiteurs de notre site aux serveurs Uptrends. Les données collectées auprès de chaque utilisateur comprennent les adresses IP, les types de périphériques, les systèmes d'exploitation et les navigateurs utilisés. Les serveurs Uptrends regroupent les données de performance de tous les visiteurs de notre site et nous fournissent des informations qui nous permettent d'améliorer l'expérience utilisateur sur notre site en fonction des informations ci-dessus. Uptrends utilise les adresses IP individuelles des visiteurs de notre site pour recueillir des informations sur le pays (ou l'état dans le pays) du visiteur, rien de plus. En outre, Uptrends ne stocke pas d'adresses IP à long terme, ni ne suit ou ne partage avec des tiers des informations sur un utilisateur individuel.*

### Vous pouvez également inclure le paragraphe suivant dans votre déclaration de confidentialité si vous utilisez les niveaux d’anonymisation 1 ou 2

*Pour protéger votre vie privée, la version du fichier de script Uptrends que nous utilisons sur notre site est configurée pour rendre votre adresse IP anonyme avant qu'elle ne soit traitée. Votre adresse IP n'est jamais stockée et elle n'est jamais utilisée autrement que pour déterminer votre pays d'origine.*
