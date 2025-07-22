{
  "hero": {
    "title": "Monitoring Web Services"
  },
  "title": "Monitoring Web Services",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/monitoring-web-services",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/monitoring-web-services"
}

{{< callout >}} **Note:** For API monitoring, the **Webservice HTTP and Webservice HTTPS** monitor types are no longer available for new users. Uptrends recommends using the [Multi-step API monitor]({{< ref path="support/kb/synthetic-monitoring/api-monitoring" lang="en" >}}) instead to maximize checking your API behaviors. {{< /callout >}}

Uptrends Webservice HTTP and HTTPS monitors are one of several [monitor types]({{< ref path="support/kb/basics/monitor-types" lang="en" >}}) that Uptrends offers. 

## Which Web Services are supported?

Uptrends supports *REST*, and *SOAP*, as well as any web services reachable through *HTTP*, *HTTPS.*

## How do these Web Services work with Uptrends?

-   We monitor that the web service response is HTTP 200 OK, and measure resolve time/connection time, download time, and total time, just like HTTP(S) monitors  
-   Web service monitoring also supports Basic Authentication, content checks, etc.  
-   Most web service monitors will use HTTP POST settings to POST data to the server as part of the web service call  
-   Typically SOAP services need an XML document (SOAP envelope) as POST data in the Request Body, as well as a specific HTTP header called SOAPAction.  
-   Some web services require setting HTTP headers for content type

**For example**:

-   \`Content-Type: application/json\` if the POST data is JSON data  
-   \`Content-Type: text/xml\` or application/xml if the POST data is XML (this is the default for webservice monitors, unlike regular HTTP(S) monitors)
