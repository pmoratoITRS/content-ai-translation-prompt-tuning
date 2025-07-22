{
  "hero": {
    "title": "Benutzerdefinierte Integrationen testen"
  },
  "title": "Benutzerdefinierte Integrationen testen",
  "summary": "Benutzerdefinierte Integrationen – Ein Leitfaden zum Testen der Einrichtung einer benutzerdefinierten Integration",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/benutzerdefinierte-integrationen-testen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/testing-your-custom-integration" 
}

Sobald du eine benutzerdefinierte Integration geändert oder erstellt hast, macht es Sinn, sie zu testen, bevor sie aktiviert wird. Dieser Artikel stellt zwei Möglichkeiten zum Testen der neu eingerichteten Integration vor. Üblicherweise bedeutet ein erfolgreicher Test, dass du die eingehenden Daten im Fremdsystem, zu dem du eine Verbindung errichtet hast, korrekt analysiert oder verarbeitet siehst.

## Prüfen einer Integration anhand von Testnachrichten

Es ist möglich, neue Integrationen zu testen, indem du Uptrends fiktive Daten erzeugen lässt und diese an das Fremdsystem sendest. Auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} im Integrationseditor gibt es die Schaltfläche **Sende Test-Alarm**, mithilfe dessen du eine Testnachricht an das Fremdsystem unter Anwenden der/des von dir erstellten HTTPS-Schritte/s übermitteln kannst. Bei der Testfunktion kannst du wählen, welchen Alarmtyp (Fehler, OK oder Erinnerung) Uptrends für diese spezielle Testnachricht verwenden soll. Du kannst bei Bedarf alle sonstigen angemessenen Werte eingeben und die verbleibenden Daten (die in der Regel Prüfobjektdaten und Alarmdaten sind) werden mit fiktionalen Werten ausgefüllt.

Sobald Uptrends die Nachricht generiert und sie an das Fremdsystem oder die API sendet, wird der vollständige Nachrichtentext, der Antwortcode des Servers und der Inhalt angezeigt. Du kannst die Request Header und Inhalte und die Response Header und Inhalte einblenden, um den aus- und eingehenden Traffic, der beim Senden dieser Testnachricht entstanden ist, zu untersuchen.

## Prüfen einer Integration anhand von echten Daten

Die oben beschriebene Testfunktion ist nützlich für das statische Testen deiner Nachrichten und Variablen sowie um festzustellen, dass der Kommunikationskanal zum externen System richtig funktioniert. Aber du solltest auch verifizieren können, dass die Integration in der Produktion ebenfalls korrekt funktioniert.
  
Stelle zunächst sicher, dass eine deiner Meldedefinitionen tatsächlich deine Integration verwendet. Andernfalls wird Uptrends niemals die Integration anstoßen, Nachrichten auszusenden. Weitere Informationen zur Aktivierung von Integrationen in deiner Alarmierungseinrichtung findest du unter [Eskalationsstufen]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="de" >}}).
  
Dann muss ein Fehler auftreten, sodass dein Prüfobjekt einen tatsächlichen Alarm auslöst. Sobald du einen Alarm unter „Meldestatus“ oder im Dashboard „Alarmierungshistorie“ siehst, klicke darauf, um die Details zu dem Alarm anzuzeigen. Die Registerkarte {{< AppElement type="tab" >}}Details{{< /AppElement >}} führt alle wichtigen Eigenschaften des Alarms auf. Die Registerkarte {{< AppElement type="tab" >}}Nachrichten{{< /AppElement >}} enthält die benötigte Information, um den Nachrichten-Traffic zwischen Uptrends und dem externen System zu untersuchen.
  
Finde auf der Registerkarte {{< AppElement type="tab" >}}Nachrichten{{< /AppElement >}} die Integration, die du untersuchen möchtest. Es können auch andere Integrationen angezeigt werden, die ebenfalls von diesem Alarm angestoßen wurden. Erweitere den Integrationsbereich und die darin enthaltenen Anfragen und Antworten. Du siehst den vollständigen Inhalt der ausgehenden Nachricht(en), die vom externen System zurückgesendeten Antworten und jegliche Fehlermeldungen, wenn beim Senden des Alarms ein Problem aufgetreten ist.

