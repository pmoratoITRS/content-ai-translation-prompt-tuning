{
  "hero": {
    "title": "Error conditions - W3C metric checks"
  },
  "title": "Error conditions - W3C metric checks",
  "summary": "Using thresholds on W3C metrics to trigger errors.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The World Wide Web Consortium (or W3C for short) is an international organization, involved in developing standards for the world wide web. As such, it has defined a standard for browsers and web applications to generate and display timing information regarding the loading of webpages. 

[Browser and transaction monitor types]([LINK_URL_1]) measure and report the [W3C navigation timing metrics]([LINK_URL_2]). These metrics are reported in the monitor check details and you can set error conditions on them. Conditions for W3C metrics are part of the [Error conditions]([LINK_URL_3]).

Note that different monitor types offer different error conditions. Check the table in [Which error conditions are available?]([LINK_URL_4]) to find out which options are available for certain monitor types.

## Define error conditions based on the W3C metrics

To define error conditions that use the W3C navigation timing:

1. Go to [SHORTCODE_1] Monitoring > Monitor setup [SHORTCODE_2].
2. Click on the monitor's name to edit it.
3. Open the [SHORTCODE_3] Error conditions [SHORTCODE_4] tab.
4. Expand the *Check W3C metrics* category by clicking the arrow in front.
 
   ![screenshot w3c metrics error condition]([LINK_URL_5])

5. Enable error conditions by ticking the check box and setting a value. Leave any metrics disabled that you don't want to assign to an error condition.
6. Click the [SHORTCODE_5] Save [SHORTCODE_6] button.

## The W3C metrics [ANCHOR_1]

The W3C metrics that are explained in the knowledge base article [W3C navigation timing metrics]([LINK_URL_6]). The metrics correspond to the error conditions in the *Check W3C metrics* category. The only metric that is not present in that list of error conditions is the Load event. Find out in [Load event error condition]([LINK_URL_7]) below how to set an error condition for this one.

## Load event error condition [ANCHOR_2]

You might miss the W3C metric load event in the *Check W3C metrics* category of the error conditions. If you want to set an error condition on this metric, you can do so for [Full Page Check]([LINK_URL_8]) monitors. Do the following:

1. Open the monitor settings.
2. On the [SHORTCODE_7] Main [SHORTCODE_8] tab, select a **Browser type**.
3. On the [SHORTCODE_9] Advanced [SHORTCODE_10] tab in the *Measurement* section set the **Base load time on** to *W3C load event*.
4. On the [SHORTCODE_11] Error conditions [SHORTCODE_12] tab set thresholds for the **Check page load time**.

The knowledge base article [Error conditions - Page load time]([LINK_URL_9]) has more information about setting limits for load times.
