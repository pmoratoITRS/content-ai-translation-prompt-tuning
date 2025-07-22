{
  "hero": {
    "title": "Overzicht monitorinstellingen"
  },
  "title": "Overzicht monitorinstellingen",
  "summary": "Elke controleregel heeft enkele algemene en meer specifieke instellingen (afhankelijk van het type controleregel). Bekijk welke instellingen beschikbaar zijn.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/overzicht-monitorinstellingen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-settings-overview",
  "sectionlist": false
}

## Toegang tot controleregelinstellingen

Uw controleregelinstellingen onderhouden:

1. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Zoek de naam van de controleregel waarvan u de instellingen wilt wijzigen en klik op de bijbehorende link in de kolom *Controleregelnaam*. Of typ in het filterzoekvak (een deel van) de naam, type, groep of URL van de controleregel om de resultaten te filteren.
    Het configuratiescherm van de controleregel verschijnt, met tabbladen die al uw controleregelinstellingen bevatten. Hieronder vindt u meer informatie over de verschillende tabbladen met instellingen.
3. Breng de benodigde wijzigingen aan op de tabbladen.
4. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen aan de controleregel op te slaan.

## Categorieën controleregelinstellingen

Verschillende controleregeltypes zijn bedoeld voor verschillende monitoringdoeleinden en niet alle instellingen zijn van toepassing op alle controleregels. Bekijk de instellingen die relevant zijn voor uw controleregel:
- Algemene instellingen
   - [Controle-interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="nl" >}})
   - [Dynamische waarden in URL's en POST-inhoud]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dynamic-date-notation-in-url-and-post-content" lang="nl" >}})
   - [Controleregelmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}})
   - [Controleregelnotities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="nl" >}})
   - [Controleregelsjablonen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="nl" >}})
- [Stappen (transactiecontroleregels)]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}})
- [Stappen (Multi-step-controleregels)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="nl" >}})
- [Foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}})
- Extra instellingen
   - [Browsertypes]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="nl" >}})
   - [Google Analytics blokkeren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="nl" >}})
   - [Bandbreedte begrenzen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling" lang="nl" >}})
   - [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="nl" >}})
- [Controlestations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="nl" >}})
- [Onderhoudsperiodes]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="nl" >}})
- [Lid van]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="nl" >}})
- [Gebruikersrechten]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}})

## Dashboard Controleregels beheren

Met alle controleregels ingesteld in uw Uptrends-webapplicatie, biedt het **Dashboard Controleregels beheren** u een beknopt overzicht om al uw controleregels en controleregelinstellingen op één plek te kunnen bekijken. Met dit dashboard kunt u de controleregelinstellingen in uw account bekijken, filteren en exporteren.

![Overzicht dashboard Controleregels beheren](/img/content/src_monitor-setup-dashboard-overview.min.png)

### Controleregelinstellingen bekijken
U kunt uw controleregelinstellingen eenvoudig visualiseren en controleren, waaronder:

- **Controleregelnaam** - specificeert de naam van uw controleregelconfiguratie en het aantal gebruikte [credits]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}). Een pictogram van een kegelvormige fles geeft aan dat uw controleregel zich in *Staging*-modus bevindt, terwijl het moersleutelpictogram aangeeft dat uw controleregel zich in *Development* [modus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}}) bevindt.
- **Dashboard controleregel** - bevat een *Ga naar het dashboard*-link waarmee u naar het specifieke controleregeldashboard gaat.
- **Type controleregel** - specificeert het [type controleregel]({{< ref path="/support/kb/basics/monitor-types" lang="nl" >}}) dat momenteel is ingesteld (bijvoorbeeld Transactie- en Multi-step API-controleregels).
- **Controle-interval (minuten)** - specificeert hoe vaak uw controleregel wordt uitgevoerd.
- **URL / Netwerkadres** - specificeert het browseradres of het IP-adres van de website die u momenteel monitort.
- **Actief** - specificeert of uw controleregel is ingeschakeld of uitgeschakeld. U ziet *Ja* als de controleregel ingeschakeld en actief is, anders ziet u *Nee*. Ingeschakelde en uitgeschakelde controleregels geven tussen haakjes ook de huidige [modus]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="nl" >}}) van uw controleregel weer, of het nu *Staging* of *Development* is.
- **Gemaakt op** - toont de datum en tijd waarop u de controleregel heeft gemaakt.
- **Laatst gewijzigd op** - toont de datum en tijd waarop u voor het laatst uw controleregel heeft bijgewerkt of wijzigingen in uw controleregel heeft opgeslagen.  
- **Lid van groepen** - specificeert tot welke controleregelgroep(en) uw controleregel behoort.

### Controleregelinstellingen filteren

Om uw hoeveelheid controleregels eenvoudig te verkleinen, gaat u naar het filtertekstveld en past u de lijst aan op basis van de controleregelnaam, type, groep en URL. U kunt ook filteren op controleregelmodi door de selectievakjes *Development, Staging en Production* aan te vinken.

### Controleregelinstellingen exporteren

Aangezien het **Dashboard Controleregels beheren** nuttig is bij het visualiseren en groeperen van uw algehele controleregelinstellingen, kunt u deze informatie ook exporteren voor beter inzicht en later gebruik. In dit [knowledgebase-artikel]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="nl" >}}) vindt u stapsgewijze aanwijzingen voor het exporteren van uw dashboards.

Nadat u uw data in het gewenste formaat heeft geëxporteerd, kunt u de details van uw controleregelinstellingen bekijken zoals beschreven in het vorige gedeelte, [Dashboard Controleregels beheren]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-setup" lang="en" >}}). U vindt hierin extra kolommen, waaronder:

- **Alert op tijdlimieten** - toont de [laad- en uitvoertijd]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})-instellingen van uw controleregel, waarbij wordt aangegeven of de foutconditie is ingesteld op *alleen met kleurcode weergeven* van het resultaat of *fout genereren*.
- **Tijdlimieten** - toont de bijbehorende [tijdlimieten in milliseconden]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}}) van uw controleregel (geconfigureerd en gerelateerd aan de alert bij tijdlimietinstellingen).
- **Notities** - toont de inhoud van het veld *Notities*.