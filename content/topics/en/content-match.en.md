{
  "hero": {
    "title": "Error conditions - Page content"
  },
  "title": "Error conditions - Page content",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match",
  "summary": "Content matches are a way to verify that the page you're monitoring is displaying the right content.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/content-match"
}

There are situations when only half of your website's content loads properly. Missing sections, text, and paragraphs make it difficult for users to navigate your website. If you have an e-commerce site, this poor user experience affects your site's performance and causes you to lose sales without realizing it.

## Page content error condition

The Page content error condition ensures your website's content loads correctly and completely. It lets you specify any texts, phrases, and regular expressions and matches if this content is showing on your website.

![Page content error condition](/img/content/scr-error-condition-page-content.min.png)

## Content match

A content match is a list of words you specify, which the monitor uses as a reference point to check against the website's loaded content:

- If a monitor checking the page *finds* the content, *no error* is reported.
- If a monitor checking the page *cannot find* the content, *an error* is reported.

## Content match for each monitor type

There are different types of content matches available for different monitor types. Content match varies depending on the monitor's category and which data it collects:

### Uptime monitors

Uptime monitors verify page content by making a GET request to your website's URL. Once the request is successful, the monitor validates the GET response content of your website.

If you are monitoring a website URL: https://galacticresorts.com/, examples of content checks are:

| Content match types | Examples |
|--|--|
| Document Object Model (DOM) or HTML elements | {{< tableformatter >}}
- `<title>Home Page - GalacticResorts.com</title>`
- `<a class="btn btn-primary btn-lg" href="/Products/Index/97f8fcc9-11b5-4d86-b208-ccb6d2be35e3">Book now!</a>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Text contents using [regular expression]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="en" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
{{< /tableformatter >}} |
| {{< tableformatter >}} [Advanced]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="en" >}}) content match {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "GalacticResottt", "IsPositive": false }]`{{< /tableformatter >}} |

### Browser monitors

Browser monitors verify page content by checking the website's page source. The page source is the website's raw structure in HTML format, including the page's metadata, scripts, and styling information.

If you are monitoring a website URL: https://galacticresorts.com/, examples of content checks are:

| Content match types | Examples |
|--|--|
| Document Object Model (DOM) or HTML elements | {{< tableformatter >}}
- `<h2>Norcadia Prime</h2>`
- `<li><a href="/APIHelp" target="_blank">API</a></li>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Text contents using [regular expression]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="en" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
{{< /tableformatter >}} |
| {{< tableformatter >}} [Advanced]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="en" >}}) content match {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "Holiday destinations", "IsPositive": true }]`{{< /tableformatter >}} |

{{< callout >}} **Note:** To open your website's page source, go to your website and press the **Ctrl + U** key. Alternatively, right-click anywhere on the page and click **View page source**. Note that not all elements in the page source are valid content checks.{{< /callout >}}

### Multi-step API (MSA) monitors

MSA monitors check a content match through **Assertions**. Assertions let you define checks to validate if the API response meets your expected conditions. For example, if the response status code is 200 or if the response body as JSON contains specific texts. To learn more, refer to [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="en" >}}).

### Transaction monitors

Transaction monitors validate page content by checking page elements shown in the browser. They check for specific text, buttons, images, and other UI elements visible on your website. Transaction monitor uses **Content checks**, which are actions configured for each step that verify if each page load turns out as expected. For example, it can check if the text "Successfully added to cart" appears on the page. To learn more, refer to [Content checks]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="en" >}}).

## Types of content match

The following are content match types available for some monitor types:

### Regular content match {id = "regular-content-match"}

You can set up a content match using regular expressions. A regular expression (regex or regexp) is a special text string that describes a search pattern. You can specify a content match using:

- Single word: `Uptrends`
- Multiple words or phrases in a particular order: `product.*order` (for example, product AND order must appear)
- Symbols to match any other elements:
  - `!error` — uses an exclamation mark to reverse or negate the meaning of a word. This content match means the word *error* should not be displayed.
  - `On Sale|Best Sellers` — uses a vertical bar to match another word. This content match means the text `On Sale` OR `Best Sellers` should be visible on your website.

For more information, refer to [Regular Expression Language - Quick Reference](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference).


### Advanced content match

You can use multiple content matches at once by storing values in JSON format. If you want to combine two patterns, which can be any form of page elements and regular expressions, use:

```json
    [
      {
        "Pattern": "PhraseA",
        "IsPositive": true
      },
      { 
        "Pattern": "PhraseB", 
        "IsPositive": false 
      }
    ]
```

Provide a valid content match in the `Pattern` field. Set `IsPositive` to `true` if the pattern should match your website content or `false` if it doesn't match any website content.  

{{< callout >}} **Note:** The Advanced content match works for HTTPS, Webservices HTTP and HTTPS, and Full Page Check monitors. {{< /callout >}}

If you want to check your website's timestamp for a content match, use:

```json
    [
    {
      "Pattern": "some content before the timestamp value (?<hour>\\d\\d):(?<minute>\\d\\d)",
      "IsPositive": true,
      "DateTime": { 
        "OffsetUTC": 60, 
        "MaxDifference": 5 
      } 
    } 
    ]
```

The JSON key, `Pattern`, can contain values in regex form, such as \<year\>, \<month\>, \<day\>, \<hour\>, \<minute\>, and \<second\>. Any of these values can be extracted from the website's content and will be merged with the current server time and then evaluated in terms of UTC.

The `OffsetUTC` is the number of minutes that should be subtracted to compare it to server time in UTC. If the webpage contains a timestamp in UTC\+1, the offset should be 60. If the webpage includes a timestamp in EST (UTC-5), the offset should be -300.

The `MaxDifference` refers to the maximum time difference in minutes that is allowed between the website's page time and your local time. For example, if your local time is 10:06 and your website's page time is 10:00, an error will occur if the `MaxDifference` is set to 5 minutes or less.

## Where to configure a content match

To configure a content match, you have to add an error condition of type **Check page content**:

1. Go to the {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click the monitor to which you'd like to add a content match.  
3. Navigate to the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.  
4. In the **Check page content**, enter your content match information.
5. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm the monitor changes.

Once done, you can [create an alert definition]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="en" >}}) to get notified when the **Check page content** error condition is met.
