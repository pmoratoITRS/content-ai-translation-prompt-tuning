{
  "hero": {
    "title": "Network Checks"
  },
  "title": "Network Checks",
  "summary": "Externe Network Checks stellen sicher, dass Ihr Netzwerk funktioniert und zugänglich ist. Sie benachrichtigen Sie über Ausfälle.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/network-checks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Uptrends entwickelte seine HTTP(S)-Prüfobjekte, um die Verfügbarkeit und Schnelligkeit deiner Website zu überprüfen. Wenn du jedoch andere nicht webbasierte Netzwerkgeräte von außerhalb der Firewall prüfen möchtest, benötigst du den Netzwerk-Check. Uptrends wird dein Team benachrichtigen, sobald es einen Fehler bei der von dir angegebenen URL oder IP-Adresse bemerkt. Abhängig von der Art des Fehlers wirst du eine Routenverfolgung erhalten, was dir dabei hilft, das Problem zu beheben. Bei den Netzwerk-Checks gibt es zwei Möglichkeiten: Ping oder Connect.

## Ping

Wenn du den Ping Netzwerk-Check wählst, verwenden die Checkpoints von Uptrends ICMP (Internet Control Message Protocol) und senden eine Echo-Anfrage. Uptrends erfasst und meldet Antwortzeiten und gibt Warnmeldungen für alle in der Antwort enthaltenen Fehler.

[SHORTCODE_1]
**Hinweis**: ICMP muss am Gerät aktiviert sein, um unnötige Warnmeldungen zu vermeiden. Geräte ignorieren zudem gelegentlich ICMP-Anfragen, wenn der Netzwerk-Traffic gerade sehr hoch ist.
[SHORTCODE_2]

## Connect

Wählst du **Connect Network Check**, wird Uptrends versuchen, mit dem von dir zugewiesenen Port zu verbinden. Du kannst jede beliebige Port-Nummer angeben. Um beispielsweise eine SSH-Verbindung (Secure Shell) mit einem Linux-Rechner zu errichten, würdest du Port 22 angeben.

## Funktionen

Ping und Connect bieten dir viele Möglichkeiten für dein Monitoring.

### Intervall

Obwohl die Standardeinstellung des Intervalls fünf Minuten ist, kannst du es auf alles von einer Minute bis zu einmal pro Stunde ändern.

[SHORTCODE_3]
**Hinweis**: Dein Überwachungsintervall ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten. [Erfahre mehr]([LINK_URL_1])
[SHORTCODE_4]

### IP-Version

IPv4 war lange der Standard. Die neue Version IPv6 gewinnt jedoch mehr und mehr an Akzeptanz. Die meisten Checkpoints von Uptrends unterstützen IPv6 und wir fügen weitere hinzu.


[SHORTCODE_5]
**Hinweis**: Wir empfehlen, deine Prüfobjekte so einzustellen, dass sie sowohl IPv4 als auch IPv6 überwachen. Die beiden Versionen handhaben das Routing unterschiedlich, sodass Tests bei einer Version eventuell einen Fehler melden, bei der anderen aber nicht.
[SHORTCODE_6]

### Performance

Langsame Verbindungen oder Pings können auf andere Netzwerk- oder Hardware-Probleme hinweisen. Auf der Registerkarte [SHORTCODE_9]Warnbedingungen[SHORTCODE_10] kannst du Performance Limits eingeben und erhältst Meldungen, wenn bei dem Netzwerk Performance-Probleme auftreten.

## Routenverfolgung

Uptrends führt in mehreren Fällen eine Routenverfolgung bzw. ein Traceroute durch:

1.  Im Rahmen eines Tests durch ein Prüfobjekt, wenn das Prüfobjekt ein Problem mit der Verbindung oder dem Netzwerk vermutet. Wenn beispielsweise ein HTTPS-Prüfobjekt versucht, einen Webserver zu erreichen, aber keine TCP-Verbindung mit der IP-Adresse des Servers erstellt werden kann, wird eine Routenverfolgung für weitere Analysen der Verbindung zwischen Uptrends‘ Checkpoint-Standort und deinem Server erstellt.
2.  Wenn du das kostenlose Routenverfolgungstool zur Erstellung einer detaillierten Routenverfolgung bei einem von Uptrends Checkpoint-Servern einsetzt.

Wenn man eine solche Routenverfolgung durchführt, ist die zu erwartende Art Traffic wichtig. Traceroute-Einrichtungen verhalten sich je nach den unterschiedlichen Plattformen: Einige Einrichtungen verwenden UDP-Pakete, andere TCP-Pakete und wieder andere ICMP-Anfragen (Ping). Die Routenverfolgung von Uptrends wird immer auf Windows-Servern ausgeführt und verwendet daher ICMP-Pakete. Daher funktioniert die Ausführung von Traceroutes in deiner Netzwerkumgebung nur, wenn dein Netzwerk ICMP-Pakete akzeptiert. Es gibt keinen TCP- oder UDP-Traffic.

Die Konfiguration eines externen Servers oder Netzwerkgeräts für das Monitoring ist ziemlich einfach und dauert in der Regel lediglich ein oder zwei Minuten. Wichtig ist, dass du deinen Server-Domainnamen oder die IP-Adresse bereitliegen hast!

1. Klicke auf die +-Schaltfläche im Menü unter [SHORTCODE_11] Überwachung > Prüfobjekteinrichtung [SHORTCODE_12].
2. Wähle im Pop-up-Fenster *Wähle einen Prüfobjekttyp aus* zunächst den Prüfobjekttyp *Ping* oder *Connect* und dann klicke auf die Schaltfläche [SHORTCODE_13] Wähle aus [SHORTCODE_14].
   Das neue Prüfobjekt wird erstellt und du siehst die Konfigurationsseite des Prüfobjekts.
3. Gib deinem Prüfobjekt einen **Namen**.
4. Lege das **Überwachungsintervall** fest. Dein [Überwachungsintervall]([LINK_URL_2]) ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.
5. Gib die Serveradresse des zu überwachenden Servers unter **Netzwerk Adresse** im Abschnitt *Details* ein, einschließlich des entsprechenden Domainnamens oder der IP-Adresse.
6.  Sofern du alle Konfigurationen für das neue Prüfobjekt vorgenommen hast, klicke auf [SHORTCODE_15] Speichern [SHORTCODE_16]. Du hast nun ein neues Prüfobjekt für das externe Server-Monitoring hinzugefügt!
      
    [SHORTCODE_7]**Hinweis**: Du kannst auch die weiteren [Einstellungen für das Prüfobjekt]([LINK_URL_3]) in den Registerkarten oben auf der Prüfobjektkonfigurationsseite erkunden.[SHORTCODE_8]


