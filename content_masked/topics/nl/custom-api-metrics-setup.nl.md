{
  "hero": {
    "title": "Vrije kengetallen instellen"
  },
  "title": "Vrije kengetallen instellen",
  "summary": "Lees meer over Vrije kengetallen en hoe u deze instelt in uw Multi-step API (MSA)-controleregels",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/vrije-kengetallen-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Aangezien API's een cruciale rol spelen in uw dagelijkse bedrijfsvoering, platform- en serviceactiviteiten, is het essentieel om hun gedrag regelmatig te controleren en datavalidatie uit te voeren. In dit artikel wordt uitgelegd hoe u **Vrije kengetallen** kunt gebruiken om uw API-uptime te monitoren, API-responsdata vast te leggen en deze data visueel weer te geven in realtime grafieken of lijsten voor analyse.

**Vrije kengetallen** is een functie die beschikbaar is in [Multi-step API (MSA)-controleregels]([LINK_URL_1]) waarmee u specifieke numerieke data van elke interne of externe API kunt vastleggen.
Van elk vastgelegd datapunt kunt u deze waarden opslaan in een [Vrij kengetal-variabele]([LINK_URL_2]) om visueel weer te geven hoe data in de loop van de tijd verlopen.

## Waarom zou u vrije kengetallen gebruiken?

Stel dat u een API voor uw e-commercesysteem heeft die realtime informatie over uw productcatalogus biedt. Deze omvat prijsgegevens, productvoorraad en andere productinformatie.

U wilt bijvoorbeeld de voorraad per product bijhouden. In plaats van de API telkens handmatig aan te roepen, halen vrije kengetallen deze data automatisch op uit de API-respons en slaan ze elk datapunt op in [Vrije kengetal-variabelen]([LINK_URL_3]):

![Vrij kengetal-productvariabele]([LINK_URL_4])

Telkens wanneer de MSA-controleregel wordt uitgevoerd, volgt deze continu de waarden van de variabelen. Van daaruit kunt u een [Lijst of grafiek van vrije kengetallen]([LINK_URL_5]) maken voor verdere data- of trendanalyse, of om uw bedrijfsrapporten en operationele prestaties te monitoren:

![Vrije kengetal-variabele]([LINK_URL_6])

Er zijn ook verschillende manieren om vrije kengetallen in verschillende contexten te gebruiken:

- Voor DevOps kunt u eenvoudig de status van uw systeem of applicatie monitoren door metingen bij te houden, zoals het aantal geregistreerde fouten, gelijktijdige gebruikers en netwerksnelheid.
- Voor IT-activiteiten kunt u metingen van de datacenteromgeving monitoren, zoals temperatuur, luchtvochtigheid en systeemstatus.
- Voor IT-ondersteuning kunt u het aantal supportoproepen in de wacht, het aantal tickets en de SLA-prestaties volgen.

## Vrije kengetallen instellen

Zodra u [een MSA-controleregel met één of meer stappen heeft ingesteld]([LINK_URL_7]), kunt u op twee manieren **Vrije kengetallen** instellen: [Instellen met behulp van een variabele]([LINK_URL_8]) of [Instellen met behulp van scripting]([LINK_URL_9]).

Gebruik bij het creëren van een nieuw vrij kengetal een naam die gemakkelijk te lezen is en context biedt voor zijn functie. De kengetalnamen en de controleregelnamen verschijnen in de lijst met beschikbare vrije kengetallen zodra ze zijn toegevoegd aan uw aangepaste API-datarapport. U kunt daarom dezelfde vrije kengetal-namen gebruiken om vergelijkbare soorten data aan te duiden die tot verschillende groepen behoren. Een vrij kengetal met de naam [INLINE_CODE_1] kan bijvoorbeeld worden gebruikt in zowel productgerelateerde als klantgerelateerde API's. Hoewel de naam hetzelfde is, komen de data die deze vertegenwoordigt uit verschillende groepen. Uptrends raadt aan om direct de juiste namen te gebruiken. Het later hernoemen van een vrij kengetal zal worden behandeld als het creëren van een nieuw en ander kengetal.

### Instellen met behulp van een variabele

Met deze methode kunt u API-responsdata volgen en opslaan zonder dat u een code of script hoeft te schrijven. U kunt eenvoudig een expressie in een variabele definiëren en een vrij kengetal-naam instellen om die variabele te gebruiken als vrij kengetal.

Laten we **Vrije kengetallen** instellen met de [Carbon API]([LINK_URL_10]) als voorbeeld. Om de Carbon [INLINE_CODE_2]-data bij te houden met behulp van de variabelemethode:

{{[HTML_TAG_1]}}

### Instellen met behulp van scripting

Met deze methode kunt u uw eigen [scripts]([LINK_URL_11]) schrijven, waardoor u volledige controle heeft over hoe u API-responsdata vastlegt en verwerkt.

Zorg ervoor dat u de [Vrije kengetal-snippets]([LINK_URL_12]) gebruikt en een vrij kengetal-naam instelt om die data als een vrij kengetal te gebruiken.

Laten we **Vrije kengetallen** instellen met de [Carbon API]([LINK_URL_13]) als voorbeeld. Om de Carbon [INLINE_CODE_3]-data te volgen gebruikt u de scriptingmethode:

{{[HTML_TAG_2]}}

Voor meer informatie over snippets en scripting, zie [Multi-step API (MSA) aangepaste scripting]([LINK_URL_14]).

[SHORTCODE_1] **Opmerking:** Binnen één MSA-controleregel kunt u maximaal vijf [Vrije kengetal-variabelen]([LINK_URL_15]) opgeven. Als u meer variabelen wilt toevoegen, neem dan contact op met ons [Support team]([LINK_URL_16]) voor hulp. [SHORTCODE_2]

## De Vrije kengetal-data inspecteren

Inspecteer na het instellen uw vrije kengetal-data om te verzekeren dat de controleregel de data correct vastlegt en volgt.

Zo controleert u de vrije kengetal-data die u volgt:

1. Ga naar het menu [SHORTCODE_3] API > API controleregels beheren [SHORTCODE_4].
2. Klik op de link **Ga naar het dashboard** van de controleregel waar u het **Vrije kengetal** heeft gecreëerd**.
3. Klik in de tegel **Controleregel log** ergens op een rij om de pop-up **Details van de controle** te openen.

In de pop-up kunt u de Vrije kengetal-data bekijken die zijn opgehaald uit de controleregelcheck. Merk op dat de waarde [INLINE_CODE_4] 85 is:

![Vrije kengetal-data Carbon intensity]([LINK_URL_17])

Dit geeft u direct toegang tot de individuele Vrije kengetal-waarden zoals deze zijn vastgelegd tijdens de uitvoering van de MSA-controleregel.

### Problemen oplossen

Als u geen vrije kengetal-waarden ziet, ga dan het volgende na:

- Heeft u per ongeluk controleresultaten geopend van een oudere controle die is uitgevoerd voordat het nieuwe vrije kengetal was gedefinieerd?

- Legt uw Vrije kengetal numerieke gehele getallen vast? Als het tekstdata of niet-gehele getallen bevat (zoals [INLINE_CODE_5] of [INLINE_CODE_6]), worden deze niet vastgelegd. Momenteel worden alleen gehele getallen ondersteund. 

- Als er iets mis is gegaan tijdens de uitvoering van de MSA-controleregel, is de variabele die aan uw vrije kengetal is toegewezen mogelijk niet gecreëerd. Controleer op typefouten in de naam of variabelen van het vrije kengetal.

## Aangepaste kengetallen weergeven in dashboards

Als u dieper wilt graven en met de onderliggende data wilt werken om plotselinge pieken in de waarden nauwkeurig te detecteren, kunt u de vrije kengetallen in uw dashboard weergeven met de **Lijst of grafiek van vrije kengetallen**:

![Grafiek van vrije kengetallen]([LINK_URL_18])

Hiermee kunt u de trend van de kengetalvariabele in de tijd bekijken, met de minimale, gemiddelde en maximale waarden. Raadpleeg [Lijst of grafiek van vrije kengetallen]([LINK_URL_19]) voor meer informatie.

U kunt de data van de lijst of grafiek van vrije kengetallen ook exporteren in verschillende gegevensindelingen via de functie [Dashboarddata exporteren]([LINK_URL_20]) feature.
