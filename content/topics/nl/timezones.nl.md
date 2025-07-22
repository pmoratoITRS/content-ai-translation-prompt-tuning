{
  "hero": {
    "title": "Tijdzone"
  },
  "title": "Tijdzone",
  "summary": "De instelling Tijdzone beïnvloedt hoe gemonitorde tijden worden gerapporteerd, gebaseerd op de door u gekozen tijdzone.",
  "url": "/support/kb/account/instellingen/tijdzones",
  "translationKey": "https://www.uptrends.com/support/kb/account/timezones"
}

De instelling **Tijdzone** beïnvloedt hoe gemonitorde tijden worden gerapporteerd, gebaseerd op de door u gekozen tijdzone.

Deze instelling wordt geconfigureerd tijdens de Uptrends-accountconfiguratie en kan worden teruggevonden door naar {{< AppElement type="menuitem" >}} Accountinstellingen > Accountinstellingen {{< /AppElement >}} te gaan en het tabblad {{< AppElement type="tab" >}} Instellingen {{< /AppElement >}} te openen.

U heeft de optie om de tijdzone zelf te wijzigen, tenzij er al Real User Monitoring (RUM)-data zijn verzameld in uw Uptrends-account. In dat geval wordt de instelling weergegeven als uitgeschakeld voor wijzigingen en moet u contact opnemen met [Support]({{< ref path="contact" lang="nl" >}}) om de opties te bespreken.

{{< callout >}}
**Opmerking:** Wijzigingen in de tijdzone-instelling zorgen voor een gat of overlapping in uw monitoringdata omdat de applicatie bestaande data niet opnieuw berekent na een tijdzonewijziging. 
{{< /callout >}}

## Zomertijd 

In de Uptrends-applicatie zijn sommige tijdzones gemarkeerd met een sterretje (\*) of hekje (\#) om aan te geven dat de tijdzone onderworpen is aan zomertijd.

- \* : Tijdzone bevindt zich op het noordelijk halfrond en houdt rekening met zomertijd
- \# : Tijdzone bevindt zich op het zuidelijk halfrond en houdt rekening met zomertijd
- Sommige tijdzones houden geen rekening met zomertijd en hebben geen \* of \#.

Als u tijden in UTC (Universal Time Coordinated) wilt zien, gebruik hiervoor dan de tijdzone **UTC** (zonder \* markering). Deze tijdzone-instelling houdt geen rekening met zomertijd. Let op: dit is niet hetzelfde als **UTC\* Engeland, Ierland** die wel zomertijd kent.

## Tijdzones voor operators

De standaard tijdzone-instelling van het Uptrends-account kan worden aangepast om een [extra tijdzone]({{< ref path="support/kb/account/users/operators/main-settings#timezone" lang="nl" >}}) te gebruiken voor individuele operators. Houd er rekening mee dat deze functie alleen beschikbaar is voor [Enterprise-accounts]({{< ref path="/pricing#plans" lang="nl" >}}).
