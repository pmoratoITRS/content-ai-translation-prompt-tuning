{
  "hero": {
    "title": "De transaction recorder downloaden en gebruiken"
  },
  "title": "De transaction recorder downloaden en gebruiken",
  "summary": "Download de transaction recorder en leer hoe u de recorder gebruikt.",
  "url": "/support/kb/synthetic-monitoring/transacties/download-en-gebruik-de-transaction-recorder",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/download-and-use-the-transaction-recorder"
}

In dit artikel wordt uitgelegd hoe u de transaction recorder kunt downloaden en gebruiken. 
Als u dit wilt uitproberen met een fictieve winkel in plaats van met uw eigen (echte) winkel, bekijk dan de tutorial [Gebruikerstraject in een winkel]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/" lang="nl" >}}). 

## Download de transaction recorder {id="download-transaction-recorder"}

De transaction recorder is een Chrome-browserextensie. Mocht u hiermee niet bekend zijn: een browserextensie is een kleine app die u aan uw Chrome-browser kunt toevoegen om bepaalde dingen te doen, zoals wachtwoorden beheren. In dit geval kunt u het klikpad voor uw transactie vastleggen. De extensie is eenvoudig te installeren, maar als u meer hulp nodig heeft, heeft Google een cursus voor u over [browserextensies installeren en beheren](https://support.google.com/chrome_webstore/answer/2664769?hl=en).

1.  Open een Chrome-browservenster. U moet [Chrome](https://www.google.com/intl/en/chrome/) gebruiken.
2.  Ga naar de [Chrome Web Store](https://chrome.google.com/webstore/detail/uptrends-transaction-reco/pbglkhekcljpmhpaeckglhfpenefpjgo). De link brengt u rechtstreeks naar de transaction recorder in de store, of u kunt in de store zoeken naar "Uptrends transaction recorder".
3.  Klik op de knop **Toevoegen aan Chrome**. Er verschijnt een pop-upvenster.  
    ![screenshot Chrome pop-up extensie toevoegen](/img/content/scr_transactionrecorder-chrome-extension-popup.min.png)
4.  Klik op **Extensie toevoegen**. Afhankelijk van uw instellingen moet u mogelijk pop-ups inschakelen voor de Chrome Web Store.
5.  U ziet het ITRS-logo rechts van de adresbalk in uw Chrome-browser nadat u de extensie heeft toegevoegd en de extensie is vastgezet. Als u deze extensie niet heeft vastgezet (of losgemaakt), kunt u deze openen via het menu Extensies (pictogram van een puzzelstukje).
    ![screenshot Uptrends extensie toegevoegd](/img/content/scr_transactionrecorder-chrome-extension-icon.min.png)  

De transaction recorder is nu klaar voor gebruik.

## De transaction recorder gebruiken {id="using-transaction-recorder"}

1. Open een nieuw Chrome-browservenster en [schakel alle opties voor automatisch invullen uit](https://support.boldbrush.com/faso-account-login/disable-clear-autofill-in-browser) die mogelijk actief zijn. De recorder kan geen automatisch ingevulde tekst zien. 
2. Open de transaction recorder door op het ITRS-logo rechts van de adresbalk te klikken.
   Er wordt een nieuw venster geopend met Engelstalige gedetailleerde instructies en belangrijke richtlijnen. 
   ![screenshot start transaction recorder](/img/content/scr_transaction-recorder-start.min.png)
2.  Lees de **Quick start** en **Important guidelines** door voordat u verder gaat.
3.  Klik linksonder op de knop **Start recording**.  
    Mogelijk verschijnt er een pop-up waarin wordt uitgelegd dat het formaat van uw venster moet worden aangepast. Sta toe dat de recorder het formaat van uw venster wijzigt.  
    Er wordt een nieuw browservenster geopend vóór het recordervenster.
    ![screenshot startpagina](/img/content/scr_transactions-REC-Start-page_040824.min.png)
4.  Navigeer naar uw startpagina door de URL in de adresbalk van het startvenster van de recorder in te voeren.
5.  Klik door uw transactie om alle stappen vast te leggen. U kunt deze [stapsgewijze handleiding]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="nl" >}}) raadplegen om u te helpen met het vastleggen van transacties in de gebruikersreis.
6.  Schakel naar het recordervenster wanneer u het einde van uw transactie heeft bereikt. 
    ![venster transaction recorder met stappen](/img/content/scr_transaction-recorder-with-steps.min.png)
7.  Controleer uw script.  
    U kunt onnodige acties verwijderen die de transaction recorder heeft opgepikt toen u door de site klikte. Onthoud dat u stappen kunt toevoegen, dingen kunt verwijderen en inhoudcontroles kunt definiëren met de stap-editor in de instellingen van uw controleregel, maar u wilt dat uw opname in dit stadium zo schoon mogelijk is. Als u denkt dat u te veel extra klikken of andere problemen heeft verzameld, kunt u deze opname altijd weggooien en opnieuw beginnen.
8.  Klik op de knop **Stop recording** als u tevreden bent of opnieuw wilt beginnen.
9. (Optioneel) Als u de opname opnieuw wilt doen, klikt u op de knop **Clear recording** en voert u de bovenstaande instructies opnieuw uit.
10. Als u tevreden bent met de transactie die u heeft opgenomen, klikt u op de knop **Upload recording** (die rechtsonder verschijnt nadat u een opname heeft gestopt).
11. Log in op uw Uptrends-account.
12. Geef uw opname een naam die zal worden gebruikt voor de transactiecontroleregel die automatisch wordt gecreëerd in uw account. De naam helpt u bij het identificeren van uw controleregel in het *Overzicht controleregels*. U kunt de controleregelnaam later altijd wijzigen.
    ![screenshot opnamedetails](/img/content/scr_transaction-upload.min.png)
13. Kies of u gebruik wilt maken van [self-service of full-service transacties]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="nl" >}}). De opties zijn:

    a) **Ik test en optimaliseer deze transactie zelf** - self-service transacties. Selecteer deze optie als u het liever zelf afhandelt. Deze optie creëert een nieuwe transactiecontroleregel in uw account. Vergeet niet dat u altijd [hulp kunt krijgen]({{< ref path="contact" lang="nl" >}}) als u die nodig heeft. 

    b) **Laat Uptrends Support deze transactie voor mij stabiliseren** - full-service transacties. Kies deze optie als u de opname naar het supportteam wilt sturen om het scripten en testen voor u te doen.
    
13. Vermeld alle informatie die u of de scriptingprofessional nodig heeft in het tekstveld.
14. Klik op de knop **Start upload** om een nieuwe controleregel in uw account te creëren (self-service transactie) of om de opname naar het team van Uptrends Support te sturen (full-service transactie). 
