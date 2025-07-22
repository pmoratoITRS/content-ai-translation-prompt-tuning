{
  "hero": {
    "title": "Vault API"
  },
  "title": "Vault API",
  "url": "[URL_BASE_TOPICS]api/vault-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De Vault wordt gebruikt voor het opslaan van herbruikbare data, vaak gevoelige data zoals certificaten, public keys en combinaties van gebruikersnaam en wachtwoord. Elke vermelding in de Vault wordt een vault-item genoemd en vault-items zijn georganiseerd in vault-secties. Het organiseren van items in verschillende secties is ook nuttig om de toegang te beperken tot bepaalde operators en groepen.

In dit artikel wordt beschreven welke API-methoden beschikbaar zijn voor het beheer van vault-items, vault-secties en vault-sectie-autorisaties. Een bespreking van de gebruiksscenario’s van Vault vindt u in de [Vault-inleiding]([LINK_URL_1]). In de [API v4-inleiding]([LINK_URL_2]) kunt u lezen hoe u toegang krijgt tot de API.

## Vault-items

Met deze reeks eindpunten kunt u afzonderlijke vault-items ophalen, creëren, bijwerken en verwijderen. Vanwege de gevoelige aard van sommige types vault-items, worden de gevoelige data zelf nooit teruggestuurd.

### Objectbeschrijving vault-item

Het volgende VaultItem object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam | Beschrijving |
|------|-----------------------------|
| [INLINE_CODE_1] | De unieke identifier van het vault-item. |
| [INLINE_CODE_2] | De schermnaam van het vault-item. |
| [INLINE_CODE_3] | De unieke identifier van de vault-sectie waarin dit vault-item is opgeslagen. |
| [INLINE_CODE_4] | Geeft aan welke items of controleregels het vault-item gebruiken. |
| [INLINE_CODE_5] | Definieert het type vault-item. Momenteel zijn de ondersteunde types: [SHORTCODE_1] 

- [INLINE_CODE_6]: voor certificaatarchiefbestanden (d.w.z. pfx-bestanden), gebruikt voor clientcertificaten in Multi-step API-controleregels.
- [INLINE_CODE_7]: voor public keys, gebruikt voor Single Sign-On-configuratie.
- [INLINE_CODE_8]: voor combinaties van gebruikersnaam/wachtwoord, gebruikt voor autenticatie-instellingen in controleregels.
- [INLINE_CODE_9]: voor bestandsopslag, gebruikt voor selfservice-transactiecontroleregels. Elk bestandsformaat wordt ondersteund, met een maximale grootte van 2 MB.
- [INLINE_CODE_10]: voor het genereren van een eenmalig wachtwoord, bevat een geheime waarde en wordt gebruikt voor tweefactorauthenticatie.
[SHORTCODE_2] |
| [INLINE_CODE_11] | De waarde die is opgeslagen in het vault-item. De inhoud van dit veld is afhankelijk van het type vault-item: [SHORTCODE_3] 
- Voor type [INLINE_CODE_12]: specificeer een Base-64 encoding van uw binaire .pfx-bestand wanneer u een vault-item van dit type creëert of bijwerkt. Wanneer u het item opnieuw ophaalt, zal het veld Value altijd leeg zijn (omdat het gevoelige informatie is).
- Voor type [INLINE_CODE_13]: specificeer de tekstinhoud van uw public key wanneer u een vault-item van dit type creëert of bijwerkt. Wanneer u het item opnieuw ophaalt, bevat het veld Value de oorspronkelijke public key data.
- Voor type [INLINE_CODE_14]: dit veld wordt niet gebruikt. Gebruik in plaats daarvan de velden UserName en Password.
[SHORTCODE_4] |remain as is in this operation
| [INLINE_CODE_15] | Geeft aan of de waarde die is opgeslagen in het vault-item versleuteld is. Wanneer bij een vault-item true is ingesteld, wordt de opgeslagen waarde of waarden niet zichtbaar voor de webapplicatie of de API. Deze waarde moet niet worden gespecificeerd bij het maken van een nieuw item: de items [INLINE_CODE_16] en [INLINE_CODE_17] worden altijd versleuteld (omdat ze per definitie gevoelige gegevens bevatten), terwijl een [INLINE_CODE_18] public key inherent openbare informatie is en als platte tekst kan worden opgeslagen. |
| [INLINE_CODE_19] | Opmerkingen of beschrijving met betrekking tot dit vault-item. |
| [INLINE_CODE_20] | Het gebruikersnaamgedeelte van een set inloggegevens. |
| [INLINE_CODE_21] | Het wachtwoord van een set inloggegevens. |

### Eindpunten vault-item

De volgende API-methoden zijn beschikbaar:

| Request type | Endpoint                    | Gebruik                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | [INLINE_CODE_22]                 | Retourneert alle vault-items in secties waartoe de gebruikerscontext toegang heeft. |
| GET          | [INLINE_CODE_23] | Retourneert het gespecificeerde vault-item.                                   |
| POST         | [INLINE_CODE_24]                 | Creëert een nieuw vault-item met de gespecificeerde waarden.                 |
| PUT          | [INLINE_CODE_25] | Werkt het gespecificeerde vault-item bij.                                   |
| PATCH        | [INLINE_CODE_26] | Werkt bepaalde delen van het gespecificeerde vault-item gedeeltelijk bij. De [INLINE_CODE_27] en [INLINE_CODE_28] kunnen niet worden gewijzigd en blijven zoals ze zijn in deze bewerking. |
| DELETE       | [INLINE_CODE_29] | Verwijdert het gespecificeerde vault-item.                                   |

#### GET /VaultItem

De GET request [INLINE_CODE_30] heeft geen parameters. Deze retourneert een lijst met alle vault-items van secties waartoe u alleen bekijken-toegang heeft.

Voorbeeld inhoud:

[CODE_BLOCK_1]

#### GET /VaultItem/{VaultItemGuid}

De GET request [INLINE_CODE_31] retourneert het vault-item dat wordt geïdentificeerd door het vault-item Guid.

Voorbeeld van een vault-item geretourneerd in de inhoud van een 200 response:
[CODE_BLOCK_2]

U ziet dat waarden die gevoelige informatie bevatten, worden geretourneerd als een lege string.

#### PUT /VaultItem/{VaultItemGuid}

De PUT request naar eindpunt [INLINE_CODE_32] werkt het vault-item bij dat wordt geïdentificeerd door het vault-item guid. Zodra u een vault-item bijwerkt, wordt elke controleregel die een verwijzing naar dit vault-item bevat ook bijgewerkt, dus uw wijziging wordt onmiddellijk van kracht.

Deze request vereist ChangeVaultSection autorisatie.

Een PUT request verwacht de volgende objectstructuur:
[CODE_BLOCK_3]

Als er in het bovenstaande voorbeeld een waarde stond in het oorspronkelijke vault-itemsveld Omschrijving, zal het Omschrijving-veld leeggemaakt zijn. [INLINE_CODE_33] De enige waarden die niet verstrekt hoeven te worden zijn de gevoelige waarden. Als u bijvoorbeeld het veld Waarde of Wachtwoord weglaat, of het gehele object CertificateArchive, blijven deze ongewijzigd. Verder kunnen de kenmerken IsSensitive en VaultSectionGuid niet worden gewijzigd.

#### DELETE /VaultItem/{VaultItemGuid}

De DELETE request naar eindpunt [INLINE_CODE_34] verwijdert het gevraagde vault-item.

Als het gespecificeerde vault-item nog in gebruik is (bijvoorbeeld een controleregel verwijst naar dat specifieke vault-item), retourneert de dienst statuscode 400, inclusief een relevant bericht. Deze request vereist ChangeVaultSection autorisatie.

#### POST /VaultItem

De POST request naar eindpunt [INLINE_CODE_35] creëert een nieuw VaultItem object. Laat bij het specificeren van de VaultItem data de VaultItemGuid weg: de nieuwe Guid voor dit item wordt geretourneerd als onderdeel van de respons. Deze request vereist ChangeVaultSection autorisatie.

Voorbeeld inhoud:
[CODE_BLOCK_4]

## Vault-secties

Er zijn verschillende eindpunten in deze API waarmee u uw vault-secties kunt beheren. Elk vault-item behoort tot precies één vault-sectie. Als u slechts enkele vault-items in uw hele account nodig heeft, kunt u ze eenvoudigweg in een enkele vault-sectie opslaan. Echter, als het aantal vault-items in uw account toeneemt, kunt u ze in afzonderlijke secties gaan organiseren.

Elk Uptrends-account begint met één standaard vault-sectie. De groep Administrators heeft volledige toegang tot deze sectie, wat betekent dat zij de sectie en alle vault-items in die sectie kunnen bewerken.

Wanneer een nieuwe vault-sectie wordt gecreëerd, krijgt de gebruiker (operator) die hoort bij de API account die de vault-sectie creëert automatisch de ChangeVaultSection autorisatie voor de nieuwe sectie. Er worden geen andere autorisaties gecreëerd.

### Objectbeschrijving vault-sectie

Het volgende VaultSection object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam               | Beschrijving                                |
|--------------------|--------------------------------------------|
| [INLINE_CODE_36] | De unieke identifier van de vault-sectie |
| [INLINE_CODE_37]             | De naam van de vault-sectie              |

### Eindpunten vault-sectie

| Request type | Eindpunt                          | Gebruik                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | [INLINE_CODE_38]                    | Retourneert alle vault-secties waartoe de gebruikerscontext toegang heeft. |
| GET          | [INLINE_CODE_39] | Retourneert de gespecificeerde vault-sectie.                       |
| POST         | [INLINE_CODE_40]                    | Creëert een nieuw vault-item met de gespecificeerde naam.       |
| PUT          | [INLINE_CODE_41] | Werkt de gespecificeerde vault-sectie bij.                       |
| DELETE       | [INLINE_CODE_42] | Verwijdert de gespecificeerde vault-sectie.                       |

#### GET /VaultSection

De GET request [INLINE_CODE_43] heeft geen parameters. Deze retourneert een lijst met alle vault-secties waartoe u alleen bekijken-toegang heeft.

Voorbeeld inhoud:
[CODE_BLOCK_5]

#### GET /VaultSection/{VaultSectionGuid}

De GET request [INLINE_CODE_44] retourneert de vault-sectie die wordt geïdentificeerd door de vault-sectie Guid.

Voorbeeld inhoud:
[CODE_BLOCK_6]


#### POST /VaultSection

De POST request naar eindpunt [INLINE_CODE_45] creëert een nieuw VaultSection object. De operator onder wiens gebruikerscontext de request wordt verstuurd krijgt ViewVaultSection en ChangeVaultSection autorisaties voor de nieuwe sectie. Er worden geen andere autorisaties verleend. Laat bij het specificeren van de VaultSection data de VaultSectionGuid weg; de nieuwe Guid voor dit item wordt geretourneerd als onderdeel van de respons.
[CODE_BLOCK_7]

#### PUT /VaultSection/{VaultSectionGuid}

De PUT request naar eindpunt [INLINE_CODE_46] werkt de vault-sectie bij die wordt geïdentificeerd door de vault-item guid. Meestal is het enige doel hiervan het wijzigen van de naam van de vault-sectie. Deze request vereist ChangeVaultSection autorisatie.

[CODE_BLOCK_8]

#### DELETE /VaultSection/{VaultSectionGuid}

De DELETE request naar eindpunt [INLINE_CODE_47] verwijdert de gevraagde vault-sectie.

Als de gespecificeerde vault-sectie nog in gebruik is (wat betekent dat er vault-items opgeslagen zijn in die sectie), zal de dienst statuscode 400 retourneren, inclusief een relevant bericht. Als dit het geval is, moet u de vault-items verwijderen voordat u de vault-sectie kunt verwijderen. Houd er rekening mee dat u een vault-item niet kunt verwijderen als het item nog in gebruik is (bijvoorbeeld wanneer een controleregel is geconfigureerd om dat vault-item te gebruiken). Deze request vereist ChangeVaultSection autorisatie.

## Autorisaties vault-sectie

Naast het gescheiden houden van vault-items, kunt u met vault-secties ook bepalen wie waartoe toegang heeft. Als een specifieke groep operators exclusieve toegang moet hebben tot bepaalde vault-items, dan plaatst u die vault-items in een aparte sectie. Alleen mensen die toegang hebben tot die vault-sectie kunnen de items in die sectie zien.

Zodra u een nieuwe vault-sectie creëert (via de API of via de online app), is die sectie eerst alleen zichtbaar voor u. Als u er vault-items aan heeft toegevoegd, kunnen andere operators deze vault-items niet bewerken of gebruiken.

Om ervoor te zorgen dat andere mensen de nieuwe vault-sectie kunnen gebruiken, er items aan toe kunnen voegen en/of deze vault-items kunnen selecteren in controleregelinstellingen, zult u ze toegang moeten geven. Dit kunt u doen met de volgende API-methoden.

Er zijn twee autorisatietypen: [INLINE_CODE_48] en [INLINE_CODE_49]. Deze autorisatietypen kunnen worden toegekend aan operators en operatorgroepen.

### Objectbeschrijving autorisatie

Het volgende Authorisatie-object wordt gebruikt in de hieronder beschreven API-methoden:

| Naam                | Beschrijving                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_50]   | De unieke id van de autorisatie.                                                                                                                        |
| [INLINE_CODE_51]         | De unieke identifier van de context waarvoor de autorisatie is gemaakt. In het geval van een vault-sectieautorisatie is dit de vault-sectie Guid. |
| [INLINE_CODE_52] | [INLINE_CODE_53] of [INLINE_CODE_54].                                                                                                                |
| [INLINE_CODE_55]      | Als de autorisatie moet worden toegepast op een enkele operator, specificeert dit de operator Guid. Ingesteld op [INLINE_CODE_56] voor operatorgroepautorisaties.             |
| [INLINE_CODE_57]   | Als de autorisatie moet worden toegepast op een operatorgroep, specificeert dit de operatorgroep-ID. Ingesteld op [INLINE_CODE_58] voor autorisaties voor één operator.        |

### Vault-sectie autorisatie eindpunten

| Request type | Eindpunt                                                            | Gebruik                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_59]                     | Retourneert een lijst met alle autorisaties voor de gespecificeerde vault-sectie.                   |
| POST         | [INLINE_CODE_60]                     | Creëert een nieuwe autorisatie voor de gespecificeerde vault-sectie, met behulp van de waarden die verstrekt worden. |
| DELETE       | [INLINE_CODE_61] | Verwijdert de gespecificeerde autorisatie.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

De GET request naar [INLINE_CODE_62] retourneert een lijst met alle autorisaties voor de vault-sectie die is gespecificeerd in VaultSectionGuid.

Voorbeeld inhoud:
[CODE_BLOCK_9]


Een autorisatie is voor een operator of een operatorgroep. Een operatorspecifieke autorisatie bevat gegevens in de OperatorGuid en de OperatorGroupId is leeg; een autorisatie voor een operatorgroep heeft een waarde in OperatorGroupId en een lege OperatorGuid.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

De POST request naar [INLINE_CODE_63] creëert een nieuwe autorisatie voor de gespecificeerde vault-sectie.

Voorbeeld inhoud:

[CODE_BLOCK_10]

Als u een autorisatie van het type ChangeVaultSection creëert, wordt er automatisch een extra ViewVaultSection autorisatie voor dezelfde operator of operatorgroep toegevoegd. Als een operator of operatorgroep Change \+ View autorisaties heeft voor een vault-sectie, verschijnt deze als *Volledige autorisatie* in de Uptrends-app.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

De DELETE request naar [INLINE_CODE_64] verwijdert een bestaande autorisatie.
