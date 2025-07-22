{
  "hero": {
    "title": "Alert escalation levels"
  },
  "title": "Alert escalation levels",
  "summary": "With alert definitions and escalation levels you can configure alerts for designated recipients or integrations, in line with your organization's escalation policy in case of downtime.",
  "url": "/support/kb/alerting/alert-escalation-levels",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-escalation-levels"
}

## What are escalation levels?

The Uptrends alerting system was built with teams in mind. With customizable escalation levels that help you make sure that the right people are alerted about a potential issue, at the right time. 

An escalation level contains a series of parameters for alert generation, number of reminders, notification method, and who will receive it. They can be configured in an alert definition.

You can configure up to three escalation levels, and generate alerts based on your own rules:

- Generate an alert when errors occur for a specific period of time or when a specific number of errors have occurred
- Define how many reminders are sent within a certain interval
- Set alert methods by using [integrations]({{< ref path="support/kb/alerting/integrations" lang="en" >}})
- Add a custom message (for Slack, PagerDuty, and email notifications only)
- Include a traceroute log in emails
- Add an extra email address to alert additional people
- Select which operators or operator groups get the alert 
- Decide (for each integration) if you want to send OK and reminder alerts 

## Setting up an alert escalation

Within each alert definition, you have one to three escalation levels. To set up your escalations:

1. Go to {{< AppElement type="menuitem" >}} Alerting > Alert definitions {{< /AppElement >}} and select an alert definition to modify. Alternatively, search for a specific definition in the [Uptrends menu search bar]({{< ref path="/support/kb/basics/user-interface/search" lang="en" >}}). If you have to create a new alert definition, check out [Creating alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}).
2. Open the {{< AppElement type="tab" >}} Escalation Level 1 {{< /AppElement >}} tab.
3. Select the **Active** check box if not already selected.
4. Set the rules for the **Escalation** by filling in the *Generate an alert when* parameters.
5. Set the frequency of the reminders. Learn more in the knowledge base article [Alert reminders]({{< ref path="support/kb/alerting/alert-reminders-in-escalations" lang="en" >}}).
6. Choose one or more **Alerting by integrations** options, e.g. the predefined **Alerting by E-mail**, **SMS** (SMS/Text uses message credits) or **Phone** integration. 
7. If you have configured other integrations you can choose them here. Visit the knowledge base article [Integrations]({{< ref path="/support/kb/alerting/integrations" lang="en" >}}) for more information.
8. For most integrations you can decide whether you want to receive OK alerts and reminders. Expand the integration by clicking the arrow > in front of the integration and activate the corresponding options. 

   ![screenshot alert options](/img/content/scr_alert-definition-escalation-choose-alerts.min.png)

   Note that [custom integrations]({{< ref path="support/kb/alerting/integrations/custom-integrations" lang="en" >}}) use [message types]({{< ref path="support/kb/alerting/integrations/custom-integrations#message-types" lang="en" >}}) to deal with different alerts (error, reminder, OK). The arrangements you made in the message types will be shown in the alert definition, but cannot be changed there. Instead you have to make any changes in the custom integration itself. 
9. Add a custom message (optional and only applies to some integrations).
10. Select the **Traceroute** check box to receive a traceroute log within the emails.
11. Use the **Groups and operators** section to select the operators for the escalation. Remember that alerts go out only if the designated operator is active and on-duty. *Active* is a main setting for an operator and on-duty is derived from the operator's [off-duty schedule]({{< ref path="/support/kb/account/users/operators/using-duty-schedules" lang="en" >}}).
12. Set up escalation levels 2 and 3 if your organization's escalation path calls for it. 
13. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button when you are finished configuring your levels.

## Alerting by integrations

The knowledge base article about [Integrations]({{< ref path="support/kb/alerting/integrations" lang="en" >}}) tells you more about the different types of integrations, which include phone (uses message credits) and other integrations like [PagerDuty]({{< ref path="support/kb/alerting/integrations/pagerduty" lang="en" >}}), [Microsoft Teams]({{< ref path="support/kb/alerting/integrations/microsoft-teams" lang="en" >}}), [Slack]({{< ref path="support/kb/alerting/integrations/slack" lang="en" >}}), and [StatusHub]({{< ref path="support/kb/alerting/integrations/statushub" lang="en" >}}).

## Testing alert configurations

Once you have set up your escalation levels and added the integrations you want to use, you can test if messages are sent succesfully. Check out the knowledge base article [Testing alert messages]({{< ref path="support/kb/alerting/testing-alert-configurations" lang="en" >}}) for the methods available for different integrations.