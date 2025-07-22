{
  "hero": {
    "title": "Tweefactorauthenticatie instellen"
  },
  "title": "Tweefactorauthenticatie instellen",
  "summary": "Hoe u tweefactorauthenticatie (2FA) instelt met op tijd gebaseerde eenmalige wachtwoorden (TOTP) voor Uptrends.",
  "url": "[URL_BASE_TOPICS]account/instellingen/2fa-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Voor het instellen van tweefactorauthenticatie in Uptrends moet een accountbeheerder eerst de accountbrede standaardinstelling configureren. Daarna kunnen de algemene instellingen van de operator afzonderlijk worden overschreven, indien zo geconfigureerd. Er kan een authenticatie-app naar keuze worden gebruikt.  

## Accountbrede standaard inlogopties inschakelen 
Deze instelling kan alleen worden geconfigureerd door accountbeheerders. 

Ga in Uptrends naar [SHORTCODE_3] Accountinstellingen > Accountinstellingen [SHORTCODE_4] en selecteer een van de opties bij **Tweefactorauthenticatie-instelling**. 

![screenshot 2FA accountinstelling]([LINK_URL_1])
  - **Vereist** - [Standaard operators]([LINK_URL_2]) moeten tweefactorauthenticatie gebruiken met een op tijd gebaseerd eenmalig wachtwoord.
  - **Optioneel** - Standaard operators kunnen kiezen of ze tweefactorauthenticatie met een op tijd gebaseerd eenmalig wachtwoord gebruiken.
  - **Uitgeschakeld** - Tweefactorauthenticatie met een op tijd gebaseerd eenmalig wachtwoord kan niet binnen het hele account worden gebruikt.

## Tweefactorauthenticatie-instellingen voor operators
Nadat u de standaard loginopties voor operators heeft geconfigureerd, kiest u op de operatorpagina een loginoptie op het tabblad [SHORTCODE_5] Algemeen [SHORTCODE_6] in het gedeelte **Loginopties voor deze operator**. Hier vindt u de standaardstatus van tweefactorauthenticatie in uw account en de optie om de standaard accountbrede instellingen voor tweefactorauthenticatie voor deze specifieke operator te overschrijven. (Deze instelling kan nog steeds alleen worden geconfigureerd door accountbeheerders.)

![screenshot 2FA loginopties voor operators]([LINK_URL_3])
Selecteer bij **Tweefactorauthenticatie-instelling** de optie **Instellingen tweefactorauthenticatie overschrijven** om de instellingen indien nodig te overschrijven. 
- **Vereist** - Tweefactorauthenticatie moet worden gebruikt. De configuratie wordt geactiveerd tijdens de volgende login van de operator. 
- **Optioneel** - Tweefactorauthenticatie kan in dit scherm handmatig worden ingesteld.
- **Uitgeschakeld** - Tweefactorauthenticatie kan niet worden gebruikt.

Om de tweefactorauthenticatie-configuratie te wissen en opnieuw in te stellen klikt u op de knop [SHORTCODE_7] Tweefactorauthenticatie opnieuw instellen [SHORTCODE_8].

[SHORTCODE_1]
**Opmerking:** Tweefactorauthenticatie met op tijd gebaseerde eenmalige wachtwoorden werkt niet in combinatie met [Single Sign-on (SSO) in Uptrends]([LINK_URL_4]). 
[SHORTCODE_2]

Er zijn verschillende manieren waarop een beheerder of operator het instellen van tweefactorauthenticatie kan inschakelen of activeren:

### Operatorinstellingen
Navigeer in Uptrends naar het tabblad [SHORTCODE_9] Algemeen [SHORTCODE_10] van de operatorpagina. U kunt dit doen door op de naam van de operator onder aan het hoofdmenu te klikken en  [SHORTCODE_11] Gebruikersinstellingen [SHORTCODE_12] te selecteren. Klik dan op [SHORTCODE_13] Scan de QR-code [SHORTCODE_14] om tweefactorauthenticatie in te stellen. Er verschijnt een pop-upvenster.

Gebruik een authenticator-app naar keuze om de QR-code te scannen. Als u deze niet kunt scannen, schakel dan over naar handmatige invoer door op de link onder de QR-code te klikken. Klik op [SHORTCODE_15] Volgende [SHORTCODE_16] en vul de verstrekte zescijferige code in. Nadat u op [SHORTCODE_17] Voltooien [SHORTCODE_18] heeft geklikt is de tweefactorauthenticatie succesvol ingesteld. 

### Via operator-uitnodiging 
Wanneer een operator die tweefactorauthenticatie moet gebruiken is [uitgenodigd voor Uptrends]([LINK_URL_5]) maakt het set-upproces van tweefactorauthenticatie deel uit van het accepteren van de uitnodiging door de operator. Het authenticatieproces is hetzelfde, met een authenticator-app naar keuze die een op tijd gebaseerd eenmalig wachtwoord verstrekt. 

### Via e-maillink
Na het inloggen krijgt een operator die tweefactorauthenticatie moet gebruiken een pagina te zien waarin hij of zij op de hoogte wordt gesteld van een e-mail. Dat e-mailbericht bevat een link naar een pagina binnen Uptrends waar tweefactorauthenticatie kan worden ingeschakeld. Daarna wordt de operator ingelogd. De operator moet vanaf dat moment inloggen met een op tijd gebaseerd eenmalig wachtwoord.