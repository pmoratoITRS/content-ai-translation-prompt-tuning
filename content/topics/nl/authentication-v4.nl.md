{
  "hero": {
    "title": "Authenticatie (versie 4)"
  },
  "title": "Authenticatie (versie 4)",
  "summary": "Hoe u uw API-account registreert en hoe authenticatie werkt",
  "url": "/support/kb/api/authenticatie-v4",
  "translationKey": "https://www.uptrends.com/support/kb/api/authentication-v4"
}

Elke API-methode vereist authenticatie met een API-account, dus u moet er eerst een maken. Deze API-account is gebaseerd op uw Uptrends-account, maar is niet hetzelfde. Het voordeel van afzonderlijke accounts is dat u de API-inloggegevens gebruikt binnen bijv. scripts en u uw inloggegevens van uw Uptrends-account niet hoeft te onthullen.

## API-accounts beheren in de operatorinstellingen

API-accounts worden rechtstreeks beheerd in de operator waaraan de accounts zijn gerelateerd. Bekijk [Operator API management]({{< ref path="support/kb/account/users/operators/operator-API-management" lang="nl" >}}) voor instructies over het toevoegen of verwijderen van API-accounts. In de meeste gevallen is dit de gemakkelijkste manier om een API-account te registreren en bij te houden welke operator welke accounts heeft, omdat er meerdere accounts geregistreerd kunnen zijn met één operator.

## Een API-account registreren met API calls {id="register-API-account"}

Er is ook een optie om het API-account aan te maken met Uptrends' API. Dit is een oudere, minder gemakkelijke manier om het te doen. Het werkt echter nog steeds en een account dat op deze manier is gemaakt, wordt ook weergegeven op het tabblad {{< AppElement type="tab" >}} API management {{< /AppElement >}} van de operator.

Met de **POST**-methode van het **/Register**-eindpunt kunt u een nieuwe API-account creëren. In de beschreven stappen gaat u de Swagger-omgeving gebruiken voor rechtstreekse toegang tot de API. De API-account die we nu gaan maken, verloopt niet, dus u hoeft dit maar één keer te doen.  

1.  Ga naar de [Swagger-pagina](https://api.uptrends.com/v4/swagger/), zoek de methode [POST /Register](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Register/Register_Post%20) en vouw deze uit.

2.  Klik op de knop *Try it out* om een API-account te maken.

3.  Klik op de knop *Execute*.

4.  Uw browser vraagt nu om de inloggegevens van uw Uptrends-operator. Vul het e-mailadres en wachtwoord in dat u normaal gesproken gebruikt om toegang te krijgen tot Uptrends en klik op OK.

5.  Nadat de inloggegevens van uw Uptrends-account zijn geverifieerd, bevat de Response body de waarden voor UserName en Password.  

```json                  
        {
           "UserName": "usernamehere",
           "Password": "passwordhere",
           "AccountId": "123456",
           "OperatorName": "Your name",
           "status": "OK"
        }
```              
      
    Dit zijn de inloggegevens van uw nieuwe API-account.

6.  Klik op de knop *Download* in de Response body om deze inloggegevens op te slaan en ze op een veilige plaats te bewaren. Gebruik ze als authenticatie voor alle andere API calls.

{{< callout >}}
**Opmerking:** De API-account verloopt niet. Maar als u uw inloggegevens kwijtraakt, kunnen die niet worden teruggehaald. U moet dan een nieuw API-account maken.
{{< /callout >}}

## Gebruik van uw API-account {id="usage-API-account"}

Nu u een API-account heeft, kunt u deze gaan gebruiken. Als u Swagger gebruikt, voert u de inloggegevens in een dialoogvenster in. In software als cURL of Postman verstrekt u ze als headers en wordt voor de benodigde codering gezorgd. Als u uw eigen scripts gebruikt, moet u uw inloggegevens eerst coderen, zie het gedeelte [Basicauthenticatie](#basic-authentication).

{{< callout >}}
**Opmerking:** Houd er rekening mee dat deze API-account gekoppeld is aan uw Uptrends-operatoraccount, dus deze heeft dezelfde bevoegdheden als in uw Uptrends-account.
{{< /callout >}}

### Swagger-omgeving

Als u API-methoden uitvoert in de Swagger-omgeving, verschijnt er een venster {{< AppElement type="menuitem" >}}Sign in{{< /AppElement >}} (verwijzend naar api.uptrends.com) waar u de gebruikersnaam en het wachtwoord van uw API-account moet invoeren.

### Basisauthenticatie

De inloggegevens van de account moeten altijd worden gecodeerd met behulp van het basisauthenticatieschema en als specifieke header aan de API worden verstrekt.

Software zoals Postman, cURL, etc. zorgt ervoor dat de inloggegevens worden gecodeerd en correct worden verstrekt. Als u uw eigen script schrijft, moet u deze header opgeven voor de API-aanroep:

`Authorization: Basic {{encoded credentials}}`

De inloggegevens moeten base64-gecodeerd zijn. Volg deze stappen om de header te maken:

1.  Definieer een tekenreeks met de syntaxis `username:password`, waarbij u `username` en `password` vervangt door uw inloggegevens. Voeg geen spaties toe.

2.  De tekenreeks `username:password` moet base64-gecodeerd zijn. De coderingsfunctionaliteit kan opgenomen zijn in uw software of scripttaal of gebruik een tool zoals https://www.base64encode.org.

3.  Zodra u de gecodeerde tekenreeks heeft, maakt en gebruikt u een header `Authorization: Basic {{encoded credentials}}`, waarbij de `encoded credentials` de met base64 gecodeerde tekenreeks uit de vorige stap is.
