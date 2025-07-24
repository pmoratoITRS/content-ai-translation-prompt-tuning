{
  "hero": {
    "title": "Browser-Cache leeren"
  },
  "title": "Browser-Cache leeren",
  "summary": "Wenn die Transaktion Seitenobjekte direkt vom Server statt aus dem Cache neu laden soll, hilft das Leeren des Cache.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/browser-cache-leeren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends‛ [Transaktionsprüfobjekte]([LINK_URL_1]) öffnen immer einen echten Browser, um Nutzeraktivitäten zu simulieren und die Performance deiner Website zu testen. Der Browser hat zu Beginn keine Daten im Cache. Während er auf der Website Nutzeraktivitäten ausführt (wie etwa Anmelden, Scrollen durch Produktangebote und Hinzufügen zu Warenkörben), werden Elemente temporär in einem Cache gespeichert, um all deine Website-Ressourcen zu erkennen. Dadurch werden die Ladeprozesse des Browsers beim nächsten Besuch derselben Seite beschleunigt.

Es gibt Fälle, bei denen die unterschiedlichen Seitenverhalten bei einem Besuch überwacht werden sollen. Wenn du das Verhalten deiner E-Commerce-Websites hinsichtlich des Ablegens von Artikeln im Warenkorb bei bestehenden Nutzern (mit im Cache gespeicherten Daten) und bei neuen Besuchern (ohne im Cache gespeicherte Daten) vergleichen möchtest, empfehlen wir das Leeren des Browser-Cache.

## Die Aktion „Browser-Cache leeren‟

Mit der neuen Aktion **Browser-Cache leeren** bei Transaktionsschritten wird der Browser-Cache gelöscht, damit Seitenelemente direkt vom Server und nicht aus dem Cache geladen werden. Diese Funktion hilft dir, die Website-Performance bei erstmaligen Besuchern zu prüfen, und stellt sicher, dass die Benutzeroberfläche (mit Bildern, Text und weiteren Front-End-Elementen) korrekt geladen wird.

[SHORTCODE_1] **Hinweis:** Diese Aktion erfordert keine Transaktions-Credits. Nutze sie, um deinen Monitoring-Anforderungen besser gerecht zu werden. Weitere Informationen zu den Credits findest du unter [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]([LINK_URL_2]). [SHORTCODE_2]

## Die Aktion „Browser-Cache leeren‟ hinzufügen

Es gibt zwei Möglichkeiten, die Aktion **Browser-Cache leeren** in einen Transaktionsschritt einzufügen: anhand des [visuellen Transaktionsschritte-Editors]([LINK_URL_3]) oder des [Transaktionsskript-Editors]([LINK_URL_4]).

### Den Transaktionsschritte-Editor verwenden

Um die Aktion **Browser-Cache leeren** im **Transaktionsschritte-Editor** hinzuzufügen:

1. Rufe [SHORTCODE_3] Transaktionen > Transaktionen einrichten [SHORTCODE_4] auf.
2. Klick auf das Transaktionsprüfobjekt, bei dem die Aktion „Browser-Cache leeren‟ hinzugefügt werden soll.
3. Wechsle zur Registerkarte [SHORTCODE_5] Schritte [SHORTCODE_6].
4. Gehe zu dem **Schritt**, bei dem der Browser-Cache geleert werden soll.
5. Klicke auf [SHORTCODE_7]Aktion hinzufügen[SHORTCODE_8].
6. Wähle im Pop-up-Fenster **Aktion hinzufügen** die Option **Browser-Cache leeren**.
7. Klicke auf [SHORTCODE_9]Auswählen[SHORTCODE_10].
8. Gib im Feld **Einstellungen > Beschreibung** eine detaillierte Beschreibung der hinzugefügten Aktion ein.
9. Klicke auf die [SHORTCODE_11]Speichern[SHORTCODE_12]-Schaltfläche, um die Prüfobjektänderungen zu sichern.

![GIF Browser-Cache leeren]([LINK_URL_5])

### Den Transaktionsskript-Editor verwenden

Um die Aktion **Browser-Cache leeren** im **Transaktionsskript-Editor** hinzuzufügen:

1. Rufe [SHORTCODE_13] Transaktionen > Transaktionen einrichten [SHORTCODE_14] auf.
2. Klick auf das Transaktionsprüfobjekt, bei dem die Aktion „Browser-Cache leeren‟ hinzugefügt werden soll.
3. Wechsele zur Registerkarte [SHORTCODE_15] Schritte [SHORTCODE_16].
4. Klicke oben rechts auf deinem Bildschirm auf die Schaltfläche [SHORTCODE_17] Wechsle zum Skript  [SHORTCODE_18].
5. Füge im **Transaktionsskript** das Snippet [INLINE_CODE_1] zum [INLINE_CODE_2]-Array hinzu:

[CODE_BLOCK_1]

6. Klicke auf die [SHORTCODE_19]Speichern[SHORTCODE_20]-Schaltfläche, um die Prüfobjektänderungen zu sichern.

Die Aktion **Browser-Cache leeren** ist nun Teil deiner Schritte und wird jedes Mal mit dem Transaktionsprüfobjekt ausgeführt.
