{
  "hero": {
    "title": "Check details"
  },
  "title": "Check details",
  "summary": "The results of a monitor check are presented in the check details. The available information depends on the monitor type.",
  "url": "/support/kb/synthetic-monitoring/monitoring-results/check-details",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/check-details"
}

The information that is collected around a monitor check is displayed in so-called "check details". These consist of the basic information if the check went fine (OK) or there was an error detected (based on your [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}})). More detailed information on the check itself and the outcome are present as well and can help you in troubleshooting the cause of an error.

## What is included in the check details?

The information in the check details heavily depends on the monitor type. It can be as simple as a status code for an HTTP(S) monitor. More complex monitors may contain screenshots for a Full Page Check or results for each step in a transaction or Multi-step API monitor, see the two examples below.

Check details ("OK") for an HTTPS monitor:

![screenshot check details https monitor](/img/content/scr_check-details-https-monitor.min.png)

Check details for a transaction monitor that returned an error:

![screenshot check details transaction monitor](/img/content/scr_check-details-transaction-monitor-041024.min.png)

## Where to find the check details?

The check details are available in several places.

If you run a monitor check by using the {{< AppElement type="buttonSecondary" >}} Test now {{< /AppElement >}} button, you will get a popup with the check details.

Several dashboards will have a list of checks. Clicking on an individual error or check will bring up the check details. You can find the errors or checks here:

- Dashboard in {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Errors overview {{< /AppElement >}} 
- Dashboard in {{< AppElement type="menuitem" >}} Monitoring > Status details {{< /AppElement >}} 
- Dashboard in {{< AppElement type="menuitem" >}} Monitoring > Monitor log {{< /AppElement >}} 
- Tile *Last check details*, a [custom report tile]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles#last-check-details" lang="en" >}}) you can add to your [custom dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-dashboards" lang="en" >}})
