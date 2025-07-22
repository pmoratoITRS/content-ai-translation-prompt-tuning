{
  "hero": {
    "title": "Receive website monitoring alerts in ServiceNow"
  }, 
  "title": "ServiceNow Integration",
  "summary": "Receive website monitoring alerts from Uptrends in ServiceNow.",
  "url": "/support/kb/alerting/integrations/service-now",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/integrations/service-now" 
}

**ServiceNow** is a cloud-based platform that helps you manage your overall Information Technology (IT) operations through the various ServiceNow applications, including Incident Management.

Integrating **ServiceNow** with Uptrends automatically creates incidents that are reflected in your **ServiceNow** account. To learn more about ServiceNow, refer to the [ServiceNow Integrations documentation](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/managing-data/concept/integrations.html) and [ServiceNow REST APIs](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html).

## Set up the integration

Adding integrations for **ServiceNow** to Uptrends requires that you have a ServiceNow account. Make sure that you have your instance name and authentication credentials ready.

To set up the integration:

1. In the Uptrends web application, go to {{< AppElement type="menuitem" >}} Alerting > Integrations {{< /AppElement >}}.
2. In the upper right corner of you screen, click the {{< AppElement type="button" >}} Add Integration {{< /AppElement >}} button.
3. In the popup menu, select **ServiceNow** as the third party integration type.
4. Click the {{< AppElement type="button" >}} Choose {{< /AppElement >}} button to create a new integration.
5. **ServiceNow** will be the default **Integration type** value. Specify the name of your new integration.
6. In the **Predefined variables** section, fill out the following **Value** fields:

- `InstanceName` — the instance name of your ServiceNow. This can be identified from the ServiceNow based URL `https://<instancename>.service-now.com`.
- `Username` — the username of your ServiceNow login account.
- `Password` — the password of your ServiceNow login account.

You can either choose to specify these values as **Plain text** or retrieve **Vault credentials** stored in the [Vault]({{< ref path="/support/kb/account/vault" lang="en" >}}). Automatically, the integration will use basic authentication to access the **ServiceNow** platform.

![ServiceNow Integration](/img/content/scr-service-now-integration.min.png)

7. (Optional) To customize your login and other integration settings, check the **Customize integration** checkbox. By enabling customization, you can:

- Add and edit existing **Predefined variables** to use such for authentication, escalation levels, and step definitions.
- Add and define steps for different alert types. In most cases, a single HTTP step might already be sufficient for your setup. If you need separate steps for other scenarios, such as authentication, click the {{< AppElement type="button" >}} Add steps {{< /AppElement >}} button.
- Customize [Alert messages]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="en" >}}) for different alert types. This message includes which third party or API to contact, the HTTP messages content, required authentication, and other information.

![Custom Pre-defined variables](/img/content/scr-service-now-integration-customization.min.png)

![Custom Step definition](/img/content/scr-service-now-integration-customization-steps.min.png)

8. (Optional) In the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab, select an operator or operator group to add [Integration permissions]({{< ref path="/support/kb/alerting/integrations/integrations-permissions" lang="en" >}}).

9. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm changes.

10. To verify your setup, test your custom integration using [test messages]({{< ref path="/support/kb/alerting/integrations/custom-integrations/testing-your-custom-integration" lang="en" >}}). For more details, refer to the [Testing alert messages to third party systems]({{< ref path="/support/kb/alerting/testing-alert-configurations#sending-a-test-message-to-third-party-systems" lang="en" >}}) knowledge base article.

This completes the **ServiceNow** integration setup in Uptrends. You can now use this integration and add it to your [Alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}).

{{< callout >}}
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you want to temporarily disable receiving alerts.
{{< /callout >}}

For any questions or concerns, please [reach out to our Support team](/contact).
