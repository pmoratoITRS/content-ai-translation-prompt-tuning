{
  "hero": {
    "title": "Ontvang alerts in Statuspage"
  },
  "title": "Statuspage",
  "summary": "Stappen die nodig zijn om het versturen van Uptrends-alertberichten naar Statuspage in te stellen.",
  "url": "[URL_BASE_TOPICS]alerting/integraties/statuspage",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Statuspage** is Atlassians status- en incidentcommunicatietool waarmee u de status van uw pagina's en websites in real time naar uw gebruikers kunt communiceren.  
Het integreren van uw Uptrends-alering in uw Statuspage-omgeving is eenvoudig! Voor het instellen van de integratie tussen beide systemen zijn de volgende stappen nodig:

1.  Stel een component in in Statuspage
2.  Creëer een Statuspage API key
3.  Configureer de integratie in Uptrends
4.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Na het opzetten van deze integratie en met de juiste alertinginstellingen, toont uw statuspagina onmiddellijk de realtimestatus van uw pagina of resource aan uw gebruikers.

![]([LINK_URL_1])

Lees verder voor gedetailleerde instructies voor het opzetten van deze integratie!

## 1. Voeg een component toe in Statuspage

1.  Voeg in uw Statuspage-omgeving een nieuwe *component* toe via het menu **Components** Geef de nieuwe component een geschikte naam en eventueel een goede omschrijving. Sla de component op.
2.  Open de zojuist gecreëerde component en noteer de URL. Deze heeft de volgende vorm: manage.Statuspage.io/pages/{page\_id}/components/{component\_id}/edit. We hebben straks zowel de *{page\_id}* als de *{component\_id}* nodig, zorg er dus voor dat u deze noteert!

[SHORTCODE_1]
**Tip:** Het is misschien een goed idee om voor elk domein dat u met Uptrends monitort een afzonderlijke component te maken. Zo kunt u beter in de gaten houden welke domeinen operationeel zijn of niet op een bepaald moment.
[SHORTCODE_2]

## 2. Creëer een API key in Statuspage

1.  Klik linksonder in het scherm op het gebruikerspictogram en ga naar **API info**.

 ![]([LINK_URL_2])
 
2.  Creëer hier een nieuwe API key door op de knop *Create key* te klikken. Voer een geschikte naam in en bevestig (Confirm).
3.  De nieuw gecreëerde API key verschijnt onmiddellijk. Noteer deze key, want die hebben we straks nodig.

Hiermee is het instellen van de integratie in Statuspage voltooid.

## 3. Configureer de integratie in Uptrends

Om een nieuwe integratie voor Statuspage toe te voegen in Uptrends volgt u deze stappen:

1.  Ga naar [SHORTCODE_7]Alerting > Integraties[SHORTCODE_8].
2.  Klik rechtsboven op [SHORTCODE_9]Integratie toevoegen[SHORTCODE_10].
3.  Kies Statuspage als het integratietype.
4.  Voer een naam in voor deze integratie.
5.  Plak de Statuspage API Key, Page\_Id en Component\_Id in de betreffende waardevelden [SHORTCODE_11]voorgedefinieerde variabele[SHORTCODE_12].
6.  Klik op [SHORTCODE_13]Opslaan[SHORTCODE_14] om uw instellingen te bewaren. De nieuwe Statuspage-integratie verschijnt op de pagina Integraties.

Hiermee is de configuratie van de integratie in Uptrends voltooid. U kunt deze integratie nu gebruiken in uw alertdefinities.

[SHORTCODE_3]
**Tip:** Het deactiveren van een integratiedefinitie betekent dat de integratie niet wordt gebruikt voor alerts. Dit kan handig zijn als u het ontvangen van alerts tijdelijk wilt uitschakelen.
[SHORTCODE_4]

## 4. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar [SHORTCODE_15]Alerting > Alertdefinities[SHORTCODE_16] en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad [SHORTCODE_17]Escalatieniveau[SHORTCODE_18] bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]([LINK_URL_3]) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor Statuspage. 
4.  Vergeet niet op de knop [SHORTCODE_19]Opslaan[SHORTCODE_20] te klikken om uw wijzigingen te bewaren.

[SHORTCODE_5]
**Tip:** Elke individuele Statuspage-integratie die u creëert heeft invloed op één Statuspage-component. Daarom raden we aan om individuele componenten in Statuspagina af te stemmen op individuele integraties en alertdefinities aan de Uptrends-kant.
[SHORTCODE_6]

**Dat was het!** U heeft de Statuspage-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team]([LINK_URL_4]).
