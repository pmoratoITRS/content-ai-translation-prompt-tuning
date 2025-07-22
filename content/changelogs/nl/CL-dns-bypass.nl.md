{
  "title": "Duidelijkere DNS-bypass-informatie in details van de controle",
  "date": "2024-03-20",
  "url": "/changelog/maart-2024-dns-bypass",
  "translationKey": "https://www.uptrends.com/changelog/march-2024-dns-bypass"
}

In de laatste update hebben we de duidelijkheid verbeterd door de bypass-URL en het resolved IP-adres expliciet weer te geven in de [details van de controle]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/check-details" lang="nl" >}}) wanneer een DNS-bypass is ingesteld. Voorheen toonde Uptrends alleen het afzonderlijk resolved IP-adres, wat voor verwarring kon zorgen. Nu kunt u gemakkelijk onderscheid maken tussen deze adressen voor beter begrip en probleemoplossing.

Bij het creëren of bewerken van een Full Page Check- of Transactiecontroleregel kunt u kiezen om een [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="nl" >}}) toe te voegen. De DNS-bypass zorgt ervoor dat de webpagina wordt omgezet naar het opgegeven IP-adres in plaats van naar het adres dat standaard wordt gebruikt. Deze optie bevindt zich in het gedeelte _Verbinding_ op het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van de controleregel. 