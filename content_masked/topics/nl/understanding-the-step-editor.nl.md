{
  "hero": {
    "title": "De stap-editor begrijpen"
  },
  "title": "De stap-editor begrijpen",
  "summary": "De stap-editor wordt gebruikt om de stappen en acties van een transactiescript te bewerken.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/de-stap-editor-begrijpen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De transactiestap-editor is nodig om de stappen en acties van een transactiescript te bewerken. Deze kan worden gebruikt als visuele editor die een UI heeft waarmee u stappen kunt toevoegen en bewerken, of als scripteditor die een gewone teksteditor is. 

Als u zich op uw gemak voelt met het schrijven van uw eigen script, bekijk dan [Broncode rechtstreeks scripten]([LINK_URL_1]) voor meer informatie over de scripteditor.

In de meeste gevallen zult u geen script schrijven, maar [de transaction recorder gebruiken]([LINK_URL_2]) om een eerste opzet van uw script te maken en vervolgens de stap-editor gebruiken om de transactie te verfijnen.

[SHORTCODE_1]
**Opmerking**: Uptrends gebruikt transactiecredits om de prijs van uw transactiecontroleregels te bepalen. Het aantal credits dat voor een controleregel wordt gebruikt, wordt weergegeven achter de controleregelnaam in het overzicht *Controleregels* (Ga naar [SHORTCODE_3] *Transacties > Transacties beheren* [SHORTCODE_4]). U kunt volledige uitleg over credits vinden in het knowledgebase-artikel [Berekenen van credits voor transactiecontroleregels]([LINK_URL_3]).
[SHORTCODE_2]

## Stappen en acties

Het script van een transactiecontroleregel bevat stappen (van de transactie die u wilt monitoren). Binnen de stappen vindt u acties, dit zijn de microstappen in uw transactie.

De stappen en acties bewerken:

1. Ga naar [SHORTCODE_5] *Transacties > Transacties beheren* [SHORTCODE_6].
2. Open het tabblad [SHORTCODE_7]Stappen[SHORTCODE_8].

![screenshot transactiestap-editor]([LINK_URL_4])

 U verfijnt en test uw transactiescript op het tabblad [SHORTCODE_9]Stappen[SHORTCODE_10], of u kunt uw script hier ook helemaal opnieuw schrijven. Hiervoor gebruikt u de knop [SHORTCODE_11] NAAR SCRIPT SCHAKELEN [SHORTCODE_12] in de rechter bovenhoek van de editor.

Als u uw script heeft geüpload vanuit de [transaction recorder]([LINK_URL_5]), ziet u een of meer stappen met reeds gedefinieerde acties. Als u uw script helemaal zelf creëert, bouwt u elke stap in uw transactie uit met de stap-editor. Het wordt aanbevolen de transaction recorder te gebruiken om u een goede basis te geven om mee te beginnen.

Uw transactiescript is opgebouwd uit *stappen* en *acties*. Hier wordt uitgelegd wat wordt bedoeld met stappen en acties.

## Wat is een stap?

Wanneer u uw script uploadt vanuit de transaction recorder, definieert Uptrends automatisch uw stappen voor u. Maar wat is een stap? Een stap is een willekeurige groepering van acties in uw transactiescript. Meestal wilt u gebruikersinteracties met uw pagina groeperen in stappen die eindigen met een server request, zoals het indienen van een formulier. Het groeperen van acties op server submits/requests helpt bij het oplossen van problemen en het rapporteren van performance.

U kunt een stap ook zien als een statusovergang in de browser, d.w.z. een actie die resulteert in een nieuwe pagina of de pagina vernieuwt met nieuwe inhoud. Maar u kunt uw stappen instellen om werkelijk elke groepering weer te geven die zinvol is voor uw gebruikssituatie en rapportagebehoeften.

### Stap-instellingen [ANCHOR_1]

Klik op het pijltje **>** naast de stapnaam voor toegang tot de stapacties en -instellingen.

![screenshot enkele stap in script]([LINK_URL_6])

Binnen elke stap worden verschillende instellingen weergegeven:

- **Waterval** - U kunt een optioneel [Waterval]([LINK_URL_7])-rapport toevoegen om het laden van de pagina, **Core Web Vitals** en **W3C Prestatiekengetallen** van elke transactiestap weer te geven. Elk watervalrapport gebruikt één [transactiestapcredit]([LINK_URL_8]). Om deze instelling in te schakelen vinkt u het selectievakje **Waterval** aan en past u het volgende naar uw behoeften aan:

  1. **Naam** — geef een beschrijvende naam op voor elke stap. Bijvoorbeeld, *Toevoegen aan winkelwagen*, *Inloggen* of *Afspraaktijd aanvragen*.

  2. **Foutafhandeling** — als u uw transactiestappen of scripts met paginafouten wilt blijven uitvoeren, kunt u dit doen door de optie **Negeer alle fouten die in deze stap optreden** aan te vinken. Uptrends gaat door naar de volgende stap, ongeacht het resultaat van de huidige stap. Uw scherm **Details van de controle** toont de fout, maar de Transactiecontroleregel gaat door ondanks de fout. Raadpleeg voor meer informatie [Negeer fouten gebruiken bij optionele stappen en acties]([LINK_URL_9]).

  3. **Prestatiekengetallen** - vink deze optie aan om deze in te schakelen en **Core Web Vitals en W3C scores op te slaan als aparte kengetallen** in uw Transactiecontroleregels. Met deze optie kunt u dergelijke [kengetallen]([LINK_URL_10]) weergeven in uw [Eenvoudige lijst/grafiek of lijst van aangepaste rapporttegels]([LINK_URL_11]) als u op het pictogram [SHORTCODE_13] [SHORTCODE_14] klikt.


- **Filmstrip** - U kunt optionele [Tijdlijnscreenshots]([LINK_URL_12]) (ook bekend als een filmstrip) per stap toevoegen. Een filmstrip gebruikt één [transactiestapcredit]([LINK_URL_13]) tenzij er al één screenshot in de stap staat. In dat geval wordt de filmstrip gratis verstrekt.

- **Screenshot** - Met een optionele [screenshot]([LINK_URL_14]) kunt u het scherm zien zoals ervaren door uw gebruiker het aan het einde van de stap. U kunt één screenshot inschakelen door de *Bediening*-[actie]([LINK_URL_15]) **Screenshot** toe te voegen. Een screenshot gebruikt één [transactiestapcredit]([LINK_URL_16]).

- **Paginabron** - Kies deze optie om de paginabroninformatie en eventuele console log-data op te halen die zijn gegenereerd tijdens de uitvoering van die stap. Houd er rekening mee dat de paginabron alleen beschikbaar is in combinatie met de waterval.


### Stappen toevoegen

Een nieuwe stap aan uw script toevoegen:

1. Scroll naar de onderkant van het tabblad [SHORTCODE_15]Stappen[SHORTCODE_16].
2. Klik op de knop [SHORTCODE_17]STAP TOEVOEGEN[SHORTCODE_18].
3. Geef de nieuwe en momenteel lege stap een naam.
4. (Optioneel) Pak de stap vast door op de handgreep te klikken (verticale stippellijnen links van de stapnaam) en sleep de stap naar de gewenste locatie in de sequentie binnen het script. 
5. Voeg acties toe. Meer informatie over acties vindt u in de volgende paragraaf.
6. Klik op de knop [SHORTCODE_19] Opslaan [SHORTCODE_20] om uw wijzigingen op te slaan.

## Wat is een actie?

Acties zijn uw gebruikersinteracties, inhoudcontroles en browserinteracties die binnen een stap plaatsvinden. Ze zijn onderverdeeld in de categorieën Interactie, Test en Bediening.

#### Interactie

De acties van het type *Interactie* zijn in het kort:

- **Navigeer** — ga naar een specifieke URL
- **Klik** — zoek een pagina-element zoals (radio)knoppen of selectievakjes en voer een muisklik uit 
- **Instellen** — zoek en vul een tekstveld, tekstgebied, wachtwoordveld, enz. 
- **Hover** — zoek een element en beweeg de cursor over het element om andere verborgen pagina-elementen te onthullen 
- **Toetsenbordgebeurtenis** — voer een enkele toetsaanslag uit, b.v. een element heeft geen klikbare knop

Deze worden uitgebreid beschreven in het knowledgebase-artikel [Pagina-interacties]([LINK_URL_17]).


#### Test

De acties van het type *Test* zijn inhoudcontroles of voeren een wachtactie in.

- **Inhoud van een element** — zoek en controleer een element op specifieke inhoud 
- **Inhoud van het document** — controleer het hele paginadocument op opgegeven inhoud 
- **Wacht op element** — zoek naar en wacht op een opgegeven pagina-element 
- **Wacht een vaste tijd** — voeg een aangepaste wachttijd toe 

Raadpleeg de knowledgebase-artikelen [Inhoudcontroles]([LINK_URL_18]) in transactiemonitoring en [Wachtvoorwaarden gebruiken]([LINK_URL_19]) om te leren wat ze eigenlijk doen.

#### Bediening

De actiecategorie *Bediening* bevat de volgende opties:

- **Screenshot** — maak een screenshot van het huidige scherm 
- **Schakelen tussen browsertabbladen** — focus op het nieuwe venster/tabblad als uw pagina een ander browservenster heeft geopend
- **Schakel naar frame** — hiermee kunt u [schakelen tussen iFrames]([LINK_URL_20]) op uw pagina 
- **Scroll** — zoek een pagina-element en scroll naar de positie op de pagina (vooral handig bij het gebruik van screenshots)
- **Inhoud variabele aanpassen** — wijzig een bestaande variabele met de actie [Inhoud van variabele aanpassen]([LINK_URL_21])
- **Browsercache legen** — [leegt de browsercache]([LINK_URL_22]) om pagina-elementen rechtstreeks vanaf de server opnieuw te laden in plaats van uit de browsercache

### Een actie toevoegen [ANCHOR_2]

Een nieuwe actie toevoegen aan een van de stappen in uw transactiecontroleregel:

1. Open de stap waaraan u een actie wilt toevoegen.
2. Klik op de knop [SHORTCODE_21]ACTIE TOEVOEGEN[SHORTCODE_22]. 
   Het pop-upvenster *Actie toevoegen* verschijnt:
   ![screenshot pop-upvenster actie toevoegen]([LINK_URL_23])
   Als u over de actieoptie hovert, krijgt u meer informatie over die actie. 
3. Klik op de actie die u aan uw stap wilt toevoegen. 
4. (Optioneel) Pas indien nodig de volgorde van de acties aan. Pak de actie vast door op de handgreep te klikken (verticale stippellijnen links van de actienaam) en sleep de actie naar de gewenste locatie in de reeks acties. U kunt de actie desgewenst ook naar een andere stap slepen.
5. Klik op de knop [SHORTCODE_23] Opslaan [SHORTCODE_24] om uw wijzigingen op te slaan.

### CSS-selectors en XPath queries [ANCHOR_3]

Het is u misschien opgevallen dat sommige acties CSS-selectors of XPath queries tonen. Deze vertellen de transactiecontroleregel precies met welk schermelement hij moet interacteren om de actie te voltooien. Als u de transaction recorder heeft gebruikt, heeft deze al gekozen wat volgens hem de beste methode is om een element op uw pagina te vinden, zoals beschreven in het knowledgebase-artikel [Selector voor de transaction recorder bepalen]([LINK_URL_24]). 

Het algoritme kiest echter niet altijd in alle gevallen de beste optie, maar u kunt de andere opties die de recorder heeft gekozen vinden door te klikken op de knop [SHORTCODE_25]\[...\][SHORTCODE_26] in het selectorwaardeveld. 

Een andere optie is om uw eigen selectors of queries te schrijven. Lees meer over [CSS-selectors]([LINK_URL_25]) of [XPath queries]([LINK_URL_26]). Bij het handmatig definiëren van de selectors kunt u gebruikmaken van [automatische variabelen]([LINK_URL_27]). Dit geeft u nog meer flexibiliteit in de selectorkeuze. 

Als u niet vertrouwd bent met CSS-selectors en XPath queries, neem dan contact op met [Uptrends Support]([LINK_URL_28]) om hen de benodigde wijzigingen te laten aanbrengen.

### Actie-instellingen

Uw acties hebben verschillende instellingen op basis van het type actie. Bekijk het knowledgebase-artikel [Pagina-interacties]([LINK_URL_29]) voor meer informatie over alle instellingen voor elk van deze acties.


## Broncode rechtstreeks scripten [ANCHOR_4]

U kunt uw scripts altijd in een andere editor of omgeving schrijven en het script knippen en plakken (of het script rechtstreeks in onze teksteditor schrijven). Gebruik de knop [SHORTCODE_27]Naar script schakelen[SHORTCODE_28] boven aan het tabblad [SHORTCODE_29]Stappen[SHORTCODE_30] om de teksteditor te openen. Aangekomen in de teksteditor klikt u op de knop [SHORTCODE_31]Naar visuele editor schakelen[SHORTCODE_32] om terug te gaan. Wanneer u tussen deze modi schakelt, wordt het script gevalideerd.

![screenshot weergave visuele en scripteditor]([LINK_URL_30])

## Gebruik de transactie-API

U kunt de Uptrends' API gebruiken om controleregels te creëren, scripts te uploaden, scripts te wijzigen en de status van uw controleregel te controleren. Raadpleeg de [API]([LINK_URL_31])-documentatie voor meer informatie over alle beschikbare methoden.
