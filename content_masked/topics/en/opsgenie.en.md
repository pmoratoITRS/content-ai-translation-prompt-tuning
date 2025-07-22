{
  "hero": {
    "title": "Receive alerts in Opsgenie"
  },
  "title": "Opsgenie",
  "summary": "Steps needed to set up sending Uptrends alert notifications to Opsgenie.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/opsgenie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Opsgenie** is Atlassian's alerting and incident management platform, allowing you to aggregate your alerts and notifications from external systems (such as Uptrends), and prioritize and assign action.  
Getting your Uptrends alerting integrated into your Opsgenie environment is simple! Setting up the integration between both systems takes these steps:

1.  Set up an API integration in Opsgenie
2.  Set up the integration in Uptrends
3.  Add the integration to an alert definition in Uptrends

After setting up this integration and with the proper alerting settings, your Uptrends alerts will generate alerts in Opsgenie as well. Below is an example of what such an alert looks like on the Opsgenie side.

![]([LINK_URL_1])

The Opsgenie alert will be generated for the team for which you set up the integration. If you wish for alerts to be sent to multiple teams, you can set up one integration for each.

Read on for detailed instructions on how to set up this integration!

## 1. Set up the integration in Opsgenie

1.  In your Opsgenie environment, set up a new team or use an existing one.
2.  Under the options for this team, go to *Integrations*.
3.  Locate the pre-existing *API* integration (it should be named *{teamname}\_API}*). If this integration does not already exist, create a new integration by clicking the **Add integration** button, and select the 'API' integration type. Open this integration and take note of the API Key - you'll need it later.
4.  Save the integration.

This completes the integration setup in Opsgenie.

## 2. Set up the integration in Uptrends

To add a new integration for Opsgenie in Uptrends follow these steps:

1.  Go to [SHORTCODE_3]Alerts > Integrations[SHORTCODE_4].
2.  Click [SHORTCODE_5]Add integration[SHORTCODE_6] at the top right.
3.  Choose Opsgenie as the integration type.
4.  Specify a name for this integration.
5.  Paste the Opsgenie API Key which you copied earlier into [SHORTCODE_7]Predefined variables > ApiKey[SHORTCODE_8].
6.  Click [SHORTCODE_9]Save[SHORTCODE_10] to store your settings. The new Opsgenie integration will appear on the Integrations page.

By default, the Opsgenie integration will use the international Opsgenie instance, with [INLINE_CODE_1] as its request URL. If you're using the EU instance of Opsgenie, the request URL should be [INLINE_CODE_2] instead. To edit this:

1. In the Opsgenie integration settings, enable **Customize integration**. 
2. Open the [SHORTCODE_11]Customizations[SHORTCODE_12] tab that appears.
3. Under **Method and URL**, change the request URL to [INLINE_CODE_3] to use the EU instance of the Opsgenie API.
![Opsgenie EU instance URL]([LINK_URL_2])
4. Send a test alert to verify you're using the correct instance, by clicking the [SHORTCODE_13]Send test alert[SHORTCODE_14] button.
5. Save the integration. 

This completes the integration setup in Uptrends. You can now use this integration in your alert definitions.

[SHORTCODE_1]
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
[SHORTCODE_2]

## 3. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to [SHORTCODE_15]Alerts > Alert definitions[SHORTCODE_16] and open the one that you want to attach the integration to.
2.  Each [SHORTCODE_17]Escalation level[SHORTCODE_18] tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]([LINK_URL_3]) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for Opsgenie. 
4.  Make sure to hit the [SHORTCODE_19]Save[SHORTCODE_20] button to save your changes.

**And that's it!** You've successfully set up the Opsgenie integration.

As always, if you have any questions, please [reach out to our support team]([LINK_URL_4]).
