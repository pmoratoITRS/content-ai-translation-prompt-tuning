{
  "hero": {
    "title": "Opties voor transactiescripts"
  },
  "title": "Opties voor transactiescripts",
  "summary": "U heeft verschillende opties als het gaat om het genereren van het definitieve script voor uw transacties, van full-service tot self-service en het rechtstreeks gebruiken van scripting.",
  "url": "/support/kb/synthetic-monitoring/transacties/self-of-full-service",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/self-or-full-service"
}

Een transactiecontroleregel heeft een script nodig om de stappen die u wilt monitoren, te repliceren. Afhankelijk van hoe vertrouwd u bent met scripting, zijn er enkele opties voor het omgaan met het transactiescript.

- **Als u veel hulp nodig heeft**, kan Uptrends Support het scripten en testen voor u afhandelen met [full-service transacties](#full-service).
-   **Als u redelijk vertrouwd bent met webtechnologieën** zoals HTML, CSS, JSON en XPath, zijn de [self-service transacties](#self-service) geschikt voor u.
-   **Als u een heel ervaren gebruiker bent**, kunt u rechtstreeks van de visuele naar de scripteditor springen en met knippen en plakken vanuit uw eigen scripttool en source control tools [helemaal zelf een script bouwen](#script-from-scratch). U kunt uw transacties en scripts ook beheren met de Uptrends [API]({{< ref path="support/kb/api" lang="nl" >}}).

Beslis voordat u uw transacties gaat scripten welke methode voor u het beste werkt. Vergeet niet dat [Support]({{< ref path="contact" lang="nl" >}}) altijd klaar staat om u te helpen wanneer u dat nodig heeft.

## Full-service transacties {id="full-service"}

U neemt uw transacties op en uploadt ze door "full-service" te kiezen, en de scriptingprofessionals van Uptrends gebruiken uw opname om uw scripts te bewerken en te testen. Het volledige full-service proces duurt ongeveer een week vanaf het moment dat u uw opname indient totdat u een voltooide controleregel in uw account ontvangt en het [beleid voor scriptbeoordeling]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="nl" >}}) van toepassing is.

### Wie zou full-service transacties moeten gebruiken?

Iedereen kan en mag kiezen voor de full-service optie, en Support helpt u graag om uw controleregels operationeel te krijgen. U kunt full service transacties kiezen als:

-   U niet vertrouwd bent met het werken met scripttechnologieën zoals HTML, CSS, JSON en XPath.
-   U eenvoudigweg niet de tijd of middelen heeft om aan de taak te besteden.
-   U het gewoon niet wilt doen.

### Om welke stappen gaat het?

Als u ervoor kiest om full-service transacties te gebruiken, moet u:

1.  Uw transacties oefenen voor een schonere opname.
2.  [De transactie opnemen]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}).
3.  Uw opnamen uploaden voor verdere scripting. Nadat u de opname heeft gestopt, heeft u de optie om "full-service transacties" te kiezen om de opname naar Support te sturen.

Het uploadproces genereert een alleen-lezen controleregel in uw account terwijl de controleregel het full-service proces doorloopt. Na het scripten en testen, laten Uptrends' scriptingprofessionals u weten dat de controleregel klaar en voor u ontgrendeld is in uw account. Bekijk ons [beleid voor scriptbeoordeling]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="nl" >}}) voor informatie over voltooiingstijden van full-service transactiescripts en beperkingen op het aantal opnames dat u tegelijkertijd kunt indienen.

{{< callout >}}
**Opmerking**: Als u wat extra hulp nodig heeft bij het begrijpen van webapplicatie monitoring of als u een systematische aanpak nodig heeft om uw transacties te begrijpen, hebben we een aantal aanvullende artikelen die u wellicht wilt bekijken: [Webapplication monitoring begrijpen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="nl" >}}) en [Uw transacties begrijpen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="nl" >}}).
{{< /callout >}}

## Self-service transacties {id="self-service"}

Met self-service transacties heeft u volledige controle over het scripten van uw transacties. Deze opties zijn beschikbaar om uw scriptingdoelen te bereiken:

- Gebruik de [transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}) om het grootste deel van het werk voor u te doen, en verfijn en test het script vervolgens met de [stap-editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}).
- Sla de transaction recorder over en gebruik de [stap-editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}) rechtstreeks om uw scripts helemaal in de visuele stap-editor te maken.

Het wordt aanbevolen om te beginnen met de recorder, omdat dit het leven een stuk eenvoudiger maakt.

### Wie zou self-service transacties moeten gebruiken?

We moedigen iedereen aan om self-service transacties te gebruiken of uit te proberen. Het kost niets om scripts in development mode te bewerken en te testen. Misschien vindt u het bewerken en testen van uw transactiescripts zelfs leuk. [Support]({{< ref path="contact" lang="nl" >}}) staat altijd klaar om u te helpen of het over te nemen als u dat wilt. U kunt self-service transacties proberen als:

- U vertrouwd bent met elementaire webtechnologie en u meestal dingen kunt uitzoeken.
- U goed op de hoogte bent van de client-side technologieën zoals HTML, CSS, XPath en JSON.

### Om welke stappen gaat het?

1. Gebruik de [transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="nl" >}}) voor een snelle start.
2.  Open uw nieuwe controleregel in uw Uptrends-account en [bewerk en test]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}) erop los.

## Het script helemaal zelf bouwen {id="scripting-from-scratch"}

Er is een derde optie voor de heel ervaren gebruiker. Als u deze kiest, kunt u de transaction recorder en de stap-editor overslaan en uw script rechtstreeks in uw controleregelinstellingen invoeren met de scripttekst-editor. Klik gewoon op de knop {{< AppElement type="button" >}}Naar script schakelen{{< /AppElement >}} boven aan het tabblad {{< AppElement type="tab" >}}Stappen{{< /AppElement >}} van uw controleregel en bewerk of plak uw script.

U kunt ook de [API]({{< ref path="support/kb/api" lang="nl" >}}) gebruiken om nieuwe transactiecontroleregels te maken, uw controleregels te bewerken en te testen. 
