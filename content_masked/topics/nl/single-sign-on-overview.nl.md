{
  "hero": {
    "title": "Overzicht Single Sign-on"
  },
  "title": "Overzicht Single Sign-on",
  "summary": "Lees hoe Uptrends en uw SSO-provider samen kunnen werken om gebruikersbeheer te verbeteren en gebruikers een snellere, naadloze inlogervaring te bieden. ",
  "url": "[URL_BASE_TOPICS]account/instellingen/overzicht-single-sign-on",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Wanneer een Uptrends-account voor het eerst wordt aangemaakt, maakt de oorspronkelijke accountbeheerder een login voor zichzelf op basis van zijn e-mailadres en een gekozen wachtwoord. In de loop van de tijd kunnen operators worden toegevoegd om meer mensen toegang tot de account te geven, waarbij elke operator inlogt met zijn eigen e-mailadres en wachtwoord.

Dit werkt goed, maar naarmate uw organisatie verandert en groeit en uw teams meer online tools en diensten gaan gebruiken, dient u het volgende te overwegen:

- Mensen moeten hun Uptrends-wachtwoord onthouden, samen met de wachtwoorden van alle andere online tools die ze gebruiken.
- Zij moeten iedere keer handmatig inloggen als zij toegang willen tot Uptrends.
- Bekeken vanuit het perspectief van gebruikersbeheer kan het steeds lastiger worden om te controleren wie toegang heeft tot welke tools.

## Makkelijker en veiliger toegangsbeheer met Single Sign-on

Om het voor zowel eindgebruikers als beheerders gemakkelijker te maken, kunt u in alle online apps die uw teams gebruiken een oplossing gebruiken die zich tussen uw gebruikers en die online apps bevindt. Er zijn veel producten van derden beschikbaar die een Single Sign-on-oplossing (SSO) bieden. Wij hebben gewerkt met [Azure Active Directory]([LINK_URL_1]), Active Directory Federation Services (ADFS), [Okta]([LINK_URL_2]), [OneLogin]([LINK_URL_3]), [SecureAuth]([LINK_URL_4]) en [Duo Access Gateway]([LINK_URL_5]), maar er zijn er nog veel meer. Elk product dat het [SAML 2.0 protocol]([LINK_URL_6]) voor Single Sign-on kan ondersteunen, zou moeten werken.

## Hoe Single Sign-on in Uptrends werkt

Zoals besproken, hebt u een product van een derde partij nodig dat functioneert als de centrale hub voor uw gebruikers om toegang te krijgen tot apps, en voor uw beheerders om te bepalen welke gebruikers toegang hebben tot welke apps - waarvan Uptrends er een is. In dit artikel noemen we dat product de **Identity Provider (IdP)**, omdat het de identiteit aantoont van elke gebruiker wanneer zij inloggen op uw apps. In deze configuratie is Uptrends een van die apps en speelt het de rol van **Service Provider (SP)**.

Nadat u een IdP hebt geconfigureerd, gebruikt u de inlogfuncties van de IdP om te verzekeren dat uw gebruikers worden geverifieerd in hun browser, op hun mobiele apparaten enzovoort - vaak op basis van hun netwerkreferenties. Die functies kunnen ook twee-stappen-authenticatie, streng wachtwoordbeleid enzovoort bevatten. Het belangrijkste voordeel voor eindgebruikers is dat ze niet langer verschillende wachtwoorden voor verschillende apps hoeven te onthouden en dat ze met één enkele klik toegang hebben tot Uptrends en andere apps. De meeste IdP's bieden een app-galerie of app-hub, die alle tools en diensten toont die beschikbaar zijn voor de gebruiker. De tools zijn meteen herkenbaar en toegankelijk, zonder bladwijzers voor URL's te hoeven maken, de juiste wachtwoorden te onthouden en het gebruikelijke gedoe om alles veilig en georganiseerd te houden.

Beheerders profiteren van een SSO-configuratie omdat zij kunnen bepalen welke gebruikers toegang hebben tot Uptrends en zij toegang eenvoudig kunnen intrekken als iemand het bedrijf verlaat of overstapt naar een ander team.

## Overzicht Single Sign-on configuratie

Om in Uptrends SSO te configureren zijn de volgende basisstappen nodig:

- **Activeer de optie Single Sign-on (SSO)** in uw Uptrends-accountinstellingen. Let op: Single Sign-on is alleen beschikbaar voor Enterprise-accounts.
- **Definieer een nieuwe app in uw Identity Provider** met behulp van de SAML-configuratiegegevens die zijn verstrekt door Uptrends. Feitelijk hoeft u slechts één URL te kopiëren: dit is de Single Sign-on URL (aan de Uptrends-kant) die uniek is voor de SSO-configuratie van uw organisatie: uw IdP moet deze URL hebben zodat deze weet waar uw gebruikers naartoe gestuurd moeten worden als zij inloggen.
- Eenmaal gedefinieerd, genereert de nieuwe Uptrends-app in uw IdP ook SAML-configuratiedata. Deze data bestaan uit twee stukjes informatie: **de login URL vanuw IdP's** (zodat Uptrends weet waar uw gebruikers vandaan komen) en het **certificaat dat door uw IdPis gegenereerd** om de SAML requests die het naar Uptrends stuurt digitaal te ondertekenen. Hierdoor kan Uptrends er absoluut zeker van zijn dat de inkomende logins echt van uw Identity Provider komen en niet van iemand anders. Dit is een cruciaal onderdeel van de beveiliging van Single Sign-on. U slaat de public key voor SSO op in uw [Uptrends vault]([LINK_URL_7]).
- Zorg ervoor dat **uw gebruikers aan beide zijden zijn gedefinieerd**: uw IdP wordt in uw eigen omgeving uitgevoerd, dus deze kent uw gebruikers al. In Uptrends moet elke gebruiker een eigen operator hebben (als deze nog niet bestaat). Als een gebruiker is ingelogd door uw IdP, kijken we naar het e-mailadres, dus dit moet aan beide zijden overeenkomen.
- U hoeft SSO niet in één keer voor alle gebruikers te gaan gebruiken: u kunt beginnen met één gebruiker, terwijl de overige gebruikers klassieke logins blijven gebruiken voor toegang tot Uptrends tot u klaar bent om over te stappen naar SSO.

## Hoe kunnen SSO-gebruikers inloggen? [ANCHOR_1]

Nadat uw SSO-configuratie is voltooid, wilt u uw gebruikers instrueren over inloggen bij Uptrends. Waar moeten ze naartoe navigeren om toegang te krijgen tot hun Uptrends-account? Er zijn twee benaderingen:

1. Configureer *IdP-geïnitieerde SSO*. Deze methode betekent dat uw gebruikers een centrale locatie hebben die zij kunnen bezoeken (vaak een webpagina die wordt gehost door uw IdP-software in de vorm van een *app-galerie*) om in te loggen bij Uptrends of andere SSO-geactiveerde diensten. De app-galerie bevat een speciale koppeling naar Uptrends die de SSO-inlogprocedure start. Deze methode wordt IdP-geïnitieerd genoemd omdat de inlogprocedure wordt gestart aan de kant van Identity Provider.
2. Configureer *SP-geïnitieerde SSO*. Deze methode veronderstelt dat u geen centrale app-galerie of portal hebt, maar dat uw gebruikers zelf naar SSO-geactiveerde diensten moeten navigeren. Zij moeten de naam van uw organisatie opgeven in het Uptrends SSO-inlogscherm om de inlogprocedure te starten die verbinding maakt met uw Identity Provider. Als alternatief kunnen ze een bladwijzer maken naar het subdomein [INLINE_CODE_1]. Neem [contact op met onze afdeling Support]([LINK_URL_8]) als u de SP-geïnitieerde inlogmethode wilt gebruiken. Zij zorgen er dan voor dat uw subdomein wordt gecreëerd.
