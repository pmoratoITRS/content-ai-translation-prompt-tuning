{
  "hero": {
    "title": "Multi-step API monitor hub"
  },
  "title": "Multi-step API monitor hub",
  "summary": "Your starting place when exploring Multi-step API monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-hub",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-hub",
  "tableofcontents": false
}

The **Multi-step API (MSA) hub** provides a general overview of MSAs and your MSA monitoring setup. To open this page, go to {{< AppElement type="menuitem" >}} API > {{< /AppElement >}} [Explore API monitoring](https://app.uptrends.com/Hubs/Api) menu. In the sidebar menu, you'll find links to relevant knowledge base articles:

![MSA Hub](/img/content/scr-msa-hub.min.png)

The following cards display your API monitor setup:

- The **API monitors** card shows the number of your monitor setups. Clicking the {{< AppElement type="buttonPrimary" >}} View all API monitors {{< /AppElement >}} button opens the API monitors overview or the {{< AppElement type="menuitem" >}}  API monitors setup {{< /AppElement >}} menu.

- The **API monitor status** card shows the number of monitors with [confirmed errors]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}) and active alerts. Clicking the {{< AppElement type="buttonPrimary" >}} View monitor status {{< /AppElement >}} button opens the **Monitors status** page. Clicking the {{< AppElement type="buttonPrimary" >}} View ongoing alerts {{< /AppElement >}} button opens the **Current alert status** page.

- The Active monitors card shows the API monitors in [Staging and Production mode]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="en" >}}).

- The API credits card shows your API credits balance. To buy more credits, refer to [Adding extra monitors and credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="en" >}}).

The hub also features a way to automatically scan your existing monitors and identify those that can be converted into [API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}). If it detects any HTTP or HTTPS monitors that appear to check an API endpoint, it will offer the option to automatically create a new API monitor for you.

This functionality instantly upgrades any [Uptime monitor]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="en" >}}) into a fully configured API monitor without deleting or modifying the original monitor. You can freely undo the action at any time if needed. Additionally, there's no need to manually recreate everything from scratch, Uptrends handles all the setup, replicating the same settings from your existing monitors.

Clicking the **See details** button opens a pop-up that lets you convert your existing monitor into an API monitor. Once converted, another pop-up will appear to let you review the configuration and enable the newly created monitor for use.