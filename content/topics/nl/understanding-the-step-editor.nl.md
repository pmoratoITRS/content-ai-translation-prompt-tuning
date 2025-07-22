{
  "hero": {
    "title": "De stap-editor begrijpen"
  },
  "title": "De stap-editor begrijpen",
  "summary": "De stap-editor wordt gebruikt om de stappen en acties van een transactiescript te bewerken.",
  "url": "/support/kb/synthetic-monitoring/transacties/de-stap-editor-begrijpen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/understanding-the-step-editor"
}

De transactiestap-editor is nodig om de stappen en acties van een transactiescript te bewerken. Deze kan worden gebruikt als visuele editor die een UI heeft waarmee u stappen kunt toevoegen en bewerken, of als scripteditor die een gewone teksteditor is. 

Als u zich op uw gemak voelt met het schrijven van uw eigen script, bekijk dan [Broncode rechtstreeks scripten]({{< ref path="#scripting-source-code-directly" lang="nl" >}}) voor meer informatie over de scripteditor.

In de meeste gevallen zult u geen script schrijven, maar [de transaction recorder gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}) om een eerste opzet van uw script te maken en vervolgens de stap-editor gebruiken om de transactie te verfijnen.

{{< callout >}}
**Opmerking**: Uptrends gebruikt transactiecredits om de prijs van uw transactiecontroleregels te bepalen. Het aantal credits dat voor een controleregel wordt gebruikt, wordt weergegeven achter de controleregelnaam in het overzicht *Controleregels* (Ga naar {{< AppElement type="menuitem" >}} *Transacties > Transacties beheren* {{< /AppElement >}}). U kunt volledige uitleg over credits vinden in het knowledgebase-artikel [Berekenen van credits voor transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="nl" >}}).
{{< /callout >}}

## Stappen en acties

Het script van een transactiecontroleregel bevat stappen (van de transactie die u wilt monitoren). Binnen de stappen vindt u acties, dit zijn de microstappen in uw transactie.

De stappen en acties bewerken:

1. Ga naar {{< AppElement type="menuitem" >}} *Transacties > Transacties beheren* {{< /AppElement >}}.
2. Open het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}}.

![screenshot transactiestap-editor](/img/content/scr_transaction-step-editor-041024.min.png)

 U verfijnt en test uw transactiescript op het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}}, of u kunt uw script hier ook helemaal opnieuw schrijven. Hiervoor gebruikt u de knop {{< AppElement type="buttonSecondary" >}} NAAR SCRIPT SCHAKELEN {{< /AppElement >}} in de rechter bovenhoek van de editor.

Als u uw script heeft geüpload vanuit de [transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}), ziet u een of meer stappen met reeds gedefinieerde acties. Als u uw script helemaal zelf creëert, bouwt u elke stap in uw transactie uit met de stap-editor. Het wordt aanbevolen de transaction recorder te gebruiken om u een goede basis te geven om mee te beginnen.

Uw transactiescript is opgebouwd uit *stappen* en *acties*. Hier wordt uitgelegd wat wordt bedoeld met stappen en acties.

## Wat is een stap?

Wanneer u uw script uploadt vanuit de transaction recorder, definieert Uptrends automatisch uw stappen voor u. Maar wat is een stap? Een stap is een willekeurige groepering van acties in uw transactiescript. Meestal wilt u gebruikersinteracties met uw pagina groeperen in stappen die eindigen met een server request, zoals het indienen van een formulier. Het groeperen van acties op server submits/requests helpt bij het oplossen van problemen en het rapporteren van performance.

U kunt een stap ook zien als een statusovergang in de browser, d.w.z. een actie die resulteert in een nieuwe pagina of de pagina vernieuwt met nieuwe inhoud. Maar u kunt uw stappen instellen om werkelijk elke groepering weer te geven die zinvol is voor uw gebruikssituatie en rapportagebehoeften.

### Stap-instellingen {id="step-settings"}

Klik op het pijltje **>** naast de stapnaam voor toegang tot de stapacties en -instellingen.

![screenshot enkele stap in script](/img/content/scr_transaction-single-step-041024.min.png)

Binnen elke stap worden verschillende instellingen weergegeven:

- **Waterval** - U kunt een optioneel [Waterval]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}})-rapport toevoegen om het laden van de pagina, **Core Web Vitals** en **W3C Prestatiekengetallen** van elke transactiestap weer te geven. Elk watervalrapport gebruikt één [transactiestapcredit]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="nl" >}}). Om deze instelling in te schakelen vinkt u het selectievakje **Waterval** aan en past u het volgende naar uw behoeften aan:

  1. **Naam** — geef een beschrijvende naam op voor elke stap. Bijvoorbeeld, *Toevoegen aan winkelwagen*, *Inloggen* of *Afspraaktijd aanvragen*.

  2. **Foutafhandeling** — als u uw transactiestappen of scripts met paginafouten wilt blijven uitvoeren, kunt u dit doen door de optie **Negeer alle fouten die in deze stap optreden** aan te vinken. Uptrends gaat door naar de volgende stap, ongeacht het resultaat van de huidige stap. Uw scherm **Details van de controle** toont de fout, maar de Transactiecontroleregel gaat door ondanks de fout. Raadpleeg voor meer informatie [Negeer fouten gebruiken bij optionele stappen en acties]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="nl" >}}).

  3. **Prestatiekengetallen** - vink deze optie aan om deze in te schakelen en **Core Web Vitals en W3C scores op te slaan als aparte kengetallen** in uw Transactiecontroleregels. Met deze optie kunt u dergelijke [kengetallen]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/monitoring-results-overview" lang="nl" >}}) weergeven in uw [Eenvoudige lijst/grafiek of lijst van aangepaste rapporttegels]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="nl" >}}) als u op het pictogram {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} klikt.


- **Filmstrip** - U kunt optionele [Tijdlijnscreenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}}) (ook bekend als een filmstrip) per stap toevoegen. Een filmstrip gebruikt één [transactiestapcredit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}) tenzij er al één screenshot in de stap staat. In dat geval wordt de filmstrip gratis verstrekt.

- **Screenshot** - Met een optionele [screenshot]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}}) kunt u het scherm zien zoals ervaren door uw gebruiker het aan het einde van de stap. U kunt één screenshot inschakelen door de *Bediening*-[actie](#adding-an-action) **Screenshot** toe te voegen. Een screenshot gebruikt één [transactiestapcredit]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}).

- **Paginabron** - Kies deze optie om de paginabroninformatie en eventuele console log-data op te halen die zijn gegenereerd tijdens de uitvoering van die stap. Houd er rekening mee dat de paginabron alleen beschikbaar is in combinatie met de waterval.


### Stappen toevoegen

Een nieuwe stap aan uw script toevoegen:

1. Scroll naar de onderkant van het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="button" >}}STAP TOEVOEGEN{{< /AppElement >}}.
3. Geef de nieuwe en momenteel lege stap een naam.
4. (Optioneel) Pak de stap vast door op de handgreep te klikken (verticale stippellijnen links van de stapnaam) en sleep de stap naar de gewenste locatie in de sequentie binnen het script. 
5. Voeg acties toe. Meer informatie over acties vindt u in de volgende paragraaf.
6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om uw wijzigingen op te slaan.

## Wat is een actie?

Acties zijn uw gebruikersinteracties, inhoudcontroles en browserinteracties die binnen een stap plaatsvinden. Ze zijn onderverdeeld in de categorieën Interactie, Test en Bediening.

#### Interactie

De acties van het type *Interactie* zijn in het kort:

- **Navigeer** — ga naar een specifieke URL
- **Klik** — zoek een pagina-element zoals (radio)knoppen of selectievakjes en voer een muisklik uit 
- **Instellen** — zoek en vul een tekstveld, tekstgebied, wachtwoordveld, enz. 
- **Hover** — zoek een element en beweeg de cursor over het element om andere verborgen pagina-elementen te onthullen 
- **Toetsenbordgebeurtenis** — voer een enkele toetsaanslag uit, b.v. een element heeft geen klikbare knop

Deze worden uitgebreid beschreven in het knowledgebase-artikel [Pagina-interacties]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="nl" >}}).


#### Test

De acties van het type *Test* zijn inhoudcontroles of voeren een wachtactie in.

- **Inhoud van een element** — zoek en controleer een element op specifieke inhoud 
- **Inhoud van het document** — controleer het hele paginadocument op opgegeven inhoud 
- **Wacht op element** — zoek naar en wacht op een opgegeven pagina-element 
- **Wacht een vaste tijd** — voeg een aangepaste wachttijd toe 

Raadpleeg de knowledgebase-artikelen [Inhoudcontroles]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}}) in transactiemonitoring en [Wachtvoorwaarden gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/using-wait-conditions" lang="nl" >}}) om te leren wat ze eigenlijk doen.

#### Bediening

De actiecategorie *Bediening* bevat de volgende opties:

- **Screenshot** — maak een screenshot van het huidige scherm 
- **Schakelen tussen browsertabbladen** — focus op het nieuwe venster/tabblad als uw pagina een ander browservenster heeft geopend
- **Schakel naar frame** — hiermee kunt u [schakelen tussen iFrames]({{< ref path="support/kb/synthetic-monitoring/transactions/switching-between-iframes-browser-tabs" lang="nl" >}}) op uw pagina 
- **Scroll** — zoek een pagina-element en scroll naar de positie op de pagina (vooral handig bij het gebruik van screenshots)
- **Inhoud variabele aanpassen** — wijzig een bestaande variabele met de actie [Inhoud van variabele aanpassen]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="nl" >}})
- **Browsercache legen** — [leegt de browsercache]({{< ref path="/support/kb/synthetic-monitoring/transactions/clear-browser-cache" lang="nl" >}}) om pagina-elementen rechtstreeks vanaf de server opnieuw te laden in plaats van uit de browsercache

### Een actie toevoegen {id="adding-action"}

Een nieuwe actie toevoegen aan een van de stappen in uw transactiecontroleregel:

1. Open de stap waaraan u een actie wilt toevoegen.
2. Klik op de knop {{< AppElement type="buttonSecondary" >}}ACTIE TOEVOEGEN{{< /AppElement >}}. 
   Het pop-upvenster *Actie toevoegen* verschijnt:
   ![screenshot pop-upvenster actie toevoegen](/img/content/scr_add-action-popup.min.png)
   Als u over de actieoptie hovert, krijgt u meer informatie over die actie. 
3. Klik op de actie die u aan uw stap wilt toevoegen. 
4. (Optioneel) Pas indien nodig de volgorde van de acties aan. Pak de actie vast door op de handgreep te klikken (verticale stippellijnen links van de actienaam) en sleep de actie naar de gewenste locatie in de reeks acties. U kunt de actie desgewenst ook naar een andere stap slepen.
5. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om uw wijzigingen op te slaan.

### CSS-selectors en XPath queries {id="css-selectors-and-xpath-queries"}

Het is u misschien opgevallen dat sommige acties CSS-selectors of XPath queries tonen. Deze vertellen de transactiecontroleregel precies met welk schermelement hij moet interacteren om de actie te voltooien. Als u de transaction recorder heeft gebruikt, heeft deze al gekozen wat volgens hem de beste methode is om een element op uw pagina te vinden, zoals beschreven in het knowledgebase-artikel [Selector voor de transaction recorder bepalen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="nl" >}}). 

Het algoritme kiest echter niet altijd in alle gevallen de beste optie, maar u kunt de andere opties die de recorder heeft gekozen vinden door te klikken op de knop {{< AppElement type="button" >}}\[...\]{{< /AppElement >}} in het selectorwaardeveld. 

Een andere optie is om uw eigen selectors of queries te schrijven. Lees meer over [CSS-selectors](https://www.w3schools.com/cssref/css_selectors.asp) of [XPath queries](https://www.w3schools.com/xml/xpath_intro.asp). Bij het handmatig definiëren van de selectors kunt u gebruikmaken van [automatische variabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}). Dit geeft u nog meer flexibiliteit in de selectorkeuze. 

Als u niet vertrouwd bent met CSS-selectors en XPath queries, neem dan contact op met [Uptrends Support]({{< ref path="contact" lang="nl" >}}) om hen de benodigde wijzigingen te laten aanbrengen.

### Actie-instellingen

Uw acties hebben verschillende instellingen op basis van het type actie. Bekijk het knowledgebase-artikel [Pagina-interacties]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="nl" >}}) voor meer informatie over alle instellingen voor elk van deze acties.


## Broncode rechtstreeks scripten {id="scripting-source-code-directly"}

U kunt uw scripts altijd in een andere editor of omgeving schrijven en het script knippen en plakken (of het script rechtstreeks in onze teksteditor schrijven). Gebruik de knop {{< AppElement type="buttonSecondary" >}}Naar script schakelen{{< /AppElement >}} boven aan het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}} om de teksteditor te openen. Aangekomen in de teksteditor klikt u op de knop {{< AppElement type="buttonSecondary" >}}Naar visuele editor schakelen{{< /AppElement >}} om terug te gaan. Wanneer u tussen deze modi schakelt, wordt het script gevalideerd.

![screenshot weergave visuele en scripteditor](/img/content/scr_transaction-visual-script-editor-041024.min.png)

## Gebruik de transactie-API

U kunt de Uptrends' API gebruiken om controleregels te creëren, scripts te uploaden, scripts te wijzigen en de status van uw controleregel te controleren. Raadpleeg de [API]({{< ref path="support/kb/api" lang="nl" >}})-documentatie voor meer informatie over alle beschikbare methoden.
