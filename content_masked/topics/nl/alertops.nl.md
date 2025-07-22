{
  "hero": {
    "title": "Ontvang alerts in AlertOps"
  },
  "title": "AlertOps",
  "summary": "Handleiding voor de AlertOps-integratie",
  "url": "[URL_BASE_TOPICS]alerting/integraties/alertops",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**AlertOps** is een realtime tool voor operationele automatisering. Hiermee kunt u uw incidenten prioriteren en uw processen automatiseren. Grote incidenten kunnen eenvoudig worden beheerd door oproepbare teams te mobiliseren en hen te voorzien van aanvullende informatie.

1.  Stel de inkomende integratie in AlertOps in
2.  Configureer de integratie in Uptrends
3.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Na het instellen van deze integratie en met de juiste alertinginstellingen, zullen uw Uptrends-alerts ook alerts genereren in AlertOps. Hieronder ziet u een voorbeeld van hoe zo'n alert eruitziet aan de kant van AlertOps.![]([LINK_URL_1])

Lees verder voor gedetailleerde instructies voor het instellen van deze integratie!

## 1. Stel een inkomende integratie in AlertOps in

1.  Navigeer in de AlertOps-interface naar het menu *Inbound Integrations* (onder *Integrations* in het zijbalkmenu).
2.  Zorg ervoor dat u zich op het tabblad **API** bevindt en klik op de knop *ADD API INTEGRATION*.
3.  Klik in het volgende scherm op *Uptrends* om de standaard Uptrends-integratie te selecteren.
4.  Geef de integratie een geschikte naam en selecteer de juiste **Recipient Group(s)/User(s)**.![]([LINK_URL_2])
5.  Klik op de knop *Save*.
6.  Kopieer de **API URL** die nu wordt vermeld in de AlertOps-interface. Deze heeft u nodig wanneer we de integratie aan de Uptrends-kant toevoegen.

Hiermee is het instellen van de integratie aan de AlertOps-kant voltooid.

[SHORTCODE_1]
**Opmerking**: AlertOps biedt een voorgedefinieerde Uptrends-integratie, die meteen functioneel zou moeten zijn. Deze integratie is in hoge mate aan te passen aan de AlertOps-kant, maar we raden aan om geen van de geavanceerde instellingen te wijzigen zolang we aan het configureren zijn. Nadat u heeft geverifieerd dat de integratie werkt, kunt u de instellingen aan uw wensen aanpassen.
[SHORTCODE_2]

## 2. Configureer de integratie in Uptrends

Om een nieuwe integratie voor AlertOps toe te voegen in Uptrends volgt u deze stappen:

1.  Ga naar [SHORTCODE_3]Alerting > Integraties[SHORTCODE_4].
2.  Klik rechtsboven op [SHORTCODE_5]Integratie toevoegen[SHORTCODE_6].
3.  Kies AlertOps als het integratietype.
4.  Voer een naam in voor deze integratie.
5.  Plak de AlertOps-**API URL** in het betreffende veld [SHORTCODE_7]voorgedefinieerde variabele[SHORTCODE_8].
6.  Klik op [SHORTCODE_9]Opslaan[SHORTCODE_10] om uw instellingen te bewaren. De nieuwe AlertOps-integratie verschijnt op de pagina Integraties.

Hiermee is de configuratie van de integratie in Uptrends voltooid. U kunt deze integratie nu gebruiken in uw alertdefinities.

## 3. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar [SHORTCODE_11]Alerting > Alertdefinities[SHORTCODE_12] en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad [SHORTCODE_13]Escalatieniveau[SHORTCODE_14] bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]([LINK_URL_3]) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor AlertOps.
4.  Vergeet niet op de knop [SHORTCODE_15]Opslaan[SHORTCODE_16] te klikken om uw wijzigingen te bewaren.

**Dat was het!** U heeft de AlertOps-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team]([LINK_URL_4]).
