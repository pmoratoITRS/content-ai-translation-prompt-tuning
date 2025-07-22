{
  "hero": {
    "title": "Certificaten installeren in Persoonlijke locaties"
  },
  "title": "Certificaten installeren in Persoonlijke locaties",
  "summary": "Installeer certificaten in Persoonlijke locaties voor interne monitoring van uw netwerkinfrastructuur.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/installeer-certificaten-persoonlijke-locatiens",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wanneer u uw [Docker-gebaseerde Persoonlijke locatie]([LINK_URL_1]) instelt, moet u mogelijk certificaten installeren om vertrouwen te creëren en verbindingen te verifiëren met de website of webservice die u monitort.

De volgende types certificaten zijn beschikbaar voor installatie:

- Clientcertificaten (PKCS #12)
- Intermediate Certificate Authority (CA)-certificaten (PKCS #7)
- Root Certificate Authority (CA)-certificaten (PKCS #7)

Merk op dat het [Uptrends Docker-gebaseerde installatie zip-bestand]([LINK_URL_2]) een **Certificates**-map bevat. Hierin vindt u submappen voor elk ondersteund certificaattype, waar certificaten kunnen worden geïnstalleerd zoals hieronder beschreven.

## Certificaten installeren op een Docker-gebaseerde Persoonlijke locatie

Dit gedeelte is een optionele installatiehandleiding voor certificaten op Docker-gebaseerde Persoonlijke locaties. Deze stappen zijn alleen nodig als voor een van uw te testen applicaties de installatie van een certificaat vereist is.

Voordat u de cliëntcertificaten installeert, moet u ervoor zorgen dat u de installatiestappen voor [Docker-gebaseerde Persoonlijke locaties]([LINK_URL_3]) heeft gevolgd.

### Certificate Authority (CA)-certificaten installeren

**CA-certificaten installeren:**

1. Open de map die de installatie van uw persoonlijke locatie bevat. U vindt er standaard verschillende bestanden, zoals het YAML-bestand [INLINE_CODE_1] en Windows PowerShell-scripts. Deze bestanden zijn essentieel voor het installatieproces.

2. Open de map **Certificates**. Deze map bevat drie submappen en een [INLINE_CODE_2] Markdown-bestand.

3. Plaats uw CA-certificaten in de juiste **Certificates**-submappen:

  - **Intermediate**-map — voor alle Intermediate Certificate Authority (CA)-certificaatbestanden (PKCS #7).
  - **Root**-map — voor alle Root Certificate Authority (CA)-certificaatbestanden (PKCS #7).
  
4. Start de Uptrends-controlestationsoftware opnieuw op door het script [INLINE_CODE_3] uit te voeren vanuit de installatie-root directory.

### Cliëntcertificaten installeren

Merk op dat [Clientcertificaten in Multi-step API (MSA)-controleregels]([LINK_URL_4]) en Clientcertificaten voor Persoonlijke locaties niet gerelateerd zijn en voor verschillende doeleinden dienen.

**Cliëntcertificaten installeren:**

1. Open de map die de installatie van uw persoonlijke locatie bevat. U vindt er standaard verschillende bestanden, zoals het YAML-bestand [INLINE_CODE_4] en Windows PowerShell-scripts. Deze bestanden zijn essentieel voor het installatieproces.

2. Open de map **Certificates**. Deze map bevat drie submappen en een [INLINE_CODE_5] Markdown-bestand.

3. Plaats uw Clientcertificaat in de map **Client**.

4. Creëer in de map **Client** een JSON-bestand met de naam [INLINE_CODE_6]. Dit JSON-bestand moet al uw cliëntcertificaten bevatten. Ga anders verder met de volgende stap.

- Kopieer en bewerk de JSON-sjabloon om te beginnen:

[CODE_BLOCK_1]

Merk op dat het JSON-fragment uit twee Cliëntcertificaten bestaat. Elk Cliëntcertificaat wordt vertegenwoordigd door een JSON-object met drie paren keywaarden. Het eerste certificaat, [INLINE_CODE_7], kan alleen worden gebruikt voor een specifiek subdomein. Terwijl het tweede certificaat, [INLINE_CODE_8], kan worden gebruikt voor het subdomein van de cliënt van [INLINE_CODE_9] bij verbinding met HTTPS-poort 1234, of bij bezoek aan [INLINE_CODE_10] of een van de subdomeinen.

Bewerk de volgende waarden op basis van uw vereisten:

  - [INLINE_CODE_11] — de bestandsnaam en bestandsextensie van uw Cliëntcertificaat.
  - [INLINE_CODE_12] — het wachtwoord dat nodig is om toegang te krijgen tot de data in het certificaatarchief, zoals de private key.
  - [INLINE_CODE_13] — de lijst met toegestane URL-domeinen of subdomeinen die het Cliëntcertificaat zullen gebruiken. Deze lijst kan bestaan uit meerdere URL-patronen die een enkel domein, subdomein of een wildcard voor een domein en al zijn subdomeinen kunnen zijn. Raadpleeg voor meer informatie de [URL-patroonnotatie voor Enterprise-beleid]([LINK_URL_5]).

5. Start de Uptrends-controlestationsoftware opnieuw op door het script [INLINE_CODE_14] uit te voeren vanuit de installatie-root directory.

6. Controleer of zowel de oude als de nieuwe certificaten worden herkend en correct zijn geïnstalleerd. Als er problemen optreden, voer dan een basisprobleemoplossing uit:

- Verifieer dat de JSON-bestandsnaam correct is.
- Zorg ervoor dat alle JSON-keywaardeparen voldoen aan de juiste JSON-syntaxis.
- Controleer op eventuele verkeerde configuraties of machtigingsproblemen.
