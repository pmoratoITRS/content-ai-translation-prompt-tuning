{
  "hero": {
    "title": "Variabelen gebruiken in transacties"
  },
  "title": "Variabelen gebruiken in transacties",
  "summary": "Een handleiding over het gebruik van variabelen in transacties.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transactievariabelen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

In sommige gevallen moet u mogelijk een waarde opslaan en hergebruiken die uw transactiecontroleregel tegenkomt tijdens het uitvoeren van het script. In dergelijke gevallen kunt u uw transactie configureren om de waarde als een **variabele** op te slaan en die later in het script weer te gebruiken. Als uw transactie bijvoorbeeld door een trechter gaat die een ordernummer genereert, kunt u de transactie dat in een variabele laten opslaan en later in het proces vergelijken met een ordernummer dat op een bevestigingspagina wordt vermeld, om er zeker van te zijn dat uw backend zijn werk goed heeft gedaan. 

## Een variabele creëren

Om een variabele te creëren gebruikt u de [actie 'Test de inhoud van een element']([LINK_URL_1]). Variabelen worden gecreëerd op basis van de volledige inhoud van een van de elementen op de pagina. Om het element dat u wilt opslaan te specificeren, moet u [een CSS selector of XPath query]([LINK_URL_2]) gebruiken. 

1. [Voeg een actie 'Test de inhoud van een element' toe]([LINK_URL_3]) op de juiste plaats in het transactiescript. De elementinhoud die u als variabele wilt opslaan, moet op dat punt in de transactie op de pagina aanwezig zijn.
2. Wijs de inhoudcontrole naar het juiste element op de pagina met behulp van [een CSS selector of XPath query]([LINK_URL_4]). Als u hierbij hulp nodig heeft, [neem dan contact op met het support team]([LINK_URL_5]). 
3. De [inhoudcontrole]([LINK_URL_6]) test op de aanwezigheid van het gespecificeerde element en verifieert ook dat zijn inhoud overeenkomt met een bepaalde waarde (u kunt gebruikmaken van regular expressions). 
4. Vul voor de optie **Variabele toewijzen** de naam van de variabele tussen dubbele accolades in: [INLINE_CODE_1]

In het onderstaande voorbeeld plaatst de tweede stap van een transactie een bestelling (door te klikken op een element met identifier [INLINE_CODE_2] in stap 2.1), controleert op de aanwezigheid van een element [INLINE_CODE_3] en verifieert of de inhoud overeenkomt met een regular expression (in stap 2.2). Tot slot slaat het een variabele [INLINE_CODE_4] op door gebruik te maken van de optie **Variabele toewijzen**. De variabele bevat de volledige waarde van het element (wat in dit geval *"Uw bestelnummer is: 1234"* zou zijn.

![Creating a transaction variable]([LINK_URL_7])

## Een variabele aanpassen

In gevallen zoals het voorbeeld hierboven, kan de inhoud die in de variabele is vastgelegd onnodige tekst bevatten. In dit geval is het interessante deel van de string in de variabele waarschijnlijk alleen het ordernummer zelf. De inhoud van de variabele kan worden aangepast door er een regular expression op toe te passen om specifieke delen ervan te behouden of te verwijderen. Zie voor meer informatie het Knowledge Base-artikel over [de actie 'Inhoud variabele aanpassen']([LINK_URL_8]).

1. Nadat de variabele in het transactiescript is gecreëerd, voegt u een actie **Inhoud variabele aanpassen** toe.
2. Voeg de eerder gedefinieerde variabelenaam toe ([INLINE_CODE_5] in het bovenstaande voorbeeld).
3. Kies **behoud** of **verwijder** alles dat overeenkomt met het patroon van de regular expression.
4. Voeg de regular expression toe.

![Een variabele transformeren]([LINK_URL_9])

Het resultaat van deze actie, zoals toegepast op het bovenstaande voorbeeld, zou het geïsoleerde bestelnummer zijn: *1234*. Houd er rekening mee dat hiermee de bestaande variabele wordt overschreven.

## Variabelen gebruiken

Nu een variabele is gedefinieerd en optioneel is aangepast, kan deze elders in de transactie worden gebruikt. Naar variabelen kan op elk moment na hun creatie worden verwezen met hun naam. Het bestelnummer dat in het voorbeeld hierboven is geïsoleerd, kan bijvoorbeeld worden hergebruikt als de waarde in een **Instellen**-actie en ingevuld worden in een zoekvak om te bevestigen dat de bestelling met succes is gemaakt. Verwijs eenvoudigweg naar de variabele met zijn naam ([INLINE_CODE_6] in dit geval).


![Een transactievariabele gebruiken]([LINK_URL_10])



