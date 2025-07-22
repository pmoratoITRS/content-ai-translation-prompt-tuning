{
  "hero": {
    "title": "Transactiescreenshots en watervallen gebruiken"
  },
  "title": "Transactiescreenshots en watervallen gebruiken",
  "summary": "Voor het grondig testen van uw transactiescripts en later voor het oplossen van problemen, moet u de watervalrapporten en screenshots bekijken om de bron van fouten en de status van uw transactiemonitoringscript te identificeren. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transactiescreenshots-watervallen-gebruiken",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends' [transactiecontroleregels]([LINK_URL_1]) bevatten verschillende opties voor analyse en debuggen. Twee van die tools zijn screenshots en watervalrapporten. De tools zijn een essentieel onderdeel van uw transactie monitoring-toolkit, zijn essentieel voor analyse van de hoofdoorzaak of performance. 

[SHORTCODE_1]
**Opmerking**: Screenshots en watervalrapporten zijn beschikbaar voor alle gebruikers bij gebruik van de knop [SHORTCODE_5] Test starten [SHORTCODE_6]. Echter, alleen **Enterprise-** en **Business**-accounts kunnen ze toevoegen voor gebruik in staging- en productionmodus.
[SHORTCODE_2]

## Watervalrapporten en screenshots inschakelen

1.   Navigeer naar de instellingen van de transactiecontroleregel waarvoor u watervallen/screenshots wilt inschakelen (bijvoorbeeld via [SHORTCODE_7] Monitoring > Controleregels beheren [SHORTCODE_8] in het zijbalkmenu).
2.   Selecteer op het tabblad [SHORTCODE_9]Stappen[SHORTCODE_10] de stap waarvoor u een waterval/screenshot wilt activeren.
3.   Schakel het betreffende selectievakje in om een waterval of screenshot voor die stap in te schakelen. 

  -  Merk op dat u ook halverwege de stappen screenshots kunt toevoegen door [ze als een actie toe te voegen]([LINK_URL_2]).

  - Om de [paginabron en console log-data]([LINK_URL_3]) te kunnen zien, moet de watervaloptie zijn ingeschakeld.
  
Houd er rekening mee dat elke waterval en screenshot die u toevoegt een [transactiecontroleregel credit]([LINK_URL_4]) kost.

[SHORTCODE_3]
**Opmerking**: U kunt uw transactiewatervallen configureren om [extra kengetallen weer te geven]([LINK_URL_5]) door **Chrome met extra kengetallen** als de browser te selecteren in het tabblad [SHORTCODE_11]Extra[SHORTCODE_12] van de controlergelinstellingen.
[SHORTCODE_4]


Uptrends genereert een waterval of screenshot in de volgende situaties:

-   **In geval van fouten:** Wanneer een bevestigde fout optreedt tijdens een transactie, wordt er een screenshot (maar **geen** waterval) gegenereerd. U hoeft niets in te stellen, dit gebeurt automatisch bij de eerste bevestigde fout.
-   **Elk resultaat van de controleregelcheck:** Wanneer u een waterval of screenshot in een specifieke stap heeft ingeschakeld, nadat de stap is voltooid.

## Uw watervalrapporten en screenshots vinden

Screenshots en watervallen zijn onmisbaar voor het oplossen van problemen en het debuggen van transactiefouten. U krijgt ze automatisch als u de knop [SHORTCODE_13] Test starten [SHORTCODE_14] gebruikt, en Enterprise- en Business-gebruikers krijgen een screenshot bij de eerste bevestigde fout.

### Waar zijn mijn screenshots en watervallen tijdens het debuggen?

U gebruikt de knop Test starten veel wanneer u uw transactie test in developmentmodus. Een belangrijke functie van de Test starten-resultaten zijn de watervalrapporten en screenshots. Voor toegang tot deze klikt u op de knop
 **Testresultaten beschikbaar** boven aan elke stap na het uitvoeren van een handmatige test.

![]([LINK_URL_6])

Nadat u op de knop **Testresultaten beschikbaar** heeft geklikt, scrollt u omlaag op de pagina naar **Debuginformatie**. Het rapport bevat automatisch de debugdetails tijdens handmatige tests.

Klik op de afbeelding om het screenshot of waterval te openen.

![Screenshot en waterval na test starten]([LINK_URL_7])

### Waar zijn mijn screenshots en watervalgrafieken in mijn rapporten?

Enterprise- en Business-gebruikers kunnen hun staging- en productionscreenshots vinden in hun Details van de controle-rapporten. Navigeer naar [SHORTCODE_15]Monitoring > Controleregel log [SHORTCODE_16] in het Uptrends-menu om uw controleregel log te bekijken.

**Screenshots**: U weet of een detail een screenshot heeft als u een camerapictogram in uw controleregel log ziet.

**Watervallen**: Als u watervalgrafieken aan uw transactiescripts heeft toegevoegd, zal elke controle de grafiek(en) bevatten. De Controleregel log toont geen indicator.

![]([LINK_URL_8]) 

Om de screenshot of watervalgrafieken te bekijken: 

1. Klik om het rapport Details van de controle te openen.
2. Zoek de sectie **Details van de controle**.
3. Klik op het camera- of watervalpictogram in uw stapresultaten.

![]([LINK_URL_9]) 

## Screenshots gebruiken voor debuggen

Uw test genereert een screenshot zodat u het resultaat van een stap op het scherm kunt zien. Het screenshot toont hoe de viewport eruitzag na een succesvolle stap of paginafout. Als de actie verderop op de pagina plaatsvindt, kunt u een scrollactie toevoegen vóór de klikgebeurtenis.

Bestudeer het screenshot om te verifiëren of:

-   **Verwachte inhoud is geladen.** Controleer na een paginanavigatie of de inhoud correct is.
-   **Dynamische inhoud als gevolg van gebruikersinvoer** goed werkt. Bijvoorbeeld als de gebruiker bij het selecteren van een item een kleur moet selecteren voordat de maatopties beschikbaar komen om te controleren of het element correct is ingevuld.
-   **Gemaskeerde velden werken zoals verwacht**. Is het teken correct opgemaakt?
-   **Responsive design verandert**. Als uw site responsive design gebruikt, moet u mogelijk de browserresolutie aanpassen in uw controleregelinstellingen. Door uw browserresolutie aan te passen, kunt u ervoor zorgen dat u de juiste paginalay-out krijgt. Als uw menu bijvoorbeeld verkleint tot een hamburgerpictogram wanneer het browservenster kleiner wordt, moet u mogelijk extra klik- of hoveracties toevoegen. Controleer op het tabblad [SHORTCODE_17]Extra[SHORTCODE_18] van de controleregel of u uw browserresolutie moet aanpassen.

## Watervalgrafieken gebruiken voor debuggen

Het watervalrapport geeft u gedetailleerde informatie over de laadtijd van de eerste pagina. U ziet precies hoe lang het duurde om elk pagina-element op te halen en te verwerken, samen met de request- en responsheaders. Met uw waterval kunt u snel problemen op de pagina identificeren. Bekijk ons artikel over de [watervalgrafiek]([LINK_URL_10]) waar dieper wordt ingegaan op wat er wordt weergegeven in de watervalgrafiek en hoe deze kan worden gebruikt voor debuggen. 

![]([LINK_URL_11])


