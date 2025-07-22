{
  "hero": {
    "title": "Browser types and their metrics"
  },
  "title": "Browser types and their metrics",
  "summary": "Which browser types are available for the Full Page Check?",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/browser-types",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/browser-types",
  "tableofcontents": false
}

You can configure a Full Page Check (FPC) to use one of several available browsers. The **Browser type** setting can be found in both the {{< AppElement type="tab" >}} Main {{< /AppElement >}} and {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tabs of the monitor settings. The following browsers are available:

- Chrome
- Microsoft Edge

Uptrends keeps the browsers up to date on the [checkpoints]({{< ref path="/checkpoints" lang="en" >}}), so your check will typically be executed in the latest version available for the selected browser.

{{< callout >}}
**Note:** If you want to monitor how your website behaves on a mobile device, you have to adjust the [user agent]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="en" >}}) on the monitor's {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tab.
{{< /callout >}}

## Metrics {id="chrome-extra-metrics"}

To know more about the available metrics for a browser monitor, refer to the [Metrics and features]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="en" >}}) knowledge base article.
