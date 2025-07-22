{
  "hero": {
    "title": "Error conditions - Availability"
  },
  "title": "Error conditions - Availability",
  "summary": "An overview of the available error conditions for the category *Availability*. ",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-page-availability"
}

The error conditions in the monitor setup are used to define situations for which you want to signal an error. Please read the knowledge base article [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) for further general information and how to [Configure an error condition]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#configure-error-condition" lang="en" >}}). 

The error condition **Availability** will check the page (HTTP/S or web service monitor), the site (transactions), or resource (other monitors) availability. It may have different options, depending on the monitor type. Check the table at [Which error conditions are available?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) to find out more.

For example, the availability check for an HTTP(S) or Webservice HTTP(S) monitor would look like this:

![screenshot page availability error condition](/img/content/scr_errorconditions-page-availability.min.png)

## General availability check

By default, all monitor types check the availability of the monitored website, page, or resource. 

Where applicable, e.g. for an an HTTP(S) or Webservice HTTP(S) monitor, any response status code that is 400 or above will result in an error. For other monitor types, e.g. DNS, (S)FTP, mail servers, or database servers, there will be no HTTP response status code but a check on whether the server or service can be reached.

## HTTP status code check

For monitor types that respond with an HTTP status code the option of checking for a specific status code is available.

Sometimes you expect an error code or another code other than a success. For example, if you have a redirect on an old web page to a new page, you may want to know if the redirect is failing. If you want to check for a certain response, select the option **Verify the response HTTP status code matches ...** and select a status code from the list.

For a complete list of status codes visit the Internet Assigned Numbers Authority's (IANA) [HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml).