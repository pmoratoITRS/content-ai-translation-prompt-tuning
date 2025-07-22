{
  "hero": {
    "title": "Single Sign-on setup guide"
  },
  "title": "Single Sign-on setup guide",
  "url": "[URL_BASE_TOPICS]account/einstellungen/sso-setup-guide",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dieser Artikel führt Dich durch die Schritte der Einrichtung des [Single Sign-ons (SSO) in Uptrends]([LINK_URL_1]). Bevor Du in Erwägung ziehst, ein Single Sign-on einzurichten, bedenke diese Faktoren:

-   Du benötigst Zugang zu einem externen Identity-Provider-(IdP)-Produkt, anhand dessen Dein Unternehmen das Single Sign-on-Verfahren einsetzen kann. Dieser IdP wird die zentrale Stelle für deine Nutzer sein, um Zugang zu Uptrends und andere Anwendungen zu erhalten. Uptrends nutzt das [SAML 2.0-Protokoll]([LINK_URL_2]) für Single Sign-on, sodass jeder IdP, der SAML 2.0 unterstützt, funktionieren sollte. Bitte prüfe die Hinweise Deines IdPs, in denen die Verfahren beschrieben werden, wie eine neue Anwendung (oder ein Service Provider, SP) zu Deiner Einrichtung hinzugefügt wird.
-   Bei Uptrends musst Du den [Enterprise Plan]([LINK_URL_3]) abonniert haben, um SSO zu nutzen. Solltest Du derzeit einen anderen Abo-Plan nutzen oder nicht sicher sein, welches Abo Du hast, [wende Dich an unser Support-Team]([LINK_URL_4]), um Deine Möglichkeiten zu überprüfen.

## Single Sign-on bei Uptrends aktivieren

1.  Wechsele auf der Seite von Uptrends zu den Account-Einstellungen (Account > Account Einstellungen) und markiere die Option **Single Sign-on (SSO) aktivieren**. Solltest Du diese Option nicht sehen, musst Du eventuell ein Upgrade nach Uptrends Enterprise durchführen.  
    Wenn Du SSO in Deinem Account aktiviert hast, werden zwei neue Abschnitte eingeblendet, in dem die Standard-Login-Optionen für Operator (siehe unten) und Deine SSO-Einstellungen aufgeführt werden.

2.  In den Single Sign-on Einstellungen siehst Du das Feld **Single Sign-on URL**. Dies ist eine vordefinierte URL, die Du in einem der nächsten Schritte in die Konfiguration Deines IdPs kopieren musst.

3.  Melde Dich bei Deinem Identity Provider mit Administratorrechten an. **Richte eine neue SAML-basierten Anwendung ein**, gib ihr einen angemessenen Namen (z. B. *Uptrends*) und füge optional das Logo von Uptrends hinzu.

4.  Sofern es Dein IdP erfordert, stelle sicher, dass Du ein **IdP-initiiertes Setup** spezifizierst, statt eines SP-initiierten. Wenn Du zudem die Web-Plattform des Service Providers angeben musst, wähle Microsoft IIS.

5.  Dein IdP wird nach der **Single Sign-on URL des Service Providers** fragen (oder nach dem SAML-Endpunkt). Bitte verwende die in Schritt 2 genannte Single Sign-on-URL.

6.  Einige IdPs fragen nach der **Audience URI bzw. Entity ID**: Bitte gib die gleiche URL ein, die Du im vorherigen Schritt verwendet hast. Einige IdPs spezifizieren jedoch ihre eigene Audience URI bzw. Entity ID. In dem Fall kopiere den Wert und füge ihn in das Feld Audience URI/Entity ID in Deinen Uptrends SSO-Einstellungen ein.

7.  Dein IdP lässt Dich wahrscheinlich bestimmen, welches Feld vom Identity Provider genutzt werden soll, damit der Service Provider erkennt, welcher Nutzer versucht, sich anzumelden. Diese Option wird häufig **Name ID Format** genannt. Uptrends verwendet die E-Mail-Adresse des Nutzers, wähle daher *Email* oder *EmailAddress* als Wert.

8.  Beende die Einrichtung bei Deinem IdP. Am Ende der Einrichtung stellt Dein IdP die Konfigurationsdaten bereit, die Uptrends benötigt, um die SSO-Einrichtung abzuschließen. Je nach IdP erhältst Du die **Identity Provider Single Sign-on URL** und die Z **ertifikatsdaten** (einen X.509 Public Key) oder Du musst eine separate XML-Datei herunterladen, in der diese Informationen enthalten sind.  

    Wenn Dein IdP Dir eine XML-Metadatendatei bereitstellt: Öffne die Datei als Textdatei und suche die entsprechenden Informationen heraus. Solltest Du nicht sicher sein, welche dies sind, wende Dich bitte an unser Support-Team. 

    Finde einen XML-Node, der ähnlich aussieht wie dieses Beispiel

    [INLINE_CODE_1]

    Die URL im **Location**-Attribut ist der Wert, den Du im nächsten Schritt benötigst.

    Finde auch einen XML-Node namens

    [INLINE_CODE_2]

    Die Base64-kodierten Daten in diesem Node sind die Zertifikatsdaten, die Du gleich benötigst.

9.  In den Einstellungen Deines Uptrends Accounts kopierst Du die Single Sign-on URL Deines Identity Providers in das Feld **Login URL**. 

10.  Der nächste Schritt besteht darin, die von Deinem IdP generierten Zertifikatsdaten in Deiner [Uptrends Vault]([LINK_URL_5]) zu speichern.  Klicke auf den Link *Erstelle ein Vault Item* im Feld Zertifikat. Ein neuer Browser-Tab öffnet sich. Darin kannst Du ein neues Item zur Speicherung der Public-Key-Daten in der Vault erstellen. Erteile einen wiedererkennbaren Namen (z. B. SSO-Zertifikat) und stelle sicher, dass der Typ auf **Public Key des Zertifikats** gesetzt ist.  
    Kopiere in das Feld **Public Key** die Base64-kodierten Daten ein, die Du bereits herausgesucht hast.  Speichere das neue Vault Item. 

11. Kehre zurück zum vorherigen Browser-Tab mit den Account-Einstellungen. Klicke auf *Aktualisieren*, um die Liste der verfügbaren Items neu zu laden, sodass nun das eben erstellte Vault Item angezeigt wird. Wähle schließlich das SSO-Zertifikat aus.  
    In Fällen, in denen du ein Zertifikats-Rollover benötigst (beispielsweise, wenn ein zuvor hochgeladenes Zertifikat bald abläuft und ein nahtloser Übergang zum folgenden Zertifikat erforderlich ist), kannst du festlegen, alle Vault Items eines Vault-Bereichs zu verwenden. Wähle dafür die Option 'Durchsuche diesen gesamten Abschnitt, um das geeignete Zertifikat zu finden' aus dem Drop-down-Menü Zertifikat. Klicke auf [SHORTCODE_1]Speichern[SHORTCODE_2] , um die SSO-Einrichtung abzuschließen.

12.  Dein Single Sign-on Setup ist jetzt einsatzbereit. 

## Verwalten der Login-Optionen 

Wenn du das Single Sign-on in Deinem Account richtig konfiguriert hast, kannst Du entscheiden, ob das SSO-basierte Anmelden für alle Operator zugleich aktiviert werden soll. 

In den Account-Einstellungen kannst Du das Standard-Verfahren für alle Operator festlegen. Du kannst sowohl das klassische Benutzername/Passwort-basierte Login als auch das SSO-basierte Login aktivieren bzw. deaktivieren. Wenn Du jedoch beide deaktivierst, sperrst Du natürlich alle Operator aus. 

Das übliche Szenario ist, zunächst Benutzername/Passwort-basierte Logins aktiviert zu belassen, dann die SSO-basierten Logins mit einigen Nutzern zu testen und schließlich das Benutzername/Passwort-basierte Login für alle Operator zu deaktivieren, um zu gewährleisten, dass jeder das Single Sign-on verwendet, um auf Uptrends zuzugreifen. 

Neben dem Standard-Verfahren kannst Du Ausnahmen für einzelne Operator eingeben. Wenn Du Dir die Einstellungen eines Operators ansiehst, wirst Du feststellen, dass sowohl die Einstellungen des Benutzername/Passwort-Logins als auch des SSO-Logins zunächst auf "Account Standard" lauten. Das bedeutet, dass das Standard-Verfahren, das Du in den Account-Einstellungen festgelegt hast, für diesen Operator zutreffen. 

Du kannst für jeden Operator unterschiedliche Einstellungen wählen, um die Login-Optionen zu gestatten oder eben nicht. Dies ist beispielsweise nützlich, wenn Du von allen regulären Operator das Verwenden des Single Sign-ons forderst, aber nicht von einem oder mehreren speziellen Operator, die Du erstellt hast, um Personen außerhalb des Unternehmens Zugang zu Berichten zu gewähren. Sie haben vielleicht keinen Zugang zu Deinem Identity Provider, aber Du kannst ihnen dennoch ermöglichen, auf Uptrends anhand des regulären Benutzername/Passwort-Logins zuzugreifen.
