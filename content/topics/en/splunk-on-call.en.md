{
  "hero": {
    "title": "Receive monitoring alerts in Splunk On-Call"
  }, 
  "title": "Splunk On-Call Integration",
  "summary": "Receive website monitoring alerts from Uptrends in Splunk On-Call.",
  "url": "/support/kb/alerting/integrations/splunk-on-call",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/splunk-on-call" 
}

**Splunk On-Call** is an incident management platform that helps DevOps team to collaborate and resolve incidents effectively. You can organize your team for on-call scheduling, incident escalations and notify them in no time whenever there are issues that requires immediate attention. 

Integrating Splunk On-Call with Uptrends automatically creates incidents reflected in your Splunk On-Call dashboard. Setting up the integration between both systems takes these steps:

## 1. Set up your REST integration in Splunk On-Call.
1. Login to your Splunk On-Call account.
2. In the {{< AppElement type="tab" >}}Integrations{{< /AppElement >}} tab, click the REST integration which is already enabled by default. For more information, check out the Splunk On-Call [REST Integration](https://help.victorops.com/knowledge-base/rest-endpoint-integration-guide/). 
3. Copy the *URL to notify* without the */$routing_key* value and save this for later use.

## 2. Set up the integration in Uptrends
1. Go to your Uptrends account and go to {{< AppElement type="menuitem" >}}Alerting > Integrations {{< /AppElement >}} menu.
2. At the upper right corner of your screen, click the {{< AppElement type="button" >}}Add Integration{{< /AppElement >}} button.
3. A popup will be shown, select *Splunk On-Call*  as the third party integration type.
4. Click {{< AppElement type="button" >}}Choose{{< /AppElement >}} button.
5. You can now edit the details for your integration setup. Give a name to your new integration.
6. By default, the {{< AppElement type="menuitem" >}}Customize integration{{< /AppElement >}} field is disabled. Tick the checkbox to enable customization and adjust the default integration settings for Splunk On-Call, otherwise, you can leave it as it is. 

{{< callout >}}
**Note:** When you enable the {{< AppElement type="menuitem" >}}Customize integration{{< /AppElement >}}, the {{< AppElement type="tab" >}}Customizations tab{{< /AppElement >}} tab will appear. This allows you to specify which messages will be sent out when an alert is generated including third party or API to contact, content of HTTP messages or any authentication that is required and so on.

In most cases, just one single HTTP step will be sufficient. However, it is possible to add more steps if you need separate steps for authentication. Additionally, you can choose to define separate steps for individual alert types. This is helpful if your error messages need to be different from your OK messages (for resolved alerts). For more information, visit our [knowledge base articles about integrations]({{< ref path="support/kb/alerting/integrations" lang="en" >}}).
{{< /callout >}}


7. Under the Predefined variables section, you can see the *SplunkOnCallUrl* name. Choose which value you'd like to specify from the dropdown menu. For instance, you may choose the *Specify value here* option.
8. Click the three ellipsis next to the *SplunkOnCallUrl* dropdown. A popup will be shown and you can choose from the two options available. You can paste the value of the *URL to notify* you've saved earlier in the Plain text field, or choose a username or password for [vault credentials]({{< ref path="support/kb/account/vault#credential-set" lang="en" >}}) (if applicable).
9. Click {{< AppElement type="button" >}}Select{{< /AppElement >}} button.
10. After which, specify the value of the *RoutingKey* you want to use. [Routing keys](https://help.victorops.com/knowledge-base/routing-keys/) can be found under the {{< AppElement type="tab" >}} Settings {{< /AppElement >}}  tab in your Splunk On-call account. 
11. Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} to confirm integration settings.

This completes the integration setup in Uptrends. You can now use this integration and add it in your [alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}).

**And that's it!** You've successfully set up the Splunk On-Call integration.

What will you get when this integration has been set up? See an example below of what the integration looks like in your Splunk On-Call dashboard. 
![Splunk On-Call dashboard with Uptrends integrations](/img/content/scr_integration-splunk-on-call.min.png)

{{< callout >}}
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
{{< /callout >}}

As always, if you have any questions, please [reach out to our support team](/contact).
