{
  "hero": {
    "title": "Dashboards en tegels filteren"
  },
  "title": "Dashboards en tegels filteren",
  "summary": "Toon uw monitoringdata met alleen geselecteerde data door filters op een dashboard of in afzonderlijke tegels te gebruiken.",
  "url": "[URL_BASE_TOPICS]dashboards-en-rapportages/dashboards/tegels-filteren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Er zijn twee verschillende manieren waarop u uw dashboarddata kunt filteren: op individuele tegel (waardoor u twee soortgelijke tegels naast elkaar kunt zien, maar met verschillende instellingen), of door een filter op het hele dashboard toe te passen.

## Dashboard filteren

Om een filter op het hele dashboard toe te passen opent u het betreffende  dashboard en gebruikt u de filteropties in het Actiemenu (in de rechterbovenhoek van het dashboard).  

![screenshot dashboardfilters]([LINK_URL_1])


U ziet verschillende filteropties die veranderen op basis van het dashboard waarop u zich bevindt, waaronder:

- **Controleregel filteren**  
  Dit filter is handig als u alleen data voor een bepaalde controleregels wilt zien. U kunt één of meer controleregel(s) of [controleregelgroep(en)]([LINK_URL_2]) selecteren.
- **Foutniveau filteren**  
  Met dit filter kunt u alles weergeven, alleen [onbevestigde/bevestigde fouten]([LINK_URL_3]), alleen bevestigde fouten of alleen succesvolle metingen (OK-resultaten).
- **Deelmetingen filteren**  
  Een filter voor alleen [gelijktijdige monitoring]([LINK_URL_4]) waarmee u deelmetingen kunt weergeven of verbergen. 
- **Controlestation filteren**  
  Toont data-uitvoer gefilterd op bepaalde [controlestations]([LINK_URL_5]).
- **Datum/tijd filteren**  
  Filter op een bepaald tijdsbestek. 

## Tegel filteren

Filteren binnen een afzonderlijke tegel::

1. Open het dashboard dat de tegel bevat die u wilt filteren.
2. Open op de betreffende tegel het menu met drie stippen [SHORTCODE_3][SHORTCODE_4] om toegang te krijgen tot de tegelinstellingen.
   Er verschijnt een pop-upvenster met een reeks tabbladen en configuratieopties die betrekking hebben op de tegel.
  
    ![screenshot tegelinstellingen]([LINK_URL_6])

   Welke tabbladen en opties beschikbaar zijn, hangt af van het [tegeltype]([LINK_URL_7]). Deze kunnen zijn (een combinatie van):

   **Tegel**  
   De opties op het tabblad [SHORTCODE_5]Tegel[SHORTCODE_6] hebben alleen betrekking op de manier waarop data in die tegel worden gepresenteerd.

   **Groepen en controleregels**  
   Op het tabblad [SHORTCODE_7]Groepen en controleregels[SHORTCODE_8] kunt u data weergeven die betrekking hebben op de context van het dashboard (meestal de standaardinstelling) of deze filteren om data weer te geven voor elke reeks controleregels of controleregelgroepen. 

   **Controlestations**  
    Filter data op het controlestation(s) dat de monitoringchecks heeft uitgevoerd. Zie de onderstaande stappen voor [Controlestation filteren]([LINK_URL_8]) voor meer informatie.

   **Periode**  
   Op het tabblad [SHORTCODE_9]Periode[SHORTCODE_10] kunt u het tijdsbestek filteren waarin data moeten worden weergegeven, dit is doorgaans standaard ingesteld op de context van het dashboard.  
3. Stel alle filters in die u op de tegel wilt toepassen.
4. Klik in het dialoogvenster met tegelinstellingen op de knop [SHORTCODE_11] Instellen [SHORTCODE_12].
5. Belangrijk: uw wijzigingen worden niet automatisch opgeslagen. Telkens wanneer u wijzigingen aanbrengt in afzonderlijke tegels (of in het dashboard), moet u deze opslaan met de knop [SHORTCODE_13]Opslaan[SHORTCODE_14] rechtsboven in uw dashboard.



[SHORTCODE_1] **Opmerking**: In het Knowledge Base-artikel [Een aangepaste tegel toevoegen]([LINK_URL_9]) wordt uitgelegd hoe u afzonderlijke tegels aan dashboards toevoegt. [SHORTCODE_2]  

## Controlestation filteren voor tegels [ANCHOR_1]

Controlestationfilters zijn beschikbaar voor de [tegeltypes]([LINK_URL_10]):
- Eenvoudige lijst/grafiek
- Controlestation lijst/grafiek
- Multicontrolestation lijst/grafiek
- Tijdsduurcontrole lijst/grafiek
- Controleregel log

Een controlestationfilter op een tegel toepassen:

1. Ga naar het menu [SHORTCODE_15] Dashboards [SHORTCODE_16]. 
2. Selecteer een dashboard. 
3. Open van een tegel het menu met drie stippen [SHORTCODE_17] [SHORTCODE_18] om toegang te krijgen tot de instellingen. 
4. Ga naar het tabblad [SHORTCODE_19] Controlestations [SHORTCODE_20]. 

   ![screenshot controlestationselectie van een tegel]([LINK_URL_11]) 

5. Selecteer het controlestation(s) waarvan u checkdata in de tegel wilt weergeven.  
   U kunt individuele controlestations selecteren, controlestationregio's of landen (binnen regio's).
6. Klik op de knop [SHORTCODE_21] Instellen [SHORTCODE_22].
7. Klik op de knop [SHORTCODE_23]Opslaan[SHORTCODE_24] rechtsboven in uw dashboard.

**Opmerking:** Voor controlestationfilters gelden twee uitzonderingen: 
- Extra kengetallen met label 'Alleen FPC's & transacties'. Wanneer een van deze is geselecteerd op het tabblad [SHORTCODE_25]Tegel[SHORTCODE_26] samen met een controlestationfilter, zal Uptrends een waarschuwing weergeven. 
- Wanneer **Tijdgroepering** [SHORTCODE_27] De uren van de dag tonen[SHORTCODE_28] is geselecteerd op tabblad [SHORTCODE_29] Periode [SHORTCODE_30] en er een controlestationfilter actief is, wordt er een waarschuwing weergegeven.
   ![]([LINK_URL_12]) 