{
  "hero": {
    "title": "Get checkpoint data in JSON or XML format"
  },
  "title": "Get checkpoint data in JSON or XML format",
  "summary": "When using the Uptrends API to request checkpoint information you can get that information in different formats.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/get-checkpoint-data-in-json-and-xml-format",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/get-checkpoint-data-in-json-and-xml-format",
  "TableOfContents": false
}

JSON or XML downloads of checkpoint data are available through our API. To view the full documentation for the API, please see [this page](/support/kb/api).

You can use our API to request the lists of IPv4 or IPv6 addresses for all of Uptrends' checkpoints, including the upcoming addresses of changed or new checkpoints. Responses are available in both JSON and XML, depending on your `Accept` header. 

We also offer simple lists of [IPv4 addresses]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv4) and [IPv6 addresses]({{< AppUrl >}}/Download/DownloadCheckpointServerIpv6) to download.

All methods and links listed on this page yield a list of checkpoint IP addresses, which include **upcoming addresses** (as announced in our monthly checkpoint newsletter). 

#### For a list of IPv4 addresses:
Send a GET request to `https://api.uptrends.com/v4/Checkpoint/Server/Ipv4` with header `Accept: application/json`. No authentication is required. 

If you're using *curl*, an example would be: 
```
curl -X GET -H "accept: application/json" https://api.uptrends.com/v4/Checkpoint/Server/Ipv4
```

Replace *application/json* with *application/xml* if you need an XML response.

#### For a list of IPv6 addresses: 
Same as for IPv4, except the request should be sent to `https://api.uptrends.com/v4/Checkpoint/Server/Ipv6` instead.


{{< callout >}}
**Tip:** Instead of *curl* you can use a powershell Invoke-Webrequest.
{{< /callout >}}
