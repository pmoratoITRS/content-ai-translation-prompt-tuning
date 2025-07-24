{
  "hero": {
    "title": "Testing alert messages"
  },
  "title": "Testing Alert Messages",
  "summary": "Alerts can be a really useful way of staying in sync with the status and performance of your websites. Make sure to test them.",
  "url": "[URL_BASE_TOPICS]alerting/testing-alert-configurations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Alert messages are a really useful way of staying in sync with the status and performance of your websites, servers and web services.

When an alert occurs in Uptrends monitoring, alert messages can be sent to operators or third-party applications. The message may be a phone (voice) message, e-mail or SMS or a (customized) message to an application. How these messages have to be sent is defined in integrations. When messages have to be sent, this is organized in alert definitions, see the article [Alerting]([LINK_URL_1]) for more detail.

Since it is crucial that the messages reach the operator or application, you will want to test if they work. Sending a test message works differently for different sorts of integrations. The steps for each integration sort are explained below.

## Sending a test message by e-mail or SMS

[SHORTCODE_1]
**Note**: You have to be an administrator to access the account information of the operators.
[SHORTCODE_2]

1. Go to the menu item [SHORTCODE_3] Account setup > Operators and groups (and sub accounts) [SHORTCODE_4]. 
2. Click the [SHORTCODE_5] View all operators [SHORTCODE_6] button.
3. From the list of operators, select the one you want to test messages for.
4. Make sure that the primary e-mail and mobile phone number are filled in on the [SHORTCODE_7]Main[SHORTCODE_8] tab.
5. Click the [SHORTCODE_9]Send test e-mail[SHORTCODE_10] or [SHORTCODE_11]Send test SMS[SHORTCODE_12] button to send an e-mail or SMS respectively.

You should receive a test message following the initiation of a test.

If you're not an administrator, you can still test messages for your own account.

1. Go to the user menu at the bottom of the menu and select [SHORTCODE_13] User settings [SHORTCODE_14].
2. You will see your own account information.
3. Make sure that the primary e-mail and mobile phone number are filled in. Then use the [SHORTCODE_15]Send test e-mail[SHORTCODE_16] button or [SHORTCODE_17]Send test SMS[SHORTCODE_18] button to start your test.

## Sending a test message to third-party systems

Several third-party applications can receive alert messages from the Uptrends app. There are out-of-the-box [integrations]([LINK_URL_2]) for many third-party systems, which have test functionality. You have to add and configure their integrations to be able to send test messages.

If the test succeeds, a message is received in the third-party application. How this is treated in the system and what it looks like for the user, depends on which system you're using. For example, if you're sending a test message to Slack, you should see a test message appearing in the channel you specified.

### Slack and PagerDuty

For Slack and PagerDuty, standard test functionality exists in the integration:

1.  Go to the menu item [SHORTCODE_19]Alerts > Integrations[SHORTCODE_20].
2.  From the list of integrations, click the one you want to test.
3.  Make sure that all info is filled in.
4.  Click the [SHORTCODE_21]Send test message[SHORTCODE_22] button.

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

To run a simple test for these integrations, use the [SHORTCODE_23] Send test alert [SHORTCODE_24] button at the bottom of the integration screen.

![screenshot Microsoft Teams integration test]([LINK_URL_3])

If you have customized the integration, there is a [SHORTCODE_25] Customizations [SHORTCODE_26] tab added to your integration. You can then use the test message functionality of the custom integration as described below. This will take into account the customizations you've added.

## Sending a test message for custom integrations

Another option is a custom integration, where you can set up sending a message to a third-party application that Uptrends doesn't have a standard integration for. You define the integration using the third-party's API. These integrations also can be tested on whether they send a message in the expected way.

1.  Go to the menu item [SHORTCODE_27] Alerting > Integrations [SHORTCODE_28].
2.  From the list of integrations, click the customized integration you want to test.
3.  Make sure that all info is filled in.
4.  If you want a quick and simple test, use the [SHORTCODE_29] Send test alert [SHORTCODE_30] button at the bottom of the integration screen. 
5.  In case you want to test messaging with your specific settings (customizations) go to the [SHORTCODE_31]Customizations[SHORTCODE_32] tab. You should have defined the HTTP steps here previously while setting up the integration. You can define steps for the different alert types: Error, OK and Reminder. If you decided to have different HTTP steps for different (combinations of) alert types, a number of steps definitions exist.  
![screenshot custom integration steps for alerts]([LINK_URL_4])
 
6.  For each HTTP step definition, click the [SHORTCODE_33]Send test alert[SHORTCODE_34] button.

The article [Setting up a custom integration]([LINK_URL_5]) has more information about testing messages for custom integrations.

## Troubleshooting

If your messages are not received as expected, you can check out some general troubleshooting tips here: [Alerting - Troubleshoot]([LINK_URL_6]).
