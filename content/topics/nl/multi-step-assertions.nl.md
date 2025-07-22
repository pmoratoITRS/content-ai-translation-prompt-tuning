{
  "hero": {
    "title": "Multi-step monitoring Assertions"
  },
  "title": "Multi-step monitoring Assertions",
  "summary": "Assertions in Multi-step API monitoring begrijpen.",
  "url": "support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-assertions"
}

In de [inleiding tot multi-step monitoring](/support/kb/synthetic-monitoring/api-monitoring/multi-step) wordt beschreven dat u met behulp van assertions de inhoud van uw HTTP-responses kunt controleren, zodat u correct gedrag en performancelimieten van uw API's in de gaten kunt houden. In dit gedeelte worden de mogelijkheden van de assertion gedetailleerd uitgelegd.

Elke assertion wordt op de volgende manier gedefinieerd:

{{< Code/Symbol type="source" >}}Source{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}property{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}comparison{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}target value{{< /Code/Symbol >}} 

bijvoorbeeld:

{{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products\[0\].Price{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is greater than{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}100{{< /Code/Symbol >}} 

-   De **assertion source**: dit veld definieert welk kenmerk van de HTTP-respons u wilt controleren. [Alle beschikbare opties worden beschreven in dit artikel ](/support/kb/synthetic-monitoring/api-monitoring/multi-step-bronnen).
-   De **assertion property**: voor sommige assertion source-opties (met name de contentcontrole en aan de header gerelateerde opties) moet u verder specificeren welke content van de header moet worden gecontroleerd. Dit wordt [uitgebreider uitgelegd](/support/kb/synthetic-monitoring/api-monitoring/multi-step-bronnen) voor elk geschikt sourcetype.
-   De **assertion vergelijking**: dit veld geeft het type controle aan dat we zouden moeten uitvoeren. Standaard doen we een *X is gelijk aan Y*-vergelijking, maar er zijn veel meer vergelijkingsopties voor tekst en getallen. [Zie de lijst met vergelijkingsopties](/support/kb/synthetic-monitoring/api-monitoring/vergelijkingsoperatoren-in-multi-step-monitoring).
-   De **assertion target value**: voor de meeste assertions wilt u een vergelijking uitvoeren met een bepaalde waarde die u opgeeft. Die waarde is de doelwaarde. Afhankelijk van welke assertion source u gebruikt en het type vergelijking dat u uitvoert, kan deze waarde een tekstwaarde, een numerieke waarde of zelfs een booleaanse waarde (waar of onwaar) zijn. U kunt ook een [verwijzing naar een variabele](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variabelen) invoeren die een van deze waarden vertegenwoordigt.

## Wat gebeurt er als niet aan een assertionvoorwaarde wordt voldaan?

Alle assertions (aannames) in een stap worden uitgevoerd zodra de HTTP-request is uitgevoerd en de respons is verwerkt. In de regel wordt elke assertion voor die stap geëvalueerd, zelfs als een eerdere assertion niet slaagt. Dit betekent dat het mogelijk is dat meerdere assertions een fout voor één stap melden.

Als een of meer assertions mislukken, stopt de uitvoering van de controleregel onmiddellijk. Alle volgende stappen worden niet uitgevoerd en de controleregel zal een een fout rapporteren. De foutcode en beschrijving zijn afhankelijk van het fouttype. Als meerdere assertions mislukken, wordt de eerste in de lijst als de belangrijkste beschouwd.

Soms kan het nodig zijn om de uitvoering van een assertion nog een keer te proberen, bijvoorbeeld omdat u weet dat er een timingprobleem kan zijn dat tot een vals-negatief resultaat leidt. Het is mogelijk de assertion herhaaldelijk te evalueren en de details worden uitgelegd in [Opnieuw proberen tot het gelukt is]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step#msaretry" lang="nl" >}}).
