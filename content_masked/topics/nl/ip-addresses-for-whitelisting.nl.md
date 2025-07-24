{
  "hero": {
    "title": "IP-adressen voor whitelisting"
  },
  "title": "IP-adressen voor whitelisting",
  "summary": "Alle diensten van Uptrends, met inbegrip van de App-portal, de www-sites, de Uptrends API en alle andere diensten gerelateerd aan Uptrends, Uptrends Infra en Uptrends Real User Monitoring opereren vanaf meerdere locaties met meerdere IP-adressen.",
  "url": "[URL_BASE_TOPICS]account/ip-adressen-whitelisten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_27]
**Opmerking:** Zoekt u de lijst met **IP-adressen van controlestations** om te whitelisten zodat uw controleregels correct kunnen werken? Bekijk de volledige lijst van [Uptrends' controlestation IP-adressen]([LINK_URL_1]).
[SHORTCODE_28]

Uptrends Synthetics, Uptrends Infra en Uptrends Real User Monitoring maken gebruik van verschillende diensten. Deze diensten omvatten de App-portal, de www-sites, de Uptrends-API en meer. Ze opereren vanaf meerdere locaties met meerdere IP-adressen. Het adres waarnaar het domein api.uptrends.com wordt omgezet, kan bijvoorbeeld elke vijf minuten veranderen. Dit geldt voor alle subdomeinen van uptrends.com.

[SHORTCODE_29]
**Tip:** als u onze applicaties moet whitelisten, is ons advies om de uptrends.com-domeinen en -subdomeinen te whitelisten (alleen voor HTTPS, en voor IPv4 en IPv6), omdat u hierdoor niet afhankelijk bent van eventuele wijzigingen in onze IP-adressen.
[SHORTCODE_30]

 Zet deze ranges IPv6-adressen op de whitelist:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

De onderstaande tabellen tonen welke specifieke IPv4/IPv6-adressen op de whitelist moeten worden gezet voor bepaalde diensten.

## Uptrends Synthetics
| URL                       | IP-adres of -range                   | Gebruikt voor                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| [INLINE_CODE_1]          | [SHORTCODE_1] 
- 178.162.179.211
- 95.211.70.211 [SHORTCODE_2]  | API-communicatie (Synthetics) |
| [INLINE_CODE_2]          | [SHORTCODE_3] 
- 178.162.179.213
- 95.211.70.213 [SHORTCODE_4]  | Uptrends-app |
| [INLINE_CODE_3] | [SHORTCODE_5] 
- 178.162.179.205
- 95.211.70.205 [SHORTCODE_6] | [SHORTCODE_7] 
SP-geïnitieerde SSO
Zie voor meer informatie [Overzicht Single Sign-On]([LINK_URL_2]), *Hoe kunnen SSO-gebruikers inloggen?*, optie 2. [SHORTCODE_8] |
| [INLINE_CODE_4]       | [SHORTCODE_9] 
- 178.162.179.217
- 95.211.70.217  [SHORTCODE_10] | Publieke statuspagina's |
| [INLINE_CODE_5]          | [SHORTCODE_11]
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  [SHORTCODE_12]| Downloads |

## Uptrends Infra
| URL                       | IP-adres of -range                   | Gebruikt voor                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  [INLINE_CODE_6] | [SHORTCODE_13] 
- 178.162.179.210
- 95.211.70.210 [SHORTCODE_14] |  API-communicatie (Infra) | 
|  [INLINE_CODE_7] | [SHORTCODE_15] 
- 178.162.179.208
- 95.211.70.208 [SHORTCODE_16] |  Uptrends Infra-app | 
|  [INLINE_CODE_8] | [SHORTCODE_17] 
- 178.162.179.209
- 95.211.70.209 [SHORTCODE_18] |  [SHORTCODE_19]
Data verzonden door agents 
De machine waarop de agent is geïnstalleerd moet hier toegang toe hebben! [SHORTCODE_20] |
| [INLINE_CODE_9] | [SHORTCODE_21] 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5[SHORTCODE_22] |  Downloads, bijv. de agentupdates | 

## Uptrends RUM

| URL                 | Gebruikt voor                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_10] | Nodig om de kaarten op uw RUM-overzicht weer te geven. De machine die het dashboard weergeeft moet toegang hebben tot dit domein. |

## Alerting

| IP-adres of -range                                                        | Gebruikt voor            |
|----------------------------------------------------------------------------|-------------------|
| [SHORTCODE_23]
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 [SHORTCODE_24] | Alerting via e-mail |
| [SHORTCODE_25] 
- 95.211.70.193
- 178.162.179.193[SHORTCODE_26] | Alerting via aangepaste integraties |