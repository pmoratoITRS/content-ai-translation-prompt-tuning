{
  "hero": {
    "title": "Gebruikersrechten beheren voor automatisch aangemaakte vault-secties"
  },
  "title": "Gebruikersrechten beheren voor automatisch aangemaakte vault-secties",
  "summary": "Als u een transactie opneemt, slaat Uptrends uw gevoelige informatie op in een automatisch aangemaakte sectie van de Uptrends Vault met standaard gebruikersrechten. Leer hoe u gebruikersrechten beheert voor de automatisch aangemaakte vault-tems.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/gebruikersrechten-beheren-voor-automatisch-aangemaakte-vaultsecties",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De [Uptrends vault]([LINK_URL_1]) biedt u een veilige plek om certificaten en public keys op te slaan, samen met de inloggegevens die nodig zijn voor uw transactiescripts. Wanneer u een nieuwe transactiecontroleregel maakt met de Transactie Recorder of als Support een oudere controleregel converteert naar het nieuwere Self-Service Transaction monitoring-formaat, plaatst Uptrends uw gevoelige data automatisch in de vault. Uw script gebruikt deze vault-items en deze gevoelige waarden zijn niet zichtbaar in het script of in uw rapportage ([Lees meer]([LINK_URL_2]) over hoe u gevoelige waarden in uw script gebruikt).

## Standaard gebruikersrechten gebruikt

De vault bevat items die worden opgeslagen in vault-secties. Alleen die individuele operators of operators in de opgenomen [operatorgroepen]([LINK_URL_3]) in de tegel *Gebruikersrechten* van elke vault-sectie kunnen vault-items in de sectie benaderen en wijzigen.

**Nieuwe opnamen en nieuw geconverteerde scripts hebben de standaard gebruikersrechten die zijn toegepast op de nieuwe automatisch aangemaakte vault-sectie(s)**. De standaard gebruikersrechten omvatten de groep Administrators en de gebruikersgroep van het deelaccount, indien van toepassing.

Nieuw geüploade opnames worden altijd toegevoegd aan een automatisch aangemaakte vault-sectie met ongewijzigde standaard gebruikersrechten. Als u de rechten hebt gewijzigd, maakt de volgende upload een nieuwe sectie die de standaard gebruikersrechten gebruikt.

[SHORTCODE_1]
**Opmerking**: om meerdere automatisch gegenereerde secties te vermijden laat u de gebruikersrechten op de standaard staan en repliceert u vault-items in een aangepaste sectie en verwijdert u ze uit de automatisch gegenereerde sectie.
[SHORTCODE_2]

## De standaard gebruikersrechten wijzigen

U kunt de standaard gebruikersrechten voor elk van uw vault-secties wijzigen om ze meer of minder beperkend te maken door groepen of operators op te nemen of uit te sluiten.

1.  Navigeer naar [SHORTCODE_3] Accountinstellingen > Vault [SHORTCODE_4].
2.  Klik om de sectie te openen waarvoor u de gebruikersrechten wilt wijzigen.
3.  Om gebruikersrechten te verwijderen klikt u op *Verwijderen* rechts van een operator of groep.
4.  Om gebruikersrechten toe te voegen klikt u op [SHORTCODE_5]\+ Recht toevoegen[SHORTCODE_6] in de tegel **Gebruikersrechten**.
5.  Selecteer de groep of operator.
6.  Stel het *Rechtenniveau* in op *Alleen bekijken* of *Volledige rechten*.
7.  Klik op [SHORTCODE_7] Toevoegen [SHORTCODE_8].

![]([LINK_URL_4])
