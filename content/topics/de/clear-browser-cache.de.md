{
  "hero": {
    "title": "Browser-Cache leeren"
  },
  "title": "Browser-Cache leeren",
  "summary": "Wenn die Transaktion Seitenobjekte direkt vom Server statt aus dem Cache neu laden soll, hilft das Leeren des Cache.",
  "url": "/support/kb/synthetic-monitoring/transactions/browser-cache-leeren",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/clear-browser-cache"
}

Uptrends‛ [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) öffnen immer einen echten Browser, um Nutzeraktivitäten zu simulieren und die Performance deiner Website zu testen. Der Browser hat zu Beginn keine Daten im Cache. Während er auf der Website Nutzeraktivitäten ausführt (wie etwa Anmelden, Scrollen durch Produktangebote und Hinzufügen zu Warenkörben), werden Elemente temporär in einem Cache gespeichert, um all deine Website-Ressourcen zu erkennen. Dadurch werden die Ladeprozesse des Browsers beim nächsten Besuch derselben Seite beschleunigt.

Es gibt Fälle, bei denen die unterschiedlichen Seitenverhalten bei einem Besuch überwacht werden sollen. Wenn du das Verhalten deiner E-Commerce-Websites hinsichtlich des Ablegens von Artikeln im Warenkorb bei bestehenden Nutzern (mit im Cache gespeicherten Daten) und bei neuen Besuchern (ohne im Cache gespeicherte Daten) vergleichen möchtest, empfehlen wir das Leeren des Browser-Cache.

## Die Aktion „Browser-Cache leeren‟

Mit der neuen Aktion **Browser-Cache leeren** bei Transaktionsschritten wird der Browser-Cache gelöscht, damit Seitenelemente direkt vom Server und nicht aus dem Cache geladen werden. Diese Funktion hilft dir, die Website-Performance bei erstmaligen Besuchern zu prüfen, und stellt sicher, dass die Benutzeroberfläche (mit Bildern, Text und weiteren Front-End-Elementen) korrekt geladen wird.

{{< callout >}} **Hinweis:** Diese Aktion erfordert keine Transaktions-Credits. Nutze sie, um deinen Monitoring-Anforderungen besser gerecht zu werden. Weitere Informationen zu den Credits findest du unter [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="de" >}}). {{< /callout >}}

## Die Aktion „Browser-Cache leeren‟ hinzufügen

Es gibt zwei Möglichkeiten, die Aktion **Browser-Cache leeren** in einen Transaktionsschritt einzufügen: anhand des [visuellen Transaktionsschritte-Editors]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}) oder des [Transaktionsskript-Editors]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}).

### Den Transaktionsschritte-Editor verwenden

Um die Aktion **Browser-Cache leeren** im **Transaktionsschritte-Editor** hinzuzufügen:

1. Rufe {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf.
2. Klick auf das Transaktionsprüfobjekt, bei dem die Aktion „Browser-Cache leeren‟ hinzugefügt werden soll.
3. Wechsle zur Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}}.
4. Gehe zu dem **Schritt**, bei dem der Browser-Cache geleert werden soll.
5. Klicke auf {{< AppElement type="editbutton" >}}Aktion hinzufügen{{< /AppElement >}}.
6. Wähle im Pop-up-Fenster **Aktion hinzufügen** die Option **Browser-Cache leeren**.
7. Klicke auf {{< AppElement type="buttonCta" >}}Auswählen{{< /AppElement >}}.
8. Gib im Feld **Einstellungen > Beschreibung** eine detaillierte Beschreibung der hinzugefügten Aktion ein.
9. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um die Prüfobjektänderungen zu sichern.

![GIF Browser-Cache leeren](/img/content/gif-transaction-clear-browser-cache.gif)

### Den Transaktionsskript-Editor verwenden

Um die Aktion **Browser-Cache leeren** im **Transaktionsskript-Editor** hinzuzufügen:

1. Rufe {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf.
2. Klick auf das Transaktionsprüfobjekt, bei dem die Aktion „Browser-Cache leeren‟ hinzugefügt werden soll.
3. Wechsele zur Registerkarte {{< AppElement type="tab" >}} Schritte {{< /AppElement >}}.
4. Klicke oben rechts auf deinem Bildschirm auf die Schaltfläche {{< AppElement type="editbutton" >}} Wechsle zum Skript  {{< /AppElement >}}.
5. Füge im **Transaktionsskript** das Snippet `clearCache` zum `actions`-Array hinzu:

```json
    {
      "clearCache": {
        "description": "Provide a step description here"
      }
    },
```

6. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um die Prüfobjektänderungen zu sichern.

Die Aktion **Browser-Cache leeren** ist nun Teil deiner Schritte und wird jedes Mal mit dem Transaktionsprüfobjekt ausgeführt.
