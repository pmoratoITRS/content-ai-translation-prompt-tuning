{
  "hero": {
    "title": "Checkpoint-Informationen"
  },
  "title": "Checkpoint-Informationen",
  "summary": "Was ist ein Checkpoint und wie wählst du die richtigen aus den vielen Checkpoints, die Uptrends für das Monitoring bietet?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/checkpoint-informationen",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/checkpoint-information"
}

Uptrends verfügt über ein enormes Netzwerk von weltweit über {{% Features/Variable variable="CheckpointCount" %}} Monitoring-Checkpoints, die konfiguriert werden können, um deine Websites, Server und Webservices zu überwachen, sodass du feststellen kannst, wo ein Problem seinen Ursprung hat.

## Was ist ein Checkpoint?

Ein Checkpoint ist ein geografischer Standort, an dem Verfügbarkeit und Performance deines Prüfobjekts regelmäßig geprüft werden. Jeder Checkpoint verfügt über einen oder mehrere Server in Datenzentren, um die Tests auszuführen. Diese Checkpoints nutzen hauptsächlich, sofern verfügbar, Domain Name System (DNS) Server, die von lokalen Internet-Service-Anbietern (Internet Service Providers, ISP), bereitgestellt werden, um tatsächliche Messungen und Ergebnisse zu gewährleisten.

## Liste der IP-Adressen von Uptrends Checkpoints

Sieh dir die vollständige, aktualisierte [Liste von Uptrends globalen Monitoring Checkpoints](/checkpoints), einschließlich IPv4 und IPv6 IP-Adressen, an.

Rufe die Listen [IPv4 Adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv4) und [IPv6 Adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv6) auf. Um die IP-Adressen in JSON- oder XML-Format herunterzuladen, lies den Knowledge-Base-Artikel [Checkpoint-Daten im JSON- und XML-Format abrufen]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/get-checkpoint-data-in-json-and-xml-format" lang="de" >}}).

## Mehrere Checkpoints

Mit der enormen Anzahl der in Uptrends verfügbaren Checkpoints kannst du flexibel unterschiedliche Standorte wählen, um tests auszuführen und die Prüfobjektergebnisse verifizieren.

Checkpoints können auch ein hervorragendes Tool sein, um:

- das Content Delivery Network (CDN) an vielen Endpunkten zu testen;
- das globale DNS-Netzwerk zu prüfen: Viele von Uptrends’ Checkpoints nutzen ein lokales DNS, sodass du siehst, ob deine DNS-Änderungen auf der ganzen Welt richtig umgesetzt werden;
- zu testen, ob Latenz durch Distanz oder Backbone-Anbieter innerhalb der akzeptablen Parameter liegen.

## Die richtigen Checkpoints auswählen

Die Auswahl mehrerer Checkpoints ist bereits in deinem Abonnement enthalten und birgt keine zusätzlichen Kosten. Uptrends empfiehlt, so viele Checkpoints wie möglich auszuwählen, da dies die Performance deines Prüfobjekts besser bewertet und während Wartungs- und Ausfallzeiten alternative Standorte bereitstellt.

Standardmäßig wählt Uptrends Checkpoint-Standorte weltweit, darunter Europa, Nordamerika, Afrika, Asien, Australien, Südamerika, und der Mittlere Osten. Es ist hilfreich, eine Checkpoint-Auswahl zu treffen, die sich umsichtig auf eine Zielregion ausrichtet.

Es müssen mindestens drei Checkpoints ausgewählt werden. Sollte aus irgendeinem Grund einer dieser Checkpoints zum Beispiel aufgrund einer Wartung nicht verfügbar sein, können mindestens zwei Checkpoints eine Prüfung ausführen und jeder Fehler wird von einem anderen Checkpoint bestätigt.

Auf der Registerkarte {{< AppElement type="tab" >}}Checkpoints{{< /AppElement >}} in der Prüfobjekteinrichtung kannst du die einzelnen Checkpoints aktivieren. Du kannst auch komplette Länder und Kontinente markieren. Solltest du ein Land oder einen Kontinent auswählen, werden alle neuen Checkpoints ebenfalls aktiviert, wenn wir zu der Region weitere Standorte hinzufügen. Deine Abdeckung wächst automatisch mit unserem Netzwerk! Selbst wenn du einzelne Checkpoints auslassen möchtest, kannst du immer noch die automatische Erweiterungsfunktion nutzen: Statt einzelne Checkpoints in einem Land auszuwählen und andere auszulassen, kannst du die Funktion [Ausschlüsse hinzufügen]({{< ref path="support/kb/synthetic-monitoring/checkpoints/checkpoint-exclusions" lang="de" >}}) nutzen, um eine abgestimmte Kontrolle über deine Checkpoints zu haben.

{{< callout >}}
**Hinweis:** Deine Optionen hängen vom Accounttyp ab. Bei unseren Paketen Starter, Premium und Professional erhalten Nutzer eine festgelegte Anzahl Checkpoints. Nutzer der Business oder Enterprise Version können jeden verfügbaren Checkpoint auswählen.
{{< /callout >}}

## Checkpoint-Ausfallzeit

Aufgrund lokaler Netzwerkproblem oder Wartungen kann es vorkommen, dass Checkpoint-Standorte vorübergehend nicht verfügbar sind. In Fällen, in denen alle deine gewählten Checkpoints nicht verfügbar sind, stellt Uptrends sicher, das die Prüfungen von einem Ausweichstandort abseits der von dir konfigurierten Checkpointstandorte ausgeführt werden. Wenn nur einige deiner gewählten Checkpoints nicht verfügbar sind, führt Uptrends die Prüfobjekte von deinen anderen gewählten Checkpoints aus.

Der Ausweichstandort ist standardmäßig in den {{< AppElement type="menuitem" >}} Account Einstellungen {{< /AppElement >}} > **Ausweich-Checkpoints** aktiviert. Das stellt sicher, dass Tests an anderen Standorten ausgeführt werden und nicht gefährdet sind. Sobald die Checkpoints wieder verfügbar sind, wechselt Uptrends automatisch zurück zu den Checkpoint-Einstellungen deines Prüfobjekts.

Es gibt bestimmte Fälle, an denen Ausweichstandorte nicht so gut funktionieren. Beispielsweise, wenn du eine Whitelist eingerichtet hast, in der nur bestimmte [Uptrends IP-Adressen](/checkpoints) genannt werden. Du hast die folgenden Möglichkeiten, das Problem zu beheben:

- Erhöhe die Anzahl ausgewählter Checkpoints, um das Risiko zu verringern, das Monitoring von nicht verfügbaren Checkpoint-Standorten auszuführen.

- Rufe {{< AppElement type="menuitem" >}} Account Einstellungen {{< /AppElement >}} auf und prüfe die Option **Ausweich-Checkpoints**. Deaktivieren der Option **Ausweich-Checkpoints** bedeutet, dass keine alternativen Standorte zur Prüfung deines Prüfobjekts herangezogen werden. Wenn dein Prüfobjekt einen Test startet und feststellt, dass der Checkpoint ausgefallen ist, wird die aktuelle Prüfung übersprungen. Dann beginnt das Prüfobjekt eine neue Prüfung mit dem nächsten [Intervall]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="de" >}}). Beachte, dass das Deaktivieren der Option zu Lücken in deinen Überwachungsergebnissen führen kann.

## Probleme mit einem Checkpoint?

Hast du ein Problem mit einem bestimmten Checkpoint? [Melde es uns]({{< ref path="contact" lang="de" >}})!

{{< callout >}}
**Hinweis:** Einige Tools zur geografischen Zuordnung von IP-Adressen aus dem Internet stellen den physischen Standort unserer Datenzentren nicht korrekt dar. [Mehr erfahren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/physical-location-of-checkpoints" lang="de" >}}) 
{{< /callout >}}
