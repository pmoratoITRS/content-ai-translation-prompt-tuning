{
  "hero": {
    "title": "Controleregeltypes"
  },
  "title": "Controleregeltypes",
  "summary": "Krijg een overzicht van alle controleregeltypes die Uptrends te bieden heeft, van eenvoudige beschikbaarheid tot complexe transacties.",
  "url": "/support/kb/basics/controleregeltypes",
  "translationKey": "https://www.uptrends.com/support/kb/basics/monitor-types"
}

Uptrends biedt een breed scala aan controleregeltypes, elk gericht op uw specifieke monitoringbehoeften. Elke synthetic controleregel gebruikt [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="nl" >}}) om de prijzen voor verschillende monitoringdiensten te berekenen.

Dit artikel biedt een overzicht van hoe elk type controleregel de prestaties van uw website controleert om u op weg te helpen.

{{< callout >}} **Opmerking:** U kunt meerdere controleregeltypes gebruiken samen met [Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="nl" >}}) om de werkelijke prestaties van uw website te meten op basis van de ervaring van de gebruiker vanuit hun eigen netwerk, gebruikte browsers en andere activiteiten. {{< /callout >}}

## Uptime-controleregels (Basiscontroles)

Een Uptime-controleregel voert basiscontroles uit op uw websites. Het controleert de beschikbaarheid van de pagina en verwacht een 200-responsstatuscode. Deze controleregel kijkt alleen naar de eerste respons van uw website en scant pagina-elementen of andere specifieke websitecomponenten niet volledigs. 

Een uptime-controleregel controleert zo vaak als één keer per minuut, wat een nauwkeuriger rapport geeft van de uptime van de pagina vergeleken met Browser- of Full Page Check-controleregels.

### Types Uptime-controleregels

De verschillende types Uptime-controleregels zijn de volgende:

- Webpagina checks — **HTTP**- en **HTTPS**-controleregels (de laatste meer aan te raden dan HTTP
- Geavanceerde checks — **DNS**-, **SSL Certificaat**-, **SFTP**- en **FTP**-controleregels
- Mailservers — **SMTP**-, **POP3**- en **IMAP**-controleregels
- Databaseservers — **Microsoft SQL servers**- en **MySQL**-controleregels
- Netwerk checks — **Ping**- en **Connect**-controleregels

{{< callout >}} **Opmerking:** Het controleregeltype **HTTP** is niet langer beschikbaar voor nieuwe gebruikers. Uptrends heeft de functionaliteit van **HTTPS**-controleregels uitgebreid om de beschikbaarheid van HTTP-websites te kunnen blijven controleren. {{< /callout >}}

Voor meer informatie over uptime-controleregels en hun types, zie [Uptime-controleregels]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}}).

## Browser-controleregels (Full Page Check)

Een Browser-controleregel, ook bekend als een Full Page Check (FPC) of Real Browser-controleregel, controleert de laadprestaties van de pagina’s van uw website volledig op elementniveau. Deze controleregel opent een echte browser om te simuleren wat gebruikers zien bij een bezoek aan uw website.

Het onderzoekt hoe uw website van begin tot eind laadt, rekening houdend met hoe elk pagina-element (zoals scripts, CSS-bestanden, afbeeldingen en inhoud van derden) zich gedraagt. Browser-controleregels bieden ook informatie over de kengetallen [Core Web Vitals]({{< ref path="" lang="nl" >}}) en [W3C Navigatietijden]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}) en een [Watervalgrafiek]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="nl" >}}) van uw website.

Deze controleregel controleert zo vaak als eens in de vijf minuten en geeft u een idee van de uptime, maar met minder nauwkeurigheid dan een uptime-controleregel. Om het verschil te weten tussen basiscontroles en echte browserchecks, raadpleegt u [Eenvoudige webpaginacontroles versus echte browser checks]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="nl" >}}). Raadpleeg [Browser monitoring]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="nl" >}}) voor meer informatie.

## API-controleregels

Een API-controleregel is een krachtige controleregel die controles uitvoert op een single-step API-call of complexe multi-step API-calls. Deze controleregel beschikt over een no-code (UI-gebaseerde) oplossing en [aangepaste scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="nl" >}}) om HTTP requests en responses gemakkelijk te testen, rekening houdend met uw monitoringbehoeften.

U kunt ook aangepaste logica of [door de gebruiker gedefinieerde functies]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="nl" >}}) toevoegen, [aangepaste variabelen]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="nl" >}}) definiëren, [assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}}) gebruiken en meer API-gerelateerde mogelijkheden.  

### Types API-controleregels

De verschillende types API-controleregels zijn de volgende:

- [Multi-step API (MSA)-controleregel]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) — het primaire API-monitoringtype met geavanceerdere en krachtigere functies vergeleken met Webservice HTTP- en HTTPS-controleregels.  
- [Postman API-controleregel]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="nl" >}}) — een controleregel waarmee u API-controles kunt maximaliseren door een Postman-werkruimtecollectie uit te voeren op het Uptrends-controlestationnetwerk. 
- [Webservice HTTP- en HTTPS-controleregels]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/monitoring-web-services" lang="nl" >}}) — een klassiek type HTTP-controleregel dat alleen basiscontroles uitvoert op de uptime en beschikbaarheid van de API.

{{< callout >}} **Opmerking:** Voor API-monitoring zijn de controleregeltypes **Webservice HTTP en Webservice HTTPS** niet langer beschikbaar voor nieuwe gebruikers. Uptrends raadt aan om in plaats daarvan de Multi-step API-controleregel te gebruiken om uw API-gedrag optimaal te controleren. {{< /callout >}}

Raadpleeg [API-monitoring]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) voor meer informatie over API-controleregels.

## Transactie-controleregels

Een Transactie-controleregel, ook bekend als een Webapplicatie- of gebruikerstraject-controleregel, simuleert gebruikersactiviteiten via een echte browser om de prestaties van uw website te controleren.

Stel u een echte gebruiker voor die met uw website interacteert via een browservenster. Ze vullen formulieren in, klikken op knoppen en maken selecties terwijl ze door uw site navigeren. Met transactie-controleregels kunt u die gebruiker nu vervangen door een robot die precies hetzelfde doet. Deze robot is een Uptrends-controlestationcomputer die een Chrome-browser opent en een script gebruikt om op uw site te navigeren en deze te testen. Deze scripts worden uitgevoerd om dezelfde interacties uit te voeren die uw gebruikers elke dag doen.

Transactie-controleregels bevatten de [ITRS Uptrends Transaction recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}) om u te helpen uw transacties te automatiseren. Dit is een Chrome-extensie die uw scherm opneemt terwijl u door uw transacties klikt. Zodra uw transacties succesvol zijn opgenomen, kunt u die opslaan als een controleregel en worden er scripts gegenereerd op basis van de opname.

Om te beginnen met het instellen van een transactie-controleregel kunt u een van de volgende dingen doen:

- Creëer een transactie-controleregel helemaal zelf met de [transactiestap-editor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}).
- [Download en gebruik de transaction recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}) om in eerste instantie scripts te creëren die u later ook kunt bewerken en beheren.
- Laat het Uptrends Support-team uw opname gebruiken om uw script voor u te schrijven en te testen.

Voor meer informatie over transactie-controleregels, zie het volgende:

- [Overzicht transactie-controleregel]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}})
- [Transactiemonitoring begrijpen]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="nl" >}})
- [De ITRS Uptrends Transaction recorder gebruiken: tutorial over het gebruikerstraject in een winkel]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/tutorial-introduction" lang="nl" >}}) — stapsgewijze handleiding voor het gebruik van de transaction recorder.