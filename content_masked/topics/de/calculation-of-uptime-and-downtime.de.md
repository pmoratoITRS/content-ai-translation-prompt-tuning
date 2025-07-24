{
  "hero": {
    "title": "Berechnung der Verfügbarkeit und Ausfallzeiten"
  },
  "title": "Berechnung der Verfügbarkeit und Ausfallzeiten",
  "summary": "Wie berechnest du die Verfügbarkeit deines Prüfobjekts auf Basis der Prüfergebnisse und wie wirken sich pausierte Prüfobjekte oder eine Wartung auf diese Berechnung aus?",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/dashboards/berechnung-von-verfuegbarkeit-und-ausfallzeit",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Verfügbarkeits- und Ausfallzeit-Berechnungen sind die Grundlage für mehrere Metriken in den Datenkacheln deines Dashboards und deiner [Service Level Agreements (SLAs)]([LINK_URL_1]). Sehen wir uns an, wie diese Berechnung erfolgt und welche Faktoren sie beeinflussen.
## Der Double-Check von Uptrends

Wenn ein Fehler auf deiner Website oder deinem Server verzeichnet wird, führt Uptrends immer eine zweite Prüfung von einem anderen Checkpoint aus, um den Fehler zu bestätigen. Deshalb siehst du bei Ausfällen immer ein Muster von nicht bestätigten und bestätigten Fehlern in deinen [Website Monitoring]([LINK_URL_2])-Dashboards.

So funktioniert es beim Standard-Monitoring. Wenn du das Parallel-Monitoring einsetzt, gibt es keine doppelte Prüfung. Der Artikel [Fehler und Alarmierung beim Parallel-Monitoring]([LINK_URL_3]) erläutert den Unterschied.

[SHORTCODE_1]
**Tipp**: Um eine detaillierte Analyse der genauen Messungen und der entdeckten Fehler zu erhalten, siehe dir bitte das Dashboard **Prüfobjektprotokoll** im Menü unter [SHORTCODE_7] Überwachung > Prüfobjektprotokoll [SHORTCODE_8] an.
[SHORTCODE_2]

## Wie wird die Verfügbarkeitsrate berechnet?

Die Art, wie die Verfügbarkeit berechnet wird, ist einfach: Nimm die Anzahl der Sekunden, die dein Prüfobjekt ausgefallen ist (in einem bestimmten Zeitrahmen) und dividiere dies durch die Gesamtanzahl der Sekunden, die dein Prüfobjekt in diesem Zeitrahmen überwacht wurde. Daraus ergibt sich der Prozentsatz der Ausfälle, der dann von 100 % subtrahiert wird, um die Verfügbarkeitsrate zu erhalten.

[SHORTCODE_3]
**Tipp**: SLAs nennen die Verfügbarkeit als Prozentzahl, aber wie viel Zeit steckt tatsächlich dahinter? Nutze den [kostenlosen SLA- und Verfügbarkeitsrechner]([LINK_URL_4]), um Ausfälle in Sekunden und in Prozentangaben zu konvertieren und umgekehrt.
[SHORTCODE_4]

### Beispiel

Nehmen wir an, du hast deine Website in einer Zeit von 24 Stunden (was 86.400 Sekunden sind) überwacht und in diesem Zeitraum war die Website 10 Minuten (600 Sekunden) ausgefallen. Um die Verfügbarkeits- und Ausfallraten zu erhalten, erfolgt die folgende Berechnung:

Gesamtzeit, in der deine Website ausgefallen war: 600 Sekunden
Gesamtzeit, in der deine Website überwacht wurde: 86.400 Sekunden
Ausfallrate = 600 Sekunden / 86.400 Sekunden = 0,0069 = 0,69 %
Verfügbarkeitsrate = 100 % - 0,69% = 99,31 %

[SHORTCODE_5]
**Tipp**: Spiele etwas mit den Daten, die dein Account anzeigt, um die tatsächlichen Sekundenzahl zu erhalten. Die [benutzerdefinierten Berichtskacheln]([LINK_URL_5]) des Typs _Datenliste_ und _Datendiagramm_ ermöglichen dir, die Sekundenzahlen anzuzeigen, in denen deine Prüfobjekte Verfügbarkeit und Ausfälle verzeichneten. Rufe eine Kachel auf und öffne das Dreipunkte-Menü [SHORTCODE_9][SHORTCODE_10], um zu den Kacheleinstellungen zu gelangen, einschließlich der unterschiedlichen Messwerte, die du auswählen kannst.
[SHORTCODE_6]

## Einfluss von Prüfobjektergebnissen

Wie berücksichtigt Uptrends den Zeitraum zwischen unterschiedlichen Prüfobjektergebnissen (OK, nicht bestätigte und bestätigte Fehler)? Wird die Zeit zwischen einem nicht bestätigten und einem betätigten Fehler als Verfügbarkeit oder als Ausfall erachtet?

Die Abbildung unten zeigt mögliche Abfolgen von Prüfergebnissen und wie die Zeiträume berücksichtigt werden. Natürlich gibt es bei einem langfristigen Monitoring eines Service oder Servers viele aufeinanderfolgende Prüfergebnisse. Aber alle Ergebnisse können in die folgenden Situationen aufgeschlüsselt werden:

![Illustration Reihenfolge der Prüfergebnisse]([LINK_URL_6])

Detailliert können sich die Prüfergebnisse folgendermaßen ändern:

**Unbestätigter Fehler -> bestätigter Fehler**  
Die Zeit zwischen den zwei Messungen wird als **Ausfall** betrachtet.

**Bestätigter Fehler -> unbestätigter Fehler**  
Die Zeit zwischen zwei Messungen wird als **Ausfall** berechnet, da das Prüfobjekt noch in der Fehlerbedingung ist. Ein Prüfobjekt meldet einen Fehler, bis eine OK-Anzeige erfolgt.

**Bestätigter Fehler -> OK**  
Die Zeit zwischen den zwei Messungen wird als **Ausfall** erachtet. Ein Prüfobjekt wird erst von dem Moment als verfügbar erachtet, an dem eine OK-Anzeige erfolgt.

**OK -> nicht bestätigter Fehler**  
Die Zeit zwischen den zwei Messungen wird als **Verfügbarkeit** gezählt, da noch nicht sicher ist, dass es sich tatsächlich um einen Fehler handelt.

**Unbestätigter Fehler -> OK**  
Die Zeit zwischen den zwei Messungen wird als **verfügbar** erachtet.

## Welche Fehler zählen zur Ausfallzeit?

Bitte bedenke, dass **alle Fehler berücksichtigt** werden, wenn die Ausfallzeit berechnet wird.

Wenn du zum Beispiel Performance Limits bei den Fehlerbedingungen des Prüfobjekts eingibst und ein Performance Limit erreicht ist, wird für diese Bedingung ein Fehler gemeldet. Obwohl deine Website nicht wirklich einen Ausfall vorweist (aber die Performance unter deinen Grenzen liegt), zeigt sie eine Verfügbarkeit von weniger als 100 % auf, weil die Performance-Bedingungen nicht erfüllt wurden.

## Wie wirken sich angehaltene Prüfobjekte auf die Verfügbarkeitsrate aus?

Wenn du ein Prüfobjekt pausierst, wird diese Zeit als „unbekannt“ registriert. Beachte in Bezug auf die Verfügbarkeitsberechnung, dass die Gesamtzahl Sekunden für den Status Unbekannt ebenfalls einbezogen und die unbekannte Zeit als Verfügbarkeit verzeichnet wurde. Die Formel für die Verfügbarkeitsrate lautet **(Verfügbarkeit + unbekannt) / (Verfügbarkeit + Ausfallzeit + unbekannt)**, wobei Verfügbarkeit, Ausfallzeit und „unbekannt“ in Sekunden angegeben werden.

Dies wurde so eingerichtet, da viele Kunden es wünschten. Wenn du die Unbekannt-Zeiten aus der Verfügbarkeitsrechnung ausschließen möchtest, kannst du die Gesamtzeit der Verfügbarkeit und Ausfallzeiten in Sekunden abrufen und eine eigene Berechnung durchführen. Die Formel für die Verfügbarkeitsrate lautet **Verfügbarkeit / (Verfügbarkeit + Ausfallzeit)**, wobei Verfügbarkeit und Ausfallzeit in Sekunden angegeben werden.

## Wie wirkt sich die Wartung auf die Verfügbarkeitsrate aus?

Fehler, die während eines [Wartungszeitraums]([LINK_URL_7]) auftreten, werden aus den Verfügbarkeitsberechnungen ausgeschlossen, sofern die *Wartungsart* des Wartungszeitraums auf **Überwachung komplett deaktivieren** gesetzt wurde (im Unterschied zu „Nur Benachrichtigungen deaktivieren“).
