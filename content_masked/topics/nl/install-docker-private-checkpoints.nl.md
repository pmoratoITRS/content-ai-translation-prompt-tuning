{
  "hero": {
    "title": "Een Docker controlestation installeren"
  },
  "title": "Een Docker controlestation installeren",
  "summary": "Implementeer een Docker host en controlestation containers voor interne monitoring van uw netwerkinfrastructuur.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/docker-persoonlijke-controlestations-installeren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dit knowledgebase-artikel biedt een installatiehandleiding om Windows Server 2022 of 2019 te configureren als hostbesturingssysteem. Er wordt ook uitgelegd hoe u een containerized [Docker persoonlijk controlestation]([LINK_URL_1]) instelt en start.

Controleer vóór installatie of aan alle [vereisten en instellingen]([LINK_URL_2]) wordt voldaan. Uptrends voorziet u van alle benodigde bestanden om aan de slag te gaan.

## Installatiescript

Uptrends biedt een installatiescript dat u als een .zip-bestand kunt downloaden via het menu [SHORTCODE_5] Persoonlijke locaties [SHORTCODE_6] van de [Uptrends-app]([LINK_URL_3]). Dit script is beschikbaar voor elk van uw [Persoonlijke locaties]([LINK_URL_4]) en voert de belangrijkste installatiestappen uit. Deze stappen omvatten het installeren van Docker en Docker Compose, het ophalen van de Uptrends-containerimages, het uitvoeren van een opstart- en updatetaak en het starten van het containerized controlestation.

## Installatiestappen

**Een controlestation installeren met behulp van het script:**

1. Ga naar het menu [SHORTCODE_7] Persoonlijke locaties [SHORTCODE_8].
2. Als u geen [Persoonlijke locaties]([LINK_URL_5]) heeft toegevoegd, klik dan op de knop [SHORTCODE_9] Locatie toevoegen [SHORTCODE_10]. Na het toevoegen worden er standaard twee controlestations opgenomen.
3. Klik op de naam van het Persoonlijke locatie-controlestation.
4. Selecteer het vereiste besturingssysteem in het vervolgmenu **Host operating system**.
5. Klik op de knop [SHORTCODE_11] Zip-bestand voor installatie downloaden [SHORTCODE_12].

[SHORTCODE_1] **Belangrijk:** Houd er rekening mee dat het gedownloade .zip-bestand alleen het specifieke Persoonlijke locaties-controlestation bevat dat u heeft geselecteerd uit de twee standaardopties. Uw .zip-bestand heeft een bestandsnaam UptrendsCheckpoints\[HTML_TAG_1].zip, waarbij \[HTML_TAG_2] de naam van uw controlestation is. [SHORTCODE_2]

5. Pak het gedownloade bestand uit op de plaats waar u het persoonlijke controlestation wilt installeren.
6. Om te voorkomen dat screenshots naar de cloud worden geüpload [bewerkt u het docker-compose-bestand]([LINK_URL_6]) na het downloaden en uitpakken van de bestanden.

[SHORTCODE_3] **Belangrijk:** Afhankelijk van het beleid van uw bedrijf moet u mogelijk alle Powershell-scriptbestanden (*.ps1) in de zip-map deblokkeren voordat u ze uitvoert. Zie voor meer informatie de [instructies]([LINK_URL_7]) over het deblokkeren van bestanden. [SHORTCODE_4]

7. Open een PowerShell-console en voer deze uit als Administrator. Voer het script [INLINE_CODE_1] uit in de Uptrends (unzip) directory. Hierdoor wordt de server één keer opnieuw opgestart. Houd er rekening mee dat het script een taak configureert die één keer per uur wordt uitgevoerd om de Uptrends-containers te controleren op updates.

De controlestations zijn nu beschikbaar en kunnen worden geselecteerd op het tabblad [SHORTCODE_13] Controlestations [SHORTCODE_14] van de controleregel. U kunt de controlestations ook zien in het dialoogvenster *Details van de controle* wanneer u een snelle test rechtstreeks vanuit de controleregel uitvoert met de knop [SHORTCODE_15] Test starten [SHORTCODE_16].

Zie [Certificaten installeren in Persoonlijke locaties]([LINK_URL_8]) voor informatie over het installeren van certificaten in Persoonlijke locaties.

## Uw persoonlijke controlestation monitoren

Uptrends zal wijzigingen aanbrengen in uw account om u beter te helpen bij het monitoren van uw persoonlijke controlestations. Zorg ervoor dat uw persoonlijke controlestation-servers, -firewall, -internetverbinding en andere ondersteunende systemen toegankelijk blijven.

Tijdens de set-up van het persoonlijke controlestation voegt Uptrends extra controleregels en configuraties toe. Verwijder of wijzig niets in uw account.

Raadpleeg voor meer informatie het knowledgebase-artikel [Persoonlijke locaties gebruiken]([LINK_URL_9]).