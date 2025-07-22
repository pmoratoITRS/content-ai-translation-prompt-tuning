{
  "hero": {
    "title": "Alertdefinities creëren"
  },
  "title": "Alertdefinities creëren",
  "summary": "In dit artikel vindt u uitleg over hoe u alerts voor de beschikbaarheid en performance van uw website definieert, zodat u alleen wordt gewaarschuwd wanneer u dat wilt.",
  "url": "/support/kb/alerting/alertdefinities-creeren",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/create-alert-definitions"
}

Een alertdefinitie geeft aan hoe en naar wie een alert moet worden gestuurd door gebruik te maken van escalatieniveaus. Voordat een alertdefinitie werkt (zoals gewenst), moet u [foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}), instellen, dit zijn de regels die een alert activeren.

Een [escalatieniveau]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="nl" >}}) bevat een reeks parameters voor het genereren van alerts, aantal herinneringen, meldingsmethode en wie deze zal ontvangen.

{{< callout >}}
**Opmerking**: Er is al een standaard alertdefinitie geconfigureerd in uw Uptrends-account. U kunt de regels daarvan wijzigen of uw eigen alertdefinitie creëren.
{{< /callout >}}

## Een alertdefinitie creëren

Om een aangepaste alertdefinitie te configureren:

1. Ga naar het menu {{< AppElement type="menuitem" >}} Alerting > Alertdefinities {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="button" >}}Alertdefinitie toevoegen{{< /AppElement >}}.
3. Voer een naam in voor de alertdefinitie.
3. Schakel het selectievakje **Actief** in om de alert in te schakelen.
4. Kies de controleregels waarop de alertdefinitie van toepassing is.
5. Stel uw escalatieniveaus in, zie het artikel over [escalatieniveaus]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="nl" >}}) voor uitgebreide informatie.
6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}}.

U heeft zojuist uw eigen alertdefinitie gemaakt! Deze wordt nu weergegeven in het **dashboard Alertdefinities** wanneer u navigeert naar {{< AppElement type="menuitem" >}} Alerting > Alertdefinities {{< /AppElement >}}.

## Dashboard Alertdefinities

Het **dashboard Alertdefinities** toont een samenvattend overzicht om al uw alertdefinities op één plek te zien. U kunt uw alertdefinitie-instellingen eenvoudig visualiseren en controleren, waaronder:

- **Naam** - specificeert de naam van uw alertdefinitieset-up.
- **Actieve escalatieniveaus** - specificeert het aantal actieve of ingeschakelde escalatieniveaus. Momenteel is het minimum aantal escalatieniveaus 0 en het maximum is 3. Alle inactieve escalatieniveaus genereren geen alerts.
- **Actief** - specificeert de status van uw alertdefinitie. U ziet *Ja* als de alertdefinitie actief is, anders ziet u *Nee*.

Alle Uptrends-dashboards kunnen worden geëxporteerd voor betere monitoringinzichten en toekomstige raadpleging. In dit [artikel]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="nl" >}}) vindt u het stapsgewijze proces voor het exporteren van uw dashboards.

Zodra u uw data succesvol in het gewenste formaat heeft geëxporteerd, kunt u aanvullende details zien naast de instellingen voor de alertdefinitie die in de eerste alinea van deze sectie worden genoemd. Extra kolommen met informatie zijn als volgt:

- **Controleregels** - specificeert welke controleregel(s) de alertdefinitie gebruikt.
- **Controleregelgroepen** - specificeert welke controleregelgroep(en) de alertdefinitie gebruikt.
- **Is de alertdefinitie actief?** - toont *Ja* als de alertdefinitie ingeschakeld en actief is, anders *Nee*.
- **Is het escalatieniveau n actief?** - toont *Ja* als het escalatieniveau ingeschakeld en actief is, anders *Nee*.
- **Operators voor escalatieniveau n** - specificeert welke operators zijn toegewezen voor elk escalatieniveau.
- **Operatorgroepen voor escalatieniveau n** - specificeert welke operatorgroepen zijn toegewezen voor elk escalatieniveau.
- **Integraties voor escalatieniveau n** - specificeert het type integratie of op welk platform u uw alerts voor elk escalatieniveau ontvangt. Integraties kunnen zijn: *Alerting via e-mail, Alerting via SMS, Alerting via telefoon* of [aanpasbare integraties]({{< ref path="/support/kb/alerting/integrations" lang="nl" >}}).

{{< callout >}}
Aangezien Uptrends drie escalatieniveaus heeft, verwijst de **n** naar het nummer dat overeenkomt met het alertescalatieniveau dat u heeft ingesteld in het configuratiescherm van de alertdefinitie.
{{< /callout >}}