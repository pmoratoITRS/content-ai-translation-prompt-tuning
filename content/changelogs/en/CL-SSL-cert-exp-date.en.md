{
  "title": "SSL certificate monitors now display certificate expiration date",
  "date": "2024-02-28",
  "url": "/changelog/february-2024-ssl-cert-monitor-expiration-date",
  "translationKey": "https://www.uptrends.com/changelog/february-2024-ssl-cert-monitor-expiration-date"
}

[SSL certificate monitors]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="en" >}}) can be used to check the validity of your SSL certificate. Additionally, they can be configured to generate errors when the checked certificate is due to expire in a configurable number of days. The monitor check result for SSL certificate monitors has now been expanded to also include the date the certificate is due to expire.

![SSL certificate monitor displaying expiration date](/img/content/scr-ssl-expiration-date_26022024.min.png)