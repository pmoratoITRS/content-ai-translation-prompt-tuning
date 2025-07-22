{
  "hero": {
    "title": "Operator API accountmanagement"
  },
  "title": "Operator API accountmanagement",
  "summary": "Geregistreerde API-gebruikers toevoegen aan of verwijderen uit een operator",
  "url": "[URL_BASE_TOPICS]account/gebruikers/operators/operator-API-management",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u [Uptrends' API]([LINK_URL_1]) wilt gebruiken, heeft u een API-account nodig (wat niet hetzelfde is als uw Uptrends-account). De inloggegevens van het API-account moeten worden ingevoerd met behulp van het *Basisauthenticatie*-schema voor het uitvoeren van een API call. Bekijk de informatie in [Gebruik van uw API-account]([LINK_URL_2]) over het invoeren van de inloggegevens bij het maken van API calls.

Op het tabblad [SHORTCODE_3] API management [SHORTCODE_4] van een operator kunt u alle API-accounts beheren die zijn gerelateerd aan een specifieke operator.

[SHORTCODE_1] **Opmerking**: U kunt geen wachtwoorden ophalen op het tabblad *API management* of elders in uw account. Zorg ervoor dat u de wachtwoorden noteert wanneer u een nieuw API-account maakt. [SHORTCODE_2]

## Een API-account toevoegen 

Een nieuwe API-account toevoegen aan een operator:

1. Ga naar [SHORTCODE_5] Accountinstellingen > Operators, groepen (en deelaccounts) [SHORTCODE_6].
2. Klik op de knop [SHORTCODE_7] Alle operators bekijken [SHORTCODE_8]. 
3. Klik in de lijst met operators op de operator waaraan u een API-account wilt toevoegen.
4. Ga naar het tabblad [SHORTCODE_9] API management [SHORTCODE_10].
5. Klik op de knop [SHORTCODE_11] API-gebruiker toevoegen [SHORTCODE_12].
6. Volg de wizard en noteer het wachtwoord. Het API-account wordt toegevoegd aan de lijst met API-gebruikers:

   ![screenshot tabblad API management van een operator]([LINK_URL_3])

7. Klik onderaan op de knop [SHORTCODE_13] Opslaan [SHORTCODE_14] om de wijzigingen aan de operator op te slaan.

Op het tabblad [SHORTCODE_15] API management [SHORTCODE_16] van een operator kunt u alle API-gebruikersaccounts zien die aan deze operator zijn gekoppeld. U kunt ook de aanmaakdatum zien en wanneer het account voor het laatst is gebruikt. De volgende opties kunnen worden weergegeven in de kolom *Laatst gebruikt*:

- **Onbekend** — wordt weergegeven wanneer het API-account is aangemaakt voordat de functionaliteit van "Laatst gebruikt" beschikbaar kwam.
- **Nog niet gebruikt** — betekent dat het API-account is gecreëerd na introductie van de functie "Laatst gebruikt", maar dat het account niet is gebruikt.
- **Datum/tijd** — het tijdstempel van het laatste gebruik van het API-account wordt weergegeven als het account is gecreëerd en gebruikt na introductie van de functie "Laatst gebruikt".

Merk op dat er een andere (oudere) manier is om een API-account toe te voegen door gebruik te maken van de /Register method van Uptrends' API. Deze methode wordt niet aanbevolen, omdat deze in de meeste situaties minder handig is. Dit werkt echter nog steeds en de instructies zijn te vinden in [Een API-account registreren]([LINK_URL_4]). Een account dat via de API wordt toegevoegd, verschijnt ook op het tabblad [SHORTCODE_17] API management [SHORTCODE_18] van een operator. 

 ## Een API-account verwijderen 

 Een API-account uit een operator verwijderen:

1. Ga naar [SHORTCODE_19] Accountinstellingen > Operators, groepen (en deelaccounts) [SHORTCODE_20].
2. Klik op de knop [SHORTCODE_21] Alle operators bekijken [SHORTCODE_22]. 
3. Klik in de lijst met operators op de operator waaruit u een API-account wilt verwijderen.
4. Ga naar het tabblad [SHORTCODE_23] API management [SHORTCODE_24].
5. Klik in de rij van het account dat u wilt verwijderen op de knop [SHORTCODE_25] API-gebruiker verwijderen [SHORTCODE_26].
6. Klik onderaan op de knop [SHORTCODE_27] Opslaan [SHORTCODE_28].
