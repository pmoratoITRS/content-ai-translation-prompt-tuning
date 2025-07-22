{
  "hero": {
    "title": "Vorbehalte, Tipps und Tricks"
  },
  "title": "Vorbehalte, Tipps und Tricks",
  "summary": "Bei der Einrichtung eines Transaktionsprüfobjekts solltest du einige Dinge berücksichtigen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/transaktions-monitoring-vorbehalte-tipps-und-tricks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Transaktions-Monitoring (Web Application Monitoring) kann den Ruf und die Gewinne einer Marke retten, indem Probleme bei Transaktionen aufgedeckt werden, bevor sie sich auf die Nutzer auswirken. Das Transaktions-Monitoring ist ein synthetischer Monitoring-Ansatz, bei dem Uptrends' Checkpoints einem Skript folgen, um den Weg eines echten Nutzers zu simulieren. Bei der Einrichtung eines User-Journey-Tests ist es wichtig, die kurz- und langfristigen Konsequenzen des Testens zu berücksichtigen. Viele Probleme lassen sich vermeiden, indem die Transaktion vor der Aufzeichnung sorgfältig kartiert wird. Alle Fälle unterscheiden sich und wir haben einige häufige Probleme gesammelt, die bei der Einrichtung eines Transaktions-Monitorings berücksichtigt werden sollten.

## Bestandsengpässe vermeiden

Bestandsengpässe aufgrund des Testens von Einkaufs- und Bezahlvorgängen können Probleme verursachen. Beim Synthetic Monitoring werden mit den Tests bis zu 288 Bestellungen pro Tag aufgegeben. Wenn dies nicht richtig gehandhabt wird, kann das Testen deinen Bestand künstlich verringern und dieser für tatsächliche Käufer als „nicht verfügbar“ erscheinen. Es ist schon vorgekommen, dass ein Lager die Bestellung verarbeitet und zum Versand bereitgestellt hat.  Es gibt mehrere unterschiedliche Lösungen, Bestandsprobleme zu vermeiden.

**Die Datenbanklösung**

Obwohl einige Unternehmen sich dazu entschieden haben, Testkäufe und Einkaufskörbe manuell aus ihrer Datenbank zu löschen, kann eine hinterlegte Lösung oder ein automatisierter Prozess zuverlässiger sein. Zum Beispiel könnte das System zur Bestellverarbeitung Bestellungen vom Testanwender oder Bestellungen von Uptrends’ [Checkpoint-IP-Adressen]([LINK_URL_1]) ignorieren.

**Verwendung von (virtuellen) Testartikeln**

Es kann von Vorteil sein, einen Artikel im Bestand einzurichten, der ausschließlich für Testzwecke genutzt wird. Durch den Einsatz eines Testartikels bleiben die Bestände genau und verfügbar. Testartikel helfen zudem, bei einer Säuberung der Datenbank Testtransaktionen zu identifizieren, und sorgen dafür, dass nicht aus Versehen tatsächlich vorhandene Artikel versendet werden.

**Einkaufskörbe leeren**

Beim Testen von Einkaufsvorgängen kannst du die Entfernung des Artikels als Transaktionsschritt einarbeiten. Füge einen Artikel hinzu und lösche ihn, bevor die Transaktion abgeschlossen wird.

[SHORTCODE_1]
**Hinweis**: Das Entfernen von Artikeln aus dem Einkaufskorb kann gewährleisten, dass die Bestände für echte Kunden verfügbar bleiben. Wenn die Transaktion jedoch einen Fehler aufweist, bevor das Skript die Artikel aus dem Einkaufskorb entfernen kann, können sich diese trotzdem ansammeln. Überwache den Einkaufskorb des Testnutzers häufig, um Artikel zu löschen.
[SHORTCODE_2]

**Wähle einen Artikel mit großem Bestand**

Wenn du einen tatsächlichen Artikel wählst, wähle einen für den Test, bei dem große Mengen vorhanden sind, sodass ein Bestandsengpass nahezu unmöglich ist.

## Nachschubsysteme im Blick behalten

Bestandsmanagementsoftware verfügt häufig über Prozesse, durch die beliebte Artikel oder Artikel mit geringem Bestand nachbestellt werden. Sprich mit deinen Systemadministratoren, um ein Überfüllen des Artikels im Bestand zu vermeiden. Mögliche Maßnahmen könnten Einrichten eines Testartikels oder Abschalten des automatischen Wiederauffüllens des Artikels sein.

## Vermeidung, Daten für Termine oder Reservierungen auszubuchen

Wenn dein Transaktions-Monitoring die Terminvergabe für Ärzte, Hotelzimmer, Flüge oder Restaurants prüft, können schnell alle Zeitfenster ausgebucht sein. Die Identifizierung von Terminvergaben durch Tests und ihr Löschen ist entscheidend.

## Dein Transaktionsprüfobjekt WIRD das Senden von E-Mails auslösen

Enthält ein Teil deiner Transaktion ein E-Mail-Feld und die Transaktion sendet aus irgendeinem Grund wie etwa Rechnungen, Passwort-Zurücksetzungen oder Erinnerungen für Nutzer-IDs Bestätigungs-E-Mails, wird dein Transaktionsprüfobjekt ebenfalls E-Mails erzeugen. Um zu verhindern, dass das Postfach mit unerwünschten E-Mails gefüllt wird, nutze für das Transaktionsprüfobjekt eine E-Mail-Adresse wie noreply@mysite.com.

## Unerwartete Kreditkartenbelastungen

Wenn du eine echte Kreditkarte zum Testen der Einkaufsvorgänge einsetzt, kann das zu Kosten und Händlergebühren führen, verfügbares Guthaben sperren und Betrugsalarme aufgrund häufiger Transaktionen auslösen. Verwende stattdessen Testkreditkartenkonten. Die meisten Händlerservices bieten Testkontonummern, mit denen du den Bezahlvorgang ohne Gebührenerhebung oder Sperrung eines echten Kontos testen kannst.

## Lösungen zur Erstellung eines neuen Kontos

Beim Testen der Einrichtung eines neuen Kontos kannst du nur einmal den gleichen Nutzernamen wählen. Wird das Skript für die Transaktion ein zweites Mal ausgeführt, wird wegen eines doppelten Kontos eine Fehlermeldung erzeugt. Wir haben hier einige Lösungen für das Testen einer Kontoeinrichtung gesammelt.

### Die Daten nicht speichern

Obwohl diese Möglichkeit dazu führt, dass die Kontoeinrichtung nicht vollständig getestet wurde, haben sich einige Uptrends Nutzer dazu entschieden, kurz vor der Speicherung abzubrechen. Das Prüfobjekt testet jeden Aspekt der Kontoeinrichtung, außer das abschließende Senden.

### Datenbanklösungen

Du kannst einen Datenbank-Trigger zur Prüfung nach einer Testkonto-ID nach einem ERSTELLUNGSvorgang einsetzen, der das Testkonto aus der Datenbank löscht, bevor der nächste Test eingeleitet wird.

### Neue einzigartige Logins erzeugen

Du kannst auch neue einzigartige Logins erzeugen, indem du Elemente wie einen Datumsstempel nutzt. Du musst sie nur regelmäßig löschen. [Wende dich an den Support]([LINK_URL_2]), um mehr zu erfahren.

## Konto ist bereits angemeldet

Wenn du dieselben Anmeldedaten für mehrere Prüfobjekte nutzt oder das Skript sich nach dem letzten Test nicht abmeldet, kann dies zu Fehlermeldungen führen. Best Practice ist die Einrichtung eines anderen Testkontos für jedes Prüfobjekt und sich immer als letzten Schritt des Testprozesses abzumelden, um unnötige Warnmeldungen zu vermeiden.

## Sensible Daten schützen

Wenn ein Nutzer sich anmelden muss, um einen Vorgang auszuführen, muss das Prüfobjekt sich ebenfalls anmelden. Sieh dir den Authentifizierungsablauf an und betrachte das Schützen der Anmeldedaten. Du kannst die Authentifizierungsdaten mithilfe unserer [Vault]([LINK_URL_3]) schützen und in den Testergebnissen verbergen.

Bedenke auch die Berechtigungen, die du einem Test-Nutzer gewährst, vom Standpunkt der Sicherheit. Behalte den Nutzer im Auge, um sicherzugehen, dass es keine ominösen Aktivitäten gibt.

## Inhaltsprüfungen nutzen

[Inhaltsprüfungen]([LINK_URL_4]) sind kostenlos und du kannst sie zu jedem Schritt deiner Transaktion hinzufügen. Inhaltsprüfungen sind eine großartige Möglichkeit, sicherzustellen, dass eine Seite vollständig geladen wurde und dass der Browser den richtigen Inhalt erhalten hat. Du kannst Inhaltsprüfungen auf drei unterschiedlichen Wegen hinzufügen: über die Schaltfläche *Inhaltsprüfung hinzufügen* oder über das Kontextmenü. Du kannst Inhaltsprüfungen später auch mithilfe des Prüfobjekt-Schritte-Editors in deinem Account hinzufügen. Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]([LINK_URL_5]) an, um zu erfahren, wie Inhaltsprüfungen in tatsächlichen Szenarien funktionieren.

## Tastaturaktionen nutzen
Der Transaktionsrekorder ermöglicht dir auch, Tastatureingaben der Nutzer zu erfassen. Du kannst verschieden Zeichen wählen, darunter Steuerungstasten, Spezialtasten, Zifferntasten, Nummernblocktasten, Groß- und Kleinbuchstaben. Wähle, ob die Taste allgemein oder nur auf das letzte Element im Fokus oder auf das letzte geklickte Element gedrückt werden soll.

Das ist nützlich, wenn es eine Website mit der Anweisung *Irgendeine Taste drücken, um fortzufahren* oder *Die Eingabetaste drücken, um zu bestätigen* ist. Beachte, dass du im Gegensatz zu Mausklickaktionen (bei denen eine Bewegung automatisch aufgezeichnet wird) manuell eine Tastaturaktion hinzufügen musst, um ein Tastaturereignis als Aktivität aufzuzeichnen. Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]([LINK_URL_6]) an, um mehr über Tastaturaktionen zu erfahren.

## Die Aktionen „Hover“ und Warten, bis Element sichtbar ist“ verwenden

Du kannst auch Aktionen aufzeichnen, bei denen die Maus auf ein Element zeigt, und verifizieren, ob ein Element sichtbar ist, wenn du auf ein Element der Seite mit der rechten Maustaste klickst und die entsprechende Option im Kontextmenü des *ITRS Uptrends Transaction Recorders* wählst. Das ist nützlich, wenn du prüfen möchtest, ob ein Element über bestimmte Hover-Trigger wie Anzeigen einer Nachricht oder späteres Sichtbarmachen eines Elements oder eines Untermenüs verfügt. Siehe dir das [Step-by-Step-Tutorial für Shop-Funktionen]([LINK_URL_7]) an, um Beispiele zu sehen.

[SHORTCODE_3]
**Hinweis**: Jeder Fall ist anders. Zögere nicht, dich an unsere Skriptentwickler zu wenden, um eine Lösung zu finden, die zu deinem einzigartigen Fall passt. Verwende das [Ticket-System]([LINK_URL_8]) oder füge bei deiner Einreichung einer Transaktionsaufzeichnung einen Hinweis hinzu, mit dem du unsere Entwickler auf deine Bedenken aufmerksam machst.
[SHORTCODE_4]