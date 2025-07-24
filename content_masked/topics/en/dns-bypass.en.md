{
  "hero": {
    "title": "DNS bypass"
  },
  "title": "DNS bypass",
  "summary": "Understand and learn how and if to set up a DNS bypass for a transaction or a Full Page Check type monitor. This bypass can be added to the 'Chrome' browser type. The DNS bypass will make sure the web page is resolved to a specified domain name or IP address.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/dns-bypass",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The DNS bypass makes sure the web page is resolved to a specified domain name or IP address. 

For example, you might need this to successfully monitor and check a website’s specific location, if the site is part of a Content Delivery Network (CDN) or load-balancing solution or in one of these [DNS bypass scenarios]([LINK_URL_1]). 

## Which monitors use DNS bypass

The Uptrends DNS bypass is implemented in the [Full Page Check]([LINK_URL_2]) monitor and in [transaction]([LINK_URL_3]) monitors.

For other types of monitors, like HTTPS, you can use host headers. Learn more about this similar function in our knowledge base article about [Monitoring websites other than the production server]([LINK_URL_4]).

## Why use a DNS bypass 
When Uptrends loads a URL into the browser for a Full Page Check or a transaction, the browser will ask a DNS service on an external server to translate the requested domain name to an IP address. It needs this address for the actual HTTP request. An FPC mimics exactly what a normal end user's browser would do. 

For monitoring or testing purposes, this may not be sufficient. What if you still want to use your company's URL, but need to target a specific server or IP address instead of relying on the regular DNS?

The DNS bypass lets you do just that. You can specify a fixed IP address (or another CNAME domain name) that should be used whenever the browser needs to connect to a particular domain name. It essentially bypasses or overrides the normal DNS system. In this way, it works very similar to the _hosts file_ on Windows or Linux.

## How to add a DNS bypass

1. Go to the monitor editor screen where you want to add a DNS bypass.
2. Click the [SHORTCODE_3] Advanced [SHORTCODE_4]tab.
3.  Scroll to the **Connection** and click [SHORTCODE_5] Add DNS bypass [SHORTCODE_6].
![DNS bypass]([LINK_URL_5])
4.  Enter the source domain and target domain. Please note that due to security reasons, not all target domains are supported.
5.  Click [SHORTCODE_7]Save[SHORTCODE_8] to confirm monitor changes.

 [SHORTCODE_1]
**Note**: You can use wildcards in the name of the _source_ domain, but not the target domain. E.g., you can create a rule *acc.example.com to www.example.com that redirect requests to server1-acc.example.com to www.example.com.
[SHORTCODE_2]

## When to use a DNS bypass  [ANCHOR_1]
When would you want to choose to bypass the DNS server used as default? These are scenarios when this could be useful or necessary: 
### DTAP / User Acceptance Testing (UAT) server
You would like to test and monitor the performance of web pages in a DTAP environment or on a User Acceptance Testing (UAT) server. These pages provide you with an actual view of what they will look like in production and therefore might require monitoring. With a DNS bypass, you tell Uptrends to monitor and check at the desired location.
### Different SSL configuration
Suppose your test environment needs to use the same SSL certificates as your production environment does. The certificate check web server address needs to be identical with the address specified in the certificate, otherwise the full page check will result in an error. 
### Preproduction website on an external domain
For example, your website is being redesigned by a third party. You would like to test and monitor the new web pages on their current location at the website developers' web server.
### Webpage on one node in a web cluster
Use a DNS bypass if you want to make sure that every individual node in the cluster is working properly and monitor them separately.
### Webpage on a CDN origin machine
For example, your website resides in a Content Delivery Network (CDN). It's possible that you would like to test and monitor the website on the origin server, not the cached ones on the CDN edge servers. Configure a DNS bypass to tell Uptrends to check directly at the origin server.
### Webpage on a specific CDN location 
If your website resides in a Content Delivery Network (CDN), it's possible that you would like to monitor one of the webpage instances cached on one of the edge servers in the delivery network. Configuring a DNS bypass will let Uptrends look directly at this server. But there is actually a preferable way to monitor those locations: set up an (FPC) monitor and let it perform checks from [checkpoints]([LINK_URL_6]) in the appropriate region. 
### Webpage or website within an internal network
When using private checkpoints within your network, an FPC could use an internal network route that results in the page's address being resolved through the internal server. If you prefer to test from the outside of your network, you can use a DNS bypass to change the network route. This might come into play when there are different pages and ways to log on internally and externally. 