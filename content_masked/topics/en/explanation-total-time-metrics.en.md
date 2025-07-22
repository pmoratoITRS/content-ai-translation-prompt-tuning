{
  "hero": {
    "title": "Explanation of total time metrics"
  },
  "title": "Explanation of Total Time Metrics",
  "url": "[URL_BASE_TOPICS]dashboards-and-reporting/dashboards/explanation-total-time-metrics",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

One of the most useful functions of the Uptrends service is the ability to hone in on your website, server, and web application uptime and performance data. But sometimes it can be tough to know just what this data actually represents!

Below you’ll learn about the different “*Total Time Metrics*,” and what they actually mean:

## Resolve

**Resolve Time** is the time that it takes to translate a domain name or URL to a corresponding IP address.

For each monitor where a URL or domain name was specified to connect to a webpage or server, we will need to perform a translation in order to connect, through a DNS query. (Just like how your browser works when you load a webpage!)

## Connection time

**Connection Time** represents the time it takes to connect to the IP address of your webpage or server.

## Download time

**Download Time** is the time after the connection to your webpage or server has been made, where the download request is performed. It indicates the time between the start of the actual request, and the moment the action is completed.

## Total time

**Total Time** is the total amount of time it takes to complete a monitor check. (The sum of resolve time, connection time, and download time.)
