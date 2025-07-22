{
  "hero": {
    "title": "Monitor alerting coverage"
  },
  "title": "Monitor alerting coverage",
  "summary": "Overview of all monitors with information about why alerting is covered or not for the monitor",
  "url": "/support/kb/alerting/monitor-alerting-coverage",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/monitor-alerting-coverage",
  "tableofcontents": false
}

The [Monitor alerting coverage]({{< AppUrl >}}/Report/AlertingCoverage) overview is a list of your monitors, showing if they are covered by alert definitions and giving you detailed information about why this may not be the case.

{{< callout >}} **Note**: the **Monitor alerting coverage** takes into account your permissions to give you a personalized view. It will show only alert definitions that you have the edit permission for. This means for the Uptrends account in general there could be a monitor that is covered by an alert definition and sending alerts, but still appears as not covered in the overview because you don't have access rights to the alert definition. {{< /callout >}}

If you have monitors that you expect to generate alerts, but they don't or they do while they should not, this is the place where you can start your troubleshooting.

To open the overview, go to {{< AppElement type="menuitem" >}}Alerting > Explore alerting{{< /AppElement >}}, then click the statistic "Production monitors covered by alerting".

![screenshot of statistic monitor alerting coverage](/img/content/scr-alerting_hub-statistic_monitor_coverage.min.png)

The *Monitor alerting coverage* appears and the monitors that are not covered by alerting are shown at the top of the list with a red shading.

![screenshot of overview monitor alerting coverage](/img/content/scr-monitor-alerting-coverage-overview.min.png)

Why are those monitors not covered?
There are a number of conditions for alerting coverage:

- The monitor itself is active.
- The alerting for the monitor is activated.
- There is at least one active alert definition attached to the monitor (directly or via a monitor group). 
- Within the active alert definition, at least one escalation level has to be active.

Check the list for a "No" or "inactive" (alert definitions) to find out which condition is not met. 
