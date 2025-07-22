{
  "hero": {
    "title": "Transaction Recorder incognitomodus"
  },
  "title": "Transaction Recorder incognitomodus",
  "url": "/support/kb/synthetic-monitoring/transacties/transaction-recorder-incognitomodus",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-recorder-incognito-mode",
  "tableofcontents": false,
  "sectionlist": true
}

{{< callout >}} **Opmerking**: Het wordt altijd aangeraden om de Transaction Recorder in incognitomodus te gebruiken voor een probleemloze opname-ervaring. Gebruik eenvoudig een schakelknop om te voorkomen dat de recorder cookies, opgeslagen informatie en gecachete data gebruikt. {{< /callout >}}

De **Uptrends Transaction Recorder** is een handige tool voor het monitoren van gebruikersinteracties en de algehele flow van activiteiten die op uw website worden uitgevoerd. Deze omvatten activiteiten zoals inloggen, formulieren invullen en artikelen toevoegen aan een winkelwagen. Het monitoren van dergelijke activiteiten houdt in dat u uw transactieflows zo soepel mogelijk vastlegt, zonder opgeslagen informatie van uw website toe te voegen die verwarring kan veroorzaken in uw gewenste flow.

Uptrends kan u zeker helpen een naadloze opname-ervaring te bereiken! Door de recorder in de incognitomodus te draaien, kunt u voorkomen dat cookies, sitedata en cache die tijdens eerdere sessies zijn gebruikt in uw opnames blijven verschijnen.

Het gebruik van de incognitomodus verbetert de kwaliteit van uw transactieopnames. Hier volgen enkele veelvoorkomende scenario's:

- Meerdere inlogsessies testen – gebruik van de incognitomodus wordt aanbevolen als u een website test die toegang nodig heeft tot verschillende gebruikersaccounts (bijvoorbeeld het testen van een account als standaardgebruiker versus een gebruiker met beheerdersrechten). Het uitvoeren van de recorder in incognitomodus voorkomt problemen zoals onjuiste gebruikersinterface (UI)-schermen, overlappende gebruikersfuncties en authenticatiefouten.

- Gegevensformulieren automatisch invullen – in gevallen waarin u formulieren helemaal vanaf nul wilt invullen, zorgt de incognitomodus ervoor dat al uw cookies (een stukje data dat is opgeslagen vanuit uw webbrowser) en andere opgeslagen informatie worden genegeerd wanneer de opname start. Als u een foutbericht wilt testen wanneer een onjuist e-mailadres word ingevoerd, kunt u dit doen zonder een voorgestelde lijst met teksten te krijgen uit uw vorige browsersessies. Incognitomodus geeft u een soepelere en gemakkelijkere ervaring om formulierscenario's te valideren en te testen.

- Vertaalde of gepersonaliseerde websites testen – gebruik de recorder in incognitomodus om websites met personalisatie-instellingen en vertaalde inhoud efficiënt te testen. Hierdoor kunt u eenvoudig van de ene naar de andere pagina doorverwijzen zonder meerdere vensters te openen en te sluiten, door verschillende webbrowsers te navigeren en de cache handmatig te resetten.

- Vergeten de interactieflow van de gebruiker op de website op te nemen – het kan ook gebeuren dat u snel naar een website navigeert, op de optie *Cookies accepteren* klikt, inlogt met uw inloggegevens en normale gebruikersactiviteiten uitvoert. Maar u realiseerde zich dat u niet op de knop *Start recording* in de Transaction Recorder heeft geklikt.
    - Als uw recorder in een normale browser draait en u na al die stappen net bent begonnen met opnemen, herkent uw recorder u als een ingelogde gebruiker en moet u alles aanpassen en opnieuw beginnen. 
    - Maar als uw recorder in incognitomodus draait, herkent uw recorder u niet als een ingelogde gebruiker. Hij zal geen cookies traceren, zodat u de opname kunt starten vanaf waar u was gebleven.

### Schakel de incognitomodus-optie in

Het is een eerste vereiste dat u ervoor zorgt dat u de browserextensie *ITRS Uptrends Transaction Recorder* succesvol heeft [ingesteld]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}).

De Transaction Recorder in incognitomodus draaien:

1. Open Chrome.
2. Navigeer naar *chrome://extensions/*.
3. Zoek naar *ITRS Uptrends Transaction Recorder*.
4. Klik op de knop {{< AppElement type="buttonSecondary" >}}Details{{< /AppElement >}}.
5. Scrol tot u de optie *Toestaan in incognitomodus* ziet en klik dan op de schakelknop in om de Transaction Recorder in incognitomodus te draaien.

### Handige links

Meer informatie:

- [Wat zijn Transactie-controleregels?]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="nl" >}})
- [De Transaction Recorder downloaden en gebruiken]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}})
- [Stapsgewijze instructies voor het gebruik van de Transaction Recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="nl" >}})