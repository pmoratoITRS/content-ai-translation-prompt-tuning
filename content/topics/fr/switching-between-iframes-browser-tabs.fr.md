{
"hero": {
"title": "Changer d'iframes et changer d'onglets du navigateur"
},
"title": "Changer d'iframes et changer d'onglets du navigateur",
"summary": "Lorsque votre transaction doit ouvrir et interagir avec de nouveaux onglets ou iframes intégrés, vous aurez peut-être à apporter des modifications à votre script pour gérer le retour en arrière ou choisir les sélecteurs.",
"url": "/support/kb/surveillance-synthetique/transactions/Changer-iframes-onglets",
"translationKey": "https://www.uptrends.com/support/kb/transactions/switching-between-iframes-browser-tabs"
}

Lorsque votre scénario utilisateur doit basculer sur un onglet ou un (inline) frame (cadre intégré) nouvellement ouvert, toutes les actions ultérieures après le basculement ont lieu sur le (inline) frame ou le nouvel onglet. Le basculement entre onglets ou entre (inline) frames est similaire, mais elle présente des différences que vous devez connaître afin de les intégrer dans les scripts de vos transactions.

## Changer de cadre intégré (inline frame)

Lorsque la navigation de l'utilisateur inclut des interactions avec un cadre intégré sur la page, l'enregistreur de transactions capture le basculement entre le document racine et le document intégré, mais vous aurez peut-être à modifier les sélecteurs choisis lors de la conversion de votre enregistrement en un script.

Lors de l'envoi de l'enregistrement vers votre compte Uptrends, il est converti en script. Pendant le processus de conversion, Uptrends fait de son mieux pour choisir le bon sélecteur pour le cadre intégré. Cependant, [l'algorithme d'Uptrends]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="fr" >}}) ne fait pas toujours le meilleur choix, et parfois il ne sait pas quel attribut utiliser. Est-ce un nom ou un identifiant ? Uptrends n'a aucun problème à reconnaître les URL, mais pour les identifiants et les attributs de nom, l'algorithme fait de son mieux. S'il choisit le mauvais type d'attribut, vous aurez à corriger le sélecteur.

{{< callout >}}
**Remarque** : Vous avez la possibilité d'utiliser l'index du cadre pour l'identification (et l'enregistreur choisit souvent cette option pour vous), mais nous vous la déconseillons car les index changent. Par conséquent, là où c'est possible, utilisez les identifiants, les noms et les URL comme sélecteurs.
{{< /callout >}}

Pour **manuellement ajouter un commutateur** entre le document racine et le cadre, voici comment faire.

1. Cliquez sur {{< AppElement type="button" >}}Ajouter une action{{< /AppElement >}} pour ouvrir la boîte de dialogue
2. Cliquez sur **Contrôle : cadre de commutation** pour souligner votre choix
3. Cliquez sur {{< AppElement type="button" >}}Sélectionner{{< /AppElement >}}
4. Choisissez soit

   **Les actions suivantes cibleront le document racine HTML** - aucune autre information n'est nécessaire.

   **Les actions suivantes cibleront le cadre/Iframe suivant** - choisir le type d'identifiant et la valeur.

5. Continuez à ajouter des commutateurs de cadres si vous devez accéder à d'autres cadres intégrés.

{{< callout >}}
**Remarque** : Étant donné que les cadres se chargent après le document racine, il sera peut-être nécessaire d'ajouter une [action d'attente]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="fr" >}}) (4000 ms) avant d'interagir avec le contenu.
{{< /callout >}}

### Exemple de commutation de cadre

Dans cet exemple du commutateur de cadre, nous parcourons le planificateur de démonstration d'Uptrends. Le script exécute les étapes suivantes :

1. Ouvrir la page de démonstration
2. Faire une vérification du contenu
3. Cliquer pour choisir un consultant pour la démo
4. Marque une pause pour s'assurer que le cadre sur la nouvelle page est complètement chargé
5. Faire une autre vérification de contenu
6. Cliquer sur un lien pour accéder au calendrier
7. Vérifier le contenu
8. Ferme le cadre pour revenir au document racine

<!-- -->

    { 
    "steps": [ 
      { 
        "name": "Allez à 'https://www.uptrends.com/demos'",
        "ignoreErrors": false, 
        "recordWaterfall": false, 
        "actions": [ 
        { 
        "navigate": { 
        "url": "https://www.uptrends.com/demos" 
        } 
      }, 
      { 
        "testDocumentContent": { 
          "value": "Participer à un webinar", 
          "testType": "Contains" 
          } 
         } 
        ] 
       }, 
       { 
         "name": "Démos en direct | Uptrends", 
         "ignoreErrors": false, 
         "recordWaterfall": false, 
         "actions": [ 
           { 
             "click": { 
               "element": { 
                 "xpath": "//a[contains(.,'Planifier une démo gratuite avec Mark')]" 
                 }, 
               "description": "Cliquez sur un lien hypertexte (Planifiez une démo gratuite avec Mark)" 
             } 
           }, 
           { 
             "wait": { 
               "waitTimeMs": 4000 
               } 
             }, 
             { 
               "switchIframe": { 
               "framePath": [ 
                 { 
                   "iframeUrl": "https://calendly.com/mark-ridderhof/demo?embed_domain=www.uptrends.com&embed_type=PopupText" 
                 } 
               ] 
             } 
           }, 
           { 
             "testElementContent": { 
               "value": "Bienvenue sur ma page d'agenda", 
               "testType": "Contains", 
               "element": { 
                 "xpath": "//div[contains(.,'Bienvenue sur ma page d'agenda')]", 
                 "alternatives": [] 
               } 
             }
           } 
         ] 
        }, 
        { 
          "name": "Calendly - Mark Ridderhof", 
          "ignoreErrors": false, 
          "recordWaterfall": false, 
          "actions": [ 
            { 
              "click": { 
                "element": { 
                   "xpath": "//a[@data-id='event-type']", 
                } 
              } 
            }, 
            { 
              "testElementContent": { 
                "value": "Sélectionnez une date et une heure", 
                "testType": "Contains", 
                "element": { 
                  "xpath": "//h2[@class='spotpicker-title']", 
                  "alternatives": [] 
                } 
              } 
            } 
          ] 
        }, 
        { 
          "name": "Calendly - Mark Ridderhof", 
          "ignoreErrors": false, 
          "recordWaterfall": false, 
          "actions": [ 
             { 
               "switchIframe": { 
                 "framePath": [] 
               } 
             }, 
             { 
               "click": { 
                 "element": { 
                   "xpath": "//div[@class='calendly-popup-close']" 
                 } 
               } 
             }, 
             { 
               "testDocumentContent": { 
                 "value": "Participer à un webinar", 
                 "testType": "Contains" 
               } 
             } 
          ] 
        } 
      ] 
    }

## Changer d'onglet de navigateur

Lorsqu'une action de l'utilisateur ouvre un nouvel onglet, l'enregistreur suit automatiquement votre transaction jusqu'au nouvel onglet et continue d'enregistrer. Par contre, l'enregistreur ne capturera pas un retour à un onglet précédent. Pour basculer vers l'onglet d'origine ou tout autre onglet précédemment ouvert, vous devez ajouter vous-même l'action de basculement à l'aide de l'éditeur d'étapes.

{{< callout >}}
**Remarque** : N'oubliez pas de faire suivre le changement d'onglet avec une vérification du contenu. La [vérification du contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}}) permet de s'assurer que le basculement a bien été fait.
{{< /callout >}}

Pour changer d'onglet

1. Cliquez sur {{< AppElement type="button" >}}Ajouter une action{{< /AppElement >}} pour ouvrir la boîte de dialogue
2. Cliquez sur **Contrôle : Changer d'onglet de navigateur** pour souligner votre choix.
3. Cliquez sur {{< AppElement type="button" >}}Sélectionner{{< /AppElement >}}
4. Choisissez soit le **Titre de la page** unique (le titre affiché sur l'onglet) ou l'unique **URL**. Vous pouvez utiliser seulement une partie du titre de la page ou de l'URL. Par exemple, à la place de `https://www.votresite.com/votrepage` vous pouvez simplement utiliser `/votrepage`.

Si aucun des identifiants ne fonctionne pour votre scénario, [contactez le support](/contact).

{{< callout >}}
**Remarque** : Si plusieurs onglets correspondent au titre (partiel) de la page ou à l'URL, l'ordre de préférence est de droite à gauche (onglet le plus récent en premier).
{{< /callout >}}

### Exemple de script de changement d'onglet

L'exemple de script suivant ouvre un nouvel onglet de navigateur et revient au premier onglet. Le script effectue cette série d'actions :

1. Ouvrir une page du [Blog Uptrends](https://blog.uptrends.com)
2. Confirmer que c'est la bonne page avec une [vérification du contenu]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="fr" >}})
3. Cliquer sur un élément qui ouvre un nouvel onglet
4. Confirmer le changement d'onglet réussi avec une vérification du contenu
5. Revient à l'onglet précédent
6. Confirmer le changement d'onglet avec une vérification du contenu

Essayez-le. Copiez le code et collez-le dans un nouveau moniteur de transactions.

    {  
    "steps": [ 
      {
        "name": "Allez à 'https://blog.uptrends.com/web-performance/6-ways-to-reduce-time-to-first-byte-ttfb/'",
        "ignoreErrors": false,
        "recordWaterfall": false,
        "actions": [
          {
            "navigate":  
              {
                "url": "https://blog.uptrends.com/web-performance/6-ways-to-reduce-time-to-first-byte-ttfb/"
              }
            },
            {
              "testDocumentContent":  {
                "value": "You’ve come to the right place",
                "testType": "Contains"
              }
            } 
          ]
       },        
       {
         "name": "Allez vers un nouvel onglet",
         "ignoreErrors": false,
         "recordWaterfall": false,
         "actions": [  
           { "click":   
             { 
               "element": {  
                 "xpath": "//a[contains(.,'Dedicated hosting')]",
               },
               "description": "Cliquez sur un lien hypertexte (Dedicated hosting)"
             }
          },
          { 
            "testDocumentContent": {  
              "value": "dedicated server",
              "testType": "Contains" 
            }
          }
        ]
      },
      {
        "name": "Revenir au premier onglet",
        "actions": [
          { "switchBrowserTab":  
            {  
              "windowTitle": "https://blog.uptrends.com"
            }
          },
          {  
            "testDocumentContent":
              {
                "value": "Participer à un webinar",
                "testType": "Contains"
              }
            }
          ]
        }
      ]  
    }
