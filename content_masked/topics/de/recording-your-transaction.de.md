{
  "hero": {
    "title": "Aufzeichnen der User Journey bei Shop-Funktionen"
  },
  "title": "Aufzeichnen der User Journey bei Shop-Funktionen",
  "summary": "In diesem Tutorial wirst du Schritt für Schritt durch den Aufzeichnungsvorgang geführt, bei dem du den Weg des Nutzers beim Einkauf erfasst.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/tutorial-record-user-journey-in-shop/transaction-aufzeichnen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

In diesem Beispiel durchläufst du den Prozess der Aufzeichnung einer User Journey, den Weg eines Nutzers, der seinen Warenkorb füllt und ändert.

Die folgenden Anweisungen führen dich durch ein detailliertes Beispiel des Aufzeichnungsvorgangs einer Transaktion. Sobald das Transaktionsprüfobjekt aktiv ist, verwendet es Transaktions-Credits, die du für deinen Account kaufen musst. Das Beispiel enthält Informationen darüber, welche Schritte Credits erfordern. Weitere Informationen zu den Credits findest du im Artikel [Berechnung der Prüfobjekt-Credits beim Transaktions-Monitoring]([LINK_URL_1]).

1. Lade den Transaktions-Recorder aus dem Chrome Webstore herunter und füge die Erweiterung zu deinem Chrome-Browser hinzu. Die Schritte werden in [Den Transaktions-Recorder herunterladen]([LINK_URL_2]) beschrieben.
2. Öffne in einem Chrome-Browser-Fenster die Transaktions-Recorder-Erweiterung und klicke auf die Schaltfläche [SHORTCODE_1] Start Recording [SHORTCODE_2]. Das Fenster **REC start** wird geöffnet.
3. Gib [[URL_1]) als URL in die Adresszeile des Fensters **REC start** ein.
   *Dies ist der erste Wechsel zu einer neuen Seite, was zu einer Server-Anfrage führt (verwendete Credits = 1).*
   Die Startseite des Shops wird angezeigt.
![Screenshot der Homepage Galactic Shirts]([LINK_URL_4])
4. Klicke auf das Bild des ersten Shirts, um die Produktseite zu öffnen.
   Das Shirt ändert sich eventuell, aber es sollte immer ein erstes Shirt geben. In diesem Fall ist das Shirt das Suraya Bay T-Shirt.
   *Mit Klicken auf den Link wechselst du zur Produktseite und sendest eine Server-Anfrage. Dafür wird ein weiterer Credit benötigt (verwendete Credits = 2).*
   Die Produktmerkmale für das Shirt werden angezeigt.
5. Klicke auf das Drop-down-Menü für **Size**, um die Größe „**L**“ zu wählen.
6. Ändere die Menge auf „**2**“.
   ![]([LINK_URL_5])
   Das Ändern der Menge, indem du die „1“ markierst und „2“ eingibst oder die Pfeiltasten betätigst, hat keine Auswirkung. Der Recorder registriert das Klicken und die Änderung nur als Wert.
7.  Klicke auf **Add to cart**.
    *Klicken auf *Add to cart* erzeugt eine Server-Anfrage und eine Aktualisierung der Seite, wodurch ein weiterer Credit benötigt wird (verwendete Credits = 3).*
8.  Füge ein Inhaltsprüfung hinzu. Im Rahmen von Best Practices wird empfohlen, stets [Inhaltsprüfungen]([LINK_URL_6]) einzufügen, um zu bestätigen, dass jede Seite wie erwartet geladen wird. In diesem Beispiel sollten wir sicherstellen, dass die Aktion „Zum Warenkorb hinzufügen“ richtig funktioniert hat (eine von vielen Inhaltsprüfungen, die du für dein Skript erwägen solltest). Du kannst eine Inhaltsprüfung auf drei unterschiedliche Weisen hinzufügen: über die Schaltfläche **Inhaltsprüfung hinzufügen** oder über das Kontextmenü. Du kannst Inhaltsprüfungen später auch mithilfe des Prüfobjekt-Schritte-Editors in deinem Account hinzufügen.

    Um eine Inhaltsprüfung über die Schaltfläche **Add content check** hinzuzufügen:
      
    1. Gehe zum Rekorder-Fenster (häufig hinter dem Browser-Fenster zu finden) und klicke auf [SHORTCODE_3] + Add content check[SHORTCODE_4]
![screenshot recorder content check]([LINK_URL_7])      

    2. Wähle einen Teil der Bestätigungsseite, der einzig auf dieser Seite vorkommt und sich wahrscheinlich nicht ändert. In diesem Fall eignet sich „added to your cart“. Gib dies in das Pop-up-Fenster **Add content check** ein.
![screenshot content check pop up]([LINK_URL_8])
    3. Klicke auf [SHORTCODE_5]Speichern[SHORTCODE_6].
    4. Kehre zum Aufzeichnungsfenster zurück.

    Um eine Inhaltsprüfung über das Kontextmenü hinzuzufügen:

    1. Markiere den Text „added to your cart“.
    2. Klicke die rechte Maustaste und wähle *ITRS Uptrends Transaction Recorder* im Kontextmenü.
    3. Wähle dann *Create a content check*. Diese Inhaltsprüfung wurde nun im Transaktionsrekorder-Fenster aufgezeichnet.
    4. Kehre zum Aufzeichnungsfenster zurück.

    ![Screenshot Menüoption Inhaltsprüfung]([LINK_URL_9])

Die Inhaltsprüfung wurde nun eingefügt.

9.  Klicke auf **View Cart**, um die Warenkorbanzeige aufzurufen.
    *Dafür wird ein weiterer Credit benötigt (verwendete Credits = 4).*
10.  Ändere die Menge von „2“ auf „1“.
11. Klicke auf **Update cart**.
    *Das Aktualisieren des Warenkorbs aktualisiert die Seite, wodurch eine Server-Anfrage gesendet und ein weiterer Credit benötigt wird (verwendete Credits = 5).*
![Screenshot Update Warenkorb]([LINK_URL_10])
12. Füge eine Inhaltsprüfung hinzu, um zu verifizieren, dass die Seite korrekt geladen wurde, indem du auf den Text „Cart updated“ prüfst.
13. Klicke auf das rote „X“, um den Artikel aus dem Warenkorb zu entfernen und die Transaktion zu beenden.
    *Das Entfernen des Artikels erzeugt eine Server-Anfrage und ein weiterer Credit wird benötigt (verwendete Credits = 6).*
14. Füge eine Inhaltsprüfung mit dem Satz „Your cart is currently empty“ hinzu.
15. Eine andere Möglichkeit zu verifizieren, dass der Warenkorb leer ist, besteht darin, mit dem Mauszeiger auf das Warenkorb-Symbol oben rechts am Bildschirm zu zeigen. Beachte, dass der Transaktionsrekorder nicht automatisch einen Schritt aufzeichnet, wenn du auf Elemente der Website zeigst bzw. darüber „hoverst“. Du musst dies daher manuell hinzufügen.
    
    Um eine Hover-Aktion während des Aufzeichnens hinzuzufügen:
    1. Klicke mit der rechten Maustaste auf das Element, über dem du die Hover-Aktion, in diesem Fall das Warenkorb-Symbol, ausführen möchtest.
    2. Klicke im Kontextmenü auf *ITRS Uptrends Transaction Recorder*.
    3. Klicke auf *Create hover action*. Du wirst sehen, dass der Schritt im Transaktionsrekorder-Fenster aufgezeichnet wurde.
    4. Bei diesem Beispiel erscheint beim Zeigen mit der Maus auf das Warenkorb-Symbol die Nachricht „No products in the cart“.   In Fällen, bei denen eine Hover-Aktion mit der Maus ein Element sichtbar macht, kannst du auch die Aktivität eines Elements nachverfolgen, dass sichtbar sein muss. Du kannst dies mit demselben Ansatz ausführen wie die Hover-Aktion, indem du mit der rechten Maustaste auf das sichtbare Element (*„No products in the cart“-Element*) klickst. Klicke im Kontextmenü auf *ITRS Uptrends Transaction Recorder* > *Wait for this element to be visible*.

     ![Screenshot leerer Warenkorb]([LINK_URL_11])

Sowohl die Hover-Aktion als auch das Element, das sichtbar sein muss, wurden nun aufgezeichnet.

16. Füge eine Inhaltsprüfung mit dem Satz „No products in the cart“ hinzu.
17. Da dein Warenkorb nun leer ist, kannst du nach einer anderen Art Shirt anhand des Suchfelds für Produkte oben rechts am Bildschirm suchen. Gib *Summer* ein. Beachte, dass das Feld nicht über eine Suchen-Schaltfläche verfügt. Stattdessen kannst du die *Eingabetaste* drücken, um Suchergebnisse zu erhalten.

    Der Transaktionsrekorder kann auch solche Tastatureingaben der Nutzer erfassen. Das ist nützlich, wenn es eine Website mit der Anweisung *Irgendeine Taste drücken, um fortzufahren* oder *Die Eingabetaste drücken, um zu bestätigen* ist. Beachte, dass du im Gegensatz zu Mausklickaktionen (bei denen eine Bewegung automatisch aufgezeichnet wird) manuell eine Tastaturaktion hinzufügen musst, um ein Tastaturereignis als Aktivität aufzuzeichnen.

    Um eine Tastaturaktion während des Aufzeichnens hinzuzufügen:
    1. Wechsle zum Recorder-Browserfenster (in der Regel hinter deinem Browser-Fenster):
       Klicke auf [SHORTCODE_7] +Add keyboard action[SHORTCODE_8].
    2. Es erscheint ein Pop-up mit einem Drop-down-Menü, aus dem du die Taste, die gedrückt werden soll, wählen kannst. Du kannst verschieden Zeichen wählen, darunter Steuerungstasten, Spezialtasten, Zifferntasten, Nummernblocktasten, Groß- und Kleinbuchstaben.
![screenshot Pop-up Tastaturaktion hinzufügen]([LINK_URL_12])
    3. Wähle, ob die Taste allgemein oder nur auf das aktuelle Element im Fokus gedrückt werden soll. Wenn du die Option *Global* wählst, wird dieses spezielle Tastaturereignis in der gesamten Anwendung berücksichtigt. Die andere Option wird nur auf das *zuletzt geklickte Element* angewendet, wie in Klammern des Optionsschalters angegeben.
    4. Klicke auf [SHORTCODE_9]Speichern[SHORTCODE_10] und kehre zum Browser-Aufzeichnungsfenster zurück.

    *Die Suche nach einem neuen Shirt erzeugt eine Server-Anfrage und erfordert ein Credit (verwendete Credits = 7).*

18. Füge eine Inhaltsprüfung hinzu, um sicherzustellen, dass das Shirt nicht existiert, indem du auf den Text „No products were found matching your selection“ testest.
19. Klicke auf [SHORTCODE_11] Stop recording[SHORTCODE_12].
20. Klicke auf **Upload recording** und wähle Self-Service Transaction), um die Transaktion zunächst selbst zu testen und zu optimieren. Lies unseren Knowledge-Base-Artikel [Optionen für Transaktionsskripte]([LINK_URL_13]), um mehr über Self-Service und Full-Service Transactions zu erfahren.

Dies ist das Ende des Aufzeichnungsvorgangs der User Journey bei Shop-Funktionen. Dein Uptrends Account hat nun ein neues Transaktionsprüfobjekt. Dieses Prüfobjekt wird wahrscheinlich sieben Transaktions-Credits benötigen, aber es gibt andere Faktoren, die sich auf die [Berechnung von Credits]([LINK_URL_14]) auswirken.

Als Nächstes steht das Testen mit gegebenenfalls erforderlichen Anpassungen an der Transaktion bevor. Lies die Anweisungen in [Testen und Bearbeiten deines Transaktionsskripts]([LINK_URL_15]), um durch das Testen geleitet zu werden.
