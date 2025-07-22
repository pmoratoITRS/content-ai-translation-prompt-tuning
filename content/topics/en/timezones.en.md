{
  "hero": {
    "title": "Time zone"
  },
  "title": "Time zone",
  "summary": "The Timezone setting is a setting that influences how monitored times are reported, based on your time zone choice.",
  "url": "/support/kb/account/settings/timezones",
  "translationKey": "https://www.uptrends.com/support/kb/account/timezones"
}

The **Timezone** is a setting that influences how monitored times are reported, based on your time zone.

This setting is configured during the Uptrends account setup and can be found back by going to {{< AppElement type="menuitem" >}} Account setup > Account settings {{< /AppElement >}} and opening the {{< AppElement type="tab" >}} Settings {{< /AppElement >}} tab.

You have the option change the time zone yourself, unless there is Real User Monitoring (RUM) data already collected in your Uptrends account. In that case the setting will appear as disabled for changes and you have to contact [Support]({{< ref path="contact" lang="en" >}}) to discuss the options.

{{< callout >}}
**Note:** Changes in the time zone setting will introduce a gap or overlap in your monitoring data because the application does not recalculate existing data after a time zone change. 
{{< /callout >}}

## Daylight savings time (DST)

In the Uptrends application, some time zones are marked with an asterisk (\*), or hash sign (\#) to indicate that the time zone is subject to daylight savings.

- \* - Time zone is on the Northern hemisphere and it observes daylight savings
- \# : Time zone is on the Southern hemisphere and it observes daylight savings
- Some time zones do not observe daylight savings and have no \* or \#.

If you want to see times in UTC (Universal Time Coordinated), use the **UTC** time zone (without \* marking) for this. This time zone setting does not observe DST. Please note this is not the same as **UTC\* England, Ireland** which does observe DST.

## Time zones for operators

The default Uptrends account time zone setting can be adjusted to use an [additional time zone]({{< ref path="support/kb/account/users/operators/main-settings#timezone" lang="en" >}}) for individual operators. Note that this feature is available for [Enterprise accounts]({{< ref path="/pricing#plans" lang="en" >}}) only.
