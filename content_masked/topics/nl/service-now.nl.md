{
  "hero": {
    "title": "Ontvang websitemonitoring-alerts in ServiceNow"
  },
  "title": "ServiceNow-integratie",
  "summary": "Ontvang websitemonitoring-alerts van Uptrends in ServiceNow.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/service-now",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**ServiceNow** is een cloudgebaseerd platform waarmee u uw algemene Informatietechnologie (IT)-activiteiten kunt beheren via de verschillende ServiceNow-applicaties, waaronder Incidentmanagement.

Door **ServiceNow** te integreren met Uptrends worden automatisch incidenten gecreëerd die worden weergegeven in uw **ServiceNow**-account. Voor meer informatie over ServiceNow raadpleegt u de [ServiceNow Integrations-documentatie]([LINK_URL_1]) en [ServiceNow REST APIs]([LINK_URL_2]).

## De integratie configureren

Om integraties voor **ServiceNow** aan Uptrends toe te voegen, heeft u een ServiceNow-account nodig. Zorg ervoor dat u uw instance name en inloggegevens bij de hand heeft.

De integratie configureren:

1. Ga in de Uptrends-webapplicatie naar [SHORTCODE_3] Alerting > Integraties [SHORTCODE_4].
2. Klik in de rechter bovenhoek van uw scherm op de knop [SHORTCODE_5] Integratie toevoegen [SHORTCODE_6].
3. Selecteer in het pop-upvenster **ServiceNow** als het third party-integratietype.
4. Klik op de knop [SHORTCODE_7] Kiezen [SHORTCODE_8] om een nieuwe integratie te creëren.
5. **ServiceNow** is de standaardwaarde bij **Integratietype**. Geef de naam op van uw nieuwe integratie.
6. Vul in het gedeelte **Voorgedefinieerde variabelen** de volgende **Waarde**-velden in:

- [INLINE_CODE_1] — de instance name van uw ServiceNow. Deze kunt u identificeren via de ServiceNow-gebaseerde URL [INLINE_CODE_2].
- [INLINE_CODE_3] — de gebruikersnaam van uw ServiceNow-inlogaccount.
- [INLINE_CODE_4] — het wachtwoord van uw ServiceNow-inlogaccount.

U kunt ervoor kiezen om deze waarden op te geven als **Platte tekst** of door **Vault-inloggegevens** op te halen die zijn opgeslagen in de [Vault]([LINK_URL_3]). De integratie gebruikt automatisch basisauthenticatie om toegang te krijgen tot het **ServiceNow**-platform.

![ServiceNow Integratie]([LINK_URL_4])

7. (Optioneel) Om uw login en andere integratie-instellingen aan te passen, vinkt u het selectievakje **Integratie aanpassen** aan. Door aanpassen in te schakelen, kunt u:

- Bestaande **Voorgedefinieerde variabelen** toevoegen en bewerken om deze te gebruiken voor authenticatie, escalatieniveaus en stapdefinities.
- Stappen toevoegen en definiëren voor verschillende alerttypen. In de meeste gevallen is één HTTP-stap al voldoende voor uw configuratie. Als u afzonderlijke stappen nodig heeft voor andere scenario's, zoals authenticatie, klikt u op de knop [SHORTCODE_9] Stappen toevoegen [SHORTCODE_10].
- [Alertberichten]([LINK_URL_5]) aanpassen voor verschillende alerttypen. Dit bericht bevat met welke derde partij of API contact moet worden gelegd, de inhoud van de HTTP-berichten, vereiste authenticatie en andere informatie.

![Aangepaste Voorgedefinieerde variabelen]([LINK_URL_6])

![Aangepaste stapdefinitie]([LINK_URL_7])

8. (Optioneel) Selecteer op het tabblad [SHORTCODE_11] Gebruikersrechten [SHORTCODE_12] een operator of operatorgroep om [Integratierechten]([LINK_URL_8]) toe te voegen.

9. Klik op [SHORTCODE_13] Opslaan [SHORTCODE_14] om de wijzigingen te bevestigen.

10. Om uw configuratie te verifiëren test u uw aangepaste integratie met [testberichten]([LINK_URL_9]). Raadpleeg voor meer informatie het knowledgebase-artikel [Een testbericht versturen naar systemen van derden]([LINK_URL_10]).

Hiermee is de **ServiceNow**-integratieconfiguratie in Uptrends voltooid. U kunt deze integratie nu gebruiken en toevoegen aan uw [Alertdefinities]([LINK_URL_11]).

[SHORTCODE_1]
**Tip:** Als u een integratiedefinitie deactiveert, wordt de integratie niet gebruikt voor alertingdoeleinden. Dit kan handig zijn als u het ontvangen van meldingen tijdelijk wilt uitschakelen.
[SHORTCODE_2]

Neem voor vragen of opmerkingen [contact op met ons Support team]([LINK_URL_12]).
