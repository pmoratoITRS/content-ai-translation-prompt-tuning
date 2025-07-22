{
  "hero": {
    "title": "API Monitoring – Übersicht"
  },
  "title": "API Monitoring – Übersicht",
  "summary": "Was ist das API Monitoring und wie kannst du es für dich nutzen?",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/api-uberwachung-im-uberblick",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/api-monitoring-overview",
  "sectionlist": false
}

Eine API (Application Programming Interface) ist eine Software, die eine Kommunikation zwischen Anwendungen ermöglicht. Möglicherweise nutzt du deine eigene API und/oder verlässt dich auf APIs Dritter. So oder so ist die richtige Funktionsweise der APIs grundlegend für den Betrieb deiner Website und Services und du solltest sie überwachen.

Das API Monitoring prüft, ob die APIs, auf die du dich verlässt, verfügbar, funktionstüchtig und leistungsstark sind. Weitere Informationen findest du im Artikel [Was ist API Monitoring?]({{< ref path="/what-is/api-monitoring" lang="de" >}}).

Das API Monitoring von Uptrends bietet unterschiedliche Prüfobjekttypen, um ein API Monitoring einzurichten. Die Typauswahl hängt davon ab, ob es sich um einen einzelnen Schritt oder eine Reihe von Anfragen mit mehreren Schritten handelt. Das Prüfobjekt für einen Schritt wird mit dem Prüfobjekttyp Webservice HTTP oder Webservice HTTPS eingerichtet. Das Prüfobjekt für eine Reihe aufeinanderfolgender Schritte wird anhand des Multi-Step API-Prüfobjekttyps (MSA-Prüfobjekt) definiert.

Die Uptrends Anwendung verfügt über einen [Multi-Step API-Prüfobjekt-Hub]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="de" >}}), bei dem du Informationen zu diesen Prüfobjekten und dem aktuellen Status an einem Ort findest.

## API-Prüfobjekte einrichten

Die Einrichtung unterschiedlicher Prüfobjekttypen wird in diesen Artikeln beschrieben:

- [Das Webservices-Monitoring einrichten]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="de" >}})
- [Das Web Services Monitoring (SOAP) einrichten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/setting-up-a-soap-web-service-probe" lang="de" >}})
- [Das Multi-Step Monitoring einrichten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="de" >}})
- [Das Postman-API-Monitoring einrichten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="de" >}})

## Schritte beim Multi-Step API Monitoring definieren

Bei der Einrichtung eines Multi-Step API-Prüfobjekts definierst du einen Schritt für jede HTTP-Anfrage, die Teil des zu überwachenden Szenarios ist. Für jeden Schritt gibt es zwei Aspekte zu bedenken: Zunächst gibst du die Daten für die Anfrage ein und definierst, was ausgeführt und an die API gesendet wird. Dann gibst du die Daten für die Antwort ein und definierst, was in der Antwort der API geprüft werden muss.

Sowohl die Anfrage- als auch Antwort-Teile für jeden Schritt können optional anhand [angepassten Skripten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}}) in Javascript erweitert werden. Du kannst deine eigenen Skripte für Authentifizierungen hinzufügen und Berechnungen und eigene Programmierungen ausführen, um die korrekte Funktion und den Inhalt der API-Schritte zu verifizieren.

Es gibt auch einige Definitionen für [benutzerdefinierte Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="de" >}}), [Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}}) und [benutzerdefinierte Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="de" >}}). Diese werden global festgelegt (verfügbar bei allen Schritten). In den Artikeln der folgenden Abschnitte erfährst du mehr über das Einrichten der HTTP-Schritte.

### Request

Der HTTP-Schritt Request (Anfrage) wird durch Angabe einer Methode und einer URL sowie des Request Bodys eingerichtet. Dann werden weitere Details wie zum Beispiel die Authentifizierung angegeben. Die Request-Definition kann auch mit eigenen Skripten weiter angepasst werden. Weitere Informationen findest du in den folgenden Artikeln:

-   [Authentifizierung]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="de" >}})
-   [Client-Zertifikate]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="de" >}})
-   [Uptrends' Client-Zertifikat]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="de" >}})
-   [Datei-Uploads bei der Multi-Step API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step#configuring-file-uploads" lang="de" >}})
- [Angepasste Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}})

### Response

Im Teil Response (Antwort) des Schritts solltest du Assertions (Prüfpunkte) definieren. Assertions sind Prüfungen, die weiter als die Frage gehen, ob es zu der Anfrage eine Antwort gibt. Eine Assertion prüft auch, ob die Antwort gültig ist oder zeitgerecht empfangen wird. Für jeden Schritt kannst du mehrere Assertions bestimmen. Neben der Definition von Assertions auf der Registerkarte Response kannst du vollständig angepasste Prüfungen und eigene Programmierungen mithilfe der Funktion für eigene Skripte einrichten. Weitere Informationen über Assertions findest du in diesen Artikeln:

-   [Assertions – Einführung]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="de" >}})
-   [Assertions – Quellen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="de" >}})
-   [Assertions – Vergleichsoperatoren]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-comparison-operations" lang="de" >}})
-   [Assertions – Beispiele mit XPath]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="de" >}})
-   [Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="de" >}})
-   [Handhabung von Redirects]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="de" >}})
- [Angepasste Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}})

### Globale Definitionen

Es gibt eine Reihe von Aspekten, die du für alle Schritte und sowohl für ihren Anfrage- wie auch den Antwortteil definieren kannst. Das kann praktisch sein, wenn du einen bestimmten Wert oder eine Funktion in unterschiedlichen Schritten verwenden möchtest. In den folgenden Artikeln findest du mehr dazu:

-   [Vordefinierte Variablen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined" lang="de" >}})
-   [Benutzerdefinierte Funktionen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="de" >}})
-   [Benutzerdefinierte Metriken]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="de" >}})
- [Hashing und Codierung]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/hashing-and-encoding" lang="de" >}})

### Die Skript-Ansicht

Du kannst Schrittdefinitionen des Multi-Step API-Prüfobjekts auch direkt in der *Skript-Ansicht* bearbeiten. Dieses Skript enthält die komplette Definition deiner Multi-Step API-Einrichtung, die du kopieren und an anderen Stellen einfügen kannst. Weitere Informationen findest du im Artikel zum [MSA Skript-Editor]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/msa-script-editor" lang="de" >}}).

Beachte, dass die *Skript-Ansicht* nicht dasselbe ist wie die Funktion [Angepasste Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="de" >}}), mit der du benutzerdefinierte Logik zu deinen Skripten hinzufügst.

## Credits

API-Prüfobjekte verwenden API-Credits, sodass du Prüfobjekte erstellen und ihre Ausführung planen kannst. Uptrends verwendet Credits, um den Preis unterschiedlicher Monitoring-Services zu berechnen. Weitere Informationen findest du im Knowledge-Base-Artikel zu [Credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="de" >}}).