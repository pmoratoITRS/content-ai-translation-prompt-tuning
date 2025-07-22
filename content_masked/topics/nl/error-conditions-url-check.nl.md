{
  "hero": {
    "title": "Foutcondities - Controleer de URL's die door de pagina worden ingeladen"
  },
  "title": "Foutcondities - Controleer de URL's die door de pagina worden ingeladen",
  "summary": "Gebruik van de foutconditie 'Controleer URL's die door de pagina worden ingeladen'",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-url-controle",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Browsergebaseerde controleregeltypes, zoals [Full Page Check-]([LINK_URL_1]) en [Transactie-]([LINK_URL_2])controleregels laden uw pagina's in een echte browser. Bij het laden genereert de browser een [watervalgrafiek]([LINK_URL_3]) die alle elementen en resources weergeeft die op uw website zijn geladen.

Deze geladen elementen omvatten first-party-inhoud, zoals het originele HTML-document, afbeeldingen, video's en andere media die op hetzelfde netwerk worden gehost. Ze kunnen ook third-party-inhoud of externe resources bevatten, zoals monitoringscripts of analyses. Elk van deze elementen wordt afzonderlijk vermeld in de watervalgrafiek, met zijn eigen request-URL en laadtijdstatistieken.

## Foutconditie Controleer de URL's die door de pagina worden ingeladen

De [foutconditie]([LINK_URL_4]) **Controleer de URL's die door de pagina worden ingeladen** controleert of specifieke pagina-elementen worden geladen op uw website. Het controleert of de request-URL van deze elementen in de watervalgrafiek verschijnt of niet.

U wilt bijvoorbeeld controleren of de [Uptrends Real User Monitoring]([LINK_URL_5]) op een pagina wordt geladen. Het toevoegen van de foutconditie **Controleer de URL's die door de pagina worden ingeladen** vertelt de controleregel te controleren of de request-URL van een van de watervalelementen overeenkomt met [INLINE_CODE_1].

Bovendien kunt u met deze foutconditie specifieke criteria instellen voor het controleren van de statistieken van elke request-URL. Als u bijvoorbeeld fouten wilt detecteren wanneer uw [INLINE_CODE_2]-afbeelding langer dan 2 seconden nodig heeft om te laden of als een bestand een statuscode hoger dan 400 retourneert, kunt u voor elk criteria definiëren.

## Instellen van Controleer de URL's die door de pagina worden ingeladen

Om te controleren of een specifiek pagina-element zichtbaar is op uw website, moet u een foutconditie van het type **Controleer de URL's die door de pagina worden ingeladen** toevoegen:

1. Ga naar het menu [SHORTCODE_1] Monitoring > Controleregels beheren [SHORTCODE_2].
2. Klik op de controleregel waarvan u een request-URL wilt controleren.
3. Ga naar het tabblad [SHORTCODE_3] Foutcondities [SHORTCODE_4].
4. Klik in **Controleer de URL's die door de pagina worden ingeladen** op de knop [SHORTCODE_5] +Nieuwe controle [SHORTCODE_6].
5. Selecteer een fouttype om te bepalen of de controleregel een fout moet genereren wanneer de request-URL wel of niet in de watervalgrafiek verschijnt.
6. Geef de request-URL op in het tekstinvoerveld. U kunt reguliere expressies als waarden gebruiken.
7. (Optioneel) Als u aanvullende criteria wilt instellen voor het controleren van de request-URL, klikt u op de knop [SHORTCODE_7] +Extra conditie toevoegen [SHORTCODE_8]. Stel vervolgens uw condities in met de beschikbare opties:

  - Selecteer de **Grootte van de respons**, de juiste vergelijkingsoperator en de waarde in bytes (B).
  - Selecteer de **Totale tijd**, de juiste vergelijkingsoperator en de waarde in milliseconden (ms).
  - Selecteer de **Statuscode**, de juiste vergelijkingsoperator en de waarde.

8. Klik op de knop [SHORTCODE_9] Opslaan [SHORTCODE_10] om de wijzigingen in de controleregel op te slaan.

![Extra condities voor Controleer de URL's die door de pagina worden ingeladen]([LINK_URL_6])

## Voorbeelden

### Uptrends RUM-script laadt op de website

Het voorbeeld toont de foutconditie die controleert of het Uptrends RUM-script correct is geconfigureerd. Als de request-URL [INLINE_CODE_3]niet in de lijst met geladen pagina-elementen staat, genereert de controleregel [een fout]([LINK_URL_7]).

![Check URL: Uptrends RUM]([LINK_URL_8])

### Afbeelding laadt op de website

Het voorbeeld toont de foutconditie die controleert of de request-URL [INLINE_CODE_4] langer dan 1000 milliseconden in de lijst met geladen pagina-elementen verschijnt. Als de laadtijd van de URL de totale tijd overschrijdt, genereert de controleregel [een fout]([LINK_URL_9]).

![Check URL: Stars.[FILE_PATH_1]]([LINK_URL_10])