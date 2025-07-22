{
  "hero": {
    "title": "Het klikpad van de winkelwagengebruiker vastleggen"
  },
  "title": "Het klikpad van de winkelwagengebruiker vastleggen",
  "summary": "In deze tutorial wordt u stapsgewijs door het opnameproces geleid terwijl u het klikpad van de winkelwagengebruiker vastlegt.",
  "url": "/support/kb/synthetic-monitoring/transacties/tutorial-record-user-journey-in-shop/uw-transactie-opnemen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction",
  "tableofcontents": false
}

In dit voorbeeld doorloopt u het opnameproces van het klikpad voor een gebruiker die items aan zijn winkelwagen toevoegt en de inhoud wijzigt.

De volgende instructies leiden u door een gedetailleerd voorbeeld van het transactie-opnameproces. Zodra de transactiecontroleregel actief is, gebruikt deze transactiecredits die u in uw account moet kopen. Dit voorbeeld bevat informatie over welke stappen credits gebruiken. Meer informatie over het gebruik van credits vindt u in het artikel [Berekenen van credits voor transactiecontroleregels]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="nl" >}}).

1. Download de Uptrends transaction recorder uit de Chrome Web Store en voeg deze extensie toe aan uw Chrome-browser. De stappen worden beschreven in [De transaction recorder downloaden]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder#download-transaction-recorder" lang="nl" >}}).
2. Open de transaction recorder-extensie in een Chrome-browservenster en klik op de knop {{< AppElement type="deletebutton" >}} Start recording {{< /AppElement >}}. Het venster **REC start** verschijnt. 
3. Voer [https://galacticshirts.com](https://galacticshirts.com/) in als de URL in de adresbalk van het venster **REC start**.  
   *Dit is u eerste overgang naar een nieuwe pagina die resulteert in een server request (gebruikte credits = 1).*  
   De startpagina van de winkel wordt weergegeven.
   ![screenshot van startpagina galactic shirts](/img/content/f0180d9f-9bf2-4947-bf11-c47c48afcd23.png)  
4. Klik op de afbeelding van het eerste shirt om de pagina met productgegevens te openen.  
   Het shirt kan wisselen, maar er moet altijd een eerste shirt zijn. In dit geval is het eerste shirt het Suraya Bay T-shirt.  
   *Als u op de link klikt, gaat u naar de pagina met productgegevens en doet u een server request. Dit zal nog een credit gebruiken (gebruikte credits = 2).*
   De productgegevens van het shirt worden getoond.
5. Klik op de vervolgkeuzelijst **Size** om maat "**L**" te selecteren.
6. Wijzig het aantal in "**2**".
   ![](/img/content/e1b42b45-fb3a-4687-af3e-fba30d780986.png)
       Het maakt niet uit of u het aantal wijzigt door de "1" te markeren en "2" te typen of door op de pijlen omhoog/omlaag te klikken, de recorder registreert alleen de klik en de waardeverandering.  
7.  Klik op **Add to cart**.  
    *Door op de knop "Add to cart" te klikken, worden een server request en een nieuwe pagina gegenereerd wat nog een credit gebruikt (gebruikte credits = 3).* 
8.  Voeg een content check toe. Voor best practices wordt aanbevolen om altijd [inhoudcontroles]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}}) toe te voegen om te verifiëren of het resultaat van elke geladen pagina is zoals verwacht. In dit voorbeeld willen we ervoor zorgen dat de actie Add to cart correct werkte (een van de vele inhoudcontroles die u aan uw script zou moeten toevoegen). U kunt op drie verschillende manieren een inhoudcontrole toevoegen: via de knop **Add content check** of via het contextmenu. U kunt content checks ook later toevoegen met de controleregel-stapeditor in uw account.

    Een inhoudcontrole toevoegen via de kop **Add content check**:
      
    1. Zoek het recordervenster (vaak achter uw browservenster) en klik op {{< AppElement type="editbutton" >}} \+ Add content check{{< /AppElement >}} 
       ![screenshot recorder content check](/img/content/6101d30a-9158-40d0-9b28-d7422f3c94c3.png)
      
    2. Kies een deel van de bevestigingspagina dat uniek is voor de pagina en het minst waarschijnlijk zal veranderen. In dit geval is "added to your cart" een goede kandidaat. Voer dit in in het pop-upvenster **Add content check**.
       ![screenshot pop-upvenster content check](/img/content/scr_transaction-recorder-add-content-check.min.png)
    3. Klik op {{< AppElement type="button" >}}Save{{< /AppElement >}}.
    4. Ga terug naar het opnamevenster.

    Een content check toevoegen via het contextmenu:

    1. Markeer de tekst "added to your cart.".
    2. Rechtsklik en kies de optie *ITRS Uptrends Transaction Recorder* in het contextmenu.
    3. Selecteer de optie *Create a content check*. Deze inhoudcontrole wordt nu opgenomen in het venster van de transaction recorder.
    4. Ga terug naar het opnamevenster.

    ![screenshot content check context menu option](/img/content/scr_transaction-recorder-content-check-hover.min.png)

De inhoudcontrole is nu succesvol vastgelegd.

9.  Klik op de knop **View Cart** om naar de winkelwagenweergave te gaan.  
    *Dit gebruikt nog een credit (gebruikte credits = 4).*
10.  Wijzig het aantal van "2" in "1."
11. Klik op **Update cart**.  
    *Update cart vernieuwt de pagina wat een server request genereert die één credit gebruikt (gebruikte credits = 5).*
    ![screenshot shopping cart update](/img/content/5ba19828-a398-41bd-b67e-e8c615442cb1.png)
12. Voeg een content check toe om te controleren of de pagina correct is geladen door te testen op de tekst "Cart updated."
13. Klik op de rode "X" om het item uit de winkelwagen te verwijderen en onze transactie te voltooien.  
    *Het verwijderen van het item genereert een server request die één credit gebruikt (totaal gebruikte credits = 6).*
14. Voeg een content check toe met de zin "Your cart is currently empty.".
15. Een andere manier om te controleren of uw winkelwagen leeg is, is door te hoveren over het mandpictogram in de rechterbovenhoek van uw scherm. Houd er rekening mee dat de transaction recorder niet automatisch een stap registreert wanneer u hovert over elementen op de website, daarom moet u deze handmatig toevoegen.
    
    Een hoveractie toevoegen tijdens het opnameproces:
    1. Rechtsklik op het element waarin u wilt hoveren, in dit geval het mandpictogram. 
    2. Klik in het contextmenu op de optie *ITRS Uptrends Transaction Recorder*.
    3. Klik op *Create hover action*. U ziet dat de daadwerkelijke stap is vastgelegd in het venster van de transaction recorder.
    4. In dit voorbeeld verschijnt er een melding "No products in the cart" wanneer u over het mandpictogram hovert. In gevallen waarin een muis-hover een element zichtbaar maakt, kunt u ook de activiteit van een element volgen dat zichtbaar moet zijn. U kunt dit op dezelfde manier doen als bij de hoveractie door te rechtsklikken op het zichtbare element (*element "No products in the cart"*) > Klik in het contextmenu op *ITRS Uptrends Transaction Recorder* > *Wait for this element to be visible*. 

     ![screenshot empty cart](/img/content/scr_transaction-recorder-hover.min.png)

Zowel de hoveractie als het element dat zichtbaar moet zijn, zijn nu vastgelegd.

16. Voeg een content check toe met de zin "No products in the cart.".
17. Nu uw winkelwagen leeg is, kunt u zoeken naar een ander type shirt met het tekstveld 'Zoek producten' rechtsboven in het scherm. Typ *Summer*, u ziet dat dit veld geen zoekknop bevat. In plaats daarvan kunt u op de *Enter-toets* drukken om zoekresultaten te genereren.

    De transaction recorder kan ook dergelijke toetsenbordacties van de gebruiker vastleggen. Dit is handig wanneer u websites tegenkomt met instructies als *Druk op een willekeurige toets om door te gaan* of *Druk op Enter om te bevestigen*. Houd er rekening mee dat u, anders dan met muisklikactiviteiten (die automatisch een beweging vastleggen), een toetsenbordactie handmatig moet toevoegen om een toetsenbordgebeurtenis vast te leggen en deze als een daadwerkelijke activiteit te laten gelden.

    Een toetsenbordactie toevoegen tijdens het opnameproces:
    1. Zoek het opnamevenster (vaak achter uw browservenster):
       ![screenshot of add keyboard action button](/img/content/scr_transaction-recorder-add-keyboard-action.min.png)
       Klik op {{< AppElement type="editbutton" >}} \+ Add keyboard action{{< /AppElement >}} 
    2. Er verschijnt een pop-upvenster met een keuzemenu om te selecteren welke toets moet worden ingedrukt. U kunt kiezen uit verschillende tekens, variërend van Control-toets, speciale toetsen, cijfertoetsen, numerieke toetsen, hoofdletter- en kleinelettertoetsen.
        ![screenshot van pop-up toetsenbordactie toevoegen](/img/content/scr_transaction-recorder-add-keyboard-action-popup.png)
    3. Kies of deze toets globaal moet worden ingedrukt of alleen bij het huidige gefocuste element. Door de optie *Global* te kiezen, wordt die specifieke toetsenbordgebeurtenis in de hele toepassing herkend. De laatste optie wordt alleen toegepast op het *last clicked element*, zoals tussen haakjes vermeld bij het keuzerondje.
    4. Klik op {{< AppElement type="button" >}}Save{{< /AppElement >}} naar het opnamevenster.

    *Het zoeken naar een nieuw shirt genereert een server request dat één credit gebruikt (gebruikte credits = 7).*

18. Voeg een content check toe om te verifiëren dat het shirt niet bestaat door de tekst "No products were found matching your selection." te testen.
19. Klik op {{< AppElement type="deletebutton" >}} Stop recording{{< /AppElement >}}.
20. Klik op de knop **Upload recording** en kies om eerst zelf de transactie te testen en te optimaliseren (self-service transactie). Bekijk het knowledgebase-artikel [Opties voor transactiescripts]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="nl" >}}) over de keuze tussen full-service en self-service transacties.

U bent aan het einde van het opnameproces van het klikpad van de winkelwagengebruiker. Het resultaat is een nieuwe transactiecontroleregel in uw Uptrends-account. U kunt verwachten dat uw controleregel zeven transactiecredits gebruikt, maar er zijn andere factoren die invloed hebben op de [berekening van credits]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="nl" >}}). 

De volgende taak is om uw transactie te testen en deze indien nodig aan te passen. Gebruik hierbij de instructies in [Uw transactiescript testen en bewerken]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="nl" >}}) om u door de tests te begeleiden.
