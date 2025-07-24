{
  "hero": {
    "title": "Systeemvariabelen voor alerting"
  },
  "title": "Systeemvariabelen voor alerting",
  "summary": "Een overzicht van beschikbare systeemvariabelen voor gebruik in (aanpasbare) integraties",
  "url": "[URL_BASE_TOPICS]alerting/integraties/aangepaste-integraties/systeemvariabelen-voor-alerting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Dit artikel bevat een overzicht van alle beschikbare **Systeemvariabelen** die kunnen worden gebruikt om het uitgaande alertbericht te vullen met relevante informatie over zaken als de controleregel die de alert heeft veroorzaakt, welke fout is opgetreden of de alert zelf. Meer informatie over het gebruik van deze systeemvariabelen vindt u in ons artikel over [het bouwen van de juiste berichtinhoud]([LINK_URL_1]).

Kort gezegd, om de hier vermelde variabelen te gebruiken moeten ze verpakt in dubbele accolades worden opgenomen in de berichtinhoud. Ter illustratie: [INLINE_CODE_1].

|  Variabele   | Beschrijving    |  Voorbeeldwaarde   |
| --- | --- | --- |
| [INLINE_CODE_2] | Uw Uptrends-account-ID. | [INLINE_CODE_3] |
| [INLINE_CODE_4] | Unieke ID van deze alert. | [INLINE_CODE_5] |
| [INLINE_CODE_6] | Bevat de naam of locatie van het controlestation van waaruit de alert het laatst is gecontroleerd. | [INLINE_CODE_7] |
| [INLINE_CODE_8] | Tekstbeschrijving van de fout die deze alert heeft getriggerd. Bevat stapnummer indien van toepassing. | [INLINE_CODE_9] |
| [INLINE_CODE_10] | De tijd tussen de eerste fout en het huidige (Ok-) alert-tijdstempel. | [INLINE_CODE_11] |
| [INLINE_CODE_12] | [SHORTCODE_1] De fouttype-ID van de fout die deze alert heeft getriggerd, zie [Fouttypes]([LINK_URL_2]) voor een lijst met fouttypes. [SHORTCODE_2] | [INLINE_CODE_13] |
| [INLINE_CODE_14] | De aangepaste foutmelding voor de specifieke actie in een transactiestap die de fout heeft veroorzaakt | [INLINE_CODE_15] |
| [INLINE_CODE_16] | Dezelfde datum en tijd als @alert.firstErrorUtc, maar in de tijdzone van uw account. Ook geformatteerd als ISO 8601. | [INLINE_CODE_17] |
| [INLINE_CODE_18] | De ID van de fout die deze alert heeft getriggerd. | [INLINE_CODE_19] |
| [INLINE_CODE_20] | De URL van een deep link die u naar de details van de fout leidt die deze alert heeft getriggerd. | [INLINE_CODE_21] |
| [INLINE_CODE_22] | De foutbeschrijving van de eerste controleregelcheck die de fout ontving. Bevat stapnummer indien van toepassing. | [INLINE_CODE_23] |
| [INLINE_CODE_24] | Dezelfde datum en tijd als @alert.firstErrorUtc, maar in de tijdzone en cultuur van uw account. | [INLINE_CODE_25] |
| [INLINE_CODE_26] | De datum en tijd van de oorspronkelijke fout die deze alert heeft getriggerd, uitgedrukt in UTC-tijd en geformatteerd als ISO 8601. | [INLINE_CODE_27] |
| [INLINE_CODE_28] | De datum en tijd van de oorspronkelijke fout die deze alert heeft getriggerd, uitgedrukt in UTC-tijd en geformatteerd in de cultuur van uw account. | [INLINE_CODE_29] |
| [INLINE_CODE_30] | Bevat het totale aantal opeenvolgende fouten (bevestigde fouten) van de alert. | [INLINE_CODE_31] |
| [INLINE_CODE_32] | Het IP-adres dat werd gebruikt om de controle uit te voeren. Kan een IPv4- of een IPv6-adres zijn. | [INLINE_CODE_33] |
| [INLINE_CODE_34] | [SHORTCODE_3] Bevat de responsheaders van de alert in sleutel-waardeparen. Houd er rekening mee dat de waarde van deze variabele leeg kan zijn als [Gegevensbescherming van persoonlijke locaties]([LINK_URL_3]) is ingeschakeld op een persoonlijke controlestationlocatie die de alertcontrole uitvoert. [SHORTCODE_4] | [INLINE_CODE_35] |
| [INLINE_CODE_36] | [SHORTCODE_5] Bevat de ontvangen response body wanneer deze beschikbaar is. Merk op dat de response body tekens kan bevatten die moeten worden gecodeerd, bijv. [met @JsonEncode of @XmlEncode]([LINK_URL_4]). De response body wordt afgekapt wanneer deze groter is dan 1 MB. [SHORTCODE_6] | [INLINE_CODE_37] |
| [INLINE_CODE_38] | Het IPv4-adres van de server waarop de controle werd uitgevoerd. | [INLINE_CODE_39] |
| [INLINE_CODE_40] | Het IPv6-adres van de server waarop de controle werd uitgevoerd. | [INLINE_CODE_41] |
| [INLINE_CODE_42] | Bevat de datum en tijd waarop het SSL-certificaat verloopt voor SSL-controleregelalerts. | [INLINE_CODE_43] |
| [INLINE_CODE_44] | Dezelfde datum en tijd als @alert.timestampUtc, maar in de tijdzone van uw account. Ook geformatteerd als ISO 8601. | [INLINE_CODE_45] |
| [INLINE_CODE_46] | Dezelfde datum en tijd als @alert.timestampUtc, maar in de tijdzone en cultuur van uw account. | [INLINE_CODE_47] |
| [INLINE_CODE_48] | De datum en tijd van de alert, uitgedrukt in UTC-tijd en geformatteerd als ISO 8601. | [INLINE_CODE_49] |
| [INLINE_CODE_50] | De datum en tijd van de alert, uitgedrukt in UTC-tijd en geformatteerd in de cultuur van uw account. | [INLINE_CODE_51] |
| [INLINE_CODE_52] | Het type van dit alertbericht:[HTML_TAG_1][HTML_TAG_2]- Alert: er is een nieuwe fout gedetecteerd.[HTML_TAG_3]- Ok: de oorspronkelijke fout is opgelost.[HTML_TAG_4]- Herinnering: de oorspronkelijke fout duurt nog steeds voort. | [INLINE_CODE_53] \| [INLINE_CODE_54] \| [INLINE_CODE_55] |
| [INLINE_CODE_56] | De unieke ID van de alertdefinitie die is gebruikt om deze alert te genereren. | [INLINE_CODE_57] |
| [INLINE_CODE_58] | De naam van de alertdefinitie die is gebruikt om deze alert te genereren | [INLINE_CODE_59] |
| [INLINE_CODE_60] | [SHORTCODE_7] Een verwijzing naar een [vrij veld]([LINK_URL_5]), dat kan worden gebruikt om aangepaste data voor individuele controleregels op te nemen. [SHORTCODE_8] | [INLINE_CODE_61] |
| [INLINE_CODE_62] | De ID van het escalatieniveau dat is gebruikt om deze alert te genereren. | [INLINE_CODE_63] |
| [INLINE_CODE_64] | Het aangepaste bericht dat is opgegeven in het escalatieniveau | [INLINE_CODE_65] |
| [INLINE_CODE_66] | Unieke ID van het incident waartoe deze alert behoort. Een foutalert en een Ok-alert delen dezelfde incident-key. | [INLINE_CODE_67] |
| [INLINE_CODE_68] | De URL van een deep link die u naar het dashboard van deze controleregel brengt. | [INLINE_CODE_69] |
| [INLINE_CODE_70] | De URL van een deep link die u naar de instellingen van deze controleregel brengt. | [INLINE_CODE_71] |
| [INLINE_CODE_72] | De unieke ID van de controleregel in uw account die deze alert heeft getriggerd. | [INLINE_CODE_73] |
| [INLINE_CODE_74] | De naam van de controleregel in uw account die deze alert heeft getriggerd. | [INLINE_CODE_75] |
| [INLINE_CODE_76] | Alle aangepaste notities die in de controleregelinstellingen zijn ingevuld | [INLINE_CODE_77] |
| [INLINE_CODE_78] | Bevat het type van de controleregel | [INLINE_CODE_79] |
| [INLINE_CODE_80] | De URL of het netwerkadres dat deze controleregel aan het controleren is. | [INLINE_CODE_81] |