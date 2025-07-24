{
  "hero": {
    "title": "Einsatz von Wartebedingungen"
  },
  "title": "Einsatz von Wartebedingungen",
  "summary": "Beim Skripterstellen für deine Transaktionen musst du das Prüfobjekt manchmal anweisen, auf das Laden eines bestimmten Objekts zu warten, bevor es fortfährt. Das Transaktions-Monitoring unterstützt drei Arten von Wartebedingungen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/einsatz-von-wartebedingungen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Das Laden einer Seite erfordert Zeit. Genauso, wie du manchmal auf das Laden einer Seite warten musst, muss auch das Transaktionsskript darauf warten, bis die Seite vollständig geladen ist, bevor es mit der nächsten Aktion fortfahren kann.

Das Laden einer Seite erfolgt etwas chaotisch, weil der Browser den Vorgang in Phasen unterteilt, bei denen manche Objekte gleichzeitig laden und andere zu einem späteren Zeitpunkt. Daher weiß das Skript nicht unbedingt immer, wann es die nächste Aktion ausführen kann. Das Skript muss warten, bis der Browser die Seitenobjekte geladen hat und bis sie interaktiv sind, um mit der nächsten Aktion zu beginnen.

Aufgrund dieses chaotischen Ladevorgangs verfügen Uptrends‘ Transaktionsprüfobjekte über die Option **Warte bis** bei allen Aktionen, die mit einem bestimmten Objekt interagieren. Mit der Option **Warte bis** kannst du festlegen, welche Bedingung das angegebene Objekt erfüllen muss, bevor die Transaktion eine Aktion ausführen kann.

Derzeit stehen dir drei unterschiedliche **Warte bis**-Bedingungen zur Verfügung.

![]([LINK_URL_1])

## Das Element existiert

Die Option **Das Element existiert** prüft, ob das angegebene Objekt im DOM der Seite vorliegt. Nur weil ein Objekt existiert, heißt das nicht unbedingt, dass du damit interagieren kannst oder dass es auf der Seite sichtbar ist. Das DOM einer Seite enthält häufig Objekte, die der Browser aus vielerlei Gründen nicht darstellt. Die Option **Das Element existiert** gestattet der Transaktion, fortzufahren, sobald sie das angegebene Objekt im DOM-Dokument-Knoten findet.

## Das Element ist sichtbar

Die Option **Das Element ist sichtbar** prüft, ob das angegebene Objekt im DOM Dokument-Knoten vorliegt und auf der Seite sichtbar ist. Zum Beispiel kann ein Drop-down-Menü mehrere Links enthalten, die nicht sichtbar werden, bis du mit dem Mauszeiger über ein bestimmtes Seitenobjekt fährst. Da diese Links im DOM existieren, bevor die Hover-Aktion verfügbar ist, muss das Transaktionsprüfobjekt warten, bis der Browser die Links anzeigt, um eine Interaktion mit den Links auszuführen.

## Das Element ist sichtbar und aktiv

Die Option **Das Element ist sichtbar und aktiv** verhält sich wie die Option **Das Element ist sichtbar**, allerdings mit einem wichtigen Unterschied: Das Objekt muss nicht nur auf der Seite sichtbar sein, es muss auch aktiv sein. Der Browser deaktiviert (häufig ausgegraut) beispielsweise bestimmte Schaltflächen, bis die Seite eine spezielle Anforderung erfüllt. Eine solche Anforderung kann sein, dass ein Formular ausgefüllt sein muss, bevor die Schaltfläche geklickt werden kann. Daher ist das Objekt zwar auf der Seite sichtbar, aber du musst das Transaktionsprüfobjekt dennoch anweisen zu warten, bis die Schaltfläche aktiv ist, bevor es eine Interaktion versucht.

## Was ist eine angemessene Wartezeit?

Die von dir eingerichtete Wartezeit, ist die Höchstdauer, die dein Prüfobjekt auf ein Element wartet. Die Standard-Wartezeit, sofern nicht anders festgelegt, beträgt 60 Sekunden für eine Navigation und 30 Sekunden für alle anderen Aktionstypen. Diese Standardangaben bieten in der Regel ausreichend Zeit, sodass sie im Allgemeinen selten geändert werden müssen. Wenn du diese Zeitüberschreitungswerte ändern musst, kannst du sie im Feld **Warte-Timeout** anpassen. Der Höchstwert für das Warte-Timeout beträgt 60 Sekunden bei allen Aktionstypen. Beachte Folgendes bei langen Wartezeiten:

-   Richte nicht zu kurze Wartezeiten ein. Kurze Timeouts führen dazu, dass dein Prüfobjekt Fehler generiert. Wir empfehlen die Standardwerte zu belassen, um unerwünschte Fehlermeldungen zu vermeiden.
-   Die Höchstdauer einer Ausführung, die Uptrends bei Transaktionsprüfobjekten ermöglicht, ist vier Minuten. Nach vier Minuten meldet die Transaktion eine Zeitüberschreitung. Obwohl das Prüfobjekt nur so lange wartet, wie es muss, und bis zur von dir eingerichteten Zeitüberschreitung, können verlängerte Wartezeiten dazu führen, dass das Prüfobjekt einen Fehler meldet, weil es die Vier-Minuten-Höchstdauer zur Ausführung erreicht hat.

[SHORTCODE_1]
**Hinweis**: Im Allgemeinen müssen die Standardeinstellungen für Wartebedingungen nicht geändert werden. Wenn du denkst, dass du die Wartebedingungen anpassen solltest, [wende dich an den Support]([LINK_URL_2]), damit er dir bei der Optimierung der Warteoptionen deines Prüfobjekts hilft.
[SHORTCODE_2]
