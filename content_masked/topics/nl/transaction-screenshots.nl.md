{
  "hero": {
    "title": "Werken met Transactie-schermopnamen"
  },
  "title": "Werken met Transactie-schermopnamen",
  "summary": "Uptrends kan schermopnamen maken van fouten van iedere transactie stap. Lees hier hoe u dit kunt instellen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transactie-schermopnamen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]
**Opmerking:** Transactie-schermopnamen zijn beschikbaar in de **Enterprise-versie** en de **Business-versie**.
[SHORTCODE_2]

Bij het monitoren van transacties kan men snel het overzicht verliezen bij alle data die via een webpagina worden gecommuniceerd. Om deze taak overzichtelijker te maken bieden we schermopnamen voor transacties.

## Waarvoor gebruik ik Transactie-schermopnamen?

Schermopnamen zijn nuttig bij het opsporen van een specifieke fout of als u wilt zien hoe een bepaalde pagina eruitzag op een specifieke tijd en dag. U kunt bepalen van welke stappen u een schermopname wilt hebben, wij zullen de schermopname van het einde van die stap verstrekken.

## Wanneer genereert Uptrends een schermopname?

We genereren een schermopname bij de volgende gebeurtenissen:

-   **Standaard:** Wanneer er tijdens een transactie een fout optreedt. Hiervoor hoeft u niets in te stellen, dit gebeurt automatisch.
-   **Ad-hoc:** Wanneer u in een specifieke stap een Transactie-schermopname hebt geactiveerd, nadat de stap is voltooid.

## Hoe configureer ik schermopnamen?

[SHORTCODE_3]
**Opmerking:** U hebt een transactie nodig om de Transactie-schermopnamen te kunnen activeren.
[SHORTCODE_4]

-   Kies *Controleregels* in het menu *Controleregels* en selecteer de transactie waarvoor u schermopnamen wilt activeren.
-   Selecteer in het tabblad [SHORTCODE_5]Stappen[SHORTCODE_6] de stap waarvoor u een schermopname wilt activeren.
-   Klik op het selectievak **Schermopname** en we zullen telkens wanneer de stap is voltooid een schermopname genereren.

## Waar vind ik Transactie-schermopnamen?

Transactie-schermopnamen worden weergegeven in de *Controleregel log* (Controleregel > Controleregel log). Wanneer u op een specifieke transactiecontrole klikt, worden de uitgevoerde stappen weergegeven. Indien een stap een schermopname bevat, klikt u op het camerapictogram om de opname te bekijken.
