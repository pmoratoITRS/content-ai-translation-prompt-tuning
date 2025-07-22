{
  "hero": {
    "title": "Transactiescreenshots en watervallen gebruiken"
  },
  "title": "Transactiescreenshots en watervallen gebruiken",
  "summary": "Voor het grondig testen van uw transactiescripts en later voor het oplossen van problemen, moet u de watervalrapporten en screenshots bekijken om de bron van fouten en de status van uw transactiemonitoringscript te identificeren. ",
  "url": "/support/kb/synthetic-monitoring/transacties/transactiescreenshots-watervallen-gebruiken",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-transaction-screenshots-waterfalls"
}

Uptrends' [transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions/" lang="nl" >}}) bevatten verschillende opties voor analyse en debuggen. Twee van die tools zijn screenshots en watervalrapporten. De tools zijn een essentieel onderdeel van uw transactie monitoring-toolkit, zijn essentieel voor analyse van de hoofdoorzaak of performance. 

{{< callout >}}
**Opmerking**: Screenshots en watervalrapporten zijn beschikbaar voor alle gebruikers bij gebruik van de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}}. Echter, alleen **Enterprise-** en **Business**-accounts kunnen ze toevoegen voor gebruik in staging- en productionmodus.
{{< /callout >}}

## Watervalrapporten en screenshots inschakelen

1.   Navigeer naar de instellingen van de transactiecontroleregel waarvoor u watervallen/screenshots wilt inschakelen (bijvoorbeeld via {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}} in het zijbalkmenu).
2.   Selecteer op het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}} de stap waarvoor u een waterval/screenshot wilt activeren.
3.   Schakel het betreffende selectievakje in om een waterval of screenshot voor die stap in te schakelen. 

  -  Merk op dat u ook halverwege de stappen screenshots kunt toevoegen door [ze als een actie toe te voegen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-an-action" lang="en" >}}).

  - Om de [paginabron en console log-data]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="nl" >}}) te kunnen zien, moet de watervaloptie zijn ingeschakeld.
  
Houd er rekening mee dat elke waterval en screenshot die u toevoegt een [transactiecontroleregel credit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) kost.

{{< callout >}}
**Opmerking**: U kunt uw transactiewatervallen configureren om [extra kengetallen weer te geven]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#metrics" lang="nl" >}}) door **Chrome met extra kengetallen** als de browser te selecteren in het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}} van de controlergelinstellingen.
{{< /callout >}}


Uptrends genereert een waterval of screenshot in de volgende situaties:

-   **In geval van fouten:** Wanneer een bevestigde fout optreedt tijdens een transactie, wordt er een screenshot (maar **geen** waterval) gegenereerd. U hoeft niets in te stellen, dit gebeurt automatisch bij de eerste bevestigde fout.
-   **Elk resultaat van de controleregelcheck:** Wanneer u een waterval of screenshot in een specifieke stap heeft ingeschakeld, nadat de stap is voltooid.

## Uw watervalrapporten en screenshots vinden

Screenshots en watervallen zijn onmisbaar voor het oplossen van problemen en het debuggen van transactiefouten. U krijgt ze automatisch als u de knop {{< AppElement type="buttonSecondary" >}} Test starten {{< /AppElement >}} gebruikt, en Enterprise- en Business-gebruikers krijgen een screenshot bij de eerste bevestigde fout.

### Waar zijn mijn screenshots en watervallen tijdens het debuggen?

U gebruikt de knop Test starten veel wanneer u uw transactie test in developmentmodus. Een belangrijke functie van de Test starten-resultaten zijn de watervalrapporten en screenshots. Voor toegang tot deze klikt u op de knop
 **Testresultaten beschikbaar** boven aan elke stap na het uitvoeren van een handmatige test.

![](/img/content/5e8923ca-fa6e-44ad-a8ef-02c744d36adb.png)

Nadat u op de knop **Testresultaten beschikbaar** heeft geklikt, scrollt u omlaag op de pagina naar **Debuginformatie**. Het rapport bevat automatisch de debugdetails tijdens handmatige tests.

Klik op de afbeelding om het screenshot of waterval te openen.

![Screenshot en waterval na test starten](/img/content/scr-waterfall-screenshot-after-test-now.min.png)

### Waar zijn mijn screenshots en watervalgrafieken in mijn rapporten?

Enterprise- en Business-gebruikers kunnen hun staging- en productionscreenshots vinden in hun Details van de controle-rapporten. Navigeer naar {{< AppElement type="menuitem" >}}Monitoring > Controleregel log {{< /AppElement >}} in het Uptrends-menu om uw controleregel log te bekijken.

**Screenshots**: U weet of een detail een screenshot heeft als u een camerapictogram in uw controleregel log ziet.

**Watervallen**: Als u watervalgrafieken aan uw transactiescripts heeft toegevoegd, zal elke controle de grafiek(en) bevatten. De Controleregel log toont geen indicator.

![](/img/content/f7f72770-69e4-4f8b-8b34-ed7c6a09848b.png) 

Om de screenshot of watervalgrafieken te bekijken: 

1. Klik om het rapport Details van de controle te openen.
2. Zoek de sectie **Details van de controle**.
3. Klik op het camera- of watervalpictogram in uw stapresultaten.

![](/img/content/70d49d55-56e4-4989-9259-1bea703b0bb3.png) 

## Screenshots gebruiken voor debuggen

Uw test genereert een screenshot zodat u het resultaat van een stap op het scherm kunt zien. Het screenshot toont hoe de viewport eruitzag na een succesvolle stap of paginafout. Als de actie verderop op de pagina plaatsvindt, kunt u een scrollactie toevoegen vóór de klikgebeurtenis.

Bestudeer het screenshot om te verifiëren of:

-   **Verwachte inhoud is geladen.** Controleer na een paginanavigatie of de inhoud correct is.
-   **Dynamische inhoud als gevolg van gebruikersinvoer** goed werkt. Bijvoorbeeld als de gebruiker bij het selecteren van een item een kleur moet selecteren voordat de maatopties beschikbaar komen om te controleren of het element correct is ingevuld.
-   **Gemaskeerde velden werken zoals verwacht**. Is het teken correct opgemaakt?
-   **Responsive design verandert**. Als uw site responsive design gebruikt, moet u mogelijk de browserresolutie aanpassen in uw controleregelinstellingen. Door uw browserresolutie aan te passen, kunt u ervoor zorgen dat u de juiste paginalay-out krijgt. Als uw menu bijvoorbeeld verkleint tot een hamburgerpictogram wanneer het browservenster kleiner wordt, moet u mogelijk extra klik- of hoveracties toevoegen. Controleer op het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}} van de controleregel of u uw browserresolutie moet aanpassen.

## Watervalgrafieken gebruiken voor debuggen

Het watervalrapport geeft u gedetailleerde informatie over de laadtijd van de eerste pagina. U ziet precies hoe lang het duurde om elk pagina-element op te halen en te verwerken, samen met de request- en responsheaders. Met uw waterval kunt u snel problemen op de pagina identificeren. Bekijk ons artikel over de [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart#what-is-presented-in-the-waterfall-chart" lang="nl" >}}) waar dieper wordt ingegaan op wat er wordt weergegeven in de watervalgrafiek en hoe deze kan worden gebruikt voor debuggen. 

![](/img/content/d4dee11f-d9f9-464c-a988-4d0c4254100b.png)


