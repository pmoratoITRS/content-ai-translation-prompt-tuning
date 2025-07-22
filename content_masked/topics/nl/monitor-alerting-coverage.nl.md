{
  "hero": {
    "title": "Controleregels gedekt door alerting"
  },
  "title": "Controleregels gedekt door alerting",
  "summary": "Overzicht van alle controleregels met informatie over waarom de controleregel wel of niet gedekt is door alerting",
  "url": "[URL_BASE_TOPICS]alerting/controleregels-gedekt-door-alerting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Het overzicht [Dekking alerting]([LINK_URL_1]) is een lijst van uw controleregels, die laat zien of ze worden gedekt door alertdefinities en u gedetailleerde informatie geeft over waarom dit niet het geval zou kunnen zijn.

[SHORTCODE_1] **Opmerking**: De **Controleregels gedekt door alerting** houdt rekening met uw gebruikersrechten om u een gepersonaliseerde weergave te geven. Deze zal alleen alertdefinities tonen waarvoor u bewerkingsrecht heeft. Dit betekent voor het Uptrends-account in het algemeen dat er een controleregel kan zijn die wordt gedekt door een alertdefinitie en alerts verstuurt, maar toch in het overzicht als niet gedekt verschijnt omdat u geen toegangsrechten heeft voor de alertdefinitie. [SHORTCODE_2]

Als u controleregels heeft waarvan u verwacht dat ze alerts genereren, maar dat niet doen of dat wel doen terwijl ze dat niet zouden moeten doen, is dit de plek waar u kunt beginnen met het oplossen van problemen.

Om het overzicht te openen gaat u naar [SHORTCODE_3]Alerting > Alerting verkennen[SHORTCODE_4] en dan klikt u op de statistiek 'Controleregels in productie gedekt door alerting'.

![screenshot van statistiek controleregels gedekt door alerting]([LINK_URL_2])

Het overzicht *Dekking alerting* verschijnt en de controleregels die niet door alerting worden gedekt, worden boven aan de lijst weergegeven met een rode arcering.

![screenshot van overzicht dekking alerting]([LINK_URL_3])

Waarom zijn die controleregels niet gedekt?
Er zijn een aantal voorwaarden voor dekking door alerting:

- De controleregel zelf is actief.
- Alerts versturen voor de controleregel is actief.
- Er is minimaal één actieve alertdefinitie gekoppeld aan de controleregel (rechtstreeks of via een controleregelgroep). 
- Binnen de actieve alertdefinitie moet minimaal één escalatieniveau actief zijn.

Controleer de lijst op een 'Nee' of 'inactief' (alertdefinities) om te achterhalen aan welke voorwaarde niet wordt voldaan. 
