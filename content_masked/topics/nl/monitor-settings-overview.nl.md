{
  "hero": {
    "title": "Overzicht monitorinstellingen"
  },
  "title": "Overzicht monitorinstellingen",
  "summary": "Elke controleregel heeft enkele algemene en meer specifieke instellingen (afhankelijk van het type controleregel). Bekijk welke instellingen beschikbaar zijn.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/overzicht-monitorinstellingen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

## Toegang tot controleregelinstellingen

Uw controleregelinstellingen onderhouden:

1. Ga naar [SHORTCODE_1] Monitoring > Controleregels beheren [SHORTCODE_2].
2. Zoek de naam van de controleregel waarvan u de instellingen wilt wijzigen en klik op de bijbehorende link in de kolom *Controleregelnaam*. Of typ in het filterzoekvak (een deel van) de naam, type, groep of URL van de controleregel om de resultaten te filteren.
    Het configuratiescherm van de controleregel verschijnt, met tabbladen die al uw controleregelinstellingen bevatten. Hieronder vindt u meer informatie over de verschillende tabbladen met instellingen.
3. Breng de benodigde wijzigingen aan op de tabbladen.
4. Klik op de knop [SHORTCODE_3] Opslaan [SHORTCODE_4] om alle wijzigingen aan de controleregel op te slaan.

## Categorieën controleregelinstellingen

Verschillende controleregeltypes zijn bedoeld voor verschillende monitoringdoeleinden en niet alle instellingen zijn van toepassing op alle controleregels. Bekijk de instellingen die relevant zijn voor uw controleregel:
- Algemene instellingen
   - [Controle-interval]([LINK_URL_1])
   - [Dynamische waarden in URL's en POST-inhoud]([LINK_URL_2])
   - [Controleregelmodus]([LINK_URL_3])
   - [Controleregelnotities]([LINK_URL_4])
   - [Controleregelsjablonen]([LINK_URL_5])
- [Stappen (transactiecontroleregels)]([LINK_URL_6])
- [Stappen (Multi-step-controleregels)]([LINK_URL_7])
- [Foutcondities]([LINK_URL_8])
- Extra instellingen
   - [Browsertypes]([LINK_URL_9])
   - [Google Analytics blokkeren]([LINK_URL_10])
   - [Bandbreedte begrenzen]([LINK_URL_11])
   - [DNS bypass]([LINK_URL_12])
- [Controlestations]([LINK_URL_13])
- [Onderhoudsperiodes]([LINK_URL_14])
- [Lid van]([LINK_URL_15])
- [Gebruikersrechten]([LINK_URL_16])

## Dashboard Controleregels beheren

Met alle controleregels ingesteld in uw Uptrends-webapplicatie, biedt het **Dashboard Controleregels beheren** u een beknopt overzicht om al uw controleregels en controleregelinstellingen op één plek te kunnen bekijken. Met dit dashboard kunt u de controleregelinstellingen in uw account bekijken, filteren en exporteren.

![Overzicht dashboard Controleregels beheren]([LINK_URL_17])

### Controleregelinstellingen bekijken
U kunt uw controleregelinstellingen eenvoudig visualiseren en controleren, waaronder:

- **Controleregelnaam** - specificeert de naam van uw controleregelconfiguratie en het aantal gebruikte [credits]([LINK_URL_18]). Een pictogram van een kegelvormige fles geeft aan dat uw controleregel zich in *Staging*-modus bevindt, terwijl het moersleutelpictogram aangeeft dat uw controleregel zich in *Development* [modus]([LINK_URL_19]) bevindt.
- **Dashboard controleregel** - bevat een *Ga naar het dashboard*-link waarmee u naar het specifieke controleregeldashboard gaat.
- **Type controleregel** - specificeert het [type controleregel]([LINK_URL_20]) dat momenteel is ingesteld (bijvoorbeeld Transactie- en Multi-step API-controleregels).
- **Controle-interval (minuten)** - specificeert hoe vaak uw controleregel wordt uitgevoerd.
- **URL / Netwerkadres** - specificeert het browseradres of het IP-adres van de website die u momenteel monitort.
- **Actief** - specificeert of uw controleregel is ingeschakeld of uitgeschakeld. U ziet *Ja* als de controleregel ingeschakeld en actief is, anders ziet u *Nee*. Ingeschakelde en uitgeschakelde controleregels geven tussen haakjes ook de huidige [modus]([LINK_URL_21]) van uw controleregel weer, of het nu *Staging* of *Development* is.
- **Gemaakt op** - toont de datum en tijd waarop u de controleregel heeft gemaakt.
- **Laatst gewijzigd op** - toont de datum en tijd waarop u voor het laatst uw controleregel heeft bijgewerkt of wijzigingen in uw controleregel heeft opgeslagen.  
- **Lid van groepen** - specificeert tot welke controleregelgroep(en) uw controleregel behoort.

### Controleregelinstellingen filteren

Om uw hoeveelheid controleregels eenvoudig te verkleinen, gaat u naar het filtertekstveld en past u de lijst aan op basis van de controleregelnaam, type, groep en URL. U kunt ook filteren op controleregelmodi door de selectievakjes *Development, Staging en Production* aan te vinken.

### Controleregelinstellingen exporteren

Aangezien het **Dashboard Controleregels beheren** nuttig is bij het visualiseren en groeperen van uw algehele controleregelinstellingen, kunt u deze informatie ook exporteren voor beter inzicht en later gebruik. In dit [knowledgebase-artikel]([LINK_URL_22]) vindt u stapsgewijze aanwijzingen voor het exporteren van uw dashboards.

Nadat u uw data in het gewenste formaat heeft geëxporteerd, kunt u de details van uw controleregelinstellingen bekijken zoals beschreven in het vorige gedeelte, [Dashboard Controleregels beheren]([LINK_URL_23]). U vindt hierin extra kolommen, waaronder:

- **Alert op tijdlimieten** - toont de [laad- en uitvoertijd]([LINK_URL_24])-instellingen van uw controleregel, waarbij wordt aangegeven of de foutconditie is ingesteld op *alleen met kleurcode weergeven* van het resultaat of *fout genereren*.
- **Tijdlimieten** - toont de bijbehorende [tijdlimieten in milliseconden]([LINK_URL_25]) van uw controleregel (geconfigureerd en gerelateerd aan de alert bij tijdlimietinstellingen).
- **Notities** - toont de inhoud van het veld *Notities*.