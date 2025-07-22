{
  "hero": {
    "title": "Ontvang website monitoring alerts in Slack"
  }, 
  "title": "Slack",
  "summary": "Ontvang website monitoring alerts van Uptrends in een Slack channel. Meld u aan voor een gratis proefperiode van 30 dagen van Uptrends!",
  "url": "/support/kb/alerting/integraties/slack",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/slack" 
}

Door **Slack** te integreren met Uptrends kunt u alertberichten sturen naar uw **Slack channels**. Elke integratie voor Slack die u definieert kan alerts naar een ander kanaal sturen, en u kunt meerdere integraties voor Slack toekennen aan een enkele alertescalatie. U configureert de integratie in twee stappen:

1.  Configureer de integraties in Uptrends
2.  Voeg in Uptrends de integraties toe aan een alertdefinitie

Bent u benieuwd naar wat u te zien krijgt als deze integratie is geconfigureerd? Hieronder ziet u een voorbeeld van de integratie in een Slack channel. Lees de **gedetailleerde aanwijzingen** hierna over de configuratie van **Integraties voor Slack**

![](/img/sub/integrations/slack-alert.png)

## 1. De integratie configureren in Uptrends

Om integraties voor Slack toe te voegen aan Uptrends heeft u een Slack-account nodig. U zult voor of tijdens de configuratie moeten inloggen. U configureert een integratie als volgt:

1.  Navigeer naar {{< AppElement type="menuitem" >}}Alerting > Integraties{{< /AppElement >}} in het hoofdmenu om de pagina Integraties te openen. De pagina Integraties bevat de integraties die u in Uptrends heeft gedefinieerd. Aanvankelijk zal deze pagina leeg zijn.
2.  Klik op de knop {{< AppElement type="button" >}}Integratie toevoegen{{< /AppElement >}} in de rechter bovenhoek om de pagina {{< AppElement type="menuitem" >}}Nieuwe integratie{{< /AppElement >}} te openen.
3.  Selecteer **Slack** als uw **Integratietype**.
4.  Klik op de knop **Add to Slack** en kies het team en Slack channel.
5.  Klik op {{< AppElement type="button" >}}Authorize{{< /AppElement >}} om terug te gaan naar de configuratiepagina Integratie.
6.  Voer in het vak **Integratienaam** een naam in voor deze integratie.
7.  Klik op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} in de linker benedenhoek. U ziet uw nieuwe integratie voor Slack op de pagina *Integratie*.
8.  Ga verder met het toevoegen van nieuwe integraties als u berichten naar meerdere Slack channels moet versturen.

{{< callout >}}
**Tip:** Het deactiveren van een integratiedefinitie betekent dat Uptrends de integratie niet zal gebruiken voor het versturen van alerts. Het deactiveren van een integratiedefinitie kan handig zijn als u bijvoorbeeld het ontvangen van alerts in uw Slack channel tijdelijk wilt uitschakelen.
{{< /callout >}}

## 2. De integratie toevoegen aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. Deze moet worden **gekoppeld aan een of meer escalatieniveaus om alerts te ontvangen** via de integratie. Om een integratiedefinitie aan een escalatieniveau te koppelen doet u het volgende:

1.  Navigeer naar de betreffende alertdefinitie in Uptrends (*Alerting* > *Alertdefinities*).
2.  Klik om een bestaande definitie te openen of een maak een nieuwe met de knop {{< AppElement type="button" >}}Alertdefinitie toevoegen{{< /AppElement >}} rechts bovenaan.
3.  Klik op een tabblad {{< AppElement type="tab" >}}Escalatieniveau{{< /AppElement >}}. Lees het Knowledge Base-artikel [Alert escalatieniveaus]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="nl" >}}) om te leren hoe escalaties werken.
4.  Selecteer de selectievakjes voor uw integratiedefinities in het gedeelte **Alerts versturen door integratie**.
5.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} als u klaar bent.

**Dat is alles!** U heeft met succes een integratie voor Slack geconfigureerd.

Zoals gewoonlijk kunt u als u vragen heeft [contact opnemen met ons support team](/contact).
