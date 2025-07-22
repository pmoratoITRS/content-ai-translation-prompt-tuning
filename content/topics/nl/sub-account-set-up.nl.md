{
  "hero": {
    "title": "Deelaccount instellen"
  },
  "title": "Deelaccount instellen",
  "summary": "In dit artikel wordt stapsgewijs uitgelegd hoe u een nieuw deelaccount instelt.",
  "url": "/support/kb/account/gebruikers/deelaccounts/deelaccount-instellen",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/sub-account-set-up"
}

## Een deelaccount creëren

Een nieuw deelaccount creëren:

1.  Open de operator-hub door te gaan naar ({{< AppElement type="menuitem" >}}Accountinstellingen > Operators, groepen en deelaccounts{{< /AppElement >}}).
2.  Klik op de knop {{< AppElement type="buttonSecondary" >}}Deelaccount toevoegen{{< /AppElement >}} in het gedeelte deelaccounts.

Nu moet u op de tabbladen van de pagina *Nieuw deelaccount* wat informatie toevoegen voor het deelaccount.

## Algemeen
### Deelaccount info

1.  Voer een **Deelaccountnaam** in. Bij het opslaan wordt deze naam ook gebruikt om een controleregelgroep en operatorgroep te genereren.
2.  Voer een **Eigen referentie** in (optioneel).

### Gebruikersrechten

In dit gedeelte bepaalt u of de deelaccountoperators controleregels kunnen wijzigen of toevoegen.

1.  Selecteer het vakje **Wijzigen van controleregels toestaan** als u wilt toestaan dat de operators controleregelinstellingen kunnen wijzigen. Door deze functie in te schakelen kunnen de deelaccounthouders ook extra operators toevoegen, maar geen operators verwijderen.
2.  Selecteer het vakje **Toevoegen van controleregels toestaan** als u wilt toestaan dat de deelaccountoperators hun eigen controleregels kunnen instellen. Indien u dit toestaat, geef dan in het vak **Maximum aantal controleregels** op hoeveel zij er mogen toevoegen.

{{< callout >}}
**Opmerking**: Als een deelaccountoperator een controleregel toevoegt, is de nieuwe controleregel afhankelijk van de beschikbaarheid van niet-gebruikte controleregels in het primaire account. Als er in het primaire account niet genoeg controleregels beschikbaar zijn, kan de deelaccountoperator geen nieuwe controleregels toevoegen, zelfs als zij hun maximum aantal controleregels niet hebben bereikt.
{{< /callout >}}

### Nieuwe controleregel info

Het creëren van een deelaccount vereist dat u informatie verstrekt voor een HTTP/HTTPS-controleregel. Selecteer het **Controleregel type** en verstrek een **URL van de controleregel** van de nieuwe controleregel. Uptrends zal deze controleregel toevoegen aan een controleregelgroep met dezelfde naam als het deelaccount.

## SLA

Heeft u een SLA met de nieuwe deelaccounthouder, stel dan de SLA-vereisten in op het tabblad {{< AppElement type="tab" >}}SLA{{< /AppElement >}}. Heeft u een opfrisser nodig over het configureren van SLA, dan kan onze [SLA-sectie]({{< ref path="support/kb/dashboards-and-reporting/sla" lang="nl" >}}) u hierbij helpen.

## Extra controleregels

Op het tabblad {{< AppElement type="tab" >}}Extra controleregels{{< /AppElement >}} kunt u bestaande controleregels toevoegen aan het deelaccount. Hier kunt u later altijd terugkomen om nieuwe controleregels aan de deelaccount toe te voegen.

## Operators

Op dit tabblad kunt u bestaande operators toevoegen aan het deelaccount door ze in de lijst te selecteren. Deelaccountoperators kunnen alleen behoren tot de groep *Iedereen*  en tot hun deelaccountgroep.

## Opslaan

Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} om de deelaccount en de nieuwe controleregel te creëren.

{{< callout >}}
**Opmerking**: Als u wilt dat uw deelaccountoperators alerts ontvangen, moet u een nieuwe [alertdefinitie]({{< ref path="support/kb/alerting/create-alert-definitions" lang="nl" >}}) instellen. En als u van plan bent sms- of telefoon/spraakalerts te gebruiken, voeg dan mobiele telefoonnummers toe in hun [operatorgegevens]({{< ref path="support/kb/account/users/operators/operator-groups" lang="nl" >}}).
{{< /callout >}}
