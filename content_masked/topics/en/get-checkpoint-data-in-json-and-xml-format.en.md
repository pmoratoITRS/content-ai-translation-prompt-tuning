{
  "hero": {
    "title": "Get checkpoint data in JSON or XML format"
  },
  "title": "Get checkpoint data in JSON or XML format",
  "summary": "When using the Uptrends API to request checkpoint information you can get that information in different formats.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/get-checkpoint-data-in-json-and-xml-format",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

JSON or XML downloads of checkpoint data are available through our API. To view the full documentation for the API, please see [this page]([LINK_URL_1]).

You can use our API to request the lists of IPv4 or IPv6 addresses for all of Uptrends' checkpoints, including the upcoming addresses of changed or new checkpoints. Responses are available in both JSON and XML, depending on your [INLINE_CODE_1] header. 

We also offer simple lists of [IPv4 addresses]([LINK_URL_2]) and [IPv6 addresses]([LINK_URL_3]) to download.

All methods and links listed on this page yield a list of checkpoint IP addresses, which include **upcoming addresses** (as announced in our monthly checkpoint newsletter). 

#### For a list of IPv4 addresses:
Send a GET request to [INLINE_CODE_2] with header [INLINE_CODE_3]. No authentication is required. 

If you're using *curl*, an example would be: 
[CODE_BLOCK_1]

Replace *application/json* with *application/xml* if you need an XML response.

#### For a list of IPv6 addresses: 
Same as for IPv4, except the request should be sent to [INLINE_CODE_4] instead.


[SHORTCODE_1]
**Tip:** Instead of *curl* you can use a powershell Invoke-Webrequest.
[SHORTCODE_2]
