{
  "hero": {
    "title": "Browser monitoring"
  },
  "title": "Browser monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/browser-monitoring/overzicht-browser-monitoring",
  "summary": "Het controleregeltype Full Page Check is het meest uitgebreide controleregeltype. Elk element wordt gedownload en geladen in een browser. Het rapport geeft uw resultaten weer in een gedetailleerd watervalrapport.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Uptrends Browser-controleregels, ook bekend als een Full Page Check (FPC), zijn een van de vele [controleregeltypes]([LINK_URL_1]) die Uptrends biedt. Dit controleregeltype verstrekt gedetailleerde performancedata over uw webpagina op elementniveau. Een FPC-controleregel laadt uw pagina in een echte browser, inclusief scripts, CSS, elementen van derden en andere websitecomponenten. Deze controleregel voltooit het laden van een pagina in een echte browser om de prestaties van de website nauwkeurig te meten zoals ervaren door uw eindgebruikers.

De FPC presenteert monitoringinformatie in de details van de controle, inclusief een [watervalgrafiek]([LINK_URL_2]). Afhankelijk van het [browsertype]([LINK_URL_3]) dat u voor de controleregel kiest, zal er nog meer informatie zijn ([Extra kengetallen en functies]([LINK_URL_4])).

Als u inhoud van derden op uw website wilt monitoren, gebruikt u de optie [Full Page Check+]([LINK_URL_5]).

## Een FPC-controleregel instellen [ANCHOR_1]

Het instellen van een FPC-controleregel begint met het creëren van de controleregel en vervolgens het kiezen van het browsertype, het controle-interval en dan het definiëren van foutcondities, het kiezen van controlestations en het instellen van meer specifieke opties zoals onderhoudsperiodes.

Bekijk voor de basisprincipes het Uptrends-artikel [Controleregeltypes - controleregels voor Website performance]([LINK_URL_6]).

## Browser-controleregels (Full Page Checks (FPC))

Er zijn verschillende types Browser-controleregels waaruit u kunt kiezen:

- [Full Page Check (FPC)]([LINK_URL_7]) — een controleregeltype dat alle elementen van de pagina controleert bij het laden van de pagina en data weergeeft in een uitgebreide [watervalgrafiek]([LINK_URL_8]).

- [Full Page Check \+ (FPC+)]([LINK_URL_9]) — een optie onder de FPC-controleregel die alle elementen van de pagina, inclusief inhoud van derden, controleert bij het laden van de pagina. Deze controleregel geeft uw data ook weer in een uitgebreide [watervalgrafiek]([LINK_URL_10]).

Het gedeelte [Full Page Check]([LINK_URL_11]) bevat alle informatie over het toevoegen van dit type controleregel en het beheren van de instellingen.

De controleregelinstellingen worden uitgelegd in een aantal knowledgebase-artikelen, zoals hieronder vermeld.

### Algemene instellingen

Alle opties op het tabblad [SHORTCODE_1] Algemeen [SHORTCODE_2] van de controleregel zijn de fundamentele instellingen voor de FPC-controleregel.


- [Controle-interval]([LINK_URL_12])
- [Gelijktijdige monitoring]([LINK_URL_13])
- [Controleregelmodus]([LINK_URL_14])
- [Browsertype]([LINK_URL_15])
- [Controleregelnotities (optioneel)]([LINK_URL_16])

### Foutcondities

Een FPC-controleregel controleert standaard de beschikbaarheid van de opgegeven server-URL. Andere controles moeten worden gedefinieerd op het tabblad [SHORTCODE_3] Foutcondities [SHORTCODE_4] tab van de controleregel.

Het knowledgebase-article [Foutcondities]([LINK_URL_17]) bevat meer informatie over hoe foutcondities werken.

Meer specifiek, de tabel [Welke foutcondities zijn beschikbaar?]([LINK_URL_18]) helpt u om overzicht te krijgen van de foutcondities die beschikbaar zijn voor een Full Page Check.

### Gebruikersrechten voor controleregels

Uptrends' systeem voor [gebruikersrechten]([LINK_URL_19]) is opgezet om te definiëren welke teams of medewerkers toegang hebben tot welke items. Er zijn verschillende gebruikersrechten voor het maken/verwijderen, bekijken en bewerken van activiteiten.

- [Gebruikersrechten voor controleregels]([LINK_URL_20])

### Meer controleregelinstellingen

De volgende instellingen zijn optioneel in de zin dat de controleregel ook werkt als deze niet zijn gedefinieerd. Echter, om de monitoring volledig te benutten en aan uw situatie aan te passen, moeten de volgende instellingen worden geconfigureerd.

- [Controlestations]([LINK_URL_21])
- [Onderhoudsperiodes]([LINK_URL_22])
- [Controleregelgroepen]([LINK_URL_23])


## Controleregeldata en rapportage

Nadat uw controleregel is ingesteld en actief is (monitoring), begint u met het verzamelen van data over de performance. Van elke controleregelcheck wordt een aantal meetgegevens verzameld en opgeslagen. Deze gegevens worden weergegeven in de details van de controleregelcheck. Ga naar [SHORTCODE_5] Monitoring > Controleregel log [SHORTCODE_6] en klik op een van de items in de lijst om de details van de controle te openen.

### Details van de controleregelcheck

De details van de controle tonen de [basisset van laadtijdmetingen]([LINK_URL_24]) (*resolvetijd*, *verbindingstijd*, *downloadtijd* en *totale tijd*). Daarnaast bevatten uw FPC-resultaten een gedetailleerde [watervalgrafiek]([LINK_URL_25]).

 Een watervalgrafiek is een visuele weergave van het laden van de pagina, voor elk afzonderlijk element dat werd geladen. Het bevat informatie zoals het IP-adres van de elementbron, alle request en response headers, elementgrootte en een gedetailleerd overzicht van de [laadtijden van individuele elementen]([LINK_URL_26]).

### Extra kengetallen en functies [ANCHOR_2]

Voor [browsertypes met extra kengetallen]([LINK_URL_27]) kunt u nog meer informatie krijgen, zoals [W3C Navigatietijden]([LINK_URL_28]), [Core Web Vitals]([LINK_URL_29]), [tijdlijn screenshots]([LINK_URL_30]) en de optie om een [DNS bypass]([LINK_URL_31]) te gebruiken.

Het volledige scala aan aanvullende data en functies wordt uitgelegd in het knowledgebase-artikel [Extra kengetallen en functies]([LINK_URL_32]).

## Credits

Browser-controleregels gebruiken Browser-credits om u controleregels te laten creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]([LINK_URL_33]) voor meer informatie.