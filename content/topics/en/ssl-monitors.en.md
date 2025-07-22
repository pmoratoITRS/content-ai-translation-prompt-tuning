{
  "hero": {
    "title": "SSL certificate monitors"
  },
  "title": "SSL certificate monitors",
  "summary": "Uptrends advanced SSL monitoring keeps track of your SSL certificates and monitors for expiration dates and changes to your certificate that could indicate a security breach. ",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors",
  "translationKey": "https://www.uptrends.com/support/kb/ssl-monitors",
  "tableofcontents": true
}

Your SSL (Secure Socket Layers) certificate is more important than most people know. Research has shown that most users will take the browser's advice and leave your site for a competitor if they get a warning about an invalid or expired SSL certificate or certificate chain. SSL errors happen to everyone; even Google has fallen victim to an expired certificate. As staff and responsibilities change, SSL certificates fall off the radar. With Uptrends, you can keep your SSL information in one place and receive alerts about expiration dates and changes to your certificate.

## What is monitored?

Besides setting up the expiration of your SSL certificate, you can also track any of the certificate values:

- Common name
- Organization
- Organizational unit
- Serial number
- Fingerprint
- Issued by common name
- Issued by organization
- Issued by organizational unit

If any of those values change on your site's certificate (a possible symptom of a hack), Uptrends issues an alert.

#### Alert and error messages

Here are the messages you'll see once your SSL certificate is about to expire:

- **SSL certificate will expire soon** — This is a generic error message based on the number of days you set in the {{< AppElement type="menuitem" >}} Expiration warning days {{< /AppElement >}} field under the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab of your SSL monitor. When the date of your certificate meets the value set in this field, you'll see this message under the *Errors overview* dashboard or in places where errors are grouped together.

Under your SSL monitor > *Monitor logs* and *Alert history* dashboard, you'll find more specific alert messages showing the number of days left before your certificate expires:

- **SSL certificate will expire in 1 day**
- **SSL certificate will expire in less than 1 day**
- **SSL certificate will expire in *n* days** — The *n* represents the actual number of days in numerical format for when the SSL certificate expires. If, for example, there are only *45* days left, the alert message will show as *SSL certificate will expire in 45 days*.

These messages are also shown in the *Check details* screen when you perform a {{< AppElement type="buttonSecondary" >}} Test Now {{< /AppElement >}} action on SSL monitors.

## Set up an SSL certificate monitor

Setting up an SSL certificate monitor is similar to configuring a web page monitor. If you need assistance with the basic steps of monitor setup, refer to the knowledge base article on [Adding a monitor]({{< ref path="support/kb/basics/adding-monitors" lang="en" >}}).

To set up an SSL certificate monitor:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}, and then click the {{< AppElement type="iconAdd" >}}{{< /AppElement >}} button.
2. In the *Select a monitor type* pop-up dialog, choose *SSL Certificate*, then click the {{< AppElement type="button" >}} Choose {{< /AppElement >}} button.  
3. Set up your [main monitor settings]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings" lang="en" >}}).
4. In the *URL field*, enter the URL or browser address you want to monitor.
5. Fill out the SSL Certificate section appropriately, information should be readily available from your SSL Certificate issuer.

![SSL Certificate details section](/img/content/scr_ssl-certificate-details.min.png)

6. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to apply changes.

Uptrends will now monitor your website's SSL certificate details and alert you when the conditions specified in the {{< AppElement type="tab" >}}Error conditions{{< /AppElement >}} and {{< AppElement type="tab" >}}Advanced{{< /AppElement >}} tabs are met. For more information, please refer to the knowledge base article on [monitor settings]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="en" >}}).