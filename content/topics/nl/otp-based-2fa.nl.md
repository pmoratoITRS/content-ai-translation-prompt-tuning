{
  "hero": {
    "title": "Op eenmalig wachtwoord gebaseerde 2FA"
  },
  "title": "Werken met OTP-gebaseerde 2FA in transacties",
  "summary": "Leer hoe u op eenmalig wachtwoord gebaseerde 2FA instelt voor uw transactiecontroleregels.",
  "url": "/support/kb/synthetic-monitoring/transacties/otp-gebaseerde-2fa",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/otp-based-2fa"
}

In een wereld waar beveiliging en bescherming van persoonsgegevens steeds belangrijker worden, willen veel organisaties niet langer vertrouwen op slechts één enkele inlogactie om toegang tot webapplicaties te beveiligen. Om de kans te vergroten dat een echte gebruiker veilig kan worden geïdentificeerd tijdens een inlogproces, maken webapplicaties nu gebruik van multifactorauthenticatie (MFA), vaak geïmplementeerd als tweefactorauthenticatie (2FA), door de gebruiker te vragen om twee bewijzen van identiteit te leveren.

Naast [sms-gebaseerde 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="nl" >}}) ondersteunt Uptrends ook het gebruik van 2FA waarbij normale gebruikers een code moeten invullen die ze van een mobiele applicatie krijgen. Deze benadering staat bekend als **Time-based One-Time Password** (TOTP of OTP) multifactorauthenticatie.

Dergelijke eenmalige wachtwoorden zijn doorgaans korte tijd geldig (gewoonlijk 30 seconden) en moeten worden ingevoerd als onderdeel van de authenticatieprocedure in de webapplicatie. Deze codes worden algoritmisch gegenereerd op basis van de huidige tijdstempel en een **geheim**: een waarde die bekend is bij zowel de authenticator-app als de webapplicatie, wat betekent dat ze dezelfde waarden zullen berekenen. Als vervolgens de waarde die door de gebruiker is ingevoerd overeenkomt met de waarde die door de webapplicatie wordt verwacht, kan deze verifiëren dat de gebruiker toegang heeft tot dezelfde geheime waarde en ook toegang moet hebben tot de applicatie. 

## Gebruikelijke flow van een OTP-gebaseerd 2FA-scenario

De flow die we verwachten te zien tijdens de tweefactorauthenticatieprocedure via een mobiele applicatie-gebaseerd eenmalig wachtwoord in een webapplicatie is als volgt:

1. Na het navigeren naar de inlogpagina van de applicatie, typt een gebruiker zijn inloggegevens in de tekstvelden van de inlogpagina. Dit deel is de eerste identificatiestap van 2FA.
2. Nadat de inloggegevens zijn ingevoerd, navigeert de webapplicatie doorgaans naar een nieuwe pagina dat één tekstveld bevat, waar het eenmalige wachtwoord moet worden ingevoerd. 
3. De gebruiker opent zijn betreffende mobiele authenticator-applicatie, die een (meestal 6-cijferige) code vermeldt, samen met een aftelklok. 
4. De gebruiker voert deze code in de webapplicatie in en kan verder gaan met inloggen (mits de code overeenkomt met wat de webapplicatie verwachtte en nog niet verlopen is).

## Overzicht van de Uptrends-oplossing voor OTP-gebaseerde 2FA

Aangezien de OTP-codes worden gegenereerd door een algoritme, is kennis van het *geheim* de enige vereiste om ze te kunnen berekenen. Door deze geheime waarde toe te voegen aan uw [account vault]({{< ref path="/support/kb/account/vault" lang="nl" >}}), kunnen we de juiste waarde berekenen, en deze kan dan op dezelfde manier worden gebruikt als een gebruikersnaam of wachtwoord [uit de vault]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="nl" >}}).

In tegenstelling tot sms-gebaseerde 2FA kunt u  OTP-gebaseerde 2FA zelf configureren. Houd er rekening mee dat u toegang moet hebben tot het *geheim* – het kan worden vermeld in de 2FA-configuratie aan uw kant, anders kunnen uw administrators het u vertellen. Als uw organisatie QR-codes gebruikt om de OTP in mobiele apps te registreren, kan het geheim ook daarvan worden verkregen. Als u hulp nodig heeft, neem dan gerust contact op met ons [Support team]({{< ref path="/contact" lang="nl" >}}).

## Stappen voor het instellen van OTP-gebaseerde 2FA in een transactie

1. Naast de reguliere inloggegevens (die u kunt [opslaan in en gebruiken vanuit de vault]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="nl" >}})), moet u het **geheim** weten voor uw OTP-implementatie. Het geheim is meestal een alfanumerieke code die u in uw OTP-configuratie moet kunnen vinden. Als uw organisatie QR-codes gebruikt om de mobiele authenticatie-apps te configureren, kan het geheim ook daaruit worden opgehaald (het scannen van de code leidt naar een URL die het geheim bevat). 
2. Als u het geheim eenmaal kent, moet u het [toevoegen aan de vault]({{< ref path="/support/kb/account/vault#adding-a-new-item-to-the-vault" lang="nl" >}}). Maak in een geschikte vault-sectie een vault-item van het type **Configuratie eenmalig wachtwoord**. 
3. Geef het vault-item een geschikte naam (en eventueel een beschrijving) en vul het **Geheim** in. Indien nodig kunt u het hashing-algoritme, het aantal cijfers of de expiratietijd voor de gegenereerde OTP-codes bewerken, maar de standaardinstellingen zouden in de meeste gevallen de juiste waarden moeten zijn.
4. Sla het vault-item op.
5. Nu is de OTP-configuratie beschikbaar voor gebruik in uw transactiescripts, op [dezelfde manier als u inloggegevens of bestanden die in de vault zijn opgeslagen zou gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="nl" >}}).
6. Voeg op de juiste plaats in het transactiescript een [Instellen-actie]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="nl" >}}) toe.
7. Voeg de juiste CSS- of XPath-selector toe om naar het tekstveld te wijzen dat wacht op de OTP-code op de pagina. 
8. Klik voor zijn waarde op het {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} pictogram en selecteer **Eenmalig wachtwoord**.
9. Selecteer de juiste OTP-configuratie in uw vault en klik op {{< AppElement type="button" >}} Selecteren {{< /AppElement >}} om de OTP-configuratie voor deze actie te gebruiken.

![OTP-configuratie selecteren in transactie](/img/content/scr-otp-selection-transaction-nm.min.png)

10. De transactie is nu geconfigureerd om de juiste OTP-code te genereren en deze in het tekstveld in te voeren. Vanaf hier kunt u de transactie op de normale manier voortzetten. 

## Kosten

Er zijn geen extra kosten verbonden aan een OTP-gebaseerde 2FA-configuratie in uw transactie. De [normale kosten van een transactie]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) zijn van toepassing.
