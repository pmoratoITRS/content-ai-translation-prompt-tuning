{
  "hero": {
    "title": "DNS Bypass"
  },
  "title": "DNS Bypass",
  "summary": "Verstehe und erfahre, ob und wie du einen DNS Bypass für ein Transaktions- oder Full Pagecheck-Prüfobjekt einrichten solltest. Dieser Bypass kann bei Auswahl des Browsertyps „Chrome mit extra Metriken“ hinzugefügt werden. Der DNS Bypass wird sicherstellen, dass die Webseite auf einen bestimmten Domainnamen oder eine bestimmte IP-Adresse aufgelöst wird.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/dns-bypass",
  "translationKey": "[URL_1]
}

Der DNS Bypass stellt sicher, dass die Webseite auf einen bestimmten Domainnamen oder eine bestimmte IP-Adresse aufgelöst wird.

Die Funktion kannst du nutzen, um einen bestimmten Standort der Website zu prüfen und zu überwachen, wenn die Website zum Beispiel Teil eines Content Delivery Network (CDN), einer Load-Balancing-Lösung oder eines der folgenden [DNS Bypass-Szenarien]([LINK_URL_1]) ist.

## Welche Prüfobjekte verwenden den DNS Bypass?

Der Uptrends DNS Bypass wird in den Prüfobjekten [Full Pagecheck]([LINK_URL_2]) und [Transaktion]([LINK_URL_3]) implementiert. Er ist nur für den Browsertyp _Chrome mit extra Metriken_ verfügbar.

Für andere Prüfobjekttypen wie etwa HTTPS kannst du Host-Header nutzen. Mit unserem Knowledge-Base-Artikel [Monitoring von Websites auf anderen Servern (nicht dem Produktionsserver)]([LINK_URL_4]) erfährst du mehr zu dieser ähnlichen Funktion.

## Weshalb einen DNS Bypass einsetzen? 
Wenn Uptrends für einen Full Pagecheck oder eine Transaktion eine URL in einem Browser lädt, fordert der Browser einen DNS-Service auf einem externen Server auf, den angefragten Domainnamen in eine IP-Adresse aufzulösen. Er benötigt diese Adresse für die tatsächliche HTTP-Anfrage. Ein FPC imitiert exakt, was der Browser eines Endnutzers normalerweise macht.

Das reicht aber für Monitoring- oder Testzwecke eventuell nicht aus. Zum Beispiel, wenn du zwar die URL deines Unternehmens nutzen, aber einen bestimmten Server oder eine bestimmte IP-Adresse ansprechen möchtest, statt dich auf das reguläre DNS zu stützen.

Mit dem DNS Bypass kannst du genau das einrichten. Du kannst eine feststehende IP-Adresse (oder einen anderen CNAME Domainnamen) festlegen, die verwendet werden soll, wenn der Browser mit einem bestimmten Domainnamen verbindet. Im Wesentlichen umgeht oder überschreibt dies das reguläre DNS-System. Es ist eine ähnliche Arbeitsweise wie mit der _Hostdatei_ auf Windows oder Linux.
## Hinzufügen eines DNS Bypass

1.  Gehe für ein Full Pagecheck-Prüfobjekt zu [SHORTCODE_3]Überwachung > Prüfobjekteinrichtung [SHORTCODE_4].
2.  Klicke auf den Namen des Prüfobjekts, um die Prüfobjekteinstellungen aufzurufen.
3.  Stelle sicher, dass der _Browsertyp_ Chrome mit extra Metriken ausgewählt ist.
4.  Öffne die Registerkarte [SHORTCODE_5] Erweitert [SHORTCODE_6].
![]([LINK_URL_5])
5.  Klicke unter _Verbindung_ auf [SHORTCODE_7] DNS Bypass hinzufügen [SHORTCODE_8].
6.  Gib _Source Domain_ und _Ziel Domain_ ein (bitte beachte, dass aus Sicherheitsgründen nicht alle Zieldomains unterstützt werden).
7.  Klicke auf die [SHORTCODE_9]Speichern[SHORTCODE_10]-Schaltfläche, bevor du die Seite verlässt.

 [SHORTCODE_1]
**Hinweis**: Du kannst Platzhalter für den Namen im Feld _Source_ Domain einsetzen, aber nicht für die Zieldomain. Beispielsweise kannst du eine Regel *acc.example.com nach www.example.com erstellen, die Anfragen an server1-acc.example.com an www.example.com umleitet.
[SHORTCODE_2]

## Einsatzbereich des DNS Bypass  [ANCHOR_1]
Wann solltest du den standardmäßig genutzten DNS Server umgehen? Hier zeigen wir einige Szenarien, wann dies nützlich oder notwendig sein könnte:
### DTAP / User Acceptance Testing (UAT) Server
Du möchtest die Performance von Webseiten in einer DTAP-Umgebung (development, testing, acceptance and production) oder auf einem User Acceptance Testing (UAT) Server testen und überwachen. Diese Seiten geben dir eine tatsächliche Sicht darauf, wie sie in der Produktion angezeigt werden, und erfordern daher eventuell ein Monitoring. Mit einem DNS Bypass sagst du dem Prüfobjekt von Uptrends, dass es am gewünschten Standort prüfen und überwachen soll.
### Unterschiedliche SSL-Konfiguration
Nehmen wir an, deine Testumgebung muss dieselben SSL-Zertifikate nutzen wie deine Produktionsumgebung. Die Webserver-Adresse für die Zertifikatsprüfung muss identisch mit der im Zertifikat angegebenen Adresse sein, andernfalls verzeichnet der Full Pagecheck einen Fehler.
### Preproduction-Website auf einer externen Domain
Zum Beispiel wird deine Website von einem externen Unternehmen neudesignt. Du möchtest die neuen Webseiten an ihrem derzeitigen Standort auf dem Server des Webentwicklers testen und überwachen.
### Webseite auf einem Knoten in einem Web Cluster
Verwende einen DNS Bypass, wenn du sicherstellen möchtest, dass jeder einzelne Knoten des Clusters richtig funktioniert und überwache sie separat.
### Webseite auf einer CDN Origin-Maschine
Nehmen wir an, deine Website befindet sich in einem Content Delivery Network (CDN). Du möchtest die Website auf dem Origin-Server testen und überwachen, nicht die gecachten Seiten auf den CDN Edge-Servern. Konfiguriere einen DNS Bypass, sodass Uptrends direkt bei dem Origin-Server prüft.
### Webseite an einem bestimmten CDN-Standort 
Wenn deine Website sich in einem Content Delivery Network (CDN) befindet, kann es sein, dass du eine der Webseiten-Instanzen überwachen möchtest, die auf einem der Edge-Server im Bereitstellungsnetzwerk gecacht ist. Wenn du einen DNS Bypass konfigurierst, prüft Uptrends direkt bei diesem Server. Um diese Standorte zu überwachen, gibt es jedoch eine geeignetere Methode: Richte ein (FPC) Prüfobjekt ein und lasse es die Prüfungen von [Checkpoints]([LINK_URL_6]) in der entsprechenden Region ausführen.
### Webseite oder Website innerhalb eines internen Netzwerks
Wenn du private Checkpoints innerhalb deines Netzwerks nutzt, könnte ein FPC eine interne Netzwerkroute nutzen, wodurch die Adresse der Seite durch den internen Server aufgelöst wird. Wenn du lieber von außerhalb deines Netzwerks testen möchtest, kannst du einen DNS Bypass nutzen, um die Netzwerkroute zu ändern. Dies kann eine Rolle spielen, wenn es unterschiedliche Seiten und Möglichkeiten gibt, sich intern und extern anzumelden.
