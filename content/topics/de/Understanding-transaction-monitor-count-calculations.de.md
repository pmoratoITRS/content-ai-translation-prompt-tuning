{
  "hero": {
    "title": "Credit-Berechnungen bei Transaktionsprüfobjekten"
  },
  "title": "Credit-Berechnungen bei Transaktionsprüfobjekten",
  "summary": "Erfahre, wie wir die Anzahl der Transaktions-Credits für deine Transaktion bestimmen.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/berechnung-transaktions-credits",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/Understanding-transaction-monitor-count-calculations"
}

Wenn du dich fragst, wie Uptrends die Kosten für ein bestimmtes Transaktionsprüfobjekt festlegt, erfährst du hier mehr. Bevor wir die Credit-Berechnung erläutern, sehen wir uns einige häufig verwendete Begriffe in Bezug auf Transaktionsprüfobjekte an.

**Transaktion:** Eine Transaktion ist der Weg eines Nutzers, dem er folgt, um eine Aufgabe auf einer Website auszuführen. Transaktionen umfassen Aufgaben wie Anmeldung, Einkauf, Einreichen eines Formulars, Abruf eines Dokuments, Einrichten eines Kontos, Zurücksetzen eines Passworts usw. Eine einzelne Transaktion wird aus zwei oder mehr Schritten bestehen.

**Transaktions-Credit:** Betrachte Transaktions-Credits wie Bargeld. Auf Grundlage deines jeweiligen Uptrends Plans verfügst du über eine bestimmte Menge von Transaktions-Credits. (Du kannst immer auch Credits hinzukaufen.) Ein Transaktionsprüfobjekt „kostet“ eine bestimmte Anzahl von Credits, die auf mehreren Faktoren beruhen, zu denen wir gleich kommen werden. Während sich das Prüfobjekt im Entwicklungsmodus befindet, werden keine Credits verbraucht oder benötigt. Du nutzt die Credits, wenn das Prüfobjekt in den Staging- oder Produktionsmodus übergeht. (Erfahre mehr über [Prüfobjektmodi]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}).). Du kannst die Anzahl der dir verfügbaren Credits auf der Seite Account-Einstellungen sehen.

**Nutzeraktionen:** Eine Nutzeraktion ist die Interaktion eines Nutzers mit der Seite. Beispiele für Nutzeraktionen sind unter anderem Klicken, Texteingabe, Mausbewegungen wie etwa zum Einblenden von Text und Inhaltsprüfungen. 

**Schritt:** Ein Schritt ist eine beliebige Gruppierung von Nutzeraktionen. Du kannst die Aktionen in Schritte zusammenfassen, die für dich den meisten Sinn ergeben und dir bei der Fehlerbehebung und bei Berichten helfen. Uptrends berichtet über Zeiten auf Schritt-Basis (was du bei der Einrichtung deiner Schritte berücksichtigen solltest). Unsere Empfehlung ist, jeden Schritt mit einer Aktion, bei der die nächste Seite geladen wird, und einer Inhaltsprüfung zu beenden.

## Wie bestimmt Uptrends die Anzahl der Credits, die ein Transaktionsprüfobjekt benötigt?

Wir bestimmen die Anzahl der Transaktions-Credits für eine Transaktion auf Grundlage unterschiedlicher Faktoren:

**Die Anzahl der Nutzeraktionen, die zu einer Serveranfrage führen**. Jede Nutzeraktion (siehe Definition oben) bei einem Transaktionsprüfobjekt, die zu einer Serveranfrage führt, verbraucht einen Transaktions-Credit. Navigationsaktionen, Datei-Uploads und Klicken, durch das eine neue Seite im Browser geladen wird, verbrauchen einen Credit. Texteingabe, Mausbewegungsaktionen und Inhaltsprüfungen sind kostenlos.
  
**Transaktions-Wasserfälle, -Filmstreifen und -Screenshots:** Jeder Wasserfallbericht und Screenshot in deiner Transaktion benötigt einen Transaktions-Credit. Filmstreifen werden mit einem Transaktions-Credit berechnet, es sei denn, es wurde bereits ein Screenshot in dem Schritt eingefügt. In dem Fall wird der Filmstreifen kostenlos bereitgestellt. Zwei Screenshots und ein Filmstreifen erfordern zwei Transaktions-Credits.

## Die Berechnung der Anzahl der Transaktionsprüfobjekte

Eine Formel zur Berechnung der Anzahl der Credits für eine einzelne Transaktion könnte folgendermaßen aussehen:

**Anzahl der Aktionen mit Serveranfragen** + **Anzahl der Wasserfalldiagramme** + **Anzahl der Screenshots** = **Gesamtzahl der Transaktions-Credits**

**Hinweis:** Wenn du ein neues Prüfobjekt hinzufügst oder ein Prüfobjekt änderst, wird die Prüfobjektzahl in deiner Prüfobjektliste die Anzahl der Credits gefolgt von dem Hinweis „wird berechnet“ oder „berechnet“ anzeigen. Das System benötigt einen Moment, um deine Transaktionsschritte zu analysieren und die Kosten festzustellen. In besonderen Fällen prüft unser Support-Team die geänderten oder neuen Prüfobjekte, um sicherzustellen, dass die auf das Prüfobjekt angewendete Anzahl von Prüfobjekt-Credits korrekt ist.

## Zu guter Letzt

Wenn du immer noch Fragen hast, wie wir die Berechnung zur Nutzung der Transaktions-Credits vorgenommen haben, [wende dich an unseren Support](/contact). Unser Support-Team prüft die Transaktion mit dir und klärt alle Fragen dazu.
