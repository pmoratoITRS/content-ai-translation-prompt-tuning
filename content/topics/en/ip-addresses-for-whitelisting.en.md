{
  "hero": {
    "title": "IP addresses for whitelisting"
  },
  "title": "IP Addresses for Whitelisting",
  "summary": "All of Uptrends' services, including the App portal, the www sites, the Uptrends API, and all other services related to Uptrends, Uptrends Infra and Uptrends Real User Monitoring, are served from multiple locations with multiple IP addresses.",
  "url": "/support/kb/account/ip-addresses-for-whitelisting",
  "translationKey": "https://www.uptrends.com/support/kb/account/ip-addresses-for-whitelisting"
}

{{< callout >}}
**Note:** Looking for the list of **checkpoint IP addresses** to whitelist, so your monitors can run correctly? Check out the complete list of [Uptrends' checkpoint IP addresses]({{< ref path="/checkpoints" lang="en" >}}).
{{< /callout >}}

Several services are used by Uptrends Synthetics, Uptrends Infra and Uptrends Real User Monitoring. These services include the App portal, the www sites, the Uptrends API, and more. They are served from multiple locations with multiple IP addresses. For example, which address the api.uptrends.com domain gets resolved to, can typically change every five minutes. This is true for all subdomains of uptrends.com.

{{< callout >}}
**Tip:** If you need to whitelist our applications, our advice is to whitelist the uptrends.com domains and subdomains (for HTTPS only, and for IPv4 and IPv6) as this would make you independent of any changes that occur to our IP addresses.
{{< /callout >}}

 Please whitelist these ranges of IPv6 addresses:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

The following tables show which specific IPv4/IPv6 addresses need to be whitelisted for certain services.

## Uptrends Synthetics
| URL                       | IP address or range                   | Used for                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| `api.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.211
- 95.211.70.211 {{< /tableformatter >}}  | API communication (Synthetics) |
| `app.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.213
- 95.211.70.213 {{< /tableformatter >}}  | Uptrends app |
| `customername.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.205
- 95.211.70.205 {{< /tableformatter >}} | {{< tableformatter >}} 
SP-initiated SSO
For more info, see [Single Sign-On Overview]({{< ref path="support/kb/account/settings/single-sign-on-overview#how-sso-users-log-in" lang="en" >}}), *How can SSO users log in?*, option 2. {{< /tableformatter >}} |
| `status.uptrends.com`       | {{< tableformatter >}} 
- 178.162.179.217
- 95.211.70.217  {{< /tableformatter >}} | Public status pages |
| `www.uptrends.com`          | {{< tableformatter >}}
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  {{< /tableformatter >}}| Downloads |

## Uptrends Infra
| URL                       | IP address or range                   | Used for                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  `api.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.210
- 95.211.70.210 {{< /tableformatter >}} |  API communication (Infra) | 
|  `app.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.208
- 95.211.70.208 {{< /tableformatter >}} |  Uptrends Infra app | 
|  `collector.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.209
- 95.211.70.209 {{< /tableformatter >}} |  {{< tableformatter >}}
Data sent by agents
The machine with the agent installed on it, needs access to this! {{< /tableformatter >}} |
| `www.uptrends.com` | {{< tableformatter >}} 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5{{< /tableformatter >}} |  Downloads, e.g. the agent updates | 

## Uptrends RUM

| URL                 | Used for                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `code.highcharts.com` | Necessary for displaying the maps on your RUM overview. The machine displaying the dashboard must have access to this domain. |

## Alerting

| IP address or range                                                        | Used for          |
|----------------------------------------------------------------------------|-------------------|
| {{< tableformatter >}}
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 {{< /tableformatter >}} | Alerting by email |
| {{< tableformatter >}} 
- 95.211.70.193
- 178.162.179.193{{< /tableformatter >}} | Alerting by custom integrations |