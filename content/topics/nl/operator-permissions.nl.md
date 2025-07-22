{
  "hero": {
    "title": "Gebruikersrechten voor operator(groep) instellen"
  },
  "title": "Gebruikersrechten voor operator(groep) instellen",
  "url": "/support/kb/account/users/operators/operator-gebruikersrechten",
  "summary": "Een overzicht van hoe u gebruikersrechten instelt voor uw operators en operatorgroepen.",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-permissions"
}

{{< callout >}}Operator-gebruikersrechten zijn alleen beschikbaar voor **Enterprise-accounts**.{{< /callout >}}

De **Operator(groep)- gebruikersrechten** zijn gebruikersrechten die meer controle en flexibiliteit toevoegen aan operators en operatorgroepen. Met deze rechten kunnen beheerders een specifiek toegangsniveau instellen waarop operators of groepen operators kunnen bekijken, maken (of toevoegen), instellingen kunnen bewerken en operators kunnen verwijderen. In dit opzicht zijn dergelijke privileges niet beperkt tot beheerders, maar kunnen ze nu worden gedeeld tussen operators en groepen, mits hen dit recht is toegekend. Op dezelfde manier kunt u dergelijke instellingen voor bekijken, maken, wijzigen en verwijderen ook toekennen aan niet-beheerdersaccounts.

Standaard zijn er twee hoofd-[operatorgroepen]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="nl" >}}) ingesteld in uw Uptrends-account: Administrators en Iedereen. De *groep Administrators* verwijst naar operators met volledige toegangsrechten en kan alles in uw Uptrends-account beheren. De *groep Iedereen* verwijst naar alle operators die aan een account zijn toegevoegd. Wel komt iedereen automatisch in aanmerking voor het gebruikersrecht *alle operators bekijken*, waardoor iedereen zichtbaar is voor alle andere operators, inclusief niet-beheerders.

Er zijn echter bepaalde gevallen waarin u de brede zichtbaarheid van de *groep Iedereen* om privacy- en veiligheidsredenen wilt beperken. U wilt bijvoorbeeld dat alleen gemachtigde operators toegang hebben tot de gevoelige informatie van uw organisatie, maar u heeft ook contractanten en andere partijen uitgenodigd om lid te worden van uw Uptrends-team. Om kwetsbaarheid en potentiële risico's te voorkomen is het beter om zaken gescheiden te houden en openbare toegang te beperken. Met **Operator-gebruikersrechten** kunt u de standaardinstelling van de *groep Iedereen* zo verwijderen, dat de zichtbaarheid *iedereen kan iedereen zien* niet langer van toepassing is.

Kortom, **Operator-gebruikersrechten** zijn handig om de zichtbaarheid en het toegangsniveau van uw operators en operatorgroepen te beheren. Door de juiste gebruikersrechten in te stellen, kunnen teams effectief samenwerken en specifieke groepstaken uitvoeren, zoals dashboard delen, alerts definiëren, rapporten plannen enzovoort. Verder kunnen teams zelfvoorzienend zijn in het afhandelen van beheertaken voor verbeterde beveiliging, flexibiliteit en controle binnen uw organisatie.

![Operator-gebruikersrechten voor de groep Iedereen en niet-beheerders](/img/content/scr-everyone-operator-permissions.min.png)

## Operator(groep)-gebruikersrechten instellen
Operatorrechten kunnen individueel worden ingesteld via **Operators** of in clusters via **Operatorgroepen**. Leden die tot een operatorgroep behoren krijgen automatisch de gebruikersrechten die voor die groep zijn ingesteld.

{{< callout >}} Alle leden van de groep Administrators kunnen operators zien, maken, bewerken en nieuwe operators aan elke groep toevoegen. {{< /callout >}}

## Toegangsrechten
Er zijn vier niveaus van toegangsrechten die u kunt instellen voor elke operator en/of operatorgroep:
- Geen: er is geen specifiek gebruikersrecht ingesteld voor een operator en/of operatorgroep. Om de zichtbaarheid van operator(groepen) voor anderen te beperken, moet de standaardzichtbaarheid van de *groep Iedereen* zelf eerst worden verwijderd.
- Bekijk operators: operators toestaan de operatorgroep en de operators binnen de groep te zien.
- Instellingen wijzigen: operators toestaan de instellingen van elke operator binnen de groep te bewerken.
- Toevoegen en verwijderen: operators toestaan operators binnen de groep te maken en te verwijderen.

### Gebruikersrechten instellen via operators

1. Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators en groepen {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="button" >}} Alle operators bekijken {{< /AppElement >}}.
3. Selecteer de operatornaam waaraan u gebruikersrechten wilt toekennen.
4. Op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} ziet u de container met *Operatorrechten*. Voeg uw operators toe door ze te selecteren in het keuzemenu en stel de gewenste gebruikersrechten in met de schuifregelaar. Klik op de *X* om instellingen te verwijderen of de hele rij te wissen.
![Instellingen operatorrechten](/img/content/scr-operator-permissions.min.png)
5. Klik linksonder in het scherm op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.

### Gebruikersrechten instellen via Operatorgroepen

1. Ga naar {{< AppElement type="menuitem" >}} Accountinstellingen > Operators en groepen {{< /AppElement >}}.
2. Klik op de knop {{< AppElement type="button" >}} Alle operatorgroepen bekijken {{< /AppElement >}}.
3. Selecteer de operatorgroep waaraan u gebruikersrechten wilt toekennen. 
4. Op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} ziet u de container met *Operatorrechten*. Voeg uw operatorgroepen toe door ze te selecteren in het keuzemenu en stel de gewenste gebruikersrechten in met de schuifregelaar. Klik op de *X* om instellingen te verwijderen of de hele rij te wissen.
![Instellingen operatorgroeprechten](/img/content/scr-operator-group-permissions.min.png)
5. Klik linksonder in het scherm op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.

{{< callout >}} **Opmerking:** Het niveau van gebruikersrechten dat is geconfigureerd met de **Operatorrechten**, is ook van kracht en wordt weerspiegeld op andere locaties waar operators kunnen worden geselecteerd, bijvoorbeeld *Alertdefinities* en *Geplande rapporten*. Daarom kan de zichtbaarheid van elke operator of operatorgroepen variëren, afhankelijk van de rechten die aan hen zijn toegekend.
