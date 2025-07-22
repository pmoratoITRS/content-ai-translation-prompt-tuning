{
  "hero": {
    "title": "Browsercache legen"
  },
  "title": "Browsercache legen",
  "summary": "Wanneer uw transactie pagina-elementen rechtstreeks vanaf de server opnieuw moet laden in plaats vanuit de opgeslagen cache, helpt het legen van de browsercache.",
  "url": "/support/kb/synthetic-monitoring/transactions/browsercache-legen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/clear-browser-cache"
}

Uptrends [transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}) openen altijd een browser om gebruikersactiviteiten te simuleren om de prestaties van uw website te controleren. De browser start zonder data in de cache. Terwijl deze gebruikersactiviteiten uitvoert (zoals inloggen, door producten scrollen en toevoegen aan winkelwagen) op uw website, slaat hij tijdelijk cache op om al uw websiteresources te herkennen. Dit versnelt het laadproces van de browser de volgende keer dat die dezelfde pagina bezoekt.

Er zijn gevallen waarin u wilt verschillend paginagedrag wilt controleren bij het bezoeken van een pagina. Als u het gedrag van uw e-commercesite wilt vergelijken bij het laden van items in de winkelwagen voor bestaande gebruikers (met data in de cache) vergeleken met nieuwe bezoekers (zonder data in de cache), raden we u aan de browsercache te wissen.

## Actie Browsercache legen

De actie **Browsercache legen** in uw transactiestappen leegt de browsercache om pagina-elementen rechtstreeks vanaf de server opnieuw te laden in plaats vanuit de browsercache. Deze functie helpt u de prestaties van het eerste bezoek aan de website te controleren en zorgt ervoor dat UI-elementen (zoals afbeeldingen, tekst en andere front-end-elementen) correct worden geladen.

{{< callout >}} **Opmerking:** Deze actie kost geen transactiecredits. Gebruik deze om uw monitoringbehoeften te verbeteren. Raadpleeg [Berekenen van credits voor transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) voor meer informatie. {{< /callout >}}

## Browsercache legen-actie toevoegen

Er zijn twee manieren om de actie **Browsercache legen** toe te voegen aan uw transactiestappen: de [Transactiestap-editor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}) of de [Transactiescript-editor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}).

### De Transactiestap-editor gebruiken

De actie **Browsercache legen** toevoegen in de **Transactiestap-editor**:

1. Ga naar {{< AppElement type="menuitem" >}} Transacties > Transacties beheren {{< /AppElement >}}.
2. Klik op de transactiecontroleregel waaraan u de Browsercache legen-actie wilt toevoegen.
3. Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}}.
4. Ga naar het **Stap**-gedeelte waaraan u de actie Browsercache legen wilt toevoegen.
5. Klik op de knop {{< AppElement type="editbutton" >}} Actie toevoegen {{< /AppElement >}}.
6. In de pop-up **Actie toevoegen** selecteert u de optie **Browserscache legen**.
7. Klik op {{< AppElement type="buttonCta" >}} Selecteren {{< /AppElement >}}.
8. Geef in het veld **Instellingen > Omschrijving** een gedetailleerde beschrijving van de toegevoegde actie.
9. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel te bevestigen.

![Browsercache legen GIF](/img/content/gif-transaction-clear-browser-cache.gif)

### De Transactiescript-editor gebruiken

De actie **Browsercache legen** toevoegen in de **Transactiescript-editor**:

1. Ga naar {{< AppElement type="menuitem" >}} Transacties > Transacties beheren {{< /AppElement >}}.
2. Klik op de transactiecontroleregel waaraan u de Browsercache legen-actie wilt toevoegen.
3. Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}}.
4. Klik in de rechter bovenhoek van uw scherm op de knop {{< AppElement type="editbutton" >}} Naar script schakelen {{< /AppElement >}}.
5. Voeg in het **Transactiescript** het volgende `clearCache`-fragment toe aan de `actions`-array:

```json
    {
      "clearCache": {
        "description": "Geef hier een stapbeschrijving"
      }
    },
```

6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel te bevestigen.

**Browsercache legen** maakt nu deel uit van uw stappen en wordt elke keer uitgevoerd wanneer uw transactiecontroleregel wordt uitgevoerd.
