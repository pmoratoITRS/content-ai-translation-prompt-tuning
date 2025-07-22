{
  "hero": {
    "title": "Nachrichtenformatierung"
  },
  "title": "Nachrichtenformatierung",
  "summary": "Benutzerdefinierte Integrationen – Korrektes Formatieren deiner Nachrichten",
  "url": "/support/kb/alarme/integrationen/benutzerdefinierte-integrationen/nachrichtenformatierung",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/message-formatting" 
}

Da die ausgehenden Warnmeldungen meistens JSON-formatiert sind, müssen Regeln eingehalten werden, damit der JSON-Code gültig bleibt. Dafür müssen bestimmte Zeichen (wie Zeilenumbrüche oder Anführungszeichen) codiert werden, bevor sie in die ausgehende, JSON-formatierte Warnmeldung aufgenommen werden können. Erfolgt die Codierung nicht, würde das die JSON-Struktur der ausgehenden Nachricht zerstören, was dazu führen kann, dass der empfangene Endpunkt einen Fehler verzeichnet und die eingehende Warnmeldung nicht korrekt verarbeitet. Dieser Artikel behandelt die integrierten Funktionen zur automatischen Nachrichtenformatierung.


## Anwenden der automatischen Formatierung {id="applying-automatic-formatting"}


Wenn beispielsweise das Prüfobjekt-Feld „Anmerkungen“ (die du zu der Warnmeldung anhand der Systemvariable @monitor.notes hinzufügen kannst) solche Zeichen (Zeilenumbrüche, Anführungszeichen usw.) enthält, würde dies so aufgelöst, dass es die JSON-Struktur der ausgehenden Nachricht zerstört.

  
Beispiel: 
`{ "notes": "{{@monitor.notes}}" }`
Würde aufgelöst als:

```json
{ "notes": "Monitor notes that include 
 a line break or "a quote"" }`  
```

Damit ist die zuvor gültige JSON-Struktur zerstört und das wird wahrscheinlich zu einer nicht korrekten Verarbeitung der Warnmeldung am Empfangspunkt führen. Um dieses Problem zu beheben, haben wir die Möglichkeit eingerichtet, Textteile zu codieren (oder decodieren), damit sie korrekt in eine JSON- oder XML-formatierte Nachricht eingefügt werden können. Bei Nutzung dieser Funktion werden alle Zeichen, die mit einem Steuerzeichen versehen werden müssen, damit das JSON gültig bleibt, automatisch codiert.

  
Um diese Funktion zu nutzen, bette die gewünschte Systemvariable oder den gewünschten Text in die folgende Syntax:

`{{@JsonEncode(your-variable-here)}}`  

Beispielsweise sollte die zuvor erwähnte Systemvariable für Prüfobjekt-Anmerkungen wie folgt eingebettet sein:

`{ "Notes": "{{@JsonEncode({{@monitor.notes}})}}"}`  

Mit der `@JsonEncode`-Funktion wird der zuvor erwähnte JSON-enthaltende Hinweis auf die Prüfobjekt-Anmerkung nun folgendermaßen aufgelöst:

`{ "notes": "Monitor notes that include\na line break or \"a quote\"" }`  

Wie du siehst, sind die Prüfobjekt-Anmerkungen nun korrekt eingefügt und auf eine Weise codiert, mit der die JSON-Struktur erhalten bleibt.

  
Wenn du XML statt JSON verwendest – keine Sorge: Wir unterstützen eine ähnliche Funktion für das Codieren in XML! Du kannst diese Funktion anwenden, indem du die gewünschte Systemvariable in `{{@XmlEncode()}}` einbettest.


