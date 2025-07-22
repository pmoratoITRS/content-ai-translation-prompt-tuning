{
  "hero": {
    "title": "Monitoring websites other than the production server"
  },
  "title": "Monitoring websites other than the production server",
  "summary": "Do you need to monitor a website other than the production server, but they share the same domain name? You can do this with the proper setup using host headers.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/http-and-https/monitoring-websites-other-than-the-production-server",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

If you find yourself needing to monitor a website that shares a domain but is not your production server such as a backup or non-production site, you can do this with the proper monitor setup using host headers.

## What types of monitors work for this?

You can set up this type of monitoring using HTTP, HTTPS, and web service monitors. Unfortunately, this doesn't work with the Full Page Check or transaction monitoring.

## What you need

To set up monitors with host headers you need:

-   The URL the web server is listening to, and
-   The IP address of the server Uptrends needs to access directly.

## Setting up the monitor

To set up a monitor:

1.  Open an existing or new monitor

2.  Enter the IP Address into the **URL** field on the [SHORTCODE_1]Main[SHORTCODE_2] tab.

    ![]([LINK_URL_1])

3.  Switch to the [SHORTCODE_3]Advanced[SHORTCODE_4] tab.

4.  Enter "Host:" followed by the domain name in the **HTTP request headers** field (see below).  
    ![]([LINK_URL_2])

5.  Add a **Page content match** ([SHORTCODE_5]Error Conditions[SHORTCODE_6] tab) that contains content unique to the backup site that is not on the live site to ensure that you are accessing the correct site (optional).

6.  Complete your setup and click [SHORTCODE_7]Save[SHORTCODE_8].
