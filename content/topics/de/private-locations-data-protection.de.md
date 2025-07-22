{
  "hero": {
    "title": "Private Standorte – Datenschutz"
  },
  "title": "Private Standorte – Datenschutz",
  "summary": "Was sind die Vorkehrungen zum Datenschutz bei privaten Standorten?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-locations-datenschutz",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-data-protection"
}

Mit diesem Knowledge-Base-Artikel wird erläutert, wie du den Datenschutz bei deinen privaten Standorten bzw. Private Locations einrichtest. Eine der in Uptrends’ Private Locations eingerichteten Vorkehrungen verhindert den Upload von Screenshots in die Cloud. Du kannst auch Seiteninhalt deaktivieren, HTTP-Abfrage- und Antwort-Header sowie die aufgelösten IP-Adressen in den Prüfergebnissen verbergen.

## Die Docker Compose-Datei bearbeiten

Zuerst, sofern nicht schon geschehen, solltest du deinen Checkpoint gemäß den Schritten wie in [Einen Docker-Checkpoint installieren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}) aufgeführt, installieren.

1. Erstelle ein Back-up der extrahierten Docker Compose-Datei. Bitte beachte: Wenn du Änderungen an der bereitgestellten Compose-Datei vornimmst, erfolgt das auf dein eigenes Risiko. [Wende dich an den Support]({{< ref path="/contact" lang="de" >}}), wenn du nicht sicher bist.
2. Öffne die Datei docker-compose.yml und entferne den Kommentar-Tag ``#`` vor den Datenschutz-Variable(n) zum Checkpoint-Service, die du aktivieren möchtest. Indem du den Tag entfernst, wird der Datenschutz für die gewählte Umgebungsvariable aktiviert.


 ```
 Checkpoint:
    container_name: Checkpoint
    image: uptrends.azurecr.io/win2022/checkpoint
    depends_on:
      - TransactionProcessor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: "json-file"
      options:
        max-size: 10m
        max-file: "3"
    environment:
     - ServerId=
     - Password=
     - HasIpv6Support=false
#    - AllowScreenshotsInResults=false
#    - AllowPageContentInResults=false
#    - AllowHttpHeadersInResults=false
#    - AllowResolvedIpAddressesInResults=false
  
 ```    
3. Speichere deine Datei.
4. Starte den Container manuell durch Ausführen des Befehls ```docker-compose down``` neu, und führe dann ```docker-compose up``` in der Befehlszeile des Ordners aus, in dem die bearbeitete Compose-Datei abgelegt ist. Prüfe in der Uptrends Anwendung die geänderten Einstellungen unter [Datenschutzeinstellungen](#data-protection-settings-status) auf der Registerkarte {{< AppElement type="tab" >}} Checkpoint-Zustand {{< /AppElement >}}.
 
### Hochladen von (Fehler-)Screenshots und Filmstrips in die Cloud verhindern
Nachdem die Einstellung aktiviert ist, zeigen die **Kontrolldetails** in Uptrends einen Text, der dich darüber informiert, dass Screenshots aufgrund der Datenschutzrichtlinie des Unternehmens nicht erfasst werden.

Dies ist der Fall für alle Screenshots, einschließlich [Timeline-Screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="de" >}}) (auch Filmstrip genannt) und [Fehler-Screenshots]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="de" >}}) bei einem HTTP(S)-Prüfobjekt.

Um Screenshots bei den Ergebnissen zu deaktivieren, entferne den Tag ``#`` vor `- AllowScreenshotsInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.

{{< callout >}} **Wichtig**: Deaktivieren von Screenshots bedeutet genau das. Es werden keine Screenshots aufgenommen. Das heißt, für die [Fehlerbehebung]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#further-troubleshooting" lang="de" >}}) ist diese Art der Information dann nicht verfügbar.
 {{< /callout >}}

### Seiteninhalt deaktivieren 
Diese Einstellung stellt sicher, dass kein Inhalt in der [Seitenquelle und im Konsolenprotokoll]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="de">}}) angezeigt wird. Daten-URLs werden immer ohne Daten in den Ergebnissen angezeigt.

Um Seiteninhalt bei den Ergebnissen zu deaktivieren, entferne den Tag ``#`` vor `- AllowPageContentInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.

### HTTP-Anfrage- und -Antwort-Header verbergen
Nach Einrichtung dieser Einstellung, wird das Wasserfalldiagramm in den Kontrolldetails keine HTTP-Abfrage- und Antwort-Header zeigen.

Um HTTP-Abfrage- und Antwort-Header zu verbergen, entferne den Tag ``#`` vor `- AllowHttpHeadersInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.
![Datenschutz – HTTP Abfrage- und Antwort-Header in Wasserfalldiagramm nicht sichtbar](/img/content/scr-data-protection-waterfall-headers.min.png)

### Aufgelösten IP-Adressen für Request und Response Header verbergen
Diese Einstellung stellt sicher, dass der Berichts-Header bei einem Prüfergebnis keine aufgelösten IP-Adressen zeigt. Bitte beachte, dass dies nicht funktioniert, wenn es eine numerische IP-Adresse statt eines Domain-Werts im URL-Feld deines Prüfobjekts bzw. deiner Prüfobjekte gibt.

Um aufgelöste IP-Adressen zu verbergen, entferne den Tag ``#`` vor `- AllowResolvedIpAddressesInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.

### Aufgelöste IP-Adressen in Kontrolldetails deaktivieren 
Diese Einstellung stellt sicher, dass aufgelöste IP-Adressen nicht unter **Aufgelöste IP-Adresse** angezeigt werden.

Um aufgelöste IP-Adressen zu verbergen, entferne den Tag ``#`` vor `- AllowResolvedIpAddressesInResults=false` in der Liste der Checkpoint-Umgebungsvariablen. Speichere die Datei und starte den Docker-Container manuell neu, wie oben bei den Bearbeitungsanweisungen beschrieben, um die Änderungen zu den Datenschutzeinstellungen in der Uptrends Anwendung wiederzugeben.

DNS-Prüfobjekte werden an das Ausführen auf Checkpoint-Servern an deinen privaten Standorten gehindert, wenn dieser Wert auf „false“ gesetzt ist.

{{< callout >}} **Bitte beachten**: Nicht alle Einstellungen decken jeden Prüfobjekttyp ab. Zum Beispiel funktionieren für Basic HTTP(S)-Prüfobjekte nur Fehler-Screenshot-Einstellungen, die Einstellungen zu aufgelösten IP-Adressen gelten nicht für diesen Prüfobjekttyp.
{{< /callout >}}

## Status Datenschutzeinstellungen 

Die Registerkarte [Checkpoint-Zustand]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="de" >}}) in der Uptrends Anwendung zeigt den Status der Datenschutzeinstellungen. Ein rotes Kreuz besagt, dass Daten nicht angezeigt werden, ein Datenschutz also aktiviert ist. Beachte bitte, dass dies nur eine Anzeige ohne Bearbeitungsmöglichkeit ist. Die Einstellungen können nur in der Docker-Datei angepasst werden.

![Datenschutzeinstellungen auf der Registerkarte Checkpoint-Zustand](/img/content/scr_private-location-checkpoint-health-data-protected.min.png)