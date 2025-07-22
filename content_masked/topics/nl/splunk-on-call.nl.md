{
  "hero": {
    "title": "Ontvang monitoringalerts in Splunk On-Call"
  },
  "title": "Splunk On-Call-integration",
  "summary": "Ontvang websitemonitoring-alerts van Uptrends in Splunk On-Call.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/splunk-on-call",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Splunk On-Call** is een incidentmanagementplatform dat DevOps-teams helpt om samen te werken en incidenten effectief op te lossen. U kunt uw team organiseren voor on-call-planning, incidentescalaties en hen in een mum van tijd op de hoogte stellen wanneer er problemen zijn die onmiddellijke aandacht vereisen. 

Integratie van Splunk On-Call met Uptrends creëert automatisch incidenten die worden weergegeven in uw Splunk On-Call-dashboard. Volg de volgende stappen voor het configureren van de integratie tussen beide systemen:

## 1. Configureer uw REST-integratie in Splunk On-Call.
1. Log in op uw Splunk On-Call-account.
2. Klik in het tabblad [SHORTCODE_5]Integrations[SHORTCODE_6] op de REST-integratie die standaard al is ingeschakeld. Raadpleeg voor meer informatie de Splunk On-Call [REST Integration]([LINK_URL_1]). 
3. Kopieer de *URL to notify* zonder de waarde */$routing_key* en sla deze op voor later gebruik.

## 2. Configureer de integratie in Uptrends
1. Ga naar uw Uptrends-account en ga naar het menu [SHORTCODE_7]Alerting > Integraties [SHORTCODE_8].
2. Klik in de rechterbovenhoek van uw scherm op de knop [SHORTCODE_9]Integratie toevoegen[SHORTCODE_10].
3. Er verschijnt een pop-upvenster, selecteer *Splunk On-Call* als het integratietype.
4. Klik op de knop [SHORTCODE_11]Kiezen[SHORTCODE_12].
5. U kunt nu de details voor uw integratieconfiguratie bewerken. Geef uw nieuwe integratie een naam.
6. Standaard is het veld [SHORTCODE_13]Integratie aanpassen[SHORTCODE_14] uitgeschakeld. Vink het selectievakje aan om aanpassing in te schakelen en de standaard integratie-instellingen voor Splunk On-Call aan te passen. Anders kunt u het laten zoals het is. 

[SHORTCODE_1]
**Opmerking:** Wanneer u [SHORTCODE_15]Integratie aanpassen[SHORTCODE_16] inschakelt, verschijnt het tabblad [SHORTCODE_17]Aanpassingen[SHORTCODE_18]. Hier kunt u opgeven welke berichten worden verzonden wanneer een alert is gegenereerd, waaronder naar derden of API's, inhoud van HTTP-berichten of vereiste authenticatie enzovoort.

In de meeste gevallen is één enkele HTTP-stap voldoende. Het is echter mogelijk om meer stappen toe te voegen als u afzonderlijke stappen voor authenticatie nodig heeft. Daarnaast kunt u ervoor kiezen om afzonderlijke stappen te definiëren voor afzonderlijke alerttypes. Dit is handig als uw foutberichten moeten verschillen van uw OK-berichten (voor opgeloste alerts). Raadpleeg onze [knowledgebase-artikelen over integraties]([LINK_URL_2]) voor meer informatie.
[SHORTCODE_2]


7. In het gedeelte Voorgedefinieerde variabelen ziet u de naam *SplunkOnCallUrl*. Kies welke waarde u wilt opgeven in het keuzemenu. U kunt bijvoorbeeld de optie *Waarde hier opgeven* kiezen.
8. Klik op de drie stippen naast het menu *SplunkOnCallUrl*. Er verschijnt een pop-upvenster en u kunt kiezen uit twee opties. U kunt de waarde van de *URL om te melden* die u eerder heeft opgeslagen, plakken in het veld Platte tekst of een gebruikersnaam of wachtwoord kiezen voor [vault-inloggegevens]([LINK_URL_3]) (indien van toepassing).
9. Klik op de knop [SHORTCODE_19]Selecteren[SHORTCODE_20].
10. Geef vervolgens de waarde op van de *RoutingKey* die u wilt gebruiken. [Routing keys]([LINK_URL_4]) vindt u op het tabblad [SHORTCODE_21] Settings [SHORTCODE_22] in uw Splunk On-call-account. 
11. Klik op [SHORTCODE_23]Opslaan[SHORTCODE_24] om de integratie-instellingen te bevestigen.

Hiermee is de integratieconfiguratie in Uptrends voltooid. U kunt deze integratie nu gebruiken en toevoegen aan uw [alertdefinities]([LINK_URL_5]).

**Dat is alles!** U heeft de Splunk On-Call-integratie succesvol geconfigureerd.

Wat krijgt u wanneer deze integratie is geconfigureerd? Bekijk hieronder een voorbeeld van hoe de integratie eruitziet in uw Splunk On-Call-dashboard. 
![Splunk On-Call-dashboard met Uptrends-integratie]([LINK_URL_6])

[SHORTCODE_3]
**Tip:** Als u een integratiedefinitie deactiveert, wordt de integratie niet gebruikt voor alertingdoeleinden. Dit kan handig zijn als u het ontvangen van alerts tijdelijk wilt uitschakelen.
[SHORTCODE_4]

Mocht u nog vragen hebben, neem dan gerust [contact op met ons supportteam]([LINK_URL_7]).
