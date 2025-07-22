{
  "hero": {
    "title": "Uw monitoringdata weergeven in Grafana"
  },
  "title": "Grafana-integratie",
  "summary": "Een handleiding voor het weergeven van uw monitoringdata in Grafana.",
  "url": "/support/kb/dashboards-en-rapportages/grafana",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/grafana"
}

Met de Uptrends Grafana-databron kan informatie over de status en statistieken die worden gerapporteerd door Uptrends’ controleregels en controleregelgroepen worden weergegeven binnen een Grafana-omgeving. Deze maakt gebruik van de Uptrends API om statistische data, of data over de huidige status, op te halen voor uw controleregels en controleregelgroepen. 

In deze handleiding wordt beschreven hoe u een eenvoudige Grafana-instance instelt die verbinding kan maken met en data kan ophalen uit Uptrends, zodat deze kunnen worden weergegeven in uw Grafana-omgeving. Als u problemen tegenkomt, vragen heeft of feedback wilt geven, neem dan [contact met ons op]({{< ref path="/contact" lang="nl" >}}). 

## Vereisten
- Een actief Uptrends-account.
- Een set Uptrends APIv4-inloggegevens: in deze handleiding wordt uitgelegd hoe u deze kunt genereren.
- Een Grafana-instance met toegang tot de serverconfiguratie.

## Pre-configuratie

### Een Uptrends APIv4-account creëren

{{< callout >}} **Opmerking**: Als u al een set APIv4-inloggegevens beschikbaar heeft, kunt u die gebruiken en deze stap overslaan. {{< /callout >}}

Grafana communiceert met Uptrends via de API (versie 4 - zie de [API-documentatie]({{< ref path="/support/kb/api" lang="nl" >}}) voor meer informatie) door de relevante informatie op te vragen en deze vervolgens weer te geven in uw Grafana-dashboards. Om die requests te kunnen doen, moet Grafana toegang hebben tot een geregistreerd API-account. U kunt een API-account creëren door de instructies te volgen in het artikel [Operator API accountbeheer]({{< ref path="/support/kb/account/users/operators/operator-API-management" lang="nl" >}}).

Het resultaat van de stappen die in dat artikel worden beschreven, zijn een gebruikersnaam en wachtwoord. Noteer deze, want u moet ze straks aan de databron in Grafana toevoegen. 

Een API-account is verbonden met een operator in Uptrends. Zorg ervoor dat de operator ten minste het [gebruikersrecht *Controleregelgegevens in groep bekijken*]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}}) heeft voor elk van de controleregels of controleregelgroepen die u in Grafana wilt weergeven. 

## De plug-in installeren

1. **Download de plug-in —** de actuele versie van de Uptrends Grafana plug-in is [versie 0.9.274](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana.0.9.274.zip). U kunt het nieuwste zip-bestand downloaden via deze [link](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana_latest.zip).
2. **Pak de .zip uit en kopieer de inhoud naar de Grafana plugin directory —** de standaardlocatie voor de plugin directory is `/var/lib/grafana/plugins`. Raadpleeg de Grafana-documentatie voor meer informatie.
3. **Schakel de plug-in in —** de plug-in is momenteel niet ondertekend, wat betekent dat deze expliciet moet worden ingeschakeld binnen de Grafana-configuratie. Om de plug-in in te schakelen doet u het volgende:

    - Zoek op de server die uw Grafana-instance host, *grafana.ini* (de standaardlocatie is `/etc/grafana/grafana.ini`) en open het bestand met de bestandseditor van uw voorkeur.
    - Zoek onder `[plugins]` (mogelijk moet u behoorlijk ver naar beneden scrollen of een zoekfunctie gebruiken) de key `allow_loading_unsigned_plugins`. 
    - Voeg de waarde `uptrends-uptrends-plugin` toe aan de opdracht `allow_loading_unsigned_plugins`.

![Niet-ondertekende plug-in toestaan](/img/content/scr-grafana-allow-unsigned-plugins.min.png)

4. **Herstart Grafana —** de plug-in zou nu beschikbaar moeten zijn voor gebruik in de Grafana-interface.

## De databron creëren
1. Ga in uw Grafana-interface naar _Configuration_ (het tandwielpictogram in het linkermenu) -> _Data sources_.
2. Klik op _Add data source_.
3. Filter op _Uptrends_ en klik op de resulterende plug-in (deze zou `uptrends-plugin` moeten heten).
4. Voer de APIv4-gebruikersnaam en -wachtwoord in die u in de eerste stap van deze handleiding heeft gegenereerd, of gebruik een bestaande set inloggegevens.
5. Klik op _Save & test_.

![Databron creëren](/img/content/scr-grafana-plugin-config.min.png)

### Creëer een dashboard

Nu de databron is ingesteld, kan deze beginnen met het ophalen van data uit Uptrends en Grafana-dashboards vullen met deze data. 

1. Ga naar *Dashboards > New dashboard*, of bewerk een bestaand dashboard.
2. Klik op *Add a new panel*.

![Een paneel bewerken](/img/content/scr-grafana-edit-panel.min.png)

3. Controleer dat de juiste databron (genaamd `uptrends-plugin`) is geselecteerd als de **Data source** van het paneel.
4. Kies een paneeltype in de rechter bovenhoek en vul eventuele andere opties in het rechtermenu in.
5. Kies de data die u wilt weergeven. 

    \- U kunt kiezen tussen controleregelstatusdata (gerelateerd aan de huidige fout/ok-status van uw controleregels) of controleregelstatistieken (gerelateerd aan controleregelperformance in de loop van de tijd).

    \- U kunt filteren op een specifieke controleregel of controleregelgroep per query die u toevoegt. De lijsten met controleregels en controleregelgroepen worden automatisch gevuld. 

  ![Uptrends-data selecteren om in het paneel weer te geven](/img/content/scr-grafana-populating-panel.min.png)

6. Klik op *Apply* in de rechter bovenhoek. 

De bovenstaande handleiding is een zeer eenvoudige beschrijving van het ophalen van Uptrends-data in Grafana. Als volledig product ondersteunt Grafana vele extra opties.
