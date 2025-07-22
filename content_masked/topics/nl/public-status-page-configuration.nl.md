{
  "hero": {
    "title": "Publieke statuspagina’s instellen"
  },
  "title": "Publieke statuspagina’s instellen",
  "summary": "In dit artikel wordt beschreven hoe u een nieuwe publieke statuspagina maakt en instelt.",
  "url": "[URL_BASE_TOPICS]dashboards-en-rapportages/statuspaginas/publieke-statuspagina-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Een Publieke statuspagina creëren

1. Ga naar [SHORTCODE_3] Accountinstellingen > Publieke statuspagina’s [SHORTCODE_4].
2. U ziet een lijst met uw huidige publieke statuspagina’s. Uw account bevat standaard één voorgeconfigureerde publieke statuspagina. 
3. Klik rechtsboven op de knop [SHORTCODE_5]Publieke statuspagina toevoegen[SHORTCODE_6].
4. Voer een beschrijvende *Naam* in voor de nieuwe statuspagina.
5. De *URL* wordt gegenereerd en is zichtbaar zodra u de statuspagina opslaat. Deze URL is nodig om [de statuspagina in te sluiten]([LINK_URL_1]) in een webpagina.
6. Selecteer de optie *Publiceren* om uw publieke statuspagina beschikbaar te maken op de URL die wordt weergegeven in het veld *URL*. De pagina is dan toegankelijk zonder inloggegevens van Uptrends. 
7. Ga vervolgens naar het tabblad [SHORTCODE_7]Data[SHORTCODE_8].
8. Configureer de **Periode** waarvoor u wilt dat data worden opgehaald en openbaar worden weergegeven.
9. Stel de **SLA** in ([service level agreement]([LINK_URL_2])). De data op uw publieke statuspagina zijn gebaseerd op de geselecteerde SLA.
10. Voeg de controleregels of controleregelgroepen toe waarvan u data wilt weergeven op de statuspagina. 
11. Klik onderaan op de knop [SHORTCODE_9]Opslaan[SHORTCODE_10].

U heeft nu met succes uw publieke statuspagina ingesteld en wordt naar de hoofdlijst met publieke statuspagina's gebracht, waar u uw nieuwe publieke statuspagina ziet. Om een preview van gepubliceerde pagina's te bekijken klikt u op de previewlinks. 

Als u extra hulp nodig heeft, aarzel dan niet om [een supportticket in te dienen]([LINK_URL_3]).

## Uw publieke statuspagina insluiten in een webpagina [ANCHOR_1]

Het insluiten van een publieke statuspagina op uw website is eenvoudig.
1. Ga naar het tabblad [SHORTCODE_11]Layout instellingen[SHORTCODE_12] van de publieke statuspagina.
2. Kopieer de waarde van de *Embed-code*, die er ongeveer uitziet als [INLINE_CODE_1].
3. Plak de *Embed-code* in de bron van uw webpagina.
4. Bewaar en ververs de pagina om het resultaat te bekijken.

## Uw publieke statuspagina aanpassen

Er zijn een aantal dingen die u kunt doen om het uiterlijk van uw publieke statuspagina aan te passen.
Ga naar het tabblad [SHORTCODE_13] Layout instellingen [SHORTCODE_14] van uw publieke statuspagina om instellingen zoals kleur, logo, onderwerp, berichten, sorteervolgorde enzovoort te wijzigen.

![screenshot tabblad layout instellingen van publieke statuspagina]([LINK_URL_4])

### Berichten gebruiken [ANCHOR_2]

Als u uw klanten wilt informeren over lopende incidenten en deze wilt weergeven op uw publieke statuspagina's, kunt u een statusrapport of bericht invoeren in de berichtvelden.

U vindt de velden **Berichttitel** en **Berichttekst** op het tabblad [SHORTCODE_15] Layout instellingen [SHORTCODE_16].

Nadat u een titel en tekst heeft ingevoerd, worden deze weergegeven tussen de titelbalk en de inhoud van uw publieke statuspagina.

![]([LINK_URL_5])

[SHORTCODE_1]**Tip:** Als u het bericht wilt benadrukken, kopieer dan een emoji zoals 'waarschuwing', 'uitroepteken' of 'let op', en plak deze in het tekstveld van uw bericht.[SHORTCODE_2]

### De pagina automatisch verversen

Als u wilt dat de pagina automatisch wordt ververst, schakelt u de instelling **Automatisch verversen** in op het tabblad [SHORTCODE_17] Layout instellingen [SHORTCODE_18] van uw publieke statuspagina. De pagina wordt dan elke 30 seconden ververst. Het automatisch verversen is standaard uitgeschakeld. 

### Het logo wijzigen 

Als u het logo van uw pagina wilt wijzigen, moet u eerst een [support ticket]([LINK_URL_6]) openen en een PNG- of JPG-afbeeldingsbestand van 210 x 40 pixels bijvoegen. Houd er rekening mee dat grotere afbeeldingen worden verkleind. Support voegt vervolgens het bestand toe aan uw account, zodat u het bestaande Uptrends-logo op uw pagina kunt vervangen. 

### Alternatieve controleregelnamen [ANCHOR_3]

De controleregelnamen die u intern gebruikt, kunnen minder betekenisvol zijn voor uw externe publiek of misschien wilt u de controleregelnamen die binnen uw bedrijf worden gebruikt gewoon niet delen. In dat geval kunt u alternatieve controleregelnamen gebruiken. Deze worden ingesteld door een vrij veld met een identieke naam te gebruiken in zowel de publieke statuspagina als de controleregels. 

Alternatieve controleregelnamen definiëren:

1. Ga naar [SHORTCODE_19] Accountinstellingen > Publieke statuspagina's [SHORTCODE_20].
2. Open de publieke statuspagina waarvoor u alternatieve controleregelnamen wilt instellen.
3. Ga naar het tabblad [SHORTCODE_21]Layout instellingen[SHORTCODE_22] van een publieke statuspagina.
4. Voer een *Vrij veld voor de naam* in, bijv. [INLINE_CODE_2].
5. Klik onderaan op de knop [SHORTCODE_23]Opslaan[SHORTCODE_24].
6. Ga naar [SHORTCODE_25] Monitoring > Controleregels beheren [SHORTCODE_26].
7. Open het tabblad [SHORTCODE_27] Algemeen [SHORTCODE_28].
8. Voeg in het gedeelte **Metadata** een vrij veld toe met de naam die u in de publieke statuspagina heeft gebruikt, bijv. [INLINE_CODE_3] en voeg een waarde toe. Deze waarde is de alternatieve controleregelnaam die wordt weergegeven op de publieke statuspagina.
9. Klik op de knop [SHORTCODE_29]Opslaan[SHORTCODE_30].
10. Herhaal stap 6 t/m 9 voor alle controleregels die met alternatieve namen op de publieke statuspagina moeten verschijnen.

Als u meerdere publieke statuspagina's heeft waarop alternatieve controleregelnamen moeten worden weergegeven, herhaalt u stap 1 tot en met 5 voor die pagina's. 
