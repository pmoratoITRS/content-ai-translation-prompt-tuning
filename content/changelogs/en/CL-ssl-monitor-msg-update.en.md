{
  "title": "SSL monitor error messages are now more specific",
  "date": "2024-09-25",
  "url": "/changelog/september-2024-ssl-monitor-error-messages",
  "translationKey": "https://www.uptrends.com/changelog/september-2024-ssl-monitor-error-messages"
}

We've now included the remaining days before your SSL certificate expires in the error descriptions of SSL monitors. You can now see specific alert messages under SSL monitors > *Monitor logs* and *Alert logs* dashboard;

- *SSL certificate will expire in 1 day*
- *SSL certificate will expire in less than 1 day*
- *SSL certificate will expire in **x** days*

Likewise, the generic SSL error message: *"SSL certificate will expire soon"* can still be found in the *Errors overview* dashboard or in places where errors are grouped together. Explore the [SSL certificate knowledge base article]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="en" >}}) to know more!
