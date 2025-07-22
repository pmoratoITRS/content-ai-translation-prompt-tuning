{
  "title": "Easily convert Uptime monitors into API monitors on the API hub",
  "date": "2025-04-24",
  "url": "/changelog/april-2025-api-suggestions",
  "translationKey": "https://www.uptrends.com/changelog/april-2025-api-suggestions"
}

The [API hub](https://app.uptrends.com/Hubs/Api) now includes a feature that automatically scans your existing monitors and identifies those that can be converted into [API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}). If it detects any HTTP or HTTPS monitors that appear to check an API endpoint, it will offer the option to automatically create a new API monitor for you.

This functionality instantly upgrades any [Uptime monitor]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="en" >}}) into a fully configured API monitor without deleting or modifying the original monitor. You can freely undo the action at any time if needed. Also, there's no need to manually recreate everything from scratch, Uptrends handles all the setup, replicating the same settings from your existing monitors.

Once converted, you can review the configuration and enable it for use. For more information, refer to the [Multi-step API hub]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="en" >}}) knowledge base article.

![API suggestions tile](/img/content/scr-api-suggestions.min.png)