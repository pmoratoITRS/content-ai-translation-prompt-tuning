{
  "title": "New Core Web Vitals metric: Interaction to Next Paint (INP)",
  "date": "2024-06-12",
  "url": "/changelog/june-2024-new-cwv-inp",
  "translationKey": "https://www.uptrends.com/changelog/june-2024-new-cwv-inp"
}

Certain monitor types, such as [Full Page Checks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) and [Transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="en" >}}), can include [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) as part of the page load metrics for the checked URL. Core Web Vitals are Google's standardized set of metrics to measure user experience.

We've expanded the set of Core Web Vitals included in the monitor results to now also include Interaction to Next Paint (INP). This metric measures the page's responsiveness to user interactions, by measuring the time between user input and visual feedback on the page.