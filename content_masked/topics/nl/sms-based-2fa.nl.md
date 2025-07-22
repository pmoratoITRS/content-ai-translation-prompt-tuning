{
  "hero": {
    "title": "Sms-gebaseerde 2FA"
  },
  "title": "Werken met sms-gebaseerde 2FA in transacties",
  "summary": "Leer hoe u sms-gebaseerde 2FA instelt voor uw transactiecontroleregels.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/sms-gebaseerde-2fa",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In een wereld waar beveiliging en bescherming van persoonsgegevens steeds belangrijker worden, willen veel organisaties niet langer vertrouwen op slechts één enkele inlogactie om toegang tot webapplicaties te beveiligen. Om de kans te vergroten dat een echte gebruiker veilig kan worden geïdentificeerd tijdens een inlogproces, maken webapplicaties nu gebruik van multifactorauthenticatie (MFA), vaak geïmplementeerd als tweefactorauthenticatie (2FA) door de gebruiker te vragen om twee bewijzen van identiteit. 

De meest voorkomende manieren voor bewijs van identiteit, naast de gangbare combinatie van gebruikersnaam en wachtwoord, zijn gebaseerd op het verzenden van een unieke code via e-mail, sms (mobiel tekstbericht) of een mobiele authenticatie-app.

Deze extra menselijke interactie biedt een extra uitdaging voor het geautomatiseerd testen van de webapplicatie. In dit artikel wordt de aanpak besproken die Uptrends momenteel ondersteunt voor sms-gebaseerde 2FA als onderdeel van de Uptrends transactiemonitoring. 

[SHORTCODE_1] **Opmerking**: MFA-implementaties die afhankelijk zijn van authenticatie-apps worden [ook ondersteund]([LINK_URL_1]). [SHORTCODE_2]

## Normale flow van een sms-gebaseerd 2FA-scenario
De flow die we verwachten te zien tijdens de 2FA-procedure met een sms-bericht in een webapplicatie is als volgt:

1. Na het navigeren naar de inlogpagina van de applicatie, typt een gebruiker zijn inloggegevens in de tekstvelden van de inlogpagina. Dit deel is de eerste identificatiestap van 2FA.
2. Deze inlogpoging zou het onderliggende systeem moeten triggeren om een sms-bericht te sturen naar het mobiele telefoonnummer dat is voorgeconfigureerd voor de gebruiker.
3. Terwijl het sms-bericht wordt verzonden, navigeert de webapplicatie naar een nieuwe pagina die een tekstveld bevat, in afwachting van verdere gebruikersinvoer.
4. Wanneer de gebruiker het sms-bericht op zijn mobiele telefoon ontvangt, ziet hij een unieke code die op die nieuwe webpagina moet worden ingevoerd. Dit deel is de tweede identificatiestap van 2FA.
5. Als alles klopt krijgt de gebruiker toegang tot de webapplicatie.
6. Eenmaal volledig ingelogd, voltooit de gebruiker zijn taak in de webapplicatie.

## Overzicht van de Uptrends-oplossing voor sms-gebaseerde 2FA
In plaats van een fysieke mobiele telefoon te gebruiken, regelt Uptrends een virtueel telefoonnummer dat zal worden gebruikt om sms-berichten te ontvangen. Aan de kant van Uptrends zijn een paar eenvoudige handmatige stappen nodig om de sms-component van het 2FA-proces in te stellen. 

Een van de acties in het transactiescript zal zijn om te wachten op het inkomende sms-bericht. Eenmaal ontvangen, wordt de unieke code (meestal een 6-cijferige numerieke code, maar andere formaten worden ook ondersteund) geëxtraheerd en kan deze worden gebruikt om in te voeren in het betreffende tekstveld. Dit hele proces is een exacte simulatie van wat een normale gebruiker zou doen, waardoor het een zeer goede oplossing is voor eindgebruikerstesten.

## Stappen voor het instellen van sms-gebaseerde 2FA in een transactie
1. Tijdens de set-upfase voor het creëren van de transactie is er eerst overleg en handmatige voorbereiding nodig. [Neem contact op met support]([LINK_URL_2]) om te kunnen beginnen.
2. Er wordt geen fysieke mobiele telefoon gebruikt. In plaats daarvan wordt een nieuw virtueel telefoonnummer aangevraagd bij onze partner Twilio. Om dit te doen moeten we bepalen in welk land dat telefoonnummer moet worden geregistreerd.
3. Nadat het nieuwe mobiele telefoonnummer is geregistreerd, moet het worden voorgeconfigureerd in het gebruikersprofiel in de doelapplicatie. Bovendien moet in het gebruikersprofiel mogelijk worden aangegeven dat sms-gebaseerde tweefactorauthenticatie is vereist.
4. Voordat Uptrends begint met het bouwen van de transactie, is het zinvol om eerst een handmatige test uit te voeren om te zien of de set-up correct werkt en daadwerkelijk een sms-bericht triggert dat door het Uptrends-systeem kan worden ontvangen.
5. Als we hebben vastgesteld dat de sms-communicatie betrouwbaar werkt, bouwt Uptrends Support een transactie (meestal gebaseerd op een transactie-opname die is gemaakt door onze [Transaction Recorder browser-plugin]([LINK_URL_3]) te gebruiken.

![Een sms-gebaseerde 2FA-actie in een transactiescript]([LINK_URL_4])

6. Als de transactie is getest en in production is geplaatst, kan de transactie onbelemmerd worden onderhouden en bijgewerkt zonder hulp van buitenaf van Uptrends Support, hoewel het Supportteam altijd bereid is te helpen.



## Kosten
De [normale kosten voor een transactie]([LINK_URL_5]) zijn van toepassing; deze kosten zijn gebaseerd op het aantal acties dat ervoor zorgt dat de browser naar een nieuwe pagina navigeert. Boven op de normale kosten wordt één extra transactiecredit gerekend voor de actie wachten-op-sms. 

## Waarschuwingen
Sommige 2FA-systemen sturen niet bij elke inlogpoging een sms-bericht. Ons advies is om bij elke controle een configuratie te gebruiken die consistent gedrag vertoont. Dit maakt het transactiescript voorspelbaarder en de kans dat een probleem in het 2FA-systeem zo snel mogelijk wordt ontdekt neemt enorm toe.

Als een specifiek telefoonnummer is geregistreerd, is het altijd bedoeld om voor **één enkele transactie** te werken. Als 2FA in meerdere transacties moet worden gebruikt, is voor elke transactie een apart telefoonnummer nodig. De reden hiervoor is dat de transacties parallel worden uitgevoerd, mogelijk gelijktijdig, en dat het onmogelijk is om te bepalen welk sms-bericht bij welke transactie hoort als ze allemaal naar hetzelfde telefoonnummer worden verzonden.