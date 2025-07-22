{
  "hero": {
    "title": "SMS-basierte 2FA"
  },
  "title": "SMS-basierte 2FA bei Transaktionen",
  "summary": "Erfahre, wie du eine SMS-basierte 2FA bei deinen Transaktionsprüfobjekten einrichtest.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/sms-basierte-2fa",
  "translationKey": "[URL_1]
}

In einer Welt, in der Sicherheit und Schutz persönlicher Daten immer wichtiger werden, möchten sich viele Organisationen nicht mehr nur auf eine Anmeldeaktion für einen sicheren Zugriff auf Webanwendungen verlassen. Um mit größerer Wahrscheinlichkeit feststellen zu können, dass es sich bei einem Anmeldevorgang um einen echten Nutzer handelt, verwenden Webanwendungen nun die mehrstufige bzw. Multi-Faktor-Authentifizierung (MFA), die häufig als 2-Faktor-Authentifizierung (2FA) umgesetzt wird, und verlangen vom Nutzer zwei Identitätsnachweise.

Die häufigsten Methoden eines Identitätsnachweises neben der üblichen Benutzername-Passwort-Kombination basieren auf das Senden eines eindeutigen Codes per E-Mail, SMS oder einer mobilen Authentifizierungs-App.

Diese zusätzliche menschliche Interaktion stellt eine Herausforderung für das automatisierte Testen einer Webanwendung dar. Dieser Artikel beschreibt den Ansatz, den Uptrends derzeit für die SMS-basierte 2FA beim Uptrends Transaktions-Monitoring unterstützt.

[SHORTCODE_1] **Hinweis**: MFA-Einrichtungen, die sich auf Authentifizierungs-Apps stützen, werden [ebenfalls unterstützt]([LINK_URL_1]). [SHORTCODE_2]

## Normaler Ablauf eines SMS-basierten 2FA-Szenarios
Dies ist der Ablauf, den wir bei einem 2-Faktor-Authentifizierungsverfahren mit einer SMS-Nachricht für eine Webanwendung erwarten:

1. Auf der Anmeldeseite eine Anwendung gibt der Nutzer seine Anmeldedaten in die entsprechenden Felder ein. Dies ist der erste Schritt des 2FA-Identifizierungsablaufs.
2. Diese Anmeldung sollte im zugrunde liegenden System das Senden einer SMS-Nachricht an die Mobiltelefonnummer auslösen, die vom Nutzer voreingestellt wurde.
3. Während die SMS-Nachricht gesendet wird, wechselt die Webanwendung auf eine neue Seite mit einem Textfeld, in dem die Eingabe des Nutzers erwartet wird.
4. Wenn der Nutzer die SMS-Nachricht erhält, sieht er einen eindeutigen Code, der auf der neuen Webseite eingegeben werden muss. Dies ist der zweite Schritt des 2FA-Identifizierungsablaufs.
5. Stimmt alles überein, kann der Nutzer die Webanwendung aufrufen.
6. Sobald er vollständig angemeldet ist, erledigt der Nutzer seine Aufgaben in der Webanwendung.

## Überblick über die Uptrends Lösung für die SMS-basierte 2FA
Statt eines tatsächlichen Mobiltelefons setzt Uptrends eine virtuelle Telefonnummer ein, die zum Empfang von SMS-Nachrichten zur Verfügung steht. Es sind einige einfache manuelle Schritte seitens Uptrends erforderlich, um die SMS-Komponente des 2FA-Verfahrens einzurichten.

Eine der Aktionen im Transaktionsskript wird das Warten auf die eingehende SMS-Nachricht erfordern. Wurde die Nachricht empfangen, wird der eindeutige Code (in der Regel ein numerischer 6-Ziffern-Code, aber andere Formate werden ebenfalls unterstützt) extrahiert und kann zur Eingabe in das entsprechende Feld genutzt werden. Dieser Vorgang ist eine exakte Simulation dessen, was ein normaler Nutzer durchführen würde, sodass es eine sehr gute Lösung für das Endnutzer-Testen ist.

## Schritte zur Einrichtung einer SMS-basierten 2FA bei einer Transaktion
1. In der Einrichtungsphase bei der Erstellung einer Transaktion ist eine erste Besprechung und manuelle Vorbereitung erforderlich. [Wende dich an den Support]([LINK_URL_2]), um die ersten Schritte zu unternehmen.
2. Es wird kein physisches Mobiltelefon verwendet. Stattdessen wird eine neue virtuelle Telefonnummer bei unserem Partner, Twilio, angefordert. Dafür müssen wir wissen, in welchem Land die Telefonnummer registriert werden soll.
3. Nach dieser Registrierung muss die neue Mobiltelefonnummer im Nutzerprofil der Zielanwendung vorkonfiguriert werden. Zudem muss im Nutzerprofil eventuell die Anforderung der SMS-basierten 2-Faktor-Authentifizierung aktiviert werden.
4. Bevor Uptrends an der Einrichtung der Transaktion arbeitet, ist es sinnvoll, einen manuellen Test durchzuführen, um zu sehen, ob die Einrichtung korrekt funktioniert und eine SMS-Nachricht auslöst, die das System von Uptrends empfangen kann.
5. Wurde bestätigt, dass die SMS-Kommunikation zuverlässig funktioniert, richtet Uptrends Support eine Transaktion ein (üblicherweise auf Grundlage einer Transaktionsaufzeichnung anhand unseres [Browser-Plug-ins, dem Transaktionsrekorder]([LINK_URL_3])).

![Eine SMS-basierte 2FA-Aktion bei einem Transaktionsskript]([LINK_URL_4])

6. Nach dem Testen der Transaktion und der Inbetriebnahme des Prüfobjekts, kann die Transaktion ohne Hilfe seitens des Uptrends Supports verwaltet und aktualisiert werden. Das Support-Team steht aber weiterhin gern helfend zur Verfügung.



## Kosten
Es fallen die [normalen Kosten für eine Transaktion]([LINK_URL_5]) an. Diese Kosten richten sich nach der Anzahl der Aktionen, die den Browser veranlassen, eine neue Seite aufzurufen. Zusätzlich zu den üblichen Kosten wird ein Transaktions-Credit für die Warte–Aktion auf die SMS berechnet.

## Vorbehalte
Einige 2FA-Systeme senden nicht zu jeder versuchten Anmeldung eine SMS-Nachricht. Wir empfehlen eine Konfiguration, die für jede Prüfung dasselbe Verhalten zeigt. Damit wird das Transaktionsskript vorhersehbarer und es erhöht erheblich die Chance, dass ein Problem mit dem 2FA-System so schnell wie möglich erkannt wird.

Wird eine Telefonnummer für eine Transaktion registriert, funktioniert sie nur für **eine Transaktion**. Muss die 2FA in mehreren Transaktionen verwendet werden, wird jeweils eine Telefonnummer für jede Transaktion benötigt. Der Grund hierfür ist, dass die Transaktionsskripte nebeneinander, wahrscheinlich sogar simultan ausgeführt werden. Dann wäre es unmöglich, festzustellen, welche SMS-Nachricht sich auf welche Transaktion bezieht, wenn die Nachrichten an dieselbe Telefonnummer gesendet werden.
