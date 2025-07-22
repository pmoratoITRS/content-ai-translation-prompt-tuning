{
  "hero": {
    "title": "Shadow DOM"
  },
  "title": "Werken met een shadow DOM",
  "summary": "Leer hoe u interacties instelt binnen een shadow DOM voor uw transactiecontroleregels.",
  "url": "/support/kb/synthetic-monitoring/transacties/shadow-dom",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/shadow-dom"
}

In dit artikel bespreken we de stappen voor het afhandelen van een shadow DOM op uw pagina bij het configureren van een transactiecontroleregel. 

## Document Object Model (DOM)

Een **DOM (Document Object Model)** is een weergave van elk van de elementen in een markup-document (zoals een HTML-document voor webpagina's). Wanneer u een webpagina laadt, maakt uw browser een DOM op basis van het HTML-document, waarbij elk afzonderlijk element in een boomstructuur wordt gerangschikt. U kunt de DOM voor een bepaalde pagina bekijken door de *Developer tools* van uw browser te openen (meestal door op F12 te drukken), in het tabblad 'Elements'. 

De DOM wordt gebruikt als een live weergave van het document (wijzigingen in de DOM zijn gelijk aan wijzigingen op de webpagina die wordt weergegeven in de browser), zodat tijdelijke wijzigingen aan de pagina kunnen worden aangebracht terwijl deze in het browservenster wordt weergegeven, met JavaScript bijvoorbeeld. 

## Shadow DOM

Zaken als JavaScript en CSS zijn globaal van toepassing op elke node binnen de DOM. In sommige gevallen kan dat echter tot problemen leiden. Als uw pagina bijvoorbeeld webcomponenten bevat (herbruikbare elementen, zoals tabellen of betalingsmodules die op meerdere pagina's kunnen voorkomen), kunnen er conflicten zijn in markup of styling met de rest van de pagina. Om dit te voorkomen is het een goede gewoonte om deze webcomponenten in te kapselen: zorg ervoor dat ze los van het hoofddocument kunnen bestaan, om conflicten te voorkomen en de code te vereenvoudigen.

Eén mogelijkheid om dit te bereiken bestaat in de vorm van **shadow DOM's**. Een shadow DOM maakt het mogelijk om een aparte, verborgen DOM-boom te koppelen aan specifieke elementen in de reguliere DOM-boom. Een shadow DOM is op dezelfde manier gestructureerd als een reguliere DOM, maar is gekoppeld aan een **shadow host**: een node binnen de gewone DOM. Aangezien een shadow DOM een afzonderlijke 'boom in een boom' is, kan geen van de code erin de nodes in het reguliere DOM beïnvloeden, en vice versa. 

## Shadow DOM configureren voor transacties

De interacties binnen een transactiescript werken op de nodes in de pagina-DOM. Aangezien een shadow DOM afzonderlijk is, moet een transactiecontroleregel worden geconfigureerd om in die shadow DOM te kijken in plaats van in de hoofddocument-DOM. Laten we een voorbeeld bekijken en zeggen dat de DOM van uw webpagina het volgende bevat:

```html
<html>
    <head>...</head>
    <body>
        ...
        <example-root-element id="exampleId" class="class example">
            #shadow-root (open)
                <a class="linkClass" href="https://www.exampledomain.com">Example link</a>
                <div>Some example text</div>
                <input type="text" id="exampleTextfield">
        </example-root-element>
        ...
    </body>
</html>
```

Dit gedeelte van een DOM bevat een shadow DOM, aangeduid door de node **#shadow-root (open)**. De shadow DOM bevat drie elementen: een koppeling (met class 'linkClass'), een tekstreeks (de `<div>` met daarin "Some example text") en een tekstveld `<input>`-element (met ID 'exampleTextfield'). 

Zoals altijd het geval is met een shadow DOM, is deze gekoppeld aan een element in de hoofddocument-DOM. In dit geval is dat element (bekend als de **shadow host**) `<example-root-element>` dat zijn eigen ID en class heeft. 

Als de transactie een stap nodig heeft die een waarde in het tekstveld invult, moeten we de transactie expliciet vertellen dat deze in de shadow DOM moet kijken. Dit doet u als volgt:

1. Voeg [een actie]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="nl" >}}) van het juiste type toe. In dit voorbeeld vullen we wat tekst in, dus gebruiken we de actie **Instellen**. Dezelfde stappen gelden voor de andere interactietypes.
2. Klik in de instellingen voor de actie op de knop {{< AppElement type="button" >}} Geef een shadow DOM host op {{< /AppElement >}}.
3. Vul de identifier voor het shadow host element in. In dit geval kunnen we naar het shadow root element verwijzen met zijn ID *exampleId*. Wanneer u een shadow host specificeert, kunt u een CSS (`#exampleId`) of XPath (`//example-root-element[@id='exampleId']`) selector gebruiken.
4. Nu we de transactie hebben verteld om in deze specifieke shadow DOM te kijken, kunnen we doorgaan zoals we normaal zouden doen. Specificeer het element waarop de Instellen-actie moet plaatsvinden. In dit geval gebruiken we de ID van het tekstveld *exampleTextfield*. Wanneer u elementen specificeert binnen een shadow DOM, kunt u **alleen gebruikmaken van CSS selectors**.
5. Vul tot slot de tekst in die in het tekstveld moet worden ingesteld en configureer zo nodig andere opties.

![Voorbeeld shadow DOM](/img/content/scr-transactions-shadow-dom-example.min.png)

Als u de [transactie-scripteditor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="en" >}}) gebruikt (door te klikken op *Naar script schakelen* in de rechter bovenhoek van de stapeditor), ziet diezelfde actie er als volgt uit:

```json
{
"set": {
    "value": "Fill out some text",
        "element": {
            "css": "#exampleTextfield",
            "alternatives": [],
            "shadowRoots": [
                {
                "css": "#exampleId"
                }
              ]
            },
    "description": "Shadow DOM example"
    }
}
```

### Geneste shadow DOM's

In sommige gevallen kan een shadow DOM worden genest in een andere shadow DOM. U kunt uw transactie configureren om dit af te handelen door simpelweg een andere geneste shadow DOM host toe te voegen en de shadow DOM selectors in te voeren in de volgorde waarin ze verschijnen.

![Geneste shadow DOM](/img/content/scr-transactions-shadow-dom-nesting.min.png)

Voeg in de transactie-scripteditor gewoon extra waarden toe aan de shadowRoots array:

```json
 "shadowRoots": [
    {
        "css": "#firstShadowDom"
    },
    {
        "css": "#secondShadowDom"
    }
]
```