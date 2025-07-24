{
  "hero": {
    "title": "Browsertypen mit extra Metriken"
  },
  "title": "Browsertypen mit extra Metriken",
  "summary": "Einige Browsertypen bieten mehr Informationen als andere und verfügen über verbesserte Funktionen. Hier erfährst du, welche Informationen dies sind und welche Funktionen sich unterscheiden.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-ergebnisse/extra-metriken-und-funktionen",
  "translationKey": "[URL_1]
  "tableofcontents": true
}

Die folgenden Full Pagecheck- oder Transaktions-[Browsertypen]([LINK_URL_1]) unterstützen einige zusätzlichen Metriken und Funktionen:

- Chrome mit extra Metriken
- Microsoft Edge

Chrome mit extra Metriken unterstützt Core Web Vitals und W3C Navigation Timings beim Transaktions-Monitoring.

## Funktionen

### Native Checks

Für die unterstützten Browsertypen misst der FPC die Performance direkt im Browser. Damit kann der Browser so natürlich wie möglich funktionieren.

### Support von HTTP2, HTTP3, QUIC und Header

Neben dem Protokoll HTTP werden auch die Protokolle HTTP2, HTTP3 und QUIC unterstützt.

Abfragen anhand eines Protokolls wie HTTP2, HTTP3 oder QUIC werden auch andere Header haben als beim HTTP-Protokoll. Es gibt keine X-Uptrends-Header wie X-Uptrends-PortInfo und X-Blocked-By-Uptrends.

### Inhaltsprüfung

Es wird nur das Endergebnis für die Inhaltsüberprüfung berücksichtigt. Inhalt, der während einer Weiterleitung angezeigt wird, löst keinen Übereinstimmungsabgleich aus.

### Blockieren von URLs

Beim Navigieren zu einer Website wird diese Navigation erfolgreich sein, selbst wenn die URL der Website in der Liste blockierter URLs aufgeführt ist. Ein FPC, der einen Browsertyp mit extra Metriken nutzt, blockiert nicht die Navigation. Andere Elemente, auf die die Website verweist, zum Beispiel Bilder, werden jedoch blockiert.

### Im Cache gespeicherte Objekte

Da Uptrends die Performance-Daten aus dem Browser extrahiert, können gecachte Objekte angezeigt werden. Sie können nach Wunsch gefiltert werden.

### DNS Bypass

Du kannst einen DNS Bypass hinzufügen. Ein Full Pagecheck lädt deine Seite und jedes Objekt mit einem tatsächlichen Browser und zeigt schließlich eine Wasserfallgrafik an, anhand derer du diese Objekte untersuchen kannst. Der [DNS Bypass]([LINK_URL_2]) stellt sicher, dass die Webseite zu einem Domainnamen oder eine IP-Adresse aufgelöst wird, die du angegeben hast. Diese DNS-Vorgabe ist auch für Transaktionen verfügbar.

## Messwerte

### Messmethoden

Die Ergebnisse (Ladezeiten und Gesamt-Bytes) bei einem Browsertyp mit extra Metriken unterscheiden sich von anderen Browsertypen.

Der FPC (Browsertypen mit extra Metriken) unterstützt neue Protokolle wie HTTP2 und HTTP3 und ist direkter in den Browser integriert. Daher kann das erzeugte Wasserfalldiagramm sich von dem eines FPC mit anderem Browsertyp unterscheiden. Du wirst mehr gleichzeitige Anfragen sehen, die schneller übertragen werden. Die Messung kann schneller oder langsamer erfolgen, sodass die Gesamt-Bytes sich ebenfalls unterscheiden können. Der Grund liegt darin, dass Uptrends eine unterschiedliche Zahl an Hintergrundaktivitäten erfasst, nachdem die Seite geladen wurde. Das kann ein ladendes Video oder JavaScript Service Worker sein, der Aufgaben im Hintergrund ausführt.

### Core Web Vitals 

Core Web Vitals sind eine Reihe von Standard-Messwerten von Google, die eingesetzt werden, um mehr über die Leistung (Performance) deiner Website zu erfahren. Uptrends misst und berichtet diese Messwerte in den Prüfergebnissen. Du kannst die Ergebnisse in einem Dashboard anzeigen, indem du eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]([LINK_URL_3]) hinzufügst und aus der Liste Core Web Vitals auswählst.

Diese Messungen können sich von den Messungen des Lighthouse-Tools unterscheiden.
Das von Google bereitgestellte Lighthouse-Tool setzt andere Messmethoden ein als Uptrends. Wir führen einen Browser aus, der eine Website besucht – genauso wie es ein normaler Nutzer machen würde. Das Lighthouse-Tool führt erst ein Warm-up aus und besucht die Website dann mehrere Male, um einen Durchschnittswert zu bestimmen. Das Lighthouse-Tool löst auch nicht bestimmte Nutzereingabeprüfungen aus, wie das bei unserer Messmethode und regulären Nutzern der Fall ist. Es simuliert zudem eine langsamere Verbindung anhand von Bandbreiten-Drosselung. Daher können die von Lighthouse berichteten Core Web Vitals sich von den Messungen von Uptrends unterscheiden.

Im Artikel zu den [Core Web Vitals]([LINK_URL_4]) findest du alle Infos zu diesen Messungen.

### W3C-Metriken

Das World Wide Web Consortium (W3C) hat eine Reihe von Navigationsmesszeiten definiert, die für das Laden einer Webseite von Bedeutung sind. Uptrends hat einige dieser Messwerte übernommen und zeigt sie in den Berichten. Du kannst die Ergebnisse in einem Dashboard anzeigen, indem du eine benutzerdefinierte Kachel des Typs [Einfache Daten Liste/Diagramm]([LINK_URL_5]) hinzufügst und aus der Liste Daten der W3C Navigation Timings auswählst.

Der Knowledge-Base-Artikel [W3C Navigation Timings]([LINK_URL_6]) bietet Einzelheiten zu den von Uptrends implementierten Navigation Timings.

[Core Web Vitals]([LINK_URL_7]) und W3C Navigation Timings sind auch für deine [Transaktionen]([LINK_URL_8]) verfügbar. Um diese Extra-Metriken für das Transaktions-Monitoring zu aktivieren, wähle **Chrome mit extra Metriken** aus dem Drop-down-Menü bei *Browsertyp* auf der Registerkarte [SHORTCODE_1] Erweitert [SHORTCODE_2] der Prüfobjekteinstellungen. Du findest die zusätzlichen Messwerte beim [Transaktionswasserfall]([LINK_URL_9]) bei den Schritten, für die das Wasserfalldiagramm aktiviert wurde. (Nur für [Accounts auf Business- und Enterprise-Stufe]([LINK_URL_10]) verfügbar.)

### Ladezeit: W3C Gesamtzeit oder Netzwerk-Gesamtzeit? [ANCHOR_1]

Ein Full Pagecheck oder Transaktionsprüfobjekt mit dem Browsertyp *mit extra Metriken* stellt die Möglichkeit bereit, die Gesamtzeit als *W3C Load Event* oder die *Netzwerkzeit* zu messen.

#### W3C Gesamtzeit

Bei der Wahl der W3C Gesamtzeit als Messung, wird die W3C Load Event End-Metrik verwendet. Das W3C Load Event wird hier näher beschrieben: [URL_2]

In der Uptrends App wird diese Metrik nicht ausgerechnet, sondern stammt direkt vom Browser, genauer gesagt von den Entwicklertools des Browsers.

Du findest die Ergebnisse der Messung in den Kontrolldetails des Prüfobjekts unter *Load Event* im Bereich *W3C Navigation Timing*-Metriken.

![Screenshot W3C Navigation Timing Load Event hervorgehoben]([LINK_URL_11])

#### Netzwerkzeit

Die Netzwerkzeit wird gemessen, indem auf eine Leerlaufzeit bei der Netzwerkaktivität gewartet wird.

#### Die Ladezeitbasis für ein Prüfobjekt einrichten

Triff deine Wahl auf der Registerkarte [SHORTCODE_3] Erweitert [SHORTCODE_4] bei den Prüfobjekteinstellungen. Wähle eine der Optionen im Abschnitt *Messung* für *Basiere Ladezeit auf*:

![Screenshot Gesamtzeitmessung]([LINK_URL_12])

#### Metrikunterschiede und Vorschläge für die Wahl der Einstellung

Das Messen der Ladezeit als W3C Ladezeit oder als Netzwerkzeit kann zu erheblichen unterschieden führen.
Die Ergebnisse (und Unterschiede) hängen von dem ab, was überwacht wird, z. B. ändern sich bei einer Transaktion, bei der das W3C Load Event verwendet wird, die Ladezeiten einzelner Schritte, wenn eine andere Methode genutzt wird. Dann ändert sich auch die Gesamtzeit.

Bei einem Full Pagecheck-Prüfobjekt werden eventuell mehr als eine Navigationsaktion verzeichnet, z. B. wenn Weiterleitungen eingerichtet wurden. Die Metriken werden für jede Navigation aufgezeichnet und für die komplette Metrik *W3C Load Event* zusammengefasst.

Bei einem Transaktionsprüfobjekt gibt es mehrere Navigationen innerhalb eines Schritts, d. h., mehrere Navigationsaktionen oder eine Navigation, die andere Navigationen auslöst. Die Ladezeiten werden pro Schritt zusammengefasst und schließlich für die gesamte Transaktion in der Metrik *Gesamtzeit* addiert.
Ausnahme: Wenn in einem Schritt keine Navigation, aber beispielsweise eine Inhaltsprüfung vorhanden ist, lautet die Zeit für diesen Schritt 0 (anders als bei der Nutzung der *Netzwerkzeit*). In diesem Fall ist die Netzwerkzeit nicht die Leerlaufzeit der Netzwerkaktivität, sondern wird von der Ausführungszeit der Schritte abgeleitet.

Einige Hinweise zur Wahl der optimalen Methode für Transaktionen:

- Wenn du wissen möchtest, wie schnell die Seite lädt – mit anderen Worten, du bist nur an das Laden interessiert –, empfiehlt sich die W3C Ladezeit.
- Möchtest du mehr über das Endnutzer-Erlebnis erfahren, zum Beispiel wie lange es dauert, bis ein Nutzer die gesamte Transaktion ausgeführt hat, ist die Netzwerkzeit empfohlen. Der Grund besteht darin, dass alles berücksichtigt wird, auch Schritte, die keine Navigation sind, aber sich trotzdem auf die Zeit auswirken, die der Nutzer benötigt, um die Transaktion abzuschließen.

### Timeline Screenshots

Der [Zeitstrahl mit Screenshots (a.k.a. Filmstrip)]([LINK_URL_13]) enthält mehrere Screenshots, die während des Ladens der überwachten Webseite aufgenommen werden. Der Zeitstrahl wird über dem Wasserfallbericht in den Kontrolldetails des Prüfobjekts angezeigt.

![Screenshot Filmstrip bei Kontrolldetails]([LINK_URL_14])

### Daten-URLs im Wasserfalldiagramm

Elemente, die im HTML-Dokument eingebettet sind, beispielsweise Daten-URLs, oder solche, die aus JavaScript stammen, wie etwa Blob URLs, werden ebenfalls im Wasserfalldiagramm angezeigt. Du kannst bei Bedarf einen Filter anwenden.

### TLS-Informationen

Im Wasserfallbericht der Kontrolldetails des Prüfobjekts findest du TLS-Informationen zu jedem Objekt.
Öffne die Details im Wasserfalldiagramm, indem du auf das Plus-Zeichen neben dem Element klickst:

![Screenshot TLS-Info in Wasserfall]([LINK_URL_15])



