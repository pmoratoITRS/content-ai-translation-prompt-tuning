{
  "hero": {
    "title": "URL handling in Uptrends RUM"
  },
  "title": "URL handling in Uptrends RUM",
  "summary": "Ever wondered how Uptrends handles URLs in Real User Monitoring? Give this article a read!",
  "url": "/support/kb/rum/url-handling-in-uptrends-rum",
  "translationKey": "https://www.uptrends.com/support/kb/rum/url-handling-in-uptrends-rum"
}

Uptrends RUM allows you to view your real user performance metrics in many different groupings. Grouping by page gives you great insights into statistics for specific pages that may need attention due to issues like slow load times.

Uptrends looks at the URL to determine which page your visitor viewed. Many modern websites use automatically generated URLs that could lead to an extremely large number of unique URLs. As it wouldn't be useful to gather data for tens of thousands of pages, **we've capped the maximum number of unique pages per website to 10,000 by default**. When you exceed this number, we register new unique pages under "Other."

## URL normalization

To reduce the number of unique URLs that we need to keep track of while still properly separating your website's different pages, we apply a **URL normalization process**. URL normalization means that the URLs you see in Uptrends RUM may differ slightly from the actual URLs your website uses. In particular, we:

-   Ignore the difference between `http://` and `https://`
-   Remove the query string (e.g. `?parameter=value` at the end)
-   Remove fragments (e.g. `#fragment` at the end) except if the option **Include URL fragment** is enabled in the RUM website settings
-   Remove double slashes from the path part of the URL
-   Replace segments (parts of the path delimited by forward slashes) that consist entirely of numbers or GUIDs with asterisks (`***`)
-   Replace long numbers (&gt;4 digits) and guids in segments with asterisks. For example, `www.mysite.com/coupon-12345` and `www.mysite.com/coupon-123456` both become `www.mysite.com/coupon-***`  
    URLs with guids such as `www.mysite.com/coupon-19740f6e-e7e6-41f2-84e4-de0b290eb05e` become `www.mysite.com/coupon-***` with the three asterisks replacing the entire guid.

## Feedback

We're happy to receive your questions and feedback. Don't hesitate to [contact us](/contact), especially if you notice Uptrends RUM isn't optimally keeping track of your website's different pages.
