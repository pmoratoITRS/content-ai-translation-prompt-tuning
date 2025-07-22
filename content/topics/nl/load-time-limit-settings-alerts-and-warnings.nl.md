{
  "hero": {
    "title": "Foutcondities - Laadtijd / Tijd van uitvoeren"
  },
  "title": "Foutcondities - Laadtijd / Tijd van uitvoeren",
  "summary": "Het definiëren van limieten voor laadtijd of tijd van uitvoeren en hun effect op alerting",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/laadtijdlimiet-instellingen-alerts-en-waarschuwingen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/load-time-limit-settings-alerts-and-warnings"
}

Bij het definiëren van foutcondities voor uw controleregels heeft u de optie om limieten voor laadtijd of tijd van uitvoeren in te stellen. U kunt twee limieten invoeren: een lagere limiet voor wanneer de duur een punt van zorg wordt en een hogere limiet voor wanneer de duur kritiek wordt.

De limiet voor tijd van uitvoeren wordt gebruikt voor transactiecontroleregels en controleregels die niet zijn gebaseerd op HTTP(S) of een browser, zoals DNS-, Ping- of mailserver-controleregels.

De laadtijd wordt gebruikt voor HTTP(S)-, webservice HTTP(S)- en Full Page Check-controleregels. Deze kijkt naar de hoeveelheid tijd die de controle duurde van eerste request tot de controle is voltooid. 

{{< callout >}}
**Opmerking**: Uptrends baseert laadtijd op de hoeveelheid tijd die de test duurde van eerste request tot de test is voltooid. Deze tijd verschilt per type controleregel. De laadtijd van een basiscontrole verschilt erg van de laadtijd van een echte browser check voor dezelfde URL. Lees meer over het [verschil tussen eenvoudige controles versus echte browser checks]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="nl" >}}).
{{< /callout >}}

Terwijl andere [foutcondities]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="nl" >}}) altijd een fout genereren wanneer aan de conditie wordt voldaan, kan de paginalaadtijd worden ingesteld om een fout te genereren of de situatie aan te geven door alleen een kleurcode weer te geven op het dashboard *Controleregelstatus*. Houd er rekening mee dat als u de [alerting]({{< ref path="support/kb/alerting" lang="nl" >}})-functionaliteit wilt gebruiken, u fouten moet genereren op basis van deze foutconditie. 

## Totale tijd van uitvoeren controleren toevoegen

Een nieuwe totale tijd van uitvoeren controleren toevoegen:

1. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de naam van de controleregel om deze te bewerken.
3. Open het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}} en vouw het gedeelte **Totale tijd van uitvoeren controleren** uit.
   ![screenshot foutconditie voor tijd van uitvoeren](/img/content/scr_errorconditions-running-times.min.png)
4. Kies of u alleen kleurcodering wilt gebruiken (dashboard *Controleregelstatus*) of een fout wilt genereren.
5. Vul de waarden (in milliseconden) in voor de lagere (zorgelijke) en hogere (kritieke) tijd van uitvoeren.
6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen in de controleregel op te slaan.

Wanneer gebruikt voor een transactiecontroleregel, is de totale tijd van uitvoeren de tijd die nodig is om de volledige transactie te voltooien.

## Een controle voor laadtijden toevoegen

Een nieuwe controle voor de laadtijden toevoegen:

1. Ga naar { {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de naam van de controleregel om deze te bewerken.
3. Open het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}} en vouw het gedeelte **Laadtijd van de pagina controleren** uit.
   ![screenshot foutconditie voor paginalaadtijden](/img/content/scr_errorconditions-load-times.min.png)
4. Kies of u alleen kleurcodering wilt gebruiken (dashboard *Controleregelstatus*) of een fout wilt genereren.
5. Vul de waarden (in milliseconden) in voor de lagere (zorgelijke) en hogere (kritieke) laadtijdlimieten.
6. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen in de controleregel op te slaan.

## Alleen met kleurcode weergeven

Als u de optie *Alleen met kleurcode weergeven* heeft gekozen voor één of beide tijdlimieten, zal het dashboard *Controleregelstatus* aangeven dat de tijdlimieten zijn bereikt. Als de ondergrens (drempel punt van zorg) wordt overschreden, verschijnt de waarde met een gele achtergrond in de kolom **Totale tijd**, en als de bovengrens (kritieke drempel) wordt overschreden, verschijnt de tijd met een rode achtergrond. U kunt het dashboard *Controleregelstatus* openen door naar het menu {{< AppElement type="menuitem" >}} Monitoring > Statusdetails {{< /AppElement >}} te gaan.

![screenshot dashboard Controleregelstatus met kleurcodes](/img/content/scr_errorconditions-colorcode-loadtime.min.png)

U ziet dat er in het dashboard *Controleregelstatus* hierboven twee controleregels zijn die de totale tijd in geel en rood weergeven, maar dat de foutindicator aan de linkerkant nog steeds groen is voor geslaagde tests. Dit is het resultaat van het gebruik van de optie *Alleen met kleurcode weergeven*.

## Fout genereren {id="generate-error"}

Als u alerts wilt genereren op basis van de paginalaad- of uitvoertijden, moet u de optie **Fout genereren** gebruiken in de foutconditie. Alleen wanneer er fouten worden gegenereerd, kunnen vervolgens alerts worden gegenereerd. In het Knowledge Base-artikel [Overzicht alerting]({{< ref path="support/kb/alerting/alerting-overview" lang="nl" >}}) wordt gedetailleerd uitgelegd hoe de opeenvolging van controleregelchecks naar alerts werkt.

Als u de optie *Fout genereren* kiest krijgt u nog steeds de kleurcodering van de laad- of uitvoertijden op het dashboard *Controleregelstatus.
