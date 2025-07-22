{
  "hero": {
    "title": "Real User Monitoring instellen"
  },
  "title": "Real User Monitoring instellen",
  "summary": "Leer hoe u met enkele eenvoudige stappen aan de slag gaat met Real User Monitoring.",
  "url": "[URL_BASE_TOPICS]rum/instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Real User Monitoring** (RUM) verzamelt performancedata van echte bezoekers van uw website. De reguliere synthetische monitoring van Uptrends werkt in een voorspelbare omgeving en gebruikt een vast monitoringinterval. Synthetische monitoring werkt goed voor het monitoren van beschikbaarheid en het detecteren van veranderingen in de performance van webpagina’s. RUM daarentegen, werkt in minder voorspelbare omgevingen (bijvoorbeeld op de apparaten en computers van uw eindgebruikers) en richt zich dus veel meer op het meten van de feitelijke ervaring van uw gebruikers. We hebben uw op RUM gebaseerde data in uw bestaande Uptrends-account geplaatst, en u kunt uw RUM-data en synthetische data naast elkaar bekijken.

## Aan de slag met Uptrends RUM

Om aan de slag te gaan met RUM zijn twee handelingen nodig: 
- Een RUM-websitedefinitie aan uw account toevoegen.
- Het script in uw eigenlijke website implementeren.

### Uw eerste RUM-website aan uw account toevoegen

1. Log in bij uw Uptrends-account. Als u nog geen account heeft, ga dan naar de [aanmeldpagina]([LINK_URL_1]) en meld u aan voor uw gratis proefperiode.
2. Als u de functie Real User Monitoring in Uptrends nog niet gebruikt, kunt u deze gratis uitproberen door een RUM-proefperiode te starten. Klik in het menu Tools & apps op de optie *Real User Monitoring proberen*.
3. Klik op de pagina  *RUM proefperiode starten* op de knop [SHORTCODE_7]Real User Monitoring proberen[SHORTCODE_8].
4. Vul de URL in van de website die u wilt monitoren. Klik op de knop [SHORTCODE_9]Voeg uw eerste RUM-website toe[SHORTCODE_10].
5. Uw RUM proefperiode is nu begonnen. Klik op de knop [SHORTCODE_11]Instructies tonen[SHORTCODE_12] om naar de instellingen van uw nieuwe RUM-website te gaan.

### Extra RUM-websites toevoegen

Nadat de initiële configuratie is voltooid, bevat de sectie *RUM* in het menu een subsectie *Echte gebruikers* waar u de RUM-gerelateerde dashboards kunt vinden en uw RUM-websites kunt beheren. Om extra RUM-websites toe te voegen:

1. Vouw de *RUM*-sectie in het menu uit.
2. Klik op het pictogram *\+* naast *RUM websites*.
![Een RUM-website toevoegen]([LINK_URL_2])
3. Vul de *Naam* voor de website en zijn *URL* in.
4. Als uw website een single-page application (SPA) is, vink dan de optie *Single Page Application Tracking gebruiken* aan. 
5. Als de website URL-fragmenten gebruikt (bijvoorbeeld [INLINE_CODE_1] aan het eind), en die een aanzienlijk deel van uw URL’s vormen, vink dan de optie *URL-fragment meerekenen* aan. Door dit te doen voorkomt u dat Real User Monitoring alles na het #-symbool negeert.
6. Nadat u alle opties heeft ingesteld, klikt u linksonder op de knop [SHORTCODE_13]Opslaan[SHORTCODE_14].
7. Het script verschijnt nu in het tabblad [SHORTCODE_15]Implementatie[SHORTCODE_16]. In het volgende gedeelte wordt de implementatie van het script behandeld. 

### Het script in uw website implementeren

Anders dan bij reguliere website monitoring moet u nu zelf wat werk doen. U krijgt van Uptrends een klein stukje JavaScript dat u toevoegt aan de webpagina’s die u met RUM wilt monitoren. Uptrends heeft het script zo ontworpen dat het andere scripts op uw website niet hindert en uw eindgebruikers niet merken dat u het Uptrends RUM-script aan uw pagina’s heeft toegevoegd. De [impact van de aanwezigheid van het RUM script op uw site]([LINK_URL_3]) is vrijwel nul.

1. Zorg ervoor dat u toegang heeft tot de code van uw website, zodat u de inhoud van uw pagina’s kunt wijzigen.
2. Ga naar [SHORTCODE_17] RUM > Echte gebruikers > RUM websites [SHORTCODE_18].
3. Klik op de website die u wilt implementeren.
4. Ga naar het tabblad [SHORTCODE_19]Implementatie[SHORTCODE_20].
5. Selecteer en kopieer het [RUM-script]([LINK_URL_4]).
6. Plak het script tussen de [INLINE_CODE_2] tags van de pagina's die u met RUM wilt monitoren. Door het script binnen de [INLINE_CODE_3] tags te plaatsen weet u zeker dat het script zo vroeg mogelijk laadt. Door vroeg te laden kan de controleregel zoveel mogelijk timinggegevens vastleggen.

- Als uw website een Content Security Policy (CSP)-response header bevat, zorg er dan voor dat het Uptrends RUM-domein [INLINE_CODE_4] is [toegevoegd en correct ingesteld]([LINK_URL_5]) op uw website. Om te verifiëren dat het Uptrends RUM-script correct werkt, controleert u de broncode van uw website en kijkt u of het Uptrends RUM-script bestaat. Open het tabblad *Hulpprogramma's voor ontwikkelaars > Netwerk* van uw browser en controleer of Uptrends RUM-bronnen zonder problemen worden geladen.

7. Start uw website opnieuw op om deze bij te werken met het toegevoegde script.
8. RUM-data worden verzameld zodra gebruikers uw bijgewerkte site bezoeken. U ziet de data meteen in het [dashboard RUM-overzicht]([LINK_URL_6]), [in real time]([LINK_URL_7]).

[SHORTCODE_1]
**Opmerking:** Als u de optie *Single Page Application tracking gebruiken* voor een bestaande RUM-website inschakelt, moet u er rekening mee houden dat het script na het opslaan verandert en daarom ook aan uw kant moet worden bijgewerkt.
[SHORTCODE_2]

## Licentie

Uptrends stelt het RUM-script en de componenten die het script gebruikt beschikbaar onder een BSD (Berkeley Software Distribution) licentie. De volledige tekst kunt u vinden op [HTML_TAG_1].

[SHORTCODE_3]
**Bezorgd over privacy?** We hebben een [privacypagina]([LINK_URL_8]) met uitleg over hoe Uptrends gebruikersprivacy beschermt, extra stappen waarmee u gebruikersprivacy kunt verbeteren en suggesties voor aanvullingen op uw privacystatement.
[SHORTCODE_4]

## Eén script per website

Houd er rekening mee dat elk script specifiek is voor één enkele website aangezien het een [INLINE_CODE_5] bevat dat de corresponderende RUM-website in uw account op unieke wijze identificeert. Voor elke paginaweergave die Uptrends registreert bij een bepaalde RUM-website, verifiëren wij dat de paginaweergave werkelijk afkomstig is van het websitedomein dat u heeft gespecificeerd. We geven een voorbeeld om duidelijk te maken wat we bedoelen. 
**Voorbeeld**: We gebruiken [INLINE_CODE_6] als voorbeeldwebsite. Er wordt standaard toegestaan dat er page views komen van zowel [INLINE_CODE_7] als [INLINE_CODE_8]. Als u hetzelfde script ook zou opnemen in een website die gehost wordt op [INLINE_CODE_9] of [INLINE_CODE_10], zal RUM op deze andere domeinen niet werken, want RUM registreert geen page views die van andere domeinen komen. Elke website moet een afzonderlijke RUM-instantie hebben om zinvolle gegevens te verkrijgen.

Als u RUM-gegevens op meer dan één website wilt volgen, moet u deze ook in Uptrends als afzonderlijke RUM-websites beschouwen. Voor elk websitedomein dat u wilt monitoren moet u een extra RUM-website instellen, want elk domein krijgt een ander script.

De domeinverificatie betekent ook dat RUM alleen in uw echte productieomgeving werkt. Als u afzonderlijke ontwikkel- en testomgevingen heeft die lokaal of onder een ander domein runnen, zal RUM van deze sites geen page views registreren.

[SHORTCODE_5]
**Opmerking:** Misschien gelden er bij u bijzondere omstandigheden waar precies dezelfde site op meerdere domeinen runt, terwijl u deze als één site wilt behandelen. [Neem contact op met Support]([LINK_URL_9]) om dit in te stellen.
[SHORTCODE_6]
