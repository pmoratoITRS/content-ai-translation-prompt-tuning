{
  "hero": {
    "title": "Error conditions - Core Web Vitals"
  },
  "title": "Error conditions - Core Web Vitals",
  "summary": "Using thresholds on Core Web Vitals to trigger errors.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-core-web-vitals"
}

Google has defined the Core Web Vitals as a standard set of metrics to measure the user experience of a web page.

[Browser and transaction monitor types]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}) measure and report the [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}). Since this kind of data is available it makes sense to take a closer look and use it for signaling errors when a certain threshold is reached. Therefore conditions for Core Web Vitals are part of the [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}).

Note that different monitor types offer different error conditions. Check the table in [Which error conditions are available?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) to find out which options are available for certain monitor types.

The error conditions related to Core Web Vitals are explained below.

## Defining the error condition for Core Web Vitals

To define this error condition:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click on the monitor's name to edit it.
3. Open the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.
4. Expand the *Check Core Web Vitals* section by clicking the arrow in front of it.
   ![screenshot check Core Web Vitals](/img/content/scr_errorconditions-corewebvitals.min.png)

   You can now choose to not check Core Web Vitals, use the recommended (default) threshold values, or set your own threshold values. The choices are explained below.
5. When you are done with setting the thresholds, click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button.


## Use default threshold values (recommended setting) {id="use-current-recommended-core-web-vitals"}

Google describes the performance status of your website by using three statuses: good, needs improvement, and poor. 
With Uptrends you can signal an error once the "needs improvement" status is reached. Uptrends uses the benchmark values that Google defines, which are currently:

**First Contentful Paint:** 1.8 seconds  
**Largest Contentful Paint:** 2.5 seconds  
**Time to Interactive:** 3.8 seconds  
**Cumulative Layout Shift:** 0.1  
**Total Blocking Time:** 0.2 seconds (200 ms)

If you choose the option *Use default threshold values*, an error will be triggered when at least one of the benchmark values is exceeded. 

## Specify custom threshold values

If for any reason the default threshold values do not work for you, you can still set you own thresholds.
Choose the option **Specify custom threshold values**. Then enable the error condition for certain metrics by ticking the check box and entering a value. The original value is the default threshold value (recommended) which you change by entering your own value.

For any metrics that you don't want to set an error condition for, simply uncheck the box in front of the line.

The threshold values correspond to the Core Web Vitals metrics as described below.
### Maximum time to First Contentful Paint (FCP)

Use this error condition to set a maximum for how long it may take before the browser starts rendering parts of the page that the user can initially see. If the user doesn't get any timely visual feedback of the page loading, it may impact the experience of a user interacting with your website.

### Maximum time to Largest Contentful Paint (LCP)

With this error condition, you set a maximum for how long it may take before the browser can render the main content of the page. If the user needs to wait longer than expected for the bulk of the content to load, it may impact their experience.

### Maximum Time To Interactive (TTI)

You can use this to set a maximum for how long it may take for the page to respond to user interactions. If this takes too long, the user ends up waiting for the page to load before the page eventually responds to the input of the user.

### Maximum Cumulative Layout Shift (CLS)

The Cumulative Layout Shift (CLS) measures visual stability by checking whether there is an unexpected shifting of page elements taking place while loading the page. Use this error condition to make sure there is no disturbance for the user by parts moving around on your page due to late/asynchronous loading of videos, for example.

### Maximum Total Blocking Time (TBT)

Set this error condition to specify a maximum for how long the browser may be blocked from loading the page due to waiting for connections to become available, scripts to run, or rendering to finish. If the user needs to wait to interact with the page due to their browser being blocked for too long, it influences the experience of using your website. 