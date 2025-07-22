{
  "hero": {
    "title": "Foutcondities - W3C-kengetallen controleren"
  },
  "title": "Foutcondities - W3C-kengetallen controleren",
  "summary": "Grenswaarden gebruiken op W3C-kengetallen om fouten te activeren.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-w3c",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het World Wide Web Consortium (of kortweg W3C) is een internationale organisatie die zich bezighoudt met het ontwikkelen van standaarden voor het wereldwijde web. Als zodanig heeft het een standaard gedefinieerd voor browsers en webapplicaties om timinginformatie over het laden van webpagina's te genereren en weer te geven. 

De controleregeltypes die gebruikmaken van een [browsertype met extra kengetallen]([LINK_URL_1]) meten en rapporteren de [W3C-kengetallen voor navigatietijden]([LINK_URL_2]). Deze kengetallen worden gerapporteerd in de Details van de controle van de controleregel en u kunt er foutcondities voor instellen. Condities voor W3C-kengetallen maken deel uit van de [Foutcondities]([LINK_URL_3]). 

Houd er rekening mee dat verschillende controleregeltypes verschillende foutcondities bieden. Bekijk de tabel in [Welke foutcondities zijn beschikbaar?]([LINK_URL_4]) om te achterhalen welke opties beschikbaar zijn voor bepaalde controleregeltypes.

## Foutcondities definiëren op basis van de W3C-kengetallen

Om foutcondities te definiëren die de W3C-navigatietiming gebruiken:

1. Ga naar [SHORTCODE_1] Monitoring > Controleregels beheren [SHORTCODE_2].
2. Klik op de naam van de controleregel om deze te bewerken.
3. Open het tabblad [SHORTCODE_3] Foutcondities [SHORTCODE_4].
4. Vouw de categorie *W3C-kengetallen controleren* uit door op de pijl ervoor te klikken.
 
   ![screenshot foutconditie w3c-kengetallen]([LINK_URL_5])

5. Schakel foutcondities in door het selectievakje aan te vinken en een waarde in te stellen. Laat alle kengetallen uitgeschakeld die u niet aan een foutconditie wilt toewijzen.
6. Klik op de knop [SHORTCODE_5] Opslaan [SHORTCODE_6].

## De W3C-kengetallen [ANCHOR_1]

De W3C-kengetallen die worden gemeten door controleregels met het [browsertype met extra kengetallen]([LINK_URL_6]) worden uitgelegd in het Knowledge Base-artikel [Kengetallen voor W3C-navigatietijden]([LINK_URL_7]). De kengetallen komen overeen met de foutcondities in de categorie *W3C-kengetallen controleren*. Het enige kengetal dat niet aanwezig is in die lijst met foutcondities is de Load event. In [Foutconditie load event]([LINK_URL_8]) hieronder leest u hoe u een foutconditie voor dat kengetal instelt.

## Foutconditie load event [ANCHOR_2]

Mogelijk mist u het W3C-kengetal load event in de categorie *W3C-kengetallen controleren* van de foutcondities. Als u een foutconditie voor dit kengetal wilt instellen, kunt u dit doen voor [Full Page Check]([LINK_URL_9]) controleregels. Doe het volgende:

1. Open de controleregelinstellingen.
2. Zorg ervoor dat u op het tabblad [SHORTCODE_7] Algemeen [SHORTCODE_8] het **Browsertype** *Chrome met extra kengetallen* heeft gekozen.
3. Op het tabblad [SHORTCODE_9] Extra [SHORTCODE_10] in het gedeelte *Meting* stelt u de **Laadtijd baseren op** in op *W3C load event*.
4. Stel op het tabblad [SHORTCODE_11] Foutcondities [SHORTCODE_12] grenswaarden in voor **Laadtijd van de pagina controleren**.

Het Knowledge Base-artikel [Foutcondities - Paginalaadtijd]([LINK_URL_10]) bevat meer informatie over het instellen van grenswaarden voor laadtijden.
