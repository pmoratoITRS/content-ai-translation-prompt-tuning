{
  "hero": {
    "title": "User agents en echte browser checks"
  },
  "title": "User agents en echte browser checks",
  "summary": "User agents zijn een uitstekende manier om synthetische tests uit te voeren voor specifieke gebruikersomgevingen zoals mobiel. In dit artikel leest u hoe echte browsercontroles en user agents handig voor u kunnen zijn.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/user-agents-en-echte-browser-checks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Als u het onderwerp user agents en real browser monitoring verwarrend vindt, kunt u gerust zijn: u bent niet de enige. Verwarring over user agents en hun toepassing met real browser monitoring is een van de meestgestelde vragen aan ons support team. Het korte antwoord is:

Real browser checks (Full Page Check en transactiemonitoring) gebruiken een echte browser (net als de bezoekers van uw site) om de inhoud van uw website op te halen en te laden. De browser genereert een user agent die uw servers vertelt over de omgeving van uw gebruiker. Door de user agent kan de server geoptimaliseerde inhoud retourneren voor de specifieke omgeving die door de user agent is gedefinieerd. U kunt de user agent in uw controleregels manipuleren om inhoud te testen die is bedoeld voor andere browsers, besturingssystemen en apparaten zoals mobiele telefoons en tablets.

Misschien niet zo kort, maar als het korte antwoord voor u voldoet — geweldig! Voor de anderen gaan we iets dieper in op het onderwerp. Laten we eerst kijken naar de drie belangrijkste componenten van HTTP-communicatie.

## De spelers

Communicatie is tweerichtingsverkeer tussen twee partijen; de ene partij vraagt om informatie en de andere geeft informatie. Wat die informatie mogelijk maakt, is taal, en opdat beide partijen elkaar begrijpen, moeten ze een taal delen. Laten we de spelers eens bekijken:

-   **Client**: De client vraagt om iets van een resource. De client kan een internetbrowser zijn of een ander soort softwareapplicatie zoals een webcrawler.
-   **HTTP**: De gemeenschappelijke taal. Het Hypertext Transfer Protocol geeft duidelijk de semantiek van de communicatie aan.
-   **Server**: De server stuurt de informatie terug naar de client. De informatie is aangepast voor die client op basis van de user agent.

Een client gebruikt een HTTP request om informatie van de server te vragen, en de server stuurt de informatie terug als een HTTP-response. Maar hoe sluit dit allemaal aan bij real browser checks en user agents? Laten we beginnen met de user agent.

## Wat is een user agent?

Een user agent is een specifiek veld in de HTTP request dat informatie over de client bevat. De server zoekt naar specifieke woorden in de tekst en negeert al het andere. Dus op basis van wat de server wel of niet vindt in de tekst van de user agent, bouwt de server de inhoud op die is geoptimaliseerd voor de client. De user-agent omvat:

-   Browsertype en -versie
-   Besturingssysteem en -versie
-   Rendering engine

Om het verwarrend te maken zult u zien dat user agents stukjes informatie bevatten zoals de tekst 'Mozilla / 5.0' (te vinden in de meeste user agents van de browser) die de server inseinen dat deze client compatibel is met die browser. 

De Chrome user agent vertelt de server dat het een Mozilla/5.0-browser, een Safari-browser en een Chrome-browser is, zoals u kunt zien in de onderstaande user agent.

[INLINE_CODE_1]

## Wat is een real browser check?

Zoals hierboven beschreven, kan een client elke softwareapplicatie zijn die in staat is om via internet te communiceren, en een internetbrowser is slechts één type cliënt. Softwareapplicaties zijn perfect tevreden met de communicatie in het ruwe formaat, maar uw eindgebruikers zouden dat niet leuk vinden. In plaats daarvan neemt de browser voor eindgebruikers alle geretourneerde inhoud, parst deze en geeft deze visueel weer op het scherm.

U kunt uw site testen met behulp van een [eenvoudig type controleregel of een echte browser check]([LINK_URL_1]). Uptrends' controlestations kunnen wel of geen browser gebruiken, afhankelijk van het type controleregel dat u heeft geselecteerd. De standaard HTTP- en HTTPS-controleregels genereren een request en sturen deze naar de server (zonder een browser te gebruiken). Wanneer de controlestationcomputer de response ontvangt, zoekt die naar een resultaatcode, misschien wat specifieke inhoud en enkele andere basiselementen. De response wordt nooit verwerkt, afbeeldingen worden nooit gedownload en scriptbestanden nooit uitgevoerd. Dit proces vertelt u of uw site wel of niet in de lucht is.

Wanneer u ervoor kiest te monitoren met een echte browser, openen Uptrends' controlestationcomputers een browservenster en verzenden ze een request naar uw server, net zoals uw sitebezoekers dat doen met de browser. De response wordt ontvangen, verwerkt, afbeeldingen worden gedownload, scriptbestanden uitgevoerd en CSS-bestanden toegepast en de pagina verschijnt in het browservenster. Een echte browser check zoals de [Full page check]([LINK_URL_2]) voorziet u van informatie over verbindingstijden en laadtijden voor elk element op de pagina, samen met eventuele niet-werkende inhoud. We kunnen zelfs een screenshot maken wanneer er fouten op de pagina optreden.

## Wat is nu de cross-over tussen user agents en Real Browser Monitoring?

U kunt de user agent wijzigen voor zowel niet-browsergebaseerde controleregels als voor browsergebaseerde controleregels. U wilt misschien de user agent voor eenvoudige controleregels wijzigen, zodat u inhoudcontroles kunt uitvoeren die specifiek zijn voor bepaalde gebruikersomgevingen. U zult zien dat de echte kracht in het gebruik van een echte browser ligt. Door de user agent te wijzigen, kunt u de performance en inhoud van de pagina testen voor vrijwel elke gebruikersomgeving. We bekijken een paar voorbeelden:

### Het is een mobiel-gecentreerde wereld

Mobiel is snel bezig de desktop te overtreffen in gebruikersvoorkeur. Dus is het heel belangrijk dat u weet dat uw servers met uw mobielspecifieke inhoud snel reageren. Behalve handmatig testen, denkt u misschien dat u niet veel kunt doen aan de manier van testen van uw mobiele site. Niet waar. Het gebruik van user agents voor een real browser check kan elk apparaat, schermformaat en mobiele browser emuleren. Uw servers reageren met uw mobiele inhoud en onze real browser checks laden de inhoud. Hieronder vindt u enkele user agents voor populaire apparaten, besturingssystemen en browsers.

**Android Chrome**

[INLINE_CODE_2]

**iPhone Safari**

[INLINE_CODE_3]

**Amazon Fire**

[INLINE_CODE_4]

### Test voor niet-ondersteunde browsers

Momenteel kunt u native testen met Chrome en binnenkort hebben we anderen in onze pijplijn om toe te voegen. Het gebruik van de huidige native browser is geweldig voor het testen van uw gebruikers die hun browsers regelmatig bijwerken, maar een groot percentage gebruikers doet dat niet. Dus hoewel uw site goed werkt in de huidige Chrome-browser, hoe werkt deze dan op een versie die vijf updates achterloopt? Door de user agent te wijzigen, kunt u elke versie van de browser testen.

### Test andere besturingssystemen

Een Chrome-browser die op Mac OSX draait, kan een heel andere ervaring hebben dan dezelfde Chrome-browser die op Windows 10 draait. De enige manier om dit zeker te weten, is door uw user agent aan te passen en andere besturingssystemen en versies te specificeren. Als u de native browser op het controlestation gebruikt, gebruikt de user agent standaard het besturingssysteem van het controlestation en de huidige browserversie.
