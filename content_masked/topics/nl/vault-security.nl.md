{
  "hero": {
    "title": "Vault-beveiliging"
  },
  "title": "Vault-beveiliging",
  "url": "[URL_BASE_TOPICS]account/vault-beveiliging",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Vault-beveiligingsfunctie

Uptrends zorgt ervoor dat alle gevoelige informatie in de **Vault** versleuteld en veilig opgeslagen wordt.

Telkens wanneer u een [Vaultitem]([LINK_URL_1]) creëert, worden al uw gevoelige gegevens automatisch versleuteld door de **Vault Engine** voordat ze in de database worden opgeslagen. De **Vault Engine** maakt gebruik van een cryptografiebibliotheek die voldoet aan de Advanced Encryption Standard (AES) voor gegevensversleuteling. Dit proces omvat verdere stappen die uitgevoerd moeten worden, zoals het genereren van encryptiesleutels voor elke Uptrends-omgeving.

Bovendien werkt Uptrends de wachtwoordzin strikt en regelmatig bij, waardoor het risico op aanvallen wordt geminimaliseerd en veilige toegang tot gevoelige gegevens mogelijk wordt gemaakt. Toegang tot deze protocollen wordt zorgvuldig gecontroleerd en geïmplementeerd, zodat gebruikers ervan verzekerd zijn dat geheimen verborgen en afgeschermd zijn voor Uptrends-medewerkers.

Als onderdeel van Uptrends-gegevensbeveiliging kunnen geheimen die zijn opgeslagen in de **Vault** niet worden opgehaald uit de Uptrends-webapplicatie of de [Vault API]([LINK_URL_2]). Als u een [set inloggegevens]([LINK_URL_3]) heeft, is alleen specifieke informatie zoals Vault-beschrijving, Vault Item Guid, Vault Section Guid, gebruikersnaam en andere toegankelijk. Verder geeft Uptrends geheimen weer als gemaskeerde waarden ([INLINE_CODE_1]). Deze waarden kunnen op elk moment worden bijgewerkt en verwijderd, maar worden in geen geval ontsleuteld of zichtbaar. 

Op dezelfde manier valideert Uptrends de [Gebruikersrechten]([LINK_URL_4]) en het gebruik van elk vault-item. Als u geen toegangsrecht heeft tot een vault-item dat in een controleregel wordt gebruikt, worden het bijwerken van de controleregelinstellingen en het gebruiken van de **Test starten**-functionaliteiten uitgeschakeld. Dit gedrag voorkomt dat onbevoegde gebruikers de waarde van het vault-item verzenden in situaties zoals het verzenden ervan naar externe eindpunten zoals webhook-sites. Dit houdt ook in dat gebruikers met toegang voornamelijk bepalen welke controleregels of eindpunten vault-items gebruiken. Daarom moet u er ook verantwoordelijk voor zijn dat u uw geheimen niet onbedoeld onthult.

Op deze manier worden al uw gevoelige gegevens beschermd tegen mogelijke risico's en kwetsbaarheden.