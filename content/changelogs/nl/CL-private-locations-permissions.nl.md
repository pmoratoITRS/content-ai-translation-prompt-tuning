{
  "title": "Introductie Gebruikersrechten Persoonlijke locaties",
  "date": "2025-01-29",
  "url": "/changelog/januari-2025-gebruikersrechten-persoonlijke-locaties",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-private-locations-permissions"
}

Met [Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="nl" >}}) kunt u in controleregelchecks (intern) uitvoeren binnen uw server en firewall in plaats van de standaard [Uptrends publieke controlestations]({{< ref path="/checkpoints" lang="nl" >}}) te gebruiken.

Standaard hebben alle operators toegang tot alle persoonlijke controlestationlocaties. Operators kunnen op elk gewenst moment een controlestation creëren, bijwerken, uitschakelen en verwijderen. Het is van essentieel belang om het niveau van zichtbaarheid en gebruikersrechten tussen operators te beheren.

Met de nieuwe functie **Persoonlijke locaties beheren** kunt u gebruikersrechten instellen voor specifieke operators en operatorgroepen:

- Toevoegen — hiermee kunnen operators en operatorgroepen toegang krijgen tot persoonlijke locaties en deze maken.
- Bewerken — hiermee kunnen operators en operatorgroepen toegang krijgen tot persoonlijke locaties, deze bewerken en verwijderen.
- Gebruiken — hiermee kunnen operators en operatorgroepen de persoonlijke locatie selecteren als een controlestation om controleregels uit te voeren.

Als een operator een van de bovenstaande rechten heeft, is de persoonlijke locatie zichtbaar op het tabblad {{< AppElement type="tab" >}} Controlestations {{< /AppElement >}} van een controleregel en toegankelijk in het menu {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.

![Gebruikersrechten Persoonlijke locaties GIF](/img/content/gif-private-locations-permissions.gif)