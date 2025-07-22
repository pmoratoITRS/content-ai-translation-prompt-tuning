{
  "hero": {
    "title": "Foutcondities - W3C-kengetallen controleren"
  },
  "title": "Foutcondities - W3C-kengetallen controleren",
  "summary": "Grenswaarden gebruiken op W3C-kengetallen om fouten te activeren.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-w3c",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-w3c"
}

Het World Wide Web Consortium (of kortweg W3C) is een internationale organisatie die zich bezighoudt met het ontwikkelen van standaarden voor het wereldwijde web. Als zodanig heeft het een standaard gedefinieerd voor browsers en webapplicaties om timinginformatie over het laden van webpagina's te genereren en weer te geven. 

De controleregeltypes die gebruikmaken van een [browsertype met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}) meten en rapporteren de [W3C-kengetallen voor navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="nl" >}}). Deze kengetallen worden gerapporteerd in de Details van de controle van de controleregel en u kunt er foutcondities voor instellen. Condities voor W3C-kengetallen maken deel uit van de [Foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}). 

Houd er rekening mee dat verschillende controleregeltypes verschillende foutcondities bieden. Bekijk de tabel in [Welke foutcondities zijn beschikbaar?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="nl" >}}) om te achterhalen welke opties beschikbaar zijn voor bepaalde controleregeltypes.

## Foutcondities definiëren op basis van de W3C-kengetallen

Om foutcondities te definiëren die de W3C-navigatietiming gebruiken:

1. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de naam van de controleregel om deze te bewerken.
3. Open het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}}.
4. Vouw de categorie *W3C-kengetallen controleren* uit door op de pijl ervoor te klikken.
 
   ![screenshot foutconditie w3c-kengetallen](/img/content/scr_errorconditions-w3cmetrics.min.png)

5. Schakel foutcondities in door het selectievakje aan te vinken en een waarde in te stellen. Laat alle kengetallen uitgeschakeld die u niet aan een foutconditie wilt toewijzen.
6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}}.

## De W3C-kengetallen {id="w3c-metrics"}

De W3C-kengetallen die worden gemeten door controleregels met het [browsertype met extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}) worden uitgelegd in het Knowledge Base-artikel [Kengetallen voor W3C-navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="nl" >}}). De kengetallen komen overeen met de foutcondities in de categorie *W3C-kengetallen controleren*. Het enige kengetal dat niet aanwezig is in die lijst met foutcondities is de Load event. In [Foutconditie load event]({{< ref path="#load-event" lang="nl" >}}) hieronder leest u hoe u een foutconditie voor dat kengetal instelt.

## Foutconditie load event {id="load-event"}

Mogelijk mist u het W3C-kengetal load event in de categorie *W3C-kengetallen controleren* van de foutcondities. Als u een foutconditie voor dit kengetal wilt instellen, kunt u dit doen voor [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="nl" >}}) controleregels. Doe het volgende:

1. Open de controleregelinstellingen.
2. Zorg ervoor dat u op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} het **Browsertype** *Chrome met extra kengetallen* heeft gekozen.
3. Op het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} in het gedeelte *Meting* stelt u de **Laadtijd baseren op** in op *W3C load event*.
4. Stel op het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}} grenswaarden in voor **Laadtijd van de pagina controleren**.

Het Knowledge Base-artikel [Foutcondities - Paginalaadtijd]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}}) bevat meer informatie over het instellen van grenswaarden voor laadtijden.
