{
  "hero": {
    "title": "Foutcondities - Controleer de URL's die door de pagina worden ingeladen"
  },
  "title": "Foutcondities - Controleer de URL's die door de pagina worden ingeladen",
  "summary": "Gebruik van de foutconditie 'Controleer URL's die door de pagina worden ingeladen'",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-url-controle",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-url-check",
  "tableofcontents": true
}

Browsergebaseerde controleregeltypes, zoals [Full Page Check-]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) en [Transactie-]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}})controleregels laden uw pagina's in een echte browser. Bij het laden genereert de browser een [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}) die alle elementen en resources weergeeft die op uw website zijn geladen.

Deze geladen elementen omvatten first-party-inhoud, zoals het originele HTML-document, afbeeldingen, video's en andere media die op hetzelfde netwerk worden gehost. Ze kunnen ook third-party-inhoud of externe resources bevatten, zoals monitoringscripts of analyses. Elk van deze elementen wordt afzonderlijk vermeld in de watervalgrafiek, met zijn eigen request-URL en laadtijdstatistieken.

## Foutconditie Controleer de URL's die door de pagina worden ingeladen

De [foutconditie]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}) **Controleer de URL's die door de pagina worden ingeladen** controleert of specifieke pagina-elementen worden geladen op uw website. Het controleert of de request-URL van deze elementen in de watervalgrafiek verschijnt of niet.

U wilt bijvoorbeeld controleren of de [Uptrends Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="nl" >}}) op een pagina wordt geladen. Het toevoegen van de foutconditie **Controleer de URL's die door de pagina worden ingeladen** vertelt de controleregel te controleren of de request-URL van een van de watervalelementen overeenkomt met `hit.uptrends.com/.*`.

Bovendien kunt u met deze foutconditie specifieke criteria instellen voor het controleren van de statistieken van elke request-URL. Als u bijvoorbeeld fouten wilt detecteren wanneer uw `uptrends.png`-afbeelding langer dan 2 seconden nodig heeft om te laden of als een bestand een statuscode hoger dan 400 retourneert, kunt u voor elk criteria definiëren.

## Instellen van Controleer de URL's die door de pagina worden ingeladen

Om te controleren of een specifiek pagina-element zichtbaar is op uw website, moet u een foutconditie van het type **Controleer de URL's die door de pagina worden ingeladen** toevoegen:

1. Ga naar het menu {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de controleregel waarvan u een request-URL wilt controleren.
3. Ga naar het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}}.
4. Klik in **Controleer de URL's die door de pagina worden ingeladen** op de knop {{< AppElement type="buttonSecondary" >}} +Nieuwe controle {{< /AppElement >}}.
5. Selecteer een fouttype om te bepalen of de controleregel een fout moet genereren wanneer de request-URL wel of niet in de watervalgrafiek verschijnt.
6. Geef de request-URL op in het tekstinvoerveld. U kunt reguliere expressies als waarden gebruiken.
7. (Optioneel) Als u aanvullende criteria wilt instellen voor het controleren van de request-URL, klikt u op de knop {{< AppElement type="buttonSecondary" >}} +Extra conditie toevoegen {{< /AppElement >}}. Stel vervolgens uw condities in met de beschikbare opties:

  - Selecteer de **Grootte van de respons**, de juiste vergelijkingsoperator en de waarde in bytes (B).
  - Selecteer de **Totale tijd**, de juiste vergelijkingsoperator en de waarde in milliseconden (ms).
  - Selecteer de **Statuscode**, de juiste vergelijkingsoperator en de waarde.

8. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel op te slaan.

![Extra condities voor Controleer de URL's die door de pagina worden ingeladen](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

## Voorbeelden

### Uptrends RUM-script laadt op de website

Het voorbeeld toont de foutconditie die controleert of het Uptrends RUM-script correct is geconfigureerd. Als de request-URL `hit.uptrends.com/.*`niet in de lijst met geladen pagina-elementen staat, genereert de controleregel [een fout]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}}).

![Check URL: Uptrends RUM](/img/content/scr-error-conditions-url-check.min.png)

### Afbeelding laadt op de website

Het voorbeeld toont de foutconditie die controleert of de request-URL `stars.png` langer dan 1000 milliseconden in de lijst met geladen pagina-elementen verschijnt. Als de laadtijd van de URL de totale tijd overschrijdt, genereert de controleregel [een fout]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}}).

![Check URL: Stars.png](/img/content/scr-error-conditions-url-check-image.min.png)