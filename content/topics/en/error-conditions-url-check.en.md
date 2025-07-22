{
  "hero": {
    "title": "Error conditions - Check URLs loaded by the page"
  },
  "title": "Error conditions - Check URLs loaded by the page",
  "summary": "Using the 'Check URLs loaded by the page' error condition",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-url-check",
  "tableofcontents": true
}

Browser-based monitoring types, such as [Full Page Check]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) and [Transaction]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="en" >}}) monitors, load your pages in an actual browser. Upon loading, the browser generates a [waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}) that lists all the page elements and resources loaded on your website.

These loaded elements include first-party content, such as the original HTML document, images, videos, and other media hosted on the same network. They may also include third-party content or external resources, such as monitoring scripts or analytics. Each of these elements appears as an individual entry in the waterfall chart, with its own request URL and load time metrics.

## Check URLs loaded by the page error condition

The **Check URLs loaded by the page** [error condition]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) checks whether specific page elements are loaded on your website. It verifies if the request URL of these elements appears in the waterfall chart or not.

For example, you want to check if the [Uptrends Real User Monitoring]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="en" >}}) loads on a page. Adding the **Check URLs loaded by the page** error condition tells the monitor to verify if the request URL of any of the waterfall elements matches `hit.uptrends.com/.*`.

Additionally, this error condition allows you to set specific criteria for checking each request URL's metrics. For example, if you want to detect errors when your `uptrends.png` image takes longer than 2 seconds to load or if a file returns a status code higher than 400, you can define criteria for each.

## Set up Check URLs loaded by the page

To check if a specific page element is visible on your website, you need to add an error condition of the type **Check URLs loaded by the page**:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}} menu.
2. Click the monitor to which you'd like to check a request URL.
3. Go to the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.
4. In the **Check URLs loaded by the page**, click the {{< AppElement type="buttonSecondary" >}} +New check {{< /AppElement >}} button.
5. Select an error type to determine whether the monitor should generate an error when the request URL appears or does not appear in the waterfall chart.
6. Provide the request URL in the text input field. You can use regular expressions as values.
7. (Optional) To set additional criteria for checking the request URL, click the {{< AppElement type="buttonSecondary" >}} +Add additional condition {{< /AppElement >}} button. Then set your conditions using the available options:

  - Select the **Response size**, the appropriate comparison operator, and the value in bytes (B).
  - Select the **Total time**, the appropriate comparison operator, and the value in milliseconds (ms).
  - Select the **Status code**, the appropriate comparison operator, and the value.

8. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to confirm the monitor changes.

![Additional conditions for Check URLs loaded by the page](/img/content/gif-additional-conditions-check-urls-loaded-by-page.gif)

## Examples

### Uptrends RUM script loads on the website

The example shows the error condition checking if the Uptrends RUM script has been correctly configured. If the `hit.uptrends.com/.*` request URL is not in the list of loaded page elements, the monitor will generate [an error]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}).

![Check URL: Uptrends RUM](/img/content/scr-error-conditions-url-check.min.png)

### Image loads on the website

The example shows the error condition checking if the request URL, `stars.png`, appears in the list of loaded page elements for more than 1000 milliseconds. If the URL's load time exceeds the total time, the monitor will generate [an error]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}).

![Check URL: Stars.png](/img/content/scr-error-conditions-url-check-image.min.png)