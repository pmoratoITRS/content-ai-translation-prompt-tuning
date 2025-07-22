{
  "hero": {
    "title": "Berichttypes"
  },
  "title": "Berichttypes",
  "summary": "Aangepaste integraties - beschrijving van de verschillende berichttypes",
  "url": "/support/kb/alerting/integraties/aangepaste-integraties/berichttypes",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/message-types" 
}

Er zijn verschillende soorten alertberichten. Uptrends maakt onderscheid tussen **Foutberichten**, **Herinneringen** en **Ok-berichten**. Standaard worden al deze berichttypes gemaakt met dezelfde instellingen. Wanneer u echter een aanpasbare integratie configureert of een bestaande integratie aanpast, kunt u verschillende sets acties maken voor elk afzonderlijk berichttype.

## Foutberichten, Ok-berichten en Herinneringen

Wanneer u in de tab {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}} een berichtdefinitie maakt, gebruikt Uptrends die berichtdefinitie voor alle fouttypes: een Foutalert wanneer de controle de alert voor het eerst genereerde, een Ok-alert wanneer de controle de alert oplost en Herinneringalerts (afhankelijk van uw escalatieniveau-instellingen) daartussen.

De berichtinhoud is vrijwel hetzelfde voor alle alerttypes, behalve voor timestamp-waarden en de variabele {{@ alert.type}}, die het alerttype zelf uitvoert.

Hoewel prima voor veel situaties, is het gebruik van dezelfde berichtinhoud niet voldoende als u verschillende inhoud nodig heeft voor verschillende alerttypes, of als u een nieuw incident in uw systeem moet maken (op basis van een Foutalert) waarvoor een andere URL nodig is om datzelfde incident op te lossen (op basis van een OK-alert).

### Afzonderlijke berichten voor verschillende alerttypes

Om afzonderlijke berichtdefinities voor alerttypes te maken klikt u op de knop Stappen toevoegen onder aan de tab {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}}. De knop Stappen toevoegen creëert een extra berichtdefinitie die u bijvoorbeeld zo kunt configureren dat die alleen van toepassing is op Ok-alerts. Voor elk alerttype kunt u nu de juiste HTTP-methode (GET/POST/PUT/PATCH/DELETE), URL, headers en request body opgeven.

Selecteer de selectievakjes *Foutalert*, *Ok-alert* en *Herinneringalert* boven elke stapdefinitie om de gewenste set-up te maken. U kunt elk alerttype slechts één keer selecteren, maar Ok-alerts en Herinneringalerts zijn optioneel. Wilt u helemaal geen Ok-alerts of Herinneringalerts versturen, selecteer dan deze selectievakjes niet.

### Foutalerts en Ok-alerts horen bij elkaar

Of u nu afzonderlijke berichten gebruikt voor Fout- en Ok-alerts of niet, het is waarschijnlijk handig voor het externe systeem om te weten welke alerts bij elkaar horen. Elk incident begint immers met een Foutalert en eindigt met een Ok-alert. Om het externe systeem te helpen dit te begrijpen, kunt u de variabele {{@ incident.key}} in uw berichten gebruiken. Fout- en Ok-alerts delen dezelfde incident-key, maar elk nieuw incident heeft een unieke key. In sommige systemen wordt de incident-key een deduplicatiesleutel of incident-ID genoemd.
