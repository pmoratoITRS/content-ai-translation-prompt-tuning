{
  "hero": {
    "title": "Ontvang websitemonitoring-alerts in ServiceNow"
  }, 
  "title": "ServiceNow-integratie",
  "summary": "Ontvang websitemonitoring-alerts van Uptrends in ServiceNow.",
  "url": "/support/kb/alerting/integrations/service-now",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/service-now" 
}

**ServiceNow** is een cloudgebaseerd platform waarmee u uw algemene Informatietechnologie (IT)-activiteiten kunt beheren via de verschillende ServiceNow-applicaties, waaronder Incidentmanagement.

Door **ServiceNow** te integreren met Uptrends worden automatisch incidenten gecreëerd die worden weergegeven in uw **ServiceNow**-account. Voor meer informatie over ServiceNow raadpleegt u de [ServiceNow Integrations-documentatie](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/managing-data/concept/integrations.html) en [ServiceNow REST APIs](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html).

## De integratie configureren

Om integraties voor **ServiceNow** aan Uptrends toe te voegen, heeft u een ServiceNow-account nodig. Zorg ervoor dat u uw instance name en inloggegevens bij de hand heeft.

De integratie configureren:

1. Ga in de Uptrends-webapplicatie naar {{< AppElement type="menuitem" >}} Alerting > Integraties {{< /AppElement >}}.
2. Klik in de rechter bovenhoek van uw scherm op de knop {{< AppElement type="button" >}} Integratie toevoegen {{< /AppElement >}}.
3. Selecteer in het pop-upvenster **ServiceNow** als het third party-integratietype.
4. Klik op de knop {{< AppElement type="button" >}} Kiezen {{< /AppElement >}} om een nieuwe integratie te creëren.
5. **ServiceNow** is de standaardwaarde bij **Integratietype**. Geef de naam op van uw nieuwe integratie.
6. Vul in het gedeelte **Voorgedefinieerde variabelen** de volgende **Waarde**-velden in:

- `InstanceName` — de instance name van uw ServiceNow. Deze kunt u identificeren via de ServiceNow-gebaseerde URL `https://<instancename>.service-now.com`.
- `Username` — de gebruikersnaam van uw ServiceNow-inlogaccount.
- `Password` — het wachtwoord van uw ServiceNow-inlogaccount.

U kunt ervoor kiezen om deze waarden op te geven als **Platte tekst** of door **Vault-inloggegevens** op te halen die zijn opgeslagen in de [Vault]({{< ref path="/support/kb/account/vault" lang="nl" >}}). De integratie gebruikt automatisch basisauthenticatie om toegang te krijgen tot het **ServiceNow**-platform.

![ServiceNow Integratie](/img/content/scr-service-now-integration.min.png)

7. (Optioneel) Om uw login en andere integratie-instellingen aan te passen, vinkt u het selectievakje **Integratie aanpassen** aan. Door aanpassen in te schakelen, kunt u:

- Bestaande **Voorgedefinieerde variabelen** toevoegen en bewerken om deze te gebruiken voor authenticatie, escalatieniveaus en stapdefinities.
- Stappen toevoegen en definiëren voor verschillende alerttypen. In de meeste gevallen is één HTTP-stap al voldoende voor uw configuratie. Als u afzonderlijke stappen nodig heeft voor andere scenario's, zoals authenticatie, klikt u op de knop {{< AppElement type="button" >}} Stappen toevoegen {{< /AppElement >}}.
- [Alertberichten]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="nl" >}}) aanpassen voor verschillende alerttypen. Dit bericht bevat met welke derde partij of API contact moet worden gelegd, de inhoud van de HTTP-berichten, vereiste authenticatie en andere informatie.

![Aangepaste Voorgedefinieerde variabelen](/img/content/scr-service-now-integration-customization.min.png)

![Aangepaste stapdefinitie](/img/content/scr-service-now-integration-customization-steps.min.png)

8. (Optioneel) Selecteer op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} een operator of operatorgroep om [Integratierechten]({{< ref path="/support/kb/alerting/integrations/integrations-permissions" lang="nl" >}}) toe te voegen.

9. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.

10. Om uw configuratie te verifiëren test u uw aangepaste integratie met [testberichten]({{< ref path="/support/kb/alerting/integrations/custom-integrations/testing-your-custom-integration" lang="nl" >}}). Raadpleeg voor meer informatie het knowledgebase-artikel [Een testbericht versturen naar systemen van derden]({{< ref path="/support/kb/alerting/testing-alert-configurations#sending-a-test-message-to-third-party-systems" lang="nl" >}}).

Hiermee is de **ServiceNow**-integratieconfiguratie in Uptrends voltooid. U kunt deze integratie nu gebruiken en toevoegen aan uw [Alertdefinities]({{< ref path="support/kb/alerting/create-alert-definitions" lang="nl" >}}).

{{< callout >}}
**Tip:** Als u een integratiedefinitie deactiveert, wordt de integratie niet gebruikt voor alertingdoeleinden. Dit kan handig zijn als u het ontvangen van meldingen tijdelijk wilt uitschakelen.
{{< /callout >}}

Neem voor vragen of opmerkingen [contact op met ons Support team](/contact).
