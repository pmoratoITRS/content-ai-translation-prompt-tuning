{
  "hero": {
    "title": "Browsercache legen"
  },
  "title": "Browsercache legen",
  "summary": "Wanneer uw transactie pagina-elementen rechtstreeks vanaf de server opnieuw moet laden in plaats vanuit de opgeslagen cache, helpt het legen van de browsercache.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/browsercache-legen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends [transactiecontroleregels]([LINK_URL_1]) openen altijd een browser om gebruikersactiviteiten te simuleren om de prestaties van uw website te controleren. De browser start zonder data in de cache. Terwijl deze gebruikersactiviteiten uitvoert (zoals inloggen, door producten scrollen en toevoegen aan winkelwagen) op uw website, slaat hij tijdelijk cache op om al uw websiteresources te herkennen. Dit versnelt het laadproces van de browser de volgende keer dat die dezelfde pagina bezoekt.

Er zijn gevallen waarin u wilt verschillend paginagedrag wilt controleren bij het bezoeken van een pagina. Als u het gedrag van uw e-commercesite wilt vergelijken bij het laden van items in de winkelwagen voor bestaande gebruikers (met data in de cache) vergeleken met nieuwe bezoekers (zonder data in de cache), raden we u aan de browsercache te wissen.

## Actie Browsercache legen

De actie **Browsercache legen** in uw transactiestappen leegt de browsercache om pagina-elementen rechtstreeks vanaf de server opnieuw te laden in plaats vanuit de browsercache. Deze functie helpt u de prestaties van het eerste bezoek aan de website te controleren en zorgt ervoor dat UI-elementen (zoals afbeeldingen, tekst en andere front-end-elementen) correct worden geladen.

[SHORTCODE_1] **Opmerking:** Deze actie kost geen transactiecredits. Gebruik deze om uw monitoringbehoeften te verbeteren. Raadpleeg [Berekenen van credits voor transactiecontroleregels]([LINK_URL_2]) voor meer informatie. [SHORTCODE_2]

## Browsercache legen-actie toevoegen

Er zijn twee manieren om de actie **Browsercache legen** toe te voegen aan uw transactiestappen: de [Transactiestap-editor]([LINK_URL_3]) of de [Transactiescript-editor]([LINK_URL_4]).

### De Transactiestap-editor gebruiken

De actie **Browsercache legen** toevoegen in de **Transactiestap-editor**:

1. Ga naar [SHORTCODE_3] Transacties > Transacties beheren [SHORTCODE_4].
2. Klik op de transactiecontroleregel waaraan u de Browsercache legen-actie wilt toevoegen.
3. Ga naar het tabblad [SHORTCODE_5] Stappen [SHORTCODE_6].
4. Ga naar het **Stap**-gedeelte waaraan u de actie Browsercache legen wilt toevoegen.
5. Klik op de knop [SHORTCODE_7] Actie toevoegen [SHORTCODE_8].
6. In de pop-up **Actie toevoegen** selecteert u de optie **Browserscache legen**.
7. Klik op [SHORTCODE_9] Selecteren [SHORTCODE_10].
8. Geef in het veld **Instellingen > Omschrijving** een gedetailleerde beschrijving van de toegevoegde actie.
9. Klik op de knop [SHORTCODE_11] Opslaan [SHORTCODE_12] om de wijzigingen in de controleregel te bevestigen.

![Browsercache legen GIF]([LINK_URL_5])

### De Transactiescript-editor gebruiken

De actie **Browsercache legen** toevoegen in de **Transactiescript-editor**:

1. Ga naar [SHORTCODE_13] Transacties > Transacties beheren [SHORTCODE_14].
2. Klik op de transactiecontroleregel waaraan u de Browsercache legen-actie wilt toevoegen.
3. Ga naar het tabblad [SHORTCODE_15] Stappen [SHORTCODE_16].
4. Klik in de rechter bovenhoek van uw scherm op de knop [SHORTCODE_17] Naar script schakelen [SHORTCODE_18].
5. Voeg in het **Transactiescript** het volgende [INLINE_CODE_1]-fragment toe aan de [INLINE_CODE_2]-array:

[CODE_BLOCK_1]

6. Klik op de knop [SHORTCODE_19] Opslaan [SHORTCODE_20] om de wijzigingen in de controleregel te bevestigen.

**Browsercache legen** maakt nu deel uit van uw stappen en wordt elke keer uitgevoerd wanneer uw transactiecontroleregel wordt uitgevoerd.
