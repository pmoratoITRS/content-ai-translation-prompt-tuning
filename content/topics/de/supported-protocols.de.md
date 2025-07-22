{
  "hero": {
    "title": "Unterstützte Protokolle"
  },
  "title": "Unterstützte Protokolle",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/unterstuetzte-protokolle",
  "summary":"Eine Liste der von Uptrends unterstützen Protokolle.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/supported-protocols"
}

## Unterstützte Protokolle

Fragst du dich, ob Uptrends die Protokolle unterstützt, die du brauchst, um deine Websites, Server, Webapplikationen und andere Webservices zu überwachen? **Die Antwort**: Darauf kannst du wetten!

**Uptrends unterstützt**: *HTTP*, *HTTPS*, *SMTP*, *POP3*, IMAP, *Ping*, *DNS*, *FTP*, *Connect*, *SQL*, *MySQL* und noch weitere.

## HTTP

#### Was ist das HTTP-Protokoll?

Das **HTTP-Protokoll** wird verwendet, um ungesicherte Webseiten anzuzeigen und Interaktionen auszuführen. Es ist der Standard-Prüfobjekttyp bei Uptrends und sollte gewählt werden, wenn du eine Webseite überprüfen musst.

#### Wie funktioniert das HTTP-Protokoll?

Zunächst musst du ein [neues Prüfobjekt hinzufügen]({{< ref path="support/kb/basics" lang="de" >}}) (vollständig mit URL für das Monitoring).

Wenn das Monitoring dann ausgeführt wird, kontaktiert der Service von Uptrends die Webadresse. Er prüft auf übliche Netzwerk- und HTTP-Fehler und versucht, den Inhalt der Webseite herunterzuladen.

{{< callout >}}
**Hinweis:** Dieser Prüfobjekttyp lädt nur den HTML-Inhalt der Seite herunter. Es umfasst keine Bilder, Scripts oder interaktiven Objekte, die Teil einer Seite sein können. Wenn du den vollständigen Inhalt einer Webseite überprüfen möchtest, schlagen wir vor, dass du den Prüfobjekttyp Full Page Check in Betracht ziehst.
{{< /callout >}}

#### Kann ich mit dem HTTP-Protokoll mehr überwachen?

Ja! Neben den einfachen oben genannten Überprüfungen kannst du auch Folgendes prüfen:

**Ladezeiten:**

Wenn du Zeiteinschränkungen einstellst, werden wir prüfen, ob die Gesamtladezeit der Webseite innerhalb dieser Grenzen liegt. Mit anderen Worten: Wir können überprüfen, dass deine Webseite so schnell lädt, wie du es erwartest.

**Größe**:

Wir können überprüfen, dass der heruntergeladene Inhalt größer ist als die Mindestzahl an Bytes oder Zeichen, die du festlegst. Dies ist nützlich, wenn du sicherstellen möchtest, dass eine bestimmte Datei auf deinem Webserver (etwa ein generiertes Bild) nicht defekt oder leer ist.

**Inhalt:**

Uptrends kann verifizieren, dass ein bestimmtes Wort oder eine Phrase tatsächlich im Inhalt der Seite vorhanden ist. Dies ist eine leistungsstarke Möglichkeit zu überprüfen, dass deine Webseite den richtigen Inhalt zeigt.

Wähle ein Wort oder eine Phrase, das bzw. die ein wesentlicher Bestandteil deiner Seite ist, etwas, das im Falle eines Fehlers nicht gezeigt wird. Gib einfach das Wort oder die Phrase in das Feld „Übereinstimmungsmuster“ zum Abgleich ein.

In einigen Fällen möchtest du eventuell das Nichtvorhandensein eines Worts überprüfen. Beginne hierfür mit einem Rufzeichen. Wenn wir zum Beispiel verifizieren sollen, dass das Wort „Fehler“ NICHT im Inhalt vorkommt, gib !Fehler ein.

## HTTPS

#### Was ist das HTTPS-Protokoll und wie funktioniert es?

Das **HTTPS-Protokoll** ist und arbeitet genauso wie das HTTP-Protokoll (oben erwähnt), außer dass es zum Überprüfen von einer Webseite genutzt wird, die anhand eines SSL-Zertifikats geschützt ist.

## SMTP, POP3 und IMAP

#### Was sind SMTP, POP3- und IMAP-Protokolle?

Die **Protokolle SMTP, POP3 und IMAP** werden zur Verbindung mit E-Mail-Servern eingesetzt, um die ausgehende E-Mail-Funktion zu testen.

#### Wie funktionieren die SMTP, POP3- und IMAP-Protokolle?

Zunächst musst du ein „Neues Prüfobjekt hinzufügen“, bei dem du das SMTP-, POP3- oder IMAP-Protokoll wählst und die entsprechenden IP- und Port-Informationen eingibst.

Wenn das Monitoring ausgeführt wird, versucht der Service von Uptrends die IP-Adresse zu erreichen. Wenn Uptrends die Adresse erreichen kann, wird die Verfügbarkeit aufgezeichnet.

{{< callout >}}
**Hinweis**: Wenn du dich für die Option entscheidest, einen Benutzernamen und ein Passwort (Anmeldedaten für deinen E-Mail-Server) einzugeben, wird der Service von Uptrends auch versuchen, sich im Rahmen des Tests anzumelden.
{{< /callout >}}

## Ping

#### Was ist das Ping-Protokoll?

**Ping** (oder ICMP) ist eine sehr einfache Möglichkeit, zu sehen, ob ein Server noch in Betrieb und erreichbar ist.

#### Wie funktioniert das Ping-Protokoll?

Das Ping-Protokoll funktioniert, indem eine sogenannte ICMP-Echo-Anfrage gesendet wird, um zu sehen, wie lang es dauert, bis diese Anfrage den Server erreicht. Du kannst diese Option wählen, wenn keine weiteren, über das Internet aufrufbaren Dienste (Webservices, Datenbanken oder E-Mail) auf diesem Server ausgeführt werden.

{{< callout >}}
**Hinweis:** Die Einstellungen deines Netzwerks oder Servers müssen ICMP-Anfragen ausdrücklich gestatten.
{{< /callout >}}

## DNS

#### Was ist das DNS-Protokoll?

Das **DNS-Protokoll** ermöglicht dir, den Verfügbarkeitsstatus der Infrastruktur zu überwachen, die den Nutzern eine Möglichkeit bereitstellt, deine Website-Adresse aufzurufen. Beispielsweise eine URL wie www.uptrends.com statt einer IP-Adresse.

Uptrends kann lokale, primäre und spezifische DNS überwachen.

#### Wie funktioniert das DNS-Protokoll?

Melde dich an und füge ein Prüfobjekt (DNS) hinzu. Konfiguriere es mit der DNS Serveradresse (Domainname oder IP-Adresse), Port, DNS Abfragetype, Testwert und erwartetes Ergebnis.

Der häufigste Aspekt, der geprüft wird, ist, ob der Domainname (www\.yourcompany.com) noch auf die IP-Adresse deines Webservers verweist. Wenn das nicht der Fall ist, werden deine Nutzer deine Website wahrscheinlich nicht aufrufen können. Indem du diese DNS-Abfrage direkt überwachst, wird der Service von Uptrends jegliche DNS-Probleme entdecken, noch bevor deine Website für Nutzer nicht verfügbar ist.

Das DNS Monitoring von Uptrends ermöglicht dir erweiterte DNS-Überprüfungen: Verifiziere Website-Domain-Namen (A- und CNAME-Einträge), Domain-Name-Mapping des Mail-Servers (MX-Einträge), DNS-Zonen-Delegationen (NS-Einträge), autoritative Informationen über DNS-Zonen (SOA-Einträge) und andere DNS-Informationen, die in TXT-Einträgen enthalten sind (einschließlich SPF-Daten für E-Mail-Authentifizierung).

## FTP

#### Was ist das FTP-Protokoll?

Mit dem **FTP-Protokoll** kannst du die Verfügbarkeit deines FTP-Servers über den Port deiner Wahl überwachen.

#### Wie funktioniert das FTP-Protokoll?

Um das FTP-Protokoll zu nutzen, melde dich an und füge ein neues Prüfobjekt (FTP) mit den entsprechenden Daten hinzu.

Der Service von Uptrends überwacht dann den Status, indem er regelmäßig versucht, über den geeigneten Port eine Verbindung zum FTP-Server zu erstellen.

{{< callout >}}
**Hinweis**: Es ist möglich, dem Prüfobjekt Anmeldedaten hinzuzufügen, sodass du sicher sein kannst, dass die FTP-Anmeldefunktion ihren Dienst tut. Jedoch kannst du derzeit keine Dateien vom FTP-Server abrufen.
{{< /callout >}}

## Connect

Wenn kein anderes Protokoll für deine Gegebenheiten geeignet ist, kannst du das **Connect-Protokoll** für einen sehr einfachen Test einsetzen. Wenn du einen Domainnamen oder eine IP-Adresse deines Servers oder einer Firewall sowie einen Port angibst, versucht Uptrends eine einfache Verbindung zu dieser Kombination von Adresse und Port zu errichten.

## SQL

#### Was ist das SQL-Protokoll?

Das **SQL-Protokoll** ermöglicht dir, die Verfügbarkeit deiner Microsoft SQL-Server-Datenbank zu überwachen.

{{< callout >}}
**Hinweis**: SQL-Server können nur überwacht werden, wenn sich direkt (und regelmäßig) über das Internet auf sie zugreifen lässt.
{{< /callout >}}

#### Wie funktioniert das SQL-Protokoll?

Um ein SQL Monitoring auszuführen, melde dich an und füge ein Prüfobjekt (SQL) in deinem Account hinzu. Du musst wenigstens die IP-Adresse des Servers und einen Port (standardmäßig 1433) angeben.

Der Service von Uptrends versucht dann, den Server zu kontaktieren, und liefert ein positives Ergebnis, wenn alles OK ist. Er löst einen unbestätigten Fehler (und später möglicherweise einen bestätigten Fehler) aus, wenn der Server nicht erreichbar ist.

{{< callout >}}
**Hinweis**: Du kannst einen Benutzernamen und Passwort sowie einen Datenbanknamen angeben, um die Anmeldung zu testen und damit wir prüfen können, ob auf die Datenbank zugegriffen werden kann.
{{< /callout >}}

## MySQL

#### Was ist das MySQL-Protokoll?

Das **MySQL-Protokoll** ermöglicht der Uptrends Anwendung, die Verfügbarkeit von MySQL-Datenbanken zu überprüfen.

#### Wie funktioniert das MySQL-Protokoll?

Das MySQL-Protokoll funktioniert im Grunde wie das SQL-Protokoll, aber eben mit MySQL-Datenbanken! (Der Standard-Port zur Verbindung mit MySQL-Datenbanken ist 3306.)
