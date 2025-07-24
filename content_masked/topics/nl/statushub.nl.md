{
  "hero": {
    "title": "Toon uw API- en sitestatus in StatusHub"
  },
  "title": "StatusHub Integratie",
  "summary": "Combineer de kracht van de alertingmogelijkheden van StatusHub met uw Uptrends-instellingen door deze handige integratie te gebruiken.",
  "url": "[URL_BASE_TOPICS]alerting/integraties/statushub",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Door uw [Statushub]([LINK_URL_1]) te integreren met Uptrends zijn automatische statusupdates van de services op uw StatusHub-statuspagina mogelijk. Het configureren van de integratie tussen beide systemen bestaat uit drie stappen.

1.  Webhook-integraties configureren in StatusHub.
2.  Een integratie creëren en deze webhooks specificeren in Uptrends.
3.  Servicelinks creëren in Uptrends om Uptrends-controleregels aan StatusHub-services te kunnen koppelen.

Deze pagina bevat een gedetailleerde beschrijving van de stappen die nodig zijn om Uptrends te integreren met uw StatusHub-statuspagina’s.

## 1. Webhook-integraties configureren in StatusHub

1.  Eerst bereidt u alles voor aan de kant van StatusHub. Log in op uw StatusHub-account en klik op het potloodpictogram om uw statussite te bewerken.

2.  Klik op ‘Service & integrations’ in het menu aan de linkerkant. Vervolgens bewerkt u de eerste service die u wilt besturen met Uptrends.

3.  Zoek in het menu met services het gedeelte ‘Enable/disable integrations’. Klik op de knop Uptrends en zorg dat deze gemarkeerd is.

4.  Klik onderaan in het menu op ‘Update Service’. Terug in het serviceoverzicht ziet u dat er nu een URL bij de service wordt vermeld in de vorm

    [INLINE_CODE_1]

    Deze URL gaat u straks gebruiken om Uptrends te koppelen aan deze StatusHub-service.

5.  Herhaal deze procedure voor elke service die u wilt besturen met Uptrends.

Hiermee is het configureren van de integratie in StatusHub voltooid.

[SHORTCODE_1]
**Tip:** Er is in Uptrends geen beperking op het aantal StatusHub-services dat u kunt besturen. U kunt zo veel servicelinks creëren als u nodig heeft, of met slechts één service beginnen.
[SHORTCODE_2]

## 2. De integratie configureren in Uptrends

1.  Ga in uw Uptrends-account naar [SHORTCODE_5] Alerting > Integraties [SHORTCODE_6] in het zijbalkmenu.
2.  Om een geheel nieuwe StatusHub-integratie in te stellen klikt u op **Integratie toevoegen** in de rechterbovenhoek.
3.  Kies StatusHub als het integratietype. Voer een naam in voor deze integratie (bijvoorbeeld *Statushub*).
4.  Sla de integratie op.
5.  Selecteer in het volgende scherm (het overzicht Integrations) de integratie die u zojuist heeft opgeslagen.
6.  Terug in het integratiescherm StatusHub moet u ons informatie geven over uw StatusHub-services. Klik op de knop [SHORTCODE_7]Service toevoegen[SHORTCODE_8] om er een toe te voegen.
7.  Voer voor elke StatusHub-service de servicenaam en de URL van de service in. De service-URL is de webhook-URL die u zojuist heeft gemaakt door de Uptrends-functie in StatusHub in te schakelen.
8.  Klik tot slot op [SHORTCODE_9]Opslaan[SHORTCODE_10] om uw instellingen op te slaan. De nieuwe StatusHub-integratie verschijnt op de pagina Integraties.

## 3. De StatusHub-integratie gebruiken in alertdefinities

Voordat de integratie daadwerkelijk kan worden gebruikt, moet deze worden gekoppeld aan ten minste één alertdefinitie en moeten een aantal servicelinks worden geconfigureerd. Een servicelink is de koppeling tussen een Uptrends-controleregel en een StatusHub-service. Alerts voor die controleregel zullen worden verzonden naar de service waaraan u deze koppelt.

1.  Navigeer naar een van uw alertdefinities of maak een nieuwe ([SHORTCODE_11] Alerting > Alertdefinities [SHORTCODE_12]).
2.  Selecteer het escalatieniveau waaraan u StatusHub wilt toevoegen.
3.  Zoek in het gedeelte **Alerts versturen door integraties** de StatusHub-integratie en selecteer die. Lees het Knowledge Base-artikel [Alert escalatieniveaus]([LINK_URL_2]) om te leren hoe escalaties werken.
4.  De integratie is nog niet actief; klik op het selectievakje om deze in dit escalatieniveau te activeren.
5.  Er verschijnt een knop [SHORTCODE_13]Servicelink toevoegen[SHORTCODE_14]. Klik erop om een koppeling te creëren tussen een Uptrends-controleregel aan de linkerkant en een StatusHub-service aan de rechterkant. Met behulp van deze instellingen beschikt u over verfijnde controle over welke Uptrends-controleregel welke service bijwerkt in StatusHub. U kunt zoveel servicelinks aan deze escalatie toevoegen als u nodig heeft.
6.  Klik links onderaan op de knop [SHORTCODE_15]Opslaan[SHORTCODE_16] om deze alertdefinitie op te slaan.

[SHORTCODE_3]
**Tip:** Bij de meeste configuraties worden eenvoudige een-op-een-servicelinks gebruikt tussen controleregels en services. Maar het is ook mogelijk om meer geavanceerde configuraties te creëren. U kunt bijvoorbeeld meerdere servicelinks creëren die een enkele controleregel gebruiken om verschillende services in StatusHub te updaten.
[SHORTCODE_4]

## Wat u kunt verwachten als uw integratie is voltooid

De normale voorwaarden voor alertdefinities zijn van toepassing. Wanneer Uptrends een fout detecteert voor een van uw controleregels, genereren wij een alert op basis van de instellingen in uw escalatieniveaus. Wanneer een escalatieniveau een nieuwe alert triggert, genereren we een nieuw incident in StatusHub voor de desbetreffende service(s). De servicestatus wordt gewijzigd in **Service disruption**, en het nieuwe incident krijgt de status **Investigating**. Uw StatusHub-statuspagina wordt onmiddellijk bijgewerkt met deze wijzigingen.

Deze situatie blijft ongewijzigd zolang de errorsituatie in Uptrends voortduurt. In de tussentijd kunt u uw StatusHub-services naar eigen inzicht bijwerken. Zodra Uptrends detecteert dat de error is opgelost, updaten we uw service naar **Service is operating normally**, en het incident naar **Monitoring**. Wanneer u zeker weet dat het probleem is opgelost, kunt u het incident in StatusHub instellen op **Resolved**. Op deze manier kunt u altijd bepalen wat er op uw statuspagina wordt weergegeven.

Heeft u vragen over het maken van de juiste set-up? Neem dan [contact op met ons support team]([LINK_URL_3]).
