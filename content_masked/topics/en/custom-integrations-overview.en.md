{
  "hero": {
    "title": "Custom integrations overview"
  },
  "title": "Custom integrations overview",
  "summary": "Hub with information on setting up a custom integration",
  "url": "[URL_BASE_TOPICS]alerting/integrations/custom-integrations/custom-integrations-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Imagine connecting your Uptrends account to the operations management system your organization uses. Feeding Uptrends alert data into your existing incident management processes creates a seamless integration of Uptrends' external monitoring into the day-to-day procedures your teams already use.

If our [predefined integration types]([LINK_URL_1]) don't include your DevOps software, you can use the custom integration option to build the integration yourself. The key to building a successful integration is knowing what kind of message the other system is expecting. The third party's API documentation tells you which URL to use and which content to post to that URL. Often called webhook-based integrations, they let Uptrends "hook" into the other system by allowing direct calls into them. Uptrends can initiate a call to the integration as soon as a relevant alert appears.

The articles in this section will cover building the right message content (including correct formatting), creating different rules for different message types, and how to test your custom integration once you're done setting it up.

## Setting up a custom integration

To start using custom integrations, follow these steps:

1.  Add a custom integration template to your account. To do so, click the [SHORTCODE_1]\+[SHORTCODE_2] button next to *Integrations* under the *Alerts* drop-down menu, in the Uptrends application.
2.  A popup will appear, prompting you for an integration type. For a custom integration, scroll to the bottom of the list and select **Uptrends integration**.
3.  Specify the URL of the API you're connecting to, using the *ApiUrl* variable under **Predefined variables**. You should be able to find out which URL this should be in the documentation or UI of the external system you're connecting Uptrends to.
4.  Make sure to give the integration a suitable name in the **Integration name** field.
5.  If necessary, customize your integration by visiting the [SHORTCODE_3]Customizations[SHORTCODE_4] tab. The other chapters in this article will guide you through the process.
6.  When you're done setting up, click [SHORTCODE_5]Save[SHORTCODE_6] to store your settings. You can return to the integration to finish customizing it if necessary.

## Building the right message content

This new integration will be a predefined template, containing a (customizable) JSON-formatted message body containing the full range of available alerting variables. This default message format allows you to process all available information related to each alert, but you can remove data you don't need, add your own data or change the message format. You can find the predefined message body under the [SHORTCODE_7]Customizations[SHORTCODE_8] tab, along with other options to further customize your integration.

-   To understand how to start setting up the desired message content and how to use variables, we recommend that you read our article on [building the right message content]([LINK_URL_2]) first.
-   You can find a complete overview of available alerting variables in our list of [alerting system variables]([LINK_URL_3]).
-   Keep in mind your outgoing message must be formatted correctly. Make sure to read our [guide on message formatting]([LINK_URL_4]) to avoid unnecessary errors in your external application.

## Message types [ANCHOR_1]

Alerting messages come in different types. Uptrends makes the distinction between **Error** messages, **Reminder** messages, and **Ok** messages. By default, all these message types are created with the same setup. However, when setting up a custom integration or customizing an existing integration, you can create different sets of actions for each individual message type. Check out our [article on message types]([LINK_URL_5]) to learn more.

## Testing your custom integration

Once you've created or modified a customized integration, it's useful to test it first before using it in production. Our [article on testing your custom integration]([LINK_URL_6]) will cover the ways of testing the newly set up integration.

## Adding the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to **attach it to one or more escalation levels to receive alerts** through the integration. To attach an integration definition to an escalation level:

1.  Navigate to the desired alert definition in Uptrends (*Alerts* > *Alert Definitions*).
2.  Click to open an existing definition or create a new one using the [SHORTCODE_9]Add alert definition[SHORTCODE_10] button on the top right.
3.  Click an [SHORTCODE_11]Escalation level[SHORTCODE_12] tab.
4.  Select the checkboxes for your custom integration definitions in the **Alerting by integrations** section.
5.  Click [SHORTCODE_13]Save[SHORTCODE_14] when finished.

**And that's it!** You've successfully set up a custom integration.

As always, if you have any questions, please [reach out to our Support team]([LINK_URL_7]).
