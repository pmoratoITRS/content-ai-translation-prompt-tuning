{
  "hero": {
    "title": "Gebruikersrechten beheren voor automatisch aangemaakte vault-secties"
  },
  "title": "Gebruikersrechten beheren voor automatisch aangemaakte vault-secties",
  "summary": "Als u een transactie opneemt, slaat Uptrends uw gevoelige informatie op in een automatisch aangemaakte sectie van de Uptrends Vault met standaard gebruikersrechten. Leer hoe u gebruikersrechten beheert voor de automatisch aangemaakte vault-tems.",
  "url": "/support/kb/synthetic-monitoring/transacties/gebruikersrechten-beheren-voor-automatisch-aangemaakte-vaultsecties",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/managing-authorizations-for-automatically-created-vault-sections"
}

De [Uptrends vault](/support/kb/vault) biedt u een veilige plek om certificaten en public keys op te slaan, samen met de inloggegevens die nodig zijn voor uw transactiescripts. Wanneer u een nieuwe transactiecontroleregel maakt met de Transactie Recorder of als Support een oudere controleregel converteert naar het nieuwere Self-Service Transaction monitoring-formaat, plaatst Uptrends uw gevoelige data automatisch in de vault. Uw script gebruikt deze vault-items en deze gevoelige waarden zijn niet zichtbaar in het script of in uw rapportage ([Lees meer](/support/kb/synthetic-monitoring/transacties/gevoelige-transactiedata-gebruiken-die-zijn-opgeslagen-in-de-vault) over hoe u gevoelige waarden in uw script gebruikt).

## Standaard gebruikersrechten gebruikt

De vault bevat items die worden opgeslagen in vault-secties. Alleen die individuele operators of operators in de opgenomen [operatorgroepen](/support/kb/account/gebruikers/operators/operatorgroepen) in de tegel *Gebruikersrechten* van elke vault-sectie kunnen vault-items in de sectie benaderen en wijzigen.

**Nieuwe opnamen en nieuw geconverteerde scripts hebben de standaard gebruikersrechten die zijn toegepast op de nieuwe automatisch aangemaakte vault-sectie(s)**. De standaard gebruikersrechten omvatten de groep Administrators en de gebruikersgroep van het deelaccount, indien van toepassing.

Nieuw geüploade opnames worden altijd toegevoegd aan een automatisch aangemaakte vault-sectie met ongewijzigde standaard gebruikersrechten. Als u de rechten hebt gewijzigd, maakt de volgende upload een nieuwe sectie die de standaard gebruikersrechten gebruikt.

{{< callout >}}
**Opmerking**: om meerdere automatisch gegenereerde secties te vermijden laat u de gebruikersrechten op de standaard staan en repliceert u vault-items in een aangepaste sectie en verwijdert u ze uit de automatisch gegenereerde sectie.
{{< /callout >}}

## De standaard gebruikersrechten wijzigen

U kunt de standaard gebruikersrechten voor elk van uw vault-secties wijzigen om ze meer of minder beperkend te maken door groepen of operators op te nemen of uit te sluiten.

1.  Navigeer naar {{< AppElement type="menuitem" >}} Accountinstellingen > Vault {{< /AppElement >}}.
2.  Klik om de sectie te openen waarvoor u de gebruikersrechten wilt wijzigen.
3.  Om gebruikersrechten te verwijderen klikt u op *Verwijderen* rechts van een operator of groep.
4.  Om gebruikersrechten toe te voegen klikt u op {{< AppElement type="button" >}}\+ Recht toevoegen{{< /AppElement >}} in de tegel **Gebruikersrechten**.
5.  Selecteer de groep of operator.
6.  Stel het *Rechtenniveau* in op *Alleen bekijken* of *Volledige rechten*.
7.  Klik op {{< AppElement type="button" >}} Toevoegen {{< /AppElement >}}.

![](/img/content/scr-vault-add-permission.min.png)
