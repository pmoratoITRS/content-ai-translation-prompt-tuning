{
  "hero": {
    "title": "Overzicht Transactiemonitoring"
  },
  "title": "Overzicht Transactiemonitoring",
  "url": "/support/kb/synthetic-monitoring/transacties/overzicht-transactiemonitoring",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transactions-overview",
  "sectionlist": false
}

Transactiemonitoring, ook wel web application monitoring genoemd, wordt gebruikt om het correct functioneren van gebruikersinteracties op uw website te controleren. De interactie kan een simpele login zijn of alle acties die nodig zijn om een product in uw webshop te kopen. 

Om deze gebruikersinteracties te monitoren, moet u ze in een script plaatsen dat telkens opnieuw kan worden uitgevoerd om te controleren of alles nog steeds werkt zoals verwacht. Uptrends biedt de transaction recorder (als een Chrome-extensie) om op een eenvoudige manier een script te bouwen. Nadat u het script heeft opgenomen, kunt u het zelf bijschaven (self-service transacties) of Uptrends' support vragen het script te verfijnen (full-service transacties). Als u goed bent in scripten, kunt u besluiten het opnemen over te slaan en uw eigen script meteen in een transactiecontroleregel plaatsen.

Wanneer u een transactieopname uploadt naar uw Uptrends-account, wordt er een transactiecontroleregel gemaakt met wat basisinformatie. U zult een aantal instellingen aan uw behoeften moeten aanpassen.

Zodra u uw transactiecontroleregel heeft getest en tevreden bent over de manier waarop deze werkt, gaat u verder en stelt u er [alerting]({{< ref path="support/kb/alerting" lang="nl" >}}) voor in. Dit is immers waar het om gaat: gewaarschuwd worden wanneer dingen niet werken zoals verwacht.

{{< callout >}}
We hebben een stapsgewijze tutorial [Gebruikersreis in een winkel]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop" lang="nl" >}}) met uitleg vanaf de basis tot transactiemonitoring en het controleren van monitoringdata.
{{< /callout >}}

## 1. Introductie

Als webapplicatie-/transactiemonitoring nieuw is voor u, kunt u achtergrondinformatie vinden in de volgende artikelen:

- Krijg een introductie in [Wat is Web Application Monitoring?]({{< ref path="what-is/web-application-monitoring" lang="nl" >}})
- Lees [waarom u web application monitoring zou moeten gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#why-monitor-your-web-applications" lang="nl" >}})
- Controleer of web application monitoring [de juiste oplossing]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#transaction-best-choice" lang="nl" >}}) voor u is

## 2. Uw transactiemonitoring plannen

Inzicht in de werking van uw transacties, de functionaliteit die u moet testen en de impact van uw monitoring op uw systemen is een essentieel onderdeel van het plannen van uw transacties. Mogelijk moet u ook andere teams van uw bedrijf betrekken bij het opzetten van transactiemonitoring.

- [Breng mogelijke transactiepaden in kaart]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="nl" >}})
- Beslis [wat te testen]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="nl" >}})
- [Waarschuwingen, tips en trucs]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="nl" >}}): dingen om rekening mee te houden en op te letten bij het opzetten van uw monitoring
- [Redenen waarom u mogelijk hulp nodig heeft]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#programming-skills" lang="nl" >}}) van andere teams binnen uw bedrijf

## 3. Uw transacties opnemen

Het op de juiste manier gebruiken van de [transaction recorder]({{< ref path="features/transaction-recorder" lang="nl" >}}) leidt tot schonere opnamen en een snellere set-up van de controleregel.

- [Download en gebruik de transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}})
- Volg de [stapsgewijze winkelwagentutorial]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="nl" >}}) om te leren hoe u de transaction recorder gebruikt
- Kies tussen [full-service en self-service transacties]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="nl" >}})

## 4. Uw transactiescript bewerken en testen

Nadat u uw transactie heeft opgenomen en ervoor heeft gekozen het script zelf te testen (u kunt uw tests ook door ons support team laten uitvoeren), moet u problemen met het resulterende script oplossen, inhoudcontroles instellen als u dat nog niet heeft gedaan en de vault-gebruikersrechten aanpassen voor nieuw gecreëerde items. Tot slot moet u de controleregel in staging mode in de gaten houden voordat u uw controleregel naar production verplaatst.

- Meer informatie over de editor, stappen en acties is te vinden in [De stap-editor begrijpen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}})

- Acties vormen de kern van transacties. Meer informatie over acties:
   - [Pagina-interacties - navigeren, klikken, instellen, etc.]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="nl" >}})
   - [Test-acties - inhoudcontroles en wachten]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}})
   - [Bediening-acties - schakelen tussen (inline) frames of tabbladen]({{< ref path="support/kb/synthetic-monitoring/transactions/Switching-between-iframes-browser-tabs" lang="nl" >}})
   - [Bediening-acties - aanpassen variabele-inhoud]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="nl" >}})
   - [Negeer fouten voor optionele stappen en acties]({{< ref path="support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="nl" >}})
   - [Selectors gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="nl" >}}) en [selectoralternatieven]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="nl" >}})
   - [Transactievariabelen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="nl" >}}) en [inhoud variabele aanpassen]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="nl" >}})

- In de oefening [Uw script testen en bewerken]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="nl" >}}) vindt u meer informatie over de *Test starten*-functionaliteit, omgaan met dynamische ID's en time-out fouten. De les bevat ook een [Checklist voor testen]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction#script-testing-checklist" lang="nl" >}}).

- Een paar andere zaken waarmee u te maken kunt krijgen, afhankelijk van uw set-up en transacties:
  - [Beheer gevoelige waarden]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="nl" >}}) die automatisch aan de vault zijn toegevoegd tijdens het opnemen
  - [Beheer vaultrechten (automatisch gecreëerde secties)]({{< ref path="support/kb/synthetic-monitoring/transactions/managing-authorizations-for-automatically-created-vault-sections" lang="nl" >}})
  - Transactiemonitoring voor [mobiel instellen]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup" lang="nl" >}})
  - Werken met een [shadow DOM]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="nl" >}}) in uw transactie
  - Werken met [sms-gebaseerde 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="nl" >}}) of [op eenmalig wachtwoord gebaseerde 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="nl" >}}) in uw transactie

  - Toevoegen van [extra kengetallen]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}) zoals [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}) en [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}) aan uw transactieresultaten.

  - Bypass of omzeil het standaard DNS-systeem door een [DNS bypass]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="nl" >}}) in uw transactie te gebruiken.

## 5. Resultaten van transactiemonitoring

Zodra uw transacties worden gemonitord ontvangt u feedback. Er zijn een aantal bronnen die u kunt bekijken om erachter te komen wat er misgaat, wanneer er dingen misgaan.

- [Screenshots]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-screenshots" lang="nl" >}})

- [Watervallen]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="nl" >}})

- [W3C Navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}})

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}})

- [Fouten analyseren]({{< ref path="support/kb/synthetic-monitoring/transactions/analyzing-transaction-errors" lang="nl" >}})

## 6. Problemen oplossen

Wanneer de transactiemonitoring niet naar verwachting werkt, zijn hier een paar dingen om te controleren: 

- [A/B-tests uitsluiten]({{< ref path="support/kb/synthetic-monitoring/transactions/exclude-a-b-tests-from-transaction-requests" lang="nl" >}})

- [Gebruik incognito-modus]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-incognito-mode" lang="nl" >}})

- [Waarschuwingen, tips en trucs]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="nl" >}})

## Credits

Transactiecontroleregels gebruiken transactiecredits waarmee u controleregels kunt creëren en plannen voor uitvoering. Uptrends gebruikt credits om de prijzen voor verschillende monitoringdiensten te berekenen. Raadpleeg het knowledgebase-artikel [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="nl" >}}) voor meer informatie.
