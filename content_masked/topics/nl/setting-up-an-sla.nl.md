{
  "hero": {
    "title": "Een SLA instellen"
  },
  "title": "Een SLA instellen",
  "summary": "U kunt uw SLA's (service level agreement) monitoren op naleving met Uptrends.",
  "url": "[URL_BASE_TOPICS]dashboards-en-rapportages/sla/een-sla-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## SLA-definities

Door een SLA-definitie te creëren, kunt u dezelfde minimale vereisten configureren die door uw aanbieder zijn bepaald en deze monitoren met het dashboard **SLA-overzicht** dat u vindt in het menu bij [SHORTCODE_3]Dashboards > Synthetics > SLA-overzicht [SHORTCODE_4]. Als de site of service niet voldoet aan de minimale eisen, wordt dit rood weergegeven in het SLA-overzicht. Meer informatie over het dashboard SLA-overzicht vindt u in het artikel [Werken met SLA-data en -rapporten]([LINK_URL_1]).

[SHORTCODE_1]
**Opmerking:** Ziet u in uw rapport SLA-overzicht streepjes en nullen in plaats van data, dan hebben uw tegel-/dashboardinstellingen een conflict in de data veroorzaakt, wat resulteert in ongeldige data. Lees meer over de mogelijke oorzaken in het knowledgebase-artikel [Ontbrekende gegevens SLA-overzicht]([LINK_URL_2]).
[SHORTCODE_2]

### SLA-grenswaardes

De volgende elementen worden de **SLA-grenswaardes** genoemd. Uw SLA-definitie kan alleen uptime of een van de andere SLA-grenswaardes bevatten.

- **Uptime foutpercentage** – SLA-uptimeresultaten lager dan deze grenswaarde voldoen niet aan het SLA-doel: deze veroorzaken een rode fout in de SLA-rapporten. Waarden hoger dan deze grenswaarde (maar lager dan het gewenste uptimepercentage) veroorzaken waarschuwingen in de SLA-rapportage.
- **Gewenst uptimepercentage** – SLA-uptimeresultaten met deze waarde (of hoger) zijn goed, zij voldoen aan het SLA-doel. Waarden tussen deze grenswaarde en het uptime foutpercentage veroorzaken een gele waarschuwing in de SLA-rapporten.
- **Pagina laadtijd** – De maximale laadtijd zoals overeengekomen in de SLA.
- **Operator responstijd** – De hoeveelheid tijd tussen een Uptrends-alert en de tijd dat een operator inlogt bij Uptrends en de alert bevestigt om aan te geven dat er aan de situatie wordt gewerkt. Het dashboard **Huidige alertstatus** ([SHORTCODE_5] Alerting > Huidige alertstatus [SHORTCODE_6]) heeft de functionaliteit voor het bevestigen van een alert.

 Als u meer wilt weten over hoe het uptimepercentage wordt berekend, lees dan het knowledgebase-artikel [Berekening van uptime en downtime]([LINK_URL_3]).

### SLA-tijdschema [ANCHOR_1]

Als uw SLA niet 24/7 actief is, bijvoorbeeld als deze alleen de reguliere kantooruren dekt, of als u gepland onderhoud heeft, kunt u een SLA-tijdschema toevoegen. Met SLA-tijdschema's kunt u de tijden specificeren waarop uw SLA actief is. Downtime, verhoogde laadtijden of fouten buiten deze tijden worden niet meegerekend in de SLA-rapportage. U configureert uw SLA-tijdschema op het tabblad [SHORTCODE_7]Tijdschema[SHORTCODE_8], waar u het tijdschema vindt en de optie om dagen voor gepland onderhoud uit te sluiten.

Houd er rekening mee dat bij het instellen van het SLA-tijdschema de tijd en datum van uw Uptrends-hoofdaccount worden gebruikt. Elke datum en tijd van de lokale computer (waar u het SLA-schema bewerkt) wordt genegeerd. Dit vereenvoudigt de zaken wanneer u werkt met operators in verschillende tijdzones, aangezien de SLA-tijdschema's alleen gebaseerd zijn op de tijd/datum van het Uptrends-account.

- **Tijdschema** – Voor elk uur van elke dag van de week kunt u aangeven of deze SLA actief moet zijn of niet. 

- **Uitsluitingsperiodes** – Als u niet-routinematig geplande downtime heeft, kunt u tijd uitsluiten op basis van specifieke kalenderdagen en tijden.

## Een SLA-definitie instellen

Een SLA definiëren:

1. Ga naar  [SHORTCODE_9] Accountinstellingen > SLA-definities [SHORTCODE_10].
2. Klik rechtsboven op de knop [SHORTCODE_11]SLA-definitie toevoegen [SHORTCODE_12].
3. Geef uw definitie een beschrijvende naam.
4. Stel het uptime-foutpercentage in in het geelomlijnde vak in het veld **Uptime**. Uptimeresultaten onder deze waarde worden rood gemarkeerd in de rapporten SLA-overzicht.
5. Stel het groenomlijnde vak in het veld **Uptime** in op het percentage waar de uptime een punt van zorg wordt voor het voldoen aan SLA-compliance. Uptimeresultaten tussen dit percentage en het uptime-foutpercentage worden geel gemarkeerd in de rapporten SLA-overzicht.
6. (Optioneel) Indien uw SLA dit vereist past u de **Pagina laadtijd** en/of **Operator responstijd** aan.
7. (Optioneel) Als uw SLA niet altijd actief is, stelt u een tijdschema in. In het rooster op het tabblad [SHORTCODE_13]Tijdschema[SHORTCODE_14] geven de blauwe vierkanten aan dat de SLA op die tijd actief is, terwijl witte vierkanten een inactief tijdslot aangeven. Klik op een vierkant om te schakelen tussen actief en inactief. Als u hele dagen of hetzelfde uur van elke dag wilt uitschakelen, klikt u op de kolom- of rijkoppen in plaats van op afzonderlijke vierkanten.
8. (Optioneel) Voeg voor geplande downtime (buiten het tijdschema) uitsluitingsdagen toe op het tabblad [SHORTCODE_15]Tijdschema[SHORTCODE_16]:

   1. Klik op de knop [SHORTCODE_17]Nieuwe uitsluitingsperiode toevoegen[SHORTCODE_18].
   2. Geef de uitsluitingsperiode een beschrijvende naam.
   3. Selecteer de begin- en einddatum en -tijden in de velden **Van** en **Tot**.
   4. Klik op [SHORTCODE_19]Instellen[SHORTCODE_20].

9. Klik linksonder op de knop [SHORTCODE_21]Opslaan[SHORTCODE_22].
