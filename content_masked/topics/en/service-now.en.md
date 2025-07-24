{
  "hero": {
    "title": "Receive website monitoring alerts in ServiceNow"
  },
  "title": "ServiceNow Integration",
  "summary": "Receive website monitoring alerts from Uptrends in ServiceNow.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/service-now",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**ServiceNow** is a cloud-based platform that helps you manage your overall Information Technology (IT) operations through the various ServiceNow applications, including Incident Management.

Integrating **ServiceNow** with Uptrends automatically creates incidents that are reflected in your **ServiceNow** account. To learn more about ServiceNow, refer to the [ServiceNow Integrations documentation]([LINK_URL_1]) and [ServiceNow REST APIs]([LINK_URL_2]).

## Set up the integration

Adding integrations for **ServiceNow** to Uptrends requires that you have a ServiceNow account. Make sure that you have your instance name and authentication credentials ready.

To set up the integration:

1. In the Uptrends web application, go to [SHORTCODE_3] Alerting > Integrations [SHORTCODE_4].
2. In the upper right corner of you screen, click the [SHORTCODE_5] Add Integration [SHORTCODE_6] button.
3. In the popup menu, select **ServiceNow** as the third party integration type.
4. Click the [SHORTCODE_7] Choose [SHORTCODE_8] button to create a new integration.
5. **ServiceNow** will be the default **Integration type** value. Specify the name of your new integration.
6. In the **Predefined variables** section, fill out the following **Value** fields:

- [INLINE_CODE_1] — the instance name of your ServiceNow. This can be identified from the ServiceNow based URL [INLINE_CODE_2].
- [INLINE_CODE_3] — the username of your ServiceNow login account.
- [INLINE_CODE_4] — the password of your ServiceNow login account.

You can either choose to specify these values as **Plain text** or retrieve **Vault credentials** stored in the [Vault]([LINK_URL_3]). Automatically, the integration will use basic authentication to access the **ServiceNow** platform.

![ServiceNow Integration]([LINK_URL_4])

7. (Optional) To customize your login and other integration settings, check the **Customize integration** checkbox. By enabling customization, you can:

- Add and edit existing **Predefined variables** to use such for authentication, escalation levels, and step definitions.
- Add and define steps for different alert types. In most cases, a single HTTP step might already be sufficient for your setup. If you need separate steps for other scenarios, such as authentication, click the [SHORTCODE_9] Add steps [SHORTCODE_10] button.
- Customize [Alert messages]([LINK_URL_5]) for different alert types. This message includes which third party or API to contact, the HTTP messages content, required authentication, and other information.

![Custom Pre-defined variables]([LINK_URL_6])

![Custom Step definition]([LINK_URL_7])

8. (Optional) In the [SHORTCODE_11] Permissions [SHORTCODE_12] tab, select an operator or operator group to add [Integration permissions]([LINK_URL_8]).

9. Click [SHORTCODE_13] Save [SHORTCODE_14] to confirm changes.

10. To verify your setup, test your custom integration using [test messages]([LINK_URL_9]). For more details, refer to the [Testing alert messages to third party systems]([LINK_URL_10]) knowledge base article.

This completes the **ServiceNow** integration setup in Uptrends. You can now use this integration and add it to your [Alert definitions]([LINK_URL_11]).

[SHORTCODE_1]
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you want to temporarily disable receiving alerts.
[SHORTCODE_2]

For any questions or concerns, please [reach out to our Support team]([LINK_URL_12]).
