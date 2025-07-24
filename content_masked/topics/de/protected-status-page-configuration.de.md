{
  "hero": {
    "title": "Protected Status Pages einrichten"
  },
  "title": "Protected Status Pages einrichten",
  "summary": "Dieser Artikel beschreibt, wie du eine neue Protected Status Page erstellst und Operatoren einrichtest.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/statusseiten/protected-status-page-konfiguration",
  "translationKey": "[URL_1]
}

Um eine Protected Status Page bzw. geschützte Statusseite zu erstellen, musst du die Seite sowie die notwendigen Berechtigungen für die Operatoren einrichten, die sie anzeigen können sollen. Die Berechtigungen des neuen Operators müssen eingeschränkt werden, sodass er nur auf die geschützte Statusseite (und nicht auf andere Elemente wie zum Beispiel Prüfobjekte) zugreifen kann. Beachte, dass du Administrator-Rechte benötigst, um Operatoren und Berechtigungen zu verwalten.

## Eine geschützte Statusseite erstellen


1. Erstelle einen normale Public Status Page anhand der Anweisungen unter [Public Status Pages einrichten]([LINK_URL_1]).
2. Da du eine Protected Status Page einrichtest, stelle sicher, dass das Kontrollkästchen **Publish** auf der Registerkarte [SHORTCODE_1] Allgemein [SHORTCODE_2] nicht aktiviert ist. Wenn du eine Statusseite durch Markieren von „Publish“ veröffentlichst, wird sie der allgemeinen Öffentlichkeit zugänglich sein.
3. Füge optional ein Logo ein und ändere die Farben sowie Titel- und Fußzeilen. Dies ist beschrieben unter [Public Status Pages anpassen]([LINK_URL_2]).
4. Speichere die Statusseite.
5. Du wirst in der Übersicht der Statusseiten den *Preview*-Link für die neue Statusseite sehen. Dieser Link enthält die URL, die autorisierte Nutzer zum Aufrufen der Statusseite verwenden müssen.

## Operatoren mit Zugang zur geschützten Statusseite einrichten

Du musst mindestens einen Operator erstellen und die Berechtigungen so setzen, dass der Operator nur die geschützte Statusseite aufrufen kann. Beachte, dass du ein Administrator sein musst, um Operatoren hinzuzufügen und Berechtigungen zu verwalten. Darüber hinaus benötigst du etwas Unterstützung von Uptrends, um die Einrichtung abzuschließen:

1. Füge einen [neuen Operator]([LINK_URL_3]) hinzu. Wir empfehlen dir, die neuen Anmeldedaten nicht an Dritte weiterzugeben, bevor du die nächsten Schritte durchgeführt hast.
2. Entferne bei dem neuen Operator die *Basic Operator*-[Berechtigung]([LINK_URL_4]), indem du die Operator-Einstellungen öffnest. Klicke auf der Registerkarte [SHORTCODE_3] Berechtigungen [SHORTCODE_4] im Abschnitt **Systemweite Berechtigungen** neben der Berechtigung *Basic Operator* auf [SHORTCODE_5] Deaktivieren [SHORTCODE_6].
3. Bestätige deine Wahl durch Klicken auf [SHORTCODE_7] Deaktivieren [SHORTCODE_8] im Pop-up-Fenster.
4. Klicke auf [SHORTCODE_9] Speichern [SHORTCODE_10] unten auf der Bildschirmseite des Operators.
5. Gewähre dem Operator Zugriff auf die geschützte Statusseite. Dieser Schritt erfolgt durch den Uptrends Support. Bitte [reiche ein Support-Ticket ein]([LINK_URL_5]) und fordere eine Protected Status Page an. Nenne in deiner Anfrage den Namen der Protected Status Page und den Namen der Operatoren, die Zugriff erhalten sollen. Das Support-Team wird den neuen Operatoren Zugang zur neuen Statusseite gewähren und dich benachrichtigen, sobald die Anfrage bearbeitet ist.
