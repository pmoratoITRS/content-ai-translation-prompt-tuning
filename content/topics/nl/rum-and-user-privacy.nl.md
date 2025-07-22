{
  "hero": {
    "title": "RUM en gebruikersprivacy"
  },
  "title": "RUM en gebruikersprivacy",
  "summary": "Het monitoren van performancegegevens van echte gebruikers kan leiden tot bezorgdheid voor uw merk omtrent privacy. Lees hoe Uptrends gebruikersprivacy beschermt en wat u verder moet weten.",
  "url": "/support/kb/rum/rum-en-gebruikersprivacy",
  "translationKey": "https://www.uptrends.com/support/kb/rum/rum-and-user-privacy"
}

Bescherming van gebruikersprivacy is belangrijk. In dit artikel leggen we uit hoe Uptrends informatie van uw gebruikers gebruikt en met welke extra stappen u uw merk en de privacy van uw gebruikers kunt beschermen.

## Privacy, persoonlijke gegevens en de Wet bescherming persoonsgegevens

Als een van uw websitegebruikers uw website bezoekt, stuurt het RUM-script dat in uw pagina's zit een klein verzoek naar Uptrends. Het is de aard van internet dat we bij dit verzoek ook het IP-adres van de bezoeker ontvangen. We erkennen de gevoelige aard van deze informatie aangezien systemen het IP-adres kunnen gebruiken om individuele gebruikers te identificeren en volgen. We hebben RUM van de grond af ontworpen om er zeker van te zijn dat u volledige controle hebt over hoe er met de IP-adressen van uw bezoekers wordt omgegaan. De twee belangrijkste aspecten hierbij zijn:

-   We bieden anonimisering van IP-adressen op meerdere niveaus.
-   We slaan de IP-adressen niet langdurig op.

### Anonimisering van IP-adressen op meerdere niveaus

Uptrends gebruikt het IP-adres om u het land van oorsprong van uw bezoeker te laten weten (en in sommige gevallen informatie op staatniveau voor Australië, Canada en de VS). Uptrends identificeert uw bezoekers niet, verzamelt geen persoonlijke gegevens en volgt uw websitebezoekers niet. Echter, als het privacybeleid van uw applicatie Uptrends niet toestaat het volledige IP-adres van uw bezoekers op welke manier dan ook te gebruiken, bieden we twee niveaus van anonimisering:

-   **Niveau 0:** Het volledige IP-adres wordt gebruikt. Dit is de standaardinstelling.
-   **Niveau 1:** We zetten het laatste (meest identificerende) octet van het IP-adres vóór inspectie op nul.
-   **Niveau 2:** We zetten de laatste twee octets van het IP-adres vóór inspectie op nul.

**Voorbeeld:** Bij Niveau 1 verwerken we het oorspronkelijke IP-adres `123.123.123.123` van de gebruiker tot `123.123.123.0`. Anonimisering op Niveau 2 wordt `123.123.0.0`.

{{< callout >}}
**Opmerking:** Uptrends bewaart oorspronkelijke of geanonimiseerde IP-adressen niet langdurig (zie hieronder).
{{< /callout >}}

Door de belangrijkste delen van het IP-adres te verwijderen (in termen van het uniek identificeren van een netwerkadres) krijgen we alleen een heel globale indruk van de locatie van elke bezoeker. Het gevolg is dat bij een hoger anonimiseringsniveau de land- en staatinformatie minder accuraat wordt.

### Het anonimiseringsniveau specificeren

Als u geen IP-anonimisering nodig hebt, kunt u het gewone RUM-script gebruiken — zonder extra configuratie. Voor Niveau 1 en 2 is een heel kleine wijziging in het script nodig.

In het RUM-script dat in uw webpagina's zit, ziet u dat de aip parameter standaard op 0 staat. **Zet deze waarde op 1 voor Niveau 1-anonimisering en gebruik 2 voor Niveau 2-anonimisering.**

**Voorbeeld:**

`var _urconfig = { sid: "9acad2af-b1f5-4438-8de6-5047a02a7ecf", aip: 1 };`

Het script stuurt de anonimiseringswaarde mee met elk RUM request dat wordt uitgevoerd als onderdeel van uw webpagina's. Het anonimiseringsniveau dat u hebt gespecificeerd wordt onmiddellijk van kracht.

### Geen langdurige opslag van IP-adressen

Als u besluit IP-anonimisering te gebruiken, garanderen we dat we de oorspronkelijke IP-adressen niet zullen inspecteren of opslaan, noch in geheugen, op schijf of welke andere opslagfaciliteit of -apparaat dan ook. De allereerste stap in onze pijplijn is het anonimiseren van de IP-adressen voordat we ze op welke manier dan ook onderzoeken.

Bovendien **bewaren we de IP-adresgegevens slechts tijdelijk** — totdat het oorspronkelijke verzoek door onze gehele pijplijn is verwerkt. Daarna wissen we de informatie. Elke combinatie van IP-adresinformatie, user agent gegevens, URL's, datums, tijden en tijdzone-informatie wordt gewist.

## Real User Monitoring en uw privacyverklaring

Sommige Real User Monitoring-klanten vragen ons wat zij moeten toevoegen aan hun privacyverklaring op hun website. Hoewel wij geen advocaten zijn, kunt u onderstaande alinea kopiëren en opnemen in uw privacyverkaring.

*&lt;Uw merknaam&gt; gebruikt Uptrends’ Real User Monitoring om de performance te monitoren die gebruikers ervaren tijdens hun bezoek aan onze website. Uptrends gebruikt geen cookies om data te verzamelen van de gebruikers van onze website of om hen te volgen; in plaats daarvan gebruikt Uptrends een klein scriptbestand op onze webpagina's dat performancegegevens over onze websitebezoekers naar Uptrends' servers stuurt. De gegevens die van elke bezoeker worden verzameld omvatten IP-adres, apparaattype, besturingssysteem en de gebruikte browser. Uptrends' servers voegen de performancegegevens van al onze websitebezoekers samen en voorzien ons van informatie waarmee we de gebruikerservaring op onze site kunnen verbeteren aan de hand van de genoemde informatie. Uptrends gebruikt de individuele IP-adressen van onze websitebezoekers alléén om informatie te verzamelen over de staat of het land van de bezoekers. Uptrends slaat bovendien IP-gegevens niet langdurig op, volgt geen individuele gebruikers en deelt geen informatie over individuele bezoekers met derden.*

### Als u anonimiseringsniveau 1 of 2 gebruikt, kunt u ook onderstaande alinea opnemen in uw privacyverklaring 

*Om uw privacy te beschermen is de versie van Uptrends' scriptbestand dat wij in onze site hebben opgenomen zo ingesteld dat uw IP-adres wordt geanonimiseerd voordat het wordt verwerkt. Uw IP-adres wordt nooit opgeslagen en nooit gebruikt voor andere doeleinden dan het vaststellen van uw land van oorsprong.*
