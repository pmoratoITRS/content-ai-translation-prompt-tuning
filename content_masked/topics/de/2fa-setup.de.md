{
  "hero": {
    "title": "Zwei-Faktor-Authentifizierung"
  },
  "title": "Zwei-Faktor-Authentifizierung",
  "summary": "Erfahre, wie du die Zwei-Faktor-Authentifizierung (2FA) mit zeitbasierten Einmal-Passwörtern (TOTP) für Uptrends einrichtest.",
  "url": "[URL_BASE_TOPICS]account/einstellungen/2fa-einrichtung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Um die Zwei-Faktor-Authentifizierung für Uptrends einzurichten, muss der Account-Administrator zunächst die Standardeinstellung für den gesamten Account konfigurieren. Danach können die allgemeinen Einstellungen für Operatoren einzeln überschrieben werden, sofern die Konfiguration dies vorsieht. Es kann eine Authentifizierungs-App nach Wahl genutzt werden.

## Standardanmeldeoptionen für den gesamten Account aktivieren 
Diese Einstellung kann nur von einem Account-Administrator vorgenommen werden.

Rufe in Uptrends [SHORTCODE_3] Accounteinstellungen > Account Einstellungen [SHORTCODE_4] auf und aktiviere eine der Optionen für die **Zwei-Faktor-Authentifizierung**.

![Screenshot 2FA Accounteinstellungen]([LINK_URL_1])
  - **Erforderlich** – [Basic Operatoren]([LINK_URL_2]) müssen die Zwei-Faktor-Authentifizierung unter Einsatz eines zeitbasierten Einmal-Passworts verwenden.
  - **Optional** – Basic Operatoren können wählen, ob sie die Zwei-Faktor-Authentifizierung mit einem zeitbasierten Einmal-Passwort nutzen möchten.
  - **Deaktiviert** – Im gesamten Account kann die Zwei-Faktor-Authentifizierung mit zeitbasiertem Einmal-Passwort nicht genutzt werden.

## Einstellungen der Zwei-Faktor-Authentifizierung für Operatoren
Nach der Konfiguration der Standardanmeldeoptionen für Operatoren, wähle auf der Operatorseite auf der Registerkarte [SHORTCODE_5] Allgemein [SHORTCODE_6] im Abschnitt **Login Optionen für diesen Operator** eine Anmeldeoption. Hier wird die Standardeinstellung für die Zwei-Faktor-Authentifizierung des Accounts angezeigt und die Option des Überschreibens der Account-weiten Einstellungen für die Zwei-Faktor-Authentifizierung für diesen Operator gegeben. (Diese Einstellung kann ebenfalls nur von einem Account-Administrator vorgenommen werden.)

![Screenshot 2FA Anmeldeoptionen für Operatoren]([LINK_URL_3])
Aktiviere unter **Zwei-Faktor-Authentifizierung Einstellungen** das Kontrollkästchen **Einstellungen der Zwei-Faktor-Authentifizierung überschreiben**, um bei Bedarf die allgemeingültigen Einstellungen außer Kraft zu setzen.
-   **Erforderlich** – Zwei-Faktor-Authentifizierung muss verwendet werden. Die Einstellung wird bei der nächsten Anmeldung des Operators wirksam.
-   **Optional** – Zwei-Faktor-Authentifizierung kann manuell auf diesem Bildschirm eingerichtet werden.
-   **Deaktiviert** – Zwei-Faktor-Authentifizierung kann nicht verwendet werden.

Um die Konfiguration der Zwei-Faktor-Authentifizierung zu löschen und neu einzurichten, klicke auf [SHORTCODE_7] Zwei-Faktor-Authentifizierung zurücksetzen [SHORTCODE_8].

[SHORTCODE_1]
**Hinweis**: Die Zwei-Faktor-Authentifizierung mit zeitbasierten Einmal-Passwörtern funktioniert nicht in Kombination mit dem [Single Sign-on (SSO) in Uptrends]([LINK_URL_4]).
[SHORTCODE_2]

Es gibt unterschiedliche Möglichkeiten, wie ein Administrator oder Operator die Einrichtung der Zwei-Faktor-Authentifizierung aktivieren bzw. auslösen kann:

### Einstellungen des Operators
Wechsle in Uptrends auf der Operatorseite zur Registerkarte [SHORTCODE_9] Allgemein [SHORTCODE_10]. Führe dies aus, indem du auf den Operatornamen am Ende des Hauptmenüs klickst und [SHORTCODE_11] Benutzereinstellungen [SHORTCODE_12] wählst. Klicke dann auf [SHORTCODE_13]  Scanne den QR-Code [SHORTCODE_14], um die Zwei-Faktor-Authentifizierung einzurichten. Es öffnet sich ein Pop-up-Fenster.

Wähle eine Authentifizierungs-App nach Wahl, um den QR-Code zu scannen. Solltest du den Code nicht scannen können, wechsle zur manuellen Eingabe, indem du auf den Link unter dem Code klickst. Klicke [SHORTCODE_15] Weiter [SHORTCODE_16] und gib den bereitgestellten 6-stelligen Code ein. Nachdem du auf [SHORTCODE_17] Beenden [SHORTCODE_18] geklickt hast, ist die Zwei-Faktor-Authentifizierung eingerichtet.

### Auf Operator-Einladung
Wenn ein Operator, der die Zwei-Faktor-Authentifizierung verwenden muss, [zu Uptrends eingeladen wird]([LINK_URL_5]), ist der Ablauf zur Einrichtung der Zwei-Faktor-Authentifizierung Teil der Annahme der Einladung des Operators. Der Authentifizierungablauf ist derselbe – mit einer Authentifizierungs-App nach Wahl, die ein zeitbasiertes Einmal-Passwort erzeugt.

### Per E-Mail-Link
Nach der Anmeldung wird dem Operator, der die Zwei-Faktor-Authentifizierung verwenden muss, eine Seite mit dem Hinweis auf eine E-Mail angezeigt. Die E-Mail-Nachricht enthält einen Link zu einer Seite in Uptrends, auf der die Zwei-Faktor-Authentifizierung aktiviert werden kann. Danach ist der Operator angemeldet. Der Operator muss sich ab dem Zeitpunkt mit einem zeitbasierten Einmal-Passwort anmelden.