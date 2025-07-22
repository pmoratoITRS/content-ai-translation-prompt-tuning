{
  "hero": {
    "title": "Audit log"
  },
  "title": "Audit log",
  "summary": "In dit artikel vindt u instructies over audit logs.",
  "url": "[URL_BASE_TOPICS]account/audit-log",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met alle updates en verschillende activiteiten die plaatsvinden in uw Uptrends-webapplicatie, is het moeilijk om handmatig bij te houden wie wanneer waar welke wijzigingen in uw instellingen heeft aangebracht. In dergelijke scenario's is het is het om verschillende redenen nuttig om een historie log bij te houden. Bijvoorbeeld om snel onbedoelde wijzigingen te herstellen, de hoofdoorzaak van een probleem te identificeren, gebruikersrechten te beoordelen en andere soortgelijke zaken.

De Uptrends **Audit log** is een handige tool die aan al uw behoeften voldoet! Deze functie registreert alle activiteiten in uw Uptrends-applicatie en geeft gedetailleerde informatie over wie wanneer waar welke specifieke updates in uw account heeft uitgevoerd.

![Audit log dashboard overzicht]([LINK_URL_1])

[SHORTCODE_1]
De **Audit log** is beschikbaar in alle abonnementen, waardoor die gemakkelijk toegankelijk is. Ga gewoon naar [SHORTCODE_3] Accountinstellingen > Audit log [SHORTCODE_4] om wijzigingen in uw applicatie weer te geven.
[SHORTCODE_2]

## Functies van de Audit log

Met het dashboard Audit log kunt u logs die in uw account zijn gemaakt bekijken, filteren en exporteren.

### Audit logs bekijken

Standaard bevat het dashboard Audit log een lijst met informatie, waarbij de meest recente wijzigingen bovenaan worden weergegeven, inclusief kolommen zoals:

- **Datum/tijd** — toont de werkelijke datum en tijd waarop de update is gemaakt.
- **Type gebeurtenis** — specificeert het type wijziging dat de gebruiker heeft aangebracht, waaronder *Inlogactie, Item bijgewerkt, Wijziging in lidmaatschap*.
- **Operator** — specificeert de naam van de operator die de wijziging heeft aangebracht.
- **Bericht** — beschrijft welke items zijn gemaakt, bijgewerkt of verwijderd. Als u bijvoorbeeld een nieuwe operator creëert, toont het bericht *Operator 'ABC' is gemaakt*.
- **Bron** — specificeert de bron van de wijziging. Als er een update is uitgevoerd via de Uptrends-webapplicatie zelf, ziet u *Webapplicatie* als bron. Als er wijzigingen zijn aangebracht via de API, ziet u de *API* als bron.

### Audit logs filteren

Om specifieke activiteiten in uw applicatie gemakkelijk vast te stellen, kunt u met de Audit log vermeldingen filteren op *Type gebeurtenis* en *Itemtype*.

Door op het keuzemenu [SHORTCODE_5] Type gebeurtenis[SHORTCODE_6] te klikken, kunt u eenvoudig het type updates filteren dat in uw account is aangebracht. U kunt categorieën kiezen zoals *Inlogactie, Wijziging in lidmaatschap, Rechtenwijziging, Item toegevoegd* en nog veel meer.

Op dezelfde manier kunt u met het keuzemenu [SHORTCODE_7] Itemtype [SHORTCODE_8] specifieke itemwijzigingen filteren die zijn aangebracht in uw *Controleregels, Controleregelgroepen, Operator, Operatorgroepen* of andere specifieke gebieden.

### Audit logs exporteren

Net als elk Uptrends-dashboard kan de Audit log ook worden geëxporteerd naar PDF-, Excel- en HTML-formaat. In dit [knowledgebase-artikel]([LINK_URL_2]) vindt u stapsgewijze aanwijzingen voor het exporteren van uw Audit log-dashboarddata.

Nadat u uw data succesvol heeft geëxporteerd, kunt u dezelfde details zien als in de overzichtslijst van uw dashboard Audit log. Alleen de kolom *Bron* is weggelaten om het overzicht te vereenvoudigen.

## Audit log details

Terwijl de lijst Audit log een overzicht biedt van de geschiedenis van wijzigingen in uw account, geven de **Audit log details** meer specifieke informatie over welke wijzigingen er precies zijn doorgevoerd.

Klik gewoon op een item in de audit log om het pop-upvenster **Audit log details** weer te geven:

![Audit log details overzicht]([LINK_URL_3])

Over het algemeen toont dit pop-upvenster details die lijken op wat is te zien in de lijst in het dashboard Audit log. In de pop-up ziet u ook aanvullende informatie, zoals de audit log-ID (een unieke identificatie van het audit log-item), de Naam van een Itemtype (bijvoorbeeld Controleregel, Operator, Alertdefinitie en meer) en ook specifieke informatie over welke items zijn gemaakt, bijgewerkt en verwijderd.

In de illustratie hierboven is te zien dat wanneer een item wordt gemaakt, de **Audit log details** de sectie *Aangemaakt met deze waardes* toont met details over het gemaakte item en de bijbehorende instellingen. Wanneer u een item bijwerkt, ziet u in de Audit log details de sectie *Aangepast met deze nieuwe waardes* met de vorige en de bijgewerkte waarden. Merk op dat de informatie die wordt weergegeven in de Audit log details varieert, afhankelijk van welke updates u maakt en welke items u heeft bijgewerkt.

## Audit log details voor elk Itemtype

Deze sectie bevat de historie van wijzigingen die zijn vastgelegd door de Audit log voor elk *Itemtype*.

### Dashboards
De Audit log registreert wijzigingen die zijn gemaakt vanuit en naar **Dashboards** wanneer u:
- *Delen*-rechten voor dashboards toekent en intrekt.

### Alertdefinities
De Audit log legt wijzigingen vast die zijn aangebracht vanuit en naar **Alertdefinities** wanneer u:

- Een nieuwe alertdefinitie creëert.
- Een bestaande alertdefinitie hernoemt of verwijdert.
- De status van de alertdefinitie activeert of deactiveert.
- Instellingen toevoegt, wijzigt of verwijdert uit de scope van de alertdefinitie van controleregels en controleregelgroepen en escalatieniveaus.
- Gebruikersrechten voor alertdefinities toekent en intrekt.

### Integraties
De Audit log legt wijzigingen vast die zijn aangebracht vanuit en naar **Integratie** wanneer u:

- Een nieuwe integratie creëert.
- Een bestaande integratie hernoemt of verwijdert.
- De status van de integratie activeert of deactiveert.
- Voorgedefinieerde variabelen en algemene instellingen toevoegt, wijzigt of verwijdert uit de integratie.
- Gebruikersrechten voor integraties toekent en intrekt.

### Controleregels
De Audit log registreert wijzigingen die zijn aangebracht vanuit en naar **Controleregels** wanneer u:

- Een nieuwe controleregel creëert.
- Een bestaande controleregel hernoemt of verwijdert.
- De status van de controleregel activeert of deactiveert.
- Controleregelinstellingen toevoegt, bijwerkt of verwijdert die zijn geconfigureerd in de tabbladen [SHORTCODE_9] Algemeen [SHORTCODE_10], [SHORTCODE_11] Stappen [SHORTCODE_12], [SHORTCODE_13] Foutcondities [SHORTCODE_14], [SHORTCODE_15] Extra [SHORTCODE_16], [SHORTCODE_17] Controlestations [SHORTCODE_18], [SHORTCODE_19] Onderhoudsperiodes [SHORTCODE_20] en [SHORTCODE_21] Lid van [SHORTCODE_22].
- Controleregels en controleregelalerts start and stopt.
- Gebruikersrechten voor controleregels toekent en intrekt.

### Controleregelgroepen
De Audit log registreert wijzigingen die zijn aangebracht vanuit en naar **Controleregelgroepen** wanneer u:

- Een nieuwe controleregelgroep creëert.
- Een bestaande controleregelgroep hernoemt of verwijdert.
- Controleregeldetails en het bereik van controleregels binnen de controleregelgroep toevoegt, bijwerkt of verwijdert.
- Gebruikersrechten voor controleregelgroepen toekent en intrekt.

### Controleregelsjablonen
De Audit log legt wijzigingen vast die zijn aangebracht in **Controleregelsjablonen** wanneer u:

- Een nieuwe controleregelsjabloon creëert.
- Een bestaande controleregelsjabloon hernoemt of verwijdert.
- Configuratie toevoegt, bijwerkt of verwijdert van de tabbladen algemene instellingen, [SHORTCODE_23] Controlestations [SHORTCODE_24] en [SHORTCODE_25] Onderhoudsperiodes [SHORTCODE_26] van de controleregelsjabloon.

### Operators
De Audit log registreert wijzigingen die zijn aangebracht vanuit en naar **Operators** wanneer u:

- Een nieuwe operator creëert.
- Een bestaande operator hernoemt of verwijdert.
- Configuratie toevoegt, bijwerkt of verwijdert uit de tabbladen algemene instellingen, [SHORTCODE_27] Geen-dienstperiodes [SHORTCODE_28] en [SHORTCODE_29] Lid van [SHORTCODE_30] van operators.
- Tijdzone-instellingen bijwerkt.
- Een uitnodiging naar een operator stuurt of een operator uw uitnodiging heeft geaccepteerd.
- Gebruikersrechten voor operators toekent en intrekt.

De Audit log registreert ook items met betrekking tot operators per *Gebeurtenistype*, zoals *Inlogactie en Mislukte aanmeldingspoging*.

### Operatorgroepen

De Audit log registreert wijzigingen die zijn aangebracht vanuit en naar **Operatorgroepen** wanneer u:

- Een nieuwe operatorgroep creëert.
- Leden aan een operatorgroep toevoegt of uitsluit.
- De naam van een operatorgroep bewerkt.
- Een bestaande operatorgroep verwijdert.
- Gebruikersrechten voor operatorgroepen toekent en intrekt.

### Persoonlijke locaties

De Audit log registreert wijzigingen die zijn aangebracht vanuit en naar een **Persoonlijke locatie** wanneer u:

- Een nieuwe persoonlijke locatie creëert.
- Een bestaande persoonlijke locatie hernoemt of verwijdert.
- Controlestations in- of uitschakelt.
- Instellingen aan de persoonlijke locatie toevoegt, bijwerkt of verwijdert.

### SLA-definities

De Audit log legt wijzigingen vast die zijn aangebracht vanuit en naar **SLA-definitie** wanneer u:

- Een nieuwe SLA-definitie creëert.
- Een bestaande SLA-definitie hernoemt of verwijdert.
- Instellingen toevoegt, bijwerkt of verwijdert uit het SLA-tijdschema en uitsluitingsperiode.

### Vault

De Audit log registreert wijzigingen die zijn aangebracht vanuit de **Vault** wanneer u:

- Een vault-item creëert, bijwerkt of verwijdert.
- Een vault-sectie creëert, bijwerkt of verwijdert.
- Vault-items toevoegt, bijwerkt of verwijdert uit een vault-sectie.
- Gebruikersrechten voor vault-secties toekent en intrekt.