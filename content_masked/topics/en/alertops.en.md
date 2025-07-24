{
  "hero": {
    "title": "Receive alerts in AlertOps"
  },
  "title": "AlertOps",
  "summary": "How-to guide for the AlertOps integration",
  "url": "[URL_BASE_TOPICS]alerting/integrations/alertops",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**AlertOps** is a real-time operations automation tool. It allows you to prioritize your incidents, and automate your processes. Major incidents can be easily managed by mobilizing on-call teams and empowering them with additional information.

1.  Set up the inbound integration in AlertOps
2.  Set up the integration in Uptrends
3.  Add the integration to an alert definition in Uptrends

After setting up this integration and with the proper alerting settings, your Uptrends alerts will generate alerts in AlertOps as well. Below is an example of what such an alert looks like on the AlertOps side.![]([LINK_URL_1])

Read on for detailed instructions on how to set up this integration!

## 1. Set up an inbound integration in AlertOps

1.  In the AlertOps interface, navigate to the *Inbound Integrations* menu (under *Integrations* in the sidebar menu).
2.  Make sure you're on the **API** tab, and click the *ADD API INTEGRATION* button.
3.  In the next screen, click *Uptrends*, to select the default Uptrends integration.
4.  Give the integration a suitable name, and select the appropriate **Recipient Group(s)/User(s)**.![]([LINK_URL_2])
5.  Click the *Save* button.
6.  Take note of the **API URL** that is now listed in the AlertOps interface. You'll need it when we add the integration on the Uptrends end.

This completes the integration setup on the AlertOps end.

[SHORTCODE_1]
**Note**: AlertOps offers a predefined Uptrends integration, that should be functional right away. This integration is highly customizable on the AlertOps end, but while we're setting up, we recommend not changing any of the advanced settings. Once you have verified that the integration works, it can be customized to suit your needs.
[SHORTCODE_2]

## 2. Set up the integration in Uptrends

To add a new integration for AlertOps in Uptrends, follow these steps:

1.  Go to [SHORTCODE_3]Alerts > Integrations[SHORTCODE_4].
2.  Click [SHORTCODE_5]Add integration[SHORTCODE_6] at the top right.
3.  Choose AlertOps as the integration type.
4.  Specify a name for this integration.
5.  Paste the AlertOps **API URL** in the corresponding [SHORTCODE_7]predefined variable[SHORTCODE_8] field.
6.  Click [SHORTCODE_9]Save[SHORTCODE_10] to store your settings. The new AlertOps integration will appear on the Integrations page.

This completes the integration setup in Uptrends. You can now use this integration in your alert definitions.

## 3. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to [SHORTCODE_11]Alerts > Alert definitions[SHORTCODE_12] and open the one that you want to attach the integration to.
2.  Each [SHORTCODE_13]Escalation level[SHORTCODE_14] tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]([LINK_URL_3]) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for AlertOps.
4.  Make sure to hit the [SHORTCODE_15]Save[SHORTCODE_16] button to save your changes.

**And that's it!** You've successfully set up the AlertOps integration.

As always, if you have any questions, please [reach out to our support team]([LINK_URL_4]).
