{
  "hero": {
    "title": "Browser monitoring"
  },
  "title": "Browser monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
  "summary": "The Full Page Check monitor type is the most comprehensive monitor type. Each element is downloaded and loaded into a browser. The report displays your results in a detailed waterfall report.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true
}

Uptrends Browser monitors, also known as a Full Page Check (FPC), are one of several [monitor types]([LINK_URL_1]) Uptrends offers. This monitor type provides detailed performance data about your web page on an element-by-element basis. An FPC monitor will load your page in a real browser, including scripts, CSS, images, third-party elements, and other website components. This monitor completes a page load in a real browser to accurately measure the website's performance as experienced by your end users.

The FPC presents monitoring information in the monitor check details, including a [waterfall chart]([LINK_URL_2]) and other [metrics]([LINK_URL_3]). If you want to monitor third party content on your website, you should use the [enhanced Full Page Check]([LINK_URL_4]) option.

## Setting up an FPC monitor [ANCHOR_1]

Setting up an FPC monitor starts with the creation of the monitor and then choosing the browser type, check interval, and then defining error conditions, choosing checkpoints and setting more specific options like maintenance periods.

For the basics, look into the Uptrends article [Monitor types - Website performance monitors]([LINK_URL_5]).

## Browser monitors (Full Page Checks (FPC))

There are several Browser monitor types that you can choose from:

- [Full Page Check (FPC)]([LINK_URL_6]) — a monitor type that checks all the page's elements upon page load and displays data in a comprehensive [waterfall chart]([LINK_URL_7]).

- [Enhanced Full Page Check or Full Page Check \+ (FPC+)]([LINK_URL_8]) — an option under the FPC monitor that checks all the page's elements, including third-party content, upon page load. This monitor also displays your data in a comprehensive [waterfall chart]([LINK_URL_9]).

The section [Full Page Check]([LINK_URL_10]) has all the information on adding this kind of monitor and managing the settings.

The monitor settings are explained in a number of knowledge base articles, as listed below.

### Main settings

All options on the [SHORTCODE_1] Main [SHORTCODE_2] tab of the monitor are the fundamental settings for the FPC monitor.


- [Check interval]([LINK_URL_11])
- [Concurrent monitoring]([LINK_URL_12])
- [Monitor mode]([LINK_URL_13])
- [Browser type]([LINK_URL_14])
- [Monitor notes (optional)]([LINK_URL_15])

### Error conditions

An FPC monitor by default checks the availability of the given server URL. Other checks need to be defined on the [SHORTCODE_3] Error conditions [SHORTCODE_4] tab of the monitor.

The knowledge base article [Error conditions]([LINK_URL_16]) has more information on how error conditions work.

More specifically, the table [Which error conditions are available?]([LINK_URL_17]) helps you to get an overview of the error conditions that are available for a Full Page Check.

### Monitor permissions

Uptrends' [permission]([LINK_URL_18]) system is in place to define which teams or employees have access to which items. There are different permissions for creation/deletion, view, and edit activities.

- [Monitor permissions]([LINK_URL_19])

### More monitor settings

The following settings are optional in the sense that the monitor will work without defining them. However, to use the monitoring to its full potential and to adjust to your situation, the following settings should be configured.

- [Checkpoints]([LINK_URL_20])
- [Maintenance periods]([LINK_URL_21])
- [Monitor groups]([LINK_URL_22])


## Monitor data and reporting

Once your monitor is set up and running (monitoring) you will start collecting data on the performance. For each monitor check a number of metrics is collected and stored. This data is shown in the monitor check details. Go to [SHORTCODE_5] Monitoring > Monitor log [SHORTCODE_6] and click one of the list entries to open the check details.

### Monitor check details

The check details show the [basic set of load time metrics]([LINK_URL_23]) (*resolve*, *connection*, *download*, and *total time*). In addition your FPC results will include a detailed [waterfall chart]([LINK_URL_24]).

 A waterfall chart is a visual representation of the page load, for each individual element that was loaded. It includes such information as element source IP address, any request and response headers, element size, and a detailed overview of the [load times for individual elements]([LINK_URL_25]).

### Metrics and features [ANCHOR_2]
For more information about metrics related to the browser monitor type, refer to [Metrics and features]([LINK_URL_26]).



## Credits

Browser monitors use Browser credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]([LINK_URL_27]) knowledge base article.