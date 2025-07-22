{
  "hero": {
    "title": "Error conditions overview"
  },
  "title": "Error conditions overview",
  "summary": "What are error conditions and how to use them? ",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
  "tableofcontents": true,
  "sectionlist": false
}

Error conditions play a major role in generating your monitor alerts. Setting up an error condition is the first step of the [alert and error flow cycle]({{< ref path="support/kb/alerting/alerting-overview" lang="en" >}}) that lets you receive alert messages.

An **Error condition** lets you define a set of criteria to inform your monitor of any errors on your website, web service, or server. It serves as your monitor's basis for deciding which website behaviors result in an error and which don't.

If, for example, you want to ensure that your website takes less than three seconds to load, you can set an error condition and specify thresholds for the page load time. Similarly, if you want to check if your website's contents, plugins, or scripts load correctly, you can set specific error conditions for each.

Once any error condition is met, an error is generated, triggering an alert. If alerting is configured, you'll be notified by an alert message right away.

## Error conditions for monitor types {id="error-conditions-by-category"}

The {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab lets you set different error conditions available for each monitor type. Note that the availability of error conditions may vary depending on the monitor's category and which data it collects:

![screenshot error conditions monitor setup](/img/content/scr_monitor-setup-errorconditions.min.png)

### Uptime monitor

The following error conditions are available for [Uptime monitor]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="en" >}}) types:

| Monitor type | Error conditions | 
|--|--|
| HTTPS, Webservice HTTP and HTTPS | {{< tableformatter >}} 
- [Check page availability]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="en" >}}) 
- [Check page content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="en" >}})
- [Check page load time]({{< ref path="" lang="en" >}})
- [Check resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
{{< /tableformatter >}} |
| DNS, SSL, SFTP, FTP | {{< tableformatter >}}
- [Check  resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
- [Check total running time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}})
{{< /tableformatter >}} |
| SMTP, POP3, IMAP | {{< tableformatter >}}
- [Check  resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
- [Check total running time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}})
{{< /tableformatter >}} |
| Microsoft SQL servers,  MySQL | {{< tableformatter >}}
- [Check  resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
- [Check total running time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}})
{{< /tableformatter >}} |
| Ping, Connect | {{< tableformatter >}}
- [Check  resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
- [Check total running time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}})
{{< /tableformatter >}} |

### Browser or Full-Page Check (FPC) monitor

The following error conditions are available for [Browser or Full-Page Check (FPC) monitor]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="en" >}}):

| Monitor type | Error conditions |
|--|--|
| Browser or Full-Page Check | {{< tableformatter >}}

- [Check page availability]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="en" >}}) 
- [Check page content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="en" >}})
- [Check URLs loaded by the page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="en" >}}) 
- [Check page load time]({{< ref path="" lang="en" >}})
- [Check Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="en" >}})
- [Check W3C metrics]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="en" >}})
- [Check console content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="en" >}})
- [Check resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
{{< /tableformatter >}} |

### Transaction monitor

Error conditions in [transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}) are also available for each step. Depending on the [transaction step setup]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}), the following error conditions may or may not be available:

![screenshot error conditions monitor setup](/img/content/scr-error-condition-transactions.min.png)

| Monitor type | Error conditions |
|--|--|
| Transaction or User journey | {{< tableformatter >}} 
- [Content checks]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="en" >}})
- [Check resources]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="en" >}})
- [Check URLs loaded by the page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="en" >}}) 
- [Check Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="en" >}})
- [Check W3C metrics]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="en" >}})
- [Check console content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="en" >}})
- [Check site availability]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="en" >}}) 
- [Check total running time]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}})
{{< /tableformatter >}} |

Note that the [Multi-step API (MSA) monitor]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}) uses a different way to detect errors. It uses **Assertions** to let you define checks to validate if the API response meets your expected conditions. To learn more, refer to [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="en" >}}).

## Set up an Error condition {id="configure-error-condition"}

You can add error conditions when [setting up your monitor from scratch]({{< ref path="support/kb/basics/adding-monitors" lang="en" >}}) or editing an existing monitor.

To set up error conditions:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click the monitor to which you wish to add an error condition.
3. Go to the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.
4. Click the error condition to expand the section and configure the monitor settings.
5. (Optional) To add new checks for an error condition, click the {{< AppElement type="buttonSecondary" >}} \+ New check {{< /AppElement >}} button.
6. Continue configuring conditions.
7. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm the monitor changes.

If you want to get notified when an error condition is met, [create an alert definition]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="en" >}}).

![screenshot error conditions monitor setup](/img/content/gif-set-up-error-condition.gif)