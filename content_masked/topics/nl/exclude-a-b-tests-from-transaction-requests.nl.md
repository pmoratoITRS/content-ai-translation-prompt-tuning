{
  "hero": {
    "title": "A/B-tests uitsluiten van transactierequests"
  },
  "title": "A/B-tests uitsluiten van transactierequests",
  "summary": "A/B tests can cause errors and generate needless alerts. You can prevent unwanted alerts by telling Uptrends to exclude requests to your A/B test tool's URL.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/a-b-tests-uitsluiten-van-transactierequests",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

A/B-testtools splitsen het verkeer naar uw webpagina door de ene groep gebruikers naar versie A van uw webpagina te sturen en de andere groep gebruikers naar versie B. Uw transactie monitoring genereert mogelijk fouten door A/B-testen vanwege verschil in pagina-inhoud. Als u bijvoorbeeld in versie A een knop 'Leg in winkelmandje' hebt genoemd en dezelfde knop in versie B 'Leg in winkelwagen', zult u fouten zien als het slagen van het script afhankelijk is van het vinden van de tekst 'Leg in winkelmandje.' Wanneer het script voor transactie monitoring gebaseerd is op het zoeken naar een element dat alleen voorkomt op versie A van uw pagina, zal het script niet slagen als het versie B ontvangt. U kunt deze fout voorkomen door de URL uit te sluiten voor uw A/B-testtool voor de requests die de Uptrends-controleregel uitvoert op uw site.  

[SHORTCODE_1]
**Opmerking:** Natuurlijk geldt dit ook voor de controleregel Full page check als u een controle uitvoert op specifieke inhoud die verandert tijdens een A/B-test.
[SHORTCODE_2]

## URL's uitsluiten bij A/B-testtool

Om URL's uit te sluiten bij de A/B-testtool doet u het volgende:

1.  Log in op uw Uptrends-account.
2.  Kies [SHORTCODE_5]Controleregels[SHORTCODE_6] in het menu Controleregels op het hoofdmenu.
3.  Klik op de controleregel om de details ervan weer te geven.
4.  Klik op het tabblad [SHORTCODE_7]Extra[SHORTCODE_8].
5.  Hier ziet u het tekstveld 'Deze (deel-)URL's blokkeren.'
6.  Typ de URL voor uw testtool in het tekstveld. Plaats elke uit te sluiten URL op een afzonderlijke regel.
7.  Klik op [SHORTCODE_9]Opslaan[SHORTCODE_10].

Meer hoeft u niet te doen. Nadat u uw uit te sluiten URL's hebt toegevoegd, verstuurt Uptrends geen uitgaande request naar uw A/B-testtool bij een controle van uw site. Zonder deze uitgaande request, triggert Uptrends nooit het A/B-testscript.

### Voorbeeld

Vul bij 'Deze (deel-)URL's blokkeren' de URL van uw A/B-testtool in. Gebruikt u bijvoorbeeld Visual Website Optimizer voor uw A/B-test, typ dan visualwebsiteoptimizer.com in het veld. Als u Optimizely gebruikt, moet u optimizely.com uitsluiten.

![]([LINK_URL_1])

[SHORTCODE_3]
**Opmerking:** Hoewel we de request die komt van de uitgesloten URL actief filteren, wordenwordt deze wel opgenomen in het watervalrapport onder de responsekopresponsheader 'X-Blocked-By-Uptrends: true.'
[SHORTCODE_4]
