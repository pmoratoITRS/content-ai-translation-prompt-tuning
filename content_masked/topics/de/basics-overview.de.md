{
  "hero": {
    "title": "Grundlagenübersicht"
  },
  "title": "Grundlagenübersicht",
  "summary": "Ist Uptrends komplett neu für dich? Lies diese Artikel, um eine Einführung und ein grundlegendes Verständnis dessen zu erhalten, wie die Uptrends Anwendung dir nutzen kann.",
  "url": "[URL_BASE_TOPICS]basics/grundlagenuebersicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Uptrends ist ein SaaS (Software as a Service) Digital Experience Monitoring Tool, das seinen Nutzern detaillierte Einsichten in die Verfügbarkeit und Performance ihrer Websites und -services aus der Endnutzer-Perspektive bietet. Uptrends lässt sich einfach konfigurieren und unterstützt eine große Breite an [Monitoring-Typen]([LINK_URL_1]) für jedes Überwachungsszenario sowie auch das [Real User Monitoring (RUM)]([LINK_URL_2]).

## Synthetic Monitoring

Beim proaktiven [Synthetic Monitoring]([LINK_URL_3]) nutzt Uptrends sein weltweites [Netzwerk an Checkpoints]([LINK_URL_4]), um deine Websites und Prozesse rund um die Uhr auf Verfügbarkeit und Performance zu prüfen – von Standorten, die für dein Unternehmen von Bedeutung sind. Verschiedene Prüfobjekttypen bilden jeden deiner möglichen Einsatzfälle ab.

{{[HTML_TAG_1]}}

### Uptime Monitoring [ANCHOR_1]

[Uptime Monitoring]([LINK_URL_5]) ist ein Hoch-Frequenz-Monitoring der Verfügbarkeit deiner Websites und -services. Prüfobjekte wie der [HTTPS-Prüfobjekttyp]([LINK_URL_6]) prüfen deine Website auf Verfügbarkeit und richtiges Funktionieren, so häufig wie jede Minute und von überall auf der Welt.

![Ein Protokoll eines Basic-Prüfobjekts]([LINK_URL_7])

Es gibt weitere Basic-Prüfobjekttypen wie das [DNS-Prüfobjekt]([LINK_URL_8]), bei dem die Korrektheit deiner DNS-Einrichtung geprüft wird, in dem eine Anfrage an einen DNS-Server gesendet wird, und das [Prüfobjekt für SSL-Zertifikate]([LINK_URL_9]), um die Gültigkeit deiner SSL-Zertifikate zu bestätigen und Warnmeldungen zu senden, wenn sie nicht mehr korrekt sind oder demnächst ablaufen.

### Browser Monitoring [ANCHOR_2]

Anders als beim Uptime Monitoring wird beim [Browser Monitoring]([LINK_URL_10]) ein tatsächlicher Browser verwendet, um deine Websites aufzurufen. Auf diese Weise kann der Prüfobjekttyp Full Pagecheck (FPC) deine Seite vollständig laden, genauso wie es die Endnutzer machen, und du erhältst eine große Menge detaillierter Performance-Messwerte.

Diese Messwerte umfassen ein [Wasserfalldiagramm]([LINK_URL_11]) (eine detaillierte Aufschlüsselung technischer Daten und Performance-Metriken, die das Laden einer Seite ausmachen, für jedes einzelne Objekt), aber auch Schlüsselwerte wie die [Core Web Vitals]([LINK_URL_12]) und [W3C Navigation Timings]([LINK_URL_13]), die sich auf das Kundenerlebnis oder auf Suchmaschinen-Rankings auswirken.

![Beispiel Full Pagecheck-Ergebnisse]([LINK_URL_14])

### Transaktions- / Web Application Monitoring [ANCHOR_3]

Ein [Transaktionsprüfobjekt (oder Web Application-Prüfobjekt)]([LINK_URL_15]) lädt deine Seite in einen tatsächlichen Browser und führt dann ein Skript aus, um mit der Seite zu agieren. Dabei werden die Aktionen eines echten Nutzers imitiert. Dieser Prüfobjekttyp kann verwendet werden, um komplette User Journeys, also Pfade eines Nutzers, auf deiner Website zu testen, beispielsweise Anmeldung, Shop-Funktionen mit Suche nach Produkten, Hinzufügen zum Warenkorb und Bezahlen sowie Ausfüllen von Formularen usw.

Ein typischer Nutzerablauf, bei dem der Nutzer mit deiner Website in mehreren Schritten interagiert, um eine bestimmte Aktion auszuführen, betrifft mehrere Webserver, Datenbanken, APIs oder externe Ressourcen. Transaktions-Monitoring ist der beste Weg zu prüfen, dass alle Aspekte deiner wichtigen Nutzeraktionen korrekt funktionieren. Es ist leicht, dies auch on Programmierkenntnisse einzurichten, wenn du das [Transaktionsrekorder]([LINK_URL_16])-Plug-in für Chrome verwendest.

![Der Schritteditor für Transaktionen]([LINK_URL_17])

#### API-Monitoring

Der [Multi-Step API (MSA)Prüfobjekttyp]([LINK_URL_18]) macht für Backend/APIs, was das Transaktions-Monitoring für Frontend/User Journeys macht. APIs ermöglichen die Kommunikation zwischen Anwendungen und sind das Rückgrat des modernen Internets.

Dein Unternehmen verlässt sich auf die eine oder andere Art mit Sicherheit auf mehrere APIs, aber das Erkennen möglicher Probleme, die eventuell auftreten, kann schwierig sein, da API-Kommunikation und Interaktionen im Hintergrund ablaufen. Mit dem Multi-Step API Monitoring kannst du deine APIs direkt prüfen, indem du Aufrufe erzeugst und die Antworten auf Richtigkeit, Vollständigkeit und Zeitnähe testest.

## Real User Monitoring

Neben dem Synthetic Monitoring bietet Uptrends ein [Real User Monitoring (RUM)]([LINK_URL_19]). RUM verwendet ein einfaches Skript, dass im HTML deiner Seite eingebettet ist, um tatsächliche Performance-Daten deiner Endnutzer in Echtzeit zu erfassen. In Ergänzung zu den Synthetic Monitoring-Daten kann RUM dir Einblicke in das Erlebnis deiner tatsächlichen Nutzer geben, ungeachtet davon, wo sie sich befinden. Es liefert dir Informationen zu den Einrichtungen deiner Nutzer in Bezug auf die von ihnen benutzten Browser und Betriebssysteme.

![Ein Beispiel für RUM-Daten]([LINK_URL_20])

## Alarme

Uptrends’ Monitoring umfasst ein leistungsstarkes und vielseitiges [Alarmierungssystem]([LINK_URL_21]). Lege fest, wann Alarme erzeugt und Benachrichtigungen gesendet werden – durch Einrichten von [Meldedefinitionen]([LINK_URL_22]). Verwende unsere schlüsselfertigen [Integrationen]([LINK_URL_23]), um Warnmeldungen per E-Mail, SMS oder Telefonanruf zu erhalten oder um sie an eine externe Plattform zu senden. Richte alternativ eine [benutzerdefinierte Integration]([LINK_URL_24]) ein, um eine Verbindung von Uptrends Alarmen zu jeder beliebigen externen Plattform herzustellen, auch solchen, die nicht auf der Integrationenseite gelistet sind.
