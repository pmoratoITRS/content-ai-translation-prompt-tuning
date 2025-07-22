{
  "hero": {
    "title": "IP-adressen voor whitelisting"
  },
  "title": "IP-adressen voor whitelisting",
  "summary": "Alle diensten van Uptrends, met inbegrip van de App-portal, de www-sites, de Uptrends API en alle andere diensten gerelateerd aan Uptrends, Uptrends Infra en Uptrends Real User Monitoring opereren vanaf meerdere locaties met meerdere IP-adressen.",
  "url": "/support/kb/account/ip-adressen-whitelisten",
  "translationKey": "https://www.uptrends.com/support/kb/account/ip-addresses-for-whitelisting"
}

{{< callout >}}
**Opmerking:** Zoekt u de lijst met **IP-adressen van controlestations** om te whitelisten zodat uw controleregels correct kunnen werken? Bekijk de volledige lijst van [Uptrends' controlestation IP-adressen]({{< ref path="/checkpoints" lang="nl" >}}).
{{< /callout >}}

Uptrends Synthetics, Uptrends Infra en Uptrends Real User Monitoring maken gebruik van verschillende diensten. Deze diensten omvatten de App-portal, de www-sites, de Uptrends-API en meer. Ze opereren vanaf meerdere locaties met meerdere IP-adressen. Het adres waarnaar het domein api.uptrends.com wordt omgezet, kan bijvoorbeeld elke vijf minuten veranderen. Dit geldt voor alle subdomeinen van uptrends.com.

{{< callout >}}
**Tip:** als u onze applicaties moet whitelisten, is ons advies om de uptrends.com-domeinen en -subdomeinen te whitelisten (alleen voor HTTPS, en voor IPv4 en IPv6), omdat u hierdoor niet afhankelijk bent van eventuele wijzigingen in onze IP-adressen.
{{< /callout >}}

 Zet deze ranges IPv6-adressen op de whitelist:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

De onderstaande tabellen tonen welke specifieke IPv4/IPv6-adressen op de whitelist moeten worden gezet voor bepaalde diensten.

## Uptrends Synthetics
| URL                       | IP-adres of -range                   | Gebruikt voor                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| `api.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.211
- 95.211.70.211 {{< /tableformatter >}}  | API-communicatie (Synthetics) |
| `app.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.213
- 95.211.70.213 {{< /tableformatter >}}  | Uptrends-app |
| `customername.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.205
- 95.211.70.205 {{< /tableformatter >}} | {{< tableformatter >}} 
SP-geïnitieerde SSO
Zie voor meer informatie [Overzicht Single Sign-On]({{< ref path="support/kb/account/settings/single-sign-on-overview#how-sso-users-log-in" lang="nl" >}}), *Hoe kunnen SSO-gebruikers inloggen?*, optie 2. {{< /tableformatter >}} |
| `status.uptrends.com`       | {{< tableformatter >}} 
- 178.162.179.217
- 95.211.70.217  {{< /tableformatter >}} | Publieke statuspagina's |
| `www.uptrends.com`          | {{< tableformatter >}}
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  {{< /tableformatter >}}| Downloads |

## Uptrends Infra
| URL                       | IP-adres of -range                   | Gebruikt voor                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  `api.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.210
- 95.211.70.210 {{< /tableformatter >}} |  API-communicatie (Infra) | 
|  `app.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.208
- 95.211.70.208 {{< /tableformatter >}} |  Uptrends Infra-app | 
|  `collector.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.209
- 95.211.70.209 {{< /tableformatter >}} |  {{< tableformatter >}}
Data verzonden door agents 
De machine waarop de agent is geïnstalleerd moet hier toegang toe hebben! {{< /tableformatter >}} |
| `www.uptrends.com` | {{< tableformatter >}} 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5{{< /tableformatter >}} |  Downloads, bijv. de agentupdates | 

## Uptrends RUM

| URL                 | Gebruikt voor                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `code.highcharts.com` | Nodig om de kaarten op uw RUM-overzicht weer te geven. De machine die het dashboard weergeeft moet toegang hebben tot dit domein. |

## Alerting

| IP-adres of -range                                                        | Gebruikt voor            |
|----------------------------------------------------------------------------|-------------------|
| {{< tableformatter >}}
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 {{< /tableformatter >}} | Alerting via e-mail |
| {{< tableformatter >}} 
- 95.211.70.193
- 178.162.179.193{{< /tableformatter >}} | Alerting via aangepaste integraties |