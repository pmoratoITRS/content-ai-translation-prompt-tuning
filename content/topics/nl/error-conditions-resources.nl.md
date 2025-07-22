{
  "hero": {
    "title": "Foutcondities - Resources"
  },
  "title": "Foutcondities - Resources",
  "summary": "Een overzicht van de beschikbare foutcondities voor de categorie *Resources*. De resources zijn de elementen die uw webpagina laadt om deze zichtbaar en functioneel te maken.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-resources",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-resources"
}

Elke controleregel voert enkele standaardcontroles uit, die afhankelijk zijn van het controleregeltype. Bovendien kunt u in de foutcondities van een controleregel aangepaste controles definiëren om alerts voor specifieke situaties te genereren. Het Knowledge Base-artikel [Foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) legt uit welke dat zijn en hoe u ze gebruikt.

In dit artikel wordt uitgelegd hoe de foutcondities van de categorie *Resource* werken. In een controleregel kunt u ze vinden op het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}} in het gedeelte *Resources controleren*. Houd er rekening mee dat niet alle controleregels alle foutcondities hebben. Bekijk de tabel in [Welke foutcondities zijn beschikbaar?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) om te achterhalen welke opties beschikbaar zijn in bepaalde controleregeltypes.

## Wat is een resourcecontrole?

Uw website is afhankelijk van een aantal resources (afbeeldingen, stylesheets, scripts, enz.) die moeten worden geladen. De resources zijn de elementen die moeten worden geladen voor uw website. Een controleregelcheck retourneert informatie over de omvang (in kilobytes) van de response van de server. De paginaomvang (samen met een inhoud match) kan aangeven of een pagina volledig werd geladen of niet. 

Onverwachte (kleine of grote) formaten kunnen ook een aanwijzing zijn voor frauduleuze paginamanipulatie. Bij een Full Page Check of een transactiecontroleregel krijgt u een [watervalgrafiek]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}) wat een visuele weergave is van het laadproces van de elementen. De grafiek bevat de statistieken en enkele details van de monitoringcheck.

Met de foutcondities in het gedeelte **Resources controleren** stelt u een grenswaarde in voor de totale omvang of een percentage van individuele resources die mogelijk niet worden geladen voordat u oordeelt dat de website een probleem heeft. 

## Controleer de omvang van de inhoud (HTTP(S)- en Webservice HTTP(S)-controleregels)

Voor HTTP(S)- of Webservice HTTP(S)-controleregels kunt u een foutconditie definiëren die de minimale omvang van de inhoud controleert.

![screenshot resources HTTPS(S) of webservices controleren](/img/content/scr_errorconditions-resources-https.min.png)

## Controleer het totaal van alle resources gezamenlijk (Full Page Check)

U kunt een maximale en een minimale omvang (in kB) instellen om terug te komen in de server response. Kies de optie **Controleer het totaal van alle resources gezamenlijk** in het gedeelte *Resources controleren*.

![screenshot foutconditie alle resources gezamenlijk](/img/content/scr_errorconditions-resources-all.min.png)

Stel een minimale omvang in door *Alle resources gezamenlijk zijn meer dan* te selecteren en de ondergrens (in kB) in te vullen. Als de omvang van alle pagina-elementen samen kleiner is dan dit getal, kan dit erop wijzen dat er inhoud op uw pagina ontbreekt en deze mogelijk niet correct functioneert.

Stel een maximale omvang in door *Alle resources gezamenlijk zijn minder dan* te selecteren en de bovengrens (in kB) die terugkomt in de server response in te vullen. Als de omvang van alle pagina-elementen gezamenlijk boven dit getal ligt, is er te veel inhoud. Dit kan een fout in uw inhoud zijn of een hint dat er inhoud op uw website is geplaatst zonder uw bedoeling en toestemming.

U kunt een foutconditie voor minimale en maximale omvang combineren. Voeg een nieuwe foutconditie toe door op de knop {{< AppElement type="buttonSecondary" >}} Nieuwe controle {{< /AppElement >}} te klikken.

## Controleer iedere resource afzonderlijk (Full Page Check)

Naast het controleren van het totaal van alle resources gezamenlijk, kunt u ook een controle uitvoeren op afzonderlijke elementen. Kies de optie **Controleer iedere resource afzonderlijk** en bepaal dan of u wilt controleren of een bepaald percentage resources helemaal niet kan worden geladen of dat een bepaald percentage van alle resources een maximale omvang overschrijdt. 

Merk op dat de kop van de resourcecontrole dynamisch is en na het kiezen van de opties en het invullen van uw limieten, geeft de kop weer wat u in de controle heeft gedefinieerd.

Om te controleren of een bepaald percentage resources mislukt kiest u de optie **Resource kan niet worden geladen** en vult u het percentage (bovengrens) in van resources die niet kunnen worden geladen. Boven deze limiet wordt een fout gegenereerd.

![screenshot foutconditie afzonderlijke resource mislukt](/img/content/scr_errorconditions-resources-individual-fail.min.png)

Om te controleren of sommige (een percentage) of alle resources gezamenlijk een bepaalde omvang overschrijden, kiest u de optie **Omvang van de resource is meer dan** en stelt u het percentage in, indien van toepassing. Als u het percentage instelt op 0%, wordt gecontroleerd of er een enkele resource is die de grenswaarde overschrijdt. Als u het percentage instelt op 100%, wordt gecontroleerd of alle resources gezamenlijk de grenswaarde overschrijden.

![screenshot foutconditie afzonderlijke resources zijn te groot](/img/content/scr_errorconditions-resources-individual-percentage.min.png)

