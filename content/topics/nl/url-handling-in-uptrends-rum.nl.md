{
  "hero": {
    "title": "Hoe Uptrends in RUM omgaat met URL's"
  },
  "title": "Hoe Uptrends in RUM omgaat met URL's",
  "summary": "Heeft u zich weleens afgevraagd hoe Uptrends omgaat met URL's in Real User Monitoring? Lees dan dit artikel!",
  "url": "/support/kb/rum/hoe-uptrends-in-rum-omgaat-met-urls",
  "translationKey": "https://www.uptrends.com/support/kb/rum/url-handling-in-uptrends-rum"
}

Met Uptrends' RUM kunt u uw de statistieken van ervaringen van echte gebruikers op veel verschillende manieren groeperen. Als u op pagina groepeert, krijgt u veel inzicht in statistieken van specifieke pagina's die mogelijk aandacht nodig hebben vanwege problemen zoals lange laadtijden.

Uptrends kijkt naar de URL om te bepalen welke pagina uw bezoeker heeft bekeken. Veel moderne websites gebruiken automatisch gegenereerde URL's, en dit kan tot een extreem groot aantal unieke URL's leiden. Aangezien het niet zinvol zou zijn data van tienduizenden pagina's te verzamelen, **hebben we standaard het maximum aantal unieke pagina's per website beperkt tot 10.000**. Wanneer u dit aantal overschrijdt, worden de nieuwe unieke pagina's vermeld onder 'Anders'.

## URL-normalisatie

Om het aantal unieke URL's dat we moeten controleren te verminderen terwijl we tegelijkertijd de verschillende pagina's van uw website correct blijven scheiden, passen we een **URL-normalisatieproces** toe. URL-normalisatie betekent dat de URL's die u in Uptrends ziet enigszins kunnen afwijken van de URL's die uw website feitelijk gebruikt. Het gaat er met name om dat we:

-   het verschil tussen `http://` en `https://` negeren.
-   de query string verwijderen (bijv. `?parameter=value` achteraan).
-   fragmenten verwijderen (bijv. `#fragment` achteraan), behalve als de optie **URL-fragment meerekenen** is ingeschakeld in de RUM-website-instellingen.
-   dubbele schuine strepen (//) uit het padgedeelte van de URL verwijderen.
-   segmenten (delen van het pad die afgebakend worden door een schuine streep) die geheel uit cijfers of GUID's bestaan, vervangen door sterretjes (`***`)
-   lange cijferreeksen (&gt;4 cijfers) en GUID's in segmenten vervangen door sterretjes. Bijvoorbeeld `www.mysite.com/coupon-12345` en `www.mysite.com/coupon-123456` worden beide `www.mysite.com/coupon-***`  
    URL's met GUID's zoals `www.mysite.com/coupon-19740f6e-e7e6-41f2-84e4-de0b290eb05e` worden `www.mysite.com/coupon-***`, waarbij de drie sterretjes de gehele GUID vervangen.

## Feedback

We ontvangen graag uw vragen en feedback. Neem [contact met ons op](/contact), vooral als u merkt dat Uptrends' RUM de verschillende pagina's van uw website niet optimaal volgt.
