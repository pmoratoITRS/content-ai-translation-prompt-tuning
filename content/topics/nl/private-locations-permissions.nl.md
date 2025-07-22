{
  "hero": {
    "title": "Rechten voor persoonlijke locaties instellen"
  },
  "title": "Rechten voor persoonlijke locaties instellen",
  "summary": "Een overzicht van hoe u Rechten voor persoonlijke locaties instelt voor operators en operatorgroepen.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/rechten-persoonlijke-locaties",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-permissions",
  "sectionlist": false,
  "tableofcontents": false
}

Met [Persoonlijke locaties]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="nl" >}}) kunt u interne controleregelchecks uitvoeren binnen uw server en firewall in plaats van vanaf de standaard [Uptrends openbare controlestations]({{< ref path="/checkpoints" lang="nl" >}}). Voor elke persoonlijke locatie kunnen operators een persoonlijke locatie-controlestation openen, maken, bijwerken, uitschakelen en verwijderen. Vanwege veiligheids- en privacyredenen is het van essentieel belang om het zichtbaarheidsniveau en de gebruikersrechten tussen operators te beheren.

Met **Rechten voor persoonlijke locaties** kunt u gebruikersrechten instellen voor specifieke operators en operatorgroepen.

Rechten voor persoonlijke locaties beheren:

1. Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators en groepen {{< /AppElement >}}.
2. Selecteer voor welke operators of operatorgroepen u rechten voor persoonlijke locaties wilt beheren.
3. Ga naar het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} .
4. Selecteer bij **Rechten voor persoonlijke locaties** een van de volgende opties:

- **Persoonlijke locaties toevoegen** – vink deze optie aan om operators en operatorgroepen toegang te geven tot persoonlijke locaties en deze te maken.
- **Persoonlijke locatie gebruiken** – selecteer een persoonlijke locatie in het vervolgmenu en versleep de schuifregelaar om operators en operatorgroepen toe te staan de persoonlijke locatie te selecteren als controlestation om controleregels uit te voeren.
- **Persoonlijke locatie bewerken** –  selecteer een persoonlijke locatie in het vervolgmenu en versleep de schuifregelaar om operators en operatorgroepen toe te staan de persoonlijke locatie te openen, te bewerken en te verwijderen. Operators met dit recht kunnen de persoonlijke locatie ook selecteren als controlestation om controleregels uit te voeren.

Standaard krijgen alle beheerders alle rechten voor persoonlijke locaties zonder dat er extra instellingen nodig zijn. Operators met het recht **Gebruiken** of **Bewerken** kunnen persoonlijke locaties selecteren op het tabblad {{< AppElement type="tab" >}} Controlestations {{< /AppElement >}} van de controleregel. Operators met het recht **Toevoegen** of **Bewerken** hebben toegang tot persoonlijke locaties in het menu {{< AppElement type="menuitem" >}} Persoonlijke locaties {{< /AppElement >}}.

![Rechten persoonlijke locaties GIF](/img/content/gif-private-locations-permissions.gif)