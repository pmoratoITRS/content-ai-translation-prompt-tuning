{
  "hero": {
    "title": "Pagina-interacties"
  },
  "title": "Pagina-interacties",
  "summary": "Binnen uw transactiecontroleregel heeft u de mogelijkheid om vier verschillende soorten interacties of acties toe te voegen. In dit artikel splitsen we de vier typen op.",
  "url": "/support/kb/synthetic-monitoring/transacties/pagina-interactie",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/page-interactions"
}

Een van de belangrijkste dingen die transactiemonitoring onderscheidt van onze andere soorten monitoring, is de mogelijkheid om met pagina's te interacteren. Met Web Application Monitoring klikt Uptrends op pagina-elementen, vult formulieren in, voert inloggegevens in, uploadt bestanden en voert anders allerlei gebruikersacties uit om uw gebruikersreizen te testen.

Met Self-Service Transacties maakt u een script dat met uw pagina interacteert via een groep van vier beschikbare actietypen of interacties. De vier belangrijkste pagina-interacties die in dit artikel worden besproken zijn *[Navigeren](#navigate)*, *[Klikken](#click)*, *[Hoveren](#hover)* en *[Instellen](#set)*. De interactie **Instellen** maakt ook *[Bestandsupload](#file-uploading-in-transactions)* mogelijk. Er zijn nog [andere acties]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#what-is-an-action" lang="nl" >}}) waaronder inhoudcontroles, het nemen van een screenshot of het maken van een watervalrapport.

## Navigeren {id="navigate"}

Navigeren is de allereerste actie die wordt opgenomen of toegevoegd aan een transactiescript. Elke transactie begint met het navigeren naar een URL voordat deze de functionaliteit van uw site begint te testen. De navigatieactie vertelt de browser naar de URL te gaan en de controleregel wacht tot de pagina volledig is geladen (binnen een redelijk tijdsbestek).

In de meeste gevallen bevat een transactie alleen die ene navigatieactie aan het begin. Soms is echter een tweede navigatie nodig binnen de transactie. Wanneer extra navigatiestappen nodig zijn, raden we u aan om deze navigatieacties in hun eigen stappen te plaatsen. Door navigatieacties in hun eigen stap te plaatsen, houdt u overzicht op wat er op welk punt van uw transactie gebeurt, en kunt u de timingstatistieken die Uptrends per stap meet interpreteren.

Opgemerkt moet worden dat een navigatieactie altijd één [transactiecredit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) gebruikt.

### Opties voor navigatieacties

De beschikbare opties voor de navigatieactie omvatten (zie onderstaande afbeelding):

-   **URL**: de URL die wordt gebruikt voor de navigatie (vereist).
-   **Omschrijving**: een omschrijving van de actie die wordt gebruikt voor rapportagedoeleinden.
-   **Foutmelding**: het bericht dat wordt opgenomen in foutrapporten, in het geval van een fout.
-   **Resultaat**: selectievakje dat Uptrends instrueert om **de teruggegeven HTTP-statuscode te negeren**.
-   **Wachttijd**: een waarde die aangeeft hoelang Uptrends moet wachten tot de pagina is geladen. De standaard- (en maximum-) waarde is 60 seconden.

De instelling **Resultaat** verschilt van alle andere actietypen. Standaard zorgt een navigatieactie ervoor dat de pagina correct is geladen en dat de controleregel een foutloze HTTP-statuscode heeft ontvangen (een statuscode onder de 400). Elke statuscode van 400 of hoger genereert een fout voor de navigatieactie en de transactie wordt niet verder uitgevoerd. Als u de transactie wilt laten doorgaan ondanks het ontvangen van een foutstatuscode, vertelt het inschakelen van **Negeer de HTTP-statuscode die wordt teruggegeven** Uptrends door te gaan, ongeacht de resulterende statuscode.

![](/img/content/79ab474d-32d0-4c57-9709-2d86eebebd89.png)

### Volg navigeeracties met inhoudcontroles

Om ervoor te zorgen dat de transactie na de navigeeractie op de juiste pagina terechtkomt voegt u als volgende actie een inhoudcontrole toe. Een inhoudcontrole geeft u de zekerheid dat uw transactie op de juiste pagina terecht is gekomen, en dat de pagina volledig is geladen en de pagina de onderdelen weergeeft waarmee de controleregel verder met de pagina kan interacteren voordat de volgende actie wordt uitgevoerd.

### Gebruik watervalrapporten met navigatieacties

Aangezien een navigatieactie een volledig nieuwe pagina laadt, kan het handig zijn om specifieke statistieken over de paginalaadtijden te verzamelen door de optie watervalrapport in te schakelen in de stap die de navigatieactie bevat. Elk watervalrapport dat aan een transactie wordt toegevoegd, gebruikt één [transactiecredit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) .

## Klikken {id="click"}

De **Klikactie** vertelt de browser om op een specifiek pagina-element te klikken met een CSS- of XPath-selector. Er is een verscheidenheid aan mogelijke toepassingen voor een klikactie:

-   Opties selecteren,
-   Submenu's openen,
-   Selectievakjes selecteren of
-   Klikken op koppelingen die de transactie naar de volgende pagina brengen.

Daarom is de klikactie een integraal onderdeel van elke transactie.

In grote lijnen valt een klikactie in twee categorieën:

-   Klikacties die leiden naar een nieuwe pagina (koppelingen of knoppen) of
-   Klikacties voeren een actie uit op de bestaande pagina.

Een klik kan al dan niet resulteren in het gebruik van een [transactiecredit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}).

### Opties voor klikacties

De klikactie-opties omvatten (zie onderstaande afbeelding):

-   **Omschrijving**: een omschrijving van de actie die wordt gebruikt voor rapportagedoeleinden.
-   **Foutmelding**: het bericht dat wordt opgenomen in foutrapporten, in het geval van een fout.
-   **Foutafhandeling**: selecteren van het selectievakje **Negeer fouten die in deze actie optreden** vertelt de controleregel fouten te negeren die deze actie kan tegenkomen, zoals het niet vinden van het klikbare element.
-   **Wacht tot**: voordat een klikactie kan plaatsvinden, moet het element waarop de controleregel moet klikken, worden gerenderd en zichtbaar zijn op de pagina (in CSS-termen: het element moet worden weergegeven en zichtbaar zijn). Deze *wachtcondities* hebben een [eigen knowledge base-artikel]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}), waar u informatie kunt vinden over de verschillende opties.
-   **Wachttijd**: u kunt opgeven hoelang de controleregel moet wachten tot het element voldoet aan de bovenstaande vereiste **Wacht tot**. De standaard wachttijd is 30 seconden, maar u kunt de standaard wachttijd overschrijven met een maximale wachttijd van 60 seconden.
- **Shadow DOM host**: Als het element waarmee moet worden geïnteracteerd in een shadow DOM bestaat, moet de transactie worden geconfigureerd om te zoeken naar het element binnen die shadow DOM. U kunt meer informatie vinden in ons KB-artikel over [werken met een shadow DOM in uw transactie]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}).

![Pagina-interacties - klikken](/img/content/scr-page-interactions-click.min.png)

{{< callout >}}
**Opmerking**: Als u de \[Enter\]-toets gebruikt in plaats van de muis om op een verzendknop te klikken, kan de transactierecorder de interactie niet vastleggen. Als oplossing kunt u de actie [*Toetsenbordgebeurtenis*]({{< ref path="#key-event" lang="nl" >}}) gebruiken om het indrukken van een toets na te bootsen. U moet eerst uw transactie opnemen en vervolgens de *Toetsenbordgebeurtenis* handmatig toevoegen in de stapeditor. 
{{< /callout >}}


## Instellen {id="set"}

De **actie Instellen** vertelt de controleregel om waarden voor elementen in te voeren. Er zijn verschillende scenario's voor een instellenactie:

- **Tekstvelden en -vakken invullen**: inloggegevens en andere tekenreeksen die vaak nodig zijn in invoervelden.  
    Als de actie Instellen een automatische aanvulfunctie activeert; als u bijvoorbeeld een postcode of zoekterm invoert, kan de pagina een volledig adres of veelgebruikte termen voorstellen. In gevallen van automatisch aanvullen wilt u wellicht een inhoudcontrole toevoegen om er zeker van te zijn dat de automatische aanvulfunctie correct werkte en een klikactie toevoegen om de gewenste optie te selecteren.
- **Opties selecteren in een vervolgkeuzelijst**: doorgaans hebben *selecteren*-elementtypes verschillende voorgedefinieerde *<optie>*-elementen met elk hun eigen waarden. Wijs het script met een CSS- of XPath-selectie op het geselecteerde element. U kunt het *id*-kenmerk, *waarde*-kenmerk of de tekstinhoud van het optie-element instellen.
- **Bestanden uploaden vanuit de vault**: in bepaalde gevallen kan een bestandsupload vereist zijn om uw flow correct te testen. Bijvoorbeeld als u een klachtenformulier invult waarvoor een screenshot is vereist, of als u de uploadmogelijkheden van een onlinedatabank test. Het is mogelijk om de transactie een bestand te laten uploaden vanuit uw [account vault]({{< ref path="support/kb/account/vault" lang="nl" >}}). Een handleiding voor het instellen van bestandsuploads vindt u [verderop op deze pagina](#file-uploading-in-transactions).

Wanneer u [een *Instellen*-actie toevoegt]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-action" lang="nl" >}}) aan een stap zal deze er als volgt uitzien:

![Pagina-interacties - instellen](/img/content/scr-page-interactions-set.min.png)

De *Instellingen* worden uitgelegd in [Opties voor instellenacties]({{< ref path="#setaction-options" lang="nl" >}}).

Eerst moet u definiëren welk element u wilt instellen en op welke waarde. Voer de [CSS selector of XPath query]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="nl" >}}) in voor het element waarvoor u een waarde (of bestandsupload) wilt invoeren.

Klik dan op de knop met drie stippen om het pop-upvenster **Selecteer een waarde** te openen.

![screenshot van waardekiezer instellenactie](/img/content/scr_transaction-selection-value-picker.min.png)

De opties zijn [platte tekst of variabelen]({{< ref path="#variables" lang="nl" >}}), [vault-inloggegevens]({{< ref path="support/kb/account/vault#credential-set" lang="nl" >}}), [eenmalig wachtwoord]({{< ref path="support/kb/account/vault#one-time-password" lang="nl" >}}) en [upload vaultbestand]({{< ref path="#file-uploading-in-transactions" lang="nl" >}}).

### Platte tekst of variabelen {id="variables"}

U kunt eenvoudige tekst of variabelen of een combinatie van beide gebruiken om de waarde van een element in te vullen. Er zijn twee soorten variabelen: automatische variabelen en door de gebruiker gedefinieerde variabelen.
#### Automatische variabelen

U kunt de actie Instellen gebruiken voor het invullen van dynamisch gegenereerde gegevens, zoals tijdstempels of willekeurige tekenreeksen die zijn geselecteerd uit een array. Deze automatische variabelen moeten als volgt worden ingevoerd: {{< Code/Symbol type="variable" >}}{{@variableGoesHere(option1,option2)}}{{< /Code/Symbol >}}  
  
![Voorbeeld DateTime variabele](/img/content/scr-page-interactions-datetime.min.png)

Wilt u automatische variabelen in uw transactie gebruiken, raadpleeg dan de [volledige lijst met beschikbare automatische variabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}) .

#### Door de gebruiker gedefinieerde variabelen 

Meer informatie over door de gebruiker gedefinieerde variabelen vindt u in ons artikel over [het gebruik van transactievariabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="nl" >}}).

### Bestand uploaden in transacties {id="file-uploading-in-transactions"}

Om te configureren dat uw transactie bestanden uploadt moet u eerst de bestanden aan de vault toevoegen. Instructies over hoe u bestanden aan uw vault toevoegt, vindt u in ons [artikel over de vault]({{< ref path="support/kb/account/vault" lang="nl" >}}) .

Wanneer u het bestand aan uw vault heeft toegevoegd, bent u klaar om de transactie met de bestandsupload te configureren. Het uploaden van bestanden maakt gebruik van de actie **Instellen**. U moet deze actie aan de transactie toevoegen en deze vervolgens configureren om het bestand te uploaden:

1.  Navigeer naar de juiste transactiestapeditor door naar de controleregelopties te gaan en vervolgens naar het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}}.

2.  Voeg een **Instellen**-actie toe in de stap waarin het bestand moeten worden geüpload.

3.  Stel de juiste [CSS- of XPath-selector]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="nl" >}}) in om het bestandsuploadelement te selecteren. 

    {{< callout >}}**Opmerking**: Meestal is het juiste bestandsuploadelement voor interactie op de pagina een `input type="file"` element. In sommige gevallen kunnen deze elementen 'verborgen' zijn op de pagina, waar de gebruiker in plaats daarvan op een knop of koppeling klikt. De actie **Instellen** moet plaatsvinden op het feitelijke bestandsuploadelement op de pagina. Aangezien dergelijke elementen niet altijd zichtbaar zijn, is het een goed idee om de optie **Wacht tot** in de **Instellen**-actie om te zetten van de standaardwaarde *Het element is zichtbaar en actief* naar *Het element bestaat*.{{< /callout >}} 

4.  Klik op de knop met de drie stippen naast **Nieuwe waarde** om het dialoogvenster te openen waarin u de elementwaarde op kunt geven.

5.  Klik op **Upload vaultbestand** en selecteer het juiste bestand. Als u meer dan één bestand in uw kluis heeft, worden deze per vault-sectie vermeld.

    ![screenshot van waardekiezer instellenactie](/img/content/scr-page-interactions-fileupload-vault.min.png)

Hiermee wordt een bestandsupload opgenomen in de transactie. Vanaf hier kunt u doorgaan met het bouwen van de transactie zoals u dat normaal zou doen.

![Bestandsupload](/img/content/scr-page-interactions-fileupload.min.png)


### Opties voor instellenacties {id="setaction-options"}

U beschikt over verschillende opties voor de actie Instellen. 


- **Omschrijving** — Een omschrijving van de actie die wordt gebruikt voor rapportagedoeleinden.
- **Foutmelding** — Het bericht dat wordt opgenomen in foutrapporten, in het geval van een fout.
- **Foutafhandeling** — Selecteren van het selectievakje **Negeer fouten die in deze actie optreden** vertelt de controleregel fouten te negeren die deze actie kan tegenkomen, zoals het niet vinden van het klikbare element.
- **Wacht tot** — Voordat een klikactie kan plaatsvinden, moet het element waarop de controleregel moet klikken, worden gerenderd en zichtbaar zijn op de pagina (in CSS-termen: het element moet worden weergegeven en zichtbaar zijn). Deze *wachtcondities* hebben een [eigen Knowledge Base-artikel]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}), waar u informatie kunt vinden over de verschillende opties.
- **Wachttijd** — U kunt opgeven hoelang de controleregel moet wachten tot het element voldoet aan de bovenstaande vereiste Wacht tot. De standaard wachttijd is 30 seconden, maar u kunt de standaard overschrijven met een maximale wachttijd van 60 seconden.
- **Variabele toewijzen** — Voer een variabelenaam in het formaat `{{name}}` in. Deze variabele bevat de waarde die binnen deze actie was ingesteld. U kunt deze variabele dan in een latere stap of actie gebruiken.
- **Shadow DOM host** — Als het element waarmee moet worden geïnteracteerd in een shadow DOM bestaat, moet de transactie worden geconfigureerd om te zoeken naar het element binnen die shadow DOM. U kunt meer informatie vinden in ons KB-artikel over [werken met een shadow DOM in uw transactie]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}).

## Hoveren {id="hover"}

Wanneer een pagina elementen bevat waarbij de gebruiker de aanwijzer erover moet bewegen om een actie uit te voeren zoals het selecteren van een submenu of het selecteren in een vervolgkeuzelijst, moet u een **hoveractie** toevoegen. Voordat de gebruiker of controleregel kan interacteren met een onderliggend element, zoals koppelingen in een drop-down-/pull-downmenu, moet het element zichtbaar zijn op de pagina.

Omdat de cursor altijd op de pagina staat tijdens de transactie-opname, zou de recorder constant hovergebeurtenissen opnemen die u achteraf zou moeten verwijderen. In plaats van mogelijk honderden onnodige hovergebeurtenissen te verwijderen, neemt de recorder geen hoveracties op. Daarom moet u eventuele vereiste hoveracties achteraf toevoegen.

Om in het onderstaande voorbeeld toegang te krijgen tot het menu voor het selecteren van de afrekenoptie moet u eerst de aanwijzer over de winkelwagen laten zweven (hoveren).

![Hover voorbeeld](/img/content/78c2d8f8-3fb0-44ed-a056-bb9231334f6c.gif)

### Opties voor hoveracties

U heeft de volgende opties voor de hoveractie (zie onderstaande afbeelding):

- **Omschrijving**: een omschrijving van de actie die wordt gebruikt voor rapportagedoeleinden.
- **Foutmelding**: het bericht dat wordt opgenomen in foutrapporten, in het geval van een fout.
- **Foutafhandeling**: selecteren van het selectievakje **Negeer fouten die in deze actie optreden** vertelt de controleregel fouten te negeren die deze actie kan tegenkomen, zoals het niet vinden van het klikbare element.
- **Wacht tot**: voordat een klikactie kan plaatsvinden, moet de browser het element renderen waardoor het zichtbaar wordt op de pagina. Deze *wachtcondities* hebben een [eigen knowledgebase-artikel]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}), waar u informatie kunt vinden over de verschillende opties.
- **Wachttijd**: u kunt opgeven hoelang de controleregel moet wachten tot het element voldoet aan de bovenstaande vereiste Wacht tot. De standaard wachttijd is 30 seconden, maar u kunt de standaard overschrijven met een maximale wachttijd van 60 seconden.
- **Shadow DOM host**: Als het element waarmee moet worden geïnteracteerd in een shadow DOM bestaat, moet de transactie worden geconfigureerd om te zoeken naar het element binnen die shadow DOM. U kunt meer informatie vinden in ons knowledgebase-artikel over [werken met een shadow DOM in uw transactie]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}).

![Pagina-interacties - hoveren](/img/content/scr-page-interactions-hover.min.png)

### Gebruik inhoudcontroles na hoveracties

Als u wilt controleren op een geslaagde hoveractie (het submenu is correct geladen), kunt u overwegen om direct na de hoveractie een inhoudcontrole-actie toe te voegen om te verifiëren dat de controleregel met het menu kan communiceren voordat u verdergaat.

## Toetsenbordgebeurtenis {id="key-event"}

Met de actie *Toetsenbordgebeurtenis* kunt u een enkele toetsaanslag toevoegen aan een transactiestap. Deze actie kan handig zijn als er een element op uw webpagina staat dat geen klikbaar element (knop) heeft, bijvoorbeeld om een zoekterm in te dienen als er geen knop aanwezig is om de zoekopdracht in te dienen. 

Voeg in een transactiestap een nieuwe actie toe en kies de actie *Toetsenbordgebeurtenis* in de lijst met pagina-interacties. In de nieuwe actie moet u een teken kiezen uit de lijst met beschikbare tekens. Voer een [CSS-selector of XPath]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="nl" >}}) in om het element te identificeren waarin u de toets wilt invoeren. 

### Opties voor Toetsenbordgebeurtenissen

De volgende instellingen zijn beschikbaar in een stap voor de actie *Toetsenbordgebeurtenis*:

- **Omschrijving** — Een omschrijving van de actie die wordt gebruikt voor rapportagedoeleinden.
- **Foutmelding** — Het bericht dat wordt opgenomen in foutrapporten, in het geval van een fout.
- **Foutafhandeling** — Selecteren van het selectievakje **Negeer fouten die in deze actie optreden** vertelt de controleregel fouten te negeren die deze actie kan tegenkomen, zoals het niet vinden van het klikbare element.
- **Wacht tot** — Voordat een actie kan plaatsvinden, moet het element waarmee de controleregel moet interacteren, worden gerenderd en zichtbaar zijn op de pagina (in CSS-termen: het element moet worden weergegeven en zichtbaar zijn). Deze *wachtcondities* hebben een [eigen knowledgebase-artikel]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}), waar u informatie kunt vinden over de verschillende opties.
- **Wachttijd** — U kunt opgeven hoelang de controleregel moet wachten tot het element voldoet aan de bovenstaande Wacht tot-vereiste. De standaard wachttijd is 30 seconden, maar u kunt de standaard overschrijven met een maximale wachttijd van 60 seconden.
- **Shadow DOM host** — Als het element waarmee moet worden geïnteracteerd in een shadow DOM bestaat, moet de transactie worden geconfigureerd om te zoeken naar het element binnen die shadow DOM. U kunt meer informatie vinden in ons knowledgebase-artikel over [werken met een shadow DOM in uw transactie]({{< ref path="/support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}).

![Toetsenbordgebeurtenis voorbeeld](/img/content/scr-page-interactions-keyevent.min.png)
