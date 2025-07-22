{
  "hero": {
    "title": "Een operator toevoegen of verwijderen"
  },
  "title": "Een operator toevoegen of verwijderen",
  "summary": "Een operator toevoegen en configureren of verwijderen. Elke gecreëerde operator moet correct worden geconfigureerd met contactinformatie, inloginformatie en gebruikersrechten.",
  "url": "/support/kb/account/gebruikers/operators/operator-toevoegen-of-verwijderen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/add-or-delete-operator"
}

In Uptrends is de [Hub voor gebruikersbeheer]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="nl" >}}) de plek om te beginnen voor het beheren van operators (en operatorgroepen). 

## Een operator toevoegen

1. Navigeer naar de [Gebruikersbeheerhub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="nl" >}}). Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators, groepen (en deelaccounts) {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="buttonSecondary" >}}Operator toevoegen{{< /AppElement >}}.
3. Onder **Operator configureren** kunt u bepalen of u de nieuwe operator handmatig toevoegt (in de Uptrends app) of een [uitnodiging](#by-invitation) stuurt en het aan de nieuwe operator overlaat om zijn of haar eigen inloggegevens in te vullen. 
4. Als u *Operator handmatig toevoegen* heeft gekozen, kunt u nu het e-mailadres, wachtwoord, volledige naam, back-up e-mailadres en mobiel telefoonnummer (begin met een \+ teken en uw landcode, gevolgd door het nummer zonder streepjes of spaties) van uw nieuwe operator toevoegen. 
5.  Als u klaar bent met het configureren van uw operator, klikt u op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.
6. Geef hierna het wachtwoord door aan de operator. Er wordt geen automatische e-mail verzonden bij een handmatige accountconfiguratie.


Meer informatie over alle opties voor het configureren van de operator vindt u in de artikelen in [Operators en operatorgroepen]({{< ref path="support/kb/account/users/operators" lang="nl" >}}). 
### Via uitnodiging  {id="by-invitation"}

De uitnodiging wordt per e-mail verzonden naar het e-mailadres in de *E-mail*-instelling van de **Login informatie** en deze bevat een link waarop de nieuwe gebruiker kan klikken om zijn of haar wachtwoord in te stellen. De uitnodiging is 21 dagen geldig. Daarna vervalt de link in de uitnodiging. 

U kunt een uitnodiging opnieuw verzenden, bijvoorbeeld als u de nieuwe operator een herinnering wilt sturen dat hij of zij zijn/haar account nog moet activeren of als de uitnodiging is verlopen.

Op de pagina met operatorinstellingen kunt u de status van de uitnodiging zien. 

Een andere optie om de status van de uitnodiging te controleren, is door te kijken op de pagina Operators, die u vindt door naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators, groepen (en deelaccounts) {{< /AppElement >}} te gaan. Klik op de knop {{< AppElement type="buttonSecondary" >}}Alle operators bekijken{{< /AppElement >}}. De pagina Operators heeft een kolom met informatie over de laatste login van de gebruiker en de status van (lopende) uitnodigingen. Deze heet *Laatste login* en kan de volgende waarden hebben:

   - Tijdstempel van de laatste login – Het account is geactiveerd en gebruikt.
   - Uitgenodigd – De uitnodiging is verzonden en is nog steeds geldig.
   - Uitnodiging verlopen – De uitnodiging is verzonden, maar er zijn 21 dagen verstreken zonder dat de gebruiker op de link in de e-mail heeft geklikt.
   - Nooit ingelogd – De uitnodiging is geaccepteerd door op de link te klikken, maar de gebruiker heeft sindsdien niet meer ingelogd.


{{< callout >}} **Opmerking**: Operators die gebruikmaken van single sign-on (SSO) kunnen alleen via een uitnodiging worden toegevoegd als zowel de gebruikersnaam/wachtwoord- als de SSO-inlogoptie is ingeschakeld. {{< /callout >}}

## Een operator verwijderen

Om een operator te verwijderen:

1. Navigeer naar de [Gebruikersbeheerhub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="nl" >}}). Afhankelijk van uw accounttype kan de route om daar te komen enigszins variëren.
  - Bij **Enterprise** accounts: ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators, groepen en deelaccounts {{< /AppElement >}}.
  - Bij alle andere accounttypes: ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators en groepen {{< /AppElement >}}.

2. Klik op {{< AppElement type="buttonPrimary" >}} Alle operators bekijken {{< /AppElement >}} om het volledige overzicht van operators in uw account te openen.
3. Zoek in de lijst de operator die u wilt verwijderen en klik op de naam. Of voer (een deel van) de naam of het e-mailadres in het filterzoekvak in om de resultaten te filteren.
4. Klik in de operatorinstellingen op {{< AppElement type="deletebutton" >}} Verwijder deze operator {{< /AppElement >}} in de linker benedenhoek van het scherm.

De operator is nu verwijderd. Houd er rekening mee dat u een operator alleen kunt verwijderen als deze niet is gekoppeld aan of eigenaar is van dashboards, publieke statuspagina's of geplande rapporten binnen het account. Als een operator zoiets heeft gecreëerd, is hij over het algemeen automatisch de eigenaar. In dergelijke gevallen kunt u deze objecten verwijderen of eigendom opnieuw toewijzen, of [contact opnemen met support]({{< ref path="/contact" lang="nl" >}}).