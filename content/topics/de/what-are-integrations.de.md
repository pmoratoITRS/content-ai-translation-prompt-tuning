{
  "hero": {
    "title": "Was sind Integrationen?"
  },
  "title": "Was sind Integrationen?",
  "summary": "Integrationen sind Verbindungen in die externe Welt, die das Senden von Warnmeldungen, die von Uptrends Monitoring ausgelöst wurden, übernehmen.",
  "url": "/support/kb/alarme/integrationen/was-sind-integrationen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/what-are-integrations"
}

Integrationen sind Verbindungen in die externe Welt, die das Senden von Warnmeldungen, die von Uptrends Monitoring ausgelöst wurden, übernehmen. Jedes Mal, wenn ein Check einen Alarm gemäß den Einstellungen der von dir eingerichteten Meldedefinitionen auslöst, sendet Uptrends die entsprechende Nachricht anhand der Integrationen, die du in den Meldedefinitionen aktiviert hast. Die einfachste Integration ist E-Mail. Eine E-Mail-Integration erstellt eine E-Mail-Nachricht und sendet sie an die angegebenen Empfänger. Ein weiteres einfaches Beispiel ist SMS. Eine SMS-Integration sendet SMS an die Mobiltelefone deiner Operator.

## Verbindung mit externen Systemen

Neben dem Senden von Warnmeldungen an einzelne Personen ist es wahrscheinlich, dass du Alarm-Informationen von Uptrends zur automatischen Verarbeitung an andere Systeme senden möchtest. Das Senden von Alarm-Informationen an automatisierte Prozesse ist nützlich, um direkt mit deinem System zum Verfolgen und Handhaben von Ereignissen (z. B. PagerDuty, Splunk On-Call oder ServiceNow) zu verbinden oder um Warnmeldungen im Kommunikationstool (z. B. in Slack) oder für die allgemeine Öffentlichkeit (z. B. StatusHub) zu veröffentlichen.

Einige der verfügbaren Integrationen verwenden ein festgelegtes Textformat (E-Mail, SMS, Telefon, Slack). Andere folgen dem Nachrichtenformat, dass vom Drittsystem erwartet wird, sodass das System die von Uptrends erhaltenen Daten nach eigenen Vorgaben anzeigen und verarbeiten kann (PagerDuty, StatusHub, Splunk On-Call, ServiceNow). Wir haben Leitfäden zur Integration aller unterstützten Drittsysteme. Die jeweiligen Integrationsleitfäden findest du auf unserer [Hauptseite zu Integrationen](/integrationen).

## Benutzerdefinierte Webhook-Integrationen

Obwohl die Liste der vordefinierten Integrationen von Uptrends ständig erweitert wird, kann es sein, dass dein System eventuell nicht aufgeführt ist. Es ist dennoch möglich, eine Verbindung zu solchen Systemen einzurichten – mit der Funktion für benutzerdefinierte Integrationen. Damit lässt sich eine Integration mit jedem System erreichen, dass Webhooks unterstützt, d. h. wenn es über eine API verfügt, die eingehende Nachrichten verarbeitet.

Wenn du eine Verbindung mit einem Drittsystem errichtest, erwartet das Drittsystem den eingehenden Webhook (d. h. die Daten, die von Uptrends an das System gesendet werden) in einem bestimmten Nachrichtenformat, um ihn verarbeiten zu können. Die Dokumentation des Systems erläutert den erforderlichen Content der Nachricht, einschließlich der Bedeutung jedes Felds und der URL, in der die Nachricht gesendet wird. Der Integrationseditor von Uptrends ermöglicht die Konfiguration aller benötigten Daten.

Möglicherweise verfügt aber das System, mit dem du verbinden möchtest, nicht über ein erforderliches Nachrichtenformat. In dem Fall ist es nützlich, die benutzerdefinierte Integration **Uptrends Integration** zu verwenden. Sie enthält eine vorkonfigurierte Nachricht mit allen verfügbaren Warnmeldungsvariablen von Uptrends. Du musst lediglich die URL der API eingeben, mit der du eine Verbindung errichten möchtest.

Weitere Informationen findest du im Artikel [Benutzerdefinierte Integrationen einrichten](/support/kb/alarme/integrationen/benutzerdefinierte-integrationen). Der Artikel ist auch hilfreich, wenn du eine der anpassbaren Integrationen ändern möchtest.
