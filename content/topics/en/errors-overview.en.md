{
  "hero": {
    "title": "Errors overview"
  },
  "title": "Errors overview",
  "summary": "When a monitor check encounters a problem (as defined in error conditions), an error is signalled.",
  "url": "/support/kb/alerting/errors/errors-overview",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/errors-overview",
  "sectionlist": false,
  "tableofcontents": false
}

When something is wrong with your website or services, a monitor check will result in an error. You have to define the details of what 'something is wrong' means by setting up [error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) for your monitors.

Note that an error is not the same as an alert. Check out this [Alerting overview]({{< ref path="support/kb/alerting/alerting-overview" lang="en" >}}) to better understand the differences and how they relate to each other.

Errors are always double-checked to avoid wrong positives. Read more about this in the knowledge base article [Unconfirmed and confirmed errors]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}).

Once an error has occurred, it will appear on the *Error overview* dashboard. Navigate to {{< AppElement type="menuitem" >}} Dashboards > Synthetics > Error overview {{< /AppElement >}} to open this dashboard. There will be more info on an error in the [check details]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}}) related to the monitor check that caused the error.

Depending on the monitor and error situation, there will be an [error snapshot]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="en" >}}) that could help you in troubleshooting the situation.

There are many different types of errors. If you need info on the error you can look it up on the page [error types]({{< ref path="support/kb/alerting/errors/error-types" lang="en" >}}) by searching for the error code or other characteristics.

If there are errors that you think are not correct or should be removed from the list of errors, you have the option of [clearing errors]({{< ref path="support/kb/alerting/errors/clearing-errors" lang="en" >}}).
