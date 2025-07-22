{
"title": "Script à utiliser pour le test d'enregistrement du parcours d'utilisation du panier d'achats",
"summary": "Copiez et collez ce script dans votre éditeur de script pour suivre le tutoriel de test.",
"url": "/support/kb/surveillance-synthetique/transactions/tutorial-record-user-journey-in-shop/script-pour-test",
"translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/test-script",
"tableofcontents": false
}

Le script ci-dessous est la version non modifiée du script généré par l'enregistreur de transaction lors de l'exercice [Enregistrer un parcours d'utilisation du panier d'achats]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="fr" >}}). Si vous n'avez pas réalisé votre propre script en suivant le tutoriel, vous pouvez utiliser ce script pour la partie du tutoriel sur [le test et la modification]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="fr" >}}).

Pour saisir le script dans votre moniteur de transaction :

1. Copiez le code ci-dessous.
2. Ouvrez l'onglet {{< AppElement type="tab" >}} Étapes {{< /AppElement >}} dans les paramètres de votre moniteur de transaction.
3. Cliquez sur le bouton {{< AppElement type="button" >}} Basculer vers le script {{< /AppElement >}} en haut à droite.
4. Copiez le code dans l'éditeur.
5. Cliquez sur {{< AppElement type="button" >}}Basculer vers l'éditeur visuel{{< /AppElement >}}.

```json
{
  "steps": [ 
    {
      "name": "Go to start URL",
      "ignoreErrors": false,
      "recordWaterfall": false,
      "actions": [
        { "navigate": 
          {
            "url": "https://www.galacticshirts.com/"
          }
        }
      ]
    },
    {
      "name": "GalacticShirts.com - Shop cosmiclicious apparel",
      "ignoreErrors": false,
      "recordWaterfall": false,
      "collectPageSource": false,
      "actions": [
        {
          "click": {
            "element": {
              "xpath": "(//img[contains(@src,'https://www.galacticshirts.com/wp-content/uploads/2017/08/tshirt-suraya-300x300.png')])[1]",
              "alternatives": [
                {
                  "xpath": "(//img[contains(@src,'https://www.galacticshirts.com/wp-content/uploads/2017/08/tshirt-suraya-300x300.png')])[1]",
                  "name": "xpath:img"
                },
                {
                  "xpath": "(//main[@id='main']/section/div/ul/li/a/img)[1]",
                  "name": "xpath:idRelative"
                },
                {
                  "css": ".storefront-product-section:nth-child(2) .post-130 .attachment-woocommerce_thumbnail",
                  "name": "css:finder"
                }
              ],
              "shadowRoots": []
            }
          }
        }
      ]
    },
    {
      "name": "\"What Happens\" t-shirt | GalacticShirts.com",
      "ignoreErrors": false,
      "recordWaterfall": false,
      "actions": [
        {
          "set": {
            "value": "l",
            "isPassword": false,
            "element": {
              "css": "#pa_size"
            }
          }
        },
        {
          "click": {
            "element": {
              "css": "#pa_size" 
            },
            "description": "Click on an element \"Choose an option\""
          }
        },
        {
          "set": {
            "value": "2",
            "isPassword": false,
            "element": {
              "css": "input#quantity_6346b8b92ac97",
              "alternatives": [
                {
                  "css": "input#quantity_6346b8b92ac97",
                  "name": "id"
                },
                {
                  "css": "input[name=\"quantity\"]",
                  "name": "name"
                },
                {
                  "xpath": "(//input[@id='quantity_6346b8b92ac97'])[1]",
                  "name": "xpath:attributes"
                },
                {
                  "xpath": "(//div[@id='product-130']/div[2]/form/div/div[2]/div/input)[1]",
                  "name": "xpath:idRelative"
                },
                {
                  "css": "#quantity_6346b8b92ac97",
                  "name": "css:finder"
                }
              ],
              "shadowRoots": []
            },
            "description": "Set element (quantity_6346b8b92ac97) to '2'"
          }
        },
        {
          "click": {
            "element": {
              "css": "#quantity_5d3f4b334e9d1"
            },
            "description": "Click on an element (quantity_5d3f4b334e9d1)"
          }
        },
      {
        "click": {
          "element": {
            "css": "button.single_add_to_cart_button.button.alt"
          },
          "description": "Click on a button (Add to cart)"
        }
      },
      {
        "testDocumentContent": {
          "value": "added to your cart",
          "testType": "Contains",
          "description": "Content check"
        }
      },
      {
        "click": {  
          "element": {                
            "css": "div.woocommerce-message &gt; a.button.wc-forward"              
          },              
          "description": "Click on a hyperlink (View cart)"            
        }          
      }        
    ]     
  },      
  {        
    "name": "Cart | GalacticShirts.com",        
    "ignoreErrors": false,        
    "recordWaterfall": false,        
    "actions": [          
      {            
        "set": {              
          "value": "1",              
          "isPassword": false,              
          "element": {                
            "css": "#quantity_5d3f4dbc85bab"              
          },              
          "description": "Set element (quantity_5d3f4dbc85bab) to '1'"            
        }          
      },          
      {            
        "click": {              
          "element": {                
            "css": "button[name=\"update_cart\"]"              
          },              
          "description": "Click on a button (Update cart)"            
        }          
      },          
      {            
        "testDocumentContent": {              
          "value": "Cart updated",              
          "testType": "Contains",              
          "description": "Content check"            
          }          
        },          
        {            
          "click": {              
            "element": {                
              "css": "a.remove"              
              },              
            "description": "Click on a hyperlink (×)"            
          }          
        },          
        {            
          "testDocumentContent": {              
          "value": "your cart is currently empty",              
          "testType": "Contains",              
          "description": "Content check"            
          }          
        }        
      ]      
    }    
  ]  
}
```
