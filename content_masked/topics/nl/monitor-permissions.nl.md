{
  "hero": {
    "title": "Gebruikersrechten voor controleregels"
  },
  "title": "Gebruikersrechten voor controleregels",
  "summary": "Een overzicht van hoe u gebruikersrechten voor controleregels instelt voor uw operators of operatorgroepen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/gebruikersrechten-voor-controleregels",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]Gebruikersrechten voor controleregels zijn alleen beschikbaar voor accounts op **Enterprise-niveau**.[SHORTCODE_2]

Standaard kunnen alle [standaard operators]([LINK_URL_1]) in uw account gegevens van controleregels bekijken (dashboards, statistieken, controleresultaten) van al uw controleregels. Ze kunnen echter geen bestaande controleregels bewerken of verwijderen, of nieuwe maken. Deze acties zijn standaard alleen beschikbaar voor [Administrators]([LINK_URL_2]) (operators die zijn lid van de operatorgroep *Administrators*). 

Voor meer verfijnde controle over welke operators bepaalde dingen in uw account mogen bekijken of doen, kunnen gebruikers op Enterprise-niveau **gebruikersrechten voor controleregels** instellen. Kort gezegd: een gebruikersrecht is een regel die van toepassing is op een specifieke controleregel of controleregelgroep die het toegangsniveau bepaalt dat een specifieke operator of operatorgroep heeft voor die controleregels. 

Dit is alleen van toepassing op controleregels in uw account. Meer informatie over **gebruikersrechten**, zoals de mogelijkheid om bestellingen te plaatsen, facturen te bekijken, toegang te krijgen tot uw Uptrends Infra-abonnement, enz. vindt u in ons artikel over [gebruikersrechten]([LINK_URL_3]). 

## Gebruikersrechten voor controleregels instellen

Gebruikersrechten kunnen worden ingesteld op [controleregelgroepen]([LINK_URL_4]) of individuele controleregels. Dit kan worden gedaan in de controleregel(groep)-instellingen, maar u kunt controleregelrechten ook direct toewijzen in de instellingen voor [operatorgroepen]([LINK_URL_5]).

#### Gebruikersrechten instellen via operatorgroepinstellingen:

1. Navigeer naar het overzicht [Operatorgroepen]([LINK_URL_6]) (ofwel door op de link te klikken, ofwel via het menu bij *Accountinstellingen > Operators, groepen en deelaccounts*) en selecteer de operatorgroep waaraan u rechten voor controleregels wilt toekennen.
2. U vindt de instelling **Rechten voor controleregels** in het tabblad [SHORTCODE_3] Gebruikersrechten [SHORTCODE_4]. 
3. Voeg zo nodig de controleregelgroep of individuele controleregel toe waarvoor u een gebruikersrecht wilt toekennen.
4. Zet het gebruikersrecht op het juiste niveau met de schuifregelaar (hieronder vindt u een overzicht van beschikbare rechtenniveaus).
![Rechten voor controleregels via operatorgroep]([LINK_URL_7])
5. Vergeet niet op [SHORTCODE_5] Opslaan [SHORTCODE_6] linksonder in het scherm te klikken!

In het bovenstaande voorbeeld kunnen leden van deze operatorgroep controleregels toevoegen aan en verwijderen uit *Controleregelgroep A*, controleregeldata bekijken voor *Alle controleregels* in het account en de instellingen wijzigen van een individuele controleregel genaamd *Example SSL Cert monitor*.

#### Gebruikersrechten instellen via controleregel(groep)instellingen:

1. Navigeer naar de [controleregelgroep]([LINK_URL_8]) of controleregel waarvoor u een gebruikersrecht wilt instellen.
2. Open het tabblad [SHORTCODE_7] Gebruikersrechten [SHORTCODE_8] voor een overzicht van de rechten die momenteel voor die groep of controleregel zijn ingesteld. De operatorgroep *Administrators* heeft altijd het recht **Maken en verwijderen van controleregels in groep**, dat niet kan worden verwijderd. Standaard heeft de operatorgroep *Iedereen* het recht **Gegevens van controleregels in groep bekijken**.
3. Om een bestaand recht te verwijderen klikt u op de betreffende knop aan de rechterkant. Ga dan verder met stap 7. 
4. Om een nieuw recht te creëren klikt u op **Recht toevoegen** in de rechter bovenhoek. Om een bestaand recht te bewerken klikt u op de knop **Bewerken** ernaast. 
5. Selecteer het recht dat u wilt toewijzen. Hieronder vindt u een overzicht van de beschikbare typen rechten. Als u een nieuw recht creëert, selecteert u de individuele operator of operatorgroep waaraan u het recht wilt geven. 
6. Klik op **Toevoegen** of **Bewerken**, afhankelijk van of u een nieuw recht toevoegt of een bestaand recht bewerkt.
7. Vergeet niet op [SHORTCODE_9] Opslaan [SHORTCODE_10] linksonder in het scherm te klikken!

### Controleregelrechten en de groep 'Alle controleregels'

Wanneer er een nieuwe controleregel wordt gemaakt, wordt deze automatisch toegevoegd aan de groep *Alle controleregels* (aangezien die groep per definitie alle controleregels in het account moet bevatten). Standaard hebben gewone (niet-Administrator) operators echter niet de benodigde rechten om controleregels te maken/verwijderen in de groep *Alle controleregels*. Dat zou betekenen dat een operator zonder het expliciete gebruikersrecht om controleregels te maken in de groep *Alle controleregels* nooit iets zou kunnen maken. Om dit te ondervangen wordt het lidmaatschap van de groep *Alle controleregels* genegeerd bij het maken van een nieuwe controleregel, zolang de controleregel aan ten minste één andere groep wordt toegevoegd. 

Neem bijvoorbeeld een operator zonder gebruikersrechten voor de groep *Alle controleregels* en met een gebruikersrecht maken/verwijderen voor *Controleregelgroep A*. Deze operator kan de bestaande controleregels in groep A bekijken en bewerken, en nieuwe controleregels maken die lid zijn van deze groep. Deze operator kan geen bestaande controleregels bekijken of bewerken buiten *Controleregelgroep A*. 

Wanneer deze operator een nieuwe controleregel maakt, moet die worden toegevoegd aan ten minste één van de controleregelgroepen waarvoor hij de benodigde gebruikersrechten heeft. 

![De groep Alle controleregels]([LINK_URL_9])

De controleregel zal worden aangemaakt als lid van zowel *Controleregelgroep A* als *Alle controleregels*, zonder dat voor de laatste een expliciet gebruikersrecht voor maken/verwijderen nodig is.

## Typen gebruikersrechten [ANCHOR_1]

De volgende typen gebruikersrechten zijn beschikbaar:

- **Gegevens van controleregels in groep bekijken**: Operators die dit recht hebben, kunnen alleen controleregelgegevens bekijken voor de controleregel(groep) waarop ze van toepassing zijn. Controleregelgegevens omvatten dashboards, statistieken en controleresultaten. Het omvat **geen** controleregelinstellingen.
- **Controleregelinstellingen in groep bekijken**: Dit recht heeft betrekking op controleregelgegevens, maar omvat ook controleregelinstellingen. Operators met dit recht kunnen controleregelinstellingen bekijken voor de controleregel(groep) waarop deze van toepassing is, zoals monitoringinterval, -modus, controlestationselectie, onderhoudsperiodes, enz. Let wel, met dit recht zijn deze instellingen **alleen-lezen**, en mogen niet worden bewerkt.
- **Controleregelinstellingen in groep bewerken**: Operators met dit recht kunnen wijzigingen aanbrengen in de individuele controleregel(s), of controleregels in de controleregelgroep waarvoor dit recht is ingesteld. Ook kunnen zij de controleregel in- of uitschakelen, het interval wijzigen, de selectie van controlestations bewerken, onderhoudsperiodes toevoegen, enz. 
- **Maken en verwijderen van controleregels in groep**: Als het hoogste recht dat kan worden toegewezen, geeft dit een operator in feite administratorrechten voor specifieke controleregelgroepen. Ze kunnen nieuwe controleregels creëren (zij het alleen als leden van aan hen toegewezen controleregelgroep) of bestaande controleregels verwijderen. Dit recht is alleen beschikbaar voor controleregelgroepen en kan niet worden toegewezen aan individuele controleregels. 

Opgemerkt dient te worden dat deze rechten cumulatief zijn. Elk volgend rechtenniveau bevat alle rechten ervoor. Een operator met het recht *Controleregelinstellingen in groep bekijken* kan bijvoorbeeld automatisch ook de controleregelgegevens bekijken. 

![Voorbeeld rechten]([LINK_URL_10])

In de bovenstaande afbeelding (die van toepassing is op de *Voorbeeld controleregelgroep*) kan de operatorgroep *Iedereen* alleen controleregelgegevens bekijken, dat wil zeggen dashboards, statistieken en individuele controleresultaten. Operatorgroep *Voorbeeld operatorgroep* kan controleregelgegevens bekijken en instellingen bewerken voor bestaande controleregels binnen deze groep. De groep *Administrators* heeft volledige CRUD-rechten (Create, Update, Delete) voor de controleregels in de *Voorbeeld controleregelgroep*. 

## Standaard controleregelgroep [ANCHOR_2]

Elke controleregel in uw account is per definitie lid van de  [controleregelgroep]([LINK_URL_11]) **Alle controleregels**. Controleregels kunnen niet uit deze groep worden verwijderd. Dat is in veel gevallen handig, maar mogelijk niet ideaal voor het toewijzen van gebruikersrechten, afhankelijk van uw vereisten. 

Alle gebruikersrechten die u toewijst aan de groep Alle controleregels zijn van toepassing op alle controleregels in uw account. Echter, misschien wilt u een bepaald recht toepassen op *alle behalve enkele* controleregels in uw account. Als een bepaalde [operatorgroep]([LINK_URL_12]) bijvoorbeeld de instellingen van alle controleregels in uw account moet kunnen bewerken, behalve enkele specifieke, zou het toewijzen van het recht 'Controleregelinstellingen bewerken' aan de groep Alle controleregels niet werken (aangezien ze de mogelijkheid zouden hebben om alle controleregels te bewerken, inclusief de controleregels die ze niet zouden moeten kunnen bewerken). 

Om u hierbij te helpen kunt u een **Standaard controleregelgroep** instellen. Dit is een aangepaste controleregelgroep, vergelijkbaar met de groep Alle controleregels, behalve dat controleregels kunnen worden verwijderd als leden van deze groep. Nadat een standaard controleregelgroep is ingesteld, wordt elke nieuw gecreëerde controleregel automatisch ook lid van deze groep (naast de groep Alle controleregels) en krijgt deze dus dezelfde rechten zonder dat verdere handmatige tussenkomst nodig is. 

Alle gebruikersrechten die u wilt toewijzen aan alle behalve enkele controleregels in uw account, kunnen worden toegewezen aan de Standaard controleregelgroep in plaats van aan de groep Alle controleregels. 

Een standaard controleregelgroep instellen:

1. Gebruik een bestaande controleregelgroep of creëer een nieuwe groep.
2. Zorg ervoor dat deze controleregelgroep alle controleregels bevat waarop u het gewenste gebruikersrecht wilt toepassen. Onze [MonitorGroup API]([LINK_URL_13]) kan handig zijn om controleregels in bulk aan deze groep toe te voegen. 
3. Navigeer naar uw accountinstellingen door in het menu naar [SHORTCODE_11] Accountinstellingen > Accountinstellingen [SHORTCODE_12] te gaan.
4. Selecteer de controleregelgroep in de keuzelijst bij de optie **Standaard controleregelgroep**.
![Instelling Standaard controleregelgroep]([LINK_URL_14])
5. Klik op [SHORTCODE_13] OPSLAAN [SHORTCODE_14] om uw instellingen op te slaan.

