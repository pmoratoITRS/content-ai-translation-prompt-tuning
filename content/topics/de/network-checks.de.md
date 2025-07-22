{
  "hero": {
    "title": "Network Checks"
  },
  "title": "Network Checks",
  "summary": "Externe Network Checks stellen sicher, dass Ihr Netzwerk funktioniert und zugänglich ist. Sie benachrichtigen Sie über Ausfälle.",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/network-checks",
  "translationKey": "https://www.uptrends.com/support/kb/network-checks",
  "tableofcontents": true
}

Uptrends entwickelte seine HTTP(S)-Prüfobjekte, um die Verfügbarkeit und Schnelligkeit deiner Website zu überprüfen. Wenn du jedoch andere nicht webbasierte Netzwerkgeräte von außerhalb der Firewall prüfen möchtest, benötigst du den Netzwerk-Check. Uptrends wird dein Team benachrichtigen, sobald es einen Fehler bei der von dir angegebenen URL oder IP-Adresse bemerkt. Abhängig von der Art des Fehlers wirst du eine Routenverfolgung erhalten, was dir dabei hilft, das Problem zu beheben. Bei den Netzwerk-Checks gibt es zwei Möglichkeiten: Ping oder Connect.

## Ping

Wenn du den Ping Netzwerk-Check wählst, verwenden die Checkpoints von Uptrends ICMP (Internet Control Message Protocol) und senden eine Echo-Anfrage. Uptrends erfasst und meldet Antwortzeiten und gibt Warnmeldungen für alle in der Antwort enthaltenen Fehler.

{{< callout >}}
**Hinweis**: ICMP muss am Gerät aktiviert sein, um unnötige Warnmeldungen zu vermeiden. Geräte ignorieren zudem gelegentlich ICMP-Anfragen, wenn der Netzwerk-Traffic gerade sehr hoch ist.
{{< /callout >}}

## Connect

Wählst du **Connect Network Check**, wird Uptrends versuchen, mit dem von dir zugewiesenen Port zu verbinden. Du kannst jede beliebige Port-Nummer angeben. Um beispielsweise eine SSH-Verbindung (Secure Shell) mit einem Linux-Rechner zu errichten, würdest du Port 22 angeben.

## Funktionen

Ping und Connect bieten dir viele Möglichkeiten für dein Monitoring.

### Intervall

Obwohl die Standardeinstellung des Intervalls fünf Minuten ist, kannst du es auf alles von einer Minute bis zu einmal pro Stunde ändern.

{{< callout >}}
**Hinweis**: Dein Überwachungsintervall ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten. [Erfahre mehr]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}})
{{< /callout >}}

### IP-Version

IPv4 war lange der Standard. Die neue Version IPv6 gewinnt jedoch mehr und mehr an Akzeptanz. Die meisten Checkpoints von Uptrends unterstützen IPv6 und wir fügen weitere hinzu.


{{< callout >}}
**Hinweis**: Wir empfehlen, deine Prüfobjekte so einzustellen, dass sie sowohl IPv4 als auch IPv6 überwachen. Die beiden Versionen handhaben das Routing unterschiedlich, sodass Tests bei einer Version eventuell einen Fehler melden, bei der anderen aber nicht.
{{< /callout >}}

### Performance

Langsame Verbindungen oder Pings können auf andere Netzwerk- oder Hardware-Probleme hinweisen. Auf der Registerkarte {{< AppElement type="tab" >}}Warnbedingungen{{< /AppElement >}} kannst du Performance Limits eingeben und erhältst Meldungen, wenn bei dem Netzwerk Performance-Probleme auftreten.

## Routenverfolgung

Uptrends führt in mehreren Fällen eine Routenverfolgung bzw. ein Traceroute durch:

1.  Im Rahmen eines Tests durch ein Prüfobjekt, wenn das Prüfobjekt ein Problem mit der Verbindung oder dem Netzwerk vermutet. Wenn beispielsweise ein HTTPS-Prüfobjekt versucht, einen Webserver zu erreichen, aber keine TCP-Verbindung mit der IP-Adresse des Servers erstellt werden kann, wird eine Routenverfolgung für weitere Analysen der Verbindung zwischen Uptrends‘ Checkpoint-Standort und deinem Server erstellt.
2.  Wenn du das kostenlose Routenverfolgungstool zur Erstellung einer detaillierten Routenverfolgung bei einem von Uptrends Checkpoint-Servern einsetzt.

Wenn man eine solche Routenverfolgung durchführt, ist die zu erwartende Art Traffic wichtig. Traceroute-Einrichtungen verhalten sich je nach den unterschiedlichen Plattformen: Einige Einrichtungen verwenden UDP-Pakete, andere TCP-Pakete und wieder andere ICMP-Anfragen (Ping). Die Routenverfolgung von Uptrends wird immer auf Windows-Servern ausgeführt und verwendet daher ICMP-Pakete. Daher funktioniert die Ausführung von Traceroutes in deiner Netzwerkumgebung nur, wenn dein Netzwerk ICMP-Pakete akzeptiert. Es gibt keinen TCP- oder UDP-Traffic.

Die Konfiguration eines externen Servers oder Netzwerkgeräts für das Monitoring ist ziemlich einfach und dauert in der Regel lediglich ein oder zwei Minuten. Wichtig ist, dass du deinen Server-Domainnamen oder die IP-Adresse bereitliegen hast!

1. Klicke auf die +-Schaltfläche im Menü unter {{< AppElement type="menuitem" >}} Überwachung > Prüfobjekteinrichtung {{< /AppElement >}}.
2. Wähle im Pop-up-Fenster *Wähle einen Prüfobjekttyp aus* zunächst den Prüfobjekttyp *Ping* oder *Connect* und dann klicke auf die Schaltfläche {{< AppElement type="button" >}} Wähle aus {{< /AppElement >}}.
   Das neue Prüfobjekt wird erstellt und du siehst die Konfigurationsseite des Prüfobjekts.
3. Gib deinem Prüfobjekt einen **Namen**.
4. Lege das **Überwachungsintervall** fest. Dein [Überwachungsintervall]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}}) ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.
5. Gib die Serveradresse des zu überwachenden Servers unter **Netzwerk Adresse** im Abschnitt *Details* ein, einschließlich des entsprechenden Domainnamens oder der IP-Adresse.
6.  Sofern du alle Konfigurationen für das neue Prüfobjekt vorgenommen hast, klicke auf {{< AppElement type="savebutton" >}} Speichern {{< /AppElement >}}. Du hast nun ein neues Prüfobjekt für das externe Server-Monitoring hinzugefügt!
      
    {{< callout >}}**Hinweis**: Du kannst auch die weiteren [Einstellungen für das Prüfobjekt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="de" >}}) in den Registerkarten oben auf der Prüfobjektkonfigurationsseite erkunden.{{< /callout >}}


