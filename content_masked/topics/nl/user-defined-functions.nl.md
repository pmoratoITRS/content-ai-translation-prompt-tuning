{
  "hero": {
    "title": "Door de gebruiker gedefinieerde functies"
  },
  "title": "Door de gebruiker gedefinieerde functies",
  "summary": "Een overzicht van beschikbare gebruiker-gedefinieerde functies en hoe u deze kunt gebruiken",
  "url": "[FRONTMATTER_URL]",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met Uptrends' [Multi-Step API monitoring]([LINK_URL_1]) kunt u meerdere opeenvolgende HTTP-requests op uw API uitvoeren, waarbij inkomende data worden geparseerd, opgeslagen in variabelen of gecontroleerd op de aanwezigheid van specifieke inhoud. In bepaalde gevallen moeten de waarden van de inkomende data echter worden getransformeerd of gemapt om deze gemakkelijker te begrijpen. Voorbeelden hiervan zijn de XML- en JSON-coderingsfuncties en -decoderingsfuncties die worden beschreven in onze [handleiding voor berichtopmaak bij aanpasbare integraties]([LINK_URL_2]). Naast deze voorgedefinieerde functies kunt u in Uptrends **Door de gebruiker gedefinieerde functies** instellen. Deze functies kunnen worden gebruikt voor het omzetten van [waarden van variabelen]([LINK_URL_3]) (verkregen in een vorige stap, of van een [systeemvariabele die door Uptrends is geleverd]([LINK_URL_4])) naar een nieuwe waarde.

## Beschikbare types van gebruiker-gedefinieerde functies

We bieden de volgende types gebruiker-gedefinieerde functies:

- **Regular Expression:** met dit functietype kunt u een regular expression (RegEx) toepassen op uw eerder gemaakte variabelen. Dit is handig voor het extraheren van specifieke secties van de response data (zoals het extraheren van een authenticatiecode uit een *Location* redirect-header).
- **Mapping:** met het functietype mapping kunt u automatisch bepaalde waarden in de response vervangen door specifieke andere waarden. Als het ene eindpunt bijvoorbeeld de termen *error* of *ok* gebruikt (zoals Uptrends' [eigen API]([LINK_URL_5])) terwijl het volgende eindpunt waarmee u zult interacteren de termen *incident* of *healthy* verwacht, kunt u een mappingfunctie gebruiken om deze waarden automatisch aan te passen naar de juiste equivalenten.
- **Hash**: Hashing-functies zijn eenrichtingsalgoritmen, die een bericht van elke lengte nemen en dit omzetten in een waarde met een vaste lengte. Elke invoer moet altijd hetzelfde resultaat retourneren, waardoor hashing-functies nuttig zijn bij het veilig vergelijken van gevoelige gegevens zoals wachtwoorden, autorisatietokens of digitale handtekeningen, zonder dat ze daadwerkelijk hoeven te worden uitgewisseld. Meer informatie over het gebruik van hashing-functies in Multi-step API-controleregels kunt u lezen in ons artikel over [hashing en codering]([LINK_URL_6]).

## Gebruiker-gedefinieerde functies maken

U kunt een gebruiker-gedefinieerde integratie instellen op het tabblad [SHORTCODE_3]Stappen[SHORTCODE_4] van uw Multi-Step API-controleregels of in het tabblad [SHORTCODE_5]Aanpassingen[SHORTCODE_6] van uw (aangepaste) integraties.

[SHORTCODE_1]
**Opmerking:** Een door de gebruiker gedefinieerde functie is specifiek voor de Multi-Step API-controleregel of aangepaste integratie waarvoor u deze instelt en wordt niet overgedragen naar andere controleregels of integraties.
[SHORTCODE_2]

1.  In het tabblad [SHORTCODE_7]Stappen[SHORTCODE_8] van een van uw Multi-Step API-controleregels of op het tabblad [SHORTCODE_9]Aanpassingen[SHORTCODE_10] van uw (aanpasbare) integraties vindt u de sectie **Door de gebruiker gedefinieerde functies** onder aan de pagina.

2.  Klik op de knop [SHORTCODE_11]Functie toevoegen[SHORTCODE_12] om te beginnen met het definiëren van een nieuwe functie.

3.  Selecteer het juiste functietype: **Mapping**, **Regular expression** of **Hash**, en geef de functie een toepasselijke naam - we raden iets eenvoudigs en zonder spaties aan, omdat u er later naar moet verwijzen.

4.  Vul aanvullende vereiste informatie in:
  - Voeg in het geval van een mappingfunctie de individuele mappings toe die u nodig heeft. De mappingfunctie vertaalt de "Van"-waarden naar de overeenkomstige "Naar"-waarden.
  - Geef voor een regular expression-functie de RegEx op zoals vereist. De Regex wordt vergeleken met de invoertekst en kan worden gebruikt om een specifiek deel van die invoer te extraheren.
  - Voor een hashing-functie die een van de HMAC-algoritmen gebruikt, vult u de waarde van de geheime sleutel in.

U kunt indien nodig extra functies toevoegen door deze stappen te herhalen.

![Voorbeeld gebruiker-gedefinieerde functie]([LINK_URL_7])

## Uw functies gebruiken [ANCHOR_1]

Om uw nieuw gedefinieerde **Door de gebruiker gedefinieerde functie(s)** te gebruiken moet u de variabele(n) waarop de functie moet werken in de functieverwijzing verpakken, zoals [INLINE_CODE_1]. Laten we als voorbeeld eens kijken naar een mappingfunctie die als doel heeft inkomende response data te vertalen van 'Error' naar 'Incident', van 'Warning' naar 'Unhealthy' en van 'Ok' naar 'Healthy', zodat het eindpunt dat in de volgende stap wordt aangeroepen de termen krijgt toegezonden die het begrijpt. In dit voorbeeld:

-   Er is een gebruiker-gedefinieerde functie gemaakt, zoals te zien is in de afbeelding hierboven, genaamd [INLINE_CODE_2].
-   Het eindpunt stuurt een JSON-response die een 'Status'-veld bevat met de waarde 'Error', 'Warning' of 'Ok'.
-   In de volgende stap gaan we die statusdata doorsturen naar een andere API. Deze nieuwe API begrijpt de gebruikte termen echter niet en vereist in plaats daarvan de waarden 'Incident', 'Unhealthy' of 'Healthy'.

Om de functie [INLINE_CODE_3] te gebruiken om de statuswaarde automatisch naar de juiste termen te vertalen volgt u deze stappen:

1.  Extraheer de waarde van het veld 'Status' uit de response data, zoals u dat normaal zou doen (zie onze [handleiding voor het instellen van variabelen bij Multi-Step monitoring]([LINK_URL_8])). n dit voorbeeld heet de resulterende variabele statusRaw. Zoals beschreven, zal deze variabele 'Error'/'Warning'/'Ok' bevatten.
2.  Om de gebruiker-gedefinieerde functie toe te passen, klikt u eerst op de knop [SHORTCODE_13]Variabele toevoegen[SHORTCODE_14].
3.  Stel de variabelebron (de vervolgkeuzelijst aan de linkerkant) in op [SHORTCODE_15]Functie uitvoeren[SHORTCODE_16].
4.  Voor de **functie-expressie** verpakt u de variabeleverwijzing in de functie zoals hierboven beschreven: [SHORTCODE_17]{{errorMapping({{statusRaw}})}}[SHORTCODE_18] 
5.  De resulterende waarde is 'Incident', 'Unhealthy' of 'Healthy', afhankelijk van wat de waarde van de variabele statusRaw was. Geef in het tekstveld **Naam van de variabele** een naam op voor de uitvoerwaarde.

![Een gebruiker-gedefinieerde functie gebruiken]([LINK_URL_9])

Nu hebben we een nieuwe variabele gecreëerd, *status*, waarvan de waarde 'Incident', 'Unhealthy' of 'Healthy' is. In volgende stappen kunnen we op de reguliere manier naar deze variabele verwijzen (bijvoorbeeld door de notatie [INLINE_CODE_4] te gebruiken. In dit voorbeeld hebben we een **Mapping**-functie gebruikt, maar de stappen voor een **RegEx**-functie zijn identiek.
