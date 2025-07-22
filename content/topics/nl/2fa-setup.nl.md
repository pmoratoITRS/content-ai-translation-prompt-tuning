{
  "hero": {
    "title": "Tweefactorauthenticatie instellen"
  },
  "title": "Tweefactorauthenticatie instellen",
  "summary": "Hoe u tweefactorauthenticatie (2FA) instelt met op tijd gebaseerde eenmalige wachtwoorden (TOTP) voor Uptrends.",
  "url": "/support/kb/account/instellingen/2fa-instellen",
  "translationKey": "https://www.uptrends.com/support/kb/account/2fa-setup"
}

Voor het instellen van tweefactorauthenticatie in Uptrends moet een accountbeheerder eerst de accountbrede standaardinstelling configureren. Daarna kunnen de algemene instellingen van de operator afzonderlijk worden overschreven, indien zo geconfigureerd. Er kan een authenticatie-app naar keuze worden gebruikt.  

## Accountbrede standaard inlogopties inschakelen 
Deze instelling kan alleen worden geconfigureerd door accountbeheerders. 

Ga in Uptrends naar {{< AppElement type="menuitem" >}} Accountinstellingen > Accountinstellingen {{< /AppElement >}} en selecteer een van de opties bij **Tweefactorauthenticatie-instelling**. 

![screenshot 2FA accountinstelling](/img/content/scr_2fa-authentication-setting.min.png)
  - **Vereist** - [Standaard operators]({{< ref path="/support/kb/account/users/operators/permissions#basic-operator" lang="nl" >}}) moeten tweefactorauthenticatie gebruiken met een op tijd gebaseerd eenmalig wachtwoord.
  - **Optioneel** - Standaard operators kunnen kiezen of ze tweefactorauthenticatie met een op tijd gebaseerd eenmalig wachtwoord gebruiken.
  - **Uitgeschakeld** - Tweefactorauthenticatie met een op tijd gebaseerd eenmalig wachtwoord kan niet binnen het hele account worden gebruikt.

## Tweefactorauthenticatie-instellingen voor operators
Nadat u de standaard loginopties voor operators heeft geconfigureerd, kiest u op de operatorpagina een loginoptie op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} in het gedeelte **Loginopties voor deze operator**. Hier vindt u de standaardstatus van tweefactorauthenticatie in uw account en de optie om de standaard accountbrede instellingen voor tweefactorauthenticatie voor deze specifieke operator te overschrijven. (Deze instelling kan nog steeds alleen worden geconfigureerd door accountbeheerders.)

![screenshot 2FA loginopties voor operators](/img/content/scr_2fa-operator-login-options.min.png)
Selecteer bij **Tweefactorauthenticatie-instelling** de optie **Instellingen tweefactorauthenticatie overschrijven** om de instellingen indien nodig te overschrijven. 
- **Vereist** - Tweefactorauthenticatie moet worden gebruikt. De configuratie wordt geactiveerd tijdens de volgende login van de operator. 
- **Optioneel** - Tweefactorauthenticatie kan in dit scherm handmatig worden ingesteld.
- **Uitgeschakeld** - Tweefactorauthenticatie kan niet worden gebruikt.

Om de tweefactorauthenticatie-configuratie te wissen en opnieuw in te stellen klikt u op de knop {{< AppElement type="deletebutton" >}} Tweefactorauthenticatie opnieuw instellen {{< /AppElement >}}.

{{< callout >}}
**Opmerking:** Tweefactorauthenticatie met op tijd gebaseerde eenmalige wachtwoorden werkt niet in combinatie met [Single Sign-on (SSO) in Uptrends]({{< ref path="support/kb/account/settings/single-sign-on-overview" lang="nl" >}}). 
{{< /callout >}}

Er zijn verschillende manieren waarop een beheerder of operator het instellen van tweefactorauthenticatie kan inschakelen of activeren:

### Operatorinstellingen
Navigeer in Uptrends naar het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} van de operatorpagina. U kunt dit doen door op de naam van de operator onder aan het hoofdmenu te klikken en  {{< AppElement type="menuitem" >}} Gebruikersinstellingen {{< /AppElement >}} te selecteren. Klik dan op {{< AppElement type="editbutton" >}} Scan de QR-code {{< /AppElement >}} om tweefactorauthenticatie in te stellen. Er verschijnt een pop-upvenster.

Gebruik een authenticator-app naar keuze om de QR-code te scannen. Als u deze niet kunt scannen, schakel dan over naar handmatige invoer door op de link onder de QR-code te klikken. Klik op {{< AppElement type="buttonPrimary" >}} Volgende {{< /AppElement >}} en vul de verstrekte zescijferige code in. Nadat u op {{< AppElement type="buttonPrimary" >}} Voltooien {{< /AppElement >}} heeft geklikt is de tweefactorauthenticatie succesvol ingesteld. 

### Via operator-uitnodiging 
Wanneer een operator die tweefactorauthenticatie moet gebruiken is [uitgenodigd voor Uptrends]({{< ref path="support/kb/account/users/operators/add-or-delete-operator#by-invitation" lang="nl" >}}) maakt het set-upproces van tweefactorauthenticatie deel uit van het accepteren van de uitnodiging door de operator. Het authenticatieproces is hetzelfde, met een authenticator-app naar keuze die een op tijd gebaseerd eenmalig wachtwoord verstrekt. 

### Via e-maillink
Na het inloggen krijgt een operator die tweefactorauthenticatie moet gebruiken een pagina te zien waarin hij of zij op de hoogte wordt gesteld van een e-mail. Dat e-mailbericht bevat een link naar een pagina binnen Uptrends waar tweefactorauthenticatie kan worden ingeschakeld. Daarna wordt de operator ingelogd. De operator moet vanaf dat moment inloggen met een op tijd gebaseerd eenmalig wachtwoord.