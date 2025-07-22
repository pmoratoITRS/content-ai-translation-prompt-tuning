{
  "hero": {
    "title": "Unconfirmed and confirmed errors"
  },
  "title": "Unconfirmed and Confirmed Errors",
  "summary": "What are unconfirmed and confirmed errors and how do they count for the downtime that is calculated?",
  "url": "/support/kb/alerting/errors/unconfirmed-and-confirmed-errors",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/unconfirmed-and-confirmed-errors"
}

One of the highlights of using Uptrends for server and website monitoring is its ability to keep your team apprised of downtime or performance related events. But what exactly makes an error unconfirmed or confirmed?

## The difference between an unconfirmed/confirmed errors

An **unconfirmed error** is an error that has been reported after checking a monitor from one checkpoint location, but has yet to be verified by a second checkpoint location.

A **confirmed error** is an error that has been verified by two checkpoint locations.

This **downtime double-check** helps to prevent the creation of false alerts. However, if the double-check does not confirm an error, it is assumed that the first unconfirmed error was a temporary problem.

{{< callout >}}
**Note**: Unconfirmed errors are displayed in yellow, within the Monitor Log dashboard report. Confirmed errors are displayed in red. No errors will be displayed in green.
{{< /callout >}}

## How errors contribute towards downtime and alerting

It is important to note that the Uptrends service only contributes confirmed (double-checked) errors to the downtime alerting system.

To control when an alert should be sent, you can edit the default Alert Definition, or create your own. To learn more about Alert Definitions, we recommend reading the appropriate [Alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}) article.
