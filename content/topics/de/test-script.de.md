{
  "title": "Testskript einer Aufzeichnung der Shop-Funktionen",
  "summary": "Kopiere und füge dieses Skript in deinen Skript-Editor, um dem Test-Tutorial zu folgen.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/tutorial-record-user-journey-in-shop/test-skript",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/test-script",
  "tableofcontents": false
}

Unten findest du das nicht bearbeitete Skript, das im Transaktions-Recorder bei der Übung [Aufzeichnen der User Journey bei Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="de" >}}) erzeugt wurde. Wenn du während des Tutorials kein eigenes Skript erstellt hast, kannst du dieses Skript verwenden, um dem Tutorial-Teil [Testen und Bearbeiten]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="de" >}}) zu folgen.

Das Skript in dein Transaktionsprüfobjekt einfügen:

1.  Kopiere den unten stehenden Code.
2.  Wechsle zur Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}} bei deinem Transaktionsprüfobjekt.
3.  Klicke auf {{< AppElement type="button" >}} Wechsle zum Skript {{< /AppElement >}} oben rechts.
4.  Füge den Code in den Editor ein.
5.  Klicke auf {{< AppElement type="button" >}}Wechsle zum visuellen Editor{{< /AppElement >}}.

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
