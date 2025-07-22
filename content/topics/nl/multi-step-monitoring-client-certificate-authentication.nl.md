{
  "hero": {
    "title": "Multi-step Cliëntcertificaten monitoren"
  },
  "title": "Monitoring van Multi-step Cliëntcertificaat-authenticatie",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-clientcertificaten-monitoren",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-client-certificate-authentication"
}

Veel API's vereisen dat de caller authenticatie-informatie verstrekt om hun identiteit te verifiëren en mogelijk de toegangsrechten van die caller. Authenticatie-informatie kan worden doorgegeven met behulp van HTTP headers (Basic/NTLM/Digest-authenticatie), door uitwisselen van access tokens (OAuth), door van de cliënt te eisen een cliëntcertificaat op te nemen in de request, of een combinatie hiervan.

In dit artikel worden de opties voor **cliëntcertificaten** besproken. Meer informatie over het instellen van traditionele authenticatiemethoden vindt u in [het artikel over authenticatietypes]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="nl" >}}).

## Types cliëntcertificaten

Het gedeelte Cliëntcertificaat op het tabblad Request van een Multi-step API-controleregel biedt de volgende opties. Als u meerdere stappen gebruikt in uw stapdefinitie, zorg er dan voor dat u voor elke stap de gewenste instellingen heeft.

-   **Uptrends cliëntcertificaat**: Deze optie is handig als u van uw API-gebruikers eist dat zij hun eigen cliëntcertificaat genereren en meesturen om hun identiteit te bewijzen. Als u deze optie kiest, wordt er een certificaat dat eigendom is van Uptrends meegestuurd als de HTTP request wordt verzonden. Uw API kan die inkomende request verifiëren met behulp van de bijbehorende public key. Als deze overeenkomt, kunt u er zeker van zijn dat de request afkomstig is van iemand die eigenaar is van het originele certificaat (d.w.z. Uptrends), en van niemand anders. Het certificaat is niet beschikbaar op (containerized) [persoonlijke controlestations.]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="nl" >}}) 
Lees voor meer informatie het artikel over [Uptrends' public key-informatie]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="nl" >}}). 
-   **Eigen cliëntcertificaat**: Gebruik deze optie als u de eigenaar of beheerder bent van het cliëntcertificaat dat met de request meegestuurd moet worden. Nadat u het certificaat naar Uptrends hebt geüpload kunt u het in uw Multi-step API-controleregels opnemen. Aangezien u eigenaar bent van dat certificaat, zal uw API in staat zijn inkomende requests die het gebruiken te verifiëren. In het volgende gedeelte leest u hoe u dit instelt.
-   **Geen**: Kies *Geen* als u geen cliëntcertificaat wilt opnemen in uw HTTP request.

## Een gebruiker-gedefinieerde of eigen cliëntcertificaat instellen 

Om een cliëntcertificaat op te nemen in uw Multi-step API-controleregels moet u het eerst naar uw Uptrends-account uploaden. Certificaten (en andere gevoelige informatie) worden geüpload naar en opgeslagen in de Vault. Nadat u een certificaat aan uw vault heeft toegevoegd, kunt u het gebruiken bij het instellen van monitoring.

### Een cliëntcertificaat uploaden

Als u de optie van een eigen cliëntcertificaat voor het eerst kiest, zult u zien dat er nog geen certificaten beschikbaar zijn. Om een certificaat toe te voegen klikt u op *Item toevoegen* om naar de vault te schakelen. U kunt ook naar het menu {{< AppElement type="menuitem" >}}Accountinstellingen > Vault{{< /AppElement >}} gaan, een vault-sectie openen en klikken op {{< AppElement type="button" >}}Vault-item toevoegen{{< /AppElement >}}.

Voer op de pagina *Nieuw vault-item* een unieke naam in voor het certificaat, zodat u het later terug kunt vinden. Zorg ervoor dat het Type van het nieuwe vault-item is ingesteld op **Certificaatarchief**. Voer in de *Omschrijving* alle informatie in die u belangrijk vindt.

Kies tot slot een certificaatbestand dat u wilt uploaden. Het bestand moet het formaat PKCS \#12 hebben of het moet een certificaatarchief zijn dat zowel de private key als de public key bevat. Bestanden met het formaat PKCS \#12 hebben de extensie .pfx of .p12.

Een certificaatarchiefbestand is meestal versleuteld. Daarom hebben we het bijbehorende wachtwoord nodig om het archief te kunnen gebruiken. Voer het wachtwoord in het veld *Wachtwoord van het archief* en klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

### Cliëntcertificaten gebruiken in een Multi-step API-controleregel

Zodra u een geschikt cliëntcertificaat in de vault heeft opgeslagen, kunt u het gebruiken voor Multi-step API-monitoring. Klik in het gedeelte **Cliëntcertificaat** van een stap op **Verversen** om de lijst met beschikbare certificaten bij te werken. Kies vervolgens voor elke stap waarvoor een certificaat vereist is het bijbehorende certificaat.
