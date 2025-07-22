{
  "title": "Eindeutigere DNS Bypass-Informationen bei den Kontrolldetails",
  "date": "2024-03-20",
  "url": "/changelog/maerz-2024-dns-bypass",
  "translationKey": "https://www.uptrends.com/changelog/march-2024-dns-bypass"
}

Mit dem letzten Update haben wir für mehr Klarheit gesorgt, indem wir eindeutig die Bypass URL und aufgelösten IP-Adressen in den [Kontrolldetails]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/check-details" lang="de" >}}) anzeigen, wenn ein DNS Bypass eingerichtet ist. Zuvor hat Uptrends nur die getrennt aufgelösten IP-Adressen angezeigt, was zu Verwirrung führen konnte. Nun kann zwischen diesen Adressen leicht unterschieden werden. Es soll zu einem besseren Verständnis bei Fehlerbehebungen führen.

Bei der Erstellung oder Bearbeitung eines Full Pagechecks oder eines Transaktionsprüfobjekts kannst du einen [DNS Bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="de" >}}) einrichten. Der DNS Bypass stellt sicher, dass die Webseite auf die angegebene IP-Adresse aufgelöst wird, statt der standardmäßig genutzten. Diese Option findest du beim Prüfobjekt im Bereich _Verbindung_ auf der Registerkarte {{< AppElement type="tab" >}}Erweitert {{< /AppElement >}}.