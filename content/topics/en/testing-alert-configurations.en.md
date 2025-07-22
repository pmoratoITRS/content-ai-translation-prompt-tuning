{
  "hero": {
    "title": "Testing alert messages"
  },
  "title": "Testing Alert Messages",
  "summary": "Alerts can be a really useful way of staying in sync with the status and performance of your websites. Make sure to test them.",
  "url": "/support/kb/alerting/testing-alert-configurations",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/testing-alert-configurations"
}

Alert messages are a really useful way of staying in sync with the status and performance of your websites, servers and web services.

When an alert occurs in Uptrends monitoring, alert messages can be sent to operators or third-party applications. The message may be a phone (voice) message, e-mail or SMS or a (customized) message to an application. How these messages have to be sent is defined in integrations. When messages have to be sent, this is organized in alert definitions, see the article [Alerting]({{< ref path="support/kb/alerting" lang="en" >}}) for more detail.

Since it is crucial that the messages reach the operator or application, you will want to test if they work. Sending a test message works differently for different sorts of integrations. The steps for each integration sort are explained below.

## Sending a test message by e-mail or SMS

{{< callout >}}
**Note**: You have to be an administrator to access the account information of the operators.
{{< /callout >}}

1. Go to the menu item {{< AppElement type="menuitem" >}} Account setup > Operators and groups (and sub accounts) {{< /AppElement >}}. 
2. Click the {{< AppElement type="buttonPrimary" >}} View all operators {{< /AppElement >}} button.
3. From the list of operators, select the one you want to test messages for.
4. Make sure that the primary e-mail and mobile phone number are filled in on the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab.
5. Click the {{< AppElement type="button" >}}Send test e-mail{{< /AppElement >}} or {{< AppElement type="button" >}}Send test SMS{{< /AppElement >}} button to send an e-mail or SMS respectively.

You should receive a test message following the initiation of a test.

If you're not an administrator, you can still test messages for your own account.

1. Go to the user menu at the bottom of the menu and select {{< AppElement type="menuitem" >}} User settings {{< /AppElement >}}.
2. You will see your own account information.
3. Make sure that the primary e-mail and mobile phone number are filled in. Then use the {{< AppElement type="button" >}}Send test e-mail{{< /AppElement >}} button or {{< AppElement type="button" >}}Send test SMS{{< /AppElement >}} button to start your test.

## Sending a test message to third-party systems

Several third-party applications can receive alert messages from the Uptrends app. There are out-of-the-box [integrations](/integrations) for many third-party systems, which have test functionality. You have to add and configure their integrations to be able to send test messages.

If the test succeeds, a message is received in the third-party application. How this is treated in the system and what it looks like for the user, depends on which system you're using. For example, if you're sending a test message to Slack, you should see a test message appearing in the channel you specified.

### Slack and PagerDuty

For Slack and PagerDuty, standard test functionality exists in the integration:

1.  Go to the menu item {{< AppElement type="menuitem" >}}Alerts > Integrations{{< /AppElement >}}.
2.  From the list of integrations, click the one you want to test.
3.  Make sure that all info is filled in.
4.  Click the {{< AppElement type="button" >}}Send test message{{< /AppElement >}} button.

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

To run a simple test for these integrations, use the {{< AppElement type="buttonSecondary" >}} Send test alert {{< /AppElement >}} button at the bottom of the integration screen.

![screenshot Microsoft Teams integration test](/img/content/scr_test-message-to-microsoft-teams.min.png)

If you have customized the integration, there is a {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab added to your integration. You can then use the test message functionality of the custom integration as described below. This will take into account the customizations you've added.

## Sending a test message for custom integrations

Another option is a custom integration, where you can set up sending a message to a third-party application that Uptrends doesn't have a standard integration for. You define the integration using the third-party's API. These integrations also can be tested on whether they send a message in the expected way.

1.  Go to the menu item {{< AppElement type="menuitem" >}} Alerting > Integrations {{< /AppElement >}}.
2.  From the list of integrations, click the customized integration you want to test.
3.  Make sure that all info is filled in.
4.  If you want a quick and simple test, use the {{< AppElement type="buttonSecondary" >}} Send test alert {{< /AppElement >}} button at the bottom of the integration screen. 
5.  In case you want to test messaging with your specific settings (customizations) go to the {{< AppElement type="tab" >}}Customizations{{< /AppElement >}} tab. You should have defined the HTTP steps here previously while setting up the integration. You can define steps for the different alert types: Error, OK and Reminder. If you decided to have different HTTP steps for different (combinations of) alert types, a number of steps definitions exist.  
![screenshot custom integration steps for alerts](/img/content/scr_custom-integration-steps-for-alerts.min.png)
 
6.  For each HTTP step definition, click the {{< AppElement type="button" >}}Send test alert{{< /AppElement >}} button.

The article [Setting up a custom integration](/support/kb/alerting/integrations/custom-integrations) has more information about testing messages for custom integrations.

## Troubleshooting

If your messages are not received as expected, you can check out some general troubleshooting tips here: [Alerting - Troubleshoot](/support/kb/alerting#troubleshooting).
