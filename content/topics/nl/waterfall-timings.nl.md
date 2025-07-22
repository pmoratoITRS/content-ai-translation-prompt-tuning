{
  "hero": {
    "title": "Waterval timings"
  },
  "title": "Waterval timings",
  "url": "/support/kb/synthetic-monitoring/monitoring-resultaten/waterval-timings",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/waterfall-timings",
  "tableofcontents": true
}

Voor sommige soorten controleregels kunt u een watervalgrafiek krijgen als resultaat van de controleregelcheck. De waterval bevat een [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}) die een grafische weergave is van hoe lang het duurde voordat de pagina-elementen waren geladen. 

Als u over de grafiek hovert (zweeft), kunt u inzoomen op de timings per element. 

![screenshot waterval timings popup](/img/content/scr_waterfall_chart-popup-detail.min.png)

## Stappen van het laadproces

De timings worden opgesplitst door een aantal stappen die nodig zijn om het element te laden. Boven de watervalgrafiek staat een legenda met de kleuren van de stappen: 

![screenshot waterval timings legenda](/img/content/scr_waterfall_chart-timings-legend.min.png)

Alle timings worden weergegeven in milliseconden. Hieronder worden de verschillende stappen in het laadproces beschreven.

### Start time

De waarde *Start time* is de enige waarde in deze verzameling die geen duur aangeeft, maar een tijdstip. Preciezer gezegd: dit is het tijdstip waarop het laden van het gerelateerde pagina-element begon binnen de volledige tijdlijn van de pagina.

### Wachtrij

De *Wachtrij*-tijd is de duur gedurende welke een request in de wachtrij stond.

Er zijn verschillende redenen om in de wachtrij te staan:

- Er bestaat een request met een hogere prioriteit. Afbeeldingen hebben bijvoorbeeld vaak een lagere prioriteit dan scripts of stylesheets.
- De request wacht tot een TCP-socket is vrijgegeven.
- Er zijn al 6 TCP-verbindingen open voor dezelfde oorsprong. Deze reden is alleen van toepassing op HTTP/1.0 en HTTP/1.1. 
- De browser wijst ruimte toe in de schijfcache.

### Resolve

Dit is de tijd die de browser nodig had om de DNS-lookup voor het pagina-element uit te voeren. De DNS-lookup wordt gebruikt om een domeinnaam of URL te vertalen naar het bijbehorende IP-adres.

### TCP Connect

*TCP Connect* is de tijd die nodig is om de daadwerkelijke TCP-verbinding van de client naar het IP-adres van de webserver tot stand te brengen.

### HTTPS Handshake

Een handshake bestaat uit een aantal substappen die nodig zijn om een veilige communicatie tussen client en server op gang te brengen. Deze stap wordt ook wel een TLS handshake genoemd. 

### Verzenden

Zodra de verbinding tot stand is gebracht en er over veilige communicatie is onderhandeld, stuurt de client een request naar de webserver. 

### Wachten

Dit is de tijd die nodig is tussen het verzenden van een request en de response van de webserver.

### Ontvangen

Deze stap legt de tijd vast die nodig is om de response van de webserver te ontvangen.

### Timeout

Deze timing is alleen van toepassing als de request is mislukt. In dat geval wordt de periode weergegeven waarin de client geen response heeft ontvangen. In dit geval zijn er alleen een starttijd en time-outperiode, geen andere timings.
