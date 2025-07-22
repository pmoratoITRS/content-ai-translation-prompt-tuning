{
  "hero": {
    "title": "Wachtvoorwaarden gebruiken"
  },
  "title": "Wachtvoorwaarden gebruiken",
  "summary": "Bij het scripten van uw transacties moet u soms de controleregel instrueren dat hij moet wachten tot een specifiek element is geladen voordat hij verder gaat. Transactie monitoring ondersteunt drie types wachtvoorwaarden",
  "url": "/support/kb/synthetic-monitoring/transacties/wachtvoorwaarden-gebruiken",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-wait-conditions"
}

Het laden van een pagina kost tijd. Net zoals wanneer je moet wachten tot een pagina is geladen, moet het transactiescript soms ook wachten tot de pagina klaar is met laden voordat het verder kan met de volgende actie.

Het laden van een pagina is een beetje chaotisch omdat de browser het proces in fasen verdeelt, waarbij sommige elementen tegelijkertijd worden geladen terwijl andere elementen wachten tot later. Daarom kan het voor een script lastig zijn om bij te houden wanneer het welke actie kan uitvoeren. Het script moet wachten tot de browser de pagina-elementen laadt en deze elementen interactief worden voordat het script kan doorgaan met de volgende actie.

Vanwege het chaotische laadproces hebben de transactiecontroleregels van Uptrends een **Wacht tot** optie beschikbaar voor alle acties die interacteren met een specifiek element. Met de optie **Wacht tot** kunt u definiëren aan welke voorwaarde het aangegeven element moet voldoen voordat de transactie een actie uitvoert.

Momenteel heeft u de keuze uit drie verschillende **Wacht tot** voorwaarden.

![](/img/content/37df779f-b4a7-4e0e-bf9f-8bc1ca996396.png)

## Het element bestaat

De optie **Het element bestaat** controleert of het aangegeven element bestaat in de DOM van de pagina. Het feit dat een element bestaat, betekent niet noodzakelijkerwijs dat u met het element kunt communiceren, het betekent evenmin dat het element zichtbaar is op de pagina. Heel vaak bevat de DOM van een pagina elementen die de browser om een groot aantal mogelijke redenen niet weergeeft. Met de optie **Het element bestaat** kan de transactie proberen verder te gaan zodra het het aangegeven element in de DOM Document-node vindt.

## Het element is zichtbaar

De optie **Het element is zichtbaar** controleert of het element bestaat in de DOM Document-node en of het element zichtbaar is op de pagina. Een vervolgkeuzemenu kan bijvoorbeeld meerdere links bevatten die pas zichtbaar worden als u de cursor over een specifiek pagina-element beweegt (hovert). Aangezien deze links in het DOM aanwezig zijn voordat de hoveractie beschikbaar is, moet u de transactiecontroleregel vertellen dat hij moet wachten met interactie met de links tot de browser de links weergeeft.

## Het element is zowel zichtbaar als actief

De optie **Het element is zowel zichtbaar als actief** gedraagt zich hetzelfde als de optie **Het element is zichtbaar**, met één belangrijk verschil: het element moet niet alleen zichtbaar zijn op de pagina, het moet ook ingeschakeld zijn. De browser schakelt bijvoorbeeld bepaalde knoppen op sommige pagina's uit (vaak lichtgrijs weergegeven) tot de pagina aan een specifieke vereiste voldoet. De vereiste kan zijn dat de gebruiker een formulier moet invullen voordat hij de knop gebruikt. Daarom is het element zichtbaar op de pagina, maar u moet de transactiecontroleregel ook vertellen om te wachten tot de knop is ingeschakeld voordat deze een interactie probeert.

## Wat is een redelijke wachttijd?

De wachttijd die u instelt is de maximale tijd die uw controleregel wacht op een element. De standaard wachttijden zijn, tenzij anders aangegeven, 60 seconden voor navigatie en 30 seconden voor alle andere actietypes. Die standaardwaarden zijn meestal lang genoeg, dus tenzij u het nodig heeft, is het over het algemeen niet nodig om af te wijken van de standaardinstellingen. Als u deze wachttijden toch moet verlengen, kunt u dit doen in het veld **Wachttijd**. De maximale wachttijdwaarde voor elk actietype is 60 seconden. Aandachtspunten bij lange wachttijden:

-   Maak uw wachttijden niet te kort. Korte wachttijden kunnen veroorzaken dat uw controleregel fouten genereert. We raden aan om de wachttijden op de standaardinstelling te laten staan om ongewenste fouten te voorkomen.
-   De maximale runtime die Uptrends toestaat voor een transactiecontroleregel is vier minuten. Na vier minuten stopt de transactie. Hoewel de controleregel slechts zo lang wacht als nodig is tot de wachttijd die u hebt ingesteld, kunnen verlengde wachttijden ertoe leiden dat uw controleregel mislukt doordat de maximale runtime van vier minuten wordt overschreden.

{{< callout >}}
**Opmerking**: Over het algemeen hoeft u de standaardinstellingen voor de wachtvoorwaarden niet te wijzigen. Als u denkt dat u de wachtvoorwaarden moet aanpassen, [neem dan contact op met support]({{< ref path="contact" lang="nl" >}}) om u te helpen de wachtopties van uw controleregel te optimaliseren.
{{< /callout >}}
