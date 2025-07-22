{
  "hero": {
    "title": "Monitoring results overview"
  },
  "title": "Monitoring results overview",
  "url": "/support/kb/synthetic-monitoring/monitoring-results/monitoring-results-overview",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/monitoring-results-overview",
  "sectionlist": false
}

When running monitor checks there will be different types of results or reports depending on the type of monitor and your settings. The [check details]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}}) hold a lot of results and they exist for all monitors. However, some results may apply to a number of monitor types only, e.g. the waterfall exists for Full Page Check monitors as well as transaction monitors, but not in other monitor types.

## Metrics

With the **Core Web Vitals** and **W3C navigation timings** you have two sets of metrics that are based on international standards. The metrics allow you to better understand the performance of your website and find out what needs to be improved to score higher in search engine rankings.

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}})
- [W3C navigation timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}})

Note that you can add these metrics to a custom dashboard by adding a custom report tile of the type [Simple data list / chart]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="en" >}}).

## Waterfall

The waterfall chart is a visualization of your monitoring results in a bar chart and shows in detail when page elements are loaded and how long it took. It is a good tool to do troubleshooting and find out what slows down the loading of a page. Check out the knowledge base articles about waterfalls:

- [Waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}})
- [Waterfall timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="en" >}})
- [Interpreting the results of the waterfall report]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="en" >}})

## Further troubleshooting

The results of a monitor check are collected in the check details. They can be the starting point for troubleshooting.

- [Check details]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}})

In addition the check results contain the page source (HTML source) and the console log (from loading the page). This information is available in check results of transactions and Full Page Check monitors. You may have to switch on the feature, please check the knowledge base article below for details.

- [Page source and console log]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="en" >}})

The waterfall chart gives you a good insight into the loading of your page elements. However, it may be difficult to imagine what is happening there step-by-step. The timeline screenshots may help you to understand what the page looks like at different steps in the loading process.

- [Timeline screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="en" >}})
