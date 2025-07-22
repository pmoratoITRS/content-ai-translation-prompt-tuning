{
  "hero": {
    "title": "Alert reminders in escalations"
  },
  "title": "Alert reminders in escalations",
  "summary": "Alert definitions have a reminder option for all escalation levels.",
  "url": "/support/kb/alerting/alert-reminders-in-escalations",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-reminders-in-escalations"
}

## What are reminders?

A reminder is a method to repeatedly inform operators about an unresolved error. When an alert is generated (always based on a confirmed error), you can notify operators or systems by sending a message (using an integration). The operators should then take action to fix the problem that was signaled. In case the operators did not see the message or did not act on it, you may want to send reminders to draw the operators' attention or to emphasize the urgency of the problem.  
If the SLAs (service level agreements) with your customers promise a fix within a specified time frame, you want to make sure that the operators are getting the message and acting in line with the expectations set forth in the SLA.

The reminders in the Uptrends app are part of Escalation levels in Alert definitions. Depending on the escalation levels in your SLAs, you may want to implement the reminder mechanism here.

Once an alert is created and persists, as long as no OK alert is generated, the reminders will be sent according to your specifications. As soon as the signaled error is resolved (has an OK check and an OK alert), the sending of reminders will stop.

## How to implement reminders

The *Reminders* setting is part of the [Escalation levels]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="en" >}}) within an Alert definition.

![](/img/content/c8407764-8f48-49fa-8608-79e3ee2b1c4f.png)

You set the maximum number and interval of reminders by completing the sentence with values for 'n' and 'x':  
*Send a maximum of 'n' reminder alerts, every 'x' minutes.*

Keep the following in mind when setting the values:

-   If you don't want to send reminders, set 'n' to 0.
-   Synchronize the reminder interval 'x' with the Escalation interval (if used). For example, if you have set the Escalation to "Generate an alert when error occurs for more than 5 minutes.", it makes no sense to set a reminder for every 3 minutes.
-   Think about the check interval (in the monitor settings). If you have set the reminders to be sent more frequently than the monitor is doing checks, this might not work efficiently. You could end up with a situation, where you send a reminder while the next monitor check returns an OK result and therefore the reminder is not needed anymore.

{{< callout >}}
**Note:** To stay in control of your reminders, avoid reminders that are overlapping for different escalation levels. If in escalation level 1 you set 3 reminders every 5 minutes, and suppose that escalation level 2 kicks in after 10 minutes, the two start overlapping.
{{< /callout >}}

## Integrations suitable for reminders

Integrations are the definitions of how a message is sent, once an alert is created. Not all integrations are equally suited for use with reminders.

The implementation of reminders is useful for integrations like email, SMS and Slack. In other words, reminders make sense for integrations where a real person receives the message and acts upon it.

For other integrations like PagerDuty, Statushub, Splunk On-Call, ServiceNow and probably several custom integrations, it might not make sense to implement reminders. Often, such integrations set a status within a system, based on an error alert or OK alert. A reminder will not change the status itself and therefore does not make sense in most cases. The error status will stay in the system until the system receives an OK alert notification. A reminder does not change that process and therefore is not recommended.
