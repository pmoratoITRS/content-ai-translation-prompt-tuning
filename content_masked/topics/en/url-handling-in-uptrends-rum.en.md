{
  "hero": {
    "title": "URL handling in Uptrends RUM"
  },
  "title": "URL handling in Uptrends RUM",
  "summary": "Ever wondered how Uptrends handles URLs in Real User Monitoring? Give this article a read!",
  "url": "[URL_BASE_TOPICS]rum/url-handling-in-uptrends-rum",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends RUM allows you to view your real user performance metrics in many different groupings. Grouping by page gives you great insights into statistics for specific pages that may need attention due to issues like slow load times.

Uptrends looks at the URL to determine which page your visitor viewed. Many modern websites use automatically generated URLs that could lead to an extremely large number of unique URLs. As it wouldn't be useful to gather data for tens of thousands of pages, **we've capped the maximum number of unique pages per website to 10,000 by default**. When you exceed this number, we register new unique pages under "Other."

## URL normalization

To reduce the number of unique URLs that we need to keep track of while still properly separating your website's different pages, we apply a **URL normalization process**. URL normalization means that the URLs you see in Uptrends RUM may differ slightly from the actual URLs your website uses. In particular, we:

-   Ignore the difference between [INLINE_CODE_1] and [INLINE_CODE_2]
-   Remove the query string (e.g. [INLINE_CODE_3] at the end)
-   Remove fragments (e.g. [INLINE_CODE_4] at the end) except if the option **Include URL fragment** is enabled in the RUM website settings
-   Remove double slashes from the path part of the URL
-   Replace segments (parts of the path delimited by forward slashes) that consist entirely of numbers or GUIDs with asterisks ([INLINE_CODE_5])
-   Replace long numbers (&gt;4 digits) and guids in segments with asterisks. For example, [INLINE_CODE_6] and [INLINE_CODE_7] both become [INLINE_CODE_8]  
    URLs with guids such as [INLINE_CODE_9] become [INLINE_CODE_10] with the three asterisks replacing the entire guid.

## Feedback

We're happy to receive your questions and feedback. Don't hesitate to [contact us]([LINK_URL_1]), especially if you notice Uptrends RUM isn't optimally keeping track of your website's different pages.
