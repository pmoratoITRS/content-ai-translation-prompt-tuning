{
  "title": "Ondersteuning voor Multi-part form is nu beschikbaar op MSA-controleregels",
  "date": "2025-01-08",
  "url": "[URL_BASE_CHANGELOG]januari-2025-msa-multi-part-form",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bij het [instellen van een Multi-step API-controleregel]([LINK_URL_1]) kunt u een payload (data die worden verzonden) opgeven als onderdeel van een requestdefinitie. Voorheen ondersteunde Uptrends alleen het verzenden van één type inhoud tegelijkertijd, ook al staat het HTTP-protocol toe dat meerdere onderdelen worden verzonden. Bijvoorbeeld het verzenden van zowel wat onbewerkte tekst als een binair bestand als onderdeel van één API-aanroep.

Met de nieuwe optie **Multi-part form** kunt u nu meerdere typen inhoud opnemen in de request body van uw MSA-stappen. Deze optie stelt de request header [INLINE_CODE_1] automatisch in op [INLINE_CODE_2] en laat u meerdere inhouden in verschillende typen specificeren. Deze typen kunnen plattetekstregels zijn of bestanden die zijn opgehaald uit de [Vault]([LINK_URL_2]).

![MSA Multi-part form]([LINK_URL_3])