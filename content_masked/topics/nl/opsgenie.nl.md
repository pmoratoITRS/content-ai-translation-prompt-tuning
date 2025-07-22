{
  "hero": {
    "title": "Ontvang alerts in Opsgenie"
  },
  "title": "Opsgenie",
  "summary": "Stappen die nodig zijn om het versturen van Uptrends-alertberichten naar Opsgenie in te stellen.",
  "url": "[URL_BASE_TOPICS]alerting/integraties/opsgenie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Opsgenie** is Atlassians platform voor alerting- en incidentmanagement waarmee u uw alerts en meldingen van externe systemen (zoals Uptrends) kunt samenvoegen en prioriteiten kunt stellen en acties kunt toewijzen.  
Het integreren van uw Uptrends-alerting in uw Opsgenie-omgeving is eenvoudig! Voor het instellen van de integratie tussen beide systemen zijn de volgende stappen nodig:

1.  Stel een API-integratie in in Opsgenie
2.  Configureer de integratie in Uptrends
3.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Na het opzetten van deze integratie en met de juiste alertinginstellingen, genereren uw Uptrends-alerts ook alerts in Opsgenie. Hieronder ziet u een voorbeeld van hoe een dergelijke alert eruitziet in Opgenie.

![]([LINK_URL_1])

De Opsgenie-alert wordt gegenereerd voor het team waarvoor u de integratie instelt. Als u wilt dat alerts naar meerdere teams worden verzonden, kunt u voor elk team één integratie instellen.

Lees verder voor gedetailleerde instructies voor het opzetten van deze integratie!

## 1. Stel de integratie in in Opsgenie

1.  Stel in uw Opsgenie-omgeving een nieuw team in of gebruik een bestaand team.
2.  Ga bij de opties voor dit team naar *Integrations*.
3.  Zoek de reeds bestaande *API*-integratie (genaamd *{teamname}\_API*). Bestaat deze integratie nog niet, creëer dan een nieuwe integratie door op de knop **Add integration** te klikken en het integratietype 'API' te selecteren. Open deze integratie en kopieer de API key, deze heeft u straks nodig.
4.  Sla de integratie op.

Hiermee is het instellen van de integratie in Opsgenie voltooid.

## 2. Configureer de integratie in Uptrends

Om een nieuwe integratie voor Opsgenie toe te voegen in Uptrends volgt u de volgende stappen:

1.  Ga naar [SHORTCODE_3]Alerts > Integraties[SHORTCODE_4].
2.  Klik rechtsboven op [SHORTCODE_5]Integratie toevoegen[SHORTCODE_6].
3.  Kies Opsgenie als het integratietype.
4.  Voer een naam in voor deze integratie.
5.  Plak de Opsgenie API key die u eerder heeft gekopieerd in [SHORTCODE_7]Voorgedefinieerde variabelen > ApiKey[SHORTCODE_8].
6.  Klik op [SHORTCODE_9]Opslaan[SHORTCODE_10] om uw instellingen te bewaren. De nieuwe Opsgenie-integratie verschijnt op de pagina Integraties.

Standaard gebruikt de Opsgenie-integratie de internationale Opsgenie-instance, met [INLINE_CODE_1] als request-URL. Als u de EU- instance van Opsgenie gebruikt, dan moet de request-URL in plaats daarvan [INLINE_CODE_2] zijn. Om dit te bewerken doet u het volgende:

1. Schakel in de Opsgenie-integratie-instellingen **Integratie aanpassen** in. 
2. Klik op het tabblad [SHORTCODE_11]Aanpassingen[SHORTCODE_12] dat verschijnt.
3. Wijzig onder **Method en URL** de request-URL in [INLINE_CODE_3] om de EU-instance van de Opsgenie API te gebruiken.
![Opsgenie EU-instance URL]([LINK_URL_2])
4. Verstuur een testalert om te controleren of u de juiste instance gebruikt door op de knop [SHORTCODE_13]Testalert versturen[SHORTCODE_14] te klikken.
5. Sla de integratie op. 

Hiermee is de configuratie van de integratie in Uptrends voltooid. U kunt deze integratie nu gebruiken in uw alertdefinities.

[SHORTCODE_1]
**Tip:** Het deactiveren van een integratiedefinitie betekent dat de integratie niet wordt gebruikt voor alerts. Dit kan handig zijn als u het ontvangen van alerts tijdelijk wilt uitschakelen.
[SHORTCODE_2]

## 3. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar [SHORTCODE_15]Alerts > Alertdefinities [SHORTCODE_16] en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad [SHORTCODE_17]Escalatieniveau[SHORTCODE_18] bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]([LINK_URL_3]) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor Opsgenie. 
4.  Vergeet niet op de knop  [SHORTCODE_19]Opslaan[SHORTCODE_20] te klikken om uw wijzigingen te bewaren.

**Dat was het!** U heeft de Opsgenie-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team]([LINK_URL_4]).
