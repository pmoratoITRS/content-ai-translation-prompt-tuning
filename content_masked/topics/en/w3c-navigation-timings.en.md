{
  "hero": {
    "title": "W3C navigation timings"
  },
  "title": "W3C navigation timings",
  "summary": "Description of the W3C navigation timing metrics as shown in the Full Page Check and transaction monitoring waterfalls",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-results/w3c-navigation-timings",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The **World Wide Web Consortium** (or W3C for short) is an international organization, involved in developing standards for the world wide web. As such, it has defined a standard for browsers and web applications to generate and display timing information regarding the loading of webpages. The complete specification of the standard can be found on the [W3C website (Copyright © 2012, World Wide Web Consortium)]([LINK_URL_1]).

Uptrends' [Full Page Check (FPC)]([LINK_URL_2]) and [transaction]([LINK_URL_3]) monitor types come with the option to display a subset of W3C navigation timing metrics (plus some additional information such as [Core web vitals]([LINK_URL_4])). This article will provide you with an overview of the metrics shown and what they mean exactly. 

For illustration, the following image shows all navigation timing events as defined by the W3C, on a timeline.

![w3c navigation timings]([LINK_URL_5])
(Copyright © 2012, [World Wide Web Consortium]([LINK_URL_6]))

## Metrics

This is an overview of the W3C navigation timing metrics you can find in Uptrends' Full Page Checks. 

![W3C navigation timings in Uptrends]([LINK_URL_7])

- **Request start**: Equal to the [INLINE_CODE_1] as defined by the W3C. It is a timestamp indicating when the browser starts requesting the resource from the web server after the DNS lookup and TCP connection. 
- **Time to first byte**: Equal to the difference between [INLINE_CODE_2] and [INLINE_CODE_3] as defined by the W3C. In short, it's the time between when the first request was sent from browser to server, and when the first byte of the following response was received by the browser (this includes any redirects, and SSL/TCP connections). 
- **DOM interactive**: Equal to [INLINE_CODE_4] as defined by W3c. It is a timestamp, indicating the document readiness is set to "interactive", to indicate that the browser has stopped parsing the page and the user can start interacting with it. Resources such as scripts, images, stylesheets, or frames may still be loading. 
- **DOM completed**: Equal to the [INLINE_CODE_5] as defined by W3C. It is a timestamp, indicating when the main document has been parsed, the DOM has been fully loaded, and the page readiness is set to "complete".
- **Load event**: Equal to [INLINE_CODE_6] as defined by W3C. It is a timestamp, indicating when the load event of the current document has completed, including all dependent resources such as stylesheets and images.

## Dashboard reporting

You can report all the metrics on a custom dashboard. Just add a custom report tile of the type [Simple data list / chart]([LINK_URL_8]). Then click the settings button  [SHORTCODE_1] [SHORTCODE_2] on the tile and choose the values you want to show by checking their check boxes. 

You can show the W3C navigation metrics of a transaction monitor per individual step. You have to activate the *Waterfall* and the *Performance metrics* options for each step that you want to view in the graph. See the information on [step settings]([LINK_URL_9]) for how this works.

![screenshot detail tile settings]([LINK_URL_10])
