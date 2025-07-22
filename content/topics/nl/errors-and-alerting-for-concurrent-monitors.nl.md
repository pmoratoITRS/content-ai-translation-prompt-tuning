{
  "hero": {
    "title": "Fouten en alerting bij gelijktijdige controleregels"
  },
  "title": "Fouten en alerting bij gelijktijdige controleregels",
  "summary": "Hoe werken het genereren van fouten en alerting bij gelijktijdige controleregels?",
  "url": "/support/kb/synthetic-monitoring/gelijktijdige-monitoring/fouten-en-alerting-gelijktijdige-controleregels",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors"
}

Vergeleken met standaard monitoring werkt de manier waarop fouten worden gegenereerd bij gelijktijdige controleregels net iets anders. Standaard monitoring volgt doorgaans een opeenvolging van *[OK (groen) – Onbevestigde fout (geel) – Bevestigde fout (rood)](/support/kb/alerting/fouten/onbevestigde-en-bevestigde-fouten)* voor het genereren van fouten, waarbij alerts worden gegenereerd na een gespecificeerd aantal bevestigde fouten voor een bepaalde controleregel. Bij gelijktijdige controleregels worden fouten echter anders gegenereerd. In dit artikel gaan we dieper in op hoe een gelijktijdige controleregel fouten genereert. Houd in gedachten dat nadat de fouten zijn gegenereerd, de alerting [op dezelfde manier werkt als bij standaard monitoring](/support/kb/alerting).

## Gelijktijdige grenswaarden voor fouten

Als u een gelijktijdige controleregel maakt (of een bestaande controleregel instelt op gelijktijdige modus), moet u twee nieuwe velden invullen: **Grenswaarde voor onbevestigde fout ** en **Grenswaarde voor bevestigde fout**. Bovendien moeten bij een gelijktijdige controleregel minimaal 3 controlestations met hoge beschikbaarheid worden geselecteerd of 5 controlestations uit de volledige set. Samen bepalen deze instellingen de omstandigheden waaronder de controleregelcheck de status OK, onbevestigde fout of bevestigde fout ontvangt. Kortom, een gelijktijdige controleregel rapporteert fouten wanneer het aantal controlestations dat individueel een fout detecteert de ingestelde grenswaarden overschrijdt.

Als voorbeeld bekijken we een Https-controleregel met een grenswaarde voor onbevestigde fout** ** van 30%, een grenswaarde voor bevestigde fout van 50% en 10 geselecteerde controlestations.

-   Onder normale omstandigheden retourneert elk van de geselecteerde controlestations afzonderlijk een OK-resultaat – geen van de controlestations die de test gelijktijdig uitvoeren detecteert een fout, wat betekent dat het foutpercentage 0 is. In dergelijke gevallen is het algehele resultaat van de gelijktijdige controleregel *OK*.
-   Als twee van de geselecteerde controlestations een fout detecteren, is het foutpercentage 20 (want 2/10 geselecteerde controlestations hebben een fout gedetecteerd). Omdat geen van beide grenswaarden is bereikt, wordt het algehele controleresultaat nog steeds als *OK* gerapporteerd.
-   In het geval dat vier van de geselecteerde controlestations fouten detecteren, wordt het foutpercentage 40. Dit overschrijdt de grenswaarde voor onbevestigde fout (30%), maar niet de grenswaarde voor bevestigde fout (50%). Het algehele controleresultaat is *onbevestigd* en zal daarom onder geen enkele omstandigheid alerting activeren.
-   Wanneer vijf (of meer) controlestations afzonderlijk een fout detecteren, bereikt of overschrijdt het foutpercentage de grenswaarde voor bevestigde fout. In dit geval wordt het algehele resultaat onmiddellijk geregistreerd als een *bevestigde* fout. Dat betekent dat dergelijke fouten alerts kunnen activeren, afhankelijk van de instellingen in uw alertdefinities.

In de onderstaande voorbeeldafbeelding ziet u dat twee van de zes geselecteerde controlestations (of \~ 33%) een fout hebben gerapporteerd. Dat overschrijdt de grenswaarde voor *onbevestigde* fout (25% in dit voorbeeld), maar niet de grenswaarde voor *bevestigde* fout (ingesteld op 50%). Dat betekent dat het algehele controleresultaat *onbevestigd* is en geen alerts zal genereren.

![](/img/content/5d220dc1-4e11-45a7-b13f-152bd67a10b1.png)

Anders gezegd: gelijktijdige monitoring voert geen dubbele controle uit zoals standaard controleregels doen. Een standaard controleregel zal bij het detecteren van een fout de test onmiddellijk opnieuw uitvoeren vanuit een andere controlestationlocatie om de fout te bevestigen. Bij gelijktijdige monitoring overtreffen we die robuustheid door de controle vanuit meerdere locaties tegelijkertijd uit te voeren. Als een bepaald aantal hiervan fouten meldt, is het veilig om aan te nemen dat de fout echt is.

{{< callout >}}
**Opmerking:** de afzonderlijke controleregelchecks volgen niet het gangbare foutschema* OK – Onbevestigd – Bevestigd*. In plaats daarvan zijn afzonderlijke controles ofwel *OK* (groen) of *Bevestigd* (rood). Aangezien de status van uw controleregel wordt bepaald op basis van de grenswaarden voor fouten die u hebt ingesteld, zal een individuele bevestigde fout op zichzelf geen alerting veroorzaken.
{{< /callout >}}

## Over downtime van controlestations

Aangezien ons [wereldwijde netwerk van controlestations](/controlestations) zeer uitgebreid is, is enige downtime onvermijdelijk. Voornamelijk vanwege regulier onderhoud, maar soms om andere redenen, kan het gebeuren dat bepaalde controlestations niet beschikbaar zijn voor het uitvoeren van uw controleregelcheck. Gebeurt dit bij een van de controlestations die u hebt geselecteerd voor uw gelijktijdige controleregel terwijl een controle wordt uitgevoerd, dan wordt bij het algehele controleresultaat een grijs **?** weergegeven voor dat specifieke controlestation. De individuele controle door dat controlestation zal *onduidelijk* zijn en niet worden meegerekend bij de berekening of het aantal fouten van de afzonderlijke controles de grenswaarden voor fouten overschrijdt.![](/img/content/052d85fc-3b36-448c-b4bd-e30431fe53a8.png)
