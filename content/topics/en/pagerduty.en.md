{
  "hero": {
    "title": "Receive website monitoring alerts in PagerDuty"
  },
  "title": "PagerDuty",
  "summary": "Receive website monitoring alerts from Uptrends in PagerDuty. Sign up for a free 30 day trial of Uptrends!",
  "url": "/support/kb/alerting/integrations/pagerduty",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/pagerduty" 
}

PagerDuty provides alerting, on-call scheduling, escalation policies, and incident tracking to alert your team and aggregate system information. Uptrends' integration option with **PagerDuty** can send alerting messages out of your **Uptrends account** to a **PagerDuty account**. Setting up the integration requires you to take three steps:

1.  Setting up the integration in PagerDuty
2.  Setting up the integration in Uptrends
3.  Adding the integration to an alert definition in Uptrends

Curious to see what you'll get when this integration has been set up? Below, you see an example of what the integration looks like in PagerDuty. Read on for **detailed instructions** on how to set it up!

![](/img/sub/integrations/integration-pagerduty-dashboard.png)

## 1. Setting up the integration in PagerDuty

This preparation is only applicable if you would like to receive alerts in your PagerDuty account. The integration between Uptrends and PagerDuty consists of alerts which are sent by Uptrends to a user defined service in PagerDuty. In order for Uptrends to be able to send alerts to that PagerDuty service, you need to create a service within your PagerDuty account. This process is detailed below.

1.  Select **Services** from the top menubar of the main screen of your PagerDuty account.
2.  A page named *Services* will open. Click on the button named **\+ New Service**.
3.  A page named *Create a Service* will open. On this page, you can provide the service information. 
4.  Enter a name for the service and optionally a description. Select an existing Escalation Policy, or generate a new one, as required. If necessary, select an appropriate **Alert Grouping** setting.
5. It is **not** necessary to add an integration at this point, as one will be created automatically. Click *Create service without an integration*.
6.  You are now directed to the service page of your newly created service. The *Integrations*-tab will contain the **Integration Key** of your service.

This completes the integration set up in PagerDuty.

## 2. Setting up the integration in Uptrends

The integrations feature in Uptrends can be accessed from the main menu.

1.  In the sidebar menu, click **Alerting**. Start adding a new integration by clicking the **+** icon next to *Integrations*. ![Adding a new integration](/img/content/scr-integrations-add_new_integration.png)
2.  Select *PagerDuty* to create a PagerDuty integration. ![Selecting PagerDuty](/img/content/scr-pagerduty-before_setup.png)
3.  Click on the **Alert with PagerDuty** button, to start the process of connecting Uptrends and PagerDuty. Log in using your PagerDuty credentials. ![PagerDuty login portal](/img/content/scr-pagerduty-signin.png)
4. In the next screen, select the PagerDuty service(s) you wish to use with your Uptrends alerting. 
![Selecting the PagerDuty service(s)](/img/content/scr-pagerduty-servicesselection.png)
5.  After clicking *Connect*, you will be returned to Uptrends.
6.  To complete the definition, enter a name for this integration and click on the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button in the lower left corner. After saving you will return to the integrations panel, which will contain your newly created integration definition.
7.  You can click on this integration to open it for editing purposes or to send test messages.
![PD post setup](/img/content/scr-pagerduty-post_setup_integration.png)

{{< callout >}}
**Tip:** Deactivating an integration definition means that the integration will not be used for alerting purposes. This might be useful if you would like to temporarily disable receiving alerts in your PagerDuty service for example.
{{< /callout >}}

## 3. Adding the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to **attach it to one or more escalation levels in order to receive alerts** through it.

1.  In order to attach an integration definition to an escalation level, navigate to the desired alert definition and escalation level in Uptrends.

 ![Navigate to alert definitions](/img/content/scr-integrations-to_alert_defs.png)

2.  Each {{< AppElement type="tab" >}}Escalation level{{< /AppElement >}} tab contains an element called **Alerting by integrations**. Read the knowledge base article [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}) to learn how escalations work.
3. Select the integration definition that you would like to attach to this escalation level. In this case the **PagerDuty** integration.
4.  Make sure to hit the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button to save your changes.

**And that's it!** You've successfully set up the PagerDuty integration.

As always, if you have any questions, please [reach out to our support team](/contact).
