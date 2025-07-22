{
  "hero": {
    "title": "URL en analytics blokkeren"
  },
  "title": "URL en analytics blokkeren",
  "summary": "Analytics en andere URL's blokkeren in uw Full Page Checks en Transactie monitoring.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/analytics-blokkeren",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/analytics-blocking"
}

{{< callout >}}
**Opmerking:** URL- en analyticsblokkering zijn alleen beschikbaar voor [Enterprise- en Business-accounts]({{< ref path="/pricing" lang="nl" >}}).
{{< /callout >}}

De controleregeltypes Full page check (FPC) en Transactie laden uw webpagina in een browser, samen met alle elementen op de pagina, inclusief Google Analytics-scripts en andere derdepartijelementen. De pagina die wordt geladen in de browser van het controlestation, triggert echte paginaweergaven in uw webanalyse. Als uw website monitoring uw analyses te veel vertekent of als er een andere reden is waarom u niet wilt dat bepaalde elementen in de browser worden geladen, heeft u twee opties:

-   Google Analytics blokkeren
-   URL's blokkeren

{{< callout >}}
**Opmerking:** U hoeft zich geen zorgen te maken dat uw HTTP(S)-controleregels uw analyses vertekenen, want HTTP(S)-controleregels laden uw pagina niet in een browser, dus uw controles verschijnen sowieso niet in uw analyses.
{{< /callout >}}

## Hoe werkt request blokkering?

Als u de watervalgrafiek opent, ziet u de geblokkeerde element requests nog steeds. Waarom is dat? Nou, we kunnen niet simpelweg de browser vertellen deze URL’s niet te laden. Dus in plaats daarvan omzeilen we deze requests zodra we ze zien en voorkomen we dat ze naar internet gaan. Google Analytics zal deze requests nooit zien, dus blijven uw analyses veilig. De browser heeft nog steeds een antwoord nodig op deze requests om het normale HTTP-gedrag dat de browser verwacht niet te verstoren, dus retourneren we in plaats daarvan een normale response header met een 200 OK-status en een body content van 512 bytes.

## Hoe beïnvloedt request blokkering mijn rapporten?

Blokkeren heeft niet veel invloed op uw rapportage; wij laten u nog steeds zien wanneer de browser een geblokkeerd element zou hebben gedownload en we stoppen alle requests die deze elementen genereren. Om u te laten weten dat de controle het element blokkeerde is het element in uw watervalrapport doorgehaald. De doorhaling vertelt u precies welke requests de controle heeft onderschept op basis van de blokkeerinstellingen van uw controleregel.

![](/img/content/e13feb2b-6a95-479e-92aa-eea4deac6169.png)

## Wat wordt er geblokkeerd als je Google Analytics blokkeert?

Google biedt een reeks services die meer dan alleen analytics bevatten, daarom blokkeert Uptrends de meest voorkomende Google-elementen. Als u de optie Google Analytics blokkeren selecteert, blokkeert Uptrends:

-   google-analytics.com
-   stats.g.doubleclick.net
-   googleadservices.com
-   google.com/ads

Uptrends **blokkeert** googletagmanager.com **niet** om geen pagina's te verstoren die afhankelijk zijn van de elementenfunctionaliteit.

## Hoe blokkeer ik Google Analytics?

Omdat zoveel sites Google Analytics gebruiken, hebben we een selectievakje opgenomen bij uw controleregelinstellingen.

1.  Ga naar de instellingen van uw controleregel.
2.  Selecteer het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}}.
3.  Selecteer het selectievakje **Google Analytics blokkeren**.
4.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

Dat is alles! U bent klaar. Lees verder als u andere elementen heeft die u moet blokkeren.

## Hoe blokkeer ik andere URL's en andere elementen?

U kunt een URL om uiteenlopende redenen blokkeren, zoals bij het uitvoeren van een A/B-test. Met Uptrends' monitoring kunt u zo veel elementen blokkeren als u nodig heeft.

1.  Ga naar de instellingen van uw controleregel.
2.  Selecteer het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}}.
3.  Typ de volledige of gedeeltelijke URL van het element dat u wilt blokkeren in het vak **Deze (deel-)URL’s blokkeren**.
4.  Plaats elke URL op een nieuwe regel.
5.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

Wanneer het controlestation een uitgaande request ziet met een URL of tekenstrings in dit vak, zal het controlestation de request blokkeren. Mocht u hulp nodig hebben bij het blokkeren van elementen, [vraag het onze experts](/contact)!

{{< callout >}}
**Opmerking:** Het blokkeren van URL's kan veroorzaken dat uw pagina niet meer werkt en er onnodige alerts worden verstuurd. [Laat het ons weten](/contact) als u hulp nodig heeft.
{{< /callout >}}
