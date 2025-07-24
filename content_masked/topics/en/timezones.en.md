{
  "hero": {
    "title": "Time zone"
  },
  "title": "Time zone",
  "summary": "The Timezone setting is a setting that influences how monitored times are reported, based on your time zone choice.",
  "url": "[URL_BASE_TOPICS]account/settings/timezones",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The **Timezone** is a setting that influences how monitored times are reported, based on your time zone.

This setting is configured during the Uptrends account setup and can be found back by going to [SHORTCODE_3] Account setup > Account settings [SHORTCODE_4] and opening the [SHORTCODE_5] Settings [SHORTCODE_6] tab.

You have the option change the time zone yourself, unless there is Real User Monitoring (RUM) data already collected in your Uptrends account. In that case the setting will appear as disabled for changes and you have to contact [Support]([LINK_URL_1]) to discuss the options.

[SHORTCODE_1]
**Note:** Changes in the time zone setting will introduce a gap or overlap in your monitoring data because the application does not recalculate existing data after a time zone change. 
[SHORTCODE_2]

## Daylight savings time (DST)

In the Uptrends application, some time zones are marked with an asterisk (\*), or hash sign (\#) to indicate that the time zone is subject to daylight savings.

- \* - Time zone is on the Northern hemisphere and it observes daylight savings
- \# : Time zone is on the Southern hemisphere and it observes daylight savings
- Some time zones do not observe daylight savings and have no \* or \#.

If you want to see times in UTC (Universal Time Coordinated), use the **UTC** time zone (without \* marking) for this. This time zone setting does not observe DST. Please note this is not the same as **UTC\* England, Ireland** which does observe DST.

## Time zones for operators

The default Uptrends account time zone setting can be adjusted to use an [additional time zone]([LINK_URL_2]) for individual operators. Note that this feature is available for [Enterprise accounts]([LINK_URL_3]) only.
