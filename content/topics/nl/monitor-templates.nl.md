{
  "hero": {
    "title": "Controleregelsjablonen"
  },
  "title": "Controleregelsjablonen",
  "summary":"Met een controleregelsjabloon kunt u bepaalde instellingen op meerdere controleregels tegelijk toepassen.",
  "url": "/support/kb/synthetic-monitoring/controleregelbeheer/controleregelsjablonen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-templates"
}

Met Uptrends is het nog nooit zo eenvoudig geweest om de uptime of performancestatus van een website, server of webservice te monitoren. Maar wat doet u als u een reeks services wilt monitoren en deze snel wilt opzetten? Dan gebruikt u **Controleregelsjablonen**.

Een controleregelsjabloon is een tool die kan worden gebruikt voor het toevoegen van bepaalde instellingen, zoals *foutcondities*, *controlestations* en *onderhoudsperiodes* aan groepen controleregels. U kunt ze beschouwen als een manier om controleregelconfiguraties te dupliceren, maar dan supersnel.

## Waarom zijn controleregelsjablonen handig?

Als u een reeks controleregels maakt die dezelfde regels volgen voor foutcondities, controlestations of onderhoudsperiodes, kan het handmatig configureren veel moeite en tijd kosten. Door een controleregelsjabloon te gebruiken, kunt u met minimale moeite en tijd specifieke instellingen toevoegen aan controleregels, en verdergaan met waar u het beste in bent.

{{< callout >}} **Opmerking**: U moet een beheerder zijn of het [gebruikersrecht Beheer controleregelsjablonen]({{< ref path="/support/kb/account/users/operators/permissions#manage-monitor-templates" lang="nl" >}}) hebben om sjablonen te kunnen maken, bewerken en toepassen. {{< /callout >}}

## Hoe creëer ik een controleregelsjabloon?

1.  Ga naar {{< AppElement type="menuitem" >}}Accountinstellingen > Controleregelsjablonen{{< /AppElement >}}. 
2.  Klik in de rechter bovenhoek van het scherm op de knop {{< AppElement type="button" >}}Sjabloon toevoegen{{< /AppElement >}}.   
3. Nu kunt u uw sjablooninstellingen aanpassen:
- Voer een naam in voor uw controleregelsjabloon.
- Op het tabblad Instellingen voor controleregels heeft u een optie om [laadtijdlimieten]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}}) in te voeren om een fout te genereren als de respons van de server langzamer is dan deze duur.
Verder kunt u een [user agent]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="nl" >}}) selecteren om het browsertype en het besturingssysteem van de gebruiker te identificeren dat naar de server wordt gestuurd tijdens HTTPS requests. De user agent is standaard ingesteld op *Ongewijzigd laten*.
- Gebruik de selectievakjes op het tabblad [controlestations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="nl" >}}) om de locaties te bepalen van waaruit u wilt monitoren. 
- U kunt ook [Onderhoudsperiodes]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="nl" >}}) toevoegen en de herhaling ervan instellen.

{{< callout >}} **Opmerking**: Als u een controleregelsjabloon toepast, passen we alleen de instellingen toe waarin u wijzigingen heeft aangebracht toen de sjabloon werd gemaakt. Als u bijvoorbeeld een sjabloon wilt gebruiken om alleen een onderhoudsperiode toe te passen, zorg er dan voor dat u alleen die instelling aanpast bij het creëren van de controleregelsjabloon. Hetzelfde geldt voor het toepassen van een bepaalde controlestationselectie of foutconditie. {{< /callout >}}

4.  Als u klaar bent, klikt u op de groene knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

U kunt nu uw opgeslagen controleregelsjablonen toepassen op elke bestaande controleregel, hierbij heeft u twee opties. De eerste optie is om één controleregel bij te werken of bulkupdates uit te voeren voor meerdere controleregels via het menu {{< AppElement type="menuitem" >}}Controleregelsjablonen{{< /AppElement >}}. Met de tweede optie kunt u een sjabloon van uw huidige controleregel rechtstreeks toepassen via het scherm {{< AppElement type="menuitem" >}}controleregel-editor{{< /AppElement >}}. Zie de onderstaande stapsgewijze instructies voor meer informatie over het toepassen van controleregelsjablonen.

## Een controleregelsjabloon toepassen
Om een sjabloon op één controleregel toe te passen of om bulkupdates op meerdere controleregels tegelijk uit te voeren:

1. Ga naar {{< AppElement type="menuitem" >}}Accountinstellingen > Controleregelsjablonen{{< /AppElement >}}. 
2. Zoek de juiste controleregelsjabloon in de lijst en klik op **Toepassen**. 
3. Selecteer de individuele controleregel(s) of controleregelgroep(en) waarop u de sjabloon wilt toepassen.
4. Klik op de knop {{< AppElement type="button" >}} Toepassen {{< /AppElement >}}.

Hiermee worden de opgegeven instellingen toegepast op de geselecteerde controleregel(s)/controleregelgroep(en).

## Een controleregelsjabloon toepassen met het scherm controleregel-editor
Om een sjabloon rechtstreeks vanaf uw huidige controleregel toe te passen:

1. Ga naar {{< AppElement type="menuitem" >}}Monitoring > Controleregels beheren{{< /AppElement >}}.
2. Klik op de controleregelnaam waarop u de sjabloon wilt toepassen.
3. Klik onder aan de pagina controleregel-editor op de knop {{< AppElement type="button" >}} Sjabloon toepassen {{< /AppElement >}}.
4. In het venster Sjabloon toepassen selecteert u in het menu welke controleregelsjabloon u wilt toepassen. Alle beschikbare secties van uw gekozen sjabloon worden weergegeven. U kunt de selectievakjes gebruiken om afzonderlijke secties toe te passen of over te slaan. Uitgeschakelde selectievakjes geven aan dat de sjabloon geen instellingen voor die sectie bevat.

![Een screenshot met een pop-up over hoe je controleregelsjablonen toepast in het venster controleregel-editor](/img/content/scr-apply-monitor-template-monitor-editor-page.min.png)

5. Klik op de knop {{< AppElement type="button" >}} Toepassen {{< /AppElement >}} om de wijzigingen in uw huidige controleregel te bevestigen.
