{
  "title": "Performance metrics for individual transaction steps",
  "date": "2024-02-07",
  "url": "/changelog/february-2024-performance-metrics-transaction-steps",
  "translationKey": "https://www.uptrends.com/changelog/february-2024-performance-metrics-transaction-steps"
}

Would you like to show the performance metrics [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) and [W3C navigation timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}}) of individual steps on a dashboard? Now you can activate the storage of data for this purpose inside the transaction step. Open your transaction and expand the step you want to report on, then enable the "Performance metrics" option in the step settings at the top. Note that this option is only available when you activate the Waterfall setting.

Once enabled, the performance metrics Core Web Vitals and W3C navigation timings are available and allow you to report them on a dashboard using the custom tile [Simple data chart]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#simple-data-list-chart" lang="en" >}}). The legend of the tile will indicate which graph belongs to which step, e.g. *First contentful paint (step 1)* will be shown in there. You can also hover over the graph to get more details. 
