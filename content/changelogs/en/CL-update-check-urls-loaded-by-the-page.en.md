{
  "title": "Additional conditions for Check URLs loaded by the page",
  "date": "2025-02-19",
  "url": "/changelog/february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition"
}

The [Check URLs loaded by the page]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="en" >}}) is an error condition that checks if specific page elements are loaded on your website. These page elements are the URLs displayed in your [Waterfall chart]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}), including images, files, and other website resources.

This error condition now allows you to set extra criteria for checking each page element's metrics. By clicking the new {{< AppElement type="editbutton" >}} +Add additional condition{{< /AppElement >}} button, you can now specify the page element's response size in bytes (B), total time in milliseconds (ms), and status code:

![Additional conditions for Check URLs loaded by the page](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

If you want to get errors when your image loads longer than 2 seconds or if a file results in a status code higher than 400, you can add specific criteria for each.

The Check URLs loaded by the page error condition are available for [Browser or Full-Page checks]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="en" >}}) and [Transaction]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}) monitors. Note that for transaction monitors, you need to select the [Waterfall option in a step]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="en" >}}) to set the additional conditions.