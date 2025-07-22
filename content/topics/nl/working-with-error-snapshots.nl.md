{
  "hero": {
    "title": "Werken met snapshots van fouten"
  },
  "title": "Werken met snapshots van fouten",
  "summary": "Snapshots van fouten kunnen helpen bij het oplossen van problemen, kijk wanneer ze beschikbaar zijn",
  "url": "/support/kb/alerting/fouten/werken-met-snapshots-van-fouten",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/working-with-error-snapshots"
}

Stel, uw website is down, maar u weet niet waarom. U logt in op uw Uptrends-account voor websitemonitoring en concludeert dat gebruikers mogelijk een verbindingsfout ondervinden. Maar hoe? Door de foutdetails en de foutsnapshots van uw controleregel te controleren.

## Wat is een foutsnapshot?

Een foutsnapshot is een schermopname die door de Uptrends-service wordt gemaakt om u te laten zien wat gebruikers mogelijk ervaren in hun browser wanneer er een probleem optreedt.

![screenshot van controledetails met foutsnapshot](/img/content/scr_check-details-with-error-snapshot.min.png)

## Hoe werken foutsnapshots?

Uptrends genereert foutsnapshots in specifieke omstandigheden.

- Snapshots zijn alleen beschikbaar voor **HTTP(S)-**, **Webservice (HTTP(S))-** en **Transactie-controleregels**.
- Uptrends maakt alleen snapshots bij specifieke fouten (patternmatch-fouten bijvoorbeeld, maar niet bij performancelimiet-fouten). In het geval van een infrastructuurgerelateerde fout, zoals een TCP-verbindingsfout, hebben we geen inhoud om weer te geven.  
- De Uptrends-service maakt alleen snapshots van bevestigde fouten die de **eerste** zijn in een reeks. Opeenvolgende fouten krijgen geen snapshot van de fout. {{< callout >}}**Let op**: Het kan enkele minuten duren voordat foutsnapshots zichtbaar zijn nadat een fout is opgetreden. In sommige gevallen is een snapshot mogelijk niet beschikbaar, dit hangt af van de inhoud die Uptrends ontvangt.{{< /callout >}}
