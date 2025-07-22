{
  "hero": {
    "title": "Physischer Standort von Checkpoints"
  },
  "title": "Physischer Standort von Checkpoints",
  "summary": "Uptrends zeigt seine Checkpoint-Standorte so nah bei den physischen Standorten wie möglich, aber Tools zur Geolokalisation können die Checkpoint-Standorte falsch repräsentieren.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/physischer-standort-von-checkpoints",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/physical-location-of-checkpoints"
}

Ein einzelner Checkpoint-Standort besteht aus einem oder mehreren Servern in einem oder mehreren Datenzentren, die wir sowohl von lokalen wie auch internationalen Anbietern anmieten. Wir benennen die meisten Checkpoints mit dem Namen der nächsten Stadt zu dem Datenzentrum. Auf der [Checkpoints-Karte](/checkpoints) zeigen wir eher auf die Stadtmitte, nicht auf den genauen Standort. Wir möchten sicherstellen, dass der physische Standort jedes Servers korrekt ist. Daher verifizieren wir den Standort aktiv, indem wir die Distanz zu anderen Standorten prüfen (zum Beispiel anhand der Sprünge in einer Traceroute).

## Überlegungen bei der Nutzung von Ortungstools für IPs

Du kannst Tools im Internet finden, mithilfe derer du nach dem physischen Standort einer IP-Adresse suchen kannst. Die Anbieter solcher Tools verwenden mehrere Informationen, um den geografischen Standort zu bestimmen, aber mit unterschiedlichen Graden von Genauigkeit. Sei dir darüber klar, dass die von diesen bereitgestellten Informationen nicht immer 100 % genau sind. Einer der Gründe, weshalb diese Tools einen Standort falsch wiedergeben könnten, liegt darin, dass die Administratordaten der Adresse eines bestimmten Internetanbieters sich erheblich von der physischen Adresse unseres Datenzentrums unterscheiden können. Es kann sogar ein anderes Land dabei herauskommen. Gute IP-Ortungsservices bieten Genauigkeitsinformationen über ihre [Daten](https://www.maxmind.com/en/geoip2-city-database-accuracy).

## Noch Zweifel?

Wenn du noch Zweifel hinsichtlich des Standorts eines Checkpoints hast, kannst du eigene netzwerkbasierte Tests durchführen. Solltest du nicht zufriedenstellende Ergebnisse erhalten, zögere nicht, dich an [uns zu wenden](/contact).

{{< callout >}}
**Bitte beachten**: Wir können die von Anbietern geografischer Standortinformationen bereitgestellten Daten nicht ändern.
{{< /callout >}}
