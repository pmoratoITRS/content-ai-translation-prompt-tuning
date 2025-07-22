{
  "hero": {
    "title": "URL and analytics blocking"
  },
  "title": "URL and analytics blocking",
  "summary": "Blocking analytics and other URLs in your Full Page Checks, Real Browser, and Transaction monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/analytics-blocking",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]
**Note:** URL and analytics blocking are available to [Enterprise- & Business-level accounts]([LINK_URL_1]) only.
[SHORTCODE_2]

Full Page Check (FPC) and Transaction monitor types load your webpage into a browser along with all the elements on the page including Google Analytics scripts and other third party elements. The page loading into the checkpoint’s browser triggers genuine page views in your web analytics. If your website monitoring skews your analytics too much or if there's another reason you don't want particular elements loaded into the browser, you have two options:

-   Block Google Analytics
-   URL blocking

[SHORTCODE_3]
**Note:** Don’t worry about your HTTP(S) monitors messing with your analytics; HTTP(S) checks do not load your page into a browser, so your monitoring checks won’t show up in your analytics anyway.
[SHORTCODE_4]

## How does request blocking work?

When you open up the waterfall chart, you'll still see the blocked element requests. Why is that? Well, we can't simply tell the browser not to load those URLs, so instead, we bypass those requests as soon as we see them and prevent them from going out onto the Internet. Google Analytics will never see those requests, so your analytics remain safe. The browser still needs an answer for those requests, so to not disrupt the normal HTTP behavior expected by the browser, we instead return a normal response header with a 200 OK status and a body content of 512 bytes.

## How does request blocking affect my reports?

Blocking doesn’t affect your reporting much; we still show you when the browser would have downloaded a blocked element, and we stop any requests those elements generate. So that you know the check blocked the element, the element appears with a strikethrough in your waterfall report. The strikethroughs tell you exactly which requests the check intercepted based on your monitor’s block settings.

![]([LINK_URL_2])

## When blocking Google Analytics, what gets blocked?

Google offers a suite of services that include more than just analytics; therefore Uptrends blocks the most common Google elements. When you select to block Google Analytics Uptrends blocks:

-   google-analytics.com
-   stats.g.doubleclick.net
-   googleadservices.com
-   google.com/ads

Uptrends **does not block** googletagmanager.com, so as not to disrupt pages that have a dependency on the elements functionality.

## How do I block Google Analytics?

Because so many sites use Google Analytics, we include a checkbox in your monitor settings.

1.  Go to your monitor’s settings
2.  Select the [SHORTCODE_7]Advanced[SHORTCODE_8] tab
3.  Select the checkbox labeled **Block Google Analytics**.
4.  Click [SHORTCODE_9]Save[SHORTCODE_10].

That’s it! You’re done. If you have other elements you need to block, read on.

## How do I block other URLs and other elements?

You may want to block an URL for a variety of reasons such when performing A/B testing. With Uptrends monitoring, you can block as many elements as you need.

1.  Go to your monitor settings
2.  Select the [SHORTCODE_11]Advanced[SHORTCODE_12] tab.
3.  Type the full or partial URL for the element you wish to block into the box labeled **Block these (parts of) URLs**.
4.  Place each URL on its own line.
5.  Click [SHORTCODE_13]Save[SHORTCODE_14]

When the checkpoint sees an outgoing request that contains any URL or character strings found in this box, the checkpoint will block the request. Need further help with element blocking, [ask our experts]([LINK_URL_3])!

[SHORTCODE_5]
**Note:** Blocking URLs may or may not break your page and cause needless alerts. If you need help, [let us know]([LINK_URL_4]).
[SHORTCODE_6]
