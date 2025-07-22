{
  "hero": {
    "title": "What are integrations"
  },
  "title": "What are integrations?",
  "url": "/support/kb/alerting/integrations/what-are-integrations",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/what-are-integrations"
}

Integrations are connections to the outside world that take care of sending out alert messages triggered by Uptrends monitoring. Every time a check triggers an alert, according to the settings in alert definitions you set up, Uptrends sends out the appropriate messages using the integrations you've activated in your alert definitions. The simplest integration is the Email integration; an Email integration creates an email message and sends it to the recipients you specify. Another simple example is the SMS integration; an SMS integration sends SMS/text messages to your operators' mobile phones.

## Connecting to external systems

Aside from sending alert messages to individual people, it's likely that you want to send alert information from Uptrends to other systems for automated processing. Sending the alert information to automated processes is useful for connecting directly to your incident tracking and handling system (e.g., PagerDuty, Splunk On-Call or ServiceNow) or simply sharing alert information in your team's communication tool (e.g., in Slack) or with the general public (e.g., StatusHub).

Some of the available integrations use a fixed text message format (Email, SMS, Phone, Slack) while others adhere to the message format expected by the third party system, so that system can display and process the data coming from Uptrends exactly how it wants to (PagerDuty, StatusHub, Splunk On-Call, ServiceNow). We have integration guides available for all of the supported third party systems. To find the right integration guide, please look at our [Integrations main page](/integrations).

## Building a custom webhook integration

Even though Uptrends has a growing list of predefined integrations, the chances are that you're looking to connect to a system that's not yet listed. Connecting to systems beyond those offered by Uptrends is still possible using the custom integration function to set up an integration with any system that supports webhooks, i.e., if it has an API that can process incoming messages.

If you're connecting to a third party system, the third party system expects the incoming webhook (i.e., the data sent from Uptrends to that system) to use a particular message format so that they can process it. The system's documentation explains the required content of the message, including the meaning of each field and the URL in which to send the message. The integration editor in Uptrends lets you configure all of the needed data.

Alternatively, perhaps you want to connect to a system that doesn't have a required or preferred message format. In that case, it's useful to use the custom integration titled **Uptrends integration**. It has a preconfigured message that contains all alerting variables available in Uptrends. All you need to do is provide the URL of the API you want to connect to.

For more information, please read this article on [how to build a custom integration](/support/kb/alerting/integrations/custom-integrations), which is also useful for changing one of the customizable integrations.
