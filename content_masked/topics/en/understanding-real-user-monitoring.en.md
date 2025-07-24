{
  "hero": {
    "title": "Understanding Real User Monitoring"
  },
  "title": "Understanding Real User Monitoring",
  "summary": "In this article you can find the basic RUM concepts and how RUM works. ",
  "url": "[URL_BASE_TOPICS]rum/understanding-real-user-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In this article, the basic concepts and the theory of the setup is explained.

## What is Real User Monitoring?

When it comes to measuring the performance experienced by your site's actual users, you can't beat Real User Monitoring (RUM). RUM records your RUM enabled page's performance, aggregates the data, and displays the data in interactive dashboards where you can compare performance based on page viewed, device, browser and version, operating system and version, and user location.

RUM is a passive approach to monitoring because it relies on your users accessing your site to generate data. If your site goes down, your users can't access the site, and, as a result, there is no data to report. That is where your synthetic or active monitoring comes in. Your [synthetic monitors]([LINK_URL_1]) such as Uptime monitors, Performance monitors, API monitors, and Transaction monitors check your site on a regular basis, and if they experience a problem, we let you know about it right away using your [alerting settings]([LINK_URL_2]).

## How does Real User Monitoring work?

You place a tiny, [non-invasive script]([LINK_URL_3]) in the [INLINE_CODE_1] tags on the pages you would like to track with RUM. When your users access a RUM enabled page, the script records the page's performance. Once the page finishes loading, the script bundles the performance data with information about the user's environment and location and sends it to the cloud. Uptrends retrieves the data [in almost real time]([LINK_URL_4]) and displays it in your rum dashboards. The result is a comprehensive picture of your site's actual performance as experienced by your users. If you're concerned about user privacy, please read the article about [RUM and user privacy]([LINK_URL_5]).

## What does a RUM script look like?

Uptrends' engineers designed the RUM script to be as non-invasive as possible. The small script loads fast with virtually no impact on page performance. It does its work in the background as the page load progresses, and after the page load completes, the script finishes by sending the user data and performance data to the cloud. Your script will look similar to the script below.
[CODE_BLOCK_1]
