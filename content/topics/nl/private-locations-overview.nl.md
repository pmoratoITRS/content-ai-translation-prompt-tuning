{
  "hero": {
    "title": "Overzicht persoonlijke locaties"
  },
  "title": "Overzicht persoonlijke locaties",
  "summary": "Gebruik persoonlijke locaties om uw controlestations te beheren.",
  "url": "/support/kb/synthetic-monitoring/controlestations/persoonlijke-locaties/overzicht-privelocaties",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-overview",
  "sectionlist": false
}

{{< callout >}} **Aankondiging:** Uptrends biedt een proefperiode van 30 dagen aan voor Persoonlijke locaties! Raadpleeg voor meer informatie de sectie [Proefperiode Persoonlijke locaties trial]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="nl" >}}). {{< /callout >}}

Over het algemeen monitort Uptrends uw websites, applicaties en API's met behulp van het wereldwijde netwerk van [publieke controlestationlocaties]({{< ref path="/checkpoints" lang="nl" >}}). Er zijn echter momenten waarop u mogelijk intern monitoringactiviteiten moet uitvoeren. Voor deze situaties biedt Uptrends de **Persoonlijke locaties**, waarmee u controleregelchecks kunt uitvoeren binnen uw eigen server en firewall.

Met **Persoonlijke locaties** kunt u uw controlestations creëren, definiëren en groeperen op basis van een specifiek doel, gebruik of fysieke locatie (zoals stad, land en continent). Om u volledige controle te geven zal Uptrends de benodigde instructies voor software-installatie verstrekken en bent u verantwoordelijk voor het beheer van alle interne hardware-infrastructuur, installatie, updates en andere [set-upvereisten]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="nl" >}}).

Om toegang te krijgen tot de **Persoonlijke locaties** ** in de Uptrends-webapplicatie gaat u naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.

![screenshot van persoonlijke locaties](/img/content/scr_private-locations-v3.min.png)

## Persoonlijke locaties toevoegen

Een nieuwe locatie toevoegen:

1. Ga naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="buttonPrimary" >}} Locatie toevoegen {{< /AppElement >}}.
3. Geef de naam op van de locatie van waaruit u wilt monitoren.
4. Kies een [controleregelgroep]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="nl" >}}) met het gebruikersrecht om controleregels te creëren. In deze groep worden de statuscontroleregels voor de locatie gecreëerd. Controleregelgroepen met de benodigde rechten worden vermeld in het vervolgkeuzemenu.
5. Klik op de knop {{< AppElement type="savebutton" >}} Persoonlijke locatie toevoegen {{< /AppElement >}} .

 De nieuwe locatie wordt gecreëerd en toegevoegd aan de lijst met persoonlijke locaties. Standaard worden twee niet-geconfigureerde en niet-geïnstalleerde controlestations toegevoegd. Zie de [Veelgestelde vragen]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq" lang="nl" >}}) voor uitleg over waarom er twee controlestations worden toegevoegd (en niet slechts één).

Om de naam van een persoonlijke locatie te wijzigen klikt u op de knop {{< AppElement type="iconSettings" >}} {{< /AppElement >}} achter de naam.

## Een Controlestation toevoegen

Merk op dat aan een nieuwe persoonlijke locatie automatisch twee controlestations worden toegevoegd. U kunt deze eerst installeren of (nu of later) meer controlestations toevoegen.

Een **Controlestation** toevoegen:

1. Ga naar {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}} in het menu.
2. Klik op de knop {{< AppElement type="buttonSecondary" >}} Controlestation toevoegen {{< /AppElement >}} in de locatie waar u een controlestation wilt toevoegen.
3. Kies een controleregelgroep met het gebruikersrecht om controleregels te creëren. In deze groep worden de statuscontroleregels voor de locatie gecreëerd.
4. Klik op de knop {{< AppElement type="savebutton" >}} Controlestation toevoegen {{< /AppElement >}}.

De naam van een **Controlestation** wijzigen:

Klik op het controlestation om zijn pagina te openen en klik op de bewerkknop {{< AppElement type="iconSettings" >}} {{< /AppElement >}} achter de naam en voer een nieuwe naam in.

Het controlestation dat u toevoegt, bestaat alleen als een digitale representatie in de Uptrends-webapplicatie. Het controlestation dat de monitoringchecks uitvoert, moet ook worden geïnstalleerd.

Om een Controlestation te installeren raadpleegt u de instructies [Een Docker controlestation installeren]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="nl" >}}). Meer informatie over Persoonlijke locaties vindt u in [Controlestations voor persoonlijke locaties gebruiken]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="nl" >}}).

## Proefperiode Persoonlijke locaties

The Uptrends **Persoonlijke locaties-proefperiode** is beschikbaar voor alle accountgebruikers. Tijdens deze proefperiode kunt u uw **Persoonlijke locaties** creëren en configureren om deze te testen en te gebruiken met uw bestaande controleregels.

Om u voldoende tijd te geven om u voor te bereiden blijft de proefperiode open totdat u uw eerste Persoonlijke locatie op het Uptrends-platform succesvol heeft geïnstalleerd. Dat gezegd hebbende, u heeft al aan alle noodzakelijke [vereisten]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="nl" >}}) voldaan en [een gecontaineriseerd Docker persoonlijk controlestation geconfigureerd en geïnstalleerd]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="nl" >}}).

Zodra uw eerste persoonlijke locatie actief is, begint uw gratis proefperiode van 30 dagen. Houd er rekening mee dat de einddatum van de proefperiode wordt ingesteld, ongeacht of de **Persoonlijke locaties** zijn geselecteerd in een controleregel-controlestation.

Om de proefperiode te verlengen of over te stappen op een betaald abonnement neemt u contact op met uw accountmanager of het [Support team](/contact).
