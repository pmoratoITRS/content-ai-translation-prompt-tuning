{
  "hero": {
    "title": "Benutzerdefinierte Metriken einrichten"
  },
  "title": "Benutzerdefinierte Metriken einrichten",
  "summary": "Erfahre mehr über benutzerdefinierte Metriken und wie du sie bei Multi-Step API (MSA) Prüfobjekten einrichtest",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/einrichtung-von-custom-api-metrics",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Da APIs eine bedeutende Rolle im täglichen Geschäfts-, Plattform- und Servicebetrieb spielen, ist es wichtig, regelmäßig ihr Verhalten zu prüfen und eine Datenvalidierung durchzuführen. Hier erläutern wir, wie du **Benutzerdefinierte Metriken** nutzen kannst, um die Verfügbarkeit deiner API zu überwachen, API-Antwortdaten zu erfassen und diese Daten visuell in Echtzeit-Diagrammen oder als Liste zur Analyse darzustellen.

**Benutzerdefinierte Metriken** ist in [Multi-Step API (MSA)-Prüfobjekten]([LINK_URL_1]) verfügbar und ermöglicht dir, bestimmte numerischen Daten von jeder internen oder externen API zu erfassen.
Mit jedem erfassten Datenpunkt kannst du diese Werte in einer [benutzerdefinierten Metrikvariable]([LINK_URL_2]) speichern, um den Fortschritt der Daten über einen Zeitraum visuell anzuzeigen.

## Welchen Nutzen haben benutzerdefinierte Metriken?

Nehmen wir an, wir haben eine API für ein E-Commerce-System, die Echtzeit-Informationen über einen Produktkatalog liefert. Darin sind Preise, Produktinventar und andere Produktdaten enthalten.

Beispielsweise möchten wir die Anzahl pro Produkt im Lagerbestand nachhalten. Statt die API jedes Mal manuell aufzurufen, erfassen benutzerdefinierte Metriken diese Daten automatisch aus der API-Antwort und speichern jeden Datenpunkt in [Variablen benutzerdefinierter Metriken]([LINK_URL_3]):

![Benutzerdefinierte Metrikvariable für Produkte]([LINK_URL_4])

Jedes Mal, wenn das MSA-Prüfobjekt ausgeführt wird, verfolgt es die Werte dieser Variablen. Dann kannst du damit eine [Liste benutzerdefinierte Metriken]([LINK_URL_5]) zur weiteren Daten- oder Trendanalyse erstellen oder deine Geschäftsberichte und die betriebliche Leistung überwachen:

![Benutzerdefinierte Metrikvariable]([LINK_URL_6])

Es gibt auch verschiedene Wege, um benutzerdefinierte Metriken in unterschiedlichen Kontexten zu verwenden:

- Bei DevOps kannst du den Status deines Systems oder einer Anwendung überwachen, indem du Metriken wie die Anzahl erfasster Fehler, gleichzeitiger Nutzer und Netzwerkgeschwindigkeit verfolgst.
- Im IT-Betrieb kannst du Umgebungsmetriken von Datenzentren wie Temperatur, Luftfeuchtigkeit und Systemstatus überwachen.
- Beim IT-Support kannst du die Anzahl an Supportanrufen verfolgen, die in der Warteschleife sind, die Anzahl an Tickets und die SLA-Performance.

## Benutzerdefinierte Metriken einrichten

Sobald du ein [MSA-Prüfobjekt eingerichtet hast]([LINK_URL_7]) – mit einem Schritt oder mehreren Schrittdefinitionen –, kannst du **benutzerdefinierte Metriken** auf zwei Weisen spezifizieren: [Mit einer Variable setzen]([LINK_URL_8]) oder [Mit Skripting setzen]([LINK_URL_9]).

Hinweis: Verwende bei der Erstellung einer neuen benutzerdefinierten Metrik einen Namen, der verständlich ist und der die Funktion in Kontext setzt. Der Metrikname und der Name des Prüfobjekts erscheinen in der Liste verfügbarer benutzerdefinierter Metriken, wenn du diese zu deinem Bericht über benutzerdefinierte API-Daten hinzufügst. Du kannst denselben Namen für benutzerdefinierte Metriken verwenden, um ähnliche Datentypen darzustellen, die zu unterschiedlichen Gruppen gehören. Beispielsweise kann eine benutzerdefinierte Metrik namens [INLINE_CODE_1] sowohl in produktspezifischen APIs als auch in kundenspezifischen APIs genutzt werden. Obwohl der Name derselbe ist, gehören die Daten, für die der Name steht, zu unterschiedlichen Gruppen. Uptrends empfiehlt, direkt die richtigen Namen zu vergeben. Späteres Umbenennen einer benutzerdefinierten Metrik wird als Erstellen einer neuen, anderen Metrik behandelt.

### Mit einer Variable setzen

Anhand dieser Methode kannst du API-Antwortdaten verfolgen und speichern, ohne Code oder ein Skript zu schreiben. Du kannst einfach einen Ausdruck in einer Variable definieren und einen Namen für die benutzerdefinierte Metrik vergeben, um diese Variable als benutzerdefinierte Metrik zu verwenden.

Als Beispiel richten wir eine **benutzerdefinierte Metrik** anhand der [Carbon API]([LINK_URL_10]) ein. Um die Kohlenstoff-[INLINE_CODE_2]-Daten anhand der Variablenmethode zu verfolgen:

{{[HTML_TAG_1]}}

### Mit Skripting setzen

Diese Method ermöglicht dir, deine eigenen [Skripte]([LINK_URL_11]) zu schreiben. Damit hast du volle Kontrolle, wie du API-Antwortdaten erfasst und behandelst.

Stelle sicher, dass du [Schnipsel für Custom metrics]([LINK_URL_12]) nutzt und einen Namen für die benutzerdefinierte Metrik vergibst, um die Daten als benutzerdefinierte Metrik zu verwenden.

Als Beispiel richten wir eine **benutzerdefinierte Metrik** anhand der [Carbon API]([LINK_URL_13]) ein. Um die Kohlenstoff-[INLINE_CODE_3]-Daten anhand der Skripting-Methode zu verfolgen:

{{[HTML_TAG_2]}}

Um mehr über die Schnipsel und Skripting zu erfahren, lies [Multi-Step API (MSA) Benutzerdefinierte Skripte]([LINK_URL_14]).

[SHORTCODE_1] **Hinweis:** Innerhalb eines MSA-Prüfobjekts kannst du höchstens fünf [Variablen für benutzerdefinierte Metriken]([LINK_URL_15]) festlegen. Um weitere hinzuzufügen, wende dich bitte an das [Support-Team]([LINK_URL_16]), das dir weiterhilft. [SHORTCODE_2]

## Daten der benutzerdefinierten Metriken untersuchen

Untersuche nach der Einrichtung die Daten der benutzerdefinierten Metriken, um sicherzustellen, dass das Prüfobjekt die Daten richtig nachverfolgt und erfasst.

Um die Daten der benutzerdefinierten Metriken, die du überwachst, zu untersuchen:

1. Gehe zur [SHORTCODE_3] API-Prüfobjekteeinrichtung [SHORTCODE_4].
2. Klicke auf den Link **Geh zu Dashboard** bei dem Prüfobjekt, bei dem du die **Benutzerdefinierte Metrik** erstellt hast.
3. Klicke in der Kachel **Prüfobjekt Protokoll** auf eine beliebige Zeile, um die **Kontrolldetails** zu öffnen.

Im Pop-up-Fenster siehst du die Daten der benutzerdefinierten Metriken, die vom Prüfobjekt abgerufen wurden. Beachte, dass der Wert [INLINE_CODE_4] 85 beträgt:

![Carbon-intensity-Daten der benutzerdefinierten Metriken]([LINK_URL_17])

Du erhältst direkten Zugriff auf die einzelnen Werte der benutzerdefinierten Metrik, wie sie während der Ausführung des MSA-Prüfobjekts erfasst wurden.

### Fehlerbehebung

Solltest du keine Werte der benutzerdefinierten Metriken sehen, bedenke Folgendes:

- Hast du versehentlich die Check-Ergebnisse für einen älteren Check geöffnet, der ausgeführt wurde, bevor die neue benutzerdefinierte Metrik definiert wurde?

- Erfasst deine benutzerdefinierte Metrik numerische Ganzzahldaten? Enthält sie Textdaten oder Kommazahlen (wie etwa 99,9 % oder 3,1415 ), dann wird die benutzerdefinierte Metrik nicht erfasst. Derzeit werden nur Ganzzahlen unterstützt. 

- Wenn bei der Ausführung des MSA-Prüfobjekts ein Fehler aufgetreten ist, wurde die Variable, die deiner benutzerdefinierten Metrik zugewiesen wurde, möglicherweise gar nicht erst erstellt. Prüfe, ob es Tippfehler im Namen der benutzerdefinierten Metrik oder bei den Variablen gibt.

## Benutzerdefinierte Metriken in Dashboards anzeigen

Wenn du dir die Werte genauer ansehen willst und mit den zugrunde liegenden Daten arbeiten möchtest, um plötzliche Änderungen der Werte zu erkennen, kannst du die benutzerdefinierten Metriken in einem Dashboard mit **Liste oder Diagramm Benutzerdefinierte Metriken** anzeigen:

![Diagramm benutzerdefinierter Metriken]([LINK_URL_18])

Damit kannst du einen Trend bei der Metrikvariable darstellen, und Tiefst- Durchschnitts- und Höchstwerte anzeigen. Weitere Informationen findest du unter [Liste oder Diagramm Benutzerdefinierte Metriken]([LINK_URL_19]).

Du kannst die Daten auch als Liste/Diagramm benutzerdefinierter Metriken in unterschiedlichen Datenformaten über die
Funktion des [Exports von Dashboard-Daten]([LINK_URL_20]) exportieren.
