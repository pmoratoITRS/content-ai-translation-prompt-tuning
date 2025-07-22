{
  "hero": {
    "title": "Controlefrequentie uitgelegd"
  },
  "title": "Controlefrequentie uitgelegd",
  "summary": "De controlefrequentie is de tijd tussen het einde van de laatste controle en het begin van de volgende.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/controlefrequentie-uitgelegd",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/check-interval-explained"
}

De derde optie in uw controleregelinstellingen vraagt om de frequentie voor uw monitoringcontroles (zie onderstaande afbeelding). U kunt uw controles zo vaak instellen als eenmaal per minuut tot één keer per uur. Maar wat betekent “Controlefrequentie” precies? **De frequentie is de tijd tussen het einde van een controle en het begin van de volgende.** Laten we dit wat verder onderzoeken.

![](/img/content/208e20d2-aa65-4d61-8ff7-678629d4c1d7.png)

U denkt misschien dat als u één minuut als uw controlefrequentie kiest, Uptrends uw website 1440 keer per dag controleert, waarbij controles elke hele minuut beginnen, maar zo werkt het niet. Uptrends moet weten dat de vorige controle met succes is voltooid voordat de volgende controle wordt gepland. Daarom is het aantal dagelijkse controles afhankelijk van:

-   Controleregeltype,
-   Paginalaad- of responstijden,
-   Welke frequentie u selecteert,
-   Het aantal fouten dat Uptrends tegenkomt bij uw site of dienst, en
-   Systeemoverhead  voor het verzenden van de controledefinitie naar het controlestation, het verzenden en verwerken van de resultaten.

Laten we een paar voorbeelden bekijken:

**Uptimecontrole, frequentie één minuut**

Als een uptimecontrole tien seconden duurt van start tot einde, begint de volgende controle 60 seconden na de succesvolle voltooiing van de eerste controle. In dit geval kunt u dus intervallen van ongeveer 70 seconden verwachten tussen het begin van de ene controle en het begin van de volgende. In plaats van 1440 controles per dag, zou u ongeveer 1234 controles per dag hebben.

**Transactiemonitor, frequentie vijf minuten**

Complexe transacties kunnen even duren voordat ze voltooid zijn, afhankelijk van het aantal stappen en de responsiviteit van uw site of dienst. Als het twee minuten duurt om een controle van begin tot eind te voltooien, begint de volgende controle vijf minuten nadat de eerste controle is voltooid ofwel zeven minuten na het begin van de eerste controle. In plaats van 288 controles per dag resulteert dit scenario in ongeveer 206 controles per dag.

## Hoe beïnvloeden fouten de frequentie van mijn controleregel?

Wanneer Uptrends een foutmelding ontvangt van uw website of dienst, negeert Uptrends de controlefrequentie en voert meteen de volgende controle uit vanuit een ander controlestation. Als Uptrends een tweede foutmelding ontvangt, stuurt Uptrends een alert. Uptrends plant vervolgens de volgende controle op basis van uw frequentie-instellingen. Bij de start van het volgende testinterval controleert Uptrends weer en voert opnieuw een dubbele controle uit als er een fout optreedt. U ziet in de onderstaande controleregel log dat hoewel de controleregel een controlefrequentie van vijf minuten heeft, de bevestigde fouten (rood) telkens meteen na de onbevestigde fout (geel) optreden. Het tijdsinterval tussen de bevestigde fout en de volgende controle is vijf minuten.

![](/img/content/be606700-fbc5-4b64-879a-59cc32b3ecbe.png)
