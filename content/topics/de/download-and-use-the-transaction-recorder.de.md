{
  "hero": {
    "title": "Den Transaktions-Recorder herunterladen und nutzen"
  },
  "title": "Den Transaktions-Recorder herunterladen und nutzen",
  "summary": "Lade den Transaktions-Recorder herunter und erfahre, wie du ihn verwendest.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/transaktions-recorder-herunterladen-und-nutzen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/download-and-use-the-transaction-recorder"
}

Dieser Artikel beschreibt, wie du den Transaktions-Recorder herunterlädst und verwendest.
Wenn du ihn anhand eines fiktiven Web-Shops statt deines eigenen ausprobieren möchtest, sieh dir unser Tutorial [User Journey bei Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/" lang="de" >}}) an.

## Den Transaktions-Recorder herunterladen {id="download-transaction-recorder"}

Die Transaktions-Recorder-Erweiterung ist eine Chrome-Browser-Erweiterung. Solltest du nicht mit Browser-Erweiterungen vertraut sein: Eine Browser-Erweiterung ist eine kleine App, die du dem Chrome-Browser hinzufügen kannst, um bestimmte Dinge zu handhaben, beispielsweise das Verwalten von Passwörtern. In diesem Fall ermöglicht es dir, die Klickpfade für deine Transaktion aufzuzeichnen. Die Erweiterung ist einfach zu installieren, solltest du jedoch Hilfe benötigen, bietet Google ein Tutorial zur [Installation und Verwaltung von Browser-Erweiterungen](https://support.google.com/chrome_webstore/answer/2664769?hl=en).

1.  Öffne ein Chrome-Browser-Fenster. Für die Erweiterung musst du [Chrome](https://www.google.com/intl/en/chrome/) verwenden.
2.  Rufe den [Chrome Web Store](https://chrome.google.com/webstore/detail/uptrends-transaction-reco/pbglkhekcljpmhpaeckglhfpenefpjgo) auf. Der Link führt dich direkt zum Transaktionsrekorder im Store, alternativ kannst du im Store unter „Uptrends Transaction Recorder“ nach ihm suchen.
3.  Klicke auf die Schaltfläche **Zu Chrome hinzufügen**. Ein Pop-up-Fenster wird geöffnet.
![Screenshot Chrome Pop-up zum Hinzufügen der Erweiterung](/img/content/scr_transactionrecorder-chrome-extension-popup.min.png)
4.  Klicke auf **Erweiterung hinzufügen**. Abhängig von deinen Einstellungen musst du eventuell Pop-ups für den Chrome Web Store erlauben.
5.  Nachdem du die Erweiterung hinzugefügt hast und diese mit Pin angeheftet wurde, erscheint in der Adressleiste deines Chrome-Browsers das ITRS Logo. Wenn du diese Erweiterung nicht mit einem Pin versehen hast (oder den Pin entfernt hast), kann sie über das Menü Erweiterungen (Puzzleteil-Symbol) aufgerufen werden.
![screenshot Uptrends Erweiterung hinzugefügt](/img/content/scr_transactionrecorder-chrome-extension-icon.min.png)

Der Transaktionsrekorder steht nun zum Einsatz bereit.

## Den Transaktionsrekorder nutzen {id="using-transaction-recorder"}

1. Öffne ein neues Chrome-Browser-Fenster und [deaktiviere automatische Ausfülloptionen](https://support.boldbrush.com/faso-account-login/disable-clear-autofill-in-browser), die du eventuell aktiviert hast. Der Rekorder kann automatisch ausgefüllte Texte nicht erkennen.
2. Um den Transaktionsrekorder zu starten, klicke auf das ITRS-Logo rechts in der Adressleiste.
   Ein neues Fenster wird geöffnet, welches detaillierte Anweisungen und wichtige Hinweise enthält.
![Screenshot Transaktionsrekorder Start](/img/content/scr_transaction-recorder-start.min.png)
2.  Lies die **Kurzanleitung** und **wichtigen Hinweise**, bevor du fortfährst.
3.  Klicke auf die Schaltfläche **Start recording** unten links.
    Es öffnet sich vielleicht eine Pop-up-Meldung mit dem Hinweis, dass die Fenstergröße angepasst werden muss. Erlaube dem Rekorder, die Fenstergröße anzupassen.
    Vor dem Rekorder-Fenster wird ein neues Browser-Fenster geöffnet.
![Screenshot Startseite](/img/content/scr_transactions-REC-Start-page_040824.min.png)
4.  Navigiere zur Startseite, indem du die URL in die Adressleiste des Aufzeichnungsfensters eingibst.
5.  Klicke durch die Transaktion, um alle Schritte aufzuzeichnen. Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="de" >}}) an, um mehr über User-Journey-Transaktionen zu erfahren.
6.  Wechsle zum Rekorder-Fenster, wenn du das Ende deiner Transaktion erreicht hast.
![Transaktionsrekorder-Fenster mit Schritten](/img/content/scr_transaction-recorder-with-steps.min.png)
7.  Überprüfe dein Skript.
    Du kannst unnötige Aktionen, die der Rekorder auf deinem Weg durch die Website aufgezeichnet hat, löschen. Bedenke, dass du über den Step-Editor bei den Prüfobjekteinstellungen Schritte hinzufügen kannst, Dinge entfernen und Inhaltsprüfungen einfügen kannst, aber dass deine Aufzeichnung zu diesem Zeitpunkt so klar wie möglich sein sollte. Wenn du denkst, dass du zu viele zusätzliche Klicks erfasst hast oder dass es andere Probleme gibt, kannst du diese Aufzeichnung immer auch komplett löschen und von vorn beginnen.
8.  Klicke auf **Stop recording**, wenn du zufrieden bist oder von vorn beginnen möchtest.
9. (Optional) Wenn du die Aufzeichnung erneut vornehmen möchtest, klicke auf **Clear recording** und folge erneut den obigen Anweisungen.
10. Bist du mit der aufgezeichneten Transaktion zufrieden, wähle **Upload recording** (erscheint unten rechts, nachdem du die Aufzeichnung gestoppt hast).
11. Melde dich bei deinem Uptrends Account an.
12. Gib deiner Aufzeichnung einen Namen, der für das Transaktionsprüfobjekt verwendet wird, das automatisch in deinem Account erstellt wird. Anhand des Namens findest du dein Prüfobjekt in der *Prüfobjekt-Übersicht*. Du kannst den Prüfobjektnamen später ändern.
![Screenshot Aufzeichnungsdetails](/img/content/scr_transaction-upload.min.png)
13. Wähle, ob du [Self-Service oder Full-Service Transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="de" >}}) nutzen möchtest. Deine Option dabei sind:
    
    a) **I'll test and optimize this transaction by myself first.** – Self-Service Transactions. Wähle diese Option, wenn du das Skript selbst anpassen und testen möchtest. Damit wird in deinem Account ein neues Transaktionsprüfobjekt erstellt. Unser [Support]({{< ref path="contact" lang="de" >}}) steht aber immer bereit, dir gegebenenfalls weiterzuhelfen.
    
    b) **Let Uptrends Support stabilize this transaction for me** – Full-Service Transactions. Wähle diese Option, wenn du die Aufzeichnung an das Support-Team senden möchtest, damit es die Skriptentwicklung und das Testen für dich übernimmt.

13. Gib alle Informationen, die du oder der Skriptentwickler eventuell benötigt, in das Textfeld ein.
14. Klicke auf **Start upload**, um ein neues Prüfobjekt in deinem Account zu erstellen (Self-Service Transaction) oder die Aufzeichnung an das Uptrends Support-Team (Full-Service Transaction) zu senden.
