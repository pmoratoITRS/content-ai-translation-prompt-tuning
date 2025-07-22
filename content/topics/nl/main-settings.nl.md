{
  "hero": {
    "title": "Algemene instellingen voor operators"
  },
  "title": "Algemene instellingen voor operators",
  "summary": "Elke operator moet correct worden geconfigureerd met contactinformatie, inloginformatie en gebruikersrechten of tijd- en taalinstellingen.",
  "url": "/support/kb/account/gebruikers/operators/algemene-instellingen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/main-settings"
}

Als u een [operator heeft toegevoegd]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="nl" >}}) moet u een aantal instellingen configureren, te beginnen met instellingen op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} van de operatorpagina. De opties worden in dit artikel beschreven. U moet administratorrechten hebben om operators toe te voegen en te configureren.

## Logininformatie {id="logininfo"}
Logininformatie wordt verstrekt bij het configureren van een operator. Lees meer in ons KB-artikel [Een operator toevoegen of verwijderen]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="nl" >}}).

## Taalinstellingen {id="langsettings"}
De **Taal** wordt geconfigureerd tijdens de account set-up. De taal die in de accountinstellingen is opgegeven wordt weergegeven en standaard gebruikt. Als u de accounttaal wilt overschrijven, selecteert u **Overschrijf taalinstellingen van het account** en kiest u een andere taal in het vervolgkeuzemenu.

## Operatorrol {id="operatorrole"}
De instelling **Operatorrol** kan worden gebruikt om aan te geven welke rol specifieke operators binnen het bedrijf hebben, als interne referentie. Een speciale rol is de *Gebruiker voor meldingsroutering*, die als vlag kan worden gebruikt om aan te geven dat die specifieke operator alleen mag worden gebruikt voor het ontvangen, parseren en verwerken van e-mailalerts. 

## Instellingen voor nieuwsbriefabonnement {id="newslettersub"}
Met de opties voor **Nieuwsbriefabonnement** kunnen operators (en beheerders) configureren welke soorten e-mails moeten worden ontvangen. De opties zijn het ontvangen van *feature-updates*, dit zijn algemene berichten over nieuw uitgebrachte of bijgewerkte functies, en *updates over controlestations*, die updates bevatten over ons [controlestationnetwerk]({{< ref path="/checkpoints" lang="nl" >}}) (nieuwe controlestations toegevoegd, oude verwijderd, wijzigingen in IP-adressen enzovoort). 

Standaard ontvangen operators e-mails met feature-updates, terwijl de controlestationupdates alleen worden verzonden naar [accountbeheerders]({{< ref path="/support/kb/account/users/operators/giving-an-operator-administrator-rights" lang="nl" >}}) en operators die zijn aangemerkt als [technisch contactpersoon]({{< ref path="/support/kb/account/users/operators/permissions#technical-contact" lang="nl" >}}).

## Standaard dashboard {id="defaultdash"}
Het **Standaard dashboard** is geconfigureerd als {{< AppElement type="dropdown" >}} door uw beheerder ingesteld {{< /AppElement >}} tijdens account set-up, maar kan worden gewijzigd door een ander dashboard te kiezen in het menu.

Lees meer over dashboards in ons KB-artikel [Dashboards en publieke statuspagina's]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/" lang="nl" >}}).

## Tijdzone-instellingen {id="timezone"}
Tijdens het configureren van het Uptrends-account (wanneer u voor het eerst inlogt) is de [tijdzone]({{< ref path="support/kb/account/settings/timezones" lang="nl" >}}) ingesteld voor het hele account. Deze instelling is van toepassing op alle operators die worden toegevoegd aan het Uptrends-account. U kunt de tijdzone-instelling vinden in {{< AppElement type="menuitem" >}} Accountinstellingen > Accountinstellingen {{< /AppElement >}}. 


Als u een [Enterprise-account]({{< ref path="/pricing#plans" lang="nl" >}}) heeft kunt u een extra tijdzone invoeren voor individuele operators. Dit is handig voor operators die in een andere tijdzone werken dan de standaardtijdzone in uw Uptrends-account.

Kies in de **Tijdzone-instellingen** de optie *Extra tijdzone* en kies de juiste tijdzone in de lijst. Klik dan op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om deze optie te activeren.

Nu kan de operator deze extra informatie voor tijdstempels zien:

- Binnen alle details van de controleregelchecks worden beide tijdstempels op basis van de standaardtijd en de extra tijdzone weergegeven.
- Als u in het dashboard **Controleregel log**  (ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregel log {{< /AppElement >}}) over het tijdstempel van een log-vermelding hovert, wordt het tijdstempel in de extra tijdzone weergegeven.

## Telefooninstellingen {id="phonesettings"}
Er wordt een mobiel telefoonnummer opgegeven tijdens de operator set-up. Lees meer in ons KB-artikel [Een operator toevoegen of verwijderen]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="nl" >}}).  