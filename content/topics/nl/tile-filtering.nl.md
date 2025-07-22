{
  "hero": {
    "title": "Dashboards en tegels filteren"
  },
  "title": "Dashboards en tegels filteren",
  "summary": "Toon uw monitoringdata met alleen geselecteerde data door filters op een dashboard of in afzonderlijke tegels te gebruiken.",
  "url": "/support/kb/dashboards-en-rapportages/dashboards/tegels-filteren",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/tile-filtering"
}

Er zijn twee verschillende manieren waarop u uw dashboarddata kunt filteren: op individuele tegel (waardoor u twee soortgelijke tegels naast elkaar kunt zien, maar met verschillende instellingen), of door een filter op het hele dashboard toe te passen.

## Dashboard filteren

Om een filter op het hele dashboard toe te passen opent u het betreffende  dashboard en gebruikt u de filteropties in het Actiemenu (in de rechterbovenhoek van het dashboard).  

![screenshot dashboardfilters](/img/content/scr_dashboard-filters.min.png)


U ziet verschillende filteropties die veranderen op basis van het dashboard waarop u zich bevindt, waaronder:

- **Controleregel filteren**  
  Dit filter is handig als u alleen data voor een bepaalde controleregels wilt zien. U kunt één of meer controleregel(s) of [controleregelgroep(en)]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="nl" >}}) selecteren.
- **Foutniveau filteren**  
  Met dit filter kunt u alles weergeven, alleen [onbevestigde/bevestigde fouten]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="nl" >}}), alleen bevestigde fouten of alleen succesvolle metingen (OK-resultaten).
- **Deelmetingen filteren**  
  Een filter voor alleen [gelijktijdige monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="nl" >}}) waarmee u deelmetingen kunt weergeven of verbergen. 
- **Controlestation filteren**  
  Toont data-uitvoer gefilterd op bepaalde [controlestations]({{< ref path="#checkpoint-filtering" lang="nl" >}}).
- **Datum/tijd filteren**  
  Filter op een bepaald tijdsbestek. 

## Tegel filteren

Filteren binnen een afzonderlijke tegel::

1. Open het dashboard dat de tegel bevat die u wilt filteren.
2. Open op de betreffende tegel het menu met drie stippen {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} om toegang te krijgen tot de tegelinstellingen.
   Er verschijnt een pop-upvenster met een reeks tabbladen en configuratieopties die betrekking hebben op de tegel.
  
    ![screenshot tegelinstellingen](/img/content/scr_tile-settings.min.png)

   Welke tabbladen en opties beschikbaar zijn, hangt af van het [tegeltype]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="nl" >}}). Deze kunnen zijn (een combinatie van):

   **Tegel**  
   De opties op het tabblad {{< AppElement type="tab" >}}Tegel{{< /AppElement >}} hebben alleen betrekking op de manier waarop data in die tegel worden gepresenteerd.

   **Groepen en controleregels**  
   Op het tabblad {{< AppElement type="tab" >}}Groepen en controleregels{{< /AppElement >}} kunt u data weergeven die betrekking hebben op de context van het dashboard (meestal de standaardinstelling) of deze filteren om data weer te geven voor elke reeks controleregels of controleregelgroepen. 

   **Controlestations**  
    Filter data op het controlestation(s) dat de monitoringchecks heeft uitgevoerd. Zie de onderstaande stappen voor [Controlestation filteren]({{< ref path="#checkpoint-filtering-tiles" lang="nl" >}}) voor meer informatie.

   **Periode**  
   Op het tabblad {{< AppElement type="tab" >}}Periode{{< /AppElement >}} kunt u het tijdsbestek filteren waarin data moeten worden weergegeven, dit is doorgaans standaard ingesteld op de context van het dashboard.  
3. Stel alle filters in die u op de tegel wilt toepassen.
4. Klik in het dialoogvenster met tegelinstellingen op de knop {{< AppElement type="button" >}} Instellen {{< /AppElement >}}.
5. Belangrijk: uw wijzigingen worden niet automatisch opgeslagen. Telkens wanneer u wijzigingen aanbrengt in afzonderlijke tegels (of in het dashboard), moet u deze opslaan met de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} rechtsboven in uw dashboard.



{{< callout >}} **Opmerking**: In het Knowledge Base-artikel [Een aangepaste tegel toevoegen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="nl" >}}) wordt uitgelegd hoe u afzonderlijke tegels aan dashboards toevoegt. {{< /callout >}}  

## Controlestation filteren voor tegels {id="checkpoint-filtering-tiles"}

Controlestationfilters zijn beschikbaar voor de [tegeltypes]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="nl" >}}):
- Eenvoudige lijst/grafiek
- Controlestation lijst/grafiek
- Multicontrolestation lijst/grafiek
- Tijdsduurcontrole lijst/grafiek
- Controleregel log

Een controlestationfilter op een tegel toepassen:

1. Ga naar het menu {{< AppElement type="menuitem" >}} Dashboards {{< /AppElement >}}. 
2. Selecteer een dashboard. 
3. Open van een tegel het menu met drie stippen {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} om toegang te krijgen tot de instellingen. 
4. Ga naar het tabblad {{< AppElement type="tab" >}} Controlestations {{< /AppElement >}}. 

   ![screenshot controlestationselectie van een tegel](/img/content/scr-cp-selection-tiles.min.png) 

5. Selecteer het controlestation(s) waarvan u checkdata in de tegel wilt weergeven.  
   U kunt individuele controlestations selecteren, controlestationregio's of landen (binnen regio's).
6. Klik op de knop {{< AppElement type="button" >}} Instellen {{< /AppElement >}}.
7. Klik op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} rechtsboven in uw dashboard.

**Opmerking:** Voor controlestationfilters gelden twee uitzonderingen: 
- Extra kengetallen met label 'Alleen FPC's & transacties'. Wanneer een van deze is geselecteerd op het tabblad {{< AppElement type="tab" >}}Tegel{{< /AppElement >}} samen met een controlestationfilter, zal Uptrends een waarschuwing weergeven. 
- Wanneer **Tijdgroepering** {{< AppElement type="dropdown" >}} De uren van de dag tonen{{< /AppElement >}} is geselecteerd op tabblad {{< AppElement type="tab" >}} Periode {{< /AppElement >}} en er een controlestationfilter actief is, wordt er een waarschuwing weergegeven.
   ![](/img/content/scr-cp-tile-time-grouping.min.png) 