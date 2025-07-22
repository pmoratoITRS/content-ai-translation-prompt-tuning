{
  "hero": {
    "title": "Browsertypes"
  },
  "title": "Browsertypes",
  "summary": "Welke browsertypes zijn beschikbaar voor de Full Page Check?",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/browsertypes",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/browser-types",
  "tableofcontents": false
}

U kunt een FPC configureren om een van de verschillende beschikbare browsers te gebruiken. De instelling **Browser type** is zowel te vinden op het tabblad {{< AppElement type="tab" >}} Algemeen {{< /AppElement >}} als op het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van de controleregelinstellingen. De volgende browsers zijn beschikbaar:

- Chrome met extra kengetallen
- Chrome standaard
- Microsoft Edge

Uptrends houdt de browsers up-to-date op de [controlestations]({{< ref path="/checkpoints" lang="nl" >}}), dus uw controle wordt doorgaans uitgevoerd in de nieuwste versie die beschikbaar is voor de geselecteerde browser.

{{< callout >}}
**Opmerking:** Als u wilt monitoren hoe uw website zich gedraagt op een mobiel apparaat, moet u de [user agent]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="nl" >}}) aanpassen op het tabblad {{< AppElement type="tab" >}} Extra {{< /AppElement >}} van de controleregel.
{{< /callout >}}

## Extra kengetallen {id="chrome-extra-metrics"}

Als aanvulling op enkele standaardmetingen biedt Uptrends aanvullende informatie, zoals [W3C-navigatietijden]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="nl" >}}), [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="nl" >}}), [tijdlijn screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="nl" >}}) en meer gedetailleerde informatie op elementniveau, inclusief protocolversie en TLS-info. Zie het Knowledge Base-artikel [Extra kengetallen en functies]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="nl" >}}) voor een volledige beschrijving .

De extra kengetallen zijn beschikbaar voor de browsertypes: 

- Chrome met extra kengetallen
- Microsoft Edge
