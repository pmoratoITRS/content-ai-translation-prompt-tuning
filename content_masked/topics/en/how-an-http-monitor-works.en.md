{
  "hero": {
    "title": "How an HTTP monitor works"
  },
  "title": "How an HTTP monitor works",
  "summary": "Learn how Uptrends performs an HTTP(S) test and what the system does when it encounters and error.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/http-and-https/how-an-http-monitor-works",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Have you ever wondered what happens when Uptrends fires off an HTTP or HTTPS monitor check on your website? Many different scenarios can play out based on the circumstances; let's take a look at a few of them.

1.  Uptrends randomly picks one of your designated worldwide checkpoints for the test.
2.  Uptrends attempts to resolve the specified domain name.  
    [SHORTCODE_1]**Note:** You can specify the IP address instead of the domain name to skip the resolve portion of the test, but you won't receive an alert if your site has resolve issues.[SHORTCODE_2] 
3.  Using the IP address, Uptrends then attempts a low-level TCP connection over port 80 for HTTP, 443 for HTTPS, or the port you specified.
4.  After the basic test described in step 3, we open a new TCP connection to send the HTTP(S) request, and we wait for the response.

## What happens when Uptrends finds a problem?

Errors can happen during any step in the testing process, and depending on the error, Uptrends immediately tries a variety of things before issuing an alert. With most errors, Uptrends will attempt to get an error free connection using a different checkpoint. If Uptrends duplicates the error from a different checkpoint, Uptrends sounds the alarms. Uptrends does make a few exceptions based on specific errors.

### HTTPS failures

If using the HTTPS monitor type and the request fails (step 3), Uptrends may try several times using different security protocols before declaring the test a failed attempt.

### HTTP(S) with authentication information provided

For HTTP and HTTPS requests that include user authentication information, Uptrends may retry a failed test before declaring the attempt a failure.

### Network errors

If the HTTP or HTTPS request fails due to a networking problem, Uptrends attempts to perform a traceroute to the IP address. The traceroute sends a series of Ping (=ICMP) packets.
