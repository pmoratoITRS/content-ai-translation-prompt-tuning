{
  "hero": {
    "title": "Waarschuwingen, tips en trucs"
  },
  "title": "Waarschuwingen, tips en trucs",
  "summary": "Bij het instellen van transactiecontroleregels kunt u een paar dingen overwegen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/waarschuwingen-tips-en-trucs-voor-transactie-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Transactiemonitoring (Web Application Monitoring) kan merkreputatie en omzet redden door problemen met uw transacties vast te leggen voordat ze gevolgen hebben voor uw gebruikers. Transactiemonitoring is een synthetische monitoringbenadering waarbij Uptrends' controlestations een script volgen om echte gebruikerstrajecten te simuleren. Bij het instellen van gebruikerstests is het belangrijk om na te denken over de gevolgen van uw tests op de korte en lange termijn. U kunt veel problemen voorkomen door uw transactie zorgvuldig in kaart te brengen voordat u deze opneemt. Elke gebruikssituatie is anders, maar we hebben een aantal veelvoorkomende problemen gevonden waar u wellicht aan wilt denken bij het instellen van uw transactiemonitoring.

## Voorkom voorraadtekorten

Voorraadtekorten als gevolg van het testen van winkelwagens en kassatransacties kunnen problemen met uw voorraad veroorzaken. Bij het synthetisch testen worden er maar liefst 288 keer per dag bestellingen geplaatst. En als dit niet correct wordt afgehandeld, kan door testen uw voorraad verminderen, waardoor het item niet meer beschikbaar is voor uw gebruikers. We hebben daadwerkelijk problemen gezien waarbij het magazijn de bestellingen al verwerkte en klaarmaakte voor verzending. We hebben verschillende oplossingen gezien om voorraadproblemen te voorkomen.

**Database oplossing**

Hoewel we hebben gezien dat sommige bedrijven ervoor kiezen om testaankopen en -winkelwagens handmatig uit de database te verwijderen, kan een opgeslagen procedure of geautomatiseerd proces betrouwbaarder blijken te zijn. U kunt bijvoorbeeld uw orderverwerkingssysteem orders laten negeren die door de testgebruiker zijn geplaatst of orders die vanaf de [IP-adressen van Uptrends' controlestations]([LINK_URL_1]) zijn geplaatst.

**Gebruik (virtuele) testitems**

Misschien vindt u het handig om een voorraaditem te maken dat uitsluitend voor testdoeleinden wordt gebruikt. Als u een testitem gebruikt, blijft uw werkelijke voorraad nauwkeurig en beschikbaar. Testitems kunnen u ook helpen bij het identificeren van testtransacties bij het opschonen van uw databases en voorkomen dat er onbedoeld werkelijke items worden verzonden.

**Dump de winkelwagen**

Als u een winkelwagentransactie test, bouw dan itemverwijdering in in de transactiestappen. Voeg een item toe en verwijder het item voordat u de transactie sluit.

[SHORTCODE_1]
**Opmerking**: Door artikelen uit de winkelwagen te verwijderen, kunt u de voorraad beschikbaar houden voor uw gebruikers. Maar als de transactie mislukt voordat het script de items uit de winkelwagen verwijdert, kunnen winkelwagenitems zich nog steeds ophopen. Monitor de winkelwagen van de testgebruiker regelmatig op het wissen van items.
[SHORTCODE_2]

**Kies een artikel met grote hoeveelheden**

Als u een echt artikel gebruikt, kies dan een artikel om te testen dat in zulke grote hoeveelheden aanwezig is dat een voorraadtekort bijna onmogelijk wordt.

## Houd bevoorradingssystemen in de gaten

Voorraadbeheersoftware heeft vaak een proces dat populaire items of items met een lage voorraad automatisch bijbestelt. Om een overvloed van het item in uw voorraad te voorkomen raadpleegt u uw systeembeheerders over de beste aanpak, zoals het gebruik van een testitem of het uitschakelen van automatisch aanvullen voor het item. 

## Vermijd het vollopen van afspraken en reserveringen

Als uw transactiecontroleregels testen op zaken als doktersafspraken, hotelkamers, vluchten of dinerreserveringen, kunnen uw tijdslots al snel vol of uitverkocht raken. Het identificeren en opschonen van door testen gemaakte afspraken is van cruciaal belang.

## Uw transactiecontroleregel ZAL e-mails versturen

Als een deel van uw transactie een e-mailveld bevat en uw transactie om welke reden dan ook bevestigingsmails verstuurt, zoals facturen, wachtwoordresets of gebruikers-ID-herinneringen, genereert uw transactiecontroleregel ook e-mails. Gebruik een e-mailadres als noreply@mysite.com voor uw transactiecontroleregel om een mailbox vol ongewenste e-mails te voorkomen. 

## Onverwachte creditcardkosten

Als u een echte creditcard gebruikt bij het testen van de afrekenprocessen, kunt u kosten en merchant fees opbouwen, kan er beslag op de beschikbare fondsen worden gelegd en activeert u fraudewaarschuwingen vanwege de frequente transacties. Gebruik in plaats daarvan testcreditcardaccounts. De meeste betaaldiensten bieden testrekeningnummers aan waarmee u de kassatransactie kosteloos kunt testen zonder problemen met een echte account te veroorzaken.

## Nieuwe oplossingen voor het maken van accounts

Wanneer u nieuwe accountinstellingen test, kunt u dit slechts één keer doen met dezelfde gebruikersnaam. De tweede keer dat het script wordt uitgevoerd, zal de transactie mislukken vanwege de dubbele account. We hebben enkele oplossingen gezien voor het testen van de accountinstellingen.

### Verstrek de data niet

Hoewel deze optie geen volledige test biedt voor de volledige accountconfiguratie, hebben sommige Uptrends-gebruikers ervoor gekozen om vlak voor de laatste bevestiging te stoppen. De controleregel test alle aspecten van het proces voor het creëren van een account, behalve het definitieve indienen.

### Database oplossingen

U kunt overwegen om een database trigger te gebruiken om te controleren op de ID van de testaccount na een CREATE-gebeurtenis die de testaccount uit de database verwijdert voordat de volgende test begint.

### Genereer nieuwe unieke logins

U kunt ook nieuwe unieke logins genereren door zaken zoals de tijd- en datumstampel te gebruiken. Vergeet niet om ze regelmatig te verwijderen. [Neem contact op met support]([LINK_URL_2]) voor meer informatie.

## Account is al ingelogd

Als u dezelfde inloggegevens voor meerdere controleregels gebruikt of als u na een test niet uitlogt, kunt u fouten genereren. De beste aanpak is om voor elke controleregel een ander testgebruikersaccount in te stellen en altijd uit te loggen als laatste stap in het testproces om onnodige alerts te voorkomen.

## Beschermen van gevoelige informatie

Als een gebruiker moet inloggen om een taak uit te voeren, moet de controleregel ook inloggen. Denk aan het authenticatieproces en het beschermen van logins en wachtwoorden. U kunt uw authenticatie-informatie beschermen in onze [vault]([LINK_URL_3]), en deze verbergen in uw testresultaten. 

Overweeg ook de gebruikersrechten die u de testgebruiker verleent vanuit een beveiligingsoogpunt en houd de gebruiker in de gaten om er zeker van te zijn dat er geen verdachte activiteit is.  

## Gebruik content checks

[Content checks]([LINK_URL_4]) (inhoudcontroles) zijn gratis en u kunt er een toevoegen aan elke stap in uw transactie. Inhoudcontroles zijn een goede manier om er zeker van te zijn dat de pagina volledig is geladen en dat de browser de juiste inhoud heeft ontvangen. U kunt content checks op drie verschillende manieren toevoegen: via de knop *Add content check* of via het contextmenu. U kunt content checks ook later toevoegen met de controleregel-stapeditor in uw account. Raadpleeg de [stapsgewijze handleiding winkelwagen]([LINK_URL_5]) om te weten te komen hoe u content checks gebruikt in echte scenario's.

## Gebruik toetsenbordacties
Met de transaction recorder kunt u ook toetsenbordacties van de gebruiker vastleggen. U kunt kiezen uit verschillende tekens, variërend van Control-toets, speciale toetsen, cijfertoetsen, numerieke toetsen, hoofdletter- en kleinelettertoetsen. Kies of deze toets globaal moet worden ingedrukt of alleen bij het huidige gefocuste element of laatst aangeklikte element. 

Dit is handig wanneer u websites tegenkomt met instructies als *Druk op een willekeurige toets om door te gaan* of *Druk op Enter om te bevestigen*. Houd er rekening mee dat u, anders dan met muisklikactiviteiten (die automatisch een beweging vastleggen), een toetsenbordactie handmatig moet toevoegen om een toetsenbordgebeurtenis vast te leggen en deze als een daadwerkelijke activiteit te laten gelden. Raadpleeg de [stapsgewijze handleiding winkelwagen]([LINK_URL_6]) voor meer informatie over toetsenbordacties.

## Gebruik de acties Hover en Wacht tot element zichtbaar is

U kunt ook muishoveracties opnemen en controleren of een element zichtbaar is wanneer u rechtsklikt op een element op de pagina en de juiste optie kiest in het contextmenu *ITRS Uptrends Transaction Recorder*. Dit is handig wanneer u wilt controleren of een element bepaalde hovertriggers heeft, zoals het weergeven van een bericht of het later zichtbaar maken van een element of submenu's. Bekijk de [stapsgewijze handleiding winkelwagen]([LINK_URL_7]) voor echte voorbeelden.

[SHORTCODE_3]
**Opmerking:** Elke gebruikssituatie is anders, dus aarzel niet contact op te nemen met onze scriptschrijvers om u te helpen oplossingen te vinden die passen bij uw unieke situaties. Gebruik het [ticketsysteem]([LINK_URL_8]) of voeg een notitie toe aan uw transactieopname om de schrijvers op de hoogte te stellen van eventuele zorgen.
[SHORTCODE_4]
