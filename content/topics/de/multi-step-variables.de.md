{
  "hero": {
    "title": "Multi-Step Monitoring-Variablen"
  },
  "title": "Multi-Step Monitoring-Variablen:",
  "summary": "Die Verwendung von Variablen zur Speicherung von Werten, die aus API-Antworten zur Verwendung in späteren Schritten extrahiert werden.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-variablen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-variables"
}

Bei der Einrichtung eines [Multi-Step API Monitorings]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}}) werden Variablen in der Regel verwendet, um Werte aus den HTTP-Antworten zu extrahieren und sie vorübergehend zu speichern, sodass sie in einem später folgenden Schritt wiederverwendet werden können. Damit kannst du im Wesentlichen Schritte miteinander verbinden. Jedes Mal, wenn du eine Information aus einer HTTP-Antwort nimmst und diese Information verwenden möchtest, um die nächste HTTP-Anfrage auszuführen, benötigst du eine Variable. Einfacher gesagt: Schritt 1 erhält einen Wert von deinem Server und speichert ihn in einer Variable. Schritt 2 nimmt dann den soeben gespeicherten Wert und verwendet ihn, um eine neue Anfrage zu erstellen. Du kannst so viele Variablen nutzen, wie du magst, und in so vielen Schritten verwenden, wie du benötigst.

Ein zweiter Grund zum Einsatz von Variablen ist, bestimmte Werte nur einmal festzulegen und sie in mehreren Schritten zu verwenden. Normalerweise werden solche Werte im Abschnitt „Vordefinierte Variablen“ angegeben: Diese Variablen sind bei jedem Schritt in einem mehrstufigen Szenario verfügbar. Weitere Informationen findest du unter [Vordefinierte Variablen](#predefined-variables).

Alle in einem Schritt definierten Variablen werden bewertet, sobald die HTTP-Anfrage ausgeführt und die Antwort verarbeitet wurde. Zu diesem Zeitpunkt wird der vorhandene Wert einer bereits bestehenden Variable (entweder aus einem vorherigen Schritt oder weil sie zuvor festgelegt wurde) überschrieben. Andernfalls wird eine neue Variable erstellt und der Liste hinzugefügt. Diese Liste von Variablen und zugehörigen Werten wird dann im nächsten Schritt übernommen.

## Festlegen von Variablen

Wenn du Variablen verwenden möchtest, müssen wir wissen, welchen Wert wir in dieser Variable speichern sollen. Ähnlich dem Muster, wie Prüfpunkte definiert wurden, werden Variablen definiert:

{{< Code/Symbol type="source" >}}Quelle{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Eigenschaft{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}Variablenname{{< /Code/Symbol >}}

Zum Beispiel:

{{< Code/Symbol type="source" >}}Response Body als JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}access_token{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}access_token{{< /Code/Symbol >}}

-   **Variablenquelle**: Dieses Feld bestimmt, welches Attribut der HTTP-Antwort extrahiert wird. [Die verfügbaren Optionen werden in diesem Artikel erläutert]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="de" >}}).


-   **Variableneigenschaft**: Einige Quelloptionen für Variablen (insbesondere Inhaltsextraktion und Optionen in Bezug auf den Header) erfordern weitere Angaben hinsichtlich der zu prüfenden Inhalte und Header. Dies wird für jeden Quelltyp [detaillierter erläutert]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="de" >}}).
-   **Variablenname**: Dies ist die Kennung (Identifier) mit einer speziellen Notation, die in nachfolgenden Schritten verwendet wird, um sich auf diese Variable zu beziehen.

Wenn bei der Bewertung einer Variable ein Problem auftritt (zum Beispiel, weil du versuchst, einen Wert zu extrahieren, der in der Antwort nicht vorhanden ist), wird der Schritt nicht erfolgreich ausgeführt und meldet einen Fehler.

## Bezugnahme auf Variablen in anderen Schritten

Sobald eine Variable erfolgreich bestimmt wurde, kann ihr Wert in der Anfragedefinition in folgenden Schritten und innerhalb von Assertions (Prüfung des Antwortinhalts) wiederverwendet werden. Beziehe dich immer auf die Variable, indem du den Variablennamen in doppelte geschwungene Klammern setzt: {{< Code/Symbol type="variable" >}}{{variable-name}}{{< /Code/Symbol >}}.

-   In der URL eines Schritts: `https://myapi.customer.com/ProductInfo/{{ProductId}}`

-   In einem Anfrage-Header: `"Authorization": Bearer {{access_token}}`

-   Im Anfrage-Inhalt:

    `{ "ProductId": "{{ProductId}}", "Code": "P123456" }`

-   Im Zielwert einer Assertion (eines Prüfpunkts). Wenn du beispielsweise eine Variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}} (die in einem vorherigen Schritt mit einem Wert ausgefüllt wurde oder eine vordefinierte Variable ist) hast, kannst du sie verwenden, um zu prüfen, dass die Antwort tatsächlich den Wert der Variable enthält:

    {{< Code/Symbol type="source" >}}Response Body als JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products[0].Id{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Ist identisch mit{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}

-   Im Eigenschaftswert einer Assertion (eines Prüfpunkts). Hast du eine Variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}, kannst du dich auf diese Variable in einem JSON-Ausdruck oder einer XPath-Abfrage beziehen, um den Inhalt auszuwählen, den du verifizieren möchtest:

    {{< Code/Symbol type="source" >}}Response Body als XML{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}//Product[@Id="{{ProductId}}"]/Name/text(){{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Ist identisch mit{{< /Code/Symbol >}} `Chocolate chip cookie`

## Vordefinierte Variablen

Unter dem Step-Editor findest du einen Abschnitt, in dem du weitere Variablen angeben kannst. Diese Variablen werden direkt zu Beginn eines Szenarios verfügbar sein. Wenn du einen bestimmten Wert häufiger benötigst, kannst du diesen Wert vorher definieren und in anderen Schritten verwenden. Dabei kann es sich um eine Produkt-ID handeln, die durchgehend in einem Szenario verwendet werden soll, oder um besondere Werte, die deine API benötigt. Ein besonderer Fall ist eine Variable, die den Domainnamen für jede API speichert. Durch Einsatz dieser Variable als Teil jeder URL musst du sie nicht bei jedem Schritt wiederholen und kannst sie ganz einfach für das gesamte Szenario ändern. Um eine vordefinierte Variable hinzuzufügen, klicke auf {{< AppElement type="button" >}} \+ Variable hinzufügen {{< /AppElement >}} in den Prüfobjekteinstellungen im Abschnitt *Vordefinierte Variablen*.  Erstelle dann eine Variable namens `BaseUrl` mit dem Wert `https://test.yourapi.com`. Anhand einer Referenz zu dieser Variable könnte die URL für jeden API-Schritt die Form `{{BaseURL}}/UserService/GetUserInfo` annehmen. Mit dieser Herangehensweise kannst du ein mehrstufiges Szenario für eine andere Umgebung anpassen (zum Beispiel Testumgebung – Produktionsumgebung), ohne jeden Schritt ändern zu müssen.

Vordefinierte Variablen können auch für die Eingabe sensibler Daten verwendet werden, sollten diese zu irgendeinem Zeitpunkt bei der Prüfobjektausführung gesendet werden müssen. Wenn deine API beispielsweise eine Authentifizierung für den Zugang erfordert, muss das Prüfobjekt sich eventuell anmelden oder einen Zugriffs-Token abrufen, indem bei einer der Anfragen Anmeldedaten übermittelt werden. Sensible Daten werden [in der Vault]({{< ref path="/support/kb/account/vault" lang="de" >}})gespeichert. Führe folgende Schritte aus, um die Vault-Anmeldedaten für den Einsatz im Multi-Step API Monitoring einzurichten:

1. Stelle zunächst sicher, dass du die Anmeldedaten der [Vault hinzugefügt]({{< ref path="/support/kb/account/vault#ein-neues-element-zur-vault-hinzufügen" lang="de" >}}) hast.
2. Erstelle wie gewöhnlich und oben beschrieben die vordefinierte Variable.
3. Um dich auf ein Vault Item zu beziehen, klicke auf das [...]-Symbol unter **Wert**, wodurch sich das Fenster zur Werteauswahl öffnet.

![MSA Vault-Wertauswahl](/img/content/scr_MSA_predefined_variables_1.min.png)

4. Wähle das entsprechende Anmeldedaten-Set aus der Liste und wähle den Wert von entweder dem Benutzernamen- oder Passwort-Feld.
5. Gib der Variable einen angemessenen **Namen**, auf den du dich bei der Ausführung des Prüfobjekts wie in diesem Artikel beschrieben beziehst. Im Beispiel unten beziehen wir uns auf die Variable *examplePassword* mit `{{examplePassword}}`.

![MSA Vault-Wertauswahl](/img/content/scr-MSA-predefined-variables-example.min.png)

Im Prüfobjektprotokoll werden Werte, die dem Feld *Passwort* entnommen werden, als Sternchen dargestellt, um sensible Daten zu schützen.

![MSA Vault-Wertauswahl](/img/content/MSA_predefined_variables_result.png)

## Codierung von Variablenwerten

Abhängig vom „Einsatzort“ der Variablen müssen die Werte gelegentlich codiert werden. Codierung bedeutet, dass wir Sonderzeichen in ein Format konvertieren müssen, das für HTTP-Anfragen geeignet ist. Zum Beispiel müssen Variablen, die in einer URL verwendet werden, codiert werden. Stelle dir vor, du erzeugst eine URL, die einen Namensparameter enthält und du möchtest eine Variable {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} verwenden, um den Wert des Parameters anzugeben. Ohne Codierung würde dies so aussehen:

`https://my.api.com/GetCompanyInfo?name={{CompanyName}}`

Nehmen wir nun an, dass die Variable {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} den Wert `Ben & Jerry's` enthält. Dieser Wert enthält Leerzeichen und ein kaufmännisches „&“: beide haben eine besondere Bedeutung in einer URL. Ohne Codierung würde nicht der richtige Wert an den Server übermittelt. Setzt du also eine codierte Version des Werts ein, wird die Variable in `Ben\+%26\+Jerry's` konvertiert, was von dem Server wie der ursprüngliche Wert interpretiert wird. Um eine Codierung für deine Variablen anzuwenden, nutze die Funktion {{< Code/Symbol type="variable" >}}{{@UrlEncode(...)}}{{< /Code/Symbol >}}. Setze innerhalb der Klammern den vollständigen Variablennamen ein, zum Beispiel {{< Code/Symbol type="variable" >}}{{CompanyName}}{{< /Code/Symbol >}}. In einer URL würde es folgendermaßen aussehen:

`https://my.api.com/GetCompanyInfo?name={{@UrlEncode({{CompanyName}})}}`

Sollte eine Variable niemals Sonderzeichen enthalten (sondern beispielsweise nur numerische Werte), ist der Einsatz der Funktion @UrlEncode nicht notwendig. Variablen, die im Feld Anfrageinhalt (Request Body) eines Schritts verwendet werden, werden automatisch URL-codiert, jedoch nur, wenn ein Content-Type Header mit dem Wert application/x-www-form-urlencoded angegeben wurde. Andere Inhalte erfordern in der Regel kein URL-Codieren.

## Automatische Variablen

Abgesehen von den Variablen, die in der Prüfobjekteinrichtung definiert werden, hast du auch Zugang zu einer Anzahl automatischer Variablen, die wir für dich erzeugt haben. Die meisten sind tatsächlich Funktionen, die einen Wert generieren, den du in den HTTP-Anfragen und während der Bewertung von HTTP-Antworten anhand von Assertions nutzen kannst. Solltest du bei deinem Multi-Step API Monitoring automatische Variablen nutzen, findest du [hier unsere vollständige Liste verfügbarer automatischer Variablen]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="de" >}}).


## Benutzerdefinierte Funktionen

In bestimmten Fällen wird es erforderlich sein, eingehende Daten zu transformieren oder zuzuweisen, um ihre Bedeutung leichter zu erfassen. Uptrends bietet dir die Möglichkeit, benutzerdefinierte Funktionen einzurichten, die dann verwendet werden können, um Variablen (aus einem vorherigen Schritt oder aus einer von Uptrends bereitgestellten Systemvariable) in einen neuen Wert zu konvertieren. Weitere Informationen zur Einrichtung von benutzerdefinierten Funktionen findest du [hier in der Knowledge Base]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="de" >}}).

## Benutzerdefinierter Metrikvariablen

Jedes Mal, wenn das MSA-Prüfobjekt Daten von deinen APIs erfasst, kann es Fälle geben, in denen du bestimmte numerische Daten nachverfolgen möchtest, die nicht im Rahmen der Standardmetriken liegen, etwa den Antwort-Statuscode und die Antwortdauer, um das Verhalten deiner API zu beurteilen.

In solchen Fällen ermöglicht dir die benutzerdefinierte Metrikvariable, eine eigene Variable zu erzeugen, um numerische Daten, die von der API-Antwort erfasst wurden, zu speichern. Mehr zur Einrichtung einer benutzerdefinierten Metrikvariable findest du im Knowledge-Base-Artikel [Benutzerdefinierte API-Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#how-to-set-up-custom-api-monitoring" lang="de" >}}).