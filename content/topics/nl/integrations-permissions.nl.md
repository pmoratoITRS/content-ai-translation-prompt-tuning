{
  "hero": {
    "title": "Gebruikersrechten voor integraties"
  },
  "title": "Gebruikersrechten voor integraties",
  "summary": "Beheer operatorrechten voor integraties",
  "url": "/support/kb/alerting/integraties/gebruikersrechten-integraties",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/integrations-permissions"
}

{{< callout >}}Gebruikersrechten voor integraties zijn alleen beschikbaar voor **Enterprise-accounts**.{{< /callout >}}

Integraties worden gebruikt in de escalatieniveaus van alertdefinities om de communicatiekanalen voor alertberichten in te stellen.
Door gebruikersrechten voor integraties toe te kennen aan operators, kunt u bepalen wie de integratie in alertdefinities kan maken, aanpassen of gebruiken.

## Wie kan gebruikersrechten beheren?

Administrators (leden van de operatorgroep Administrators) kunnen altijd integraties maken, gebruiken en aanpassen. Ze kunnen ook alle gebruikersrechten voor integraties instellen en wijzigen.

Bovendien kan een operator met zowel het gebruikersrecht **Integratie maken** (ingesteld voor een operator of operatorgroep) als **Integratie aanpassen** (ingesteld op een integratie) ook de gebruikersrechten beheren van integraties die door hemzelf zijn gemaakt. 
## Types gebruikersrechten

Er zijn twee plaatsen waar gebruikersrechten worden onderhouden: op de operator (groep) of op de integratie zelf.

### Integratie maken

Het gebruikersrecht **Integraties maken** wordt ingesteld voor een operator of operatorgroep. Bekijk het knowledgebase-artikel [Gebruikersrechten]({{< ref path="support/kb/account/users/operators/permissions#create-integration" lang="nl" >}}) over hoe dit werkt.

### Integratie gebruiken

Het gebruikersrecht **Integratie gebruiken** geeft een operator het recht om de integratie te gebruiken in de escalatieniveaus van een alertdefinitie. In de lijst met integraties op de escalatieniveau-tabbladen (van een alertdefinitie), ziet u alle integraties waarvoor u het gebruikersrecht **Integratie gebruiken** heeft.

Dit gebruikersrecht geeft geen toegang tot de integratie zelf. U zult die niet zien in de lijst met integraties ({{< AppElement type="menuitem" >}} Alerting > Integraties {{< /AppElement >}}) waar integraties worden beheerd.

De integratie **E-mail** is beschikbaar voor gebruik door alle leden van de operatorgroep **Iedereen**. Dit is om ervoor te zorgen dat u ten minste één integratie kunt kiezen als u gebruikersrechten voor alertdefinities heeft, maar er nog geen toegang tot integraties aan u is toegekend. De **E-mail**-integratie brengt geen extra Uptrends-kosten met zich mee, terwijl sms-integraties [sms-credits]({{< ref path="support/kb/alerting/sms-credit-usage" lang="nl" >}}) gebruiken. 

Gebruikt u API calls om informatie over integraties te krijgen? Dan retourneert een GET request alle integraties waarvoor u het gebruikersrecht **Integratie gebruiken** heeft. Op deze manier kunt u de `GUID` informatie van de integratie ophalen die nodig is om de integratie toe te voegen aan een alertdefinitie, die ook API's gebruikt. De request retourneert de naam, het type en de `GUID` van de integratie.

### Integratie aanpassen {id="edit-integration"}

Dit gebruikersrecht is krachtiger dan **Integratie gebruiken** omdat het u het recht geeft om de integratie te wijzigen. In feite omvat het gebruikersrecht **Integratie aanpassen** het gebruikersrecht **Integratie gebruiken** – u hoeft niet beide toe te wijzen.

Als u het gebruikersrecht **Integratie aanpassen** heeft voor een integratie, ziet u deze in de lijst met integraties in ({{< AppElement type="menuitem" >}} Alerting > Integraties {{< /AppElement >}}).

Dit gebruikersrecht omvat het recht om de integratie te verwijderen.

## Gebruikersrechten beheren

Om gebruikersrechten in te stellen of te wijzigen:

1. Ga naar {{< AppElement type="menuitem" >}} Alerting > Integraties {{< /AppElement >}}.
2. Klik in de lijst met integraties op de integratie die u wilt aanpassen.
3. Open het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}}.
4. Klik op de knop {{< AppElement type="buttonPrimary" >}} Recht toevoegen {{< /AppElement >}}.
5. Kies in het pop-upvenster de operatorgroep (of operator) en het type gebruikersrecht en klik dan op de knop {{< AppElement type="buttonPrimary" >}} Toevoegen {{< /AppElement >}}.
6. Om een  gebruikersrecht te verwijderen selecteert u {{< AppElement type="deletebutton" >}} Verwijderen {{< /AppElement >}} in de lijst **Gebruikersrechten**.
7. Klik onderaan op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de zojuist aangebrachte wijzigingen op te slaan.