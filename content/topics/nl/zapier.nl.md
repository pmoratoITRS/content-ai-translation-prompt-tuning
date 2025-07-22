{
  "hero": {
    "title": "Integreer Uptrends met Zapier"
  }, 
  "title": "Zapier",
  "summary": "Handleiding voor het integreren van uw Uptrends-alerting in Zapier",
  "url": "/support/kb/alerting/integraties/zapier",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/zapier" 
}

**Zapier** is een tool voor online automatisering die uw apps en diensten met elkaar verbindt. Hiermee kunt u uw Uptrends-alerting verbinden met vrijwel elke andere bestaande applicatie. In deze handleiding helpen we u bij het instellen van uw Uptrends-integratie met Zapier en leggen we uit waar u uw Uptrends-data vervolgens naartoe kunt brengen.

1.  Stel een *When this happens...*-actie in Zapier in
2.  Configureer de integratie in Uptrends.
3.  Test de webhook in Zapier
4.  Stel een *Do This...*-actie in Zapier in
5.  Voeg de integratie toe aan een alertdefinitie in Uptrends

Lees verder voor gedetailleerde instructies voor het opzetten van deze integratie!

## 1. Stel een When this happens…-actie in Zapier in

1.  In Zapier worden geautomatiseerde workflows *Zaps* genoemd. Ga naar *Zaps* en klik op *Create Zap.* Of klik op de knop *MAKE A ZAP* linksboven in het scherm.
2.  Geef uw nieuwe Zap een geschikte naam.
3.  Selecteer *Webhooks by Zapier*.
4.  Selecteer *Catch hook* en klik op *Continue*.
5.  Bewaar de **Custom Webhook URL** want die hebben we straks nodig om de integratie in Uptrends te configureren.
6.  Klik op *Continue*.

Op dit punt vraagt Zapier u om de webhook te testen door er data naartoe te sturen. Om dit te doen moeten we eerst de Uptrends-integratie configureren.

## 2. Configureer de integratie in Uptrends

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Integraties{{< /AppElement >}}.
2.  Klik rechtsboven op {{< AppElement type="button" >}}Integratie toevoegen{{< /AppElement >}}.
3.  Kies Zapier als het integratietype.
4.  Voer een naam in voor deze integratie..
5.  Plak de **Custom Webhook URL** die u eerder heeft bewaard in het desbetreffende veld {{< AppElement type="menuitem" >}}Voorgedefinieerde variabelen{{< /AppElement >}}.
6.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om uw instellingen te bewaren. De nieuwe Zapier-integratie verschijnt op de pagina Integraties.

## 3. Test de webhook in Zapier

1.  Ga naar de zojuist gemaakte **Zapier**-integratie in Uptrends.
2.  Klik in het tabblad {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}} op de knop {{< AppElement type="button" >}}Testalert versturen{{< /AppElement >}}.
3.  Klik op {{< AppElement type="button" >}}Start test{{< /AppElement >}} om een testalert naar de Zapier-webhook te sturen. Het maakt niet uit welk *Alerttype* u selecteert.
4.  Ga naar Zapier en klik op de knop *Test trigger*. Dit zal Zapier ertoe aanzetten om de binnenkomende data te bekijken die we in de vorige stap hebben verstuurd en zijn JSON-body te analyseren. Straks kunnen we naar de afzonderlijke velden in het uitgaande bericht verwijzen. ![](/img/content/5386ad32-943e-41ff-9533-abcb03c30fc5.png)
5.  Klik op de knop *Continue* in Zapier.

## 4. Stel een Do This…-actie in Zapier in

### Voorbeeld 1: e-mailintegratie via Zapier

Als voorbeeld stellen we eerst een eenvoudige e-mailintegratie via Zapier in.

1.  Zoek en selecteer in Zapier de ingebouwde app *Email by Zapier*.
2.  Klik op *Continue*.
3.  Voeg uw e-mailadres toe in het veld **To**.
4.  De velden **Subject** en **Body** kunnen aangepast worden met behulp van de binnenkomende Uptrends-data. Aangezien Zapier in stap 3 een testalert heeft ontvangen en geanalyseerd, is hij al op de hoogte van de data in binnenkomende Uptrends-alerts. Wanneer u op een van deze velden klikt, verschijnt er een lijst genaamd **Insert data** waaruit u verwijzingen kunt selecteren naar waarden die in een Uptrends-alert zijn opgenomen. Wanneer Zapier het uitgaande bericht verstuurt, vult hij automatisch de juiste waarden in.![](/img/content/af300fe7-01dd-4e58-b2fe-afa99b1125ff.png)
5.  Nadat u het uitgaande bericht naar wens heeft aangepast, klikt u op de knop *Continue*.
6.  Als u wilt, kunt u in dit scherm het uitgaande bericht testen. Het zou u meteen een e-mail met fictieve data moeten sturen.![](/img/content/8a4e2e5e-2288-4a6d-91c4-d9f64c54b6f0.png)

7.  Voltooi de integratie aan de Zapier-kant door op **TURN ON ZAP** te klikken.

### Voorbeeld 2: Trello-integratie via Zapier

Uw Zapier-integratie kan nog veel meer. Als tweede voorbeeld stellen we een integratie in met Trello. Uw Trello-account moet verbonden zijn met Zapier. De optie om dit te doen vindt u onder *My Apps* in het Zapier-menu aan de zijkant.

1.  Voeg een nieuwe Zap toe door dezelfde stappen te volgen als beschreven in sectie 1 ( *Stel een When this happens...-actie in Zapier in*) van deze handleiding.
2.  U krijgt een nieuwe **Custom Webhook URL**. Deze nieuwe Webhook URL moet worden toegevoegd aan een eigen integratie in Uptrends. Volg de acties van stap 2 om een nieuwe integratie in Uptrends te configureren, maar zorg ervoor dat u deze nieuwe Webhook URL gebruikt.
3.  Herhaal de acties van stap 3 om testdata naar deze nieuwe webhook te sturen zodat Zapier de binnenkomende data kan analyseren. In het kort: ga naar het tabblad {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}} en klik op de knop {{< AppElement type="button" >}}Testalert versturen{{< /AppElement >}}. Klik in Zapier op de knop *Test trigger*. Klik tot slot op *CONTINUE*.
4.  Om de integratie met Trello in te stellen, selecteert u de *Trello*-app onder **Your Apps**.
5.  U kunt de exacte actie selecteren die in Trello moet worden ondernomen wanneer er een Uptrends-alert wordt verzonden. In dit voorbeeld kiezen we *Create Card*. Klik op *CONTINUE* in het volgende scherm.
6.  Selecteer het verbonden Trello-account en klik op *CONTINUE*.
7.  Kies de juiste **Board** en **List**. Stel de **Description** in voor de kaart die moet worden gemaakt. Ook hier kunt u de inhoud volledig aanpassen, waarbij u gebruikmaakt van de Uptrends-alertingdata zoals eerder geanalyseerd door Zapier. Stel desgewenst andere opties in en klik tot slot op *CONTINUE*.![](/img/content/52217609-6954-4819-8bc1-9195a448ff72.png)
8.  Als u wilt kunt u het uitgaande bericht in dit scherm testen.![](/img/content/4cea7e0f-e577-4250-aec5-ab31d000935d.png)
9.  Voltooi het instellen van de integratie aan de Zapier-kant door te klikken op **TURN ON ZAP**.

{{< callout >}}
**Tip:** Dit zijn slechts twee voorbeelden, maar met Zapier kunt u uw Uptrends-alerts naar vrijwel elk extern platform doorsturen.
{{< /callout >}}

## 5. Voeg de integratie toe aan een alertdefinitie in Uptrends

Een integratiedefinitie op zich doet niets. U moet deze koppelen aan een escalatieniveau in een alertdefinitie om berichten via de integratie te ontvangen.

1.  Ga naar {{< AppElement type="menuitem" >}}Alerting > Alertdefinities{{< /AppElement >}} en open de definitie waaraan u de integratie wilt koppelen.
2.  Elk tabblad {{< AppElement type="tab" >}}Escalatieniveau{{< /AppElement >}} bevat een gedeelte **Alerts versturen door integraties** met een lijst met beschikbare integraties. Lees het Knowledge Base-artikel [Alert escalatieniveaus]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="nl" >}}) om te leren hoe escalaties werken.
3.  Selecteer de integratie(s) die u aan dit escalatieniveau wilt koppelen. In dit geval de **Aanpasbare integratie** voor Zapier.
4.  Vergeet niet op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} te klikken om uw wijzigingen te bewaren.

**Dat was het!** U heeft de Zapier-integratie succesvol geconfigureerd.

Als u vragen heeft, kunt u zoals altijd [contact opnemen met ons support team](/contact).
