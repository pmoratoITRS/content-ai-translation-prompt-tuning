{
  "hero": {
    "title": "Problemen met SMS oplossen"
  },
  "title": "Problemen met SMS oplossen",
  "summary": "MS-alerts zijn een heel goede manier om op de hoogte te blijven van de status van uw website, servers en webservices.",
  "url": "[URL_BASE_TOPICS]alerting/sms-problemen-oplossen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**SMS-alerts** zijn een heel goede manier om op de hoogte te blijven van de status van uw website, servers en webservices. Als uw SMS-alerts niet worden ontvangen, dan is dat wel een probleem!

Hieronder vindt u een reeks opties voor het oplossen van SMS-problemen:

## Extra afzenders wijzigen

Als u geen test-SMS-berichten kunt ontvangen, kunt u het volgende proberen aan te passen in de Uptrends-webapplicatie. Volg hiervoor deze stappen:

1. Klik linksonder in uw scherm op [SHORTCODE_1] Uw profielnaam > Gebruikersinstellingen [SHORTCODE_2].
2. Scrol op het tabblad [SHORTCODE_3] Algemeen [SHORTCODE_4] naar [SHORTCODE_5] Telefooninstellingen > SMS aanbieder [SHORTCODE_6].
3. Kies de optie **Overschrijf SMS-integratie-instellingen** om de volgende velden te bewerken.
4. Selecteer een gatewayprovider in het keuzemenu. Momenteel bieden we 4 verschillende providers waaruit u kunt kiezen:

- SMS Gateway in Europa
- SMS Gateway 2 in Europa
- SMS Gateway in VS
- Internationale SMS Gateway

5. Vink de optie **Gebruik numerieke afzender** aan.

Sommige providers hebben problemen met het ontvangen van berichten van numerieke afzenders of van alfabetische afzenders. Standaard gebruiken we een alfabetische afzender.

## Deblokkeren via uw provider

### SPRINT

Standaard kunnen sommige telefoonnummers van SPRINT-gebruikers geblokkeerd zijn. Geen paniek! Er is een manier om zelf uw nummer te deblokkeren: SMS **UPTRENDS** naar **46786**.

Als deze actie *succesvol* is, ontvangt u nu SMS-berichten zoals geconfigureerd in uw account.

Als deze poging *mislukt*, neem dan contact op met uw provider om de blokkering uit uw account te laten verwijderen.

### AT&T

Sommige AT&T-gebruikers kunnen standaard problemen hebben met het ontvangen van SMS-berichten, maar u kunt uw nummer deblokkeren: SMS **UPTRENDS** naar **64085**.

Als dit *niet werkt*, neem dan contact op met uw provider en laat hen de blokkering uit uw account verwijderen.

## Bekende SMS-problemen voor operators 

### China en India

Vanwege spamfilters in China en bel-me-niet-registers in India werkt SMS-alerting mogelijk niet voor operators in deze landen. [Lees meer]([LINK_URL_1]).

## Lijst met ondersteunde landen en providers met afzender-ID

Bekijk de Uptrends-lijst met ondersteunde landen en gatewayproviders. De kolom *Numeriek ingeschakeld* geeft aan of het selectievakje *Numerieke afzender gebruiken* in de Uptrends-webapplicatie kan worden ingeschakeld of uitgeschakeld.

Als er  *Ja* staat, kunt u het selectievakje *Numerieke afzender gebruiken* aanvinken om de SMS van een mobiel telefoonnummer te ontvangen. Anders ontvangt u de SMS van het contact **UPTRENDS**. Als zowel *Ja* als *Nee* opties zijn, kiest u degene die het beste bij uw behoeften past.

| Telefooncode | Land | Gateway | Numeriek ingeschakeld |
|--|--|--|--|
| +1 | Verenigde Staten | Gateway gevestigd in de VS of Internationaal | Ja en Nee |
| +33 | Frankrijk | Gateway 2 gevestigd in Europa | Ja en Nee |
| +40 | Roemenië | Gateway 2 gevestigd in Europa | Ja |
| +44	| Verenigd Koninkrijk | Gateway 2 gevestigd in Europa | Nee |
| +45	| Denemarken	| Gateway 2 gevestigd in Europa | Nee |
| +46 | Zweden | Gateway 2 gevestigd in Europa | Nee |
| +47 | Noorwegen | Gateway 2 gevestigd in Europa | Nee |
| +65 |	Singapore | Gateway 2 gevestigd in Europa | Nee |
| +90 |	Turkije | Gateway 2 gevestigd in Europa | Nee |
| +91	| India	| Gateway 2 gevestigd in Europa | Nee |
| +358 | Finland	| Gateway 2 gevestigd in Europa	| Nee |
| +381 |Servië |Gateway 2 gevestigd in Europa	| Nee |
| +421 | Slowakije | Gateway 2 gevestigd in Europa	| Nee |
| +998 | Oezbekistan | Gateway 2 gevestigd in Europa	| Nee |

#### Nog steeds problemen?

Als u deze opties voor het oplossen van problemen met SMS heeft geprobeerd maar nog steeds geen alerts kunt ontvangen, neem dan contact op met support door een [ticket in te dienen]([LINK_URL_2]).
