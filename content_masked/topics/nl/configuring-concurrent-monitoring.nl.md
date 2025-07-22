{
  "hero": {
    "title": "Gelijktijdige monitoring configureren"
  },
  "title": "Gelijktijdige monitoring configureren",
  "summary": "Een handleiding voor het configureren van Gelijktijdige monitoring binnen Uptrends.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/gelijktijdige-monitoring/gelijktijdige-monitoring-configureren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met gelijktijdige monitoring kunt u uw controleregels zo configureren dat ze meerdere controles tegelijk uitvoeren vanuit meerdere controlestations. Dit betekent dat u snel betrouwbare informatie kunt verzamelen over de beschikbaarheid van uw website vanuit verschillende locaties. Elk controleregeltype kan worden geconfigureerd als een gelijktijdige controleregel. Het instellen van gelijktijdige monitoring is grotendeels hetzelfde als bij standaard monitoring, met enkele belangrijke verschillen en enkele aandachtspunten waarmee u rekening moet houden.  In [dit artikel]([LINK_URL_1]) vindt u meer informatie over hoe gelijktijdige monitoring werkt.  
  
U kunt nieuwe gelijktijdige controleregels maken, maar het is ook mogelijk om de functie gelijktijdige  monitoring in te schakelen voor bestaande controleregels. Het inschakelen van gelijktijdige monitoring werkt in beide gevallen hetzelfde.

## Gelijktijdige monitoring instellen

1.  Schakel gelijktijdige monitoring in. Op het tabblad [SHORTCODE_3]Algemeen[SHORTCODE_4] van het venster controleregelinstellingen / nieuwe controleregel, ziet u de optie **Gelijktijdige monitoring**. Schakel de optie in door op het keuzerondje bij **Gelijktijdige monitoring** te klikken.
2.  Er verschijnen twee nieuwe velden: **Grenswaarde voor onbevestigde fout ** en **Grenswaarde voor bevestigde fout**. Deze grenswaarden vertegenwoordigen het percentage controlestations dat een fout kan detecteren voordat het resultaat van de gelijktijdige controleregel als geheel wordt vermeld als respectievelijk *onbevestigd* of *bevestigd*. Fouten werken iets anders bij gelijktijdige controleregels – [lees dit artikel voor een volledige beschrijving]([LINK_URL_2]). We hebben enkele standaardwaarden ingevuld, maar u kunt ze naar wens aanpassen. Let wel, de grenswaarde voor onbevestigde fout moet altijd lager zijn dan of gelijk zijn aan de grenswaarde voor bevestigde fout.  
      
    ![]([LINK_URL_3])
3.  Controleer vervolgens uw controlestationinstellingen. Selecteer op het tabblad [SHORTCODE_5]Controlestations[SHORTCODE_6] de controlestations die de controle gelijktijdig gaan uitvoeren. We staan maximaal 50 controlestations toe voor elke gelijktijdige controleregel.
4.  [SHORTCODE_1]**Opmerking:** als het gaat om het selecteren van controlestations voor gelijktijdige controleregels, hebt u twee opties, deze worden weergegeven in het scherm voor het selecteren van controlestations:
    1.  De eerste optie is om alle controlestations beschikbaar te hebben. In dit geval is het minimumaantal controlestations dat u moet selecteren voor uw gelijktijdige controleregel 5.
    2.  U kunt er ook voor kiezen om alleen controlestations *met een hoge beschikbaarheid* te gebruiken. Deze beperkte set controlestations heeft een grotere beschikbaarheid, aangezien we op die locaties met meerdere servers werken. Dit elimineert de kans dat door onderhoud of downtime een of meer locaties niet beschikbaar zijn voor uw gelijktijdige controles. Dit is belangrijk, want als een locatie uitvalt kan dat van invloed zijn op uw alertingregels voor gelijktijdige monitoring. Kiest u ervoor de set controlestations *met hoge beschikbaarheid* te gebruiken, dan moet u minimaal 3 controlestations selecteren.[SHORTCODE_2] 
5.  Maakt u een nieuwe controleregel, vul dan de rest van de verplichte velden in, afhankelijk van het geselecteerde controleregeltype. Klik linksonder in het venster op Opslaan om de controleregel te bewaren.  
      
    De controleregel begint onmiddellijk met het genereren van geaggregeerde resultaten. Hier vindt u meer informatie over [hoe u de resultaten van uw gelijktijdige monitoring interpreteert]([LINK_URL_4]).

## Dingen om rekening mee te houden

-   Houd bij het instellen van uw grenswaarde voor (on)bevestigde fouten rekening met het aantal geselecteerde controlestations. Het heeft geen zin om waarden van respectievelijk 40% en 50% te gebruiken als u maar 3 controlestations hebt geselecteerd, aangezien het niet mogelijk is om een foutpercentage van 40-50% te krijgen met een dergelijke instelling.
-   Gelijktijdige controleregels volgen niet het [gangbare foutschema]([LINK_URL_5]) van *OK – Onbevestigd –Bevestigd*. Vanwege de grenswaarde-instellingen voor fouten kan een gelijktijdige controleregel direct van *OK* naar *Bevestigd* gaan. De meting zal robuuster zijn, omdat elke fout door meerdere locaties tegelijk is bevestigd.
-   Houd er bij het instellen van gelijktijdige monitoring rekening mee dat de prijs van een gelijktijdige controleregel is gebaseerd op het totale aantal geselecteerde controlestations. Als u bijvoorbeeld een transactie van 4 credits uitvoert op 3 controlestations met hoge beschikbaarheid, zijn de totale kosten 4 × 3 = 12 credits. U kunt de totale controleregelkosten bekijken in het [Overzicht controleregels]([LINK_URL_6]).
