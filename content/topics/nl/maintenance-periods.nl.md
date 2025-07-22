{
  "hero": {
    "title": "Onderhoudsperiodes"
  },
  "title": "Onderhoudsperiodes",
  "summary": "Door onderhoudsperiodes in te stellen, kunt u uw alerts of uw controleregels tijdelijk uitschakelen om te voorkomen dat u foutmeldingen ontvangt.",
  "url": "/support/kb/synthetic-monitoring/controleregelbeheer/onderhoudsperiodes",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/maintenance-periods",
  "tableofcontents": true
}

U wilt waarschijnlijk niet worden gewaarschuwd wanneer uw servers, websites of webservices down zijn door gepland onderhoud. Stel dat u een vaste tijd heeft waarin uw team routineonderhoud uitvoert aan de website, webservers of webservice van uw bedrijf. Gedurende die tijd kunnen de beschikbaarheid en performance worden beïnvloed en kunnen uw controleregels alerts triggeren.

## Onderhoudsperiodes

Door een onderhoudsperiode voor uw controleregels in te stellen, kunt u de specifieke datums en tijden van tevoren configureren en beslissen of u uw alerts of de controleregels tijdelijk wilt uitschakelen om te voorkomen dat u foutmeldingen ontvangt:

![Monitor Onderhoudsperiodes](/img/content/gif-monitor-maintenance-periods.gif)


Bij het plannen van een onderhoudsperiode kunt u de herhaling kiezen die u nodig heeft. Periodes kunnen worden geconfigureerd om eenmalig plaats te vinden, of met een dagelijks, wekelijks of maandelijks interval. Of, als u heeft gepland dat uw servers op de laatste dag van elke maand offline zijn, kunt u het aantal alerts beheren dat u op deze datum zult ontvangen. Zie [herhaling op de laatste dag van de maand]({{< ref path="#lastday" lang="nl" >}}) voor meer informatie.

Houd er rekening mee dat bij het instellen van de onderhoudsperiode de tijd en datum van uw Uptrends-hoofdaccount worden gebruikt. Elke datum en tijd van de lokale computer (waar u de onderhoudsperiode bewerkt) wordt genegeerd. Dit vereenvoudigt de zaken wanneer u met operators in verschillende tijdzones werkt, aangezien de onderhoudsperiodes alleen gebaseerd zijn op de tijd/datum van het Uptrends-account.

### Onderhoudsperiode creëren

U creëert onderhoudsperiodes per controleregel. Om uw onderhoudsschema te plannen doet u het volgende:

1.  Ga naar {{< AppElement type="menuitem" >}}Monitoring > Controleregels beheren{{< /AppElement >}}
2.  Klik op de controleregel waarvoor onderhoud is gepland om de controleregelinstellingen te selecteren en te openen.
3.  Klik op het tabblad {{< AppElement type="tab" >}}Onderhoudsperiodes{{< /AppElement >}}
4.  Klik op de knop {{< AppElement type="button" >}}Nieuwe onderhoudsperiode toevoegen{{< /AppElement >}}.

![Een onderhoudsperiode instellen](/img/content/scr-Maintenance-period-setup.min.png)

5.  Voeg desgewenst een omschrijving toe voor uw onderhoudsperiode.
6.  Stel het type **Herhaling** in (*eenmalig, dagelijks, wekelijks, maandelijks*).
7.  Stel de datums en tijden in bij **Van** en **Tot**. Deze opties veranderen op basis van uw keuze bij **Herhaling** in de vorige stap.
8.  Kies in de lijst **Onderhoudstype** of u alleen de notificaties of de controleregel helemaal wilt uitzetten.
9.  Klik op de knop {{< AppElement type="button" >}}Instellen{{< /AppElement >}}.
10.  Klik op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} linksonder om de zojuist aangebrachte wijzigingen in de controleregelinstellingen op te slaan.

### Alerts uitschakelen of de controleregel helemaal uitschakelen

In het instellingenvenster **Onderhoudsperiode toevoegen** kunt u een **Onderhoudstype** kiezen: **Zet notificaties uit** of **Zet monitoring helemaal uit**. 

- Als u ervoor kiest om alle notificaties uit te schakelen, dan gaat de monitoring door en worden optredende fouten nog steeds weergegeven in de gebeurtenis log, maar worden er geen alerts verstuurd. 
- Als u ervoor kiest om de monitoring helemaal uit te schakelen, vindt er geen monitoring plaats en worden er dus geen fouten gelogd en worden er geen alerts gegenereerd.  

### Herhaling op de laatste dag van de maand  {id="lastday"}

Om een onderhoudsschema in te stellen dat op de laatste dag van elke maand wordt herhaald doet u het volgende: 
![Een onderhoudsperiode instellen voor de laatste dag van de maand](/img/content/scr-maintenance-last-day-month.min.png)
1. Creëer een nieuwe onderhoudsperiode zoals hierboven is beschreven. 
2. Selecteer Maandelijks in het keuzemenu **Herhaling**.  
3. Selecteer 31 in het vervolgkeuzemenu **Op dag** en klik op {{< AppElement type="button" >}}Instellen{{< /AppElement >}}  
4. Klik op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om de zojuist aangebrachte wijzigingen in de controleregelinstellingen op te slaan.

{{< callout >}} **Opmerking**: Zelfs als een maand minder dan 31 dagen bevat, zal dit schema op de laatste dag van elke maand in werking treden.   {{< /callout >}}

#### Efficiënt onderhoudsroutines configureren met controleregelsjablonen

Stel dat u onderhoud voor meerdere controleregels tegelijk wilt plannen, dan kunt u een [Controleregelsjabloon]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="nl" >}}) gebruiken. 

## Overzicht onderhoudsperiodes

Als u de onderhoudsperiodes wilt bekijken die u of een collega eerder heeft gemaakt, ga dan naar *Accountinstellingen > Onderhoudsperiodes* of klik op **Alle gelijkende periodes selecteren** in het tabblad {{< AppElement type="tab" >}} Onderhoudsperiodes {{< /AppElement >}} van de controleregel. 

In de overzichtslijst **Onderhoudsperiodes** staan alle onderhoudsperiodes in uw account, zodat u ze kunt bekijken, ongewenste periodes kunt verwijderen en ze kunt opruimen. Standaard toont het een lijst met onderhoudsperiodes voor al uw controleregels. U kunt het controleregelfilter {{< AppElement type="editbutton" >}} Alle controleregels {{< /AppElement >}} gebruiken om uw selectie specifieker te maken.

![Overzicht onderhoudsperiodes](/img/content/scr-maintenance-period-filter.min.png)

Onderhoudsperiodes kunnen eenvoudig worden gefilterd op type met behulp van het dropdownmenu, met opties zoals **Alle periodes**, **Eenmalige periodes** of **Herhalende periodes**. U kunt ze ook filteren op omschrijving met behulp van de zoekbalk voor eenvoudigere toegang. Daarnaast kunt u andere [tegelinstellingen]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/tile-filtering#tile-filtering" lang="nl" >}}) bekijken door te klikken op de knop {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} in de rechter bovenhoek.

{{< callout >}} **Opmerking**: Beheerders en operators met [het gebruikersrecht Instellingen bewerken]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#permission-types" lang="nl" >}}) voor ten minste één controleregel hebben toegang tot de overzichtspagina **Onderhoudsperiodes**. Deze operators kunnen onderhoudsperiodes bekijken, [Opruimen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods#clean-up-your-past-maintenance-periods" lang="nl" >}}) of [Alles verwijderen]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods#delete-all-maintenance-periods" lang="nl" >}}) voor de controleregels waarvoor ze **Instellingen bewerken**-rechten hebben. {{< /callout >}}

### Opruimen van voorbije onderhoudsperiodes

1. Selecteer *eenmalige periodes* of *herhalende periodes* door te klikken op de instellingenknop {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} in de rechter bovenhoek en klik op {{< AppElement type="button" >}} Instellen {{< /AppElement >}}.
![Kies periodes om weer te geven](/img/content/scr-maintenance-choose-periods.min.png)
2. Klik op de knop {{< AppElement type="editbutton" >}}Opruimen{{< /AppElement >}}.
3. Het dialoogvenster **Opruimen** toont het aantal periodes dat in het verleden ligt. 
4. Klik op {{< AppElement type="button" >}}Ok{{< /AppElement >}} om alle geselecteerde voorbije gebeurtenissen te verwijderen.

### Alle onderhoudsperiodes verwijderen

Verwijder alle onderhoudsperiodes die momenteel worden vermeld:

1. Selecteer *eenmalige periodes* of *herhalende periodes* door te klikken op de instellingenknop {{< AppElement type="editbutton" >}} ... {{< /AppElement >}} in de rechter bovenhoek en klik op {{< AppElement type="button" >}} Instellen {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="editbutton" >}}Alle verwijderen{{< /AppElement >}}.
3. In het dialoogvenster **Alle verwijderen** wordt het aantal periodes weergegeven dat is geselecteerd en zal worden verwijderd (alle periodes zijn geselecteerd en zullen worden verwijderd).
4. Klik op {{< AppElement type="button" >}}Ok{{< /AppElement >}} om alle onderhoudsperiodes te verwijderen.
