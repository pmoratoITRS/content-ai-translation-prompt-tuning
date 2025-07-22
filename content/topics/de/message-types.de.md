{
  "hero": {
    "title": "Nachrichtentypen"
  },
  "title": "Nachrichtentypen",
  "summary": "Benutzerdefinierte Integrationen – Beschreibung der verschiedenen Nachrichtentypen",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/nachrichtentypen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/message-types" 
}

Es gibt unterschiedliche Typen von Alarmierungsnachrichten. Uptrends unterscheidet zwischen **Fehler**meldungen, **Erinnerungen** und **Ok**-Benachrichtigungen. Standardmäßig werden all diese Nachrichtentypen mit der gleichen Einrichtung erstellt. Wenn du jedoch eine benutzerdefinierte Integration einrichtest oder eine bestehende Integration anpasst, kannst du unterschiedliche Aktionssets für jeden einzelnen Nachrichtentyp erstellen.


## Fehlermeldungen, OK-Benachrichtigungen und Erinnerungen

Wenn du eine Nachrichtendefinition auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}} erstellst, verwendet Uptrends diese Nachrichtendefinition für alle Fehlertypen: eine Fehlermeldung, wenn der Check einen Alarm generiert, eine OK-Benachrichtigung, wenn der Check den Alarm aufgelöst hat und dazwischen Erinnerungen (abhängig von den Einstellungen der Eskalationsstufen).

Der Nachrichteninhalt ist praktisch derselbe für alle Alarmtypen, außer für die timestamp-Werte und die Variable {{@alert.type}}, die den Alarmtyp selbst ausgibt.

Obwohl derselbe Nachrichteninhalt in vielen Situationen ausreicht, ist er unzureichend, wenn du unterschiedliche Inhalte für verschiedene Alarmtypen benötigst oder wenn du ein neues Ereignis in deinem System (basierend auf einer Fehlermeldung) erstellen musst, das eine andere URL erfordert als die Auflösung desselben Ereignisses (basierend auf einer OK-Meldung).

### Unterschiedliche Nachrichten für verschiedene Alarmtypen

Um separate Nachrichtendefinitionen für Alarmierungstypen zu erstellen, klicke auf die Schaltfläche „Füge Schritte ein“ unten auf der Registerkarte {{< AppElement type="tab" >}}Anpassungen{{< /AppElement >}}. Die Schaltfläche „Füge Schritte ein“ erzeugt eine zusätzliche konfigurierbare Nachrichtendefinition, die beispielsweise nur für OK-Benachrichtigungen genutzt wird. Für jeden Alarmtyp kannst du die geeignete HTTP-Methode (GET/POST/PUT/PATCH/DELETE), URL, Header und Request Body (Anfrage) angeben.

Klicke auf die Kontrollkästchen *Fehler Alarm*, *OK Alarm* und *Erinnerungs-Alarm* über jeder Schritte-Definition, um die gewünschte Einrichtung zu erstellen. Du kannst jeden Alarmtyp einmal aktivieren, aber OK-Alarme und Erinnerungs-Alarme sind optional. Wenn du gar keine OK-Alarme oder Erinnerungen senden möchtest, belasse die Kontrollkästchen einfach deaktiviert.

### Fehler Alarme und OK Alarme gehören zusammen

Ob du separate Nachrichten für Fehler- und OK-Meldungen verwendest oder nicht – für das externe System ist es wahrscheinlich nützlich zu wissen, welche Alarme zusammengehören. Schließlich beginnt jedes Ereignis mit einer Fehlermeldung und endet mit einer OK-Benachrichtigung. Um dem externen System bei dieser Identifikation zu helfen, kannst du die Variable {{@incident.key}} in deinen Nachrichten verwenden. Fehlermeldungen und Ok-Benachrichtigungen haben denselben Ereignisschlüssel, aber jedes neue Ereignis hat einen einzigartigen Schlüssel. Bei einigen Systemen wird der Ereignisschlüssel als „Deduplication Key“ oder als „Ereignis-ID“ bezeichnet.

