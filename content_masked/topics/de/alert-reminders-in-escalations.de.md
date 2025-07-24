{
  "hero": {
    "title": "Erinnerungsalarme bei Eskalationen"
  },
  "title": "Erinnerungsalarme bei Eskalationen",
  "summary": "Meldedefinitionen bieten eine Erinnerungsfunktion für alle Eskalationsstufen.",
  "url": "[URL_BASE_TOPICS]alarme/alarme-erinnerungen-in-eskalationen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Was sind Erinnerungen?

Eine Erinnerung ist eine Möglichkeit, um Operatoren wiederholt auf einen nicht behobenen Fehler aufmerksam zu machen. Wenn ein Alarm (basierend auf einen bestätigten Fehler) generiert wird, kannst du Operatoren und Systeme durch Senden einer Nachricht (über eine Integration) davon unterrichten. Operatoren sollten dann Maßnahmen ergreifen, um das angezeigte Problem zu lösen. Für den Fall, dass der Operator die Meldung nicht wahrgenommen oder nicht reagiert hat, kannst du ihm eine Erinnerung senden lassen, damit seine Aufmerksamkeit auf das Problem gelenkt oder dessen Dringlichkeit betont wird.
Wenn die SLAs (Service Level Agreements, Leistungsvereinbarung) mit deinen Kunden versprechen, dass Probleme innerhalb eines bestimmten Zeitraums behoben werden, solltest du sicherstellen, dass die Operatoren die Warnmeldung erhalten und beachten und entsprechend den in der SLA dargelegten Bedingungen handeln.

Die Erinnerungen in Uptrends' Anwendung sind Teil der Eskalationsstufen bei den Meldedefinitionen. Abhängig von den Eskalationsstufen deiner SLAs solltest du die Erinnerung hier einrichten.

Wurde ein Alarm erzeugt und besteht er fort, werden Erinnerungen gemäß deinen Einstellungen gesendet, bis eine OK-Meldung generiert wird. Sobald der angezeigte Fehler behoben wurde (der Check hat ein OK-Ergebnis und eine OK-Meldung ergeben), werden keine weiteren Erinnerungen mehr gesendet.

## Einrichten von Erinnerungen

Die Einstellung *Erinnerungen* ist Teil der [Eskalationsstufe]([LINK_URL_1]) innerhalb einer Meldedefinition.

![]([LINK_URL_2])

Du kannst die Maximalzahl an Erinnerungen und das Intervall, in dem sie erzeugt werden sollen, bestimmen, indem du den Satz mit Werten für "n" und "x" aktivierst:
*Sende maximal 'n' Erinnerungs-Alarme, alle 'x' Minuten.*

Folgendes ist bei der Angabe der Werte zu beachten:

-   Wenn keine Erinnerungen gesendet werden sollen, gib für "n" 0 ein.
-   Synchronisiere das Erinnerungsintervall mit dem Eskalationsintervall (falls eine Eskalation verwendet wird). Hast du unter Eskalationen beispielsweise "Generiere eine Warnmeldung, wenn Fehler länger als 5 Minuten andauern" festgelegt, macht es keinen Sinn, alle drei Minuten eine Erinnerung zu senden.
-   Berücksichtige das Überwachungsintervall (in den Einstellungen des Prüfobjekts). Wenn Erinnerungen häufiger versendet werden, als das Prüfobjekt Checks ausführt, entstehen möglicherweise Ineffizienzen. Es kann dazu kommen, dass eine Erinnerung ausgesendet wird, der nächste Check aber ein OK-Ergebnis zurückgibt. Dann ist die Erinnerung überflüssig.

[SHORTCODE_1]
**Hinweis**: Vermeide Erinnerungen, die sich mit unterschiedlichen Eskalationsstufen überschneiden, um den Überblick zu behalten. Wenn du bei Eskalationsstufe 1 drei Erinnerungen in Fünf-Minuten-Abständen eingerichtet hast und Eskalationsstufe 2 nach 10 Minuten aktiviert wird, werden sich die beiden überschneiden.
[SHORTCODE_2]

## Geeignete Integrationen für Erinnerungen

Integrationen sind die Definitionen, wie eine Benachrichtigung gesendet wird, nachdem ein Alarm erzeugt wurde. Nicht alle Integrationen sind gleich gut geeignet, eine Erinnerung zu senden.

Die Einrichtung von Erinnerungen ist nützlich bei Integrationen wie E-Mail, SMS und Slack. Anders ausgedrückt: Erinnerungen sind sinnvoll, wenn ein Mensch der Empfänger der Nachricht ist und auf sie reagiert.

Bei anderen Integrationen wie PagerDuty, Statushub, Splunk On-Call, ServiceNow und wahrscheinlich einigen benutzerdefinierten Integrationen kann die Einrichtung von Erinnerungen eventuell wenig Sinn machen. Häufig ändern solche Integrationen einen Status in einem System auf Grundlage einer Fehlermeldung oder eines OK-Ergebnisses. Eine Erinnerung würde den Status selbst nicht ändern und wäre in den meisten Fällen sinnlos. Der Fehlerstatus verbleibt im System, bis das System eine OK-Benachrichtigung erhält. Eine Erinnerung würde den Vorgang nicht ändern und wird daher nicht empfohlen.
