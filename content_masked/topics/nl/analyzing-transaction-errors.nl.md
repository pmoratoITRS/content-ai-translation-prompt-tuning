{
  "hero": {
    "title": "Transactiefouten analyseren"
  },
  "title": "Transactiefouten analyseren",
  "summary": "Hier leest u over transactiefouten en hoe u deze analyseert, zodat u alles weer goed werkt.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transactiefouten-analyseren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Soms werken de dingen niet zoals we willen of verwachten – en dat geldt ook voor uw gemonitorde transacties!

Hieronder leest u over transactiefouten en hoe u deze analyseert, zodat u alles weer goed werkt.

## Controleer de HTML-uitvoer

Wanneer er een transactiefout optreedt, maakt de Uptrends-service een schermopname van de HTML-uitvoer op het moment dat de fout wordt gedetecteerd. Deze informatie kan een krachtige tool zijn om te weten te komen hoe een pagina eruitzag op het moment dat er een probleem optrad.

**Om de HTML-uitvoer te controleren doet u het volgende**:

1.  Log in op uw Uptrends-account en navigeer via het menu *Controleregels* naar het dashboard *Controleregel log*.  
2.  Klik op een vermelde transactiefout (onbevestigd of bevestigd).  
      
    [SHORTCODE_1]**Opmerking**: We kunnen de HTML-uitvoer niet leveren bij transacties met een 'navigatie'-fout, aangezien deze fout aanduidt dat we uw website niet hebben kunnen bereiken.[SHORTCODE_2] 
3.  U ziet de HTML-uitvoer onder *Pagina-inhoud*, naast HTML-resultaat.  
4.  Als u wilt zien hoe de pagina eruitzag, selecteert u het stukje HTML-code en slaat dit op (bijvoorbeeld in Notepad) als HTML-bestand.  
5.  Open het bestand in een browser om de pagina weer te geven.

## Wordt de fout door slechts één controlepunt gedetecteerd?

Als een error door slechts een enkel controlepunt wordt gedetecteerd, betekent dat meestal dat er verbindingsproblemen zijn voor gebruikers in die regio of dat er een technisch probleem met dat controlepunt zelf is.

Stuur ons in zo'n geval een [support ticket]([LINK_URL_1]) zodat we u behulpzaam kunnen zijn bij het onderzoeken van het probleem.

## Zijn uw inloggegevens nog geldig?

Soms veranderen de inloggegevens die nodig zijn om een stap van een meerstapstransactie uit te voeren. Verander de transactie-inloggegevens met de transactiestap-editor indien dit gebeurt.
