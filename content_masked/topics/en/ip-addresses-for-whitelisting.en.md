{
  "hero": {
    "title": "IP addresses for whitelisting"
  },
  "title": "IP Addresses for Whitelisting",
  "summary": "All of Uptrends' services, including the App portal, the www sites, the Uptrends API, and all other services related to Uptrends, Uptrends Infra and Uptrends Real User Monitoring, are served from multiple locations with multiple IP addresses.",
  "url": "[URL_BASE_TOPICS]account/ip-addresses-for-whitelisting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_27]
**Note:** Looking for the list of **checkpoint IP addresses** to whitelist, so your monitors can run correctly? Check out the complete list of [Uptrends' checkpoint IP addresses]([LINK_URL_1]).
[SHORTCODE_28]

Several services are used by Uptrends Synthetics, Uptrends Infra and Uptrends Real User Monitoring. These services include the App portal, the www sites, the Uptrends API, and more. They are served from multiple locations with multiple IP addresses. For example, which address the api.uptrends.com domain gets resolved to, can typically change every five minutes. This is true for all subdomains of uptrends.com.

[SHORTCODE_29]
**Tip:** If you need to whitelist our applications, our advice is to whitelist the uptrends.com domains and subdomains (for HTTPS only, and for IPv4 and IPv6) as this would make you independent of any changes that occur to our IP addresses.
[SHORTCODE_30]

 Please whitelist these ranges of IPv6 addresses:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

The following tables show which specific IPv4/IPv6 addresses need to be whitelisted for certain services.

## Uptrends Synthetics
| URL                       | IP address or range                   | Used for                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| [INLINE_CODE_1]          | [SHORTCODE_1] 
- 178.162.179.211
- 95.211.70.211 [SHORTCODE_2]  | API communication (Synthetics) |
| [INLINE_CODE_2]          | [SHORTCODE_3] 
- 178.162.179.213
- 95.211.70.213 [SHORTCODE_4]  | Uptrends app |
| [INLINE_CODE_3] | [SHORTCODE_5] 
- 178.162.179.205
- 95.211.70.205 [SHORTCODE_6] | [SHORTCODE_7] 
SP-initiated SSO
For more info, see [Single Sign-On Overview]([LINK_URL_2]), *How can SSO users log in?*, option 2. [SHORTCODE_8] |
| [INLINE_CODE_4]       | [SHORTCODE_9] 
- 178.162.179.217
- 95.211.70.217  [SHORTCODE_10] | Public status pages |
| [INLINE_CODE_5]          | [SHORTCODE_11]
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  [SHORTCODE_12]| Downloads |

## Uptrends Infra
| URL                       | IP address or range                   | Used for                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  [INLINE_CODE_6] | [SHORTCODE_13] 
- 178.162.179.210
- 95.211.70.210 [SHORTCODE_14] |  API communication (Infra) | 
|  [INLINE_CODE_7] | [SHORTCODE_15] 
- 178.162.179.208
- 95.211.70.208 [SHORTCODE_16] |  Uptrends Infra app | 
|  [INLINE_CODE_8] | [SHORTCODE_17] 
- 178.162.179.209
- 95.211.70.209 [SHORTCODE_18] |  [SHORTCODE_19]
Data sent by agents
The machine with the agent installed on it, needs access to this! [SHORTCODE_20] |
| [INLINE_CODE_9] | [SHORTCODE_21] 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5[SHORTCODE_22] |  Downloads, e.g. the agent updates | 

## Uptrends RUM

| URL                 | Used for                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_10] | Necessary for displaying the maps on your RUM overview. The machine displaying the dashboard must have access to this domain. |

## Alerting

| IP address or range                                                        | Used for          |
|----------------------------------------------------------------------------|-------------------|
| [SHORTCODE_23]
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 [SHORTCODE_24] | Alerting by email |
| [SHORTCODE_25] 
- 95.211.70.193
- 178.162.179.193[SHORTCODE_26] | Alerting by custom integrations |