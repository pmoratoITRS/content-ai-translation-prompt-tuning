{
  "hero": {
    "title": "RUM and user privacy"
  },
  "title": "RUM and user privacy",
  "summary": "Tracking real user performance data may bring up privacy concerns for your brand. Learn how Uptrends protects users privacy and what you need to know.",
  "url": "[URL_BASE_TOPICS]rum/rum-and-user-privacy",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Protecting user privacy is important. In this article we explain how Uptrends uses your visitor's information and further steps you can take to protect your brand and your user's privacy.

## Privacy, personal data and the Data Protection Act

When one of your website visitors accesses your site, the RUM script in your pages send a small request to Uptrends. It's in the very nature of the Internet that we also receive the visitor's IP address with the request. We recognize the sensitive nature of receiving this information since systems can use the IP address to identify and track individual users. We designed RUM from the ground up to make sure that you have complete control of how your visitors' IP addresses are processed. The two key aspects for this are:

-   We offer multi-level IP address anonymization
-   We do not store IP address long term

### Multi-level IP address anonymization

To provide you with your visitor's originating country (and in some instances state level information for Australia, Canada, and the US), Uptrends uses the IP address. **Uptrends does not identify, collect personal data from, nor track your site’s visitors.** However, if your application’s privacy policy does not allow Uptrends to use your visitor's full IP address in any way, we offer two levels of anonymization:

-   **Level 0:** The full IP address is used. This is the default setting.
-   **Level 1**: We set the last (most identifying) octet of the IP address to zero before inspection.
-   **Level 2**: We set the last two octets of the IP address to zero before inspection.

**Example:** using Level 1, we process the end user’s original IP address [INLINE_CODE_1] and it becomes [INLINE_CODE_2]. Likewise, using Level 2 anonymization yields [INLINE_CODE_3].

[SHORTCODE_1]
**Note:** Uptrends does not store original or anonymized IP addresses long term (see below).
[SHORTCODE_2]

By taking out the most significant parts of the IP address (in terms of uniquely identifying a network address), we only get a very general sense of the location of each visitor. Consequently, the higher the level of anonymization, the less accurate the country and state information becomes.

### Specifying the anonymization level

If you don't need any IP anonymization, you can use the normal RUM script as-is without any additional configuration. Level 1 or 2 require a very small change in the script.

In the RUM script included in your web pages, you'll notice that the [INLINE_CODE_4] parameter is set to 0 by default. Please **set its value to 1 for Level 1 anonymization**, and **use 2 for Level 2 anonymization**.

For example:

[INLINE_CODE_5]

The script sends the anonymization value along with each RUM request executed as part of your web pages, and your specified anonymization level takes effect immediately.

### No long-term storage of IP addresses

If you decide to use IP anonymization, we guarantee that we will not inspect the original IP addresses, nor shall we store the original IP addresses neither in memory, on disk, or any other storage facility or device. The very first step in our pipeline is to anonymize the IP addresses before we examine them in any way.

Furthermore, **we only retain the IP address information temporarily** until we’ve processed the original request through our entire pipeline. After that, we purge the information. The purge includes any combination of IP address information, user agent data, URLs, dates, times, and time zone information.

## Real User Monitoring and your privacy statement

Sometimes Real User Monitoring customers ask what they need to add to their privacy statement on their website. Of course, we aren’t lawyers, but you may want to copy and paste the following paragraph into your privacy policy.

*&lt;Your brand name here&gt; uses Uptrends’ Real User Monitoring to track the performance users experience while visiting our website. Uptrends does not use cookies to collect data or track our site's users; instead, Uptrends uses a small script file on our pages that sends performance data about our site's visitors to the Uptrends servers. The data collected from each user includes IP addresses, device types, operating systems, and browsers used. Uptrends’ servers aggregate the performance data of all of our site’s visitors and provide us with information that allows us to improve the user experience on our site based on the above information. Uptrends uses the individual IP addresses of our site's visitors to gather information about the visitor’s state or country and nothing more. Also, Uptrends does not store any IP addresses long term, nor does Uptrends track or share information about any individual user with third-parties.*

### Optionally include this in your privacy statement if you use anonymization levels 1 or 2

*To protect your privacy, the version of the Uptrends script file we've included in our site is set to make your IP address anonymous before it is processed. Your IP address is never stored, and it is never used in any way other than determining your country of origin.*
