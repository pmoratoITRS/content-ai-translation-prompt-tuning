{
  "hero": {
    "title": "Ontvang alerts in AlertOps"
  }, 
  "title": "AlertOps",
  "summary": "Handleiding voor de AlertOps-integratie",
  "url": "/support/kb/alerting/integraties/alertops",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/alertops" 
}

**AlertOps** is een realtime tool voor operationele automatisering. Hiermee kunt u uw incidenten prioriteren en uw processen automatiseren. Grote incidenten kunnen eenvoudig worden beheerd door oproepbare teams te mobiliseren en hen te voorzien van aanvullende informatie.

1.  Stel de inkomende integratie in AlertOps in
2.  Configureer de integratie in Uptrends
3.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Na het instellen van deze integratie en met de juiste alertinginstellingen, zullen uw Uptrends-alerts ook alerts genereren in AlertOps. Hieronder ziet u een voorbeeld van hoe zo'n alert eruitziet aan de kant van AlertOps.![](/img/content/8f848598-92d3-4add-a9ca-3b483b0d0f14.png)

Lees verder voor gedetailleerde instructies voor het instellen van deze integratie!

## 1. Stel een inkomende integratie in AlertOps in

1.  Navigeer in de AlertOps-interface naar het menu *Inbound Integrations* (onder *Integrations* in het zijbalkmenu).
2.  Zorg ervoor dat u zich op het tabblad **API** bevindt en klik op de knop *ADD API INTEGRATION*.
3.  Klik in het volgende scherm op *Uptrends* om de standaard Uptrends-integratie te selecteren.
4.  Geef de integratie een geschikte naam en selecteer de juiste **Recipient Group(s)/User(s)**.![](/img/content/84d3f6f8-493a-48fa-95ff-0b16acf5a634.png)
5.  Klik op de knop *Save*.
6.  Kopieer de **API URL** die nu wordt vermeld in de AlertOps-interface. Deze heeft u nodig wanneer we de integratie aan de Uptrends-kant toevoegen.

Hiermee is het instellen van de integratie aan de AlertOps-kant voltooid.

{{< callout >}}
**Opmerking**: AlertOps biedt een voorgedefinieerde Uptrends-integratie, die meteen functioneel zou moeten zijn. Deze integratie is in hoge mate aan te passen aan de AlertOps-kant, maar we raden aan om geen van de geavanceerde instellingen te wijzigen zolang we aan het configureren zijn. Nadat u heeft geverifieerd dat de integratie werkt, kunt u de instellingen aan uw wensen aanpassen.
{{< /callout >}}

## 2. Configureer de integratie in Uptrends

Om een nieuwe integratie voor AlertOps toe te voegen in Uptrends volgt u deze stappen:

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Integraties{{< /AppElement >}}.
2.  Klik rechtsboven op {{< AppElement type="button" >}}Integratie toevoegen{{< /AppElement >}}.
3.  Kies AlertOps als het integratietype.
4.  Voer een naam in voor deze integratie.
5.  Plak de AlertOps-**API URL** in het betreffende veld {{< AppElement type="menuitem" >}}voorgedefinieerde variabele{{< /AppElement >}}.
6.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om uw instellingen te bewaren. De nieuwe AlertOps-integratie verschijnt op de pagina Integraties.

Hiermee is de configuratie van de integratie in Uptrends voltooid. U kunt deze integratie nu gebruiken in uw alertdefinities.

## 3. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Alertdefinities{{< /AppElement >}} en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad {{< AppElement type="tab" >}}Escalatieniveau{{< /AppElement >}} bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="nl" >}}) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor AlertOps.
4.  Vergeet niet op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} te klikken om uw wijzigingen te bewaren.

**Dat was het!** U heeft de AlertOps-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team](/contact).
