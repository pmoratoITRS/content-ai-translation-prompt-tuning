{
  "hero": {
    "title": "Foutafhandeling in Multi-step API's"
  },
  "title": "Foutafhandeling in Multi-step API's",
  "summary": "Weet hoe u fouten in een Multi-step API-controleregel kunt afhandelen en negeren.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-foutafhandeling",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Er kunnen zich situaties voordoen waarin u onverwacht en dynamisch webservergedrag tegenkomt bij het testen van uw Multi-Step API (MSA)-controleregels of wanneer een controleregel checks uitvoert. Sommige van deze gedragingen zijn request timeouts en mislukte assertions die voorkomen dat uw controleregels andere requests ontvangen.

U heeft bijvoorbeeld een MSA-controleregel ingesteld om informatie op te halen van een e-commerceplatform. Deze controleregel bevat vier /GET request-stappen die als volgt zijn gerangschikt:

1. GET /product — retourneert alle producten en hun informatie.
2. GET /products/{productID} — retourneert een specifiek product en de bijbehorende informatie.
3. GET /users — retourneert alle gebruikers en hun informatie.
4. GET /users/{userID} — retourneert een specifieke gebruiker en zijn informatie.

De bovenstaande configuratie laat zien dat stap één en twee productgegevens ophalen, terwijl stap drie en vier gebruikersgegevens ophalen. Als u deze controleregel uitvoert en stap 2 mislukt vanwege een fout, zoals een request timeout of een wijziging in de naam van het eindpunt, blokkeert de fout de controleregel om de volgende stappen uit te voeren.

Dit is waar de functie **Foutafhandeling** nuttig wordt. Zelfs als stap 2 een fout veroorzaakte, kunt u nog steeds gegevens ophalen uit stap drie en vier, omdat deze onafhankelijk zijn van de vorige /GET requests. De fout mag uw controleregel er niet van weerhouden de resterende stappen uit te voeren.

## Foutafhandeling

Met de MSA **Foutafhandeling**-functie kunt u API-fouten flexibel beheren en afhandelen. Voor elke MSA-stap in uw controleregel heeft u de optie om het selectievakje **Doorgaan met uitvoeren en fouten negeren** te selecteren om fouten te negeren die in die stap zijn opgetreden:

![MSA Foutafhandeling-selectievakje]([LINK_URL_1])

Als u deze optie inschakelt en een bepaalde stap een fout tegenkomt, slaat uw controleregel de stap automatisch over en springt naar de volgende stappen. Uw controleregel negeert fouten, wat betekent dat deze fouten niet worden vastgelegd of weergegeven in een van uw [dashboards Fouten overzicht]([LINK_URL_2]) of [rapporten]([LINK_URL_3]). Alle genegeerde fouten worden alleen weergegeven in de pop-up **Details van de controle** nadat u **Test starten** heeft uitgevoerd en in de controleregel logs.

Om dit concept beter te begrijpen toont de onderstaande afbeelding het monitorresultaat van ons vorige voorbeeld. Controleer hoe stap twee mislukte vanwege een 404 Not Found-status. Als het selectievakje **Doorgaan met uitvoeren en fouten negeren** niet is aangevinkt, mislukt de controleregel op een bepaald punt waar hij een fout tegenkomt (stap twee). Deze fout blokkeert de uitvoering van de controleregel en de resterende stappen worden niet uitgevoerd:

![MSA Uitgeschakelde Foutafhandeling]([LINK_URL_4])

Als u in stap twee de optie **Doorgaan met uitvoeren en fouten negeren** aanvinkt, negeert de controleregel deze stap en gaat hij verder met het controleren van de resterende stappen:

![MSA Ingeschakelde Foutafhandeling]([LINK_URL_5])

## Gerelateerde artikelen

Voor meer informatie over foutafhandeling in transactiecontroleregels, raadpleegt u het knowledgebase-artikel [Negeer fouten gebruiken bij optionele stappen en acties]([LINK_URL_6]).
