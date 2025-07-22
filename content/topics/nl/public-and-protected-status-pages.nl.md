{
  "hero": {
    "title": "Publieke en beveiligde statuspagina's"
  },
  "title": "Publieke en beveiligde statuspagina's",
  "summary": "Overzicht van publieke statuspagina's en het instellen van een beveiligde statuspagina voor wanneer u de zichtbaarheid wilt beperken.",
  "url": "/support/kb/dashboards-en-rapportages/statuspaginas/publieke-en-beveiligde-statuspaginas",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages"
}

## Publieke statuspagina's

Op een publieke statuspagina kunt u uptime-informatie van uw controleregels publiceren, zodat het grote publiek actuele informatie heeft over de beschikbaarheid van uw sites en diensten. U kunt bepalen welke controleregels u in uw statuspagina wilt opnemen en het uiterlijk van de pagina aanpassen zodat deze past bij de stijl van uw merk. 
Technisch gesproken is een publieke statuspagina een gespecialiseerd dashboard voor websitemonitoring dat is ontworpen om de beschikbaarheidsstatus van een gemonitorde website, webservice of server publiekelijk te tonen.

De publieke statuspagina toont de huidige status van de controleregel (kleurcode aan het begin van elke rij) en de SLA-status (pictogrammen in de tabel):

![screenshot overzicht publieke statuspagina](/img/content/scr_public-status-page-overview.min.png)

Als u meer details wilt bekijken en de uptimedata van een controleregel wilt zien, klikt u op de rij van de betreffende controleregel:

![screenshot details publieke statuspagina](/img/content/scr_public-status-page-monitor-details.min.png)

### Redenen om een publieke statuspagina te gebruiken

Ga naar de pagina [Waar worden publieke statuspagina's voor gebruikt?]({{< ref path="support/kb/dashboards-and-reporting/status-pages/why-use-public-status-pages" lang="nl" >}}) om na te gaan of een publieke statuspagina geschikt is voor u.

### Een publieke statuspagina instellen

Leer hoe u publieke statuspagina's instelt en configureert in het Knowledge Base-artikel [Publieke statuspagina configureren]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration" lang="nl" >}}).

## Beveiligde statuspagina's

{{< callout >}} **Opmerking**: Beveiligde statuspagina's zijn een functie van het Enterprise-abonnement. {{< /callout >}}

Misschien wilt u de status van uw sites en diensten delen met iemand buiten uw organisatie, zonder dit aan de rest van de wereld te laten zien. Om dit te doen kunt u de publieke statuspagina-functie gebruiken om een beveiligde statuspagina te maken. Een beveiligde statuspagina betekent dat een inlognaam en wachtwoord nodig zijn om toegang te krijgen tot die pagina. Wanneer een persoon buiten uw organisatie die login gebruikt, zien ze alleen die statuspagina; ze zullen geen ander dashboard zien en geen wijzigingen kunnen aanbrengen. Omdat de statuspagina beveiligd is, blijft deze volledig onzichtbaar voor de buitenwereld.

### Een beveiligde statuspagina creëren en operators instellen

Lees het Knowledge Base-artikel [Een beveiligde statuspagina instellen]({{< ref path="support/kb/dashboards-and-reporting/status-pages/protected-status-page-configuration" lang="nl" >}}) voor aanwijzingen over het instellen van een nieuwe beveiligde statuspagina.

### Toegang tot een beveiligde statuspagina

Nadat Support heeft bevestigd dat de gebruikersrechten zijn verleend, kunt u doorgaan en de mensen buiten uw organisatie instrueren om de beveiligde statuspagina te gaan gebruiken. Zij kunnen er op twee eenvoudige manieren naartoe navigeren: 

- Ze kunnen naar de [Uptrends-app](https://app.uptrends.com) gaan en de inloggegevens invoeren die u voor hen heeft gemaakt. Er wordt een lijst met beveiligde statuspagina's weergeven waartoe ze toegang hebben. 
- U kunt ze ook de *Preview*-link (URL) geven van de beveiligde statuspagina. Om de URL te vinden gaat u naar {{< AppElement type="menuitem" >}} Accountinstellingen > Publieke statuspagina's {{< /AppElement >}} en bekijkt u de *Preview* naast de pagina. Van deze URL kan een bladwijzer worden gemaakt voor hergebruik. Wanneer iemand deze voor het eerst bezoekt, moeten ze inloggen.

Houd er rekening mee dat een beveiligde statuspagina altijd toegankelijk is voor administrators (operators die lid zijn van de operatorgroep *Administrators*) en voor reguliere operators wanneer ze ingelogd zijn.
