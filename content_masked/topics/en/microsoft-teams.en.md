{
  "hero": {
    "title": "Receive monitoring alerts in Microsoft Teams"
  },
  "title": "Microsoft Teams Integration",
  "summary": "Receive website monitoring alerts from Uptrends in Microsoft Teams.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/microsoft-teams",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Microsoft Teams** is the hub for teamwork in Microsoft 365. You can communicate (in chat, call, video) and share information (files, agendas, etc.) in Teams. Integrating Microsoft Teams with Uptrends enables automatic notifications from Uptrends. Setting up the integration between both systems takes these steps:

1.  Set up a *workflow* in Microsoft Teams
2.  Set up the integration in Uptrends
3.  Add the integration to an alert definition in Uptrends

What will you get when this integration has been set up? Below, you see an example of what the integration looks like in Microsoft Teams. 

![Teams alert example]([LINK_URL_1])      

Within the Microsoft Teams channel for which the integration was defined, you'll get a message with details about the alert that was generated. From this message you can jump directly to the dashboard, error or monitor in Uptrends to get even more detail and further investigate the problem. Just push one of the buttons and it will bring you to the right place in the Uptrends app.

Read on for detailed instructions on how to set up this integration!

## 1. Set up a workflow in Microsoft Teams

1.  In Microsoft Teams go to the channel, where you want to receive messages from Uptrends. Hover over the channel to make the [SHORTCODE_3]More options[SHORTCODE_4] ( ... ) appear. Select [SHORTCODE_5]Workflows[SHORTCODE_6].  
    ![Adding a workflow]([LINK_URL_2])
2.  Search for and select *"Post to a channel when a webhook request is received"*.  
3.  Enter a name for the workflow.
4.  Click *Next*.
5. Double-check the **Microsoft Teams Team** and **Microsoft Teams Channel** settings, and click *Add workflow*.
5.  The workflow should be created after a few seconds. A URL will be shown at the bottom of the form:  
    ![Teams workflow URL]([LINK_URL_3])
6.  Copy the URL and save it somewhere. You will need it later to set up the integration in Uptrends.
7.  Click [SHORTCODE_7]Done[SHORTCODE_8].

This completes the integration setup in Microsoft Teams.

## 2. Set up the integration in Uptrends

To add a new integration for Microsoft Teams in Uptrends follow these steps:

1.  Go to [SHORTCODE_9]Alerts > Integrations[SHORTCODE_10].
2.  Click [SHORTCODE_11]Add integration[SHORTCODE_12] at the top right.
3.  Choose Microsoft Teams as the integration type.  
    ![]([LINK_URL_4])
4.  Specify a name for this integration.
5.  Paste the Microsoft Teams webhook URL which you copied earlier into [SHORTCODE_13]Predefined variables > WorkflowUrl[SHORTCODE_14].
6.  Click [SHORTCODE_15]Save[SHORTCODE_16] to store your settings. The new Microsoft Teams integration will appear on the Integrations page.

This completes the integration setup in Uptrends. You can now use this integration in your alert definitions.

[SHORTCODE_1]
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
[SHORTCODE_2]

## 3. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to [SHORTCODE_17]Alerts > Alert definitions[SHORTCODE_18] and open the one that you want to attach the integration to.
2.  Each [SHORTCODE_19] Escalation level [SHORTCODE_20] tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]([LINK_URL_5]) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for Microsoft Teams.
4.  Make sure to hit the [SHORTCODE_21]Save[SHORTCODE_22] button to save your changes.

**And that's it!** You've successfully set up the Microsoft Teams integration.

As always, if you have any questions, please [reach out to our support team]([LINK_URL_6]).
