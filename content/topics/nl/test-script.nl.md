{
  "title": "Testscript winkelwagenopname",
  "summary": "Kopieer en plak dit script in uw scripteditor en gebruik het samen met de testtutorial.",
  "url": "/support/kb/synthetic-monitoring/transacties/tutorial-record-user-journey-in-shop/testscript",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/test-script",
  "tableofcontents": false
}

Het volgende is het onbewerkte script dat is gegenereerd door de transaction recorder in de oefening [Het klikpad van de winkelwagengebruiker vastleggen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="nl" >}}). Als u geen eigen script heeft gemaakt aan de hand van de tutorial, kunt u dit script gebruiken om het onderdeel [testen en bewerken]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="nl" >}}) van de tutorial te volgen. 

Het script in uw transactiecontroleregel invoeren:

1.  Kopieer onderstaande code.
2.  Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}} van uw transactiecontroleregel.
3.  Klik rechtsboven op de knop {{< AppElement type="button" >}} Naar script schakelen {{< /AppElement >}}.
4.  Plak de code in de editor.
5.  Klik op {{< AppElement type="button" >}}Naar visuele editor schakelen{{< /AppElement >}}.

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