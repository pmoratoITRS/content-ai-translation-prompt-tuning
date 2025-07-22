{
  "hero": {
    "title": "Concurrent Monitoring overview"
  },
  "title": "Concurrent Monitoring overview",
  "summary": "This is the start page for all info on Concurrent monitoring.",
  "url": "/support/kb/synthetic-monitoring/concurrent-monitoring/concurrent-monitoring-overview",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/concurrent-monitoring-overview",
  "tableofcontents": false,
  "sectionlist": false
}

In Uptrends you can monitor two ways - standard or concurrent.

Concurrent monitoring allows you to run a number of monitor checks for the same monitor at the same time, to more quickly and reliably reach a conclusion whether an error can be regarded a confirmed error. In this category, you can find detailed information on how to configure concurrent monitoring, and how to interpret its results for a more complete picture of your page's performance and uptime.

## How does concurrent monitoring help me

There are several upsides to concurrent monitoring compared to standard monitoring.

- **Faster error detection and alerting:** Error detection becomes more flexible with concurrent monitoring. Because you decide how many failed checks constitute an error, alerts can be sent out instantly the minute something goes wrong, rather than having to wait for a second test to confirm the error. This speeds up the process, and allows you to more efficiently tackle any issues that might arise.
- **More data:** Concurrent monitors operate at the same intervals as regular ones, but instead of executing a single check, they execute multiple simultaneously. The volume of individual checks increases several times over, which helps you more accurately determine relevant uptime and performance metrics.
- **Higher reliability:** Intermittent or localized errors can be difficult to detect. It's possible that issues might've passed by the time the second check comes around, or the second checkpoint doesn't experience the same issue. Concurrent monitors solve this by executing the checks simultaneously - meaning if a concurrent monitor reports an error, you can be even more certain that something is the matter.
