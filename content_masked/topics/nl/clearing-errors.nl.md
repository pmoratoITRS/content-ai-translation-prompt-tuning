{
  "hero": {
    "title": "Fouten wissen"
  },
  "title": "Fouten wissen",
  "summary": "Ontdek hoe u de fouthistorie van onjuiste of ongewenste fouten kunt wissen",
  "url": "[URL_BASE_TOPICS]alerting/fouten/fouten-wissen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het is mogelijk individuele fouten of een groep fouten (zowel onbevestigde als bevestigde) te wissen die als onjuist of ongewenst worden beschouwd. Eén fout (of een klein aantal fouten) kan door u worden gewist. Als u heel veel fouten moet wissen, zal Uptrends u daarbij helpen, zie [Grote hoeveelheden fouten wissen]([LINK_URL_1]). 

Merk op dat door het wissen van fouten niet automatisch de statistieken die zijn gebaseerd op fouten worden herberekend, zoals statistieken van service level agreements ([SLA's]([LINK_URL_2])) of [publieke statuspagina’s]([LINK_URL_3]). Zie [Effect op SLA's en publieke-statuspaginadata]([LINK_URL_4]) over hoe u omgaat met het herberekenen van statistieken afhankelijk van of u zelf fouten heeft gewist of dit bij Support heeft aangevraagd.

[SHORTCODE_1]
**Opmerking**: Helaas is het niet mogelijk om SLA's opnieuw te berekenen voor data ouder dan 90 dagen, aangezien die data na deze periode niet worden bewaard.
[SHORTCODE_2]

## Individuele fouten corrigeren [ANCHOR_1]

Een fout in uw account corrigeren: 
1. Ga naar het menu [SHORTCODE_3]Monitoring > Controleregel log[SHORTCODE_4].
2. Klik op de fout die u wilt wissen. De *Details van de controle* gerelateerd aan deze fout verschijnt.
3. Klik onder aan het pop-upvenster op de knop [SHORTCODE_5] Fout corrigeren [SHORTCODE_6].
4. Bevestig de actie met de knop [SHORTCODE_7] Corrigeren [SHORTCODE_8]. 

De fout wordt gewijzigd in een OK-resultaat, dat direct zichtbaar is in het dashboard *Controleregel log*. 

De betreffende uptimepercentage-data worden ook gewijzigd. Vanwege caching kan het even duren voordat de wijzigingen zichtbaar worden.

## Grote hoeveelheden fouten wissen [ANCHOR_2]

Soms wilt u fouten over een bepaald tijdsbestek wissen (bijvoorbeeld meerdere dagen downtime). In plaats van elke fout afzonderlijk te wissen, raden wij u aan het volgende te doen:

1. Indien u een venster *Details van de controle* open heeft, klikt u op de knop [SHORTCODE_9] Wis meerdere fouten [SHORTCODE_10] onder aan het pop-upvenster. Het formulier *Verzoek om fouten te wissen* verschijnt. 
2. U kunt ook navigeren naar [SHORTCODE_11] Support [SHORTCODE_12] en klikken op de optie [SHORTCODE_13]  Verzoek om fouten te wissen [SHORTCODE_14]. Het formulier *Verzoek om fouten te wissen* verschijnt. 
3. Vul de verplichte informatie in: de controleregel(s) en de periode. Voeg eventueel optionele informatie toe die relevant is voor uw verzoek, zoals een statuscode. 
4. Klik op de knop [SHORTCODE_15] Verzenden [SHORTCODE_16].

Wanneer u uw verzoek verzendt, wordt er automatisch een ticket aangemaakt en wordt uw verzoek verwerkt. Dit kan even duren, maar u wordt door het ticketsysteem op de hoogte gesteld zodra het wissen van de fouten en de herberekening van de SLA-data zijn voltooid. 

## Effect op SLA's (service level agreements) en publieke-statuspaginadata [ANCHOR_3]

Als u fouten wist, worden bestaande [SLA]([LINK_URL_5])-data niet automatisch gewijzigd, waaronder [publieke statuspagina]([LINK_URL_6])-data, wat ook berekende SLA-data zijn. 

Het is echter mogelijk om de data opnieuw te berekenen. Wanneer u [wis meerdere fouten]([LINK_URL_7]) heeft aangevraagd bij het Support team, is de herberekening van de data bij het proces inbegrepen. U hoeft dit niet afzonderlijk aan te vragen. 

Dit is anders als u zelf fouten heeft gewist. Neem in dat geval contact op met Support via een [support ticket]([LINK_URL_8]) en geef aan wat u wilt doen. 
