{
  "hero": {
    "title": "Clearing errors"
  },
  "title": "Clearing Errors",
  "summary": "Find out how to clear the error history of incorrect or unwanted errors",
  "url": "[URL_BASE_TOPICS]alerting/errors/clearing-errors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

It is possible to clear individual errors or a group of errors (both unconfirmed and confirmed) which are deemed incorrect or unwanted. Single (or a small number of) errors can be cleared by you. If you have a whole lot of errors to clear, Uptrends will assist you with that, see [Clearing errors in bulk]([LINK_URL_1]). 

Note that clearing errors does not automatically recalculate the metrics that are based on errors, like service level agreement ([SLA]([LINK_URL_2])) statistics or [public status page]([LINK_URL_3]) numbers. See [Effect on SLAs and public status page data]([LINK_URL_4]) on how to deal with recalculating statistics depending on whether you cleared the errors yourself or requested that from Support.

[SHORTCODE_1]
**Note**: Unfortunately it is impossible to recalculate SLAs for data older than 90 days, as that data is not retained past this time period.
[SHORTCODE_2]

## How to clear individual errors [ANCHOR_1]

To clear an error in your account: 
1. Go to the menu [SHORTCODE_3]Monitoring > Monitor log[SHORTCODE_4].
2. Click on the error that you wish to clear. The *Check details* related to this error will appear.
3. At the bottom of the pop-up click the [SHORTCODE_5] Clear error [SHORTCODE_6] button.
4. Confirm the action with the [SHORTCODE_7] Clear [SHORTCODE_8] button. 

The error will be changed to an OK result, which is immediately visible in the *Monitor log* dashboard. 

The corresponding uptime percentage data will be changed as well. Due to caching, the changes may take some time to become visible.

## Clearing errors in bulk [ANCHOR_2]

Sometimes you may want to clear errors for a specific time range (for example, several days of downtime). Rather than clearing each error out individually, we advise that you do the following:

1. If you happen to have some monitoring *Check details* open, click the [SHORTCODE_9] Clear multiple errors [SHORTCODE_10] button at the bottom of the pop-up. The *Clear errors request* form will appear. 
2. Alternatively, navigate to [SHORTCODE_11] Support [SHORTCODE_12] and click the [SHORTCODE_13]  Request to clear errors [SHORTCODE_14] option. The *Clear errors request* form will appear. 
3. Fill in the mandatory information, which are the monitor(s) and date range. Add any optional information relevant to your request, like a status code. 
4. Click the [SHORTCODE_15] Send [SHORTCODE_16] button.

When you send your request, a ticket will be automatically created and your request will be processed. This may take a while, but you will be updated by the ticket system once the clearing of errors and the SLA data recalculation is completed. 

## Effect on SLAs (service level agreements) and public status page data [ANCHOR_3]

Clearing errors does not automatically change existing [SLA]([LINK_URL_5]) data, including [public status page]([LINK_URL_6]) data, which is also calculated SLA data. 

However, it is possible to recalculate it. When you requested [clearing multiple errors]([LINK_URL_7]) by the Support team, the recalculation of data is included in the process. You don't have to request this separately. 

This is different when you have cleared errors yourself. In that case, please contact Support through a [support ticket]([LINK_URL_8]), and express what you would like to do. 
