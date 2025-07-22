{
  "hero": {
    "title": "Een Docker controlestation installeren"
  },
  "title": "Een Docker controlestation installeren",
  "summary": "Implementeer een Docker host en controlestation containers voor interne monitoring van uw netwerkinfrastructuur.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/docker-persoonlijke-controlestations-installeren",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-docker-private-checkpoints"
}

Dit knowledgebase-artikel biedt een installatiehandleiding om Windows Server 2022 of 2019 te configureren als hostbesturingssysteem. Er wordt ook uitgelegd hoe u een containerized [Docker persoonlijk controlestation]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker#how-do-i-get-a-private-checkpoint" lang="nl" >}}) instelt en start.

Controleer vóór installatie of aan alle [vereisten en instellingen]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="nl" >}}) wordt voldaan. Uptrends voorziet u van alle benodigde bestanden om aan de slag te gaan.

## Installatiescript

Uptrends biedt een installatiescript dat u als een .zip-bestand kunt downloaden via het menu {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}} van de [Uptrends-app](https://app.uptrends.com/PrivateLocations). Dit script is beschikbaar voor elk van uw [Persoonlijke locaties]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="nl" >}}) en voert de belangrijkste installatiestappen uit. Deze stappen omvatten het installeren van Docker en Docker Compose, het ophalen van de Uptrends-containerimages, het uitvoeren van een opstart- en updatetaak en het starten van het containerized controlestation.

## Installatiestappen

**Een controlestation installeren met behulp van het script:**

1. Ga naar het menu {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Als u geen [Persoonlijke locaties]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="nl" >}}) heeft toegevoegd, klik dan op de knop {{< AppElement type="buttonPrimary" >}} Locatie toevoegen {{< /AppElement >}}. Na het toevoegen worden er standaard twee controlestations opgenomen.
3. Klik op de naam van het Persoonlijke locatie-controlestation.
4. Selecteer het vereiste besturingssysteem in het vervolgmenu **Host operating system**.
5. Klik op de knop {{< AppElement type="buttonPrimary" >}} Zip-bestand voor installatie downloaden {{< /AppElement >}}.

{{< callout >}} **Belangrijk:** Houd er rekening mee dat het gedownloade .zip-bestand alleen het specifieke Persoonlijke locaties-controlestation bevat dat u heeft geselecteerd uit de twee standaardopties. Uw .zip-bestand heeft een bestandsnaam UptrendsCheckpoints\<checkpoint-name\>.zip, waarbij \<checkpoint-name\> de naam van uw controlestation is. {{< /callout >}}

5. Pak het gedownloade bestand uit op de plaats waar u het persoonlijke controlestation wilt installeren.
6. Om te voorkomen dat screenshots naar de cloud worden geüpload [bewerkt u het docker-compose-bestand]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection#disable-screenshots-in-docker-compose-file" lang="nl" >}}) na het downloaden en uitpakken van de bestanden.

{{< callout >}} **Belangrijk:** Afhankelijk van het beleid van uw bedrijf moet u mogelijk alle Powershell-scriptbestanden (*.ps1) in de zip-map deblokkeren voordat u ze uitvoert. Zie voor meer informatie de [instructies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-5.1) over het deblokkeren van bestanden. {{< /callout >}}

7. Open een PowerShell-console en voer deze uit als Administrator. Voer het script `./install-checkpoint.ps1` uit in de Uptrends (unzip) directory. Hierdoor wordt de server één keer opnieuw opgestart. Houd er rekening mee dat het script een taak configureert die één keer per uur wordt uitgevoerd om de Uptrends-containers te controleren op updates.

De controlestations zijn nu beschikbaar en kunnen worden geselecteerd op het tabblad {{< AppElement type="tab" >}} Controlestations {{< /AppElement >}} van de controleregel. U kunt de controlestations ook zien in het dialoogvenster *Details van de controle* wanneer u een snelle test rechtstreeks vanuit de controleregel uitvoert met de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}}.

Zie [Certificaten installeren in Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-certificates-private-locations" lang="nl" >}}) voor informatie over het installeren van certificaten in Persoonlijke locaties.

## Uw persoonlijke controlestation monitoren

Uptrends zal wijzigingen aanbrengen in uw account om u beter te helpen bij het monitoren van uw persoonlijke controlestations. Zorg ervoor dat uw persoonlijke controlestation-servers, -firewall, -internetverbinding en andere ondersteunende systemen toegankelijk blijven.

Tijdens de set-up van het persoonlijke controlestation voegt Uptrends extra controleregels en configuraties toe. Verwijder of wijzig niets in uw account.

Raadpleeg voor meer informatie het knowledgebase-artikel [Persoonlijke locaties gebruiken]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="nl" >}}).