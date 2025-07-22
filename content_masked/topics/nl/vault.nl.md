{
  "hero": {
    "title": "Vault"
  },
  "title": "Vault",
  "url": "[URL_BASE_TOPICS]account/vault",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De Uptrends **Vault** is een gecentraliseerde opslag die u helpt uw gebruikersnamen, wachtwoorden, certificaten en andere gevoelige informatie te beheren als onderdeel van uw controleregelconfiguratie.

Met deze functie kunt u uw inloggegevens opslaan als **Vault-items** en deze bij meerdere controleregels gebruiken. Als u bijvoorbeeld een combinatie van [INLINE_CODE_1] en [INLINE_CODE_2] moet gebruiken voor zowel Multi-Step API (MSA)- als Transactiecontroleregels, kunt u deze definiëren als vault-items en deze op beide controleregels toepassen. Als er wijzigingen worden aangebracht in uw vault-items, past de **Vault** deze wijzigingen automatisch toe op alle controleregels die het vault-item gebruiken. Op deze manier kunt u uw data allemaal eenvoudig op één plek ordenen en bijhouden.

De **Vault** is zonder extra kosten inbegrepen in alle abonnementen.

[SHORTCODE_1]
**Een goedbedoelde herinnering:** Voor de veiligheid en best practices moet u de Uptrends-vault alleen gebruiken om al uw gevoelige informatie in Uptrends te beheren. Het is niet raadzaam om deze vault te gebruiken als de primaire locatie om geheimen op te slaan of voor algemeen wachtwoordbeheer.
[SHORTCODE_2]

## Functies van de Vault

De **Vault** biedt een verscheidenheid aan functies om uw informatie veilig op te slaan. Deze functies omvatten het definiëren van uw **Vault-items**, het groeperen van elk vault-item met behulp van **Vault-sectie** en het beheren van toegangsrechten met behulp van **Gebruikersrechten**.

Voor toegang tot de **Vault** gaat u naar [SHORTCODE_3] Accountinstellingen > Vault [SHORTCODE_4] om de vault-functies gemakkelijk te bekijken en te openen.

## Vault-secties

Alle items die in de vault zijn opgeslagen, zijn georganiseerd in **Vault-secties**. Deze dienen als de hoofdcontainer of parent van uw vault-items. Standaard beginnen alle Uptrends-accounts met één vault-sectie en moet elk vault-item dat u opslaat, tot precies één sectie behoren. 

Let op: leden van de groep Administrators hebben exclusieve toegang tot alle items die zijn opgeslagen in de standaardsectie; alle Administrators kunnen dus elk vault-item bekijken en wijzigen. 

Een nieuwe **Vault-sectie** creëren:

1. Klik in de rechter bovenhoek van uw scherm op de knop [SHORTCODE_5] Vault-sectie toevoegen [SHORTCODE_6].
2. Geef in de sectie **Details** de **Naam** op van de vault-sectie. Het is raadzaam om een naam te gebruiken die het doel en de opgeslagen items duidelijk definieert.
3. Klik op [SHORTCODE_7] Opslaan [SHORTCODE_8] om de wijzigingen te bevestigen.

Nadat u deze heeft gecreëerd, kunt u nu [Vault-items]([LINK_URL_1]) toevoegen en [Vault Gebruikersrechten]([LINK_URL_2]) verlenen.

Een **Vault-sectie** verwijderen:

1. Klik op de knop [SHORTCODE_9] Deze Vault-sectie verwijderen [SHORTCODE_10].
2. Klik in de **Bevestigingspop-up** op [SHORTCODE_11] Verwijderen [SHORTCODE_12] om de wijzigingen te bevestigen.

## Vault-itemtypen

Zodra u uw vault-sectie heeft, kunt u uw vault-items categoriseren en toevoegen. 

Een **Vault-item** toevoegen:

1. Klik in de rechter bovenhoek van uw scherm op de knop [SHORTCODE_13] Vault-item toevoegen [SHORTCODE_14]. 
2. Vul in het tabblad [SHORTCODE_15] Algemeen [SHORTCODE_16] het gedeelte **Details** als volgt in:

- Naam — geef een unieke naam op voor het vault-item.
- Sectie — kies uit de bestaande Vault-secties in het vervolgmenu.
- Omschrijving — geef een beschrijving of aanvullende opmerkingen over het vault-itemtype.
- Type — kies uit de verschillende vault-itemtypen die beschikbaar zijn in het vervolgmenu. De **Vault** ondersteunt verschillende typen data die u voor een bepaald doel kunt opslaan. Hieronder staan de beschikbare vault-itemtypen:

### Inloggegevens [ANCHOR_1]

Dit type vault-item is gedefinieerd als een combinatie van gebruikersnaam en wachtwoord. U kunt ze gebruiken in controleregeltypen die een gebruikersnaam of wachtwoord accepteren voor authenticatie, zoals basic, NTLM en digest authenticatie in multi-step API-controleregels, logins in SMTP, POP3, IMAP, SQL, FTP en SFTP, en gebruikersnamen en wachtwoorden die worden gebruikt in transactiescripts.

### Certificaatarchief

Dit type vault-item kan een beveiligingscertificaat opslaan in de vorm van een PKCS \#12 certificaatarchief (meestal een .p12 of .pfx bestand) dat de private key van een certificaat en zijn public key bevat. Nadat het is geüpload, kunt u het certificaat gebruiken als een clientcertificaat in Multi-step API controleregels.

Als u een certificaatarchiefbestand (een .p12 of .pfx bestand) heeft dat uw private en public key bevat, selecteert u dat bestand in het veld **Nieuw archief uploaden**. Het archiefbestand is in de meeste gevallen versleuteld, dus u moet het bijbehorende wachtwoord opgeven in het veld **Wachtwoord van het archief**.

### Public key van het certificaat

Dit type vault-item moet worden gebruikt wanneer u Single Sign-on instelt voor Uptrends. Dit vault-itemtype slaat de public key op die wordt gegenereerd door uw Identity Provider (IdP). Wanneer uw IdP SAML-inlogverzoeken naar Uptrends stuurt, ondertekent die deze verzoeken met een certificaat. Uptrends gebruikt de public key die u heeft opgegeven om te verifiëren of het inkomende verzoek daadwerkelijk van uw IdP komt.

Als u een public key aan de vault wilt toevoegen, heeft u waarschijnlijk al een public key-bestand (meestal een .pem- of .cer-bestand). Kopieer de inhoud van het bestand, dat Base64-gecodeerde inhoud moet zijn die kan worden gelezen als een X.509-certificaat, naar het veld ** Public key**.

### Bestand [ANCHOR_2]

Dit type vault-item kan worden gebruikt om bestanden op te slaan, die vervolgens kunnen worden geüpload als onderdeel van een [Self-Service transactiecontroleregel]([LINK_URL_3]) flow. Meer informatie over het instellen van bestandsuploads in uw transacties vindt u in onze [documentatie over pagina-interacties]([LINK_URL_4]) in transactiecontroleregels. Elk bestandstype of elke extensie wordt ondersteund en we stellen automatisch het juiste MIME-type in (een universele manier om de aard en de indeling van bestanden op internet te specificeren), indien van toepassing. De maximale bestandsgrootte is 2 MB.

Bestanden kunnen worden geüpload door op de knop **Bestand kiezen** te klikken die verschijnt wanneer het vault-itemtype Bestand is geselecteerd. De Naam en MIME-type eigenschappen worden automatisch ingevuld. We raden u aan het vault-item een geschikte naam te geven, zodat u er gemakkelijk naar kunt verwijzen bij het instellen van de [bestandsupload-acties]([LINK_URL_5]) in uw transactie- of [Multi-Step API-controleregel]([LINK_URL_6]).

### Configuratie eenmalig wachtwoord (OTP, one-time password) of tijdgebaseerd eenmalig wachtwoord (TOTP, time-based one-time password) [ANCHOR_3]

Dit type vault-item slaat een *geheime* waarde op die wordt gebruikt om een eenmalige wachtwoordcode te genereren. U kunt dit vault-item gebruiken als alternatieve optie om [een OTP-gebaseerde tweefactorauthenticatie (2FA) in te stellen]([LINK_URL_7]) om een [webapplicatie]([LINK_URL_8]) te monitoren waarbij gebruikers een code moeten invoeren voor inlogverificatie.

De volgende velden kunnen worden geconfigureerd op basis van uw voorkeuren:

- Geheime codeermethode — het type codeermethode dat wordt gebruikt voor de geheime waarden. Kies *Hex* als de geheime waarde die u heeft ingevoerd Hex-gecodeerd is (bestaande uit hexadecimale cijfers van 0-9 en A-F). Kies anders het Uptrends-standaardformaat, *Base32*, als uw geheime waarde Base-32-gecodeerd is (bestaande uit 32 tekens van A-Z en 2-7).
- Cijfers — de lengte van de gegenereerde eenmalige wachtwoordcode. De code kan bestaan uit *6, 7 of 8* cijfers.
- Expiratietijd (s) — de duur dat het eenmalige wachtwoord geldig blijft. De vervaltijd varieert van *1 tot 120* seconden.
- Algoritme — het type Secure Hash-algoritme (SHA) dat wordt gebruikt. Algoritmen kunnen *SHA512* (64-byte hash), *SHA256* (32-byte hash) of *SHA1* (20-byte hash) zijn.

## Vault Gebruikersrechten

### Vault-toegang beperken tot specifieke personen
In sommige gevallen is het nuttig om meer controle te hebben: verschillende operators/groepen kunnen verschillende verantwoordelijkheden hebben, en meestal is het een goed idee om toegang tot gevoelige data zoveel mogelijk te beperken.

Toegangsregels tot de vault kunnen op vault-sectieniveau worden ingesteld: u kunt de oorspronkelijk ingestelde rechten voor de standaard vault-sectie veranderen, u kunt extra vault-secties creëren en toegang verlenen aan specifieke operatorgroepen en individuele operators. 

Er zijn twee rechtenniveaus beschikbaar voor vault-secties:

-   **Volledige rechten**: operators/groepen met dit toegangsniveau voor een vault-sectie kunnen vault-items toevoegen aan en verwijderen uit die sectie, zij kunnen de vault-items die in die sectie zijn opgeslagen bijwerken en de toegangsrechten voor die sectie beheren.
-   **Alleen bekijken**: dit toegangsniveau is nodig om de vault-items die in een sectie zijn opgeslagen te kunnen bekijken bij het selecteren van een vault-item voor zijn beoogde gebruik (als een certificaat of inloggegevens in controleregelinstellingen, of als Public key van een certificaat in Single Sign-on-instellingen). Belangrijk: zodra een vault-item is geconfigureerd als onderdeel van een controleregel, zijn de bewerkingsprivileges voor die controleregel beperkt tot operators die Alleen bekijken-toegang hebben voor de betreffende vault-sectie. Bewerkingsprivileges worden beperkt om ongeautoriseerde toegang tot de inhoud van het vault-item te voorkomen.

## Vault API-itembeheer

Een van de voordelen van het configureren van een vault-item is dat elke wijziging in dat vault-item automatisch wordt toegepast bij alle controleregels die dat item gebruiken. Dit is handig als u een beleid voert waarbij inloggegevens die in uw controleregels worden gebruikt, verlopen. Stel dat die inloggegevens elke x dagen in uw eigen netwerkomgeving vervallen. U hoeft dan alleen maar de inhoud van het vault-item dat die inloggegevens bevat in Uptrends te veranderen: de bijbehorende controleregels zullen automatisch de bijgewerkte inloggegevens gebruiken.  
  
U kunt nog een stap verder gaan door het bijwerken van het vault-item te automatiseren. U kunt Uptrends [Vault API]([LINK_URL_9]) aanroepen vanaf uw eigen backend om de inloggegevens in een bestaand vault-item bij te werken. Meer informatie hierover vindt u in de [API-documentatie]([LINK_URL_10]).
