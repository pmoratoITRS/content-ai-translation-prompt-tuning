{
  "hero": {
    "title": "Controleregelmodus"
  },
  "title": "Controleregelmodus",
  "summary": "Uptrends biedt drie nieuwe monitoringmodi: development, staging en production.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/controleregelmodus",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u een nieuwe controleregel creëert, wilt u meestal dat die meteen actief wordt in uw account. Zodra de controleregel actief is, begint hij elke minuut metingen te produceren (afhankelijk van het monitoringinterval). U kunt die metingen inspecteren in de controleregel log en Uptrends genereert alerts wanneer er fouten optreden. In veel gevallen werkt het onmiddellijk activeren van uw controleregel erg goed. Deze directheid is echter niet altijd optimaal. 

## In productionmodus draaien of niet

Wanneer u bijvoorbeeld een nieuwe transactie aan het bouwen bent, werkt u waarschijnlijk enige tijd aan de transactie voordat u die in productionmodus wilt draaien. In de tussentijd wilt u de transactie misschien een tijdje laten draaien om te zien hoe stabiel hij is zonder het risico te lopen fout-positieve uitkomsten te genereren (foutmeldingen). Fout-positieve uitkomsten hebben een ongewenst effect op uw SLA's en andere account-brede uptimecijfers.

Hetzelfde geldt als u een bestaande transactie hebt die moet worden vervangen door een bijgewerkt script zodra u uw vernieuwde website lanceert. U wilt dan die nieuwe transactie voorbereiden en gereed hebben voor gebruik. Echter, zolang het nieuwe transactiescript daar staat maar inactief is, gebruikt de controleregel waardevolle transactiecredits die meetellen voor uw totaal beschikbare aantal. U kunt extra credits kopen, maar er is een efficiëntere manier om uw controleregels te organiseren.

## Levenscycli van controleregels beheren met controleregelmodus

We hebben drie verschillende controleregelmodi: **development**, **staging** en **production**. U kunt schakelen tussen deze modi bij alle controleregeltypen (niet alleen transacties) als u de Professional-, Business- of Enterprise-versie gebruikt. In andere versies is de controleregelmodus altijd production.

Maar wanneer komen de verschillende controleregelmodi van pas?

### Developmentmodus

Controleregels in developmentmodus zijn altijd inactief. U kunt een controleregel in developmentmodus niet automatisch laten uitvoeren, dus de controleregel genereert geen resultaten in de controleregel log. Dit betekent ook dat ze gratis zijn! U kunt er zoveel hebben als u wilt, zonder extra kosten. Dit betekent wel dat alle historische data die aan die controleregel zijn gekoppeld, verdwijnen zodra u een controleregel terugschakelt naar developmentmodus.

Controleregels in developmentmodus zijn handig voor het maken en testen van ontwerpversies. Stel dat u een nieuwe transactie- of Multi-step API-controleregel aan het maken bent en hierop handmatige testen uitvoert in de editor. Op basis van de testresultaten kunt u hem verder aanpassen tot u tevreden bent met die eerste testresultaten. Totdat u klaar bent om een controleregel naar staging of production te verplaatsen, kost het u niets en heeft de controleregel geen negatieve invloed op uw uptimecijfers.

Daarom kunt u in developmentmodus ook meerdere (inactieve) exemplaren hebben liggen zonder dat u extra controleregels, transactiestappen of API-stappen hoeft te kopen. Het is prima om controleregels lange tijd in developmentmodus te houden. Maar als u klaar bent om een inactieve controleregel in developmentmodus te promoveren naar staging of production, hebt u ruimte in uw account nodig om hem te activeren of om te wisselen met een andere controleregel.

### Stagingmodus

Stagingmodus is meestal de volgende stap in de levenscyclus van een nieuwe controleregel. In tegenstelling tot developmentmodus kunt u in stagingmodus een controleregel inplannen voor normale uitvoering. Eenmaal geactiveerd, produceert de controleregel nieuwe metingen zoals elke andere controleregel en zijn de resultaten zoals gewoonlijk zichtbaar in de controleregel log. Het aardige van het gebruik van stagingmodus is dat, hoewel u kunt zien hoe stabiel de monitoringresultaten zijn, deze geen invloed heeft op het uptimepercentage van uw account, geen gevolgen heeft voor uw SLA's en Uptrends geen alerts verstuurt. Het is alsof u uw controleregels in een sandboxomgeving uitvoert; de metingen zijn echt, maar de uptime, SLA's, historische statistieken en alertingpijplijn blijven schoon ([lees meer]([LINK_URL_1])).

Zodra u een controleregel naar stagingmodus verplaatst, telt deze mee voor het totale aantal controleregels/ credits in uw account. Meestal wilt u een controleregel in stagingmodus proberen te promoveren naar production zodra u zeker weet dat de controleregel stabiel is. Anders profiteert u niet van het volledige scala aan functies, terwijl de kosten hetzelfde zijn als bij een controleregel in productionmodus.

### Productionmodus [ANCHOR_1]

Production is de standaardmodus. In productionmodus is een controleregel beschikbaar voor reguliere uitvoering, de beschikbaarheid van de controleregel telt mee voor de algehele uptime van de account, de controleregelresultaten worden meegeteld bij SLA-berekeningen en alerting is beschikbaar.
