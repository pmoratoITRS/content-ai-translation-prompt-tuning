{
  "hero": {
    "title": "Configuratiehandleiding Single Sign-on"
  },
  "title": "Configuratiehandleiding Single Sign-on",
  "url": "[URL_BASE_TOPICS]account/instellingen/sso-configuratiehandleiding",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In dit artikel wordt stap voor stap besproken hoe u [Single Sign-on (SSO) in Uptrends]([LINK_URL_1]) configureert. Controleer deze uitgangspunten voordat u Single Sign-on gaat configureren:

-   U hebt toegang nodig tot een Identity Provider-product van een derde partij waarmee uw organisatie Single Sign-on kan gebruiken. Deze IdP wordt de centrale hub voor uw gebruikers om toegang te krijgen tot Uptrends en andere apps. Uptrends gebruikt het [SAML 2.0 protocol]([LINK_URL_2]) voor Single Sign-on, dus elke IdP die SAML 2.0 ondersteunt zou moeten werken. Raadpleeg de documentatie van uw IdP en volg de daarin beschreven procedure voor het toevoegen van een nieuwe app (of Service Provider, SP) aan uw configuratie.
-   In Uptrends hebt u een [Enterprise-account]([LINK_URL_3]) nodig om SSO te kunnen gebruiken. Hebt u momenteel een andere account of weet u het niet zeker, [vraag dan ons Support team]([LINK_URL_4]) u te helpen bij het evalueren van uw opties.

## Single Sign-on activeren in Uptrends

1.  Ga in Uptrends naar uw Accountinstellingen [SHORTCODE_1](Account > Accountinstellingen[SHORTCODE_2]) en selecteer de optie **Single Sign-on (SSO) activeren**. Ziet u deze optie niet, dan moet u mogelijk upgraden naar Uptrends Enterprise.  
    Als u SSO activeert in uw accountopties, ziet u een nieuw gedeelte voor Standaard inlogopties voor operators (zie hieronder) en het gedeelte met uw SSO-instellingen.

2.  Bij de Single Sign-on instellingen ziet u het veld **Single Sign-on URL**. Dit is een vooraf gedefinieerde URL die u in één van de volgende stappen in uw IdP-configuratie moet kopiëren.

3.  Log in bij uw Identity Provider met beheerdersbevoegdheden. **Start de configuratie van een nieuwe SAML-gebaseerde app**, geef deze een beschrijvende naam (bijvoorbeeld *Uptrends*) en voeg optioneel het Uptrends-logo toe.

4.  Indien uw IdP dit vereist, specificeer dan een **IdP-geïnitieerde** configuratie in plaats van een SP-geïnitieerde. Moet u bovendien het webplatform van de serviceprovider specificeren, kies dan Microsoft IIS.

5.  Uw IdP vraagt om de **Single Sign-on URL van de serviceprovider**, oftewel het SAML-eindpunt. Gebruik hier de Single Sign-on URL uit stap 2.

6.  Sommige IdP's vragen om een **Audience URI of Entity ID**: gebruik hier dezelfde URL die u in de vorige stap hebt gebruikt. Sommige IdP's specificeren feitelijk hun eigen Audience URI of Entity ID. In dat geval kopieert u die waarde en plakt deze in het veld Audience URI/Entity ID in uw Uptrends SSO-instellingen.

7.  Uw IdP laat u waarschijnlijk specificeren welk veld gebruikt moet worden door de Identity Provider zodat de Service Provider kan herkennen welke gebruiker probeert in te loggen. Deze optie wordt vaak het **Name ID Formatgenoemd**. Uptrends gebruikt het e-mailadres van de gebruiker, dus kies *Email* of *EmailAddress* bij die waarde.

8.  Voltooi de configuratieprocedure in uw IdP. Aan het eind van de procedure geeft uw IdP u de configuratiegegevens die Uptrends nodig heeft voor het afronden van de van de SSO-configuratie. Afhankelijk van uw IdP krijgt u de **Identity Provider Single Sign-on URL** en de **certificaatgegevens** (een X.509 public key) of moet u een afzondelijk XML-bestand downloaden dat dezelfde informatie bevat.  

    Alleen als u van uw IdP u een XML-metadatabestand krijgt: u kunt het bestand als een gewoon tekstbestand openen en de benodigde informatie zoeken. Als u twijfelt, vraag dan ons Support team u te helpen. 

    Zoek een XML node die er ongeveer als volgt uitziet

    [INLINE_CODE_1]

    De URL in het attribuut **Location** is de waarde die u bij de volgende stap nodig hebt.

    Zoek ook een XML node genaamd

    [INLINE_CODE_2]

    De Base64-encoded data binnen die node zijn de certificaatdata die u zo meteen nodig hebt.

9.  Weer terug bij uw Uptrends-accountinstellingen, kopieert u de Single Sign-on URL van de Identity Provider in het veld **URL om in te loggen**. 

10. De volgende stap dient om de certificaatdata die door uw IdP zijn gegenereerd op te slaan in uw [Uptrends vault]([LINK_URL_5]).   
    Klik op de koppeling *Maak een vault-item* naast het veld Certificaat. Er wordt een nieuw browsertabblad geopend waar u een nieuw item in de vault kunt maken om uw public key data op te slaan. Geef deze een beschrijvende naam (bijvoorbeeld *SSO certificaat*) en zorg dat **Public key van het certificaat** is gekozen in het menu Type.   
    In het veld **Public key** plakt u de Base64-encoded data die u zojuist had gevonden.  Sla het nieuwe vault item op. 

11. Navigeer terug naar de Accountinstellingen in het vorige browsertabblad. Klik op *Verversen* om de lijst met beschikbare items opnieuw te laden. Deze bevat nu het vault-item dat u zojuist hebt gemaakt. Selecteer tot slot het SSO-certificaat. In gevallen waar u certificaat rollover nodig hebt (bijvoorbeeld als een eerder geüpload certificaat afloopt en u een naadloze overgang nodig hebt naar het volgende), kunt u kiezen alle vault-items in een vault-sectie te gebruiken. Om dit te doen selecteert u de optie 'Zoek een geschikt certificaat in deze gehele sectie' in het menu Certificaat. Klik op [SHORTCODE_3]Opslaan[SHORTCODE_4] om uw SSO-configuratie te voltooien.

12.  Uw configuratie van Single Sign-on- is nu klaar voor gebruik. 

## Loginopties beheren

Als u Single Sign-on met succes hebt geconfigureerd in uw account, kunt u kiezen of u SSO-gebaseerde logins voor alle operators in één keer wilt inschakelen. 

In de accountinstellingen kunt u het standaardgedrag voor alle operators instellen. U kunt zowel de klassieke login met gebruikersnaam/wachtwoord als SSO-gebaseerde login inschakelen/uitschakelen. Uiteraard moet u niet beide opties uitschakelen, want dan zijn alle operators buitengesloten. 

Het gangbare scenario is dat de op gebruikersnaam/wachtwoord gebaseerde logins aanvankelijk worden ingeschakeld. Vervolgens worden de SSO-gebaseerde logins met enkele gebruikers getest. Tot slot worden de op gebruikersnaam/wachtwoord gebaseerde logins voor alle operators uitgeschakeld om te zorgen dat iedereen Single Sign-on gaat gebruiken om in te loggen bij Uptrends. 

Naast dit standaardgedrag kunt u uitzonderingen creëren voor individuele operators. Als u de instellingen van een operator bekijkt, ziet u dat de instellingen bij zowel de gebruikersnaam/wachtwoord- als die bij de SSO-inlog aanvankelijk op 'Account standaard' staan. Dit betekent dat het standaardgedrag dat u bij de accountinstellingen hebt gespecificeerd van toepassing is op deze operator. 

U kunt voor iedere operator een andere instelling selecteren om deze inlogopties toe te staan of te weigeren. Dit is bijvoorbeeld handig als u wilt dat al uw vaste operators Single Sign-on gebruiken, behalve een of meer speciale operators die u hebt gecreëerd om mensen buiten uw organisatie toegang tot bepaalde rapportages te verlenen. Zij hebben weliswaar geen toegang tot uw Identity Provider, maar u kunt ze nog steeds toegang verlenen tot Uptrends met een gewone login met gebruikersnaam/wachtwoord.
