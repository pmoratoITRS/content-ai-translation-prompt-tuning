{
  "hero": {
    "title": "Overzicht aangepaste integraties"
  },
  "title": "Overzicht aangepaste integraties",
  "summary": "Overzicht aangepaste integraties",
  "url": "[URL_BASE_TOPICS]alerting/integraties/aangepaste-integraties/overzicht-aangepaste-integraties",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Stel dat u uw Uptrends-account koppelt aan het operationsmanagementsysteem dat uw organisatie gebruikt. Door alertdata van Uptrends in te voeren in uw bestaande incidentmanagementprocessen, creëert u een naadloze integratie van Uptrends' externe monitoring in de dagelijkse procedures die uw teams al gebruiken.

Als onze [voorgedefinieerde integratietypes]([LINK_URL_1]) uw DevOps-software niet bevatten, kunt u de aangepaste-integratieoptie gebruiken om de integratie zelf te bouwen. Het belangrijkste bij het bouwen van een succesvolle integratie is, dat u weet wat voor soort bericht het andere systeem verwacht. In de API-documentatie van de third party vindt u welke URL u moet gebruiken en welke inhoud u op die URL moet posten. Deze zogenoemde webhook-gebaseerde integraties laten Uptrends “hook” (koppelen) met het andere systeem door directe calls toe te staan. Uptrends kan een call naar de integratie initiëren zodra er een relevante alert verschijnt.

De artikelen in deze sectie beschrijven het bouwen van de juiste berichtinhoud (met inbegrip van de juiste opmaak), het creëren van verschillende regels voor verschillende berichttypes en hoe u uw aangepaste integratie kunt testen als u klaar bent met de configuratie.

## Een aangepaste integratie configureren

Volg deze stappen om aangepaste integraties te gaan gebruiken:

1.  Voeg een aangepaste-integratiesjabloon toe aan uw account. Om dit te doen klikt u op de knop [SHORTCODE_1]\+[SHORTCODE_2] naast *Integraties* in het menu *Alerts* in de Uptrends-applicatie.
2.  Er verschijnt een pop-upvenster waarin u een integratietype kunt kiezen. Voor een aanpasbare integratie scrollt u naar beneden in de lijst en selecteert **Uptrends-integratie**.
3.  Specificeer de URL van de API waarmee u wilt verbinden, gebruik hierbij de variabele *ApiUrl* onder **Voorgedefinieerde variabelen**. Welke URL dit moet zijn vindt u in de documentatie of gebruikersinterface van het externe systeem waarmee u Uptrends wilt verbinden.
4.  Geef de integratie een passende naam in het veld **Integratienaam**.
5.  Pas zo nodig uw integratie aan in de tab [SHORTCODE_3]Aanpassingen[SHORTCODE_4]. De andere hoofdstukken in dit artikel begeleiden u door het proces.
6.  Als u klaar bent met de configuratie klikt u op [SHORTCODE_5]Opslaan[SHORTCODE_6] om uw instellingen te bewaren. U kunt desgewenst terugkeren naar de integratie om uw aanpassingen te voltooien.

## De juiste berichtinhoud bouwen

Deze nieuwe integratie is een voorgedefinieerde sjabloon die een (aanpasbare) JSON-geformatteerde berichtinhoud bevat met de volledige reeks beschikbare alertingvariabelen. Dit standaard berichtformaat stelt u in staat om alle beschikbare informatie bij elke alert te verwerken, maar u kunt ook gegevens verwijderen die u niet nodig heeft, uw eigen gegevens toevoegen of het berichtformaat wijzigen. U vindt de voorgedefinieerde berichtinhoud in de tab [SHORTCODE_7]Aanpassingen[SHORTCODE_8], samen met andere opties om uw integratie verder aan te passen.

-   Om te begrijpen hoe u begint met het opzetten van de gewenste berichtinhoud en hoe u variabelen gebruikt, raden we u aan eerst ons artikel over [het bouwen van de juiste berichtinhoud]([LINK_URL_2]) te lezen.
-   Een compleet overzicht van beschikbare alertingvariabelen vindt u in onze lijst met [systeemvariabelen voor alerting]([LINK_URL_3]).
-   Vergeet niet dat uw uitgaande bericht correct moet zijn opgemaakt. Zorg ervoor dat u onze [handleiding voor berichtopmaak]([LINK_URL_4]) leest om onnodige fouten in uw externe applicatie te voorkomen.

## Berichttypes

Er zijn verschillende soorten alertberichten. Uptrends maakt onderscheid tussen **Foutberichten**, **Herinneringen** en **Ok-berichten**. Standaard worden al deze berichttypes gemaakt met dezelfde instellingen. Wanneer u echter een aangepaste integratie configureert of een bestaande integratie aanpast, kunt u verschillende sets acties maken voor elk afzonderlijk berichttype. Bekijk ons [artikel over berichttypes]([LINK_URL_5]) voor meer informatie.

## Uw aangepaste integratie testen

Nadat u een aangepaste integratie heeft gemaakt of gewijzigd, is het handig om deze eerst te testen voordat u deze in production gebruikt. Ons [artikel over het testen van uw aangepaste integratie]([LINK_URL_6]) beschrijft op welke manieren u de nieuw geconfigureerde integratie kunt testen.

## De integratie toevoegen aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze **koppelen aan een of meer escalatieniveaus om alerts te ontvangen** via de integratie. Om een integratiedefinitie aan een escalatieniveau te koppelen doet u het volgende:

1.  Navigeer naar de betreffende alertdefinitie in Uptrends (*Alerts* > *Alertdefinities*).
2.  Klik om een bestaande definitie te openen of creëer een nieuwe met de knop [SHORTCODE_9]Alertdefinitie toevoegen[SHORTCODE_10] rechts bovenaan.
3.  Klik op een tab [SHORTCODE_11]Escalatieniveau[SHORTCODE_12].
4.  Selecteer de selectievakjes voor uw aanpasbare-integratiedefinities in het gedeelte **Alerts versturen door integraties**.
5.  Klik op [SHORTCODE_13]Opslaan[SHORTCODE_14] als u klaar bent.

**Dat is alles!** U heeft met succes een aangepaste integratie geconfigureerd.

Zoals gewoonlijk kunt u als u vragen heeft [contact opnemen met ons supportteam]([LINK_URL_7]).
