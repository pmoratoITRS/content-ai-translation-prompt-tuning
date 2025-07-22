{
  "title": "Uptrends' cliëntcertificaat public key-informatie",
  "summary": "Gebruik Uptrends public keys met uw Multi-step API-controleregel requests om te verzekeren dat API-controleregels afkomstig zijn van Uptrends.",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het cliëntcertificaat van Uptrends kan in Multi-step API-controleregels worden gebruikt om de authenticiteit te garanderen van de HTTP requests die door uw controleregels zijn gecreëerd: uw API server kan de identiteit verifiëren van Uptrends' controlestationservers, vanwaar de HTTP requests worden verzonden.

De controlestationservers gebruiken de private key van het certificaat om de requests te ondertekenen. Niemand anders heeft toegang tot die private key, dus niemand kan op dezelfde manier een request ondertekenen en zich voordoen als Uptrends. Dit betekent dat u, als de ontvangende partij, er zeker van kunt zijn dat deze requests daadwerkelijk afkomstig zijn van Uptrends' servers. Dit doet u door de identiteit van de inkomende requests te verifiëren met behulp van Uptrends' public key. De public key-informatie leest u hieronder.

[SHORTCODE_1]
**Let op:** Het Uptrends-cliëntcertificaat is niet beschikbaar op (containerized) [persoonlijke controlestations.]([LINK_URL_1]) 
[SHORTCODE_2]


## Hoe weet ik zeker dat deze public key echt is?

Bij het vaststellen van identiteit en authenticiteit is het belangrijk om te verifiëren dat u met de juiste informatie werkt.

### Vertrouwde verbinding en transport

-   We hebben ervoor gezorgd dat u de inhoud op deze pagina altijd leest met een HTTPS-verbinding. Deze beveiligde verbinding betekent dat de inhoud nooit gemanipuleerd kan worden (geen content hijacking) tijdens transport van onze webserver naar uw browser.
-   Zelfs als een kwaadwillende persoon erin slaagt u een HTTP-koppeling (d.w.z. een niet-beveiligde verbinding) naar de Uptrends-website te presenteren, die vervolgens onderschept kan worden en waarvan de inhoud gemanipuleerd kan zijn (een zogenoemde downgrade attack), zal uw browser dat niet accepteren. Browsers weigeren verbinding te maken met Uptrends via een niet-beveiligde verbinding om de volgende redenen:
    -   De website en customer app portal van Uptrends volgen een HTTP Strict Transport Security (HSTS)-beleid. Dit betekent dat browsers de instructie hebben nooit een onveilige HTTP-koppeling te volgen naar het domein uptrends.com, maar in plaats daarvan altijd HTTPS te gebruiken.
    -   Het domein uptrends.com bevond zich onder de eerste 1000 domeinen die vermeld werden op de HSTS-preloadlijst. Deze preloadlijst is ingebouwd in reguliere browsers zoals Chrome, Edge, Opera en Safari. Dit betekent dat deze browsers geprogrammeerd zijn om altijd HTTPS te gebruiken voor uptrends.com en zijn sub-domeinen.

### Vertrouwde identiteit

Als u het TLS-certificaat voor deze site bekijkt, zult u zien dat deze website eigendom is van Uptrends B.V. Het certificaat is ondertekend door Sectigo Limited, een van de wereldwijd erkende certificaatautoriteiten. Uw browser zou de verbinding zelfs niet vertrouwen zonder dat een CA het ondertekent. Dit is de best beschikbare manier om te bewijzen dat het domein dat u momenteel bezoekt feitelijk eigendom is van Uptrends, en dat u erop kunt vertrouwen dat de inhoud afkomstig is van Uptrends.

## Public key-informatie

De volgende informatie beschrijft eigenschappen van de public key die overeenkomen met het cliëntcertificaat dat wordt gebruikt door Uptrends' controlestationservers, wanneer zij de instructie hebben dit te doen. Dit cliëntcertificaat is, net als de certificaten die betrekking hebben op onze websites, ondertekend door een certificaatautoriteit.

[HTML_TAG_1]
  [HTML_TAG_2]
    [HTML_TAG_3]
      [HTML_TAG_4][HTML_TAG_5]
      [HTML_TAG_6][HTML_TAG_7]
    [HTML_TAG_8]
  [HTML_TAG_9]
  [HTML_TAG_10]
    [HTML_TAG_11]
      [HTML_TAG_12]Issuer[HTML_TAG_13]
      [HTML_TAG_14]CN = Sectigo RSA Client Authentication and Secure Email CA[HTML_TAG_15]O = Sectigo Limited[HTML_TAG_16]L = Salford[HTML_TAG_17]S = Greater Manchester[HTML_TAG_18]C = GB[HTML_TAG_19]
    [HTML_TAG_20]
    [HTML_TAG_21]
      [HTML_TAG_22]Subject[HTML_TAG_23]
      [HTML_TAG_24]E = certificates@uptrends.com[HTML_TAG_25]
    [HTML_TAG_26]
    [HTML_TAG_27]
      [HTML_TAG_28]Common name[HTML_TAG_29]
      [HTML_TAG_30]Uptrends[HTML_TAG_31]
    [HTML_TAG_32]
    [HTML_TAG_33]
      [HTML_TAG_34]Serial number[HTML_TAG_35]
      [HTML_TAG_36]1a223e5481b066dfda30e5f35cdb3a81[HTML_TAG_37]
    [HTML_TAG_38]
    [HTML_TAG_39]
      [HTML_TAG_40]Expiration date[HTML_TAG_41]
      [HTML_TAG_42]Sunday, 27 July 2025 01:59:59[HTML_TAG_43]
    [HTML_TAG_44]
    [HTML_TAG_45]
      [HTML_TAG_46]Full public key (Base64)[HTML_TAG_47]
      [HTML_TAG_48]—–BEGIN CERTIFICATE—– [HTML_TAG_49]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[HTML_TAG_50][HTML_TAG_51]
    [HTML_TAG_52]
  [HTML_TAG_53]
[HTML_TAG_54]