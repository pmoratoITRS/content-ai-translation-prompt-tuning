{
  "hero": {
    "title": "Een team instellen in uw account"
  },
  "title": "Een team instellen in uw account",
  "summary": "In dit artikel wordt uitgelegd uit hoe u een nieuw zelfvoorzienend team instelt in uw Uptrends-account.",
  "url": "[URL_BASE_TOPICS]account/gebruikersrechten/team-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Het doel is om een nieuw zelfvoorzienend team in te stellen in uw Uptrends-account. Het instellen bestaat uit de volgende taken:

- Een nieuwe operatorgroep maken
- Een nieuwe controleregelgroep maken en gebruikersrechten toewijzen
- Gebruikersrechten toewijzen voor alerting en integraties
- Alleen toegang geven tot relevante controleregels
- Specifieke controleregelrechten toewijzen

**Tip:** Gebruik de inhoudsopgave ‘In dit artikel:’ (links) om snel naar een van de taken te springen.

[SHORTCODE_1] **Opmerking:** U moet een administrator zijn om alle stappen in dit set-upproces te kunnen voltooien. [SHORTCODE_2]

## Een nieuwe operatorgroep maken

De nieuwe groep maken:

1. Ga naar het menu [SHORTCODE_5] Accountinstellingen > Operators en groepen [SHORTCODE_6].
2. Klik op de knop [SHORTCODE_7] Operatorgroep toevoegen [SHORTCODE_8] in het gedeelte ’U heeft x operatorgroepen’.
3. Voeg op het tabblad [SHORTCODE_9] Algemeen [SHORTCODE_10] een naam toe voor de operatorgroep in **Omschrijving**. Gebruik ‘Team A’ voor dit voorbeeld.
4. Voeg alle operators die al in uw account staan en deel moeten uitmaken van het team toe aan de operatorgroep. Om een operator toe te voegen, vinkt u het vakje voor de naam aan.
Als de operators nog niet zijn gemaakt, is dit geen probleem, omdat ze zo nodig later aan de groep kunnen worden toegevoegd.
5. Klik op [SHORTCODE_11] Opslaan [SHORTCODE_12] onder aan het scherm.

De nieuwe operatorgroep genaamd ‘Team A’ bestaat nu en er is een aantal operators aan toegewezen.

## Een nieuwe controleregelgroep maken en gebruikersrechten toewijzen

Aangezien ‘Team A’ nieuw is, heeft het geen gebruikersrechten voor andere controleregelgroepen en kunnen de leden van ‘Team A’ alleen nieuwe controleregels maken die deel gaan uitmaken van ‘Controleregels A’. Daarom moet u ervoor zorgen dat u (als administrator) reeds bestaande controleregels heeft toegevoegd aan ‘Controleregels A’, zoals uitgelegd in [De controleregelgroep maken]([LINK_URL_1]). Dit is het enige wat het team zelf niet kan doen. 

### De controleregelgroep maken [ANCHOR_1]

De volgende stap is het maken van een nieuwe controleregelgroep die wordt beheerd door het nieuwe team. 

1. Ga naar het menu [SHORTCODE_13] Accountinstellingen > Controleregelgroepen [SHORTCODE_14].
2. Klik rechtsboven op de knop [SHORTCODE_15] Controleregelgroep toevoegen [SHORTCODE_16].
3. Voer een naam in voor de controleregelgroep in de **Omschrijving**. Gebruik voor dit voorbeeld ‘Controleregels A’.
4. Voeg in de lijst **Controleregels in deze groep** onderaan controleregels toe aan de groep door de groep uit te vouwen en het vakje voor de naam van de controleregel aan te vinken. 
   Als de controleregels nog niet in het account staan, kunnen deze later nog door u of het nieuwe team worden toegevoegd. 
5. (Optioneel) Stel het maximum aantal controleregels (per type) in dat de controleregelgroep mag bevatten. Wilt u het aantal controleregels in de groep niet beperken, vink dan de instelling **Een onbeperkt aantal controleregels toestaan** aan. Houd er rekening mee dat groep nooit meer controleregels kan bevatten dan u beschikbaar heeft in uw account (zie [SHORTCODE_17] Accountinstellingen > Accountinstellingen > Abonnement [SHORTCODE_18] voor wat u heeft). Echter, controleregels kunnen in meer dan één groep voorkomen.
6. Klik op [SHORTCODE_19] Opslaan [SHORTCODE_20] onder aan het scherm.

De nieuwe controleregelgroep ‘Controleregels A’ met daarin een aantal controleregels is nu beschikbaar.

### Gebruikersrechten toewijzen 

Op dit punt heeft u een operatorgroep ‘Team A’ en een controleregelgroep ‘Controleregels A’. De leden van ‘Team A’ kunnen echter nog niet de controleregels in de controleregelgroep ‘Controleregels A’ onderhouden. 

Om dit mogelijk te maken moet u de juiste gebruikersrechten toewijzen. Voer de volgende stappen uit:

1. Ga naar [SHORTCODE_21] Accountinstellingen > Operators en groepen [SHORTCODE_22].
2. Klik op de knop [SHORTCODE_23] Alle operatorgroepen bekijken [SHORTCODE_24].
3. Selecteer de operatorgroep ‘Team A’.
4. Ga naar het tabblad [SHORTCODE_25] Gebruikersrechten [SHORTCODE_26]. 
5. Selecteer in het gedeelte **Rechten voor controleregels** de controleregelgroep ‘Controleregels A’ in de lijst.
 ![screenshot controleregelrechten aan team toevoegen]([LINK_URL_2])
6. Verplaats de schuifregelaar in de rij ‘Controleregels A’ naar het gebruikersrecht *Toevoegen en verwijderen*.
7. Klik onderaan op de knop [SHORTCODE_27] Opslaan [SHORTCODE_28].


U heeft nu de operatorgroep ‘Team A’ de mogelijkheid gegeven nieuwe controleregels te maken. 

Vanaf nu is er geen (algemene) administrator meer nodig om alle nieuwe controleregels voor het team te maken. ‘Team A’ kan nu hun eigen controleregels beheren en zo nodig nieuwe controleregels maken.

## Gebruikersrechten toewijzen voor alerting en integraties

Nu een operatorgroep en een controleregelgroep zijn ingesteld, kan ‘Team A’ de basis voor monitoring instellen. Echter, een belangrijk onderdeel van monitoring is alerting, om ervoor te zorgen dat operators op de hoogte worden gesteld en er snel actie wordt ondernomen in geval van problemen. Hiertoe moet het team alertdefinities en integraties kunnen maken en/of onderhouden. Aangezien dit een set-up is voor een zelfvoorzienend team, gaat u ‘Team A’ de gebruikersrechten geven om zichzelf volledig te beheren.

De gebruikersrechten voor alertdefinities en integraties toewijzen aan ‘Team A’:

1. Ga naar het menu [SHORTCODE_29] Accountinstellingen > Operators en groepen [SHORTCODE_30].
2. Klik op de knop [SHORTCODE_31] Alle operatorgroepen bekijken [SHORTCODE_32] in het gedeelte ‘U heeft x operatorgroepen’.
3. Klik op de operatorgroep ‘Team A’ .
4. Ga naar het tabblad [SHORTCODE_33] Gebruikersrechten [SHORTCODE_34]. 
5. Selecteer in het gedeelte **Algemene systeemrechten** de rechten **Alertdefinitie toevoegen** en **Integraties maken**.
6. Klik links onderaan op de knop [SHORTCODE_35] Opslaan [SHORTCODE_36].

‘Team A’ heeft nu het recht om alertdefinities en integraties te maken.

### Gebruikersrechten toewijzen voor bestaande alerting 

Met de nieuw toegevoegde gebruikersrechten kan het team hun eigen alertdefinities en integraties maken die nodig zijn om hun team te laten functioneren. Er zijn geen administrator-acties vereist om de alerting van het team te onderhouden. U kunt het team echter wel toegang geven tot alertdefinities of integraties die bestonden voordat het team aan uw account werd toegevoegd. Dit is een taak voor een administrator.

‘Team A’ toevoegen aan bestaande alertdefinities:

1. Ga naar het menu [SHORTCODE_37] Accountinstellingen > Operators en groepen [SHORTCODE_38].
2. Klik op de knop [SHORTCODE_39] Alle operatorgroepen bekijken [SHORTCODE_40] in het gedeelte ‘U heeft x operatorgroepen’.
3. Klik op de operatorgroep ‘Team A’.
4. Ga naar het tabblad [SHORTCODE_41] Gebruikersrechten [SHORTCODE_42].
   ![screenshot gebruikersrechten operatorgroep]([LINK_URL_3])
5. Gebruik de vervolgkeuzelijst in het gedeelte **Alertdefinitie gebruikersrechten** voor het selecteren en toevoegen van alle bestaande alertdefinities die ‘Team A’ moet kunnen beheren.
6. Als u per ongeluk een definitie heeft toegevoegd of als ‘Team A’ die definitie niet meer moet beheren, klikt u op de x rechts van de definitie om het gebruikersrecht in te trekken.
7. Klik onderaan op de knop [SHORTCODE_43] Opslaan [SHORTCODE_44].


‘Team A’ toevoegen aan bestaande integraties:

1. Ga naar [SHORTCODE_45] Alerting > Integraties [SHORTCODE_46].
2. Klik op de integratie die ‘Team A’ moet kunnen gebruiken en/of aanpassen.
3. Ga naar het tabblad [SHORTCODE_47] Gebruikersrechten [SHORTCODE_48]. 
4. Klik op de knop [SHORTCODE_49] Recht toevoegen [SHORTCODE_50].
5. Selecteer in de pop-up de operatorgroep ‘Team A’ en selecteer het gebruikersrecht dat u wilt toewijzen. 
   Kies **Integratie gebruiken** als het team de integratie in een alertdefinitie moet kunnen gebruiken.
   Kies **Integratie aanpassen** als het team de integratie volledig moet kunnen onderhouden, inclusief het recht om een integratie te verwijderen.  
6. Klik op de knop [SHORTCODE_51] Toevoegen [SHORTCODE_52].
7. Klik onderaan op de knop [SHORTCODE_53] Opslaan [SHORTCODE_54].

Herhaal de bovenstaande stappen voor alle bestaande integraties waartoe u het nieuwe team toegang wilt geven.

‘Team A’ kan nu alertdefinities instellen en wijzigen en er integraties aan toevoegen. Afhankelijk van uw keuze kunnen zij ook integraties aanpassen.

## Alleen toegang geven tot relevante controleregels

[SHORTCODE_3] **Opmerking**: Deze actie is alleen nodig wanneer u voor het eerst een team in een account instelt. [SHORTCODE_4]

In deze oefening stelt u een zelfvoorzienend team in en wilt u dat het team zich alleen richt op de monitoringdata die voor hen relevant zijn. Er is een trucje nodig om dit te bereiken, dit is waarom:

Een Uptrends-account bevat altijd de operatorgroep ‘Iedereen’. Alle operators in uw account zijn lid van de groep ‘Iedereen’ en hebben standaard allemaal toegang tot monitoringdata van alle controleregels. U kunt de groep ‘Iedereen’ niet verwijderen en u kunt geen operators uit de groep verwijderen. 

De truc is om de operators van ‘Iedereen’ te splitsen in de (bestaande) groep ‘Team A’ en een nieuwe groep ‘Hoofdoperators’. 

U kunt vervolgens het gebruikersrecht om alle data voor de groep ‘Iedereen’ te bekijken verwijderen en gebruikersrechten voor de afzonderlijke groepen (‘Team A’, ‘Hoofdoperators’) naar wens instellen. 

Maak eerst een nieuwe operatorgroep ‘Hoofdoperators’:

1. Ga naar het menu [SHORTCODE_55] Accountinstellingen > Operators en groepen [SHORTCODE_56].
2. Klik op de knop [SHORTCODE_57] Operatorgroep toevoegen [SHORTCODE_58] in het gedeelte ‘U heeft x operatorgroepen’.
3. Voeg op het tabblad [SHORTCODE_59] Algemeen [SHORTCODE_60] een naam toe voor de operatorgroep in **Omschrijving**. Gebruik hier ‘Hoofdoperators’.
4. Voeg alle operators toe die geen lid moeten zijn van het nieuwe team (‘Team A’). Om een operator toe te voegen vinkt u het vakje voor de naam aan.
5. Klik op de knop [SHORTCODE_61] Opslaan [SHORTCODE_62] onder aan het scherm.

Wijzig vervolgens de gebruikersrechten voor gegevens bekijken in de groep ‘Alle controleregels’:

1. Ga naar het menu [SHORTCODE_63] Accountinstellingen > Operators en groepen [SHORTCODE_64].
2. Klik op de knop [SHORTCODE_65] Alle operatorgroepen bekijken [SHORTCODE_66] in het gedeelte ‘U heeft x operatorgroepen’.
3. Selecteer de operatorgroep ‘Iedereen’.
4. Ga naar het tabblad [SHORTCODE_67] Gebruikersrechten [SHORTCODE_68]. 
5. Verwijder in het gedeelte **Rechten voor controleregels** de rij met ‘Alle controleregels’ (gebruikersrecht *Gegevens bekijken*) door op het kruisje aan het einde van de rij te klikken.
   ![screenshot gebruikersrechten voor gegevens bekijken verwijderen]([LINK_URL_4])
6. Klik onder aan het scherm op [SHORTCODE_69] Opslaan [SHORTCODE_70].
7. Weer terug in de lijst **Operatorgroepen** selecteert u deze keer de groep ‘Hoofdoperators’.
8. Ga naar het tabblad [SHORTCODE_71] Gebruikersrechten [SHORTCODE_72]. 
9. Voeg in het gedeelte **Rechten voor controleregels** de controleregelgroep ‘Alle controleregels’ toe met het gebruikersrecht *Gegevens bekijken* door de controleregelgroep in de lijst te kiezen en de schuifregelaar naar het gebruikerrecht te verplaatsen.
10. Klik onder aan het scherm op [SHORTCODE_73] Opslaan [SHORTCODE_74].

In de bovenstaande stappen heeft u de toegang tot alle controleregeldata voor het ‘Team A’ verwijderd en vervolgens de oorspronkelijke gebruikersrechten voor bekijken van data teruggegeven aan alle andere operators (leden van ‘Hoofdoperators’) die geen lid zijn van ‘Team A’.

Het resultaat is dat ‘Team A’ alleen controleregels in controleregelgroep ‘Controleregels A’ ziet, terwijl alle andere operators nog steeds het volledige beeld hebben, zoals voorheen.

Als een operator lid is van meerdere operatorgroepen, kan die meer zien, omdat de andere operatorgroepen hun eigen gebruikersrechten hebben ingesteld. 

## Specifieke rechten voor controleregels toewijzen

Met de instellingen tot nu toe heeft u een team dat een toegewezen controleregelgroep heeft waarin ze controleregels kunnen maken en bewerken, en ze kunnen alertdefinities en integraties maken die ze mogelijk nodig hebben. Dus in wezen zijn ze zelfvoorzienend en zijn er bijna geen administrator-acties nodig. Het kan echter zijn dat het team controleregeldata van andere teams moet kunnen bekijken of ook controleregels van andere teams moet kunnen bewerken.

Om het nieuwe team ‘Team A’ toegang te geven tot andere controleregels, wijst u de benodigde rechten toe aan de controleregelgroepen van de andere teams. Als er bijvoorbeeld een ‘Team B’ is met een controleregelgroep ‘Controleregels B’, kunt u de operatorgroep ‘Team A’ openen en op het tabblad [SHORTCODE_75] Gebruikersrechten [SHORTCODE_76] in het gedeelte **Rechten voor controleregels** de controleregelgroep ‘Controleregels B’ toevoegen uit de lijst en ‘Team A’ het gebruikersrecht **Gegevens bekijken** geven door de schuifregelaar naar dat gebruikersrecht te verplaatsen.
Hierdoor kan ‘Team A’ de monitoringgegevens van ‘Team B’ bekijken, maar niet bewerken. Zo kunnen de teams samenwerken, terwijl de toegang beperkt is. 

