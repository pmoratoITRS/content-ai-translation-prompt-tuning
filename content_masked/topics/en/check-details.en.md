{
  "hero": {
    "title": "Check details"
  },
  "title": "Check details",
  "summary": "The results of a monitor check are presented in the check details. The available information depends on the monitor type.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitoring-results/check-details",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The information that is collected around a monitor check is displayed in so-called "check details". These consist of the basic information if the check went fine (OK) or there was an error detected (based on your [Error conditions]([LINK_URL_1])). More detailed information on the check itself and the outcome are present as well and can help you in troubleshooting the cause of an error.

## What is included in the check details?

The information in the check details heavily depends on the monitor type. It can be as simple as a status code for an HTTP(S) monitor. More complex monitors may contain screenshots for a Full Page Check or results for each step in a transaction or Multi-step API monitor, see the two examples below.

Check details ("OK") for an HTTPS monitor:

![screenshot check details https monitor]([LINK_URL_2])

Check details for a transaction monitor that returned an error:

![screenshot check details transaction monitor]([LINK_URL_3])

## Where to find the check details?

The check details are available in several places.

If you run a monitor check by using the [SHORTCODE_1] Test now [SHORTCODE_2] button, you will get a popup with the check details.

Several dashboards will have a list of checks. Clicking on an individual error or check will bring up the check details. You can find the errors or checks here:

- Dashboard in [SHORTCODE_3] Dashboards > Synthetics > Errors overview [SHORTCODE_4] 
- Dashboard in [SHORTCODE_5] Monitoring > Status details [SHORTCODE_6] 
- Dashboard in [SHORTCODE_7] Monitoring > Monitor log [SHORTCODE_8] 
- Tile *Last check details*, a [custom report tile]([LINK_URL_4]) you can add to your [custom dashboards]([LINK_URL_5])
