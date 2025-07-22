{
  "title": "Ondersteuning voor Multi-part form is nu beschikbaar op MSA-controleregels",
  "date": "2025-01-08",
  "url": "/changelog/januari-2025-msa-multi-part-form",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-msa-multi-part-form"
}

Bij het [instellen van een Multi-step API-controleregel]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}}) kunt u een payload (data die worden verzonden) opgeven als onderdeel van een requestdefinitie. Voorheen ondersteunde Uptrends alleen het verzenden van één type inhoud tegelijkertijd, ook al staat het HTTP-protocol toe dat meerdere onderdelen worden verzonden. Bijvoorbeeld het verzenden van zowel wat onbewerkte tekst als een binair bestand als onderdeel van één API-aanroep.

Met de nieuwe optie **Multi-part form** kunt u nu meerdere typen inhoud opnemen in de request body van uw MSA-stappen. Deze optie stelt de request header `Content-Type` automatisch in op `multipart/form-data` en laat u meerdere inhouden in verschillende typen specificeren. Deze typen kunnen plattetekstregels zijn of bestanden die zijn opgehaald uit de [Vault]({{< ref path="/support/kb/account/vault" lang="nl" >}}).

![MSA Multi-part form](/img/content/scr-multi-part-form-msa.min.png)