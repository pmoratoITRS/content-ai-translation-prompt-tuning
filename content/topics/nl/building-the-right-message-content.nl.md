{
  "hero": {
    "title": "De juiste berichtinhoud bouwen"
  },
  "title": "De juiste berichtinhoud bouwen",
  "summary": "Aangepaste integratie - uw eigen berichtinhoud creëren",
  "url": "/support/kb/alerting/integraties/aangepaste-integraties/de-juiste-berichtinhoud-bouwen",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/building-the-right-message-content" 
}

Om relevante inhoud voor de velden in elk uitgaand alertbericht in te vullen, moet de berichtinhoud die u definieert zogenaamde systeemvariabelen bevatten. Wanneer u in uw berichtinhoud naar een systeemvariabele verwijst, wordt deze vervangen door de juiste inhoud wanneer Uptrends een alert genereert. Met systeemvariabelen kunt u berichtdefinities schrijven die voldoen aan de verwachtingen van het andere systeem. In dit artikel bespreken we hoe u verschillende variabelen instelt en gebruikt in de uitgaande berichten van uw aanpasbare integratie. Als u begrijpt hoe u variabelen moet gebruiken in uw aanpasbare integratie, wilt u misschien eens kijken naar de [volledige lijst met beschikbare systeemvariabelen](/support/kb/alerting/integraties/aangepaste-integraties/systeemvariabelen-voor-alerting).

## Correct gebruik van variabelen

Laten we een voorbeeld bekijken. Een voor de hand liggend stuk informatie dat waarschijnlijk deel moet uitmaken van elk alertbericht, is een eenvoudige tekstuele beschrijving van de fout die door Uptrends is gedetecteerd. Stel dat het systeem waarmee u wilt koppelen een veld genaamd "errordescription" heeft. U zou Uptrends' foutbeschrijving in dat veld kunnen invoeren door deze definitie op te nemen in uw JSON-geformatteerde bericht:

`{ "errordescription": "{{@alert.description}}" }`

In de systeemvariabelen van Uptrends is de tekstuele beschrijving van de fout die een alert triggert beschikbaar in de variabele {{@alert.description}}, dus u plaatst die variabele gewoon waar u hem nodig heeft in uw bericht. Op dezelfde manier kunt u {{@ alert.timestamp}} gebruiken om naar het tijdstip van de alert te verwijzen, {{@ monitor.name}} om de naam van de controleregel op te nemen enzovoort. U vindt een lijst met alle beschikbare systeemvariabelen in [dit knowledge base-artikel](/support/kb/alerting/integraties/aangepaste-integraties/systeemvariabelen-voor-alerting).

{{< callout >}}**Tip:** U kunt op verschillende punten verwijzingen naar [vault-inloggegevens](/support/kb/vault) gebruiken in de aangepaste integratieconfiguratie, zoals de request body, de URL of de authenticatievelden. Zie hoofdstuk [Inloggegevens uit de vault gebruiken](/support/kb/synthetic-monitoring/api-monitoring/multi-step#inloggegevens-uit-de-vault-gebruiken) in ons artikel over het configureren  van multi-step API-monitoring, voor een beschrijving van hoe u dit configureert. {{< /callout >}}

## Variabelen specificeren per escalatieniveau

Wanneer in een integratie de optie Aanpassen actief is, kunt u een of meer variabelen voor die integratie in de tab Algemeen behouden. De standaardinstelling voor voorgedefinieerde integratievariabelen (zoals aangegeven door Waarde hier opgeven) is dat de waarde voor die variabelen wordt gedefinieerd als een vaste waarde in de integratie. U kunt vervolgens naar die variabelen verwijzen in de berichtdefinitie in de tab {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}}. Meer informatie over het definiëren en gebruiken van variabelen vindt u in dit Knowledge Base-artikel over [variabelen gebruiken in een multi-step API-set-up](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variabelen). Voor integraties geldt precies dezelfde aanpak.

Voor integraties heeft u echter één extra optie die nog meer kracht toevoegt. Stel dat u een integratie heeft gecreëerd die verbinding maakt met uw IT-managementsysteem. De integratie stuurt informatie op basis van de controleregel en alert die het alertbericht heeft getriggerd. Maar is dat voldoende informatie voor het IT-managementsysteem om passende maatregelen te nemen? U kunt wat aanvullende informatie sturen over hoe met het nieuwe incident moet worden omgegaan. U kunt deze informatie meestal uitdrukken als: hoe moet het incident door het externe systeem worden behandeld? Verschillende alertdefinities (in feite elk escalatieniveau daarbinnen) kunnen unieke routinginformatie specificeren, die u in het uitgaande alertbericht kunt opnemen.

Om dit te doen definieert u een variabele in de tab {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}} van de integratie en kiest u *Waarde opgeven in het escalatieniveau*. U ziet dat u hem geen waarde meer kunt geven in de integratie zelf. In plaats daarvan kunt u, wanneer u deze integratie in de escalatieniveaus van uw alertdefinities gebruikt, daar waarden voor deze variabele opgeven. Hierdoor hoeft u slechts één integratiedefinitie voor uw IT-managementsysteem te maken, terwijl u flexibiliteit behoudt in de manier waarop alle alerts daar worden afgehandeld.

### Inloggegevens uit de vault gebruiken

Het is mogelijk om op elk punt verwijzingen naar [vault-inloggegevens](/support/kb/vault) te gebruiken als onderdeel van de request body, request headers of als de waarde voor uw gebruikersnaam/wachtwoord onder *Authenticatie*. Gebruik de volgende syntaxis om naar een vault-item te verwijzen: `{{@VaultItem.<itemGuid>.Password}}` ('Username' is uiteraard ook geldig). U kunt de `itemGuid` voor de inloggegevens vinden door ernaartoe te navigeren in uw accountvault en zijn URL te lezen.

![Voorbeelden van verwijzingen naar vault-items](/img/content/scr-MSA-vault-creds-references.png)

## Externe ID's of aangepaste data opnemen

Wanneer u Uptrends integreert met een third-partysysteem, is het goed om na te gaan of er een verband is tussen uw Uptrends-controleregels en de bronnen (soms componenten of services genoemd) die u in het third-partysysteem heeft gedefinieerd. De controleregels in uw Uptrends-account hebben een naam en een unieke identifier (een monitorGuid), maar deze zijn meestal niet bekend in het third-partysysteem. De bronnen die in het third-partysysteem zijn gedefinieerd, hebben waarschijnlijk ook hun eigen identifier, die Uptrends ook niet kent.

Als u wilt dat een controleregel in Uptrends een incident voor een specifieke bron aan de andere kant triggert, moet u een soort relatie tussen de twee definiëren. In Uptrends kunt u die relatie definiëren door de identifier (of andere belangrijke informatie) van de externe bron/component te nemen en deze als een aangepaste waarde toe te voegen aan de instellingen van een controleregel.

Hierdoor kunnen de alertingdata die door Uptrends naar het externe systeem zijn verstuurd die identifier bevatten, zodat het ontvangende systeem weet welke bron of component door de binnenkomende alert is beïnvloed.

U kunt aangepaste velden toevoegen in het gedeelte Metadata in de tab {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}} van een controleregel. Naast de externe waarde die u wilt opslaan, moet elk aangepast veld ook een unieke naam hebben, zodat we ernaar kunnen verwijzen in een alertbericht. Stel bijvoorbeeld dat uw third-partysysteem het concept van Components heeft en dat elke component een ComponentId als unieke identifier heeft. U wilt dan dat ComponentId specificeren in de controleregelinstellingen in Uptrends, zodat de twee aan elkaar kunnen worden gekoppeld.

Om dit te doen gaat u naar het gedeelte Vrije velden in de instellingen van uw controleregel. Voeg een vrij veld toe door "ComponentId" als de veldnaam in te vullen en de juiste externe ID-waarde (bijvoorbeeld 7149488f-0b33-460d-85eb-210c0e80d7ba) als de veldwaarde. Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om de nieuwe instellingen te bewaren.

We kunnen er nu voor zorgen dat de externe waarde als onderdeel van het alertbericht wordt verstuurd door deze op te nemen in de request body van het uitgaande bericht. U kunt de functie {{@CustomField ()}} gebruiken om te verwijzen naar het vrije veld dat u zojuist heeft toegevoegd. U kunt bijvoorbeeld dit fragment toevoegen aan de request body:

`{ "Component": "{{@CustomField(ComponentId)}}" }`

U ziet dat de veldnaam "ComponentId" die we in de controleregelinstellingen hebben gebruikt, letterlijk is opgenomen in de function call @CustomField (). Wanneer er een echte alert wordt getriggerd, genereert dit de volgende inhoud:

`{ "Component": "7149488f-0b33-460d-85eb-210c0e80d7ba" }`

Het externe systeem kan deze waarde gebruiken om een incident voor de juiste component te maken. In dit voorbeeld wordt slechts één vrij veld gebruikt, maar u kunt ervoor kiezen meerdere aangepaste waarden te gebruiken.
