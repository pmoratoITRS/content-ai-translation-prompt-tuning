{
  "hero": {
    "title": "Zwischen (Inline) Frames und Browser-Tabs wechseln"
  },
  "title": "Zwischen (Inline) Frames und Browser-Tabs wechseln",
  "summary": "Wenn deine Transaktion neue Tabs öffnen oder mit (eingebetteten) Frames interagieren muss, muss dein Skript eventuell angepasst werden, um einen Wechsel zurück oder die verwendeten Selektoren zu handhaben.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/zwischen-iframes-browser-tabs-wechseln",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/switching-between-iframes-browser-tabs"
}

Wenn bei deinem Nutzerszenario ein Fokuswechsel auf einen neu geöffneten Tab oder einen (Inline) Frame erfolgen muss, finden alle nachfolgenden Aktionen nach dem Wechsel auf dem (Inline) Frame oder neuen Tab statt, bis du zurückwechselst. Der Wechsel zwischen Tabs und (Inline) Frames ist ähnlich, aber es gibt Unterschiede, die du für das Skript deiner Transaktionen kennen musst.

## (Inline) Frames wechseln

Wenn der Nutzerpfad Interaktionen mit einem (Inline) Frame auf der Seite beinhaltet, erfasst der Transaction Recorder die Wechsel-Aktion zwischen Stamm- und eingebettetem Dokument, aber du musst eventuell einige Anpassungen an den Selektoren vornehmen, die durch den Umwandlungsprozess von Aufzeichnung in Skript ausgewählt wurden.

Wenn du die Aufzeichnung in deinen Uptrends Account hochlädst, wird sie automatisch in ein Skript umgewandelt. Während des Umwandlungsvorgangs wählt Uptrends nach Möglichkeit den korrekten Selektor für den (Inline) Frame aus. Aber es kann vorkommen, dass [Uptrends‘ Algorithmus]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="de" >}}) nicht die beste Wahl trifft oder nicht weiß, welches Attribut zu nutzen ist. Ist es ein Name oder eine ID? URLs werden problemlos erkannt, aber bei ID- und Name-Attributen folgt Uptrends den naheliegendsten Vermutungen. Wird der falsche Attributtyp ausgewählt, musst du den Selektor korrigieren.

{{< callout >}}
**Hinweis**: Obwohl die Option des (Inline) Frame-Index zur Identifizierung besteht (und der Recorder wählt häufig diese Option), empfehlen wir die Nutzung der (Inline) Frame-Indexe nicht, da diese sich ändern können. Daher sind gegebenenfalls IDs, Namen und URLs die besseren Selektoren.
{{< /callout >}}

Folge diesen Anweisungen, um zwischen Stamm- und (Inline) Frame-Dokumenten **einen Wechsel manuell hinzuzufügen**.

1.  Klicke auf {{< AppElement type="button" >}}Aktion hinzufügen{{< /AppElement >}}, um das Auswahl-Dialogfenster zu öffnen.
2.  Klicke auf **Kontrolle: Wechsle Frame**, um deine Wahl zu markieren.
3.  Klicke auf {{< AppElement type="button" >}}Auswählen{{< /AppElement >}}.
4.  Wähle entweder

    **Nachfolgende Aktionen betreffen das HTML-Stammdokument** – es sind keine weiteren Angaben erforderlich.

    **Nachfolgende Aktionen betreffen das folgende Frame / IFrame** – wähle den Kennungstyp und -wert hinzu.

5. Füge weitere Frame-Wechsel hinzu, wenn auf in den (Inline) Frame eingebettete Frames zugegriffen werden muss.

{{< callout >}}
**Hinweis**: Da (Inline) Frames nach dem Stammdokument geladen werden, musst du eventuell eine kurze [Warte-Aktion]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="de" >}}) (4000 ms) hinzufügen, damit der (Inline) Frame komplett geladen wird, bevor du mit dem Inhalt interagierst.
{{< /callout >}}

### Inline Frame wechseln – Beispiel

Bei dem Beispiel für einen Inline-Frame-Wechsel navigieren wir durch Uptrends‘ Demo-Planer. Das Skript führt die folgenden Schritte aus:

1.  Öffnen der Demo-Seite
2.  Durchführen einer Inhaltsprüfung
3.  Klicken, um einen Berater für die Demo auszuwählen
4.  Kurze Pause, um sicherzustellen, dass der Inline Frame vollständig auf der neuen Seite geladen ist
5.  Durchführen einer weiteren Inhaltsprüfung
6.  Klicken auf einen Link, um den Kalender aufzurufen
7.  Inhaltsprüfung
8.  Schließen des Inline Frames, um zum Stammdokument zurückzukehren

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

## Browser-Tabs wechseln

Wenn über eine Nutzeraktion ein neuer Tab geöffnet wird, folgt der Recorder automatisch bei deiner Transaktion zu diesem neuen Tab und zeichnet weiter auf. Allerdings erfasst der Recorder nicht den Wechsel zu einem vorherigen Tab. Um zum ursprünglichen Tab oder zu anderen zuvor geöffneten Tabs zu wechseln, musst du die Wechsel-Aktion selbst anhand des Step-Editors hinzufügen.

{{< callout >}}
**Hinweis**: Vergiss nicht, auf den Tab-Wechsel eine Inhaltsprüfung folgen zu lassen. Die [Inhaltsprüfung]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}}) stellt sicher, dass der Wechsel erfolgreich war.
{{< /callout >}}

Wechsle Tabs folgendermaßen:

1.  Klicke auf {{< AppElement type="button" >}}Aktion hinzufügen{{< /AppElement >}}, um das Auswahl-Dialogfenster zu öffnen.
2.  Klicke auf **Kontrolle: Wechsle Browser Tab**, um deine Wahl zu markieren.
3.  Klicke auf {{< AppElement type="button" >}}Auswählen{{< /AppElement >}}.
4.  Wähle dann entweder den einzigartigen **Seitentitel** (der Titel, der auf dem Tab angezeigt wird) oder die einzigartige **URL**. Du kannst einen partiellen Seitentitel oder eine partielle URL eingeben. Zum Beispiel könntest du statt `https://www.yoursite.com/yourpage` einfach `/yourpage` nutzen.

Wenn keiner der Bezeichner in deinem Szenario funktioniert, [wende dich an unseren Support](/contact).

{{< callout >}}
**Hinweis**: Stimmen mehrere Tabs mit dem (partiellen) Seitentitel oder der URL überein, lautet die Reihenfolge „von rechts nach links“ (der neueste Tab zuerst).
{{< /callout >}}

### Skript für Tab-Wechsel – Beispiel

Das folgende Beispiel-Skript öffnet einen neuen Browser-Tab und wechselt zum ersten Tab zurück. Das Skript führt diese Reihe von Aktionen aus:

1.  Öffnen einer [Uptrends Blog](https://blog.uptrends.com)-Seite
2.  Bestätigung der richtigen Seite durch eine [Inhaltsprüfung]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="de" >}})
3.  Klicken auf ein Element, das einen neuen Tab öffnet
4.  Bestätigung des erfolgreichen Tab-Wechsels durch eine Inhaltsprüfung
5.  Rückkehr zum vorherigen Tab und
6.  Bestätigung des Tab-Wechsels durch eine Inhaltsprüfung

Probiere es aus. Kopiere den Code und füge ihn in einem neuen Transaktionsprüfobjekt ein.

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
