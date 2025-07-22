{
  "title": "Custom metrics now show the minimum and maximum metric values",
  "date": "2025-01-29",
  "url": "/changelog/january-2025-custom-metrics-minimum-maximum-metric-values",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-custom-metrics-minimum-maximum-metric-values"
}

The [Custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="en" >}}) in [Multi-step API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}) (MSA) let you create custom metric variables to collect and store numerical data from an API response step.

These metric variables can be displayed through a [Custom metrics chart]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="en" >}}), showing the metric's trends over time.  Before, the chart only shows the custom metric's average value (high points) as a data point. Now, the custom metric's minimum and maximum values are also displayed. Note that existing MSA monitors with custom metrics data from 1 November 2024 onward will be reflected in your **Custom metrics chart**.

![Custom metrics chart with minimum and maximum metric values](/img/content/scr-custom-metric-min-max-values.min.png)