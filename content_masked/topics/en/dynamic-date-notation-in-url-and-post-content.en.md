{
  "hero": {
    "title": "Dynamic values in URLs and POST content"
  },
  "title": "Dynamic values in URLs and POST content",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/dynamic-values-in-url-and-post-content",
  "summary": "A guide on including dynamic values in URLs or request bodies.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Dynamic value in URL or request body

Uptrends can generate [dynamic date values]([LINK_URL_1]) in URLs or HTTP request content, for most monitor types. Timestamps are commonly used, because not only are they unique values, they also contain information about when the request was executed. This can be useful for web services that require a different value to be entered as part of the request body for a HTTP POST or the request URL, for example:

[INLINE_CODE_1]

Rather than entering a fixed value date, we can use the following notation to generate values based on today’s date/time:

[INLINE_CODE_2]

Please note that **other format values are also possible**. Additionally, we can use offsets to calculate different values. For more information on the notation, and how to apply offsets to your date values, see our article on [automatic variables]([LINK_URL_2]).


## Cache busting

**Content caching** can be incredibly useful for any webmaster, because it can improve overall performance by using fewer resources over time. But if you’re monitoring a website or service, caching can make it difficult to know whether one of your page elements is truly up or down.

By inserting a random URL value, you can bust the cache for any *HTTP*, *Web Service*, or *Full Page Check* call, and ensure that no previous content is cached.

[SHORTCODE_1]
**Note:** The following information is about server side caching on your side, not on the side of the Uptrends' website monitoring service.
[SHORTCODE_2]

### How does cache busting work?

Cache busting is made possible by using the [INLINE_CODE_3] token (see our [knowledge base article on automatic variables for more information)]([LINK_URL_3]). To use this feature, simply enter the token as part of the URL in the monitor settings, for example:

[INLINE_CODE_4]

Which gets resolved as something like:

[INLINE_CODE_5]
