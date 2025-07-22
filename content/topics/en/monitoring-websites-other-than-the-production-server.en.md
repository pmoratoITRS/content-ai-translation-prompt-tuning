{
  "hero": {
    "title": "Monitoring websites other than the production server"
  },
  "title": "Monitoring websites other than the production server",
  "summary": "Do you need to monitor a website other than the production server, but they share the same domain name? You can do this with the proper setup using host headers.",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/monitoring-websites-other-than-the-production-server",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/monitoring-websites-other-than-the-production-server"
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

2.  Enter the IP Address into the **URL** field on the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab.

    ![](/img/content/scr-monitor-url-host-header.min.png)

3.  Switch to the {{< AppElement type="tab" >}}Advanced{{< /AppElement >}} tab.

4.  Enter "Host:" followed by the domain name in the **HTTP request headers** field (see below).  
    ![](/img/content/a18cdb82-fbb6-45c4-a2f2-f4031a33d34e.png)

5.  Add a **Page content match** ({{< AppElement type="tab" >}}Error Conditions{{< /AppElement >}} tab) that contains content unique to the backup site that is not on the live site to ensure that you are accessing the correct site (optional).

6.  Complete your setup and click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.
