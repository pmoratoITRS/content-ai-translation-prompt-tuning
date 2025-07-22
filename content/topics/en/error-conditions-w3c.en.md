{
  "hero": {
    "title": "Error conditions - W3C metric checks"
  },
  "title": "Error conditions - W3C metric checks",
  "summary": "Using thresholds on W3C metrics to trigger errors.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-w3c"
}

The World Wide Web Consortium (or W3C for short) is an international organization, involved in developing standards for the world wide web. As such, it has defined a standard for browsers and web applications to generate and display timing information regarding the loading of webpages. 

[Browser and transaction monitor types]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}) measure and report the [W3C navigation timing metrics]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="en" >}}). These metrics are reported in the monitor check details and you can set error conditions on them. Conditions for W3C metrics are part of the [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}).

Note that different monitor types offer different error conditions. Check the table in [Which error conditions are available?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) to find out which options are available for certain monitor types.

## Define error conditions based on the W3C metrics

To define error conditions that use the W3C navigation timing:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click on the monitor's name to edit it.
3. Open the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.
4. Expand the *Check W3C metrics* category by clicking the arrow in front.
 
   ![screenshot w3c metrics error condition](/img/content/scr_errorconditions-w3cmetrics.min.png)

5. Enable error conditions by ticking the check box and setting a value. Leave any metrics disabled that you don't want to assign to an error condition.
6. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button.

## The W3C metrics {id="w3c-metrics"}

The W3C metrics that are explained in the knowledge base article [W3C navigation timing metrics]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings#metrics" lang="en" >}}). The metrics correspond to the error conditions in the *Check W3C metrics* category. The only metric that is not present in that list of error conditions is the Load event. Find out in [Load event error condition]({{< ref path="#load-event" lang="en" >}}) below how to set an error condition for this one.

## Load event error condition {id="load-event"}

You might miss the W3C metric load event in the *Check W3C metrics* category of the error conditions. If you want to set an error condition on this metric, you can do so for [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) monitors. Do the following:

1. Open the monitor settings.
2. On the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab, select a **Browser type**.
3. On the {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tab in the *Measurement* section set the **Base load time on** to *W3C load event*.
4. On the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab set thresholds for the **Check page load time**.

The knowledge base article [Error conditions - Page load time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}}) has more information about setting limits for load times.
