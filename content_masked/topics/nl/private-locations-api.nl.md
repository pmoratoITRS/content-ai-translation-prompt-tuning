{
  "hero": {
    "title": "Persoonlijke locaties-API"
  },
  "title": "Persoonlijke locaties-API",
  "summary": "De beschikbare API-methodes voor het manipuleren van persoonlijke locaties.",
  "url": "[URL_BASE_TOPICS]api/persoonlijke-locaties-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De Persoonlijke locaties-API bevat een reeks eindpunten die informatie verstrekken over de gezondheidsstatus en operationele status van uw geconfigureerde persoonlijke locaties. Met deze eindpunten kunt u de beschikbaarheid, performance en connectiviteit van elk controlestation monitoren.

## Gezondheid persoonlijke locatie en persoonlijk controlestation

De gezondheid van persoonlijke locaties en de gezondheid van persoonlijke controlestations zijn twee gerelateerde concepten die door elkaar kunnen worden gebruikt bij het werken met de API. Het eindpunt [INLINE_CODE_1] retourneert gezondheidgerelateerde informatie voor één specifiek controlestation binnen uw persoonlijke locatie. Het eindpunt [INLINE_CODE_2] daarentegen, biedt een overzicht van de gezondheidsstatus van alle individuele persoonlijke controlestations die aan een bepaalde persoonlijke locatie zijn gekoppeld. Zo kunt u elk controlestation afzonderlijk monitoren of een collectief beeld van hun algehele status krijgen.

## Serverinformatie

De API biedt gedetailleerde informatie over uw serverstatus, waaronder het volgende:

- Gezonde servers — het aantal volledig functionele servers zonder fouten of waarschuwingen.
- Ongezonde servers — het aantal servers met fouten, waarschuwingen of servers die niet correct zijn ingesteld.
- Aantal servers — het totale aantal servers dat draait in een persoonlijke locatie of op een specifiek controlestation.
- Naam controlestation — de naam van het controlestation dat aan de persoonlijke locatie is gekoppeld.
- Status — de huidige status van uw server: [INLINE_CODE_3], [INLINE_CODE_4] of [INLINE_CODE_5].
- Statusdetails — de datum en tijd waarop uw server voor het laatst actief was.
- Waarschuwingen — geeft de waarschuwingsinformatie weer, bijvoorbeeld of de server een update, installatie of andere aandacht vereist.

## Autorisatie

Met de API kunt u de gebruikersrechten voor persoonlijke locaties manipuleren. Met dit eindpunt kunt u controleren of uw autorisatietype bevoegd is om persoonlijke locaties te gebruiken of te bewerken. Raadpleeg [Rechten voor persoonlijke locaties instellen]([LINK_URL_1]) voor meer informatie over autorisaties.

Raadpleeg de Engelstalige [Uptrends Private locations API]([LINK_URL_2]) voor meer informatie.