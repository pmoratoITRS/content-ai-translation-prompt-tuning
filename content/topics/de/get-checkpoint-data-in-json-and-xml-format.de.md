{
  "hero": {
    "title": "Checkpoint-Daten im JSON- und XML-Format abrufen"
  },
  "title": "Checkpoint-Daten im JSON- und XML-Format abrufen",
  "summary": "Wenn du die Uptrends API nutzt, um Checkpoint-Informationen abzurufen, kannst du diese Informationen in unterschiedlichen Formaten erhalten.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/checkpoint-daten-in-json-und-xml-format-abrufen",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/get-checkpoint-data-in-json-and-xml-format",
  "TableOfContents": false
}

JSON- und XML-Downloads von Checkpoint-Daten sind über unsere API verfügbar. Die vollständige Dokumentation für diese API findest du [hier]({{< ref path="support/kb/api" lang="de" >}}).

Du kannst unsere API verwenden, um eine Liste aller IPv4- oder IPv6-Adressen für alle Checkpoints von Uptrends abzurufen, darunter zukünftige Adressen geänderter oder neuer Checkpoints. Antworten sind sowohl als JSON wie auch als XML, abhängig von deinem `Accept` Header verfügbar.

Wir halten auch einfache Listen von [IPv4-Adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv4) und [IPv6-Adressen]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv6) zum Download bereit.

Alle auf dieser Seite genannten Methoden und Links liefern eine Liste von Checkpoint-IP-Adressen, die auch **zukünftige Adressen** umfassen (wie in unserem monatlichen Newsletter angekündigt).

#### Liste der IPv4-Adressen:
Sende eine GET-Abfrage mit dem Header `Accept: application/json` an `https://api.uptrends.com/v4/Checkpoint/Server/Ipv4`. Eine Authentifizierung ist nicht erforderlich.

Wenn du *Curl* nutzt, wäre ein Beispiel:
```
curl -X GET -H "accept: application/json" https://api.uptrends.com/v4/Checkpoint/Server/Ipv4
```

Ersetze *application/json* durch *application/xml*, wenn du eine XML-Antwort benötigst.

#### Liste der IPv6-Adressen: 
Es gilt dasselbe wie für IPv4, die Abfrage sollte aber an `https://api.uptrends.com/v4/Checkpoint/Server/Ipv6` gesendet werden.


{{< callout >}}
**Tipp**: Statt *Curl* kannst du ein Powershell Invoke-Webrequest nutzen.
{{< /callout >}}
