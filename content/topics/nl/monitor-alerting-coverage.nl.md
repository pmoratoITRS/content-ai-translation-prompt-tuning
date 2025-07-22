{
  "hero": {
    "title": "Controleregels gedekt door alerting"
  },
  "title": "Controleregels gedekt door alerting",
  "summary": "Overzicht van alle controleregels met informatie over waarom de controleregel wel of niet gedekt is door alerting",
  "url": "/support/kb/alerting/controleregels-gedekt-door-alerting",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/monitor-alerting-coverage",
  "tableofcontents": false
}

Het overzicht [Dekking alerting]({{< AppUrl >}}/Report/AlertingCoverage) is een lijst van uw controleregels, die laat zien of ze worden gedekt door alertdefinities en u gedetailleerde informatie geeft over waarom dit niet het geval zou kunnen zijn.

{{< callout >}} **Opmerking**: De **Controleregels gedekt door alerting** houdt rekening met uw gebruikersrechten om u een gepersonaliseerde weergave te geven. Deze zal alleen alertdefinities tonen waarvoor u bewerkingsrecht heeft. Dit betekent voor het Uptrends-account in het algemeen dat er een controleregel kan zijn die wordt gedekt door een alertdefinitie en alerts verstuurt, maar toch in het overzicht als niet gedekt verschijnt omdat u geen toegangsrechten heeft voor de alertdefinitie. {{< /callout >}}

Als u controleregels heeft waarvan u verwacht dat ze alerts genereren, maar dat niet doen of dat wel doen terwijl ze dat niet zouden moeten doen, is dit de plek waar u kunt beginnen met het oplossen van problemen.

Om het overzicht te openen gaat u naar {{< AppElement type="menuitem" >}}Alerting > Alerting verkennen{{< /AppElement >}} en dan klikt u op de statistiek 'Controleregels in productie gedekt door alerting'.

![screenshot van statistiek controleregels gedekt door alerting](/img/content/scr-alerting_hub-statistic_monitor_coverage.min.png)

Het overzicht *Dekking alerting* verschijnt en de controleregels die niet door alerting worden gedekt, worden boven aan de lijst weergegeven met een rode arcering.

![screenshot van overzicht dekking alerting](/img/content/scr-monitor-alerting-coverage-overview.min.png)

Waarom zijn die controleregels niet gedekt?
Er zijn een aantal voorwaarden voor dekking door alerting:

- De controleregel zelf is actief.
- Alerts versturen voor de controleregel is actief.
- Er is minimaal één actieve alertdefinitie gekoppeld aan de controleregel (rechtstreeks of via een controleregelgroep). 
- Binnen de actieve alertdefinitie moet minimaal één escalatieniveau actief zijn.

Controleer de lijst op een 'Nee' of 'inactief' (alertdefinities) om te achterhalen aan welke voorwaarde niet wordt voldaan. 
