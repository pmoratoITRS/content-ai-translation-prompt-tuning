{
  "hero": {
    "title": "Browser monitoring"
  },
  "title": "Browser monitoring",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/overzicht-browser-monitoring",
  "summary": "Het controleregeltype Full Page Check is het meest uitgebreide controleregeltype. Elk element wordt gedownload en geladen in een browser. Het rapport geeft uw resultaten weer in een gedetailleerd watervalrapport.",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
  "sectionlist": true
}

Uptrends Browser-controleregels, ook bekend als een Full Page Check (FPC), zijn een van de vele [controleregeltypes]({{< ref path="support/kb/basics/monitor-types" lang="nl" >}}) die Uptrends biedt. Dit controleregeltype verstrekt gedetailleerde performancedata over uw webpagina op elementniveau. Een FPC-controleregel laadt uw pagina in een echte browser, inclusief scripts, CSS, elementen van derden en andere websitecomponenten. Deze controleregel voltooit het laden van een pagina in een echte browser om de prestaties van de website nauwkeurig te meten zoals ervaren door uw eindgebruikers.

De FPC presenteert monitoringinformatie in de details van de controle, inclusief een [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}). Afhankelijk van het [browsertype]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="nl" >}}) dat u voor de controleregel kiest, zal er nog meer informatie zijn ([Extra kengetallen en functies]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}})).

Als u inhoud van derden op uw website wilt monitoren, gebruikt u de optie [Full Page Check+]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="nl" >}}).

## Een FPC-controleregel instellen {id="set-up-fpc"}

Het instellen van een FPC-controleregel begint met het creëren van de controleregel en vervolgens het kiezen van het browsertype, het controle-interval en dan het definiëren van foutcondities, het kiezen van controlestations en het instellen van meer specifieke opties zoals onderhoudsperiodes.

Bekijk voor de basisprincipes het Uptrends-artikel [Controleregeltypes - controleregels voor Website performance]({{< ref path="support/kb/basics/monitor-types#browser-monitors" lang="nl" >}}).

## Browser-controleregels (Full Page Checks (FPC))

Er zijn verschillende types Browser-controleregels waaruit u kunt kiezen:

- [Full Page Check (FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) — een controleregeltype dat alle elementen van de pagina controleert bij het laden van de pagina en data weergeeft in een uitgebreide [watervalgrafiek]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}).

- [Full Page Check \+ (FPC+)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="nl" >}}) — een optie onder de FPC-controleregel die alle elementen van de pagina, inclusief inhoud van derden, controleert bij het laden van de pagina. Deze controleregel geeft uw data ook weer in een uitgebreide [watervalgrafiek]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}).

Het gedeelte [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) bevat alle informatie over het toevoegen van dit type controleregel en het beheren van de instellingen.

De controleregelinstellingen worden uitgelegd in een aantal knowledgebase-artikelen, zoals hieronder vermeld.

### Algemene instellingen

Alle opties op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} van de controleregel zijn de fundamentele instellingen voor de FPC-controleregel.


- [Controle-interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="nl" >}})
- [Gelijktijdige monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="nl" >}})
- [Controleregelmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}})
- [Browsertype]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="nl" >}})
- [Controleregelnotities (optioneel)]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="nl" >}})

### Foutcondities

Een FPC-controleregel controleert standaard de beschikbaarheid van de opgegeven server-URL. Andere controles moeten worden gedefinieerd op het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}} tab van de controleregel.

Het knowledgebase-article [Foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}) bevat meer informatie over hoe foutcondities werken.

Meer specifiek, de tabel [Welke foutcondities zijn beschikbaar?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="nl" >}}) helpt u om overzicht te krijgen van de foutcondities die beschikbaar zijn voor een Full Page Check.

### Gebruikersrechten voor controleregels

Uptrends' systeem voor [gebruikersrechten]({{< ref path="support/kb/account/permissions" lang="nl" >}}) is opgezet om te definiëren welke teams of medewerkers toegang hebben tot welke items. Er zijn verschillende gebruikersrechten voor het maken/verwijderen, bekijken en bewerken van activiteiten.

- [Gebruikersrechten voor controleregels]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}})

### Meer controleregelinstellingen

De volgende instellingen zijn optioneel in de zin dat de controleregel ook werkt als deze niet zijn gedefinieerd. Echter, om de monitoring volledig te benutten en aan uw situatie aan te passen, moeten de volgende instellingen worden geconfigureerd.

- [Controlestations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/checkpoint-information" lang="nl" >}})
- [Onderhoudsperiodes]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="nl" >}})
- [Controleregelgroepen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="nl" >}})


## Controleregeldata en rapportage

Nadat uw controleregel is ingesteld en actief is (monitoring), begint u met het verzamelen van data over de performance. Van elke controleregelcheck wordt een aantal meetgegevens verzameld en opgeslagen. Deze gegevens worden weergegeven in de details van de controleregelcheck. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregel log {{< /AppElement >}} en klik op een van de items in de lijst om de details van de controle te openen.

### Details van de controleregelcheck

De details van de controle tonen de [basisset van laadtijdmetingen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="nl" >}}) (*resolvetijd*, *verbindingstijd*, *downloadtijd* en *totale tijd*). Daarnaast bevatten uw FPC-resultaten een gedetailleerde [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}).

 Een watervalgrafiek is een visuele weergave van het laden van de pagina, voor elk afzonderlijk element dat werd geladen. Het bevat informatie zoals het IP-adres van de elementbron, alle request en response headers, elementgrootte en een gedetailleerd overzicht van de [laadtijden van individuele elementen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="nl" >}}).

### Extra kengetallen en functies {id="chrome-extra-metrics"}

Voor [browsertypes met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types#chrome-extra-metrics" lang="nl" >}}) kunt u nog meer informatie krijgen, zoals [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}), [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}), [tijdlijn screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}}) en de optie om een [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="nl" >}}) te gebruiken.

Het volledige scala aan aanvullende data en functies wordt uitgelegd in het knowledgebase-artikel [Extra kengetallen en functies]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}).

## Credits

Browser-controleregels gebruiken Browser-credits om u controleregels te laten creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="nl" >}}) voor meer informatie.