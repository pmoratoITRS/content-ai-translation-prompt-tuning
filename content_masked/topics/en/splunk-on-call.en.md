{
  "hero": {
    "title": "Receive monitoring alerts in Splunk On-Call"
  },
  "title": "Splunk On-Call Integration",
  "summary": "Receive website monitoring alerts from Uptrends in Splunk On-Call.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/splunk-on-call",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**Splunk On-Call** is an incident management platform that helps DevOps team to collaborate and resolve incidents effectively. You can organize your team for on-call scheduling, incident escalations and notify them in no time whenever there are issues that requires immediate attention. 

Integrating Splunk On-Call with Uptrends automatically creates incidents reflected in your Splunk On-Call dashboard. Setting up the integration between both systems takes these steps:

## 1. Set up your REST integration in Splunk On-Call.
1. Login to your Splunk On-Call account.
2. In the [SHORTCODE_5]Integrations[SHORTCODE_6] tab, click the REST integration which is already enabled by default. For more information, check out the Splunk On-Call [REST Integration]([LINK_URL_1]). 
3. Copy the *URL to notify* without the */$routing_key* value and save this for later use.

## 2. Set up the integration in Uptrends
1. Go to your Uptrends account and go to [SHORTCODE_7]Alerting > Integrations [SHORTCODE_8] menu.
2. At the upper right corner of your screen, click the [SHORTCODE_9]Add Integration[SHORTCODE_10] button.
3. A popup will be shown, select *Splunk On-Call*  as the third party integration type.
4. Click [SHORTCODE_11]Choose[SHORTCODE_12] button.
5. You can now edit the details for your integration setup. Give a name to your new integration.
6. By default, the [SHORTCODE_13]Customize integration[SHORTCODE_14] field is disabled. Tick the checkbox to enable customization and adjust the default integration settings for Splunk On-Call, otherwise, you can leave it as it is. 

[SHORTCODE_1]
**Note:** When you enable the [SHORTCODE_15]Customize integration[SHORTCODE_16], the [SHORTCODE_17]Customizations tab[SHORTCODE_18] tab will appear. This allows you to specify which messages will be sent out when an alert is generated including third party or API to contact, content of HTTP messages or any authentication that is required and so on.

In most cases, just one single HTTP step will be sufficient. However, it is possible to add more steps if you need separate steps for authentication. Additionally, you can choose to define separate steps for individual alert types. This is helpful if your error messages need to be different from your OK messages (for resolved alerts). For more information, visit our [knowledge base articles about integrations]([LINK_URL_2]).
[SHORTCODE_2]


7. Under the Predefined variables section, you can see the *SplunkOnCallUrl* name. Choose which value you'd like to specify from the dropdown menu. For instance, you may choose the *Specify value here* option.
8. Click the three ellipsis next to the *SplunkOnCallUrl* dropdown. A popup will be shown and you can choose from the two options available. You can paste the value of the *URL to notify* you've saved earlier in the Plain text field, or choose a username or password for [vault credentials]([LINK_URL_3]) (if applicable).
9. Click [SHORTCODE_19]Select[SHORTCODE_20] button.
10. After which, specify the value of the *RoutingKey* you want to use. [Routing keys]([LINK_URL_4]) can be found under the [SHORTCODE_21] Settings [SHORTCODE_22]  tab in your Splunk On-call account. 
11. Click [SHORTCODE_23]Save[SHORTCODE_24] to confirm integration settings.

This completes the integration setup in Uptrends. You can now use this integration and add it in your [alert definitions]([LINK_URL_5]).

**And that's it!** You've successfully set up the Splunk On-Call integration.

What will you get when this integration has been set up? See an example below of what the integration looks like in your Splunk On-Call dashboard. 
![Splunk On-Call dashboard with Uptrends integrations]([LINK_URL_6])

[SHORTCODE_3]
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts.
[SHORTCODE_4]

As always, if you have any questions, please [reach out to our support team]([LINK_URL_7]).
