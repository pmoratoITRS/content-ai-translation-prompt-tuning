{
  "hero": {
    "title": "Testing your custom integration"
  },
  "title": "Testing your custom integration",
  "summary": "Custom integrations - a guide on how to test your custom integration setup",
  "url": "/support/kb/alerting/integrations/custom-integrations/testing-your-custom-integration",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/testing-your-custom-integration" 
}

Once you've created or modified a customized integration, it's useful to test it first before using it in production. This article will cover two ways of testing the newly set up integration. Typically, a successful test will mean you can see the incoming alerting data in the third-party system you're connecting to, having been correctly parsed or processed.

## Checking an integration using test messages

It's possible to test new integrations by having Uptrends generate fictitious data, and sending it to the third party system. The {{< AppElement type="tab" >}}Customization{{< /AppElement >}} tab in the integration editor has a button titled **Send test message** that allows you to send a test message to the third party system using the HTTPS step(s) you've created. When you use this test function, you can select which alert type (an Error alert, an OK alert or a Reminder alert) Uptrends should use for this particular test message. You can fill in any other appropriate values if necessary, and the remaining data (which would normally be relevant monitor data and alert data) will be filled with fictitious values.

Once Uptrends generates the message and sends it out to the third party system or API, the full message content, the server's response code, and the content is displayed. You can expand the request headers and content and the response headers and content to inspect the outgoing and incoming traffic that was involved in sending this test message. 

## Checking an integration using live data

While the test function described in the previous section is useful for static testing of your message and variables and establishing that the communication channel to the external system works correctly, it's good to have the option to verify that the integration works correctly in a live situation as well.  
  
First, make sure that one of your alert definitions actually uses your integration. Otherwise, Uptrends never triggers the integration to send out messages. For more information on how to activate integrations in your alerting setup, please read about [escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}).  
  
Next, an error situation needs to happen so that your monitoring generates a real alert. As soon as you see an alert in your Alert status or Alert log dashboard, click on it to reveal the details for that alert. The {{< AppElement type="tab" >}}Details{{< /AppElement >}} tab lists all key properties of the alert; the {{< AppElement type="tab" >}}Messages{{< /AppElement >}} tab contains the information you need to inspect the message traffic between Uptrends and the external system.  
  
On the {{< AppElement type="tab" >}}Messages{{< /AppElement >}} tab, locate the integration you want to inspect; it may display other integrations that were also triggered by this alert. Expand the integration panel and the requests and responses within it. You'll see the full content of the outgoing message(s), the responses sent back by the external system, and any error messages that occurred if there was a problem in sending the alert message.
