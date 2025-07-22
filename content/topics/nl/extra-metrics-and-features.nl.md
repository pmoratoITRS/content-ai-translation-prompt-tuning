{
  "hero": {
    "title": "Browsertypes met extra kengetallen"
  },
  "title": "Browsertypes met extra kengetallen",
  "summary": "Sommige browsertypen bieden meer informatie dan andere en verbeterde functies. Lees hier welke informatie dat is en welke functies anders zijn.",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/extra-kengetallen-en-functies",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/extra-metrics-and-features",
  "tableofcontents": true
}

De volgende Full Page Check of transactie [browsertypes]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="nl" >}}) ondersteunen een aantal extra kengetallen en functies:

- Chrome met extra kengetallen
- Microsoft Edge

Chrome met extra kengetallen ondersteunt Core Web Vitals en W3C Navigatietijden voor transactiemonitoring.

## Functies

### Native controles

Voor de ondersteunde browsertypes meet de FPC de performance rechtstreeks in de browser. Hierdoor kan de browser zo natuurlijk mogelijk functioneren.

### Ondersteuning en headers voor HTTP2, HTTP3 en QUIC

Naast het HTTP-protocol worden het HTTP2-, HTTP3- en QUIC-protocol ondersteund.

Requests gedaan door een protocol zoals HTTP2, HTTP3 en QUIC zullen andere headers hebben dan bij het HTTP-protocol. Er zijn geen X-Uptrends headers, zoals X-Uptrends-PortInfo en X-Blocked-By-Uptrends.

### Inhoud match

Alleen het eindresultaat wordt beoordeeld bij het matchen van HTML-inhoud. Inhoud die tijdens een redirect wordt weergegeven, activeert geen inhoud match. 

### URL blokkeren

Bij het navigeren naar een site zal de navigatie slagen, zelfs als de URL van die site in de lijst met geblokkeerde URL's staat. Een FPC van een browsertype met extra kengetallen blokkeert de navigatie niet. Andere elementen waar de site naar verwijst, zoals afbeeldingen, worden echter geblokkeerd.

### Gecachete elementen

Omdat Uptrends performance-informatie uit de browser haalt, kunnen gecachete elementen worden weergegeven. Het is mogelijk om ze desgewenst te filteren.

### DNS bypass

U kunt kiezen om een DNS bypass toe te voegen. Een Full Page Check laadt uw pagina met een echte browser, downloadt elk element en geeft vervolgens een watervalgrafiek weer om die elementen te inspecteren. De [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="nl" >}}) zorgt ervoor dat de webpagina wordt omgezet in een domeinnaam of IP-adres dat u heeft opgegeven. Dit overschrijven van DNS is ook beschikbaar voor Transacties. 

## Kengetallen

### Meettechnieken

De resultaten (tijden en totaal aantal bytes) in een browsertype met extra kengetallen versus andere browsertypes zijn verschillend.

De FPC (browsertypes met extra kengetallen) ondersteunt nieuwe protocollen zoals HTTP2 en HTTP3 en is nauw geïntegreerd met de browser. Hierdoor kan de gegenereerde waterval verschillen van die van een FPC met een ander browsertype. U kunt verwachten dat er meer gelijktijdige requests worden weergegeven, die sneller worden overgebracht. Omdat de meting sneller of langzamer kan zijn, kan het totale aantal bytes ook verschillen, omdat Uptrends een andere hoeveelheid achtergrondactiviteit vastlegt na het laden van de pagina (bijvoorbeeld een video die wordt geladen of een JavaScript- serviceworker die achtergrondtaken uitvoert).

### Core Web Vitals 

Core Web Vitals zijn standaard kengetallen van Google die worden gebruikt om de performance van uw website te begrijpen. Uptrends meet deze kengetallen en rapporteert ze in de controleresultaten. U kunt de resultaten op een dashboard weergeven met een aangepaste rapporttegel van het type [Eenvoudige lijst/grafiek]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="nl" >}}) en kiezen uit de lijst met Core Web Vitals-data.

Die metingen kunnen afwijken van wat wordt gemeten met de Lighthouse-tool. 
De Lighthouse-tool van Google gebruikt een andere meettechniek dan Uptrends. Wij gebruiken een browser die een website bezoekt zoals een normale gebruiker dat zou doen. De Lighthouse-tool voert eerst een warming-up uit en bezoekt vervolgens de site meerdere keren om een gemiddelde te bepalen. De Lighthouse-tool activeert ook niet bepaalde gebruikersinvoerchecks, die onze meettechniek en normale gebruikers doen. Het simuleert ook een tragere verbinding met bandbreedtebegrenzing. Daarom kunnen de door Lighthouse gerapporteerde Core Web Vitals afwijken van metingen van Uptrends.

Ga naar het artikel over [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) voor meer informatie over deze kengetallen.

### W3C-kengetallen

Het Word Wide Web Consortium (W3C) heeft een reeks navigatietijden gedefinieerd die essentieel zijn voor het laden van een webpagina. Uptrends heeft een aantal van die timings overgenomen om te meten en weer te geven in rapporten. U kunt de resultaten op een dashboard weergeven met een aangepaste rapporttegel van het type [Eenvoudige lijst/grafiek]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="nl" >}}) en kiezen uit de lijst met W3C Navigatietijdendata.

Bekijk het Knowledge Base-artikel [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}) voor meer informatie over de geïmplementeerde navigatietijden.

[Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) en W3C Navigatietijden zijn ook beschikbaar voor uw [transacties]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}}). Als u deze extra kengetallen voor transactiemonitoring wilt inschakelen, selecteert u **Chrome met extra kengetallen** in het menu *Browser type* op het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} in de controleregelinstellingen. U vindt de extra kengetallen die zijn opgenomen in de transactiewaterval]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}}), in stappen waarvoor een waterval is ingeschakeld. (Alleen beschikbaar voor [Business- en Enterprise-accounts]({{< ref path="/pricing" lang="nl" >}}).)

### Laadtijd: W3C total time of Netwerktijd 

Een Full Page Check- of transactiecontroleregel met het browsertype *met extra kengetallen* biedt de opties om de laadtijd te meten op basis van de *W3C load event* of de *Netwerktijd*. 

#### W3C total time

Bij het kiezen van de W3C total time voor metingen wordt de W3C load event end metric gebruikt. De W3C load event wordt gedetailleerder beschreven in https://www.w3.org/TR/navigation-timing/#dom-performancetiming-loadend. 

In de Uptrends-app wordt dit kengetal niet berekend, deze komt rechtstreeks uit de browser, uit de ontwikkelaarstools van de browser om precies te zijn. 

U kunt de resultaten van de meting vinden in de controledetails van de controleregel. Kijk naar de *Load Event* van de *W3C Navigatietijden*-kengetallen.

![screenshot W3C Navigatietijden load event gemarkeerd](/img/content/scr_w3c-navigation-timing-load-event.min.png)

#### Netwerktijd

De Netwerktijd wordt gemeten door te wachten op een inactieve periode van netwerkactiviteit.

#### De laadtijdbasis voor een controleregel instellen

Om uw keuze te maken gaat u naar het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van de controleregelinstellingen. Selecteer in het gedeelte *Meting* een van de opties voor *Laadtijd baseren op*:

![screenshot van total time meting](/img/content/scr-fpc-choose-load-time-v2.min.png)

#### Verschillen in kengetallen en suggesties voor de te kiezen instelling

Er kan een behoorlijk groot verschil zijn tussen het meten van de laadtijd met W3C load time of Netwerktijd.
De resultaten (en verschillen) zijn sterk afhankelijk van wat er wordt gemonitord, bij b.v. een transactie die de W3C load event gebruikt veranderen de individuele laadtijden van de stappen bij gebruik van een andere methode, waardoor de totale tijd verandert. 

In een Full Page Check-controleregel ziet u mogelijk meer dan één navigatieactie, bijvoorbeeld wanneer er redirects zijn. De kengetallen worden per navigatie vastgelegd en opgeteld voor het volledige * W3C load event*-kengetal. 

In een transactiecontroleregel kunt u meerdere navigaties binnen één stap hebben, d.w.z. meerdere navigatieacties of een navigatie die andere navigaties activeert. De laadtijden worden per stap opgeteld en vervolgens voor de hele transactie opgeteld tot het *total time*-kengetal. 
Er geldt een uitzondering: als er geen navigatie in de stap zit, maar b.v. een inhoudcontrole, is de tijd voor die stap 0 (anders dan bij gebruik van *Netwerktijd*). In dit geval is de netwerktijd niet de inactieve periode van netwerkactiviteit, maar wordt deze afgeleid van de uitvoeringstijd van de stappen.

Hier zijn enkele tips voor het kiezen van de optimale methode voor transacties:

- Als u wilt weten hoe snel uw pagina laadt - met andere woorden, u bent puur geïnteresseerd in het laden - dan is W3C load time de aanbevolen keuze.
- Als u meer wilt weten over de eindgebruikerservaring, bijvoorbeeld hoelang een gebruiker erover doet om de hele transactie te doorlopen, wordt het gebruik van de Netwerktijd aanbevolen. De reden is dat er met alles rekening wordt gehouden, ook stappen die geen navigaties zijn maar toch invloed hebben op de tijd die de gebruiker nodig heeft om de transactie te voltooien.

### Tijdlijn screenshots

De [tijdlijn van screenshots (ook bekend als filmstrip)]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}}) bevat een aantal screenshots die zijn gemaakt terwijl de gemonitorde webpagina werd geladen. De tijdlijn wordt boven de waterval weergegeven in de details van de controle:

![screenshot van filmstrip in details van de controle](/img/content/scr-filmstrip.min.png)

### Data-URL's in waterval

Elementen die zijn ingesloten in het HTML-document, zoals data-URL's, of die afkomstig zijn van JavaScript, zoals Blob-URL's, worden ook weergegeven in de waterval. U kunt indien nodig een filter toepassen.

### TLS-informatie

In de waterval van de details van de controle vindt u TLS-informatie voor elk element. 
U kunt de details van de waterval openen door op het plusteken naast het element te klikken:

![screenshot van TLS-info in waterval](/img/content/scr-TLS-info.min.png)


