{
  "hero": {
    "title": "Vault API"
  },
  "title": "Vault API",
  "url": "/support/kb/api/vault-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/vault-api"
}

De Vault wordt gebruikt voor het opslaan van herbruikbare data, vaak gevoelige data zoals certificaten, public keys en combinaties van gebruikersnaam en wachtwoord. Elke vermelding in de Vault wordt een vault-item genoemd en vault-items zijn georganiseerd in vault-secties. Het organiseren van items in verschillende secties is ook nuttig om de toegang te beperken tot bepaalde operators en groepen.

In dit artikel wordt beschreven welke API-methoden beschikbaar zijn voor het beheer van vault-items, vault-secties en vault-sectie-autorisaties. Een bespreking van de gebruiksscenario’s van Vault vindt u in de [Vault-inleiding]({{< ref path="/support/kb/account/vault" lang="nl" >}}). In de [API v4-inleiding]({{< ref path="/support/kb/api/v4" lang="nl" >}}) kunt u lezen hoe u toegang krijgt tot de API.

## Vault-items

Met deze reeks eindpunten kunt u afzonderlijke vault-items ophalen, creëren, bijwerken en verwijderen. Vanwege de gevoelige aard van sommige types vault-items, worden de gevoelige data zelf nooit teruggestuurd.

### Objectbeschrijving vault-item

Het volgende VaultItem object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam | Beschrijving |
|------|-----------------------------|
| `VaultItemGuid` | De unieke identifier van het vault-item. |
| `Name` | De schermnaam van het vault-item. |
| `VaultSectionGuid	` | De unieke identifier van de vault-sectie waarin dit vault-item is opgeslagen. |
| `VaultItemUsedBy` | Geeft aan welke items of controleregels het vault-item gebruiken. |
| `VaultItemType` | Definieert het type vault-item. Momenteel zijn de ondersteunde types: {{< tableformatter >}} 

- `CertificateArchive`: voor certificaatarchiefbestanden (d.w.z. pfx-bestanden), gebruikt voor clientcertificaten in Multi-step API-controleregels.
- `Certificate`: voor public keys, gebruikt voor Single Sign-On-configuratie.
- `CredentialSet`: voor combinaties van gebruikersnaam/wachtwoord, gebruikt voor autenticatie-instellingen in controleregels.
- `File`: voor bestandsopslag, gebruikt voor selfservice-transactiecontroleregels. Elk bestandsformaat wordt ondersteund, met een maximale grootte van 2 MB.
- `OneTimePassword`: voor het genereren van een eenmalig wachtwoord, bevat een geheime waarde en wordt gebruikt voor tweefactorauthenticatie.
{{< /tableformatter >}} |
| `Value` | De waarde die is opgeslagen in het vault-item. De inhoud van dit veld is afhankelijk van het type vault-item: {{< tableformatter >}} 
- Voor type `CertificateArchive`: specificeer een Base-64 encoding van uw binaire .pfx-bestand wanneer u een vault-item van dit type creëert of bijwerkt. Wanneer u het item opnieuw ophaalt, zal het veld Value altijd leeg zijn (omdat het gevoelige informatie is).
- Voor type `Certificate`: specificeer de tekstinhoud van uw public key wanneer u een vault-item van dit type creëert of bijwerkt. Wanneer u het item opnieuw ophaalt, bevat het veld Value de oorspronkelijke public key data.
- Voor type `CredentialSet`: dit veld wordt niet gebruikt. Gebruik in plaats daarvan de velden UserName en Password.
{{< /tableformatter >}} |remain as is in this operation
| `IsSensitive` | Geeft aan of de waarde die is opgeslagen in het vault-item versleuteld is. Wanneer bij een vault-item true is ingesteld, wordt de opgeslagen waarde of waarden niet zichtbaar voor de webapplicatie of de API. Deze waarde moet niet worden gespecificeerd bij het maken van een nieuw item: de items `CertificateArchive` en `CredentialSet` worden altijd versleuteld (omdat ze per definitie gevoelige gegevens bevatten), terwijl een `Certificate` public key inherent openbare informatie is en als platte tekst kan worden opgeslagen. |
| `Notes` | Opmerkingen of beschrijving met betrekking tot dit vault-item. |
| `UserName` | Het gebruikersnaamgedeelte van een set inloggegevens. |
| `Password` | Het wachtwoord van een set inloggegevens. |

### Eindpunten vault-item

De volgende API-methoden zijn beschikbaar:

| Request type | Endpoint                    | Gebruik                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | `VaultItem`                 | Retourneert alle vault-items in secties waartoe de gebruikerscontext toegang heeft. |
| GET          | `VaultItem/{VaultItemGuid}` | Retourneert het gespecificeerde vault-item.                                   |
| POST         | `VaultItem`                 | Creëert een nieuw vault-item met de gespecificeerde waarden.                 |
| PUT          | `VaultItem/{VaultItemGuid}` | Werkt het gespecificeerde vault-item bij.                                   |
| PATCH        | `VaultItem/{VaultItemGuid}` | Werkt bepaalde delen van het gespecificeerde vault-item gedeeltelijk bij. De `VaultItemType` en `VaultItemUsedBy` kunnen niet worden gewijzigd en blijven zoals ze zijn in deze bewerking. |
| DELETE       | `VaultItem/{VaultItemGuid}` | Verwijdert het gespecificeerde vault-item.                                   |

#### GET /VaultItem

De GET request `VaultItem` heeft geen parameters. Deze retourneert een lijst met alle vault-items van secties waartoe u alleen bekijken-toegang heeft.

Voorbeeld inhoud:

```json
[
  {
    "VaultItemGuid": " FE1656C1-A606-43BB-BD61-1EEE9715EE9E ",
    "Name": "Web shop test login",
    "Value": "",
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "test@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
    "VaultItemUsedBy": "1 monitor"
  },
  {
    "VaultItemGuid": "A9CB1BE3-1715-4C31-9040-51CBBFAE23CB",
    "Name": "Marketing web site login",
    "Value": "",
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F ",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "testmarketing@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
  "VaultItemUsedBy": "-"
  }
]
```

#### GET /VaultItem/{VaultItemGuid}

De GET request `VaultItem/{VaultItemGuid}` retourneert het vault-item dat wordt geïdentificeerd door het vault-item Guid.

Voorbeeld van een vault-item geretourneerd in de inhoud van een 200 response:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "IsSensitive": true,
  "Notes": "Certificate archive test",
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Issuer": "Acme Corp, Inc.",
    "NotBefore": "2018-06-12T14:10:50.489Z",
    "NotAfter": "2020-06-12T14:10:50.489Z",
    "Password": "",
    "ArchiveData": ""
  },
  "VaultItemUsedBy": "1 monitor"
}
```

U ziet dat waarden die gevoelige informatie bevatten, worden geretourneerd als een lege string.

#### PUT /VaultItem/{VaultItemGuid}

De PUT request naar eindpunt `VaultItem/{VaultItemGuid}` werkt het vault-item bij dat wordt geïdentificeerd door het vault-item guid. Zodra u een vault-item bijwerkt, wordt elke controleregel die een verwijzing naar dit vault-item bevat ook bijgewerkt, dus uw wijziging wordt onmiddellijk van kracht.

Deze request vereist ChangeVaultSection autorisatie.

Een PUT request verwacht de volgende objectstructuur:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CredentialSet",
  "IsSensitive": true,
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

Als er in het bovenstaande voorbeeld een waarde stond in het oorspronkelijke vault-itemsveld Omschrijving, zal het Omschrijving-veld leeggemaakt zijn. `Als u een parameter weglaat, zal deze niet ongewijzigd blijven, maar als leeg beschouwd worden.` De enige waarden die niet verstrekt hoeven te worden zijn de gevoelige waarden. Als u bijvoorbeeld het veld Waarde of Wachtwoord weglaat, of het gehele object CertificateArchive, blijven deze ongewijzigd. Verder kunnen de kenmerken IsSensitive en VaultSectionGuid niet worden gewijzigd.

#### DELETE /VaultItem/{VaultItemGuid}

De DELETE request naar eindpunt `VaultItem/{VaultItemGuid}` verwijdert het gevraagde vault-item.

Als het gespecificeerde vault-item nog in gebruik is (bijvoorbeeld een controleregel verwijst naar dat specifieke vault-item), retourneert de dienst statuscode 400, inclusief een relevant bericht. Deze request vereist ChangeVaultSection autorisatie.

#### POST /VaultItem

De POST request naar eindpunt `VaultItem` creëert een nieuw VaultItem object. Laat bij het specificeren van de VaultItem data de VaultItemGuid weg: de nieuwe Guid voor dit item wordt geretourneerd als onderdeel van de respons. Deze request vereist ChangeVaultSection autorisatie.

Voorbeeld inhoud:
```json
{
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "Notes": "Certificate archive test",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

## Vault-secties

Er zijn verschillende eindpunten in deze API waarmee u uw vault-secties kunt beheren. Elk vault-item behoort tot precies één vault-sectie. Als u slechts enkele vault-items in uw hele account nodig heeft, kunt u ze eenvoudigweg in een enkele vault-sectie opslaan. Echter, als het aantal vault-items in uw account toeneemt, kunt u ze in afzonderlijke secties gaan organiseren.

Elk Uptrends-account begint met één standaard vault-sectie. De groep Administrators heeft volledige toegang tot deze sectie, wat betekent dat zij de sectie en alle vault-items in die sectie kunnen bewerken.

Wanneer een nieuwe vault-sectie wordt gecreëerd, krijgt de gebruiker (operator) die hoort bij de API account die de vault-sectie creëert automatisch de ChangeVaultSection autorisatie voor de nieuwe sectie. Er worden geen andere autorisaties gecreëerd.

### Objectbeschrijving vault-sectie

Het volgende VaultSection object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam               | Beschrijving                                |
|--------------------|--------------------------------------------|
| `VaultSectionGuid` | De unieke identifier van de vault-sectie |
| `Name`             | De naam van de vault-sectie              |

### Eindpunten vault-sectie

| Request type | Eindpunt                          | Gebruik                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | `VaultSection`                    | Retourneert alle vault-secties waartoe de gebruikerscontext toegang heeft. |
| GET          | `VaultSection/{VaultSectionGuid}` | Retourneert de gespecificeerde vault-sectie.                       |
| POST         | `VaultSection`                    | Creëert een nieuw vault-item met de gespecificeerde naam.       |
| PUT          | `VaultSection/{VaultSectionGuid}` | Werkt de gespecificeerde vault-sectie bij.                       |
| DELETE       | `VaultSection/{VaultSectionGuid}` | Verwijdert de gespecificeerde vault-sectie.                       |

#### GET /VaultSection

De GET request `VaultSection` heeft geen parameters. Deze retourneert een lijst met alle vault-secties waartoe u alleen bekijken-toegang heeft.

Voorbeeld inhoud:
```json
[
  {
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "Name": "Vault items"
  },
  {
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F",
    "Name": "Marketing web site vault items"
  }
]
```

#### GET /VaultSection/{VaultSectionGuid}

De GET request `VaultSection/{VaultSectionGuid}` retourneert de vault-sectie die wordt geïdentificeerd door de vault-sectie Guid.

Voorbeeld inhoud:
```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Vault items"
}
```


#### POST /VaultSection

De POST request naar eindpunt `VaultSection` creëert een nieuw VaultSection object. De operator onder wiens gebruikerscontext de request wordt verstuurd krijgt ViewVaultSection en ChangeVaultSection autorisaties voor de nieuwe sectie. Er worden geen andere autorisaties verleend. Laat bij het specificeren van de VaultSection data de VaultSectionGuid weg; de nieuwe Guid voor dit item wordt geretourneerd als onderdeel van de respons.
```json
{
  "Name": "Development vault items"
}
```

#### PUT /VaultSection/{VaultSectionGuid}

De PUT request naar eindpunt `VaultSection/{VaultSectionGuid}` werkt de vault-sectie bij die wordt geïdentificeerd door de vault-item guid. Meestal is het enige doel hiervan het wijzigen van de naam van de vault-sectie. Deze request vereist ChangeVaultSection autorisatie.

```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Web shop vault items"
}
```

#### DELETE /VaultSection/{VaultSectionGuid}

De DELETE request naar eindpunt `VaultSection/{VaultSectionGuid}` verwijdert de gevraagde vault-sectie.

Als de gespecificeerde vault-sectie nog in gebruik is (wat betekent dat er vault-items opgeslagen zijn in die sectie), zal de dienst statuscode 400 retourneren, inclusief een relevant bericht. Als dit het geval is, moet u de vault-items verwijderen voordat u de vault-sectie kunt verwijderen. Houd er rekening mee dat u een vault-item niet kunt verwijderen als het item nog in gebruik is (bijvoorbeeld wanneer een controleregel is geconfigureerd om dat vault-item te gebruiken). Deze request vereist ChangeVaultSection autorisatie.

## Autorisaties vault-sectie

Naast het gescheiden houden van vault-items, kunt u met vault-secties ook bepalen wie waartoe toegang heeft. Als een specifieke groep operators exclusieve toegang moet hebben tot bepaalde vault-items, dan plaatst u die vault-items in een aparte sectie. Alleen mensen die toegang hebben tot die vault-sectie kunnen de items in die sectie zien.

Zodra u een nieuwe vault-sectie creëert (via de API of via de online app), is die sectie eerst alleen zichtbaar voor u. Als u er vault-items aan heeft toegevoegd, kunnen andere operators deze vault-items niet bewerken of gebruiken.

Om ervoor te zorgen dat andere mensen de nieuwe vault-sectie kunnen gebruiken, er items aan toe kunnen voegen en/of deze vault-items kunnen selecteren in controleregelinstellingen, zult u ze toegang moeten geven. Dit kunt u doen met de volgende API-methoden.

Er zijn twee autorisatietypen: `ViewVaultSection` en `ChangeVaultSection`. Deze autorisatietypen kunnen worden toegekend aan operators en operatorgroepen.

### Objectbeschrijving autorisatie

Het volgende Authorisatie-object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam                | Beschrijving                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AuthorizationId`   | De unieke id van de autorisatie.                                                                                                                        |
| `ContextId`         | De unieke identifier van de context waarvoor de autorisatie is gemaakt. In het geval van een vault-sectieautorisatie is dit de vault-sectie Guid. |
| `AuthorizationType` | `ViewVaultSection` of `ChangeVaultSection`.                                                                                                                |
| `OperatorGuid`      | Als de autorisatie moet worden toegepast op een enkele operator, specificeert dit de operator Guid. Ingesteld op `null` voor operatorgroepautorisaties.             |
| `OperatorGroupId`   | Als de autorisatie moet worden toegepast op een operatorgroep, specificeert dit de operatorgroep-ID. Ingesteld op `null` voor autorisaties voor één operator.        |

### Vault-sectie autorisatie eindpunten

| Request type | Eindpunt                                                            | Gebruik                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | `VaultSection/{VaultSectionGuid}/Authorization`                     | Retourneert een lijst met alle autorisaties voor de gespecificeerde vault-sectie.                   |
| POST         | `VaultSection/{VaultSectionGuid}/Authorization`                     | Creëert een nieuwe autorisatie voor de gespecificeerde vault-sectie, met behulp van de waarden die verstrekt worden. |
| DELETE       | `VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}` | Verwijdert de gespecificeerde autorisatie.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

De GET request naar `VaultSection/{VaultSectionGuid}/Authorization` retourneert een lijst met alle autorisaties voor de vault-sectie die is gespecificeerd in VaultSectionGuid.

Voorbeeld inhoud:
```json
[
  {
    "AuthorizationId": "7210DD2D-3AAE-4F89-A2A8-000060F118F1 ",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ChangeVaultSection",
    "OperatorGuid": "5F71AFD7-8BEE-4C8D-9827-A107308473BE",
    "OperatorGroupId": ""
  },
  {
    "AuthorizationId": "0BACEE61-0582-40FD-B1A2-00034401421A",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ViewVaultSection",
    "OperatorGuid": "",
    "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
  }
]
```


Een autorisatie is voor een operator of een operatorgroep. Een operatorspecifieke autorisatie bevat gegevens in de OperatorGuid en de OperatorGroupId is leeg; een autorisatie voor een operatorgroep heeft een waarde in OperatorGroupId en een lege OperatorGuid.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

De POST request naar `VaultSection/{VaultSectionGuid}/Authorization` creëert een nieuwe autorisatie voor de gespecificeerde vault-sectie.

Voorbeeld inhoud:

```json
{
  "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "AuthorizationType": "ViewVaultSection",
  "OperatorGuid": "",
  "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
}
```

Als u een autorisatie van het type ChangeVaultSection creëert, wordt er automatisch een extra ViewVaultSection autorisatie voor dezelfde operator of operatorgroep toegevoegd. Als een operator of operatorgroep Change \+ View autorisaties heeft voor een vault-sectie, verschijnt deze als *Volledige autorisatie* in de Uptrends-app.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

De DELETE request naar `VaultSection/{VaultSectionGuid}/ Authorization/AuthorizationGuid` verwijdert een bestaande autorisatie.
