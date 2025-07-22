{
  "hero": {
    "title": "Error conditions - Resources"
  },
  "title": "Error conditions - Resources",
  "summary": "An overview of the available error conditions for the category *Resources*. The resources are the elements that your webpage loads to make it visible and functional.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-resources"
}

Every monitor in Uptrends runs a set of standard checks, which vary depending on the [monitor type]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}). In addition to these standard checks, you can define custom checks in the [Error conditions]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview" lang="en" >}}) tab to trigger alerts for specific situations.

This article explains how the **Check resources** error condition works. To find this monitor setting, go to the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab > **Check resources**.  Note that this error condition may not be available for all monitor types.

## What is a resource check?

Your website relies on a number of resources such as images, stylesheets, scripts, and more that must be loaded for the page to function properly. These resources make up the content that your site delivers. 

A monitor check measures the size of the server’s response in bytes, providing insight into the amount of content delivered. Using the **Check resources** error condition, you can specify thresholds for the total size of all resources or for individual ones. These settings help you assess whether your website is loading as expected. The page size, combined with content matching, can indicate whether the page has fully loaded.

Unexpected small or large page sizes can also indicate potential fraudulent page manipulation. For a [Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="en" >}}) or a [transaction monitor]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}), you can get a [waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}), which visually represents the loading process of individual page elements. The chart includes key metrics and detailed insights from the monitoring check.

## Check the content size (HTTP, HTTPS, and Webservice monitors)

For HTTP, HTTPS, or Webservice monitors, fill in the lower limit in bytes to check the content's minimum size. If the combined size of all page elements falls below the specified threshold, it may indicate that your page is missing content and might not function properly.

![screenshot check resources HTTPS(S) or webservices](/img/content/scr_errorconditions-resources-https.min.png)

## Check the sum of all resources together

You can also set the minimum and a maximum size of the server response in bytes.

To set the minimum size, select **All resources together are over** and fill in the lower limit in bytes. If the combined size of all page elements falls below the specified threshold, this could indicate that your page is missing content and might not function properly.

![screenshot error condition all resources together](/img/content/scr_errorconditions-resources-all.min.png)

To set a maximum size, select **All resources together are under** and fill in the upper limit in bytes. If the combined size of all page elements exceeds the specified threshold, it may indicate that there is too much content. This could indicate an error in your content or suggest that unauthorized content was added to your website without your knowledge or consent.

To combine both a minimum and maximum size error condition, click the {{< AppElement type="buttonSecondary" >}} +New check {{< /AppElement >}} button and set the thresholds.

## Check each resource individually (Full Page Check)

In addition to checking the sum of all resources, you can also run a check on individual elements. Select **Check each resource individually**, then select between checking if a certain percentage of resources fails to load at all or if a given percentage of all resources is above a maximum size.

To check if a certain percentage of resources fails, select **Resource fails to load** and fill in the percentage (upper limit) of resources that may fail to load. Beyond this limit an error will be generated.

![screenshot error condition individual resource fails](/img/content/scr_errorconditions-resources-individual-fail.min.png)

To check if a percentage or all resources together exceed a certain size, select **Resource size is over** and set the percentage, if applicable. Setting the percentage to 0% will check if there is a single resource that exceeds the limit. Setting the percentage to 100% will check if all resources together exceed the size limit.

![screenshot error condition individual resources are too big](/img/content/scr_errorconditions-resources-individual-percentage.min.png)

Note that once you have set the options and limits for your resource check, the heading will update to reflect your defined criteria.