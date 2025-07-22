{
  "hero": {
    "title": "Browser monitoring"
  },
  "title": "Browser monitoring",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
  "summary": "The Full Page Check monitor type is the most comprehensive monitor type. Each element is downloaded and loaded into a browser. The report displays your results in a detailed waterfall report.",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview",
  "sectionlist": true
}

Uptrends Browser monitors, also known as a Full Page Check (FPC), are one of several [monitor types]({{< ref path="support/kb/basics/monitor-types" lang="en" >}}) Uptrends offers. This monitor type provides detailed performance data about your web page on an element-by-element basis. An FPC monitor will load your page in a real browser, including scripts, CSS, images, third-party elements, and other website components. This monitor completes a page load in a real browser to accurately measure the website's performance as experienced by your end users.

The FPC presents monitoring information in the monitor check details, including a [waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}) and other [metrics]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="en" >}}). If you want to monitor third party content on your website, you should use the [enhanced Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="en" >}}) option.

## Setting up an FPC monitor {id="set-up-fpc"}

Setting up an FPC monitor starts with the creation of the monitor and then choosing the browser type, check interval, and then defining error conditions, choosing checkpoints and setting more specific options like maintenance periods.

For the basics, look into the Uptrends article [Monitor types - Website performance monitors]({{< ref path="support/kb/basics/monitor-types#browser-monitors" lang="en" >}}).

## Browser monitors (Full Page Checks (FPC))

There are several Browser monitor types that you can choose from:

- [Full Page Check (FPC)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) — a monitor type that checks all the page's elements upon page load and displays data in a comprehensive [waterfall chart]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}).

- [Enhanced Full Page Check or Full Page Check \+ (FPC+)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/fpc-plus" lang="en" >}}) — an option under the FPC monitor that checks all the page's elements, including third-party content, upon page load. This monitor also displays your data in a comprehensive [waterfall chart]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}).

The section [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) has all the information on adding this kind of monitor and managing the settings.

The monitor settings are explained in a number of knowledge base articles, as listed below.

### Main settings

All options on the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab of the monitor are the fundamental settings for the FPC monitor.


- [Check interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="en" >}})
- [Concurrent monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="en" >}})
- [Monitor mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="en" >}})
- [Browser type]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/browser-types" lang="en" >}})
- [Monitor notes (optional)]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-notes" lang="en" >}})

### Error conditions

An FPC monitor by default checks the availability of the given server URL. Other checks need to be defined on the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab of the monitor.

The knowledge base article [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) has more information on how error conditions work.

More specifically, the table [Which error conditions are available?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) helps you to get an overview of the error conditions that are available for a Full Page Check.

### Monitor permissions

Uptrends' [permission]({{< ref path="support/kb/account/permissions" lang="en" >}}) system is in place to define which teams or employees have access to which items. There are different permissions for creation/deletion, view, and edit activities.

- [Monitor permissions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}})

### More monitor settings

The following settings are optional in the sense that the monitor will work without defining them. However, to use the monitoring to its full potential and to adjust to your situation, the following settings should be configured.

- [Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/checkpoint-information" lang="en" >}})
- [Maintenance periods]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="en" >}})
- [Monitor groups]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="en" >}})


## Monitor data and reporting

Once your monitor is set up and running (monitoring) you will start collecting data on the performance. For each monitor check a number of metrics is collected and stored. This data is shown in the monitor check details. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor log {{< /AppElement >}} and click one of the list entries to open the check details.

### Monitor check details

The check details show the [basic set of load time metrics]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/explanation-total-time-metrics" lang="en" >}}) (*resolve*, *connection*, *download*, and *total time*). In addition your FPC results will include a detailed [waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}).

 A waterfall chart is a visual representation of the page load, for each individual element that was loaded. It includes such information as element source IP address, any request and response headers, element size, and a detailed overview of the [load times for individual elements]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="en" >}}).

### Metrics and features {id="chrome-extra-metrics"}
For more information about metrics related to the browser monitor type, refer to [Metrics and features]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="en" >}}).



## Credits

Browser monitors use Browser credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="en" >}}) knowledge base article.