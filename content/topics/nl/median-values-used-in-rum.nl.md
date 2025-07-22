{
  "hero": {
    "title": "Mediaanwaarden gebruikt in RUM"
  },
  "title": "Mediaanwaarden gebruikt in RUM",
  "summary": "Uptrends' RUM van geeft u de keuze tussen mediaan of gemiddelde waarden. Lees hoe Uptrends de mediaanwaarden voor uw rapporten berekent.",
  "url": "/support/kb/rum/mediaanwaarden-gebruikt-in-rum",
  "translationKey": "https://www.uptrends.com/support/kb/rum/median-values-used-in-rum"
}

[Real User Monitoring](/producten/real-user-monitoring) (RUM) gaat over  de geaggregeerde gebruikerservaring; daarom berekent RUM de resultaten op basis van al uw gebruikers. Het is belangrijk dat u weet hoe Uptrends de resultaten berekent, omdat u er zeker van wilt zijn dat de data in uw RUM-rapporten echt representatief zijn voor de ervaring van uw gebruikers. Standaard worden voor uw RUM-rapporten de mediaanwaarden gebruikt en niet het gemiddelde, maar u kunt altijd wisselen tussen de twee methoden. Om te zorgen dat u de beste keuze kunt maken voor uw rapporten worden in dit artikel de twee methoden vergeleken. Er wordt uitgelegd hoe Uptrends de mediaanwaarden berekent en waarom wij denken dat databemonstering geen goede keuze is als het om uw RUM-data gaat.

## Gemiddelde versus mediaan

Als u uw RUM-tabellen en -grafieken bekijkt, ziet u dat we standaard mediaanwaarden in plaats van gemiddelde waarden rapporteren. We gebruiken de mediaanwaarde omdat we denken dat deze representatiever is voor de dataset. We bekijken eerst de twee methoden.

**Gemiddelde**: De som van alle getallen gedeeld door het aantal. Bijvoorbeeld: het gemiddelde van de set {1, 2, 2, 3, 12} is 4.

**Mediaan**: Het middelste getal in een set. Bijvoorbeeld: de mediaanwaarde van de set {1, 2, 2, 3, 12} is 2.

In bovenstaand voorbeeld ziet u dat de uitschieter 12 de gemiddelde waarde vertekent, terwijl de mediaanwaarde de dataset nauwkeuriger weergeeft. Berekeningen waarbij de mediaanwaarde wordt gebruikt, grijpen op het zwaartepunt aan zonder de vertekening die wordt veroorzaakt door ongebruikelijk lage of hoge waarden in de set.

## Hoe Uptrends de mediaan berekent

In een relatief kleine dataset berekent Uptrends de mediaan door de dataset te sorteren en de middelste waarde te gebruiken. Grotere datasets echter, zorgen voor problemen wanneer de mediaanwaarde wordt berekend omdat het veel tijd kost om de middelste waarden in een grote dataset te vinden. Dus in plaats van u te laten wachten, berekenen we de mediaanwaarde met behulp van een [histogram](https://en.wikipedia.org/wiki/Histogram). De histogrambenadering versnelt de berekening, maar introduceert een lage standaardafwijking van ongeveer 1%. Maar zelfs met de potentiële afwijking van 1%, denken wij dat de mediaanberekening met behulp van een histogram de ervaringen van uw gebruikers nauwkeuriger beschrijft dan de gemiddelde waarde.

## Bemonsteren als alternatief voor histogrammen

Een alternatieve benadering voor histogrammen is [databemonstering](https://support.google.com/analytics/answer/2637192?hl=en). Met databemonstering wordt bij de berekening alleen een subset van de data gebruikt voor het bepalen van het gemiddelde of de mediaan. Met RUM kunt u uw data groeperen op basis uw gebruikers' locatie, browser en versie, besturingssysteem en versie, apparaattype en bekeken pagina. Maar met databemonstering kunt u complete gebruikersgroepen missen. We willen dat u met Uptrends uw resultaten ziet op basis van al uw gebruikers, maar zoals we eerder hebben uitgelegd, kost het veel tijd om uw resultaten te berekenen. Met de histogrambenadering krijgt u uw resultaten snel zonder het verlies van gebruikers in uw dataset.

## Schakelen tussen mediaan en gemiddelde

U kunt instellen welke berekeningsmethode u voor uw rapporten gebruikt.

1. Ga naar de RUM-dashboardtegel die u wilt veranderen.
2. Klik op het menupictogram met drie stippen {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} om de tegelinstellingen te openen.
3. Selecteer een optie in de lijst **Aggregatie**.
4. Klik op {{< AppElement type="button" >}}Instellen{{< /AppElement >}}.

![screenshot tegelinstellingen aggregatie](/img/content/scr_RUM-tile-median-average.min.png)
