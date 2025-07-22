{
  "hero": {
    "title": "Multi-step API-scripteditor"
  },
  "title": "Multi-step API-scripteditor",
  "summary": "Een overzicht van de scripteditor voor Multi-step API-controleregels",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Net als [transactiecontroleregels]([LINK_URL_1]) bevat het controleregeltype Multi-step API een scriptweergave-editor als een alternatief voor de standaard visuele editor. Met de scripteditor kunt u wijzigingen aanbrengen in de stappen van uw controleregel, net zoals met de visuele editor, maar in een JSON-script in plaats van in de gebruikersinterface. 

## Voordelen van de scripteditor

Het gebruik van een scripteditor heeft verschillende voordelen vergeleken met het aanbrengen van wijzigingen in de controleregel via de gebruikersinterface:

- Ervaren gebruikers vinden het misschien gemakkelijker om wijzigingen rechtstreeks in een script aan te brengen dan door een gebruikersinterface te navigeren. Sommige gebruikers geven de voorkeur aan een ervaring die lijkt op het gebruik van een command line. 
- Het beschikbaar hebben van een script maakt automatisering mogelijk, bijvoorbeeld om uw [CI/CD-proces]([LINK_URL_2]) te accomoderen. Met behulp van de [Uptrends API]([LINK_URL_3]) kunt u de stappen van de controleregel bijwerken op hetzelfde moment dat u de API bijwerkt die het controleert. 
- Met de scripteditor kunt u een lokale kopie van de stappen in uw controleregel maken door het script eenvoudigweg te kopiëren en in een lokaal bestand te plakken. Het bewaren van een lokale kopie maakt versiebeheer, back-ups van uw multi-step API-controleregels en eenvoudige replicatie van gecompliceerde set-ups mogelijk.

## Omschakelen naar de scripteditor

U kunt bij elke Multi-step API-controleregel omschakelen naar de scripteditor door naar de controleregelopties te gaan, naar het tabblad [SHORTCODE_1] Stappen [SHORTCODE_2] te gaan en rechtsboven te klikken op de knop [SHORTCODE_3] NAAR SCRIPT SCHAKELEN [SHORTCODE_4]. Omschakelen van en naar de scripteditor activeert validatie, dus zorg ervoor dat de JSON in de scriptweergave geldig blijft. Het script zal er als volgt uitzien:

![De scripteditor]([LINK_URL_4])

## Het script begrijpen

Zoals u kunt zien, is het script in wezen een JSON-geformatteerde reeks van afzonderlijke stappen, met hun request method, URL, alle headers en request body die u heeft geconfigureerd, en de authenticatie-opties. Bovendien bevat elke stap-entry de definities voor alle variabelen die zijn gemaakt van of assertions over de response. Alle noodzakelijke veranderingen kunnen direct in de scripteditor worden aangebracht.

Een individuele stap ziet er ongeveer zo uit:

[CODE_BLOCK_1]

Het toevoegen van extra stappen is net zo eenvoudig als het toevoegen van extra entries aan de array, met behulp van de volledige stapdefinitie zoals hierboven beschreven. 

Na de array met de stappen, bevat de stapdefinitie ook informatie over eventuele [voorgedefinieerde variabelen]([LINK_URL_5]) of [door de gebruiker gedefinieerde functies]([LINK_URL_6]) die u heeft ingesteld:

[CODE_BLOCK_2]