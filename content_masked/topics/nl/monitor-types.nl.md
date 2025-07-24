{
  "hero": {
    "title": "Controleregeltypes"
  },
  "title": "Controleregeltypes",
  "summary": "Krijg een overzicht van alle controleregeltypes die Uptrends te bieden heeft, van eenvoudige beschikbaarheid tot complexe transacties.",
  "url": "[URL_BASE_TOPICS]basics/controleregeltypes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends biedt een breed scala aan controleregeltypes, elk gericht op uw specifieke monitoringbehoeften. Elke synthetic controleregel gebruikt [credits]([LINK_URL_1]) om de prijzen voor verschillende monitoringdiensten te berekenen.

Dit artikel biedt een overzicht van hoe elk type controleregel de prestaties van uw website controleert om u op weg te helpen.

[SHORTCODE_1] **Opmerking:** U kunt meerdere controleregeltypes gebruiken samen met [Real User Monitoring]([LINK_URL_2]) om de werkelijke prestaties van uw website te meten op basis van de ervaring van de gebruiker vanuit hun eigen netwerk, gebruikte browsers en andere activiteiten. [SHORTCODE_2]

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

[SHORTCODE_3] **Opmerking:** Het controleregeltype **HTTP** is niet langer beschikbaar voor nieuwe gebruikers. Uptrends heeft de functionaliteit van **HTTPS**-controleregels uitgebreid om de beschikbaarheid van HTTP-websites te kunnen blijven controleren. [SHORTCODE_4]

Voor meer informatie over uptime-controleregels en hun types, zie [Uptime-controleregels]([LINK_URL_3]).

## Browser-controleregels (Full Page Check)

Een Browser-controleregel, ook bekend als een Full Page Check (FPC) of Real Browser-controleregel, controleert de laadprestaties van de pagina’s van uw website volledig op elementniveau. Deze controleregel opent een echte browser om te simuleren wat gebruikers zien bij een bezoek aan uw website.

Het onderzoekt hoe uw website van begin tot eind laadt, rekening houdend met hoe elk pagina-element (zoals scripts, CSS-bestanden, afbeeldingen en inhoud van derden) zich gedraagt. Browser-controleregels bieden ook informatie over de kengetallen [Core Web Vitals]([LINK_URL_4]) en [W3C Navigatietijden]([LINK_URL_5]) en een [Watervalgrafiek]([LINK_URL_6]) van uw website.

Deze controleregel controleert zo vaak als eens in de vijf minuten en geeft u een idee van de uptime, maar met minder nauwkeurigheid dan een uptime-controleregel. Om het verschil te weten tussen basiscontroles en echte browserchecks, raadpleegt u [Eenvoudige webpaginacontroles versus echte browser checks]([LINK_URL_7]). Raadpleeg [Browser monitoring]([LINK_URL_8]) voor meer informatie.

## API-controleregels

Een API-controleregel is een krachtige controleregel die controles uitvoert op een single-step API-call of complexe multi-step API-calls. Deze controleregel beschikt over een no-code (UI-gebaseerde) oplossing en [aangepaste scripting]([LINK_URL_9]) om HTTP requests en responses gemakkelijk te testen, rekening houdend met uw monitoringbehoeften.

U kunt ook aangepaste logica of [door de gebruiker gedefinieerde functies]([LINK_URL_10]) toevoegen, [aangepaste variabelen]([LINK_URL_11]) definiëren, [assertions]([LINK_URL_12]) gebruiken en meer API-gerelateerde mogelijkheden.  

### Types API-controleregels

De verschillende types API-controleregels zijn de volgende:

- [Multi-step API (MSA)-controleregel]([LINK_URL_13]) — het primaire API-monitoringtype met geavanceerdere en krachtigere functies vergeleken met Webservice HTTP- en HTTPS-controleregels.  
- [Postman API-controleregel]([LINK_URL_14]) — een controleregel waarmee u API-controles kunt maximaliseren door een Postman-werkruimtecollectie uit te voeren op het Uptrends-controlestationnetwerk. 
- [Webservice HTTP- en HTTPS-controleregels]([LINK_URL_15]) — een klassiek type HTTP-controleregel dat alleen basiscontroles uitvoert op de uptime en beschikbaarheid van de API.

[SHORTCODE_5] **Opmerking:** Voor API-monitoring zijn de controleregeltypes **Webservice HTTP en Webservice HTTPS** niet langer beschikbaar voor nieuwe gebruikers. Uptrends raadt aan om in plaats daarvan de Multi-step API-controleregel te gebruiken om uw API-gedrag optimaal te controleren. [SHORTCODE_6]

Raadpleeg [API-monitoring]([LINK_URL_16]) voor meer informatie over API-controleregels.

## Transactie-controleregels

Een Transactie-controleregel, ook bekend als een Webapplicatie- of gebruikerstraject-controleregel, simuleert gebruikersactiviteiten via een echte browser om de prestaties van uw website te controleren.

Stel u een echte gebruiker voor die met uw website interacteert via een browservenster. Ze vullen formulieren in, klikken op knoppen en maken selecties terwijl ze door uw site navigeren. Met transactie-controleregels kunt u die gebruiker nu vervangen door een robot die precies hetzelfde doet. Deze robot is een Uptrends-controlestationcomputer die een Chrome-browser opent en een script gebruikt om op uw site te navigeren en deze te testen. Deze scripts worden uitgevoerd om dezelfde interacties uit te voeren die uw gebruikers elke dag doen.

Transactie-controleregels bevatten de [ITRS Uptrends Transaction recorder]([LINK_URL_17]) om u te helpen uw transacties te automatiseren. Dit is een Chrome-extensie die uw scherm opneemt terwijl u door uw transacties klikt. Zodra uw transacties succesvol zijn opgenomen, kunt u die opslaan als een controleregel en worden er scripts gegenereerd op basis van de opname.

Om te beginnen met het instellen van een transactie-controleregel kunt u een van de volgende dingen doen:

- Creëer een transactie-controleregel helemaal zelf met de [transactiestap-editor]([LINK_URL_18]).
- [Download en gebruik de transaction recorder]([LINK_URL_19]) om in eerste instantie scripts te creëren die u later ook kunt bewerken en beheren.
- Laat het Uptrends Support-team uw opname gebruiken om uw script voor u te schrijven en te testen.

Voor meer informatie over transactie-controleregels, zie het volgende:

- [Overzicht transactie-controleregel]([LINK_URL_20])
- [Transactiemonitoring begrijpen]([LINK_URL_21])
- [De ITRS Uptrends Transaction recorder gebruiken: tutorial over het gebruikerstraject in een winkel]([LINK_URL_22]) — stapsgewijze handleiding voor het gebruik van de transaction recorder.