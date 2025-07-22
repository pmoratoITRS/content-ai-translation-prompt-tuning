{
  "hero": {
    "title": "Multi-step monitoring Assertions"
  },
  "title": "Multi-step monitoring Assertions",
  "summary": "Assertions in Multi-step API monitoring begrijpen.",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In de [inleiding tot multi-step monitoring]([LINK_URL_1]) wordt beschreven dat u met behulp van assertions de inhoud van uw HTTP-responses kunt controleren, zodat u correct gedrag en performancelimieten van uw API's in de gaten kunt houden. In dit gedeelte worden de mogelijkheden van de assertion gedetailleerd uitgelegd.

Elke assertion wordt op de volgende manier gedefinieerd:

[SHORTCODE_1]Source[SHORTCODE_2] [SHORTCODE_3]property[SHORTCODE_4] [SHORTCODE_5]comparison[SHORTCODE_6] [SHORTCODE_7]target value[SHORTCODE_8] 

bijvoorbeeld:

[SHORTCODE_9]Response body as JSON[SHORTCODE_10] [SHORTCODE_11]Products\[0\].Price[SHORTCODE_12] [SHORTCODE_13]Is greater than[SHORTCODE_14] [SHORTCODE_15]100[SHORTCODE_16] 

-   De **assertion source**: dit veld definieert welk kenmerk van de HTTP-respons u wilt controleren. [Alle beschikbare opties worden beschreven in dit artikel ]([LINK_URL_2]).
-   De **assertion property**: voor sommige assertion source-opties (met name de contentcontrole en aan de header gerelateerde opties) moet u verder specificeren welke content van de header moet worden gecontroleerd. Dit wordt [uitgebreider uitgelegd]([LINK_URL_3]) voor elk geschikt sourcetype.
-   De **assertion vergelijking**: dit veld geeft het type controle aan dat we zouden moeten uitvoeren. Standaard doen we een *X is gelijk aan Y*-vergelijking, maar er zijn veel meer vergelijkingsopties voor tekst en getallen. [Zie de lijst met vergelijkingsopties]([LINK_URL_4]).
-   De **assertion target value**: voor de meeste assertions wilt u een vergelijking uitvoeren met een bepaalde waarde die u opgeeft. Die waarde is de doelwaarde. Afhankelijk van welke assertion source u gebruikt en het type vergelijking dat u uitvoert, kan deze waarde een tekstwaarde, een numerieke waarde of zelfs een booleaanse waarde (waar of onwaar) zijn. U kunt ook een [verwijzing naar een variabele]([LINK_URL_5]) invoeren die een van deze waarden vertegenwoordigt.

## Wat gebeurt er als niet aan een assertionvoorwaarde wordt voldaan?

Alle assertions (aannames) in een stap worden uitgevoerd zodra de HTTP-request is uitgevoerd en de respons is verwerkt. In de regel wordt elke assertion voor die stap geëvalueerd, zelfs als een eerdere assertion niet slaagt. Dit betekent dat het mogelijk is dat meerdere assertions een fout voor één stap melden.

Als een of meer assertions mislukken, stopt de uitvoering van de controleregel onmiddellijk. Alle volgende stappen worden niet uitgevoerd en de controleregel zal een een fout rapporteren. De foutcode en beschrijving zijn afhankelijk van het fouttype. Als meerdere assertions mislukken, wordt de eerste in de lijst als de belangrijkste beschouwd.

Soms kan het nodig zijn om de uitvoering van een assertion nog een keer te proberen, bijvoorbeeld omdat u weet dat er een timingprobleem kan zijn dat tot een vals-negatief resultaat leidt. Het is mogelijk de assertion herhaaldelijk te evalueren en de details worden uitgelegd in [Opnieuw proberen tot het gelukt is]([LINK_URL_6]).
