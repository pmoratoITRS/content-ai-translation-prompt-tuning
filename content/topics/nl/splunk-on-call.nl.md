{
  "hero": {
    "title": "Ontvang monitoringalerts in Splunk On-Call"
  }, 
  "title": "Splunk On-Call-integration",
  "summary": "Ontvang websitemonitoring-alerts van Uptrends in Splunk On-Call.",
  "url": "/support/kb/alerting/integrations/splunk-on-call",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/splunk-on-call" 
}

**Splunk On-Call** is een incidentmanagementplatform dat DevOps-teams helpt om samen te werken en incidenten effectief op te lossen. U kunt uw team organiseren voor on-call-planning, incidentescalaties en hen in een mum van tijd op de hoogte stellen wanneer er problemen zijn die onmiddellijke aandacht vereisen. 

Integratie van Splunk On-Call met Uptrends creëert automatisch incidenten die worden weergegeven in uw Splunk On-Call-dashboard. Volg de volgende stappen voor het configureren van de integratie tussen beide systemen:

## 1. Configureer uw REST-integratie in Splunk On-Call.
1. Log in op uw Splunk On-Call-account.
2. Klik in het tabblad {{< AppElement type="tab" >}}Integrations{{< /AppElement >}} op de REST-integratie die standaard al is ingeschakeld. Raadpleeg voor meer informatie de Splunk On-Call [REST Integration](https://help.victorops.com/knowledge-base/rest-endpoint-integration-guide/). 
3. Kopieer de *URL to notify* zonder de waarde */$routing_key* en sla deze op voor later gebruik.

## 2. Configureer de integratie in Uptrends
1. Ga naar uw Uptrends-account en ga naar het menu {{< AppElement type="menuitem" >}}Alerting > Integraties {{< /AppElement >}}.
2. Klik in de rechterbovenhoek van uw scherm op de knop {{< AppElement type="button" >}}Integratie toevoegen{{< /AppElement >}}.
3. Er verschijnt een pop-upvenster, selecteer *Splunk On-Call* als het integratietype.
4. Klik op de knop {{< AppElement type="button" >}}Kiezen{{< /AppElement >}}.
5. U kunt nu de details voor uw integratieconfiguratie bewerken. Geef uw nieuwe integratie een naam.
6. Standaard is het veld {{< AppElement type="menuitem" >}}Integratie aanpassen{{< /AppElement >}} uitgeschakeld. Vink het selectievakje aan om aanpassing in te schakelen en de standaard integratie-instellingen voor Splunk On-Call aan te passen. Anders kunt u het laten zoals het is. 

{{< callout >}}
**Opmerking:** Wanneer u {{< AppElement type="menuitem" >}}Integratie aanpassen{{< /AppElement >}} inschakelt, verschijnt het tabblad {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}}. Hier kunt u opgeven welke berichten worden verzonden wanneer een alert is gegenereerd, waaronder naar derden of API's, inhoud van HTTP-berichten of vereiste authenticatie enzovoort.

In de meeste gevallen is één enkele HTTP-stap voldoende. Het is echter mogelijk om meer stappen toe te voegen als u afzonderlijke stappen voor authenticatie nodig heeft. Daarnaast kunt u ervoor kiezen om afzonderlijke stappen te definiëren voor afzonderlijke alerttypes. Dit is handig als uw foutberichten moeten verschillen van uw OK-berichten (voor opgeloste alerts). Raadpleeg onze [knowledgebase-artikelen over integraties]({{< ref path="support/kb/alerting/integrations" lang="nl" >}}) voor meer informatie.
{{< /callout >}}


7. In het gedeelte Voorgedefinieerde variabelen ziet u de naam *SplunkOnCallUrl*. Kies welke waarde u wilt opgeven in het keuzemenu. U kunt bijvoorbeeld de optie *Waarde hier opgeven* kiezen.
8. Klik op de drie stippen naast het menu *SplunkOnCallUrl*. Er verschijnt een pop-upvenster en u kunt kiezen uit twee opties. U kunt de waarde van de *URL om te melden* die u eerder heeft opgeslagen, plakken in het veld Platte tekst of een gebruikersnaam of wachtwoord kiezen voor [vault-inloggegevens]({{< ref path="support/kb/account/vault#credential-set" lang="nl" >}}) (indien van toepassing).
9. Klik op de knop {{< AppElement type="button" >}}Selecteren{{< /AppElement >}}.
10. Geef vervolgens de waarde op van de *RoutingKey* die u wilt gebruiken. [Routing keys](https://help.victorops.com/knowledge-base/routing-keys/) vindt u op het tabblad {{< AppElement type="tab" >}} Settings {{< /AppElement >}} in uw Splunk On-call-account. 
11. Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om de integratie-instellingen te bevestigen.

Hiermee is de integratieconfiguratie in Uptrends voltooid. U kunt deze integratie nu gebruiken en toevoegen aan uw [alertdefinities]({{< ref path="support/kb/alerting/create-alert-definitions" lang="nl" >}}).

**Dat is alles!** U heeft de Splunk On-Call-integratie succesvol geconfigureerd.

Wat krijgt u wanneer deze integratie is geconfigureerd? Bekijk hieronder een voorbeeld van hoe de integratie eruitziet in uw Splunk On-Call-dashboard. 
![Splunk On-Call-dashboard met Uptrends-integratie](/img/content/scr_integration-splunk-on-call.min.png)

{{< callout >}}
**Tip:** Als u een integratiedefinitie deactiveert, wordt de integratie niet gebruikt voor alertingdoeleinden. Dit kan handig zijn als u het ontvangen van alerts tijdelijk wilt uitschakelen.
{{< /callout >}}

Mocht u nog vragen hebben, neem dan gerust [contact op met ons supportteam](/contact).
