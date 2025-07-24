{
  "hero": {
    "title": "Non-primary checkpoints"
  },
  "title": "Non-primary checkpoints",
  "summary": "Learn why Uptrends designates some checkpoints as non-primary, and what you need to know before choosing to use them.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/non-primary-checkpoints",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

You may have noticed when selecting your checkpoints that we've designated some checkpoints *as non-primary*. Non-primary checkpoints are checkpoints subject to intermittent availability and possibly reduced bandwidth due to the local Internet infrastructure and government control.

By default, we've chosen to exclude the non-primary checkpoints when you select a region that includes them (see below), but that doesn't mean that we don't want you using them. We've excluded them so that we can make sure that you are aware that these checkpoints are subject to volatile conditions, and that they may adversely affect your uptime and performance reporting when you elect to use them. To use the non-primary checkpoints, uncheck the **Use only primary checkpoints** box.

![]([LINK_URL_1])

## I'm only testing in areas that have non-primary checkpoints, but I see tests from other checkpoints. Why?

Although it is important to test from your user's location, if that location becomes unavailable for testing, you still want to know the status of your website or service. Rather than let your site or service go untested during periods of limited or no connectivity to non-primary checkpoints, Uptrends will use other checkpoints for testing so that you will capture outages and performance problems that may occur in the meantime.
