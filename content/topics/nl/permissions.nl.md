{
  "hero": {
    "title": "Gebruikersrechten"
  },
  "title": "Gebruikersrechten",
  "summary": "De mensen in uw team hebben verschillende rollen en verantwoordelijkheden. Hoe verhoudt dat zich tot de operators in de Uptrends-app?",
  "url": "/support/kb/account/gebruikers/operators/gebruikersrechten",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/permissions"
}

{{< callout >}} De beschikbaarheid van types gebruikersrechten hangt af van uw abonnement, dat wil zeggen dat sommige types al dan niet voor u beschikbaar zijn. Alle gebruikersrechten zijn beschikbaar voor **Enterprise-accounts**. {{< /callout >}}


Gebruikers van de Uptrends-app worden binnen de app operators genoemd. Een operator heeft het gebruikersprofiel met contactgegevens, persoonlijke instellingen en meer.
De operators zijn lid van een of meerdere operatorgroepen. Meer informatie over dit onderwerp is te vinden in het artikel [Operators en operatorgroepen]({{< ref path="support/kb/account/users/operators/operator-groups" lang="nl" >}}).

Operators hebben verschillende rollen en verantwoordelijkheden, dus hebben ze verschillende gebruikersrechten nodig binnen de Uptrends-app. Een voorbeeld hiervan is de typische beheerdersrol, waarbij de operator overal toegang toe heeft. Andere operators hebben mogelijk alleen toegang tot bepaalde producten of controleregels nodig. Of u wilt gewoon beperken wie er inzage heeft in informatie of het recht om instellingen te wijzigen.

De Uptrends-app gebruikt twee benaderingen als het gaat om gebruikersrechten: algemene (of systeembrede) gebruikersrechten die zijn gekoppeld aan operatorgroepen (of operators) en gebruikersrechten die zijn gekoppeld aan specifieke items. Om de set-up eenvoudiger te maken, kunnen zowel algemene als itemgebaseerde gebruikersrechten worden ingesteld vanuit het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} van operators of operatorgroepen.

Bovendien kunnen [itemgebaseerde gebruikersrechten]({{< ref path="#item-based-permissions" lang="nl" >}}) rechtstreeks op het item (controleregel, alertdefinitie, enz.) worden ingesteld.

Onafhankelijk van waar u de gebruikersrechten instelt, worden ze weergegeven op de andere, bijbehorende locatie.

## Wie kan gebruikersrechten beheren?
Alleen operators met administratorrechten kunnen gebruikersrechten wijzigen. De operator moet lid zijn van de operatorgroep *Administrators*, waar de *Administratieve rechten* standaard en verplicht zijn. Bij Enterprise-accounts kunnen [Gebruikersrechten voor operators/operatorgroepen ]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="nl" >}}) worden ingesteld om specifieke gebruikersrechten te geven aan operators en operatorgroepen.

## Gebruikersrechten beheren

We raden aan om gebruikersrechten te beheren op het niveau van de operatorgroep. Technisch gezien kunt u ook gebruikersrechten toevoegen aan individuele operators. In de meeste situaties zal het gemakkelijker zijn om de operator toe te voegen aan de operatorgroep die de gedefinieerde gebruikersrechten al heeft, in plaats van alle gebruikersrechten toe te voegen aan de operator.

Het proces voor het verlenen en intrekken van gebruikersrechten is hetzelfde. De stappen voor operatorgroepen worden hieronder beschreven.

Volg deze stappen om een gebruikersrecht te verlenen:

1. Ga naar de [Hub voor gebruikersbeheer]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="nl" >}}) door te navigeren naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators en groepen {{< /AppElement >}} in het menu. Klik dan op {{< AppElement type="buttonPrimary" >}} Alle operatorgroepen bekijken {{< /AppElement >}} om naar het overzicht van operatorgroepen van uw account te gaan.
2. Selecteer de groep waaraan u gebruikersrechten wilt toevoegen.
  De gebruikersrechten bevinden zich op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} op de pagina *Operatorgroep*.
3. Kies de **Algemene gebruikersrechten** die u wilt toekennen of intrekken door de betreffende vakjes te selecteren of te deselecteren. 
![Gebruikersrechten operatorgroep](/img/content/scr_operatorgroup-permissions-091624.min.png)
4. Stel [itemgebaseerde gebruikersrechten]({{< ref path="#item-based-permissions" lang="nl" >}}) in voor controleregels en alertdefinities en meer.
5. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} m de zojuist aangebrachte wijzigingen op te slaan.

## Types gebruikersrechten

Alle types gebruikersrechten zijn beschikbaar op operator- en operatorgroepniveau, tenzij anders vermeld. Sommige gebruikersrechten zijn verplicht, details vindt u in de onderstaande beschrijvingen van gebruikersrechten.
### Standaard operator {id="basic-operator"}

Dit gebruikersrecht wordt standaard aan elke nieuwe operator toegevoegd en is niet zichtbaar in de operatorgroepinstellingen. 

Het gebruikersrecht omvat het recht om in te loggen en controleregels en dashboards te bekijken.

Alleen een administrator binnen een Enterprise-abonnement kan dit gebruikersrecht verlenen of intrekken en het kan worden ingesteld voor individuele operators en voor groepen.
Nadat dit gebruikersrecht is ingetrokken, kan de operator alleen inloggen en naar een [beveiligde statuspagina]({{< ref path="/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages#protected-status-pages" lang="nl" >}}) gaan. Er zijn geen andere acties meer beschikbaar.

### Administratieve rechten

Dit gebruikersrecht is verplicht voor de standaard operatorgroep *Administrators* en kan niet aan een andere operatorgroep of individuele operator worden gegeven.

Als operators administratieve rechten moeten krijgen, voegt u ze toe aan de operatorgroep *Administrators*.

### Alertdefinitie toevoegen {id="create-alert-definition"}

Als een operator (of de operatorgroep) dit gebruikersrecht heeft, kunnen ze nieuwe alertdefinities toevoegen. Merk op dat er ook het gerelateerde gebruikersrecht [Alertdefinitie wijzigen]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="nl" >}}) is, dat in de alertdefinitie zelf wordt ingesteld en niet voor een operator of operatorgroep.

Nadat u een alertdefinitie heeft toegevoegd, krijgt u automatisch het gebruikersrecht **Alertdefinitie wijzigen** voor die definitie. Dit is om ervoor te zorgen dat u wijzigingen kunt aanbrengen in de alertdefinitie voor later onderhoud.

De combinatie van de gebruikersrechten **Alertdefinitie toevoegen** en **Alertdefinitie wijzigen** geeft u ook het recht om de gebruikersrechten van de alertdefinitie te wijzigen. Op deze manier kunt u uw eigen alertdefinitie delen met andere operators.

Administrators hebben standaard het gebruikersrecht **Alertdefinitie toevoegen**.

### Integratie maken {id="create-integration"}

Met dit gebruikersrecht kunt u integraties in het algemeen maken. En zodra u een integratie heeft gemaakt, krijgt u automatisch het gebruikersrecht [Integratie aanpassen]({{< ref path="support/kb/alerting/integrations/integrations-permissions#edit-integration" lang="nl" >}}) ervoor. Zo kunt u de integratie achteraf onderhouden.

Administrators hebben standaard het gebruikersrecht **Integratie maken**.

### Financiële operator {id="financial-operator"}

Een operator met dit gebruikersrecht kan bestellingen plaatsen, facturen bekijken en betalingen doen.   
De operator krijgt bericht over het verlopen van het account, het bereiken van de limiet van SMS credits en ontvangt betalingsherinneringen. 

Het is verplicht om binnen uw Uptrends-account minimaal één operator te hebben met dit type recht. Het is standaard opgenomen in de groepsrechten van de *Administrators*.
### Infra-toegang

Als u een abonnement op Uptrends Infra heeft, kunt u operators toegang geven tot dit product.

Dit gebruikersrecht is verplicht voor de standaard operatorgroep *Administrators*.
### Technisch contactpersoon

Dit gebruikersrecht wordt ingesteld voor de operator met wie contact moet worden opgenomen bij technische problemen. 

Het is verplicht om minimaal één operator te hebben met het gebruikersrecht *Technisch contactpersoon*. Aanvullende technisch contactpersonen kunnen worden toegevoegd en verwijderd, op voorwaarde dat u altijd ten minste één operator met dit recht houdt.

### Persoonlijke locaties beheren {id="manage-private-locations"}

Operators die het gebruikersrechttype *Persoonlijke locaties beheren* hebben, kunnen bestaande [persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations" lang="nl" >}}) maken, verwijderen of beheren binnen het account. Als operators een persoonlijke locatie willen maken, hebben ze toegang nodig tot ten minste één [controleregelgroep]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="nl" >}}) met gebruikersrechttype *Maken en verwijderen van controleregels in groep*. 
Het gebruikersrecht *Persoonlijke locaties beheren* is standaard inbegrepen in de gebruikersrechten van de groep *Administrators*.

### Controleregelsjablonen beheren {id="manage-monitor-templates"}

Operators aan wie het gebruikersrecht *Beheer controleregelsjablonen* is verleend, kunnen [controleregelsjablonen]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="nl" >}}) beheren en toepassen op die controleregels binnen het account waarvoor ze bewerkingsrechten hebben, zonder dat er aanvullende beheerdersrechten nodig zijn.

## Itemgebaseerde gebruikersrechten {id="item-based-permissions"}

De volgende gebruikersrechten worden ingesteld op het item, bijvoorbeeld integratie, controleregel, terwijl algemene gebruikersrechten systeembreed worden ingesteld.

- [Alertdefinities]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="nl" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="nl" >}})
- [Integraties]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="nl" >}})
- [Controleregels]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="nl" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="nl" >}})
- [Operators en operatorgroepen]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="nl" >}})