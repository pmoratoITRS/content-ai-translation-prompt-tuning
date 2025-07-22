{
  "hero": {
    "title": "Den richtigen Nachrichteninhalt erzeugen"
  },
  "title": "Den richtigen Nachrichteninhalt erzeugen",
  "summary": "Benutzerdefinierte Integration – Erstellen deines Nachrichteninhalts",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/richtigen-nachrichteninhalt-erzeugen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/building-the-right-message-content" 
}

Um den entsprechenden Inhalt für die Felder in jeder ausgehenden Warnmeldung einzugeben, muss die von dir definierte Nachricht sogenannte **Systemvariablen** enthalten. Wenn du in deiner Nachricht auf eine Systemvariable verweist, wird sie durch den entsprechenden Inhalt ersetzt, wenn Uptrends eine Warnmeldung generiert. Der Einsatz von Systemvariablen ermöglicht dir, Nachrichtendefinitionen zu programmieren, die den Erwartungen des anderen Systems entsprechen. In diesem Artikel sehen wir uns an, wie du unterschiedliche Variablen einrichtest und in deinen ausgehenden benutzerdefinierten Integrationsnachrichten einsetzt. Wenn du verstehst, wie du Variablen in deiner benutzerdefinierten Integration nutzt, solltest du dir [die vollständige Liste verfügbarer Systemvariablen](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/warnmeldungen-systemvariablen) ansehen.

## Korrekter Einsatz von Variablen

Sehen wir uns ein Beispiel an: Eine augenscheinliche Information, die sicherlich Teil einer Warnmeldung sein sollte, ist die Klartext-Beschreibung des Fehlers, der von Uptrends identifiziert wurde. Nehmen wir an, das System, zu dem du eine Verbindung herstellen möchtest, verfügt über ein Feld namens „errordescription“. Du könntest die Fehlerbeschreibung von Uptrends in das Feld einfließen lassen, indem du diese Definition in deine JSON-formatierte Nachricht einfügst.

`{ "errordescription": "{{@alert.description}}" }`

Bei Uptrends‘ Systemvariablen steht der Beschreibungstext des Warnmeldungen auslösenden Fehlers in der Variable {{@alert.description}} bereit, sodass du einfach diese Variable dort in deine Nachricht schreibst, wo sie benötigt wird. Auf gleiche Weise kannst du {{@alert.timestamp}} verwenden, um auf den Zeitpunkt der Warnmeldung zu verweisen, {{@monitor.name}}, um den Prüfobjektnamen einzufügen usw. Alle verfügbaren Systemvariablen werden [in diesem Artikel der Knowledge Base](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/warnmeldungen-systemvariablen) aufgelistet.

{{< callout >}}**Tipp**: Du kannst an unterschiedlichen Stellen der benutzerdefinierten Integrationseinrichtung auf das [Credential Set (Anmeldedaten-Set) in der Vault](/support/kb/vault#anmeldedaten-credential-set) Bezug nehmen, etwa im Request Body, in der URL oder in Feldern zur Authentifizierung. Eine Beschreibung, wie du dies einrichtest, findest du im Kapitel [Ein Credential Set aus der Vault nutzen](/support/kb/synthetic-monitoring/api-monitoring/multi-step/#ein-credential-set-aus-der-vault-nutzen) in unserem Artikel zur Konfiguration von Multi-step API-Prüfobjekten. {{< /callout >}}


## Angeben von Variablen nach Eskalationsstufe

Wenn die Anpassungsoption bei einer Integration aktiv ist, kannst du eine oder mehrere Variablen für diese Integration auf der Registerkarte „Allgemein“ verwalten. Die Standardeinstellung für vordefinierte Integrationsvariablen (wie durch „Wert hier eintragen“ angezeigt) ist, dass der Wert für diese Variablen als fester Wert in der Integration definiert ist. Du kannst dann auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} in der Nachrichtendefinition auf diese Variablen verweisen. Weitere Informationen zur Definition und Verwendung von Variablen findest du im Artikel [Variablen im Multi-step API Monitoring](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variablen) in der Knowledge Base. Für Integrationen gilt der gleiche Ansatz.

Bei Integrationen verfügst du jedoch über eine weitere Option, die dir noch mehr Kontrolle gibt. Nehmen wir an, du hast eine Integration erstellt, die mit deinem IT-Managementsystem verbindet. Die Integration sendet Informationen aufgrund eines Prüfobjekts und eines Alarms, die eine Warnmeldung ausgelöst haben. Aber sind das ausreichend Informationen für das IT-Managementsystem, um entsprechende Maßnahmen zu aktivieren? Du kannst zusätzliche Informationen dazu senden, wie das neue Ereignis zu behandeln ist. Üblicherweise kannst du diese Information mit der Beantwortung der Frage „Wie sollte das Ereignis durch das externe System geleitet werden?“ ausdrücken: Verschiedene Meldedefinitionen (und damit auch jede Eskalationsstufe) können besondere Weiterleitungsinformationen bestimmen, die du in der ausgehenden Alarmierungsnachricht integrieren kannst.

Definiere hierfür auf der Registerkarte {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} der Integration eine Variable und wähle *Wert in Eskalations-Level definieren*. Beachte, dass du bei der Integration selbst keinen Wert mehr eintragen kannst. Stattdessen kannst du bei der Angabe der Integration in den Eskalationsstufen deiner Meldedefinitionen Werte für diese Variable angeben. Das hat den Vorteil, dass du nur eine einzige Integrationsdefinition für dein IT-Managementsystem erstellen musst, aber die Flexibilität in der Form behältst, dass alle Alarme dort gehandhabt werden.

## Externe IDs oder benutzerdefinierte Daten hinzufügen

Wenn du Uptrends in ein Fremdsystem integrierst, solltest du überlegen, ob eine Beziehung zwischen deinen Uptrends-Prüfobjekten und den im Fremdsystem von dir definierten Ressourcen (manchmal Komponenten oder Services genannt) besteht. Die Prüfobjekte in deinem Uptrends Account haben einen Namen und eine einzigartige Kennung (eine monitorGuid), die das Fremdsystem üblicherweise jedoch nicht kennt. Die im Fremdsystem definierten Ressourcen verfügen wahrscheinlich über eigene Kennungen, die wiederum Uptrends nicht kennt.

Wenn ein Prüfobjekt in Uptrends ein Ereignis für eine bestimmte Ressource auf der anderen Seite auslösen soll, musst du eine Art Beziehung zwischen den beiden definieren. In Uptrends kannst du diese Beziehung durch die Kennung (oder andere wichtige Informationen) der externen Ressource/Komponente definieren, indem du sie als benutzerdefinierten Wert in den Einstellungen eines Prüfobjekts eingibst.

Dann können die Alarmierungsdaten, die von Uptrends an das externe System gesendet werden, diese Kennung enthalten, sodass das empfangende System weiß, welche Ressource oder Komponente von der eingehenden Meldung betroffen ist.

Du kannst im Bereich „Metadaten“ auf der Registerkarte {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} eines Prüfobjekts benutzerdefinierte Felder hinzufügen. Neben dem externen Wert, den du speichern solltest, muss jedes benutzerdefinierte Feld auch einen einzigartigen Namen haben, sodass wir uns in der Alarmierungsnachricht darauf beziehen können. Beispielsweise könnte das Fremdsystem nach dem Komponenten-Konzept arbeiten und jede Komponente verfügt über eine ComponentId als einzigartige Kennung. Diese ComponentId solltest du dann in den Prüfobjekteinstellungen bei Uptrends angeben, sodass die beiden miteinander verknüpft werden können.

Scrolle dazu zum Bereich „Benutzerdefinierte Felder“ in den Einstellungen des Prüfobjekts. Füge ein benutzerdefiniertes Feld hinzu, indem du „ComponentId“ als Feldname und den entsprechenden externen ID-Wert (z. B. 7149488f-0b33-460d-85eb-210c0e80d7ba) als Feldwert eingibst. Klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}, um die neuen Einstellungen zu speichern.

Wir können nun sicherstellen, dass der externe Wert als Teil der Alarmierungsnachricht mitgesendet wird. Dazu fügen wir ihn in den Anfragetext (Request Body) der ausgehenden Nachricht ein. Du kannst auch die Funktion {{@CustomField()}} nutzen, um auf das gerade hinzugefügte benutzerdefinierte Feld zu verweisen. Du könntest beispielsweise dieses Fragment in den Request Body einfügen:

`{ "Component": "{{@CustomField(ComponentId)}}" }`

Beachte, wie der Feldname „ComponentId“ aus den Prüfobjekteinstellungen identisch im Funktionsaufruf @CustomField() eingefügt wurde. Wenn ein echter Alarm ausgelöst wird, wird der folgende Inhalt erzeugt:

`{ "Component": "7149488f-0b33-460d-85eb-210c0e80d7ba" }`

Das externe System kann diesen Wert verwenden, um ein Ereignis für die richtige Komponente zu melden. Dieses Beispiel hat nur ein benutzerdefiniertes Feld, aber du kannst bei Bedarf mehrere benutzerdefinierte Werte einsetzen.
