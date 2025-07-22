{
  "hero": {
    "title": "Uw transacties begrijpen"
  },
  "title": "Uw transacties begrijpen",
  "summary": "Inzicht in uw transacties, de vele paden die ze kunnen nemen en op de hoogte zijn van de valkuilen bij transactiemonitoring, leidt tot betere monitoring en resultaten. ",
  "url": "/support/kb/synthetic-monitoring/transacties/uw-transacties-begrijpen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-your-transactions"
}

Voordat u kunt beginnen met het opnemen of scripten van uw transacties, moet u een plan en een goed begrip hebben van uw transacties. Als u een goed plan heeft voordat u begint met het opnemen van uw transacties, kan dit u helpen bij het opname- en testproces en om later andere problemen te voorkomen.

## Ken uw transacties en breng ze in kaart

Niet alle transacties zijn hetzelfde opgebouwd. Een goede manier om meer inzicht te krijgen in uw transacties, is door ze in kaart te brengen. Om te beginnen:

- Maak een lijst van de belangrijkste taken die uw gebruikers moeten uitvoeren op uw website of app,
- Genereer stroomdiagrammen van de belangrijkste taken. Denk na over de verschillende paden die de gebruiker kan nemen om verschillende doelen op uw site te bereiken (er kunnen meerdere paden naar hetzelfde doel zijn).
- Zorg ervoor dat u zowel uw happy paths (het pad waarbij alles volgens plan verloopt) als de unhappy paths (gebruikersfouten en systeemstoringen) in kaart brengt. Voorbeelden van unhappy paths zijn problemen zoals mislukte gebruikersauthenticatie, items die niet op voorraad zijn, ongeldige creditcardgegevens, falende ondersteunende systemen zoals merchant services of databasefouten. Mogelijk wilt u deze veelvoorkomende problemen testen om er zeker van te zijn dat uw systeem correct reageert.

Hieronder vindt u de belangrijkste functies en gebruikerstrajecten voor een eenvoudige e-commercesite. Het diagram beschrijft verschillende happy paths die een gebruiker kan nemen. Sommige taken zijn afhankelijk van de succesvolle afronding van andere taken, en u zou sommige taken verder kunnen opsplitsen.

![](/img/content/3604c5bd-5c6e-4f07-acd7-0010408a7f18.png)

Laten we om het eenvoudig te houden alleen kijken naar de functionaliteit van de winkelwagen. De functionaliteit van de winkelwagen bestaat uit de eenvoudige taak om een item te selecteren, dit toe te voegen aan de winkelwagen en de winkelwagen te bewerken.

De verleiding is groot om de winkelwagenfunctionaliteit uit te breiden met testen voor het zoeken of het afrekenproces. Het wordt aanbevolen om de functionaliteit gecompartimenteerd te houden, zodat u één belangrijke taak tegelijk test.

![](/img/content/fc2b70c0-8ecf-4071-8f2b-67b3be0aa537.png)

## Andere dingen die u moet overwegen

Voordat u begint met het opnemen van uw transacties, moet u verschillende dingen overwegen:

-   Lees het artikel over [Kiezen welke transacties u kunt of moet testen]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="nl" >}}) om meer te weten te komen over de soorten transacties die u kunt en moet monitoren met transactiemonitoring. Het artikel bevat ook een opmerking over het selecteren van de controlestations voor het monitoren van uw transacties.
-   Transactiemonitoring kan reële gevolgen hebben voor een bedrijf, van het consumeren van artikelvoorraad tot het opbouwen van merchant fees. Lees het artikel [Waarschuwingen, tips en trucs voor transactiemonitoring]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="nl" >}}) voordat u een transactiecontrolergel in [staging of production mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}}) plaatst.

Als dit alles overweldigend voor u lijkt, maakt u zich dan geen zorgen, het [Support team]({{< ref path="contact" lang="nl" >}}) staat klaar om u te helpen eventuele hindernissen te nemen.
