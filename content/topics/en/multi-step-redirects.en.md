{
  "hero": {
    "title": "Multi-step monitoring - Handling redirects"
  },
  "title": "Multi-step monitoring",
  "summary": "Learn how to work with redirects within your Multi-step API Monitors.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-redirects"
}

HTTP redirects allow a web server to forward the caller (the HTTP client) to a different URL than was originally requested. This happens by returning a status code in the 3xx range, along with the new URL that should be called by the client. This new URL is returned in the HTTP Response header named Location.

Initial request and response:

`GET /p/P12345 HTTP/1.1` `HTTP/1.1 302 Redirect  Location: /ProductInfo?productId=P12345`

Request to the new location:

`GET /ProductInfo?productId=P12345 HTTP/1.1` `HTTP/1.1 200 OK`

## Checking redirects in a multi-step monitor

In a [multi-step API monitor](/support/kb/synthetic-monitoring/api-monitoring/multi-step), redirects like this are followed automatically. You don't have to worry about the mechanics of how your API or web application handles incoming requests: you can focus on checking the result. This means that if a step requests a URL that is redirected by your server, we will execute the second request as part of that same step, and you can work with the result of the second request as if there was no redirect in the middle. If the second request also returns a redirect, we will follow that one as well, up to a limit of 50 consecutive redirects. In each case, you'll get the response content and headers that correspond with the last request.

In some cases, this automatic behavior of following redirects may not be what you need. For example, if you want to monitor the redirect behavior itself (checking the status code, the content of the Location header, whether a cookie is returned, or any other value), you want to get to those values rather than executing the second request right away.

If you add an assertion and specify that the HTTP status code is equal to 301, 302, 303, 307 or 308, we will not follow that redirect. Instead, you'll get direct access to that response. You can then use additional assertions and variables in the same step to work with that response. For example:

### Assertions

{{< Code/Symbol type="source" >}}Status code{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Is equal to{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}302{{< /Code/Symbol >}} 

{{< Code/Symbol type="source" >}}Response header{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Location{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Contains{{< /Code/Symbol >}} {{< Code/Symbol type="target" >}}productId=P12345{{< /Code/Symbol >}} 

![MSA redirect](/img/content/scr-MSA-redirect-check.min.png)

## Following the redirect manually

Since we're working in a multi-step setup, we can still go ahead and execute the redirect manually after checking the redirect and optionally capturing values from it. Simply add another step and specify the new location as the URL.

To do this, you can capture the value of the Location header, store it in a variable (say, {{< Code/Symbol type="variable" >}}{{location-value}}{{< /Code/Symbol >}}) and use that variable in the URL of the nexts step. This can be a bit tricky though: the value of the Location header is likely to be a relative URL, i.e. without a domain name in it. If you're setting this up manually, you'll need to compensate this by including the domain name in the new URL:

`GET https://myapi.example.com/{{location-value}}`

This will work, but we can make it easier for you: whenever we detect a Location header in an HTTP response, we'll convert that value into an absolute URL (including the domain name of the original request) and put it in an automatic variable called {{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}}. That variable is ready to be used in the next step:

`GET {{@RedirectUrl}}`

## Capturing parameters from a redirect URL

In some scenarios, you may not want to follow the redirect URL at all, but capture a parameter value from it instead. Suppose we received this response header in the original response:

`Location: https://your.clientapp.com/auth?clientId=12345&code=SGV5LCB5b3UgZm91bmQgdGhpcyEgV2VsbCBkb25lIQ==`

What if you don't really want to follow this URL, but use that code parameter value that was returned by your server? No problem: we're automatically capturing URL parameters we find in Location headers, and put them in automatic variables you can use somewhere else. The naming scheme for these automatic variables is {{< Code/Symbol type="variable" >}}{{@RedirectUrl.&lt;parameter-name&gt;}}{{< /Code/Symbol >}}. In this case, you'll have access to {{< Code/Symbol type="variable" >}}{{@RedirectUrl.clientId}}{{< /Code/Symbol >}} and {{< Code/Symbol type="variable" >}}{{@RedirectUrl.code}}{{< /Code/Symbol >}}.
