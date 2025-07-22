{
  "hero": {
    "title": "Schakelen tussen (inline) frames en tussen browsertabbladen"
  },
  "title": "Schakelen tussen (inline) frames en tussen browsertabbladen",
  "summary": "Als uw transactie nieuwe tabbladen of (ingesloten) frames moet openen en ermee moet interacteren, moet u mogelijk wijzigingen doorvoeren in uw script om het terugschakelen of de gebruikte selectors af te handelen.",
  "url": "/support/kb/synthetic-monitoring/transacties/schakelen-tussen-iframes-browsertabbladen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/switching-between-iframes-browser-tabs"
}

Wanneer uw gebruikersscenario de focus moet verleggen naar een nieuw geopend tabblad of een (inline) frame, vinden alle daaropvolgende acties plaats op het (inline) frame of het nieuwe tabblad totdat u weer terugschakelt. Het schakelen tussen tabbladen en tussen (inline) frames is vergelijkbaar, maar er zijn verschillen die u moet weten wanneer u uw transacties script.

## Schakelen tussen (inline) frames

Wanneer uw gebruikerspad interacties met een (inline) frame op de pagina bevat, neemt de Transaction recorder de omschakelacties tussen het root- en het ingesloten document op, maar het kan zijn dat u enkele aanpassingen moet aanbrengen aan de selectors die het conversieproces heeft gekozen bij het converteren van uw opname naar een script.

Wanneer u de opname uploadt naar uw Uptrends-account, wordt de opname naar een script geconverteerd. Tijdens het conversieproces doet Uptrends zijn best om de juiste selector voor het (inline) frame te kiezen. Het [algoritme van Uptrends]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="nl" >}})  maakt echter niet altijd de beste keuze, en soms weet het niet welk kenmerk het moet gebruiken. Is het een naam of ID? URL's worden zonder probleem herkend, maar voor ID's en naamkenmerken doet Uptrends zijn 'best guess'. Als het verkeerde type kenmerk werd gekozen, moet u de selector corrigeren.

{{< callout >}}
**Opmerking**: Hoewel u de (inline) frame-index kunt gebruiken voor identificatie (en de recorder kiest deze optie vaak voor u), raden we u af om de (inline) frame-indexen te gebruiken omdat de indexen veranderen. Daarom zorgen ID's, namen en URL's waar van toepassing voor betere selectors.
{{< /callout >}}

Volg deze instructies om **handmatig een omschakeling toe te voegen** tussen de root- en (inline) frame-documenten.

1.  Klik op {{< AppElement type="button" >}}Actie toevoegen{{< /AppElement >}} om het dialoogvenster voor actieselectie te openen.
2.  Klik op **Bediening: Schakel naar frame** om uw keuze te markeren.
3.  Klik op {{< AppElement type="button" >}}Selecteren{{< /AppElement >}}.
4.  Kies een van de volgende twee opties  
    
    **Volgende acties zullen op het HTML root document gericht zijn** - er is geen andere informatie nodig.

    **Volgende acties zullen op het volgende frame/Iframe gericht zijn** - kies het type identificatie en de identificatiewaarde.

5. Ga door met het toevoegen van frame-omschakelingen als u toegang nodig heeft tot frames die ingesloten zijn in het (inline) frame.

{{< callout >}}
**Opmerking**: Omdat (inline) frames laden na het root document, moet u mogelijk een korte [wachttijd]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}) (4000 ms) toevoegen om het laden van het (inline) frame te laten voltooien voordat u interacteert met de inhoud.
{{< /callout >}}

### Voorbeeld schakelen tussen inline frames

Als voorbeeld van het schakelen tussen inline frames navigeren we door de demo-planner van Uptrends. Het script voert de volgende stappen uit:

1.  Open de demopagina
2.  Doe een inhoudcontrole
3.  Klik om een consultant voor de demo te kiezen
4.  Pauzeer kort om te controleren of het inline frame op de nieuwe pagina volledig is geladen
5.  Doe nog een inhoudcontrole
6.  Klik op een link om naar de agenda te navigeren
7.  Controleer op inhoud
8.  Sluit het inline frame om terug te gaan naar het rootdocument

<!-- -->

    { 
    "steps": [ 
      { 
        "name": "Navigate to 'https://www.uptrends.com/demos'",
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
          "value": "Attend a webinar", 
          "testType": "Contains" 
          } 
         } 
        ] 
       }, 
       { 
         "name": "Live Demos | Uptrends", 
         "ignoreErrors": false, 
         "recordWaterfall": false, 
         "actions": [ 
           { 
             "click": { 
               "element": { 
                 "xpath": "//a[contains(.,'Plan free demo with Mark')]" 
                 }, 
               "description": "Click on a hyperlink (Plan free demo with Mark)" 
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
               "value": "Welcome to my scheduling page", 
               "testType": "Contains", 
               "element": { 
                 "xpath": "//div[contains(.,'Welcome to my scheduling page')]", 
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
                "value": "Select a Date & Time", 
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
                 "value": "Attend a webinar", 
                 "testType": "Contains" 
               } 
             } 
          ] 
        } 
      ] 
    }

## Schakelen tussen browsertabbladen

Wanneer een gebruikersactie een nieuw tabblad opent, volgt de recorder automatisch uw transactie naar het nieuwe tabblad en gaat verder met de opname. De recorder neemt echter geen terugschakeling naar een vorig tabblad op. Om te schakelen naar het oorspronkelijke tabblad of andere eerder geopende tabbladen, moet u de schakelactie zelf toevoegen met de stapeditor.

{{< callout >}}
**Opmerking**: Vergeet niet om de tabbladomschakeling te laten volgen door een inhoudcontrole. De [inhoudcontrole]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}}) controleert of u succesvol bent omgeschakeld.
{{< /callout >}}

Om te schakelen tussen tabbladen:

1.  Klik op {{< AppElement type="button" >}}Actie toevoegen{{< /AppElement >}} om het dialoogvenster voor actieselectie te openen.
2.  Klik op **Bediening: Schakelen tussen browsertabbladen** om uw keuze te markeren.
3.  Klik op {{< AppElement type="button" >}}Selecteren{{< /AppElement >}}.
4.  Kies ofwel de unieke **Paginatitel** (de titel die op het tabblad wordt weergegeven) ofwel de unieke **URL**. U kunt een gedeeltelijke paginatitel of URL gebruiken. In plaats van `https://www.uwsite.nl/uwpagina` kunt u bijvoorbeeld gewoon `/uwpagina` gebruiken.

Als geen van beide ID's voor uw scenario werken, [neem dan contact op met support](/contact) voor hulp.

{{< callout >}}
**Opmerking**: Als meerdere tabbladen overeenkomen met de (gedeeltelijke) paginatitel of URL, is de voorkeursvolgorde van rechts naar links (meest recente tabblad eerst).
{{< /callout >}}

### Voorbeeldscript schakelen tussen tabbladen

Het volgende voorbeeldscript opent een nieuw browsertabblad en schakelt weer terug naar het eerste tabblad. Het script voert deze reeks acties uit:

1.  Open een [Uptrends Blog](https://blog.uptrends.com) pagina
2.  Bevestig de juiste pagina met een [inhoudcontrole]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}})
3.  Klik op een element dat een nieuw tabblad opent
4.  Bevestig de succesvolle tabbladwisseling met een inhoudcontrole
5.  Ga terug naar het vorige tabblad
6.  Bevestig de tabbladwissel met een inhoudcontrole

Probeer het. Kopieer de code en plak deze in een nieuwe transactiecontroleregel.

    {  
    "steps": [ 
      {
        "name": "Navigate to 'https://blog.uptrends.com/web-performance/6-ways-to-reduce-time-to-first-byte-ttfb/'",
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
         "name": "Navigate to new tab",
         "ignoreErrors": false,
         "recordWaterfall": false,
         "actions": [  
           { "click":   
             { 
               "element": {  
                 "xpath": "//a[contains(.,'Dedicated hosting')]",
               },
               "description": "Click on a hyperlink (Dedicated hosting)"
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
        "name": "Switch to first tab",
        "actions": [
          { "switchBrowserTab":  
            {  
              "windowTitle": "https://blog.uptrends.com"
            }
          },
          {  
            "testDocumentContent":
              {
                "value": "Attend a webinar",
                "testType": "Contains"
              }
            }
          ]
        }
      ]  
    }
