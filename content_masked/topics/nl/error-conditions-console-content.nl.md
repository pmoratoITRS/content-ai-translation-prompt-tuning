{
  "hero": {
    "title": "Foutcondities - Console-inhoud"
  },
  "title": "Foutcondities - Console-inhoud",
  "summary": "U kunt controleregelchecks en het genereren van fouten baseren op de inhoud van de console log van uw browser.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-console-inhoud",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Elke controleregel voert enkele standaardcontroles uit, die afhankelijk zijn van het controleregeltype. Bovendien kunt u in de foutcondities van een controleregel aangepaste controles definiëren om alerts voor specifieke situaties te genereren. Het Knowledge Base-artikel [Foutcondities]([LINK_URL_1]) legt uit wat ze zijn en hoe ze te gebruiken.

In dit artikel wordt uitgelegd hoe de foutcondities van de categorie *Inhoud console* werken. In een controleregel kunt u ze vinden op het tabblad [SHORTCODE_1]Foutcondities[SHORTCODE_2] in het gedeelte *Inhoud console controleren*. Houd er rekening mee dat niet alle controleregels alle types foutcondities hebben. In de tabel in [Welke foutcondities zijn beschikbaar?]([LINK_URL_2]) kunt u zien welke opties beschikbaar zijn in bepaalde controleregeltypes.

## De console log van de browser 

Wanneer een webpagina in een browser wordt geladen, legt de console log van de browser alle logberichten vast. U vindt deze berichten in bijvoorbeeld Chrome door op de toets "F12" te drukken om DevTools te openen en vervolgens naar het tabblad *Console* te gaan. De logberichten kunnen van het type info, waarschuwing of fout zijn (fout bij het laden van elementen, javascriptfout, enz.). Logberichten kunnen door de webontwikkelaar worden geïmplementeerd. 

U kunt foutcondities definiëren die zijn gebaseerd op het bestaan en eventueel de inhoud van de logberichten. Met deze foutcondities kunt u controleren of een logvermelding van het type info, waarschuwing of fout aanwezig is en ook of deze al dan niet een bepaalde tekst bevat. Er wordt een fout gegenereerd als aan de gedefinieerde voorwaarde wordt voldaan. 

Merk op dat deze foutconditie anders is dan de foutconditie [Pagina-inhoud controleren]([LINK_URL_3]), waarmee u de inhoud van de pagina zelf controleert.

## Consolebericht bestaat [ANCHOR_1]

Controleer of er een consolebericht bestaat en controleer optioneel of het bepaalde inhoud bevat.

Om deze foutconditie te definiëren:

1. Ga naar [SHORTCODE_3] Monitoring > Controleregels beheren [SHORTCODE_4].
2. Klik op de naam van de controleregel om deze te bewerken.
3. Open het tabblad [SHORTCODE_5] Foutcondities [SHORTCODE_6].
4. Klik in het gedeelte *Inhoud console controleren* op de knop [SHORTCODE_7] \+ Nieuwe controle [SHORTCODE_8] om een nieuwe controle toe te voegen.

    ![screenshot console-inhoud controleren]([LINK_URL_4])

5. Selecteer de optie **Fout als de console bepaalde inhoud bevat**.  
6. Kies het berichtniveau (info, fout, waarschuwing). 
7. De **Berichttekst** werkt als volgt: als u dit leeg laat, checkt de controleregel alleen of er een logvermelding van het gekozen berichtniveau bestaat, ongeacht de inhoud ervan. Als u wilt controleren op bepaalde inhoud in de log entry, moet u in de **Berichttekst** de tekst invoeren waarop u wilt controleren. Dit kan een woord, zinsdeel of reguliere expressie zijn. 
8. Voeg desgewenst meer controles toe.
9. Klik op de knop [SHORTCODE_9] Opslaan [SHORTCODE_10] om alle wijzigingen in de controleregel op te slaan. 

## Consolebericht bestaat niet

In plaats van te controleren op het bestaan van logberichten en eventueel bepaalde inhoud, wilt u misschien (ook) controleren op het niet-bestaan van logberichten en (optioneel) de inhoud ervan.

Gebruik de stappen zoals beschreven voor [Consolebericht bestaat]([LINK_URL_5]), maar selecteer de optie **Fout als de console bepaalde inhoud niet bevat**. 

Kies vervolgens op welk logberichtniveau (info, fout, waarschuwing) u wilt controleren. Als u **Berichttekst** leeg laat, genereert deze conditie een fout als er geen logberichten van dat niveau bestaan. Als u een **Berichttekst** invult, wordt er een fout gegenereerd als er geen logbericht van dat niveau en met de gegeven tekst is.

## Resultaten van een console-inhoud check

De controleregel voert de controle uit, rekening houdend met uw instellingen voor deze foutconditie. U kunt de resultaten bekijken door de [Details van de controle]([LINK_URL_6]) te openen. Als de controle een fout heeft geretourneerd in plaats van "OK", zal de informatie in de controledetails u helpen te begrijpen welke foutconditie een fout heeft veroorzaakt en informatie kunnen geven over waar u moet beginnen met uw probleemoplossing.

