{
  "hero": {
    "title": "Eenvoudige webpaginacontroles versus echte browser checks"
  },
  "title": "Eenvoudige webpaginacontroles versus echte browser checks",
  "summary": "Leer wat het verschil is tussen een eenvoudige webpaginacontrole en een controle die een echte browser gebruikt.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/eenvoudige-webpaginacontroles-versus-echte-browser-checks",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/basic-webpage-checks-versus-real-browser-checks"
}

Wanneer het om [synthetic monitoring](/producten/synthetics/synthetic-monitoring) gaat, hebt u twee mogelijkheden voor het monitoren van uw webpagina: basiscontroles en controles die een echte browser gebruiken. Maar wat is het verschil tussen deze twee types controleregels? Het voornaamste verschil is hoe Uptrends de respons behandelt.

#### Het korte antwoord

Basiscontroles kijken alleen naar de eerste respons; pagina-elementen zoals scripts, CSS-bestanden en afbeeldingen worden nooit opgehaald of uitgevoerd. Echte browser checks downloaden en laden alle inhoud van de hele pagina (scripts, CSS-bestanden, afbeeldingen en third-party inhoud) daadwerkelijk in een browservenster.

## Basiscontroles

Wanneer een controlestations een basiscontrole (HTTP / HTTPS) uitvoert, verzendt het controlestation een verzoek voor de pagina. Het controlestation ontvangt de respons en kijkt naar een paar belangrijke componenten. Op basis van uw instellingen kan een basiscontrole de volgende dingen meten:

-   Resultcode
-   Responstijd
-   Paginalengte in bytes
-   Inhoudmatch

De controleregel laadt de responsinhoud nooit in een browser, dus worden pagina-elementen zoals CSS-bestanden, scriptbestanden, inhoud van derden en afbeeldingen nooit gedownload, geparset of geladen. Met een basiscontrole bent u niet op de hoogte van eventuele fouten of performanceproblemen die kunnen optreden bij het ophalen en laden van de volledige inhoud. Wat u wel weet is dat de site beschikbaar is, acceptabele codes retourneert, een minimumgrootte heeft en de gespecificeerde inhoud bevat. Een basiscontrole kan zo vaak als één keer per minuut gebeuren, wat een nauwkeuriger beeld geeft van de beschikbaarheid van de pagina.

## Echte browser checks

Wanneer een controlestation een echte browser check uitvoert ([Full page check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}), [Transactie monitor]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="nl" >}})), vraagt het controlestation de pagina op en laadt het de respons in een echte browser. Het controlestation laadt alle inhoud van de hele pagina (CSS, scriptbestanden, aanvullende HTML-bestanden, third-party inhoud en afbeeldingen). Iedere request en respons wordt gecontroleerd op performance en fouten. De echte browser checks zijn zo vaak als elke vijf minuten gepland, wat u een gesimuleerd beeld geeft van de ervaring van een feitelijke gebruiker met uw pagina. Met een echte browser check kunt u een indruk krijgen van uptime, maar deze is minder nauwkeurig dan met een basiscontrole.
