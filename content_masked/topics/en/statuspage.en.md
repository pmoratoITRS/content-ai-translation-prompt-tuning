{
  "hero": {
    "title": "Receive alerts in Statuspage"
  },
  "title": "Statuspage",
  "summary": "Steps needed to set up sending Uptrends alert notifications to Statuspage. ",
  "url": "[URL_BASE_TOPICS]alerting/integrations/statuspage",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Statuspage** is Atlassian's status and incident communication tool, allowing you to communicate your pages' and websites' status with your users in real-time.  
Getting your Uptrends alerting integrated into your Statuspage environment is simple! Setting up the integration between both systems takes these steps:

1.  Set up a component in Statuspage
2.  Create a Statuspage API key
3.  Set up the integration in Uptrends
4.  Add the integration to an alert definition in Uptrends

After setting up this integration and with the proper alerting settings, your status page will immediately display the real-time status of your page or resource for your users.

![]([LINK_URL_1])

Read on for detailed instructions on how to set up this integration!

## 1. Add a component in Statuspage

1.  In your Statuspage environment, add a new *component* under the **Components** menu. Give the new component a suitable name, and optionally a good description. Save the component.
2.  Open the newly created component, and take note of the URL. It will be in the form manage.Statuspage.io/pages/{page\_id}/components/{component\_id}/edit. We'll need both the *{page\_id}* and *{component\_id}* later on, so make sure to take notes!

[SHORTCODE_1]
**Tip:** It might be a good idea to create separate components per domain you're monitoring with Uptrends. That way, you can keep better track of which domains are operational or not at any given time.
[SHORTCODE_2]

## 2. Create an API key in Statuspage

1.  At the bottom left of the screen, click the user icon, and go to **API info**. ![]([LINK_URL_2])
2.  Here, create a new API key by clicking the *Create key* button. Fill in an appropriate name and confirm.
3.  The newly created API key appears immediately. Make sure to take note of this key, as we'll need it later.

This completes the integration setup on the Statuspage end.

## 3. Set up the integration in Uptrends

To add a new integration for Statuspage in Uptrends, follow these steps:

1.  Go to [SHORTCODE_7]Alerts > Integrations[SHORTCODE_8].
2.  Click [SHORTCODE_9]Add integration[SHORTCODE_10] at the top right.
3.  Choose Statuspage as the integration type.
4.  Specify a name for this integration.
5.  Paste the Statuspage API Key, Page\_Id and Component\_Id in the corresponding [SHORTCODE_11]predefined variable[SHORTCODE_12] fields.
6.  Click [SHORTCODE_13]Save[SHORTCODE_14] to store your settings. The new Statuspage integration will appear on the Integrations page.

This completes the integration setup in Uptrends. You can now use this integration in your alert definitions.

[SHORTCODE_3]
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
[SHORTCODE_4]

## 4. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to [SHORTCODE_15]Alerts > Alert definitions[SHORTCODE_16] and open the one that you want to attach the integration to.
2.  Each [SHORTCODE_17]Escalation level[SHORTCODE_18] tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]([LINK_URL_3]) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for Statuspage. 
4.  Make sure to hit the [SHORTCODE_19]Save[SHORTCODE_20] button to save your changes.

[SHORTCODE_5]
**Tip:** Each individual Statuspage integration you create affects a single Statuspage component. Therefore, we'd recommend matching individual components on the Statuspage end to individual integrations and alert definitions on the Uptrends end.
[SHORTCODE_6]

**And that's it!** You've successfully set up the Statuspage integration.

As always, if you have any questions, please [reach out to our support team]([LINK_URL_4]).
