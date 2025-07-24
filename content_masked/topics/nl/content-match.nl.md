{
  "hero": {
    "title": "Foutcondities – Pagina-inhoud"
  },
  "title": "Foutcondities – Pagina-inhoud",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/inhoudmatch",
  "summary": "Inhoudmatches zijn een manier om te controleren of de pagina die u monitort de juiste inhoud weergeeft.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Er zijn situaties waarin slechts de helft van de inhoud van uw website correct wordt geladen. Ontbrekende secties, tekst en alinea’s maken het voor gebruikers moeilijk om door uw website te navigeren. Als u een e-commercesite heeft, heeft deze slechte gebruikerservaring invloed op de prestaties van uw site en verliest u omzet zonder dat u het doorheeft.

## Foutconditie Pagina-inhoud

De foutconditie Pagina-inhoud garandeert dat de inhoud van uw website correct en volledig wordt geladen. Hiermee kunt u alle teksten, zinnen en reguliere expressies en matches opgeven als deze inhoud op uw website wordt weergegeven.

![Foutconditie pagina-inhoud]([LINK_URL_1])

## Inhoudmatch

Een inhoudmatch is een lijst met woorden die u specificeert en die de controleregel als referentiepunt gebruikt om te controleren of deze overeenkomen met de geladen inhoud van de website:

- Als een controleregel die de pagina controleert de inhoud *vindt*, wordt er *geen fout* gerapporteerd.
- Als een controleregel die de pagina controleert de inhoud *niet kan vinden*, wordt er *een fout* gerapporteerd.

## Inhoudmatch voor elk controleregeltype

Er zijn verschillende typen inhoudmatches beschikbaar voor verschillende controleregeltypes. inhoudmatch varieert afhankelijk van de categorie van de controleregel en welke data deze verzamelt:

### Uptime-controleregels

Uptime-controleregels verifiëren pagina-inhoud door een GET-request te doen naar de URL van uw website. Zodra de request succesvol is, valideert de controleregel de GET-responsinhoud van uw website.

Als u een website-URL monitort: [URL_1] zijn voorbeelden van inhoudchecks:

| Inhoudmatch-types | Voorbeelden |
|--|--|
| Document Object Model (DOM) of HTML-elementen | [SHORTCODE_1]
- [INLINE_CODE_1]
- [INLINE_CODE_2]
- [INLINE_CODE_3] 
[SHORTCODE_2] |
| [SHORTCODE_3] Tekstinhoud met gebruik van [reguliere expressie]([LINK_URL_2]) [SHORTCODE_4] | [SHORTCODE_5]
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
[SHORTCODE_6] |
| [SHORTCODE_7] [Geavanceerde]([LINK_URL_3]) inhoudmatch [SHORTCODE_8] | [SHORTCODE_9]
- [INLINE_CODE_4][SHORTCODE_10] |

### Browsercontroleregels

Browsercontroleregels verifiëren pagina-inhoud door de bron van de pagina van de website te controleren. De paginabron is de ruwe structuur van de website in HTML-formaat, inclusief de metadata, scripts en stijlinformatie van de pagina.

Als u een website-URL monitort: [URL_2] zijn voorbeelden van inhoudchecks:

| Inhoudmatch-types | Voorbeelden |
|--|--|
| Document Object Model (DOM) of HTML-elementen | [SHORTCODE_11]
- [INLINE_CODE_5]
- [INLINE_CODE_6]
- [INLINE_CODE_7] 
[SHORTCODE_12] |
| [SHORTCODE_13] Tekstinhoud met gebruik van [reguliere expressie]([LINK_URL_4]) [SHORTCODE_14] | [SHORTCODE_15]
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
[SHORTCODE_16] |
| [SHORTCODE_17] [Geavanceerde]([LINK_URL_5]) inhoudmatch [SHORTCODE_18] | [SHORTCODE_19]
- [INLINE_CODE_8][SHORTCODE_20] |

[SHORTCODE_21] **Opmerking:** Om de paginabron van uw website te openen gaat u naar uw website en drukt u op de toets **Ctrl + U**. U kunt ook met de rechtermuisknop ergens op de pagina klikken en op **Paginabron weergeven** klikken. Houd er rekening mee dat niet alle elementen in de paginabron geldige inhoudchecks zijn.[SHORTCODE_22]

### Multi-step API (MSA)-controleregels

MSA-controleregels controleren een inhoudmatch via **Assertions**. Met assertions kunt u controles definiëren om te valideren of de API-respons voldoet aan uw verwachte condities. Bijvoorbeeld als de respons statuscode 200 is of als de respons body als JSON specifieke teksten bevat. Voor meer informatie, zie [MSA Assertions]([LINK_URL_6]).

### Transactie-controleregels

Transactie-controleregels valideren pagina-inhoud door pagina-elementen te controleren die in de browser worden weergegeven. Ze controleren op specifieke tekst, knoppen, afbeeldingen en andere UI-elementen die zichtbaar zijn op uw website. Transactie-controleregels gebruiken **Inhoudcontroles**, acties die voor elke stap zijn geconfigureerd en die verifiëren of elk laden van de pagina verloopt zoals verwacht. Het kan bijvoorbeeld controleren of de tekst 'Succesvol toegevoegd aan winkelwagen' op de pagina verschijnt. Raadpleeg [Inhoudcontroles]([LINK_URL_7]) voor meer informatie.

## Types inhoudmatch

Hieronder staan types inhoudmatch die beschikbaar zijn voor sommige controleregeltypes:

### Gewone inhoudmatch {id = "regular-content-match"}

Een inhoudmatch kan worden ingesteld met behulp van reguliere expressies. Een reguliere expressie (regex of regexp) is een speciale tekenreeks die een zoekpatroon beschrijft. U kunt een inhoudmatch opgeven met:

- Eén woord: [INLINE_CODE_9]
- Meerdere woorden of zinnen in een bepaalde volgorde: [INLINE_CODE_10] (bijvoorbeeld, product EN order moeten voorkomen)
- Symbolen om andere elementen te matchen:
  - [INLINE_CODE_11] — gebruikt een uitroepteken om de betekenis van een woord om te keren of te ontkennen. Deze inhoudmatch betekent dat het woord *error* niet mag worden weergegeven.
  - [INLINE_CODE_12] — gebruikt een verticale balk om een ander woord te matchen. Deze inhoudmatch betekent dat de tekst [INLINE_CODE_13] OF [INLINE_CODE_14] zichtbaar moet zijn op uw website.

Raadpleeg voor meer informatie [Regular Expression Language - Quick Reference]([LINK_URL_8]).


### Geavanceerde inhoudmatch

U kunt meerdere inhoudmatches tegelijk gebruiken door waarden op te slaan in JSON-formaat. Als u twee patronen wilt combineren, die elke vorm van pagina-elementen en reguliere expressies kunnen zijn, gebruikt u:

[CODE_BLOCK_1]

Geef een geldige inhoudmatch in het veld [INLINE_CODE_15]. Stel [INLINE_CODE_16] in op [INLINE_CODE_17] als het patroon moet matchen met de inhoud van uw website of op [INLINE_CODE_18] als het niet matcht met enige inhoud van uw website.  

[SHORTCODE_23] **Opmerking:** De Geavanceerde inhoudmatch werkt voor de controleregels HTTPS, Webservices HTTP en HTTPS, en Full Page Check. [SHORTCODE_24]

Als u het tijdstempel van uw website wilt controleren op een inhoudmatch, gebruikt u:

[CODE_BLOCK_2]

De JSON-sleutel, [INLINE_CODE_19], kan waarden in regex-vorm bevatten, zoals \[HTML_TAG_1], \[HTML_TAG_2], \[HTML_TAG_3], \[HTML_TAG_4], \[HTML_TAG_5], and \[HTML_TAG_6]. Al deze waarden kunnen worden geëxtraheerd uit de inhoud van de website en worden samengevoegd met de huidige servertijd en vervolgens geëvalueerd in termen van UTC.

De [INLINE_CODE_20] is het aantal minuten dat moet worden afgetrokken om het te vergelijken met de servertijd in UTC. Als de webpagina een tijdstempel in UTC\+1 bevat, moet de offset 60 zijn. Als de webpagina een tijdstempel in EST (UTC-5) bevat, moet de offset -300 zijn.

De [INLINE_CODE_21] verwijst naar het maximale tijdsverschil in minuten dat is toegestaan tussen de paginatijd van de website en uw lokale tijd. Als uw lokale tijd bijvoorbeeld 10:06 is en de paginatijd van uw website 10:00, treedt er een fout op als [INLINE_CODE_22] is ingesteld op 5 minuten of minder.

## Waar configureer je een inhoudmatch

Om een inhoudmatch te configureren moet u een foutconditie toevoegen van het type **Pagina-inhoud controleren**:

1. Ga naar [SHORTCODE_25] Monitoring > Controleregels beheren [SHORTCODE_26].
2. Klik op de controleregel waaraan u een inhoudmatch wilt toevoegen.  
3. Navigeer naar het tabblad [SHORTCODE_27] Foutcondities [SHORTCODE_28].  
4. Voer in **Pagina-inhoud controleren** uw inhoudmatch-informatie in.
5. Klik op [SHORTCODE_29] Opslaan [SHORTCODE_30] om de wijziging in de controleregel te bevestigen.

Als u klaar bent, kunt u [een alertdefinitie creëren]([LINK_URL_9]) om een bericht te ontvangen wanneer aan de foutconditie **Pagina-inhoud controleren** is voldaan.
