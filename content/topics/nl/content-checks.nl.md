{
  "hero": {
    "title": "Inhoudcontroles"
  },
  "title": "Inhoudcontroles",
  "summary": "Bij het configureren van transactiecontroleregels kunt u met een aantal zaken rekening houden.",
  "url": "/support/kb/synthetic-monitoring/transacties/inhoudcontroles",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/content-checks"
}

Als u zeker wilt weten dat uw transactie probleemloos werkt, zijn *Inhoudcontroles* de meest waardevolle tools die u tot uw beschikking heeft. Een goed gebruikte inhoudcontrole kan een groot verschil maken in een transactie. Over het algemeen is het doel van inhoudcontroles het verifiëren dat de eerder uitgevoerde actie (bijvoorbeeld klikken op een link, inloggen/uitloggen, navigeren naar een pagina) met succes is voltooid. Aangezien transactiecontroleregels worden uitgevoerd met een script, is het toevoegen van inhoudverificatie van onschatbare waarde om te garanderen dat de transactie soepel werkt en u nauwkeurige informatie over uw website geeft.

**Inhoudcontroles zijn gratis, dus we raden u aan ze te gebruiken!** Inhoudcontroles voegen waarde toe aan uw transactiecontroleregel na elke actie die nieuwe inhoud op de pagina genereert.

Omdat een inhoudcontrole in uw transactiescript wacht tot de aangegeven inhoud is geladen, heeft u twee extra voordelen.

- Ten eerste weet u zeker dat de navigatie op de juiste pagina is geëindigd door de aanwezigheid van paginaspecifieke inhoud te verifiëren.
- Ten tweede weet u zeker dat de pagina correct en volledig is geladen door te wachten tot het aangegeven element klaar is met laden. Door te verifiëren dat het laden van het element is voltooid, wordt voorkomen dat de transactie te snel doorgaat met de volgende actie.

## Wanneer moet u inhoudcontroles gebruiken?

Over het algemeen is het doel van een inhoudcontrole het verifiëren van de succesvolle voltooiing van de eerder uitgevoerde actie. U moet inhoudcontroles toevoegen na elke actie die de inhoud van de pagina op enigerlei wijze verandert. Door gebruik te maken van een inhoudcontrole test u expliciet of specifieke acties in het script het gewenste resultaat hadden in de browser. Voorbeelden van wanneer u een inhoudcontrole moet gebruiken, zijn onder andere:

- na het invoeren van de inloggegevens en klikken op de "login"-knop
- na het klikken op een productlink op een e-commercesite
- na het uitloggen
- na het navigeren naar een nieuwe pagina

U moet ook een inhoudcontrole gebruiken om te controleren of een automatisch aangevuld tekstveld werkte, een tabel correct is gevuld met data en of een script met succes is uitgevoerd.

## Inhoudcontroles toevoegen

U kunt inhoudcontroles toevoegen tijdens het [opnameproces]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks#use-content-checks" lang="nl" >}}) of via de controleregel-stapeditor hieronder.

Om een inhoudcontrole toe te voegen:

1. Open de transactiecontroleregel die u wilt wijzigen.
2. Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}}. 
3. Zoek de stap waaraan u een inhoudcontrole-actie wilt toevoegen.
4. Klik op de knop {{< AppElement type="buttonPrimary" >}} Actie toevoegen {{< /AppElement >}}. U ziet dat de actietypen voor inhoudcontrole een groen "Test"-label hebben in de lijst met beschikbare acties. 
   ![screenshot inhoudcontrole toevoegen in transactie](/img/content/scr_transaction-add-content-check.min.png)
5. Selecteer het juiste actietype in het pop-upvenster. Nadat u uw selectie heeft gemaakt, verschijnt de nieuwe actie in de editor.
   ![screenshot inhoudcontrole in transactiestap](/img/content/scr_transaction-content-check-element.min.png)
  Dit screenshot toont het actietype *Test de inhoud van een element*. 
6. Voer de instellingen in die nodig zijn voor uw inhoudcontrole. De instellingsopties variëren afhankelijk van het geselecteerde actietype. Zie de alinea [Typen inhoudcontrole]({{< ref path="#content-check-types" lang="nl" >}}) voor informatie over de opties per type.
7. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen op te slaan. 

De bovenstaande instructies zijn voor de visuele editor. U kunt ook de [script-editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="nl" >}}) gebruiken voor het toevoegen of wijzigen van stappen.

## Typen inhoudcontrole {id="content-check-types"}

U kunt kiezen tussen een aantal verschillende typen inhoudcontroles. 

### Test de inhoud van een element {id="test-element-content"}

Voor het testtype *Test de inhoud van een element* controleert Uptrends een specifiek pagina-element op inhoud die u opgeeft. De controle *Test de inhoud van een element* zorgt voor meer specifieke en robuuste controles in vergelijking met het type *Test de inhoud van het document*. Voor de meeste doeleinden raden we u aan het type *Test de inhoud van een element* te gebruiken. Het type *Test de inhoud van een element* vereist dat u naar een specifiek element op de pagina verwijst met een CSS- of XPath-selector en een inhoudstring definieert die het element moet bevatten. Dit leidt tot zeer robuuste controles die de succesvolle voltooiing van acties die het script uitvoert, verifiëren.

De actie *Test de inhoud van een element* vereist het gebruik van een CSS- of XPath-selector om naar een specifiek element te verwijzen waarvan u de inhoud wilt controleren.

![screenshot actie inhoud van element testen bovenkant](/img/content/scr_transaction-action-content-check-main.min.png)

Gebruik het vervolgkeuzemenu om te schakelen tussen de twee selectortypen. Meer informatie over selectors vindt u in de knowledgebase-artikelen [Selectors gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="nl" >}}) en [Selectoralternatieven]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="nl" >}}).

Na het selecteren van een selectortype (CSS/XPath) en het invoeren van de selector, kunt u een matchvoorwaarde kiezen uit de volgende opties:

- bevat
- bevat niet (zie ook [Negatieve inhoudcontroles]({{< ref path="#negation-content-checks" lang="nl" >}}))
- matcht met regular expression
- matcht niet met regular expression (zie ook [Negatieve inhoudcontroles]({{< ref path="#negation-content-checks" lang="nl" >}}))

Tot slot voert u in het veld **voorbeeldtekst** de waarde in die u wilt laten controleren in het aangegeven element.

De andere actie-instellingen zijn optioneel.

**Omschrijving** — Voeg een beschrijving toe voor uw inhoudcontrole, zoals "Test of het inloggen is gelukt."

**Foutmelding** — Wat moet worden weergegeven als deze inhoudcontrole een fout genereert, zoals "Inloggen is niet gelukt."

**Wacht tot** — Stel de wachtconditie in voor deze controleregelcheck. Raadpleeg het artikel [Wacht op element]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}). Opmerking: Wacht tot is niet beschikbaar voor het type *Test de inhoud van het document*.

**Wachttijd** — Hoelang, in milliseconden, Uptrends moet wachten tot de inhoud verschijnt. De standaardwaarde is 30 seconden. In de meeste gevallen raden we u aan om u aan de standaard te houden. In bepaalde gevallen kan het echter nuttig zijn om de wachttijd te verhogen. De maximale waarde voor de wachttijd is 60 seconden. Let erop dat u de wachttijd niet te veel verhoogt, want er is een absolute bovengrens voor hoelang een volledige transactie mag duren. NB: het verhogen of verlagen van de wachttijd heeft geen invloed op de meetresultaten van tijd voor de transactie.

**Variabele toewijzen** — Voer een variabelenaam in het formaat `{{name}}` in. Zie ons artikel over [transactievariabelen gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="nl" >}}) voor meer informatie.

**Shadow DOM host** — Hiermee kunt u een [shadow DOM]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}) host specificeren en zelfs geneste shadow DOMs.

Als u rechtstreeks met het JSON-transactiescript in de [script-editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#scripting-source-code-directly" lang="nl" >}}) werkt, moet het controletype *Test de inhoud van een element* de volgende indeling hebben:

```json
{
  "testElementContent": {
    "value": "Example text",
    "testType": "Contains",
    "element": {
      "xpath": "[@id='exampleId']",
      "alternatives": [],
      "shadowRoots": []
    },
    "timeoutMs": 3000,
    "description": "Description of this action"
  }
}
```

Als parameters optioneel zijn, zoals `timeoutMs`, `description` en `failureMessage`, kunt u ze weglaten. De beschikbare `testType` parameterwaarden zijn `Contains`, `DoesNotContain`, `MatchesRegex` en `DoesNotMatchRegex`. Dit voorbeeld verifieert dat het (voorbeeld)element met XPath-selector `//*[@id=’exampleId’]` de string "Example text" bevat. Natuurlijk werkt CSS ook - gebruik de waarde `“css”:”#exampleId”` in plaats van `"xpath": "[@id='exampleId']"`.

### Test de inhoud van het document

Het type *Test de inhoud van het document* is het meest rechttoe rechtaan van de beschikbare typen. Het type *Test de inhoud van het document* zoekt overal in het paginadocument naar de opgegeven inhoud, ongeacht of de inhoud zichtbaar is. Niet alle tekst in het paginadocument of DOM is zichtbaar op de pagina. Echter, aangezien het testtype *Test de inhoud van het document* het HTML-document controleert in plaats van de pagina terwijl de browser de inhoud laadt, kunt u op "onzichtbare" tekst controleren. Aangezien het type *Test de inhoud van het document* niet de inhoud van de geladen pagina controleert, kunt u geen XPath- of CSS-selectors gebruiken om naar een specifiek element te verwijzen. We ondersteunen echter wel het gebruik van een regular expression om naar specifieke patronen in de DOM-inhoud te zoeken.

Als u ervoor kiest om rechtstreeks met het JSON-transactiescript te werken in plaats van de visuele editor te gebruiken, moet het controletype *Test de inhoud van het document* de volgende indeling hebben:
```json
    { 
    "testDocumentContent": { 
      "value": "Example content in the DOM", 
      "testType": "Contains",
      "timeoutMs": 30000, 
      "description": "This check will test the page DOM for the specified content.", 
      "failureMessage": "Example failure message" 
      } 
    }
```
NB: de parameters `timeoutMs`, `description` en `failureMessage` zijn optioneel, dus die kunt u weglaten.

### Wacht op element

Het testtype *Wacht op element* is identiek aan het type *Test de inhoud van een element*, behalve dat het element in dit geval geen tekstinhoud hoeft te bevatten. U kunt het testtype *Wacht op element* gebruiken om te controleren op lege elementen, bijvoorbeeld, &lt;div&gt;-elementen zonder enige tekst erin, afbeeldingen en knoppen.

Als u rechtstreeks met het JSON-transactiescript werkt, moet het controletype *Wachten op element* de volgende indeling hebben:
```json
    {
      "waitForElement": {
        "element": {
          "xpath": "//*[@id='exampleId']" 
        },
        "timeoutMs": 30000,
        "description": "Verify that the element with the indicated XPath selector exists on the page.",
        "failureMessage": "Example failure message"
      }
    }
```
NB: de parameters `timeoutMs`, `description` en `failureMessage` zijn optioneel, dus die kunt u weglaten.

## Negatieve inhoudcontroles {id="negative-content-checks"}

In plaats van te verifiëren dat specifieke inhoud **wel** bestaat in de DOM of op de pagina verschijnt, moet u mogelijk verifiëren dat bepaalde inhoud **NIET** op de pagina bestaat. U wilt bijvoorbeeld een alert ontvangen als er een bepaalde foutmelding op uw pagina verschijnt. Om te testen dat gespecificeerde inhoud niet op de pagina verschijnt, gebruikt u *negatieve inhoudcontroles*. Als de gespecificeerde inhoud op de pagina verschijnt, faalt de controleregel.

Om een negatieve inhoudcontrole te gebruiken voegt u een controletype *Test de inhoud van het document* of *Test de inhoud van een element* toe. Wijzig vervolgens de matchvoorwaarde van de standaardwaarde **bevat** in **bevat niet** of **matcht niet met regular expression**.

Wanneer een negatieve inhoudcontrole wordt gebruikt en de transactie het gespecificeerde element of de gespecificeerde inhoud aantreft, stopt de transactie en retourneert hij een fout. Als het element of de inhoud niet verschijnt, gaat de transactie gewoon verder.

## Kwaliteit inhoudcontrole 

Om de beste resultaten van uw inhoudcontrole te garanderen, selecteert u een uniek element op de pagina dat unieke tekst bevat die het resultaat is van de vorige actie. Een nuttige inhoudcontrole is een definitieve en exclusieve test van een actie, en voor de meeste *Test de inhoud van een element*-controles komt het neer op het testen op een combinatie van een robuuste en unieke **selector** en **tekstwaarde**.

### Tekstwaarde

Het kiezen van een unieke tekstwaarde om op te testen is essentieel voor zowel het controletype *Test de inhoud van een element* als *Test de inhoud van het document*. De noodzaak om unieke tekstwaarden te kiezen is niet van toepassing op het controletype *Wacht op element* omdat die test niet op tekstwaarden test.

Zorg er bij het selecteren van de tekst voor de controle voor dat de tekst een direct gevolg is van de vorige actie. Bijvoorbeeld:

-   Na klikken op een inlogknop of uitloglink kunt u de volgende pagina testen op de aanwezigheid van een accountnaam of de bijbehorende uitlog- of inloglink.
-   Na klikken op een link om naar een productpagina te gaan, test u op productspecificaties of een knop Toevoegen aan winkelwagen.
-   Zoek op de nieuwe pagina naar een link die u nodig heeft voor de volgende stap.

**Kies geen tekst die op elke pagina (hetzelfde) verschijnt.** Gebruik bijvoorbeeld geen voettekst. Voettekst vertelt u niets over de voortgang van de transactie.

Gebruik waar van toepassing [regular expressions](https://www.w3schools.com/jsref/jsref_obj_regexp.asp) Bijvoorbeeld: als op uw pagina na het uitvoeren van een zoekactie "15 results found" staat, stelt u een inhoudcontrole in voor `.* result(s), found`, en stelt u de inhoudcontrolevoorwaarde in op **matcht met regular expression**.

Nadat u de tekst voor uw controle heeft gekozen, moet u ervoor zorgen dat u een unieke en robuuste (bestand tegen wijzigingen op de pagina) CSS- of XPath-selector formuleert. 

### Selectors

Het kiezen van een robuuste en solide selector is essentieel voor de testtypes *Test de inhoud van een element* en *Wacht op element*. Aangezien het verwijzen naar een specifiek element geen optie is voor het testtype *Test de inhoud van het document*, is deze alinea daarop niet van toepassing.

Een goede selector is uniek op de pagina. Door een unieke waarde te gebruiken, weet u zeker dat Uptrends naar het juiste element kijkt. Gebruik waar mogelijk de id attribute van het element, omdat deze over het algemeen uniek moeten zijn voor dat specifieke element. Bijvoorbeeld: `//*[@id=’testId’]` of `#testId`. 

Lees meer over selectors in de knowledgebase-artikelen [Selectors gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="nl" >}}) en [Selectoralternatieven]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="nl" >}}).

## Waarschuwingen, valkuilen en tips

**Houd hoofdlettergevoeligheid in gedachten**. Met het gebruik van CSS kan tekst (en dit gebeurt regelmatig) in hoofdletters op de pagina verschijnen, terwijl het in de DOM hoofd- en kleine letters als in zinnen gebruikt. Dat betekent dat de selector `//span[text()='Hello']` zou kunnen zijn, maar de tekst op de pagina zou "HELLO" kunnen zijn. De selector moet de informatie in de DOM weerspiegelen, en de tekenreeks die u invoert om te matchen, moet weerspiegelen wat er daadwerkelijk op de pagina staat.

**Sommige pagina's gebruiken dynamische ID's voor hun elementen**. We kunnen bijvoorbeeld een klik op een span opnemen die in de DOM verschijnt als  
`<span id="example-12345">`.  
Echter, na het opnieuw laden van een pagina, zou dit exact hetzelfde element verschijnen als  
`<span id="example-12789">`.  
Gebruik XPath om dynamische ID's te verwerken. Bijvoorbeeld:  
`//span[contains(@id,'example-')]`.
