{
  "hero": {
    "title": "Foutcondities overzicht"
  },
  "title": "Foutcondities overzicht",
  "summary": "Wat zijn foutcondities en hoe gebruik je ze? ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-overzicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": false
}

Foutcondities spelen een belangrijke rol bij het genereren van uw monitoringalerts. Het instellen van een foutconditie is de eerste stap van de [alert- en foutstroomcyclus]([LINK_URL_1]) waarmee u alertberichten kunt ontvangen.

Met een **foutconditie** kunt u een reeks criteria definiëren om uw controleregel te informeren over fouten op uw website, webservice of server. Het dient als basis voor uw controleregel om te bepalen welk websitegedrag in een fout resulteert en welk niet.

Als u bijvoorbeeld wilt dat uw website minder dan drie seconden nodig heeft om te laden, kunt u een foutconditie instellen en drempels voor de laadtijd van de pagina opgeven. Als u wilt controleren of de inhoud, plug-ins of scripts van uw website correct worden geladen, kunt u voor elk type specifieke foutcondities instellen.

Zodra aan een foutconditie is voldaan, wordt er een fout gegenereerd die een alert activeert. Als alerting is geconfigureerd, wordt u onmiddellijk door een alertbericht op de hoogte gesteld.

## Foutcondities voor controleregeltypes [ANCHOR_1]

Op het tabblad [SHORTCODE_15] Foutcondities  [SHORTCODE_16] kunt u verschillende foutcondities instellen die beschikbaar zijn voor elk type controleregel. Houd er rekening mee dat de beschikbaarheid van foutcondities kan variëren, afhankelijk van de categorie van de controleregel en welke data deze verzamelt:

![screenshot foutcondities controleregelset-up]([LINK_URL_2])

### Uptime controleregel

De volgende foutcondities zijn beschikbaar voor [Uptimecontroleregel]([LINK_URL_3])-types:

| Controleregeltype | Foutcondities | 
|--|--|
| HTTPS, Webservice HTTP en HTTPS | [SHORTCODE_1] 
- [Beschikbaarheid van de pagina controleren]([LINK_URL_4]) 
- [Pagina-inhoud controleren]([LINK_URL_5])
- [Laadtijd van de pagina controleren]([LINK_URL_6])
- [Resources controleren]([LINK_URL_7])
[SHORTCODE_2] |
| DNS, SSL, SFTP, FTP | [SHORTCODE_3]
- [Resources controleren]([LINK_URL_8])
- [Totale tijd van uitvoeren controleren]([LINK_URL_9])
[SHORTCODE_4] |
| SMTP, POP3, IMAP | [SHORTCODE_5]
- [Resources controleren]([LINK_URL_10])
- [Totale tijd van uitvoeren controleren]([LINK_URL_11])
[SHORTCODE_6] |
| Microsoft SQL servers,  MySQL | [SHORTCODE_7]
- [Resources controleren]([LINK_URL_12])
- [Totale tijd van uitvoeren controleren]([LINK_URL_13])
[SHORTCODE_8] |
| Ping, Connect | [SHORTCODE_9]
- [Resources controleren]([LINK_URL_14])
- [Totale tijd van uitvoeren controleren]([LINK_URL_15])
[SHORTCODE_10] |

### Browser- of Full-Page Check (FPC)-controleregel

De volgende foutcondities zijn beschikbaar voor [Browser- of Full-Page Check (FPC)-controleregels]([LINK_URL_16]):

| Controleregeltype | Foutcondities |
|--|--|
| Browser of Full-Page Check | [SHORTCODE_11]

- [Beschikbaarheid van de pagina controleren]([LINK_URL_17]) 
- [Pagina-inhoud controleren]([LINK_URL_18])
- [De URL's die door de pagina worden ingeladen controleren]([LINK_URL_19]) 
- [Laadtijd van de pagina controleren]([LINK_URL_20])
- [Core Web Vitals controleren]([LINK_URL_21])
- [W3C Kengetallen controleren]([LINK_URL_22])
- [Inhoud console controleren]([LINK_URL_23])
- [Resources controleren]([LINK_URL_24])
[SHORTCODE_12] |

### Transactiecontroleregel

Foutcondities in [transactiecontroleregels]([LINK_URL_25]) zijn ook beschikbaar voor elke stap. Afhankelijk van de [transactiestapset-up]([LINK_URL_26]), zijn de volgende foutcondities mogelijk wel of niet beschikbaar:

![screenshot foutcondities controleregelset-up]([LINK_URL_27])

| Controleregeltype | Foutcondities |
|--|--|
| Transactie of User journey | [SHORTCODE_13] 
- [Inhoudcontroles]([LINK_URL_28])
- [Resources controleren]([LINK_URL_29])
- [De URL's die door de pagina worden ingeladen controleren]([LINK_URL_30]) 
- [Core Web Vitals controleren]([LINK_URL_31])
- [W3C Kengetallen controleren]([LINK_URL_32])
- [Inhoud console controleren]([LINK_URL_33])
- [Beschikbaarheid van de website controleren]([LINK_URL_34]) 
- [Totale tijd van uitvoeren controleren]([LINK_URL_35])
[SHORTCODE_14] |

Houd er rekening mee dat de [Multi-step API (MSA)-controleregel]([LINK_URL_36]) een andere manier gebruikt om fouten te detecteren. Het gebruikt **Assertions** om u controles te laten definiëren om te valideren of de API-respons voldoet aan uw verwachte voorwaarden. Raadpleeg [MSA Assertions]([LINK_URL_37]) voor meer informatie.

## Een Foutconditie instellen [ANCHOR_2]

U kunt foutcondities toevoegen wanneer u [uw controleregel helemaal vanaf het begin instelt]([LINK_URL_38]) of een bestaande controleregel bewerkt.

Foutcondities instellen:

1. Ga naar [SHORTCODE_17] Monitoring > Controleregels beheren [SHORTCODE_18].
2. Klik op de controleregel waaraan u een foutconditie wilt toevoegen.
3. Ga naar het tabblad { [SHORTCODE_19] Foutcondities [SHORTCODE_20].
4. Klik op de foutconditie om de sectie uit te vouwen en de controleregelinstellingen te configureren.
5. (Optioneel) Om nieuwe controles voor een foutconditie toe te voegen klikt u op de knop [SHORTCODE_21] \+ Nieuwe controle [SHORTCODE_22].
6. Ga door met het configureren van condities.
7. Klik op [SHORTCODE_23] Opslaan [SHORTCODE_24] om de wijzigingen in de controleregel te bevestigen.

Als u een melding wilt ontvangen wanneer aan een foutconditie is voldaan, [creëert u een alertdefinitie]([LINK_URL_39]).

![screenshot foutcondities controleregelset-up]([LINK_URL_40])