{
  "title": "Nieuwe MSA-functie: Gegevensbescherming",
  "date": "2024-12-18",
  "url": "/changelog/december-2024-msa-gegevensbescherming-functie",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-data-protection-feature"
}

Uptrends verzamelt al uw MSA-monitoringresultaten van de Controlestationserver, die vervolgens direct worden opgeslagen en opgehaald op het Uptrends-platform.

Met de functie **Gegevensbescherming** kunt u uitsluiten dat specifieke monitoringinformatie wordt verzameld en opgeslagen op het Uptrends-platform. Deze functie biedt een extra beveiligingslaag die ervoor zorgt dat gevoelige informatie binnen uw netwerkomgeving blijft en niet extern wordt verzonden.

![Selectievakje MSA Gegevensbescherming](/img/content/scr-data-protection-checkbox.min.png)

Standaard zijn de volgende selectievakjes ingeschakeld, zodat Uptrends informatie kan opslaan en weergeven als onderdeel van uw MSA-monitoringresultaten:

- HTTP headers vastleggen — verzamelt de HTTP Request- en Response-headers van uw website.
- Response-inhoud vastleggen — verzamelt de HTTP Response-inhoud van uw website.
- Het resolved IP-adres vastleggen — verzamelt de verbindingsgegevens van het Resolved IP-adres van uw website.

Als u een van de selectievakjes uitschakelt, wordt voorkomen dat de bijbehorende informatie naar het Uptrends-platform wordt verzonden. In plaats daarvan wordt een informatieve tekst weergegeven.

Merk op dat de functie **Gegevensbescherming** al beschikbaar is in [Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}). We breiden deze implementatie nu uit naar ons publieke controlestationnetwerk, zoals MSA-monitoring.

