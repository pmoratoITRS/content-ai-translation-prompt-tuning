{
  "hero": {
    "title": "Controleregelnotities"
  },
  "title": "Controleregelnotities",
  "summary": "Notities toevoegen en bewerken in uw controleregels en ze gebruiken om de communicatie te vergemakkelijken.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/controleregelnotities",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-notes"
}

 De controleregelnotities van Uptrends kunnen worden gebruikt voor interne communicatie tussen operators. Het is een makkelijke manier om snel zaken met betrekking tot (instellingen van) de controleregel te bespreken. Het dashboard **Controleregelstatus** laat zien welke controleregels een notitie hebben en biedt gemakkelijk toegang om die notitie te lezen zonder het scherm te hoeven verlaten. Hierdoor hebben operators vlot toegang tot interne statusinformatie die door een andere operator is achtergelaten, zoals: 

- Controleregelstatus 
- Frequente fouten en instructies voor het oplossen van de fout  
- Snel zicht op wie eraan werkt, zodat andere teamleden zich op andere zaken kunnen concentreren 

Bijvoorbeeld een _SSL Certificaat_-controleregel. De controleregel waarschuwt van tevoren dat het certificaat verloopt. Vervolgens onderneemt een operator actie om het certificaat te vernieuwen en vermeldt in de notitie dat actie wordt ondernomen. Na verlenging van het certificaat kan de tekst in het veld **Notities** gewist worden.  
 
## Controleregelnotities toevoegen 
Het bewerkingsscherm van elke controleregel bevat een veld **Notities** voor free-form tekst. 
Om toegang te krijgen tot uw controleregelinstellingen:
1. Ga naar het menu {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}. 
2. Klik op {{< AppElement type="menuitem" >}} Controleregels beheren {{< /AppElement >}}.
3. Zoek de naam van de controleregel waarvan u de instellingen wilt openen. Klik op de bijbehorende koppeling in de kolom **Controleregelnaam**. Of filter de resultaten door (een deel van) de naam, het type, de groep of URL van de controleregel in te voeren in het zoekvak en op Enter te drukken. 
4. Het configuratiescherm van de controleregel wordt geopend op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}}. 
![Een notitie invoeren in het free-form tekstveld](/img/content/scr-monitor-settings-notes.min.png)
5. Voer notities in het veld **Notities** in, onder **Metadata**.  
6. Als u notities heeft ingevoerd die u wilt bewaren, vergeet dan niet op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} te klikken. 

## Waar worden notities weergegeven? 
Notities worden weergegeven op het dashboard **Controleregelstatus**. (Ga naar menu {{< AppElement type="menuitem" >}} Monitoring > Statusdetails {{< /AppElement >}}). De tweede dashboardkolom laat zien welke controleregels een notitie hebben. Als dit het geval is, wordt er een donker notitiepictogram weergegeven. Is er geen tekst om weer te geven, dan is het pictogram lichtgrijs. Een operator kan de tekst van de notitie lezen door erover te hoveren.

![Notities in dashboard Controleregelstatus](/img/content/scr-monitor-status-show-notes.min.png)

Notities zijn ook zichtbaar op het quick-info-paneel van een controleregel:

![Notities in quick-info-paneel van statusdashboard](/img/content/scr-monitor-notes-q-inf-pan.min.png)
## Wie heeft toegang tot controleregelnotities? 
Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Accountinstellingen {{< /AppElement >}}. Op het tabblad {{< AppElement type="tab" >}} Instellingen {{< /AppElement >}} onder Toegang tot notities bij controleregels configureert u het recht om notities te bekijken voor operators.
![Toegang tot controleregelnotities](/img/content/scr-monitor-notes-permissions.min.png)
Opmerking: De toegangsinstelling is alleen beschikbaar voor Enterprise-accounts. 