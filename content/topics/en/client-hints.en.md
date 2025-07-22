{
  "hero": {
    "title": "Transition from User-Agent to Client hints"
  },
  "title": "Transition from User-Agent to Client hints",
  "summary": "Uptrends' Real User Monitoring uses a user agent request header for collecting user data. Google is transitioning this user agent string to client hints in upcoming versions of Chromium-based browsers.",
  "url": "/support/kb/rum/client-hints",
  "translationKey": "https://www.uptrends.com/support/kb/rum/client-hints"
}
## What is the User-Agent?
The User-Agent (UA) is an HTTP request header used to adapt the web page to the browser's specifications. When a web server gets a request for a web page from a client's browser, the browser will send a request header containing the user agent string. This will tell the server which browser type is on the other end. Before responding by sending the page, the web server will fine-tune the web page so the content will be adjusted for this specific browser type. 

The user agent string for a Chrome request header could look something like this:  
`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36`

When using Uptrends' [Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="en" >}}) a small script is added on the pages that you track with RUM. When your users access a web page with a RUM script, it'll record information on the browser, the platform it's running on, and its capabilities through the HTTP User-Agent request header. Once the page finishes loading, the script bundles the collected data with information about the visitor's browser and location and sends it to your Uptrends dashboard. 
## Why client hints and what is changing?
At the moment, Uptrends collects data about the user's browser, device operating systems, and versions via the user agent string. Google Chrome is now transitioning this string to User-Agent Client Hints (UA-CH) for all Chrome devices and Chromium-based browsers, including Microsoft Edge. With client hints, this info will be divided into smaller separate sections, no longer a lengthy string with data. 

There are two reasons Google is doing this; it's a better way to safeguard the web visitor’s privacy and a method to return the data in an easier-to-use format for developers.
## How does this impact RUM monitoring?
Uptrends will be prepared for this change and will update the script accordingly. There will be **no action required** on the client side.

The information collected with the current user agent will be gradually reduced. This means that in the future there might be less accurate user information available for monitoring. As soon as this changes and our script settings need to be adapted on the client's side, we'll inform you accordingly.

As a start for more background information about this transition and the phases of the UA reduction with Chromium M101, [look up User-Agent Reduction on The Chromium Projects](https://www.chromium.org/updates/ua-reduction/).

{{< callout >}} **Note**: If you’re concerned about the RUM script and user privacy our knowledge base article tells you more about [Real User Monitoring and privacy]({{< ref path="/support/kb/rum/rum-and-user-privacy" lang="en" >}}) {{< /callout >}}