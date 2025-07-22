{
  "hero": {
    "title": "Alerting overview"
  },
  "title": "Alerting overview",
  "summary": "How alerting works. The monitor check will generate an error, which leads to an alert, which triggers a message via an alert definition.",
  "url": "/support/kb/alerting/alerting-overview",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alerting-overview"
}

In a real-world setting, websites, servers, and any other systems are expected to run around the clock and provide uninterrupted service availability. In scenarios like this, alerting is a powerful tool to immediately keep you updated  whenever an issue or something unusual occurs in your system. Alerting ensures that your system is always up and running and helps minimize system downtime.

One of the main features of the Uptrends monitoring service is **Alerting**. When errors are detected in your monitors, you'll be notified by alert messages right away. The illustration below shows the summary of the Uptrends alert workflow:

![Alert workflow illustration](/img/content/64eb1efd-9506-4cfb-ac6d-a69115ec3b68.png)

In simple terms, an alert is created whenever these four definitions exist: *Monitor check, Error condition, Alert definition and Integration*. Once you created and defined your monitor and its settings, your monitor runs several checks as defined in the monitor settings. If a monitor check results in a [confirmed error]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}), that's when an alert is generated in the Uptrends web application. This alert then triggers, sending a message to an operator or a third party application.


In this article, we'll cover the step-by-step flow of how a monitor check turns into a message.

## Monitor checks

It all starts with the monitor checks that run at the interval defined by you. The monitor checks include some standard checks which depend on the monitor type, like availability. In addition you can define your own error conditions, like a load time limit or the page content match.

![Monitor checks settings](/img/content/scr_alerting-monitor-checks.min.png)

The knowledge base article [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en">}}) explains how to configure the error conditions in more detail.

An error is signaled once the monitor check finds an issue due to a standard check failing or if an error condition is met.

## Errors

All errors are shown in the **Errors overview** section. You can filter which types of errors you want to see (*OK, unconfirmed, confirmed*) and you can set which time periods you want to look at. You can check the [dashboards knowledge base article]({{< ref path="/support/kb/dashboards-and-reporting/dashboards" lang="en" >}}) to know more about filtering and customizing dashboard settings.

The following Errors overview example shows unconfirmed (marked yellow) and confirmed (marked red) errors:

![Errors overview dashboard](/img/content/scr_errors-overview-dashboard.min.png)

As shown in the illustration, the first occurrence of an error is called an unconfirmed error. This could just be a temporary situation or a problem with the checkpoint. Therefore, a second monitor check is done from another checkpoint. If any errors are reported, the result is a confirmed error, which generates an alert.

More information on this principle can be found in the article [Unconfirmed and confirmed errors]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}).

### Sequences of errors

There are different scenarios for a sequence of errors, which are shown in the image below:

-   An unconfirmed error followed by an OK result. This will not lead to an alert.
-   An unconfirmed error followed by a confirmed error, then an OK result. This will result in an alert, if your alert definition is set to "generate an alert when 1 or more errors have occurred".
-   A number (n) of unconfirmed/confirmed errors occur in a row. This will result in an alert, if your alert definition is set to "generate an alert when n or more errors have occurred". Alternatively you can set a time limit for errors. If the sequence of errors reaches that time limit, e.g. the errors occur for more than 5 minutes, an alert is created.

![](/img/content/b4bc1e4c-3fd5-4dff-a4d4-2f7ec14b2534.png)

## Alerts

The alert definition controls the generation of alerts for different escalation levels. The escalation levels are used to create alerts in stages and to notify the selected operators in the right way, taking into account the urgency of the problem and the increasing urgency, if the problem persists.

For each level, you have to set whether an alert is created, which operator (groups) will be notified, when a time limit is reached (errors occur for more than x minutes) or an alert is created after a number of error occurrences (one or more errors have occurred). All of the errors have to be confirmed errors. Unconfirmed errors are not taken into account for these conditions.

In addition to the original alert, you can generate one or more reminder alerts. You have to set the maximum number of reminders and the interval at which they have to be created. This option is available for each escalation level individually.

The knowledge base articles [Creating alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}) and [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}) contain more information on alert definitions.

Note that, the monitor has to have *Generate alerts* turned on in order to generate alerts at all.

When the error was resolved (meaning that the same check has returned OK instead of an error) a recovery-alert (OK alert) is created.

All the alerts are shown in the **Alert history**. Error alerts are marked red, while OK alerts are marked green. As long as the error is not resolved and no recovery alert is generated, the alert remains an active alert. The active alerts are listed on the **Current alert status** dashboard.

![](/img/content/scr_alert-history-dashboard.min.png)

Looking for a specific **Alert definition** you've created? You can use Uptrends' [Search]({{< ref path="/support/kb/basics/user-interface/search" lang="en" >}}) to quickly find it.

## Messages

With the **Alert history** dashboard, you can monitor your alerts from time to time and see them in just one place. However, it's also convenient to receive real-time notifications about your alert situation without going to the web application itself. Uptrends features [Integrations]({{< ref path="/support/kb/alerting/integrations" lang="en" >}}), which allows you to have a full range of options for sending alert messages to you, to people, or to third-party systems and get notified right away.

In order to send a message when an alert is generated, you need to set up your [Alert definition]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="en" >}}) first, then choose the type of [integration]({{< ref path="/support/kb/alerting/integrations" lang="en" >}}) you prefer per escalation level. Once done, you can easily receive updates based on your preferred integration.

### Testing messages

Since you want to receive alert notifications as soon as possible, the first step is to ensure that the sending of alert messages actually works. Check out this knowledge base article to know how to [test alert messages]({{< ref path="support/kb/alerting/testing-alert-configurations" lang="en" >}}) for different integrations.