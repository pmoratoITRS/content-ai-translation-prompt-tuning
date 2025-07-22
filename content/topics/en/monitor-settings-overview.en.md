{
  "hero": {
    "title": "Monitor settings overview"
  },
  "title": "Monitor settings overview",
  "summary": "Each monitor has some general and more specific settings (depending on the monitor type). Check out which settings are available.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-settings-overview",
  "sectionlist": false
}

## Monitor settings

Uptrends offers a wide range of [monitor types]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}), each with different settings to match your specific monitoring needs. You can access and adjust these settings by opening the monitor editor. 

Each tab in the editor represents a set of monitor settings. Below is a list of settings you can configure for a monitor.
![Monitor settings](/img/content/gif-monitor-settings.gif)

### Main

The {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab contains the general monitor settings, where you can set the name, status, and other details of your monitor. In this tab, you can customize the following settings by category:

#### General

- Set a [monitor type]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}).
- Set a monitor name.
- Set the [check interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="en" >}}) in minutes to specify how often your monitor is checked.
- Select between [standard or concurrent monitoring]({{< ref path="/support/kb/synthetic-monitoring/concurrent-monitoring/concurrent-monitoring-overview" lang="en" >}}) to specify if the monitor should be executed on multiple checkpoint locations at the same time or not.

#### Status

- Set the [monitor mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="en" >}}) to specify if your monitor should run in **Development**, **Staging**, or **Production** mode.
- Enable (activate) or disable (deactivate) monitor status.
- Enable (activate) or disable (deactivate) generating [monitor alerts]({{< ref path="/support/kb/alerting/alerting-overview#alerts" lang="en" >}}).

#### Details

- Set the [IP address]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/using-an-ipv6-address-instead-of-a-domain-name" lang="en" >}}) that will be used to connect to the checkpoint server.
- Set the URL or IP address of the website, webservice, or server that you want to monitor.
- Use [dynamic values in URL and post content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dynamic-date-notation-in-url-and-post-content" lang="en" >}}).
- Set the [browser type]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="en" >}}) that will be used to load the website.
- Set [domain groups]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/working-with-domain-groups" lang="en" >}}) to manage and organize multiple domains.
- Set the port number for specific monitor types.

#### Meta data

- Add [monitor notes]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="en" >}}) to describe the purpose and usage of the monitor.  
- Use [custom fields]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#including-external-ids-or-custom-data" lang="en" >}}) to include external information and custom data from third-party integrations as part of your alerting.

### Steps

The {{< AppElement type="tab" >}} Steps {{< /AppElement >}} tab contains the settings available for Multi-step API monitors and transaction monitors only. For more information, refer to [Steps in Multi-step API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}}) and [Steps in transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}).

### Error conditions

The {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab contains all the conditions that you can set to inform your monitor of any errors on your website, web service, or server. These conditions are your monitor's basis for deciding which website behaviors result in an error and which don't. For more information, refer to the [Error conditions overview]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview" lang="en" >}}) knowledge base article.

### Advanced settings

The {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tab contains the following categories to further customize browser types, HTTP requests, and authentication settings for your monitor:

#### Advanced

- Set the [user agent]({{< ref path="" lang="en" >}}) to identify the browser type and operating system of the user.

### Browser

- Set the [browser type]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="en" >}}) that will be used to load the website.
- Specify the device and screen size that will be used to simulate monitoring checks.

#### Measurement

- Set the [load time]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features#load-time-w3c-total-time-or-network-time" lang="en" >}}) based on the W3C total time metric or your own network activity.  

#### Connection

- Use [bandwidth throttling]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling" lang="en" >}}) to intentionally limit the amount of data that can be transferred over a network connection in a given amount of time. 
- [Block or disable outgoing requests to Google Analytics]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/analytics-blocking" lang="en" >}}).
- [Block or disable Uptrends RUM]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="en" >}}) to avoid additional RUM pageviews.
- Block specific URLs to prevent the monitor from making requests to those addresses.
- Set a [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="en" >}}) to resolve certain URLs to a custom IP address.

#### Authentication

- Use [Basic, NTLM (Windows), or Digest authentication ]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication#default-authentication-types" lang="en" >}}) if the website you are monitoring requires authentication as part of the HTTP request.

#### HTTP request

- Set the HTTP methods, request headers, and request body for a more specific monitoring configuration.
- Enable or disable checking for SSL certificate errors.
- Set specific TLS versions that should be supported when running a monitor check.

### Checkpoints

The {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} tab allows you to specify checkpoint locations for monitoring your server, website, or web service. For more information, refer to the [Checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="en" >}}) knowledge base article.

### Maintenance periods

The {{< AppElement type="tab" >}} Maintenance periods {{< /AppElement >}} tab allows you to schedule maintenance periods whenever your servers, websites, or web services are down for planned maintenance. For more information, refer to the [Maintenance periods]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="en" >}}) knowledge base article.

### Member of

The {{< AppElement type="tab" >}} Member of {{< /AppElement >}} tab allows you to include your monitor as a member of a monitor group. For more information, refer to the [Monitor groups]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="en" >}}) knowledge base article.

### Permissions

The {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab allows you to set permission rights to an individual operator or operator group. For more information, refer to the [Permissions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}})
knowledge base article.

## Access monitor settings

To access the monitor settings, start by navigating the Uptrends application using the left-side menu. You'll find setup options under {{< AppElement type="menuitem" >}} Monitoring {{< /AppElement >}} and {{< AppElement type="menuitem" >}} Synthetics {{< /AppElement >}}, depending on your use case.

### Monitoring menu

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click the monitor name you wish to access the settings for.
3. Each tab represents a set of monitor settings. Click on a tab to access and adjust its configuration based on your monitoring requirements.
4. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm all your monitor changes.

### Synthetics menu

Under {{< AppElement type="menuitem" >}} Synthetics {{< /AppElement >}}, complete the following steps:

1. Hover over a monitor type (Transactions, Browser, API, Uptime) and click the monitor type setup.
2. Click the name of the monitor you wish to access the settings for.
3. Each tab represents a set of monitor settings. Click on a tab to access and adjust its configuration based on your monitoring requirements.
4. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm all your monitor changes.