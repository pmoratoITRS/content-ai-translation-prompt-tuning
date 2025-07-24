{
  "hero": {
    "title": "Gebruikersrechten"
  },
  "title": "Gebruikersrechten",
  "summary": "De mensen in uw team hebben verschillende rollen en verantwoordelijkheden. Hoe verhoudt dat zich tot de operators in de Uptrends-app?",
  "url": "[URL_BASE_TOPICS]account/gebruikers/operators/gebruikersrechten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1] De beschikbaarheid van types gebruikersrechten hangt af van uw abonnement, dat wil zeggen dat sommige types al dan niet voor u beschikbaar zijn. Alle gebruikersrechten zijn beschikbaar voor **Enterprise-accounts**. [SHORTCODE_2]


Gebruikers van de Uptrends-app worden binnen de app operators genoemd. Een operator heeft het gebruikersprofiel met contactgegevens, persoonlijke instellingen en meer.
De operators zijn lid van een of meerdere operatorgroepen. Meer informatie over dit onderwerp is te vinden in het artikel [Operators en operatorgroepen]([LINK_URL_1]).

Operators hebben verschillende rollen en verantwoordelijkheden, dus hebben ze verschillende gebruikersrechten nodig binnen de Uptrends-app. Een voorbeeld hiervan is de typische beheerdersrol, waarbij de operator overal toegang toe heeft. Andere operators hebben mogelijk alleen toegang tot bepaalde producten of controleregels nodig. Of u wilt gewoon beperken wie er inzage heeft in informatie of het recht om instellingen te wijzigen.

De Uptrends-app gebruikt twee benaderingen als het gaat om gebruikersrechten: algemene (of systeembrede) gebruikersrechten die zijn gekoppeld aan operatorgroepen (of operators) en gebruikersrechten die zijn gekoppeld aan specifieke items. Om de set-up eenvoudiger te maken, kunnen zowel algemene als itemgebaseerde gebruikersrechten worden ingesteld vanuit het tabblad [SHORTCODE_3] Gebruikersrechten [SHORTCODE_4] van operators of operatorgroepen.

Bovendien kunnen [itemgebaseerde gebruikersrechten]([LINK_URL_2]) rechtstreeks op het item (controleregel, alertdefinitie, enz.) worden ingesteld.

Onafhankelijk van waar u de gebruikersrechten instelt, worden ze weergegeven op de andere, bijbehorende locatie.

## Wie kan gebruikersrechten beheren?
Alleen operators met administratorrechten kunnen gebruikersrechten wijzigen. De operator moet lid zijn van de operatorgroep *Administrators*, waar de *Administratieve rechten* standaard en verplicht zijn. Bij Enterprise-accounts kunnen [Gebruikersrechten voor operators/operatorgroepen ]([LINK_URL_3]) worden ingesteld om specifieke gebruikersrechten te geven aan operators en operatorgroepen.

## Gebruikersrechten beheren

We raden aan om gebruikersrechten te beheren op het niveau van de operatorgroep. Technisch gezien kunt u ook gebruikersrechten toevoegen aan individuele operators. In de meeste situaties zal het gemakkelijker zijn om de operator toe te voegen aan de operatorgroep die de gedefinieerde gebruikersrechten al heeft, in plaats van alle gebruikersrechten toe te voegen aan de operator.

Het proces voor het verlenen en intrekken van gebruikersrechten is hetzelfde. De stappen voor operatorgroepen worden hieronder beschreven.

Volg deze stappen om een gebruikersrecht te verlenen:

1. Ga naar de [Hub voor gebruikersbeheer]([LINK_URL_4]) door te navigeren naar [SHORTCODE_5] Accountinstellingen > Operators en groepen [SHORTCODE_6] in het menu. Klik dan op [SHORTCODE_7] Alle operatorgroepen bekijken [SHORTCODE_8] om naar het overzicht van operatorgroepen van uw account te gaan.
2. Selecteer de groep waaraan u gebruikersrechten wilt toevoegen.
  De gebruikersrechten bevinden zich op het tabblad [SHORTCODE_9] Gebruikersrechten [SHORTCODE_10] op de pagina *Operatorgroep*.
3. Kies de **Algemene gebruikersrechten** die u wilt toekennen of intrekken door de betreffende vakjes te selecteren of te deselecteren. 
![Gebruikersrechten operatorgroep]([LINK_URL_5])
4. Stel [itemgebaseerde gebruikersrechten]([LINK_URL_6]) in voor controleregels en alertdefinities en meer.
5. Klik op [SHORTCODE_11] Opslaan [SHORTCODE_12] m de zojuist aangebrachte wijzigingen op te slaan.

## Types gebruikersrechten

Alle types gebruikersrechten zijn beschikbaar op operator- en operatorgroepniveau, tenzij anders vermeld. Sommige gebruikersrechten zijn verplicht, details vindt u in de onderstaande beschrijvingen van gebruikersrechten.
### Standaard operator [ANCHOR_1]

Dit gebruikersrecht wordt standaard aan elke nieuwe operator toegevoegd en is niet zichtbaar in de operatorgroepinstellingen. 

Het gebruikersrecht omvat het recht om in te loggen en controleregels en dashboards te bekijken.

Alleen een administrator binnen een Enterprise-abonnement kan dit gebruikersrecht verlenen of intrekken en het kan worden ingesteld voor individuele operators en voor groepen.
Nadat dit gebruikersrecht is ingetrokken, kan de operator alleen inloggen en naar een [beveiligde statuspagina]([LINK_URL_7]) gaan. Er zijn geen andere acties meer beschikbaar.

### Administratieve rechten

Dit gebruikersrecht is verplicht voor de standaard operatorgroep *Administrators* en kan niet aan een andere operatorgroep of individuele operator worden gegeven.

Als operators administratieve rechten moeten krijgen, voegt u ze toe aan de operatorgroep *Administrators*.

### Alertdefinitie toevoegen [ANCHOR_2]

Als een operator (of de operatorgroep) dit gebruikersrecht heeft, kunnen ze nieuwe alertdefinities toevoegen. Merk op dat er ook het gerelateerde gebruikersrecht [Alertdefinitie wijzigen]([LINK_URL_8]) is, dat in de alertdefinitie zelf wordt ingesteld en niet voor een operator of operatorgroep.

Nadat u een alertdefinitie heeft toegevoegd, krijgt u automatisch het gebruikersrecht **Alertdefinitie wijzigen** voor die definitie. Dit is om ervoor te zorgen dat u wijzigingen kunt aanbrengen in de alertdefinitie voor later onderhoud.

De combinatie van de gebruikersrechten **Alertdefinitie toevoegen** en **Alertdefinitie wijzigen** geeft u ook het recht om de gebruikersrechten van de alertdefinitie te wijzigen. Op deze manier kunt u uw eigen alertdefinitie delen met andere operators.

Administrators hebben standaard het gebruikersrecht **Alertdefinitie toevoegen**.

### Integratie maken [ANCHOR_3]

Met dit gebruikersrecht kunt u integraties in het algemeen maken. En zodra u een integratie heeft gemaakt, krijgt u automatisch het gebruikersrecht [Integratie aanpassen]([LINK_URL_9]) ervoor. Zo kunt u de integratie achteraf onderhouden.

Administrators hebben standaard het gebruikersrecht **Integratie maken**.

### Financiële operator [ANCHOR_4]

Een operator met dit gebruikersrecht kan bestellingen plaatsen, facturen bekijken en betalingen doen.   
De operator krijgt bericht over het verlopen van het account, het bereiken van de limiet van SMS credits en ontvangt betalingsherinneringen. 

Het is verplicht om binnen uw Uptrends-account minimaal één operator te hebben met dit type recht. Het is standaard opgenomen in de groepsrechten van de *Administrators*.
### Infra-toegang

Als u een abonnement op Uptrends Infra heeft, kunt u operators toegang geven tot dit product.

Dit gebruikersrecht is verplicht voor de standaard operatorgroep *Administrators*.
### Technisch contactpersoon

Dit gebruikersrecht wordt ingesteld voor de operator met wie contact moet worden opgenomen bij technische problemen. 

Het is verplicht om minimaal één operator te hebben met het gebruikersrecht *Technisch contactpersoon*. Aanvullende technisch contactpersonen kunnen worden toegevoegd en verwijderd, op voorwaarde dat u altijd ten minste één operator met dit recht houdt.

### Persoonlijke locaties beheren [ANCHOR_5]

Operators die het gebruikersrechttype *Persoonlijke locaties beheren* hebben, kunnen bestaande [persoonlijke locaties]([LINK_URL_10]) maken, verwijderen of beheren binnen het account. Als operators een persoonlijke locatie willen maken, hebben ze toegang nodig tot ten minste één [controleregelgroep]([LINK_URL_11]) met gebruikersrechttype *Maken en verwijderen van controleregels in groep*. 
Het gebruikersrecht *Persoonlijke locaties beheren* is standaard inbegrepen in de gebruikersrechten van de groep *Administrators*.

### Controleregelsjablonen beheren [ANCHOR_6]

Operators aan wie het gebruikersrecht *Beheer controleregelsjablonen* is verleend, kunnen [controleregelsjablonen]([LINK_URL_12]) beheren en toepassen op die controleregels binnen het account waarvoor ze bewerkingsrechten hebben, zonder dat er aanvullende beheerdersrechten nodig zijn.

## Itemgebaseerde gebruikersrechten [ANCHOR_7]

De volgende gebruikersrechten worden ingesteld op het item, bijvoorbeeld integratie, controleregel, terwijl algemene gebruikersrechten systeembreed worden ingesteld.

- [Alertdefinities]([LINK_URL_13])
- [Dashboards]([LINK_URL_14])
- [Integraties]([LINK_URL_15])
- [Controleregels]([LINK_URL_16])
- [Vault]([LINK_URL_17])
- [Operators en operatorgroepen]([LINK_URL_18])