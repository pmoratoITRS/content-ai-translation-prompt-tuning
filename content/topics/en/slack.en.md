{
  "hero": {
    "title": "Receive website monitoring alerts in Slack"
  }, 
  "title": "Slack",
  "summary": "Receive website monitoring alerts from Uptrends in any Slack channel. Sign up for a free 30 day trial of Uptrends!",
  "url": "/support/kb/alerting/integrations/slack",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/slack" 
}

Integrating **Slack** with Uptrends allows you to send alerting messages to your **Slack channels**. Each integration for Slack you define can send alerts to a different channel, and you can assign multiple integrations for Slack to a single alert escalation. Setting up the integration requires you to take two steps:

1.  Setting up the integrations in Uptrends
2.  Adding the integrations to an alert definition in Uptrends

Curious to see what you'll get when this integration has been set up? Below, you can view an example of what the integration looks like in a Slack channel. Read on for **detailed instructions** on how to set up **integrations for Slack!** 

![](/img/sub/integrations/slack-alert.png)

## 1. Setting up the integration in Uptrends

Adding integrations for Slack to Uptrends requires that you have a Slack account. You'll need to log into the account before or during setup. To set up an integration:

1.  Navigate to {{< AppElement type="menuitem" >}}Alerts > Integrations{{< /AppElement >}} in the main menu to open the Integrations page. The Integrations page contains the integrations that you've defined in Uptrends. Initially, you will find this panel empty.
2.  Click the {{< AppElement type="button" >}}Add integration{{< /AppElement >}} button in the top right corner to open the {{< AppElement type="menuitem" >}}New Integration{{< /AppElement >}} page.
3.  Select **Slack** for your **Integration type**.
4.  Click the **Add to Slack** button and choose the team and Slack channel.
5.  Click {{< AppElement type="button" >}}Authorize{{< /AppElement >}} to return to the Integration setup page.
6.  Enter a name for this integration in the **Integration name** box.
7.  Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button in the lower left corner. After saving, you'll see your new integration for Slack on the *Integration* page.
8.  Continue adding new integrations if you need to send messages to multiple Slack channels.

{{< callout >}}
**Tip:** Deactivating an integration definition means that Uptrends will not use the integration for sending alerts. You might find deactivating an integration definition useful if you would like to temporarily disable receiving alerts in your Slack channel, for example.
{{< /callout >}}

## 2. Adding the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to **attach it to one or more escalation levels to receive alerts** through the integration. To attach an integration definition to an escalation level:

1.  Navigate to the desired alert definition in Uptrends (*Alerts* > *Alert Definitions*).
2.  Click to open an existing definition or create a new one using the {{< AppElement type="button" >}}Add alert definition{{< /AppElement >}} button on the top right.
3.  Click an {{< AppElement type="tab" >}}Escalation level{{< /AppElement >}} tab. Read the knowledge base article [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}) to learn how escalations work.
4.  Select the checkboxes for your integration definitions in the **Alerting by integrations** section.
5.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} when finished.

**And that's it!** You've successfully set up an integration for Slack.

As always, if you have any questions, please [reach out to our support team](/contact).
