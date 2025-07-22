{
  "hero": {
    "title": "Receive alerts in Opsgenie"
  },
  "title": "Opsgenie",
  "summary": "Steps needed to set up sending Uptrends alert notifications to Opsgenie.",
  "url": "/support/kb/alerting/integrations/opsgenie",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/opsgenie" 
}

**Opsgenie** is Atlassian's alerting and incident management platform, allowing you to aggregate your alerts and notifications from external systems (such as Uptrends), and prioritize and assign action.  
Getting your Uptrends alerting integrated into your Opsgenie environment is simple! Setting up the integration between both systems takes these steps:

1.  Set up an API integration in Opsgenie
2.  Set up the integration in Uptrends
3.  Add the integration to an alert definition in Uptrends

After setting up this integration and with the proper alerting settings, your Uptrends alerts will generate alerts in Opsgenie as well. Below is an example of what such an alert looks like on the Opsgenie side.

![](/img/content/848ce01f-0e91-4b6e-86ed-336ceb1945ef.png)

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

1.  Go to {{< AppElement type="menuitem" >}}Alerts > Integrations{{< /AppElement >}}.
2.  Click {{< AppElement type="button" >}}Add integration{{< /AppElement >}} at the top right.
3.  Choose Opsgenie as the integration type.
4.  Specify a name for this integration.
5.  Paste the Opsgenie API Key which you copied earlier into {{< AppElement type="menuitem" >}}Predefined variables > ApiKey{{< /AppElement >}}.
6.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} to store your settings. The new Opsgenie integration will appear on the Integrations page.

By default, the Opsgenie integration will use the international Opsgenie instance, with `https://api.opsgenie.com/v2/alerts` as its request URL. If you're using the EU instance of Opsgenie, the request URL should be `https://api.eu.opsgenie.com/v2/alerts` instead. To edit this:

1. In the Opsgenie integration settings, enable **Customize integration**. 
2. Open the {{< AppElement type="tab" >}}Customizations{{< /AppElement >}} tab that appears.
3. Under **Method and URL**, change the request URL to `https://api.eu.opsgenie.com/v2/alerts` to use the EU instance of the Opsgenie API.
![Opsgenie EU instance URL](/img/content/scr-opsgenie-eu-instance.png)
4. Send a test alert to verify you're using the correct instance, by clicking the {{< AppElement type="savebutton" >}}Send test alert{{< /AppElement >}} button.
5. Save the integration. 

This completes the integration setup in Uptrends. You can now use this integration in your alert definitions.

{{< callout >}}
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
{{< /callout >}}

## 3. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to {{< AppElement type="menuitem" >}}Alerts > Alert definitions{{< /AppElement >}} and open the one that you want to attach the integration to.
2.  Each {{< AppElement type="tab" >}}Escalation level{{< /AppElement >}} tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for Opsgenie. 
4.  Make sure to hit the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button to save your changes.

**And that's it!** You've successfully set up the Opsgenie integration.

As always, if you have any questions, please [reach out to our support team](/contact).
