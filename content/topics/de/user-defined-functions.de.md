{
  "hero": {
    "title": "Benutzerdefinierte Funktionen"
  },
  "title": "Benutzerdefinierte Funktionen",
  "summary": "Ein Überblick der verfügbaren benutzerdefinierten Funktionen und wie sie eingesetzt werden",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/benutzerdefinierte-funktionen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/user-defined-functions"
}

Uptrends‘ [Multi-Step API Monitoring]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) bietet dir die Möglichkeit, mehrere aufeinanderfolgende HTTP-Abfragen bei deiner API auszuführen, bei denen eingehende Daten geparst, in Variablen gespeichert oder auf bestimmte Inhalte geprüft werden. In einigen Fällen wird es jedoch erforderlich sein, eingehende Daten zu transformieren oder zuzuweisen, um ihre Bedeutung leichter zu erfassen. Beispiele hierfür sind die XML- und JSON-Codierungs- und Decodierungsfunktionen, wie wir sie in unserem [Leitfaden zur Nachrichtenformatierung bei benutzerdefinierten Integrationen]({{< ref path="support/kb/alerting/integrations/custom-integrations/message-formatting" lang="de" >}}) beschrieben haben. Neben diesen vorbestimmten Funktionen bietet Uptrends dir die Möglichkeit, **benutzerdefinierte Funktionen** einzurichten. Diese Funktionen können dann verwendet werden, um [Variablenwerte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}) (aus einem vorherigen Schritt oder aus einer von [Uptrends bereitgestellten Systemvariable]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}})) in einen neuen Wert zu konvertieren.

## Verfügbare benutzerdefinierte Funktionen

Es gibt die folgenden Typen benutzerdefinierter Funktionen:

- **Regulärer Ausdruck:** Anhand dieser Funktion kannst du einen regulären Ausdruck (RegEx) auf deine zuvor erstellten Variablen anwenden. Dies ist nützlich, wenn man bestimmte Abschnitte aus Antwortdaten extrahieren möchte (wie etwa das Extrahieren eines Authentifizierungscodes aus einem *Location*-Header zur Weiterleitung).
- **Mapping:** Der Funktionstyp Mapping erlaubt dir, automatisch bestimmte Werte der Antwort mit spezifischen anderen Werten zu ersetzen. Wenn zum Beispiel ein Endpunkt die Begriffe *error* oder *ok* (wie etwa Uptrends‘ [eigene API]({{< ref path="support/kb/api" lang="de" >}})) nutzt, während der nächste, mit dem eine Interaktion erfolgt, die Begriffe *incident* oder *healthy* erwartet, kannst du die Mapping-Funktion nutzen, um diese Werte automatisch auf die richtigen Äquivalente anzupassen.
- **Hash**: Hash-Funktionen sind Einweg-Algorithmen, die eine Nachricht beliebiger Länge nehmen und sie in einen Wert mit fester Länge umwandeln. Jede Eingabe muss immer dasselbe Ergebnis haben, sodass Hash-Funktionen beim sicheren Vergleich sensibler Daten wie Passwörter, Autorisierungs-Tokens oder digitale Signaturen nützlich sind, ohne die Notwendigkeit, diese tatsächlich zu übergeben. Mehr zu dem Einsatz von Hash-Funktionen bei Multi-step API-Prüfobjekten findest du in unserem Artikel zu [Hashing und Codierung]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/hashing-and-encoding" lang="de" >}}).

## Benutzerdefinierte Funktionen erstellen

Du kannst eine benutzerdefinierte Integration entweder auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}} des Prüfobjekts Multi-Step API oder auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} deiner (benutzerdefinierten) Integrationen erstellen.

{{< callout >}}
**Hinweis**: Eine benutzerdefinierte Funktion gilt speziell für das bestimmte Multi-Step API-Prüfobjekt, für das du sie eingerichtet hast. Sie wird nicht in anderen Prüfobjekten oder Integrationen übernommen.
{{< /callout >}}

1.  Auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}} bei einem deiner Multi-Step API-Prüfobjekte oder auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} deiner (benutzerdefinierten) Integrationen findest du die Überschrift **Benutzerdefinierte Funktionen** am Ende der Seite.

2.  Klicke auf {{< AppElement type="buttonSecondary" >}}Funktion hinzufügen{{< /AppElement >}}, um eine neue Funktion zu definieren.

3.  Wähle den entsprechenden Funktionstyp: **Mapping**, **regulärer Ausdruck**, oder **Hash**. Gib dann der Funktion einen angemessenen Namen – wir empfehlen etwas Einfaches ohne Leerstellen, da du dich später darauf beziehen musst.

4.  Gib alle zusätzlich erforderlichen Informationen ein:
  - Füge im Falle einer Mapping-Funktion die einzelnen erforderlichen Zuweisungen hinzu. Die Mapping-Funktion übersetzt die „Von“-Werte in die zugehörigen „Zu“-Werte.
  - Gib für die Funktion „Regulärer Ausdruck“ den erforderlichen regulären Ausdruck an. Der Regex wird mit dem Eingabetext abgeglichen und kann verwendet werden, um einen bestimmten Teil der Eingabe zu extrahieren.
  - Gib bei einer Hash-Funktion, die einen der HMAC-Algorithmen verwendet, den geheimen Schlüsselwert ein.

Du kannst bei Bedarf weitere Funktionen durch Wiederholen dieser Schritte hinzufügen.

![Beispiel einer benutzerdefinierten Funktion](/img/content/scr-MSA-UDF-example.min.png)

## Die Funktionen nutzen {id="using-functions"}

Um deine neu festgelegten **benutzerdefinierten Funktionen** einzusetzen, musst du die Variablen, mit der die Funktion interagieren soll, in die Funktionsreferenz einbinden, etwa: `{{userDefinedFunction({{variableReference}})}}`. Sehen wir uns als Beispiel eine Mapping-Funktion an, deren Zweck es ist, eingehende Antwortdaten von „Error“ nach „Incident“, von „Warning“ nach „Unhealthy“ und von „Ok“ nach „Healthy“ zu übersetzen, sodass der in den folgenden Schritten aufgerufene Endpunkt Begriffe erhält, die er versteht. In diesem Beispiel:

-   Eine benutzerdefinierte Funktion, wie sie in der Abbildung oben zu sehen ist, wurde mit Namen `errorMapping` erstellt.
-   Der Endpunkt sendet eine JSON-formatierte Antwort mit dem Feld “Status“, mit dem die Werte „Error“, „Warning“ oder „Ok“ übermittelt werden.
-   Im folgenden Schritt möchten wir diese Statusdaten an eine andere API weiterleiten. Diese neue API versteht aber die verwendeten Begriffe nicht und erfordert stattdessen die Werte „Incident“, „Unhealthy“ oder „Healthy“.

Um die Funktion `errorMapping` für die automatische Übersetzung der Statuswerte in die richtigen Werte zu verwenden, folge diesen Schritten:

1.  Extrahiere wie gewohnt den Wert des „Status“-Feldes aus den Antwortdaten (siehe [Leitfaden zur Einrichtung von Multi-Step Monitoring-Variablen]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}})). In diesem Beispiel trägt die sich ergebende Variable den Namen statusRaw. Und wie beschrieben enthält diese Variable „Error“/„Warning“/„Ok“.
2.  Klicke auf {{< AppElement type="buttonSecondary" >}}Variable hinzufügen{{< /AppElement >}}, um die benutzerdefinierte Funktion anzuwenden.
3.  Setze die Variablen-Quelle (die Drop-down-Liste auf der linken Seite) auf {{< Code/Symbol type="source" >}}Funktion ausführen{{< /Code/Symbol >}}.
4.  Gib für den **Funktionsausdruck** die Variablenreferenz wie oben beschrieben in die Funktion ein: {{< Code/Symbol type="property" >}}{{errorMapping({{statusRaw}})}}{{< /Code/Symbol >}} 
5.  Der sich ergebende Wert lautet entweder „Incident“, „Unhealthy“ oder „Healthy“, abhängig davon, welcher Wert mit der Variable statusRaw eingegangen ist. Im Feld **Name der Variable** gibst du einen Namen für den Ausgabewert ein.

![Verwenden einer benutzerdefinierten Funktion](/img/content/scr-MSA-UDF-execute-function-example.min.png)

Nun haben wir einen neuen Wert, *Status*, erstellt, dessen Wert entweder „Incident“, „Unhealthy“ oder „Healthy“ lautet. In den folgenden Schritten können wir uns auf diese Variable in der regulären Notation, z. B. `{{status}}`, beziehen. In diesem Beispiel haben wir eine **Mapping**-Funktion verwendet. Die Schritte für eine **RegEx**-Funktion sind jedoch gleich.
