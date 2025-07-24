{
  "hero": {
    "title": "Show your API and site status in Statushub"
  },
  "title": "StatusHub Integration",
  "summary": "Combine the power of StatusHub's alerting capabilities with your Uptrends settings using this handy integration.",
  "url": "[URL_BASE_TOPICS]alerting/integrations/statushub",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Integrating your [Statushub]([LINK_URL_1]) account with Uptrends enables automatic status updates of the services in your Statushub status page. Setting up the integration between both systems consists of three steps.

1.  Setting up webhook integrations in Statushub.
2.  Creating an integration and specifying those webhooks in Uptrends.
3.  Create service links in Uptrends to link Uptrends monitors to Statushub services.

This page contains a detailed description of the steps needed to integrate Uptrends with your Statushub status pages.

## 1. Setting up webhook integrations in Statushub

1.  First, we'll prepare everything on the Statushub side. Log into your Statushub account and click the pencil icon to edit your status site.

2.  Click 'Service & integrations' in the menu on the left. Next, you'll edit each service you want to control with Uptrends.

3.  In the edit popup for a service, locate the 'Enable/disable integrations' section. Click on the Uptrends button and make sure it is highlighted.

4.  At the bottom of the popup, click 'Update Service'. Back in the service overview, you'll see that the service now shows a URL in the form

    [INLINE_CODE_1]

    We will use this URL later on to link Uptrends to this Statushub service.

5.  Repeat this procedure for each service you want to control with Uptrends.

This completes the integration setup in Statushub.

[SHORTCODE_1]
**Tip:** In Uptrends, there is no limit to the number of Statushub services you can control. You can create as many service links as you need, or start out with just one.
[SHORTCODE_2]

## 2. Setting up the integration in Uptrends

1.  In your Uptrends account, go to [SHORTCODE_5] Alerting > Integrations [SHORTCODE_6] in the sidebar menu.
2.  To set up a brand new Statushub integration, click **Add integration** at the top right.
3.  Choose Statushub as the integration type. Specify a name for this integration (simply *Statushub* will do).
4.  Save the integration.
5.  In the next screen (the integrations overview), select the integration you just saved.
6.  Once back in the Statushub integration screen, you need to tell us about your Statushub services. Click on the [SHORTCODE_7]Add service[SHORTCODE_8] button to add one.
7.  For each Statushub service, fill in the service name and service URL. The service URL is the webhook URL you just created by enabling the Uptrends function in Statushub.
8.  Lastly, click [SHORTCODE_9]Save[SHORTCODE_10] to store your settings. The new Statushub integration will appear on the Integrations page.

## 3. Using the Statushub integration in alert definitions

In order to actually start using the integration, we need to attach it to at least one alert definition and set up some service links. A service link is the link between one Uptrends monitor and a Statushub service. Alerts for that monitor will be sent to the service you link to it.

1.  Navigate to one of your alert definitions or create a new one ([SHORTCODE_11] Alerting > Alert definitions [SHORTCODE_12]).
2.  Select the escalation level you want to add Statushub to.
3.  In the **Alerting by integrations** section, locate the Statushub integration and select it. Read the knowledge base article [Alert escalation levels]([LINK_URL_2]) to learn how escalations work.
4.  The integration is not active yet; click the checkbox to activate it in this escalation level.
5.  A button [SHORTCODE_13]Add service link[SHORTCODE_14] appears. Click it to create a link between an Uptrends monitor on the left, and a Statushub service on the right. Using these settings, you have fine grained control over which Uptrends monitor updates which service in Statushub. You can add as many service links to this escalation level as you need.
6.  Click the [SHORTCODE_15]Save[SHORTCODE_16] button at the lower left to save this alert definition.

[SHORTCODE_3]
**Tip:** Most setups use straightforward one-on-one service links between monitors and services. However, you can create more advanced setups too. For example, it is possible to create multiple service links that use one single monitor to update several services in Statushub.
[SHORTCODE_4]

## What to expect when your integration is complete

The normal alert definition conditions apply. When Uptrends detects an error for one of your monitors, we will generate an alert according to the settings in your escalation levels. When an escalation level triggers a new alert, we will generate a new incident in Statushub for the appropriate service(s). The service status will be set to **Service disruption**, and the new incident will get the **Investigating** status. Your Statushub status page should update immediately to reflect these changes.

This situation will stay unchanged as long as the error situation continues in Uptrends. In the meantime, you can update your Statushub services as you see fit. As soon as Uptrends detects that the error has been resolved, we'll update your service to **Service is operating normally**, and the incident to **Monitoring**. When you are confident that the problem has been resolved, you can reset the incident to **Resolved** in Statushub. This way, you can always control what is displayed on your status page.

Do you have any questions about creating the right setup? Please [reach out to our support team]([LINK_URL_3]).
