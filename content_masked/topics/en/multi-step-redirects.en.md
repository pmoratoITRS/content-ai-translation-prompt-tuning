{
  "hero": {
    "title": "Multi-step monitoring - Handling redirects"
  },
  "title": "Multi-step monitoring",
  "summary": "Learn how to work with redirects within your Multi-step API Monitors.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-redirects",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

HTTP redirects allow a web server to forward the caller (the HTTP client) to a different URL than was originally requested. This happens by returning a status code in the 3xx range, along with the new URL that should be called by the client. This new URL is returned in the HTTP Response header named Location.

Initial request and response:

[INLINE_CODE_1] [INLINE_CODE_2]

Request to the new location:

[INLINE_CODE_3] [INLINE_CODE_4]

## Checking redirects in a multi-step monitor

In a [multi-step API monitor]([LINK_URL_1]), redirects like this are followed automatically. You don't have to worry about the mechanics of how your API or web application handles incoming requests: you can focus on checking the result. This means that if a step requests a URL that is redirected by your server, we will execute the second request as part of that same step, and you can work with the result of the second request as if there was no redirect in the middle. If the second request also returns a redirect, we will follow that one as well, up to a limit of 50 consecutive redirects. In each case, you'll get the response content and headers that correspond with the last request.

In some cases, this automatic behavior of following redirects may not be what you need. For example, if you want to monitor the redirect behavior itself (checking the status code, the content of the Location header, whether a cookie is returned, or any other value), you want to get to those values rather than executing the second request right away.

If you add an assertion and specify that the HTTP status code is equal to 301, 302, 303, 307 or 308, we will not follow that redirect. Instead, you'll get direct access to that response. You can then use additional assertions and variables in the same step to work with that response. For example:

### Assertions

[SHORTCODE_1]Status code[SHORTCODE_2] [SHORTCODE_3]Is equal to[SHORTCODE_4] [SHORTCODE_5]302[SHORTCODE_6] 

[SHORTCODE_7]Response header[SHORTCODE_8] [SHORTCODE_9]Location[SHORTCODE_10] [SHORTCODE_11]Contains[SHORTCODE_12] [SHORTCODE_13]productId=P12345[SHORTCODE_14] 

![MSA redirect]([LINK_URL_2])

## Following the redirect manually

Since we're working in a multi-step setup, we can still go ahead and execute the redirect manually after checking the redirect and optionally capturing values from it. Simply add another step and specify the new location as the URL.

To do this, you can capture the value of the Location header, store it in a variable (say, [SHORTCODE_15]{{location-value}}[SHORTCODE_16]) and use that variable in the URL of the nexts step. This can be a bit tricky though: the value of the Location header is likely to be a relative URL, i.e. without a domain name in it. If you're setting this up manually, you'll need to compensate this by including the domain name in the new URL:

[INLINE_CODE_5]

This will work, but we can make it easier for you: whenever we detect a Location header in an HTTP response, we'll convert that value into an absolute URL (including the domain name of the original request) and put it in an automatic variable called [SHORTCODE_17][SYSTEM_VAR_1][SHORTCODE_18]. That variable is ready to be used in the next step:

[INLINE_CODE_6]

## Capturing parameters from a redirect URL

In some scenarios, you may not want to follow the redirect URL at all, but capture a parameter value from it instead. Suppose we received this response header in the original response:

[INLINE_CODE_7]

What if you don't really want to follow this URL, but use that code parameter value that was returned by your server? No problem: we're automatically capturing URL parameters we find in Location headers, and put them in automatic variables you can use somewhere else. The naming scheme for these automatic variables is [SHORTCODE_19][SYSTEM_VAR_3][SHORTCODE_20]. In this case, you'll have access to [SHORTCODE_21][SYSTEM_VAR_4][SHORTCODE_22] and [SHORTCODE_23][SYSTEM_VAR_5][SHORTCODE_24].
