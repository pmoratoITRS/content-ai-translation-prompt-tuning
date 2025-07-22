{
  "hero": {
    "title": "Monitor settings overview"
  },
  "title": "Monitor settings overview",
  "summary": "Each monitor has some general and more specific settings (depending on the monitor type). Check out which settings are available.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/monitor-settings-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

## Monitor settings

Uptrends offers a wide range of [monitor types]([LINK_URL_1]), each with different settings to match your specific monitoring needs. You can access and adjust these settings by opening the monitor editor. 

Each tab in the editor represents a set of monitor settings. Below is a list of settings you can configure for a monitor.
![Monitor settings]([LINK_URL_2])

### Main

The [SHORTCODE_1] Main [SHORTCODE_2] tab contains the general monitor settings, where you can set the name, status, and other details of your monitor. In this tab, you can customize the following settings by category:

#### General

- Set a [monitor type]([LINK_URL_3]).
- Set a monitor name.
- Set the [check interval]([LINK_URL_4]) in minutes to specify how often your monitor is checked.
- Select between [standard or concurrent monitoring]([LINK_URL_5]) to specify if the monitor should be executed on multiple checkpoint locations at the same time or not.

#### Status

- Set the [monitor mode]([LINK_URL_6]) to specify if your monitor should run in **Development**, **Staging**, or **Production** mode.
- Enable (activate) or disable (deactivate) monitor status.
- Enable (activate) or disable (deactivate) generating [monitor alerts]([LINK_URL_7]).

#### Details

- Set the [IP address]([LINK_URL_8]) that will be used to connect to the checkpoint server.
- Set the URL or IP address of the website, webservice, or server that you want to monitor.
- Use [dynamic values in URL and post content]([LINK_URL_9]).
- Set the [browser type]([LINK_URL_10]) that will be used to load the website.
- Set [domain groups]([LINK_URL_11]) to manage and organize multiple domains.
- Set the port number for specific monitor types.

#### Meta data

- Add [monitor notes]([LINK_URL_12]) to describe the purpose and usage of the monitor.  
- Use [custom fields]([LINK_URL_13]) to include external information and custom data from third-party integrations as part of your alerting.

### Steps

The [SHORTCODE_3] Steps [SHORTCODE_4] tab contains the settings available for Multi-step API monitors and transaction monitors only. For more information, refer to [Steps in Multi-step API monitors]([LINK_URL_14]) and [Steps in transaction monitors]([LINK_URL_15]).

### Error conditions

The [SHORTCODE_5] Error conditions [SHORTCODE_6] tab contains all the conditions that you can set to inform your monitor of any errors on your website, web service, or server. These conditions are your monitor's basis for deciding which website behaviors result in an error and which don't. For more information, refer to the [Error conditions overview]([LINK_URL_16]) knowledge base article.

### Advanced settings

The [SHORTCODE_7] Advanced [SHORTCODE_8] tab contains the following categories to further customize browser types, HTTP requests, and authentication settings for your monitor:

#### Advanced

- Set the [user agent]([LINK_URL_17]) to identify the browser type and operating system of the user.

### Browser

- Set the [browser type]([LINK_URL_18]) that will be used to load the website.
- Specify the device and screen size that will be used to simulate monitoring checks.

#### Measurement

- Set the [load time]([LINK_URL_19]) based on the W3C total time metric or your own network activity.  

#### Connection

- Use [bandwidth throttling]([LINK_URL_20]) to intentionally limit the amount of data that can be transferred over a network connection in a given amount of time. 
- [Block or disable outgoing requests to Google Analytics]([LINK_URL_21]).
- [Block or disable Uptrends RUM]([LINK_URL_22]) to avoid additional RUM pageviews.
- Block specific URLs to prevent the monitor from making requests to those addresses.
- Set a [DNS bypass]([LINK_URL_23]) to resolve certain URLs to a custom IP address.

#### Authentication

- Use [Basic, NTLM (Windows), or Digest authentication ]([LINK_URL_24]) if the website you are monitoring requires authentication as part of the HTTP request.

#### HTTP request

- Set the HTTP methods, request headers, and request body for a more specific monitoring configuration.
- Enable or disable checking for SSL certificate errors.
- Set specific TLS versions that should be supported when running a monitor check.

### Checkpoints

The [SHORTCODE_9] Checkpoints [SHORTCODE_10] tab allows you to specify checkpoint locations for monitoring your server, website, or web service. For more information, refer to the [Checkpoints]([LINK_URL_25]) knowledge base article.

### Maintenance periods

The [SHORTCODE_11] Maintenance periods [SHORTCODE_12] tab allows you to schedule maintenance periods whenever your servers, websites, or web services are down for planned maintenance. For more information, refer to the [Maintenance periods]([LINK_URL_26]) knowledge base article.

### Member of

The [SHORTCODE_13] Member of [SHORTCODE_14] tab allows you to include your monitor as a member of a monitor group. For more information, refer to the [Monitor groups]([LINK_URL_27]) knowledge base article.

### Permissions

The [SHORTCODE_15] Permissions [SHORTCODE_16] tab allows you to set permission rights to an individual operator or operator group. For more information, refer to the [Permissions]([LINK_URL_28])
knowledge base article.

## Access monitor settings

To access the monitor settings, start by navigating the Uptrends application using the left-side menu. You'll find setup options under [SHORTCODE_17] Monitoring [SHORTCODE_18] and [SHORTCODE_19] Synthetics [SHORTCODE_20], depending on your use case.

### Monitoring menu

1. Go to [SHORTCODE_21] Monitoring > Monitor setup [SHORTCODE_22].
2. Click the monitor name you wish to access the settings for.
3. Each tab represents a set of monitor settings. Click on a tab to access and adjust its configuration based on your monitoring requirements.
4. Click [SHORTCODE_23] Save [SHORTCODE_24] to confirm all your monitor changes.

### Synthetics menu

Under [SHORTCODE_25] Synthetics [SHORTCODE_26], complete the following steps:

1. Hover over a monitor type (Transactions, Browser, API, Uptime) and click the monitor type setup.
2. Click the name of the monitor you wish to access the settings for.
3. Each tab represents a set of monitor settings. Click on a tab to access and adjust its configuration based on your monitoring requirements.
4. Click [SHORTCODE_27] Save [SHORTCODE_28] to confirm all your monitor changes.