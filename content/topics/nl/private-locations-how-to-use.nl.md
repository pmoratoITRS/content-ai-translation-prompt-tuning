{
  "hero": {
    "title": "Controlestations voor persoonlijke locaties gebruiken"
  },
  "title": "Controlestations voor persoonlijke locaties gebruiken",
  "summary": "Krijg een overzicht van hoe u monitoring instelt en uw persoonlijke locatie en persoonlijke controlestations na installatie onderhoudt.",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/persoonlijke-locaties-gebruiken",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-how-to-use"
}

Als u een [persoonlijke locatie]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="nl" >}}) toevoegt, worden er standaard twee controlestations gecreëerd. U kunt de controlestations in uw persoonlijke locatie selecteren in de Uptrends-app, en deze opnemen in uw dagelijkse monitoringconfiguratie. U moet het controlestation voor uw nieuwe of bestaande controleregel(s) toewijzen op de configuratiepagina van de controleregel. 

Als u de instellingen van uw individuele controlestation en persoonlijke locatie wilt bewerken, kunt u dit doen op de pagina Persoonlijke locatie. De persoonlijke locatie bevat uw controlestations. Als u een controlestation verwijdert, blijft de locatie behouden. Als u een persoonlijke locatie verwijdert, worden de gehele locatie en zijn controlestations verwijderd.

## Neem eerst een controlestation in gebruik
Een controlestation wordt niet standaard of automatisch gebruikt. Als u het controlestation(s) op uw persoonlijke locaties wilt gebruiken, moet u die eerst toevoegen aan de controlestationselectielijst van uw controleregel. 

Een controlestation voor een controleregel selecteren: 
1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}. 
2. Zoek de naam van de controleregel die het controlestation moet gaan gebruiken en klik op de bijbehorende link in de kolom *Controleregelnaam*. (Houd er rekening mee dat u de nieuwe Multi-step API-controleregels met de naam van het controlestation niet hoeft te selecteren, deze maken deel uit van uw persoonlijke controlestation.)
3. Het controleregel-configuratiescherm wordt geopend met alle tabbladen voor uw controleregelinstellingen. Open het tabblad {{< AppElement type="tab" >}} Controlestations {{< /AppElement >}} en selecteer alle controlestations op uw persoonlijke locatie of een van de persoonlijke controlestations. (U kunt dit controlestation selecteren voor alle nieuwe controleregels die u creëert.)
![screenshot van persoonlijke controlestations in a controleregel](/img/content/scr_private-location-checkpoints-tab-monitor.min.png)
4. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen in de controleregel op te slaan.

## Beheer persoonlijke locaties 

Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}. Hier kunt u de controlestations in uw persoonlijke locatie beheren. 

### De naam van een persoonlijke locatie wijzigen

1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de bewerkenknop (potlood).
3. Voer de nieuwe naam in en druk op enter.

### Een persoonlijke locatie verwijderen

1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de verwijderenknop (prullenbak). 
3. Bevestig het verwijderen van de geselecteerde persoonlijke locatie en de gekoppelde controlestations.
4. Optioneel: Verwijder de (dedicated) VM met de verwijderde controlestations.

### Een controlestation verwijderen

1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} en selecteer *Controlestation verwijderen*. U kunt ook op de naam van het controlestation klikken, dit openen en daar op de grijze knop *Controlestation verwijderen* klikken. 
3. Confirm the removal of the selected checkpoint.

### Een persoonlijk controlestation deactiveren

Als u een persoonlijk controlestation deactiveert, is het niet langer beschikbaar om controles uit te voeren. 

1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} en selecteer *Controlestation deactiveren*. U kunt ook op de naam van het controlestation klikken, dit openen en daar op de grijze knop *Controlestation deactiveren* klikken. 
3. Voeg een omschrijving toe waarom u dit controlestation deactiveert.  
4. Bevestig het verwijderen van het geselecteerde controlestation door te klikken op {{< AppElement type="deletebutton" >}} Deactiveren {{< /AppElement >}} .

### Een persoonlijk controlestation activeren

1. Ga in de Uptrends-app naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="iconTileSettings" >}}  {{< /AppElement >}} en selecteer *Controlestation activeren*. U kunt ook op de naam van het controlestation klikken, dit openen en daar op de grijze knop *Controlestation activeren* klikken. 
3. Bevestig het activeren van het geselecteerde controlestation door te klikken op {{< AppElement type="savebutton" >}} Aanzetten {{< /AppElement >}}.

## Tabbladen persoonlijk controlestation

### Controlestationstatus 
Om uw persoonlijke controlestation te monitoren geeft het tabblad [Controlestationstatus]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="nl" >}}) u inzicht in de belangrijkste statistieken die van invloed zijn op de toestand van het controlestation. Dit omvat informatie over de geïnstalleerde software, instellingen voor [gegevensbescherming]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="nl" >}}) en statistieken over de host. 

### Installatie  

Gebruik de installatiehandleiding om uw persoonlijke controlestations in Docker in te stellen. [Een door de gebruiker beheerd controlestation installeren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="nl" >}}).
### Hoe u dit controlestation gebruikt

Het tabblad {{< AppElement type="tab" >}} Hoe u dit controlestation gebruikt {{< /AppElement >}} biedt een snelle start naar de Controleregel-configuratiepagina voor het instellen van uw controleregels. Het wordt alleen weergegeven als er nog geen controles zijn uitgevoerd vanaf dit controlestation.
 

## Monitoring van uw eigen persoonlijke locatie
### Extra controleregels in uw account

Het is belangrijk om ervoor te zorgen dat er altijd een persoonlijk controlestation in uw account beschikbaar is om controles op uw persoonlijke locatie uit te voeren. Als er geen stations beschikbaar zijn, kan Uptrends geen problemen op uw eigen sites detecteren. Dat wil zeggen: als er geen controles kunnen worden uitgevoerd, zal er geen waarschuwing zijn omdat deze niet zullen mislukken.

Om gewaarschuwd te worden bij eventuele verstoringen van uw persoonlijke controlestationnetwerk worden de onderstaande controleregels gecreëerd. [Creëer een alertdefinitie]({{< ref path="support/kb/alerting/create-alert-definitions" lang="nl" >}}) om ervoor te zorgen dat de juiste mensen worden geïnformeerd wanneer een persoonlijk controlestation uitvalt.

| **Controleregelnaam**                                      | **Type**       |
|-------------------------------------------------------|----------------|
| "checkpoint `<naam van het eerste controlestation>` health"  | Multi-step API |
| "checkpoint `<naam van het tweede controlestation>` health" | Multi-step API |
| "region `<naam van de persoonlijke locatie>` health"      | Multi-step API |

### Nieuwe controleregels toevoegen 

Wanneer u controleregels aan uw Uptrends-account toevoegt, vergeet dan niet om deze in uw firewall te configureren.