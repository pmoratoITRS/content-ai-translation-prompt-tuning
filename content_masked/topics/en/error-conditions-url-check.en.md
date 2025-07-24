{
  "hero": {
    "title": "Error conditions - Check URLs loaded by the page"
  },
  "title": "Error conditions - Check URLs loaded by the page",
  "summary": "Using the 'Check URLs loaded by the page' error condition",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Browser-based monitoring types, such as [Full Page Check]([LINK_URL_1]) and [Transaction]([LINK_URL_2]) monitors, load your pages in an actual browser. Upon loading, the browser generates a [waterfall chart]([LINK_URL_3]) that lists all the page elements and resources loaded on your website.

These loaded elements include first-party content, such as the original HTML document, images, videos, and other media hosted on the same network. They may also include third-party content or external resources, such as monitoring scripts or analytics. Each of these elements appears as an individual entry in the waterfall chart, with its own request URL and load time metrics.

## Check URLs loaded by the page error condition

The **Check URLs loaded by the page** [error condition]([LINK_URL_4]) checks whether specific page elements are loaded on your website. It verifies if the request URL of these elements appears in the waterfall chart or not.

For example, you want to check if the [Uptrends Real User Monitoring]([LINK_URL_5]) loads on a page. Adding the **Check URLs loaded by the page** error condition tells the monitor to verify if the request URL of any of the waterfall elements matches [INLINE_CODE_1].

Additionally, this error condition allows you to set specific criteria for checking each request URL's metrics. For example, if you want to detect errors when your [INLINE_CODE_2] image takes longer than 2 seconds to load or if a file returns a status code higher than 400, you can define criteria for each.

## Set up Check URLs loaded by the page

To check if a specific page element is visible on your website, you need to add an error condition of the type **Check URLs loaded by the page**:

1. Go to [SHORTCODE_1] Monitoring > Monitor setup [SHORTCODE_2] menu.
2. Click the monitor to which you'd like to check a request URL.
3. Go to the [SHORTCODE_3] Error conditions [SHORTCODE_4] tab.
4. In the **Check URLs loaded by the page**, click the [SHORTCODE_5] +New check [SHORTCODE_6] button.
5. Select an error type to determine whether the monitor should generate an error when the request URL appears or does not appear in the waterfall chart.
6. Provide the request URL in the text input field. You can use regular expressions as values.
7. (Optional) To set additional criteria for checking the request URL, click the [SHORTCODE_7] +Add additional condition [SHORTCODE_8] button. Then set your conditions using the available options:

  - Select the **Response size**, the appropriate comparison operator, and the value in bytes (B).
  - Select the **Total time**, the appropriate comparison operator, and the value in milliseconds (ms).
  - Select the **Status code**, the appropriate comparison operator, and the value.

8. Click the [SHORTCODE_9] Save [SHORTCODE_10] button to confirm the monitor changes.

![Additional conditions for Check URLs loaded by the page]([LINK_URL_6])

## Examples

### Uptrends RUM script loads on the website

The example shows the error condition checking if the Uptrends RUM script has been correctly configured. If the [INLINE_CODE_3] request URL is not in the list of loaded page elements, the monitor will generate [an error]([LINK_URL_7]).

![Check URL: Uptrends RUM]([LINK_URL_8])

### Image loads on the website

The example shows the error condition checking if the request URL, [INLINE_CODE_4], appears in the list of loaded page elements for more than 1000 milliseconds. If the URL's load time exceeds the total time, the monitor will generate [an error]([LINK_URL_9]).

![Check URL: Stars.[FILE_PATH_1]]([LINK_URL_10])