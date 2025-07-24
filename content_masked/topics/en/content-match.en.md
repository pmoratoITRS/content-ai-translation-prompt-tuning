{
  "hero": {
    "title": "Error conditions - Page content"
  },
  "title": "Error conditions - Page content",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/error-conditions/content-match",
  "summary": "Content matches are a way to verify that the page you're monitoring is displaying the right content.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

There are situations when only half of your website's content loads properly. Missing sections, text, and paragraphs make it difficult for users to navigate your website. If you have an e-commerce site, this poor user experience affects your site's performance and causes you to lose sales without realizing it.

## Page content error condition

The Page content error condition ensures your website's content loads correctly and completely. It lets you specify any texts, phrases, and regular expressions and matches if this content is showing on your website.

![Page content error condition]([LINK_URL_1])

## Content match

A content match is a list of words you specify, which the monitor uses as a reference point to check against the website's loaded content:

- If a monitor checking the page *finds* the content, *no error* is reported.
- If a monitor checking the page *cannot find* the content, *an error* is reported.

## Content match for each monitor type

There are different types of content matches available for different monitor types. Content match varies depending on the monitor's category and which data it collects:

### Uptime monitors

Uptime monitors verify page content by making a GET request to your website's URL. Once the request is successful, the monitor validates the GET response content of your website.

If you are monitoring a website URL: [URL_1] examples of content checks are:

| Content match types | Examples |
|--|--|
| Document Object Model (DOM) or HTML elements | [SHORTCODE_1]
- [INLINE_CODE_1]
- [INLINE_CODE_2]
- [INLINE_CODE_3] 
[SHORTCODE_2] |
| [SHORTCODE_3] Text contents using [regular expression]([LINK_URL_2]) [SHORTCODE_4] | [SHORTCODE_5]
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
[SHORTCODE_6] |
| [SHORTCODE_7] [Advanced]([LINK_URL_3]) content match [SHORTCODE_8] | [SHORTCODE_9]
- [INLINE_CODE_4][SHORTCODE_10] |

### Browser monitors

Browser monitors verify page content by checking the website's page source. The page source is the website's raw structure in HTML format, including the page's metadata, scripts, and styling information.

If you are monitoring a website URL: [URL_2] examples of content checks are:

| Content match types | Examples |
|--|--|
| Document Object Model (DOM) or HTML elements | [SHORTCODE_11]
- [INLINE_CODE_5]
- [INLINE_CODE_6]
- [INLINE_CODE_7] 
[SHORTCODE_12] |
| [SHORTCODE_13] Text contents using [regular expression]([LINK_URL_4]) [SHORTCODE_14] | [SHORTCODE_15]
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
[SHORTCODE_16] |
| [SHORTCODE_17] [Advanced]([LINK_URL_5]) content match [SHORTCODE_18] | [SHORTCODE_19]
- [INLINE_CODE_8][SHORTCODE_20] |

[SHORTCODE_21] **Note:** To open your website's page source, go to your website and press the **Ctrl + U** key. Alternatively, right-click anywhere on the page and click **View page source**. Note that not all elements in the page source are valid content checks.[SHORTCODE_22]

### Multi-step API (MSA) monitors

MSA monitors check a content match through **Assertions**. Assertions let you define checks to validate if the API response meets your expected conditions. For example, if the response status code is 200 or if the response body as JSON contains specific texts. To learn more, refer to [MSA Assertions]([LINK_URL_6]).

### Transaction monitors

Transaction monitors validate page content by checking page elements shown in the browser. They check for specific text, buttons, images, and other UI elements visible on your website. Transaction monitor uses **Content checks**, which are actions configured for each step that verify if each page load turns out as expected. For example, it can check if the text "Successfully added to cart" appears on the page. To learn more, refer to [Content checks]([LINK_URL_7]).

## Types of content match

The following are content match types available for some monitor types:

### Regular content match {id = "regular-content-match"}

You can set up a content match using regular expressions. A regular expression (regex or regexp) is a special text string that describes a search pattern. You can specify a content match using:

- Single word: [INLINE_CODE_9]
- Multiple words or phrases in a particular order: [INLINE_CODE_10] (for example, product AND order must appear)
- Symbols to match any other elements:
  - [INLINE_CODE_11] — uses an exclamation mark to reverse or negate the meaning of a word. This content match means the word *error* should not be displayed.
  - [INLINE_CODE_12] — uses a vertical bar to match another word. This content match means the text [INLINE_CODE_13] OR [INLINE_CODE_14] should be visible on your website.

For more information, refer to [Regular Expression Language - Quick Reference]([LINK_URL_8]).


### Advanced content match

You can use multiple content matches at once by storing values in JSON format. If you want to combine two patterns, which can be any form of page elements and regular expressions, use:

[CODE_BLOCK_1]

Provide a valid content match in the [INLINE_CODE_15] field. Set [INLINE_CODE_16] to [INLINE_CODE_17] if the pattern should match your website content or [INLINE_CODE_18] if it doesn't match any website content.  

[SHORTCODE_23] **Note:** The Advanced content match works for HTTPS, Webservices HTTP and HTTPS, and Full Page Check monitors. [SHORTCODE_24]

If you want to check your website's timestamp for a content match, use:

[CODE_BLOCK_2]

The JSON key, [INLINE_CODE_19], can contain values in regex form, such as \[HTML_TAG_1], \[HTML_TAG_2], \[HTML_TAG_3], \[HTML_TAG_4], \[HTML_TAG_5], and \[HTML_TAG_6]. Any of these values can be extracted from the website's content and will be merged with the current server time and then evaluated in terms of UTC.

The [INLINE_CODE_20] is the number of minutes that should be subtracted to compare it to server time in UTC. If the webpage contains a timestamp in UTC\+1, the offset should be 60. If the webpage includes a timestamp in EST (UTC-5), the offset should be -300.

The [INLINE_CODE_21] refers to the maximum time difference in minutes that is allowed between the website's page time and your local time. For example, if your local time is 10:06 and your website's page time is 10:00, an error will occur if the [INLINE_CODE_22] is set to 5 minutes or less.

## Where to configure a content match

To configure a content match, you have to add an error condition of type **Check page content**:

1. Go to the [SHORTCODE_25] Monitoring > Monitor setup [SHORTCODE_26].
2. Click the monitor to which you'd like to add a content match.  
3. Navigate to the [SHORTCODE_27] Error conditions [SHORTCODE_28] tab.  
4. In the **Check page content**, enter your content match information.
5. Click [SHORTCODE_29] Save [SHORTCODE_30] to confirm the monitor changes.

Once done, you can [create an alert definition]([LINK_URL_9]) to get notified when the **Check page content** error condition is met.
