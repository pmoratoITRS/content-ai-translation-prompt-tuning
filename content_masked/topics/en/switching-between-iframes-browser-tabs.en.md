{
  "hero": {
    "title": "Switching between (inline) frames and browser tabs"
  },
  "title": "Switching between (inline) frames and browser tabs",
  "summary": "When your transaction needs to open and interact with new tabs or (embedded) frames, you may need to make alterations in your script to handle the switch back or the selectors used.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/switching-between-iframes-browser-tabs",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When your user scenario needs to switch focus to a newly opened tab or an (inline) frame, all subsequent actions after the switch take place on the (inline) frame or new tab until you make a switch back. The switch between tabs and (inline) frames is similar, but they have differences you need to know about when you script your transactions.

## Switching (inline) frames

When your user path includes interactions with an (inline) frame on the page, the Transaction Recorder captures the switch actions between the root and the embedded document, but you may need to make some adjustments to the selectors the conversion process chose when converting your recording into a script.

When you upload the recording to your Uptrends account, the recording is converted to a script. During the conversion process, Uptrends does its best to choose the correct selector for the (inline) frame. However, [Uptrends’ algorithm]([LINK_URL_1]) doesn’t always make the best choice, and sometimes it may not know which attribute to use. Is it a name or ID? URLs are recognized with no problem, but for IDs and name attributes, Uptrends makes its best guess. If the wrong attribute type was chosen, you’ll need to fix the selector.

[SHORTCODE_1]
**Note**: Although you have the option to use the (inline) frame index for identification (and the recorder often chooses this option for you), we don’t recommend that you use the (inline) frame indexes because indexes change. Therefore, where applicable, IDs, names, and URLs make for better selectors.
[SHORTCODE_2]

Follow these instructions to **add a switch manually** between the root and (inline) frame documents.

1.  Click [SHORTCODE_9]Add action[SHORTCODE_10] to open the action selection dialog.
2.  Click **Control: Switch frame** to highlight your choice.
3.  Click [SHORTCODE_11]Select[SHORTCODE_12].
4.  Choose either  
    **Subsequent actions will target the HTML root document** - no other information is needed.

    **Subsequent actions will target the following frame/Iframe** - choose the identifier type and identifying value.

5. Continue adding frames switches if you need to access frames embedded in the (inline) frame.

[SHORTCODE_3]
**Note**: Because (inline) frames load after the root document, you may need to add a short [wait action]([LINK_URL_2]) (4000 ms) to allow for the (inline) frame to complete loading before you interact with the content.
[SHORTCODE_4]

### Inline frame switch example

In the inline frame switch example, we navigate through Uptrends’ demo scheduler. The script carries out the following steps:

1.  Open the demo page
2.  Do a content check
3.  Click to choose a consultant for the demo
4.  Take a brief pause to make sure the inline frame on the new page has loaded completely
5.  Do another content check
6.  Click a link to navigate to the calendar
7.  Check for content
8.  Close the inline frame to go back to the root document

[HTML_TAG_1]

    { 
    "steps": [ 
      { 
        "name": "Navigate to '[URL_1]
        "ignoreErrors": false, 
        "recordWaterfall": false, 
        "actions": [ 
        { 
        "navigate": { 
        "url": "[URL_2] 
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
                   "iframeUrl": "[URL_3] 
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

## Switching browser tabs

When a user action opens a new tab, the recorder automatically follows your transaction to the new tab and continues the recording. However, the recorder will not capture a switch back to a previous tab. To switch to the originating tab or any other previously opened tabs, you need to add the switch action yourself using the step editor.

[SHORTCODE_5]
**Note**: Don’t forget to follow the tab switch with a content check. The [content check]([LINK_URL_3]) makes sure you switched successfully.
[SHORTCODE_6]

To switch tabs:

1.  Click [SHORTCODE_13]Add action[SHORTCODE_14] to open the action selection dialog.
2.  Click **Control: Switch browser tab** to highlight your choice.
3.  Click [SHORTCODE_15]Select[SHORTCODE_16].
4.  Choose either the unique **Page title** (the title displayed on the tab) or unique **URL**. You can use a partial page title or URL. For example, instead of [INLINE_CODE_1] you could simply use [INLINE_CODE_2].

If neither identifier works for your scenario, [contact support]([LINK_URL_4]) for help.

[SHORTCODE_7]
**Note**: If multiple tabs match the (partial) page title or URL, the order of preference is right-to-left (most recent tab first).
[SHORTCODE_8]

### Example tab switch script

The following example script opens a new browser tab and switches back to the first tab. The script performs this series of actions:

1.  Open an [Uptrends Blog]([LINK_URL_5]) page
2.  Confirm the correct page with a [content check]([LINK_URL_6])
3.  Click an element that opens a new tab
4.  Confirm the successful tab switch with a content check
5.  Change back to the previous tab
6.  Confirm the tab switch with a content check

Try it. Copy the code and paste it into a new transaction monitor.

    {  
    "steps": [ 
      {
        "name": "Navigate to '[URL_4]
        "ignoreErrors": false,
        "recordWaterfall": false,
        "actions": [
          {
            "navigate":  
              {
                "url": "[URL_5]
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
              "windowTitle": "[URL_6]
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
