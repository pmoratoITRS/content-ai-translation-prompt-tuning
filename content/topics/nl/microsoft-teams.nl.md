{
  "hero": {
    "title": "Ontvang monitoringalerts in Microsoft Teams"
  },
  "title": "Microsoft Teams-integratie",
  "summary": "Ontvang website monitoring-alerts van Uptrends in Microsoft Teams.",
  "url": "/support/kb/alerting/integraties/microsoft-teams",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/microsoft-teams" 
}

**Microsoft Teams** is de hub voor samenwerking in Microsoft 365. In Teams kunt u communiceren (in chat, bellen, video) en informatie delen (bestanden, agenda's, etc.). Door Microsoft Teams te integreren met Uptrends zijn automatische meldingen van Uptrends mogelijk. Voor het instellen van de integratie tussen beide systemen zijn de volgende stappen nodig:

1.  Stel een *workflow* in Microsoft Teams in
2.  Configureer de integratie in Uptrends
3.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Wat krijgt u als deze integratie is ingesteld? Hieronder ziet u hoe de integratie eruitziet in Microsoft Teams. 

![Teams alert voorbeeld](/img/content/scr-teams-integration-alert-example.min.png)      

Binnen het Microsoft Teams-kanaal waarvoor de integratie is gedefinieerd, ontvangt u een bericht met gegevens over de alert die is gegenereerd. Vanuit dit bericht kunt u direct naar het dashboard, de fout of de controleregel in Uptrends springen om nog meer gegevens te krijgen en het probleem verder te onderzoeken. Druk gewoon op een van de knoppen en u komt op de juiste plek in de Uptrends app.

Lees verder voor gedetailleerde instructies over het opzetten van deze integratie!

## 1. Stel een workflow in Microsoft Teams in

1.  Ga in Microsoft Teams naar het kanaal waar u berichten van Uptrends wilt ontvangen. Hover boven het kanaal zodat {{< AppElement type="menuitem" >}}Meer opties{{< /AppElement >}} ( ... ) verschijnt. Selecteer {{< AppElement type="menuitem" >}}Workflows{{< /AppElement >}}.  
    ![Een workflow toevoegen](/img/content/scr-teams-integration-add-workflow.min.png)
2.  Zoek naar en selecteer *Post to a channel when a webhook request is received*.  
    ![](/img/content/31cf8b92-5d3f-41ca-af1f-cd2364c47461.png)
3.  Voer een naam in voor de workflow.
4.  Klik op *Volgende*.
5.  Controleer de instellingen **Microsoft Teams Team** en **Microsoft Teams Channel** en klik op *Workflow toevoegen*.
6.  De workflow moet na een paar seconden zijn gemaakt. Onder aan het formulier wordt een URL weergegeven:  
    ![Teams workflow URL](/img/content/scr-teams-integration-workflow-added.min.png)
7.  Kopieer de URL en sla deze ergens op. U heeft die straks nodig om de integratie in Uptrends te configureren.
8.  Klik op {{< AppElement type="menuitem" >}}Gereed{{< /AppElement >}}.

Hiermee is het instellen van de integratie in Microsoft Teams voltooid.

## 2. Configureer de integratie in Uptrends

Om een nieuwe integratie voor Microsoft Teams toe te voegen in Uptrends volgt u deze stappen:

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Integraties{{< /AppElement >}}.
2.  Klik rechtsboven op {{< AppElement type="button" >}}Integratie toevoegen{{< /AppElement >}}.
3.  Kies Microsoft Teams als het integratietype.  
    ![](/img/content/9df05fe6-c315-4a7c-89d9-f4e2bf8344bf.png)
4.  Voer een naam in voor deze integratie.
5.  Plak de Microsoft Teams webhook-URL die u eerder heeft gekopieerd in {{< AppElement type="menuitem" >}}Voorgedefinieerde variabelen > WorkflowURL{{< /AppElement >}}.
6.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om uw instellingen te bewaren. De nieuwe Microsoft Teams-integratie verschijnt op de pagina Integraties.

Hiermee is de configuratie van de integratie in Uptrends voltooid. U kunt deze integratie nu gebruiken in uw alertdefinities.

{{< callout >}}
**Tip:** Het deactiveren van een integratiedefinitie betekent dat de integratie niet zal worden gebruikt voor alertingdoeleinden. Dit kan handig zijn als u het ontvangen van alerts tijdelijk wilt uitschakelen.
{{< /callout >}}

## 3. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Alertdefinities{{< /AppElement >}} en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad {{< AppElement type="tab" >}} Escalatieniveau {{< /AppElement >}} bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="nl" >}}) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor Microsoft Teams.
4.  Vergeet niet op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} te klikken om uw wijzigingen te bewaren.

**Dat was het!** U heeft de Microsoft Teams-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team](/contact).
