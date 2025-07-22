{
  "hero": {
    "title": "In RUM verwendete Medianwerte"
  },
  "title": "In RUM verwendete Medianwerte",
  "summary": "Bei RUM von Uptrends hast du die Wahl zwischen Median- und Durchschnittswerten. Erfahre wie Uptrends die Medianwerte für deine Berichte berechnet.",
  "url": "[URL_BASE_TOPICS]rum/in-rum-verwendete-medianwerte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Beim [Real User Monitoring]([LINK_URL_1]) (RUM) geht es um die aggregierte Nutzererfahrung. Daher berechnet der RUM-Bericht die Ergebnisse basierend auf allen deinen Nutzern. Zu wissen, wie Uptrends die Ergebnisse berechnet, ist wichtig, da du wissen musst, dass die RUM Daten wirklich repräsentativ für die Erfahrung der Nutzer sind. Standardmäßig zeigen die RUM-Berichte die Medianwerte vor den Durchschnittswerten, aber du kannst jederzeit zwischen den beiden Methoden wechseln. Damit du die beste Wahl für deine Berichte treffen kannst, werden in diesem Artikel die beiden Methoden verglichen und erklärt, wie Uptrends die Medianwerte berechnet. Wir erläutern zudem, warum wir überzeugt sind, dass Stichproben keine gute Wahl für die RUM-Daten sind.

## Durchschnitt gegenüber Median

Betrachtest du die RUM-Tabellen und -Diagramme, wirst du feststellen, dass standardmäßig die Medianwerte statt der Durchschnittswerte gezeigt werden. Wir verwenden den Medianwert, weil wir der Ansicht sind, dass der Median repräsentativer ist. Sehen wir uns die zwei Methoden genauer an

**Durchschnitt:** Die Summe aller Zahlen, dividiert durch die Menge. Beispielsweise lautet der Durchschnitt für das Set {1, 2, 2, 3, 12} 4.

**Median:** Die mittlere Zahl in einem Set. Beispielsweise lautet der Medianwert für das Set  
{1, 2, 2, 3, 12} 2.

An den obigen Beispielen kann man sehen, dass die „Ausreißerzahl“ 12 den Durchschnittswert verzerrt, während der Medianwert das Dataset präziser repräsentiert. Berechnungen mithilfe des Medianwerts erfassen die Zentralmenge ohne Verzerrung durch ungewöhnlich hohe oder niedrige Werte im Set. 

## Wie Uptrends den Medianwert berechnet

In einem relativ kleinen Dataset berechnet Uptrends den Median durch Sortieren der Datenreihe und Verwenden des mittleren Werts. Bei größeren Datasets kommt es jedoch bei der Berechnung des Medianwerts zu Problemen. Die mittleren Werte in großen Datasets zu finden, erfordert viel Zeit. Um dich aber nicht warten zu lassen, berechnen wir den Medianwert anhand eines [Histogramms]([LINK_URL_2]). Der Histogramm-Ansatz beschleunigt die Berechnung, aber führt auch eine geringe Normalabweichung von etwa 1 % ein. Selbst mit der möglichen 1%igen Abweichung ist aus unserer Sicht die Medianberechnung anhand eines Histogramms besser als der Durchschnittswert, um die Erfahrungen der Nutzer genau darzustellen.

## Die Zufallsstichprobe als Alternative zum Histogramm 

Ein alternativer Ansatz zum Histogramm ist die [Zufallsstichprobe]([LINK_URL_3]). Mit der Zufallsstichprobe wird bei der Berechnung nur eine Untergruppe der Daten zur Feststellung eines Durchschnitts- oder Medianwerts verwendet. RUM ermöglicht die Gruppierung der Daten auf Grundlage des Standorts, Browsers und Version, Betriebssystems und Version, Gerätetyps und der aufgerufenen Seiten. Bei der Zufallsstichprobe können ganze Nutzergruppen verloren gehen. Wir bei Uptrends möchten, dass du die Ergebnisse vor dem Hintergrund all deiner Website-Besucher siehst. Aber wie bereits erwähnt, erfordert die Berechnung der Ergebnisse Zeit. Mit dem Histogramm-Ansatz erhältst du die Ergebnisse schnell und ohne den Verlust von Nutzern in deinem Dataset.

## Zwischen Median- und Durchschnittswerten wechseln

Du kannst bestimmen, welche Berechnungsmethode für deine Berichte genutzt wird.

1.  Öffne die RUM Dashboard-Kachel, die du ändern möchtest.

2.  Klicke auf das Dreipunkte-Menü [SHORTCODE_1] [SHORTCODE_2], um die Einstellungen aufzurufen.

3.  Wähle eine Option in der **Gesamtsumme**-Liste.

4.  Klicke auf [SHORTCODE_3]Übernehmen[SHORTCODE_4].

![Screenshot Kacheleinstellung Aggregation]([LINK_URL_4])
