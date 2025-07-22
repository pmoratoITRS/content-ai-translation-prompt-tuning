{
  "hero": {
    "title": "Fouten wissen"
  },
  "title": "Fouten wissen",
  "summary": "Ontdek hoe u de fouthistorie van onjuiste of ongewenste fouten kunt wissen",
  "url": "/support/kb/alerting/fouten/fouten-wissen",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/clearing-errors"
}

Het is mogelijk individuele fouten of een groep fouten (zowel onbevestigde als bevestigde) te wissen die als onjuist of ongewenst worden beschouwd. Eén fout (of een klein aantal fouten) kan door u worden gewist. Als u heel veel fouten moet wissen, zal Uptrends u daarbij helpen, zie [Grote hoeveelheden fouten wissen]({{< ref path="#bulk-error-clearance" lang="nl" >}}). 

Merk op dat door het wissen van fouten niet automatisch de statistieken die zijn gebaseerd op fouten worden herberekend, zoals statistieken van service level agreements ([SLA's]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="nl" >}})) of [publieke statuspagina’s]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="nl" >}}). Zie [Effect op SLA's en publieke-statuspaginadata]({{< ref path="#effect-sla-psp-data" lang="nl" >}}) over hoe u omgaat met het herberekenen van statistieken afhankelijk van of u zelf fouten heeft gewist of dit bij Support heeft aangevraagd.

{{< callout >}}
**Opmerking**: Helaas is het niet mogelijk om SLA's opnieuw te berekenen voor data ouder dan 90 dagen, aangezien die data na deze periode niet worden bewaard.
{{< /callout >}}

## Individuele fouten corrigeren {id="clear-individual-errors"}

Een fout in uw account corrigeren: 
1. Ga naar het menu {{< AppElement type="menuitem" >}}Monitoring > Controleregel log{{< /AppElement >}}.
2. Klik op de fout die u wilt wissen. De *Details van de controle* gerelateerd aan deze fout verschijnt.
3. Klik onder aan het pop-upvenster op de knop {{< AppElement type="editbutton" >}} Fout corrigeren {{< /AppElement >}}.
4. Bevestig de actie met de knop {{< AppElement type="editbutton" >}} Corrigeren {{< /AppElement >}}. 

De fout wordt gewijzigd in een OK-resultaat, dat direct zichtbaar is in het dashboard *Controleregel log*. 

De betreffende uptimepercentage-data worden ook gewijzigd. Vanwege caching kan het even duren voordat de wijzigingen zichtbaar worden.

## Grote hoeveelheden fouten wissen {id="bulk-error-clearance"}

Soms wilt u fouten over een bepaald tijdsbestek wissen (bijvoorbeeld meerdere dagen downtime). In plaats van elke fout afzonderlijk te wissen, raden wij u aan het volgende te doen:

1. Indien u een venster *Details van de controle* open heeft, klikt u op de knop {{< AppElement type="editbutton" >}} Wis meerdere fouten {{< /AppElement >}} onder aan het pop-upvenster. Het formulier *Verzoek om fouten te wissen* verschijnt. 
2. U kunt ook navigeren naar {{< AppElement type="menuitem" >}} Support {{< /AppElement >}} en klikken op de optie {{< AppElement type="buttonPrimary" >}}  Verzoek om fouten te wissen {{< /AppElement >}}. Het formulier *Verzoek om fouten te wissen* verschijnt. 
3. Vul de verplichte informatie in: de controleregel(s) en de periode. Voeg eventueel optionele informatie toe die relevant is voor uw verzoek, zoals een statuscode. 
4. Klik op de knop {{< AppElement type="buttonPrimary" >}} Verzenden {{< /AppElement >}}.

Wanneer u uw verzoek verzendt, wordt er automatisch een ticket aangemaakt en wordt uw verzoek verwerkt. Dit kan even duren, maar u wordt door het ticketsysteem op de hoogte gesteld zodra het wissen van de fouten en de herberekening van de SLA-data zijn voltooid. 

## Effect op SLA's (service level agreements) en publieke-statuspaginadata {id="effect-sla-psp-data"}

Als u fouten wist, worden bestaande [SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="nl" >}})-data niet automatisch gewijzigd, waaronder [publieke statuspagina]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="nl" >}})-data, wat ook berekende SLA-data zijn. 

Het is echter mogelijk om de data opnieuw te berekenen. Wanneer u [wis meerdere fouten]({{< ref path="#bulk-error-clearance" lang="nl" >}}) heeft aangevraagd bij het Support team, is de herberekening van de data bij het proces inbegrepen. U hoeft dit niet afzonderlijk aan te vragen. 

Dit is anders als u zelf fouten heeft gewist. Neem in dat geval contact op met Support via een [support ticket]({{< ref path="contact" lang="nl" >}}) en geef aan wat u wilt doen. 
