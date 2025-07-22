{
  "hero": {
    "title": "Basisoverzicht"
  },
  "title": "Basisoverzicht",
  "summary": "Bent u helemaal nieuw bij Uptrends? Bekijk de artikelen hier voor een introductie en basiskennis van wat de Uptrends-app voor u kan doen.",
  "url": "/support/kb/basisprincipes/basisoverzicht",
  "translationKey": "https://www.uptrends.com/support/kb/basics/basics-overview",
  "sectionlist": false
}

Uptrends is een SaaS (Software as a Service) Digital Experience Monitoring-tool die gebruikers gedetailleerd inzicht biedt in de uptime en prestaties van hun websites en -diensten, vanuit het perspectief van de eindgebruiker. Uptrends is eenvoudig te configureren en ondersteunt een breed scala aan [controleregeltypes]({{< ref path="/support/kb/basics/monitor-types" lang="nl" >}}) voor elk monitoringscenario, alsmede [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="nl" >}}).

## Synthetic Monitoring

Met proactieve [synthetic monitoring]({{< ref path="/products/synthetics/synthetic-monitoring" lang="nl" >}}) gebruikt Uptrends zijn wereldwijde [netwerk van controlestations]({{< ref path="/checkpoints" lang="nl" >}}) om uw websites en processen 24/7 te controleren op beschikbaarheid en prestaties, vanaf locaties die relevant zijn voor uw bedrijf. Verschillende controleregeltypes zijn geschikt voor elk gebruiksscenario dat u heeft.

{{< Support/storylane url="https://app.storylane.io/demo/tqewkqp0c4ly" >}}

### Uptime monitoring {id="synthetic-monitoring"}

[Uptime monitoring]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring" lang="nl" >}}) is hoogfrequente monitoring van de beschikbaarheid van uw websites en -diensten. Controleregels zoals het [controleregeltype HTTPS]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https" lang="nl" >}}) controleren uw website op beschikbaarheid en correct functioneren, tot elke minuut, vanuit waar ook ter wereld.

![Een standaard controleregel log](/img/content/scr-basics-uptimelog_020224.min.png)

Er zijn andere types basiscontroleregels beschikbaar, zoals de [DNS-controleregel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="nl" >}}), die de juistheid van uw DNS-configuratie controleert door een DNS-server te bevragen, en de [controleregel SSL certificaat]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="nl" >}}) om de geldigheid van uw SSL-certificaten te controleren en alerts te sturen zodra deze niet langer correct zijn of binnenkort verlopen.

### Browsermonitoring {id="browser-monitoring"}

In tegenstelling tot uptime monitoring gebruikt [browser monitoring]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) een echte browser om uw websites te openen. Hierdoor laadt het controleregeltype Full Page Check (FPC) de pagina volledig, op precies dezelfde manier als uw eindgebruikers dat doen, waardoor een groot aantal gedetailleerde prestatiestatistieken wordt gegenereerd.

Dergelijke statistieken omvatten een [watervalgrafiek]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}) (een gedetailleerd overzicht van technische informatie en prestatiestatistieken voor elk afzonderlijk element waaruit de pagina bestaat), maar ook belangrijke kengetallen zoals [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) en [W3C Navigatietijden]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}), die van invloed kunnen zijn op uw klantervaring of de ranking in zoekmachines.

![voorbeeld Full Page Check resultaat](/img/content/scr-fpc-result-basics.min.png)

### Transactie- / Web Application monitoring {id="transaction-monitoring"}

Een [transactiecontroleregel (of Web Application-controleregel)]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="nl" >}}) laadt uw pagina in een echte browser en voert vervolgens een script uit om met de pagina te communiceren waarmee de acties van een echte gebruiker worden nagebootst. Dit controleregeltype kan worden gebruikt om volledige gebruikerstrajecten op uw website te testen, zoals logins, zoeken naar opgenomen producten, deze in een winkelwagen plaatsen en doorgaan naar het betaalscherm, formulieren invullen enzovoort.

Een typische gebruikersstroom, waarbij de gebruiker in verschillende stappen met uw website communiceert om een specifieke actie te voltooien, zal meerdere webservers, databases, API's of externe bronnen raken. Transactiemonitoring is de beste manier om te controleren of alle aspecten van uw kritische gebruikersstromen nog correct functioneren. Het is eenvoudig in te stellen, zonder dat scriptervaring vereist is, door gebruik te maken van de [transaction recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}), een plug-in voor Chrome.

![De transactiestapeditor](/img/content/scr-transaction-steps-basics_020224.min.png)

#### API monitoring

Het [controleregeltype Multi-step API (MSA)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring" lang="nl" >}}) is voor uw backend/API's wat transactiemonitoring voor uw frontend/gebruikerstrajecten is. API's maken communicatie tussen applicaties mogelijk en vormen de ruggengraat van het moderne internet.

Uw organisatie is vrijwel zeker op de een of andere manier afhankelijk van meerdere API's, maar inzicht in eventuele problemen kan lastig zijn omdat API-communicatie en -interacties op de achtergrond plaatsvinden. Met Multi-step API-monitoring kunt u uw API's rechtstreeks controleren door requests opnieuw aan te maken en de response te verifiëren op juistheid, volledigheid en stiptheid.

## Real User Monitoring

Naast de ondersteuning van synthetic monitoring biedt Uptrends [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="nl" >}}). RUM gebruikt een eenvoudig script dat is ingesloten in de HTML van uw pagina om in realtime daadwerkelijke performancedata van uw echte eindgebruikers te verzamelen. Als aanvulling op synthetic data, kan RUM u inzicht geven in de ervaringen van uw echte gebruikers, waar deze zich ook bevinden, en RUM kan u ook data verstrekken over de set-ups van uw gebruikers zoals welke browsers en besturingssystemen zij gebruiken.

![Een voorbeeld van RUM-data](/img/content/scr-rum-map-basics_020224.min.png)

## Alerting

De monitoring van Uptrends wordt geleverd met krachtige en veelzijdige [alerting]({{< ref path="/support/kb/alerting" lang="nl" >}}). Bepaal wanneer alerts moeten worden gegenereerd en welke berichten moeten worden verzonden met [alertdefinities]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="nl" >}}). Gebruik onze kant-en-klare [integraties]({{< ref path="/support/kb/alerting/integrations/what-are-integrations" lang="nl" >}}) om berichten te versturen via e-mail, SMS, telefoontje of een extern platform. U kunt ook een [aangepaste integratie]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="nl" >}}) bouwen om uw Uptrends-alerts te verbinden met elk bestaand extern platform, zelfs platforms die niet op de integratiepagina staan.

