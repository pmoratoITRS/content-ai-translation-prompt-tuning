{
  "hero": {
    "title": "Authenticatie (versie 4)"
  },
  "title": "Authenticatie (versie 4)",
  "summary": "Hoe u uw API-account registreert en hoe authenticatie werkt",
  "url": "[URL_BASE_TOPICS]api/authenticatie-v4",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Elke API-methode vereist authenticatie met een API-account, dus u moet er eerst een maken. Deze API-account is gebaseerd op uw Uptrends-account, maar is niet hetzelfde. Het voordeel van afzonderlijke accounts is dat u de API-inloggegevens gebruikt binnen bijv. scripts en u uw inloggegevens van uw Uptrends-account niet hoeft te onthullen.

## API-accounts beheren in de operatorinstellingen

API-accounts worden rechtstreeks beheerd in de operator waaraan de accounts zijn gerelateerd. Bekijk [Operator API management]([LINK_URL_1]) voor instructies over het toevoegen of verwijderen van API-accounts. In de meeste gevallen is dit de gemakkelijkste manier om een API-account te registreren en bij te houden welke operator welke accounts heeft, omdat er meerdere accounts geregistreerd kunnen zijn met één operator.

## Een API-account registreren met API calls [ANCHOR_1]

Er is ook een optie om het API-account aan te maken met Uptrends' API. Dit is een oudere, minder gemakkelijke manier om het te doen. Het werkt echter nog steeds en een account dat op deze manier is gemaakt, wordt ook weergegeven op het tabblad [SHORTCODE_5] API management [SHORTCODE_6] van de operator.

Met de **POST**-methode van het **/Register**-eindpunt kunt u een nieuwe API-account creëren. In de beschreven stappen gaat u de Swagger-omgeving gebruiken voor rechtstreekse toegang tot de API. De API-account die we nu gaan maken, verloopt niet, dus u hoeft dit maar één keer te doen.  

1.  Ga naar de [Swagger-pagina]([LINK_URL_2]), zoek de methode [POST /Register]([LINK_URL_3]) en vouw deze uit.

2.  Klik op de knop *Try it out* om een API-account te maken.

3.  Klik op de knop *Execute*.

4.  Uw browser vraagt nu om de inloggegevens van uw Uptrends-operator. Vul het e-mailadres en wachtwoord in dat u normaal gesproken gebruikt om toegang te krijgen tot Uptrends en klik op OK.

5.  Nadat de inloggegevens van uw Uptrends-account zijn geverifieerd, bevat de Response body de waarden voor UserName en Password.  

[CODE_BLOCK_1]              
      
    Dit zijn de inloggegevens van uw nieuwe API-account.

6.  Klik op de knop *Download* in de Response body om deze inloggegevens op te slaan en ze op een veilige plaats te bewaren. Gebruik ze als authenticatie voor alle andere API calls.

[SHORTCODE_1]
**Opmerking:** De API-account verloopt niet. Maar als u uw inloggegevens kwijtraakt, kunnen die niet worden teruggehaald. U moet dan een nieuw API-account maken.
[SHORTCODE_2]

## Gebruik van uw API-account [ANCHOR_2]

Nu u een API-account heeft, kunt u deze gaan gebruiken. Als u Swagger gebruikt, voert u de inloggegevens in een dialoogvenster in. In software als cURL of Postman verstrekt u ze als headers en wordt voor de benodigde codering gezorgd. Als u uw eigen scripts gebruikt, moet u uw inloggegevens eerst coderen, zie het gedeelte [Basicauthenticatie]([LINK_URL_4]).

[SHORTCODE_3]
**Opmerking:** Houd er rekening mee dat deze API-account gekoppeld is aan uw Uptrends-operatoraccount, dus deze heeft dezelfde bevoegdheden als in uw Uptrends-account.
[SHORTCODE_4]

### Swagger-omgeving

Als u API-methoden uitvoert in de Swagger-omgeving, verschijnt er een venster [SHORTCODE_7]Sign in[SHORTCODE_8] (verwijzend naar api.uptrends.com) waar u de gebruikersnaam en het wachtwoord van uw API-account moet invoeren.

### Basisauthenticatie

De inloggegevens van de account moeten altijd worden gecodeerd met behulp van het basisauthenticatieschema en als specifieke header aan de API worden verstrekt.

Software zoals Postman, cURL, etc. zorgt ervoor dat de inloggegevens worden gecodeerd en correct worden verstrekt. Als u uw eigen script schrijft, moet u deze header opgeven voor de API-aanroep:

[INLINE_CODE_1]

De inloggegevens moeten base64-gecodeerd zijn. Volg deze stappen om de header te maken:

1.  Definieer een tekenreeks met de syntaxis [INLINE_CODE_2], waarbij u [INLINE_CODE_3] en [INLINE_CODE_4] vervangt door uw inloggegevens. Voeg geen spaties toe.

2.  De tekenreeks [INLINE_CODE_5] moet base64-gecodeerd zijn. De coderingsfunctionaliteit kan opgenomen zijn in uw software of scripttaal of gebruik een tool zoals [URL_1]

3.  Zodra u de gecodeerde tekenreeks heeft, maakt en gebruikt u een header [INLINE_CODE_6], waarbij de [INLINE_CODE_7] de met base64 gecodeerde tekenreeks uit de vorige stap is.
