{
  "hero": {
    "title": "Maintenance periods"
  },
  "title": "Maintenance periods",
  "summary": "By setting up maintenance periods you can disable your alerts or your monitors temporarily to avoid receiving errors.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-management/maintenance-periods",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

You probably don't want to be alerted when your servers, websites, or web services are down for planned maintenance. Let's say you have a consistent time in which your team performs routine maintenance on your company website, web servers, or web service. During that time, availability and performance can be affected, and your monitors may trigger alerts.

## Maintenance periods

By setting up a maintenance period for your monitors, you can configure the specific dates and times in advance, and decide whether to disable your alerts or the monitors temporarily to avoid receiving errors:

![Monitor Maintenance periods]([LINK_URL_1])


When scheduling a maintenance period, you can choose the recurrence you'll need. Periods can be configured one-time only, or on a daily, weekly, and monthly interval. Or, if your servers are scheduled to be periodically off-line on the last day of the month, you can manage the number of alerts you'll receive on this date. Check out [recurrency on the last day of the month]([LINK_URL_2]) for more details.

Note that when setting up the maintenance period the time and date of your main Uptrends account are used. Any date and time of the local computer (where you are editing the maintenance period) are ignored. This simplifies things when you are working with operators in different time zones as the maintenance periods will be based on the Uptrends account time/date only.

### Create maintenance period

You create maintenance periods on a per-monitor basis. To schedule your planned maintenance:

1.  Go to  [SHORTCODE_5]Monitoring > Monitor setup[SHORTCODE_6]
2.  Click to select and open the monitor settings for the monitor scheduled to have maintenance.
3.  Click on the tab [SHORTCODE_7]Maintenance periods[SHORTCODE_8]
4.  Click the [SHORTCODE_9]Add new maintenance period[SHORTCODE_10] button.

![Setting up a maintenance period]([LINK_URL_3])

5.  Optionally add a description for your maintenance period.
6.  Set the **Recurrence** type (*once, daily, weekly, monthly*).
7.  Set the **From** and **Until** dates and times. These options change based on your **Recurrence** choice in the previous step.
8.  Choose between disabling just the alerts or disabling the monitor completely from the **Maintenance Type** list.
9.  Click the [SHORTCODE_11]Set[SHORTCODE_12] button.
10.  Click the [SHORTCODE_13]Save[SHORTCODE_14] button in the bottom left to save the changes you just made to the monitor settings.

### Disable alerts or disable the monitor entirely

The **Add maintenance period** setup window lets you choose a **Maintenance type**; **Disable notifications only** or **Disable monitoring entirely**. 

- If you select disabling all notifications, monitoring will continue and occurring errors will still be displayed in the event log, but no alerts will be sent. 
- If you choose to disable the monitoring entirely, no monitoring takes place and thus no errors will be logged, and no alerts will be generated.  

### Recurrence on the last day of the month [ANCHOR_1]

To set up a maintenance schedule that recurs on the last day of every month: 
![Setting up a maintenance period for the last day of the month]([LINK_URL_4])
1. Create a new maintenance period as described above. 
2. Select Monthly in the **Recurrence** drop-down menu.  
3. Select 31 in the **On day** drop-down menu and click [SHORTCODE_15]Set[SHORTCODE_16]  
4. Click the [SHORTCODE_17]Save[SHORTCODE_18] button to save the changes you just made to the monitor settings.

[SHORTCODE_1] **Note**: Even if a month contains fewer than 31 days, this schedule will take effect on the last day of every month.   [SHORTCODE_2]

#### Efficiently configure maintenance routines by using monitor templates

Suppose you want to schedule maintenance for multiple monitors at once, you can use a [Monitor Template]([LINK_URL_5]). 

## Maintenance periods overview

If you want to review the maintenance periods you or a coworker created earlier, go to *Account Setup > Maintenance periods*, or click **Select all similar periods** in the monitor's [SHORTCODE_19] Maintenance periods [SHORTCODE_20] tab. 

The **Maintenance periods** overview lists all maintenance periods in your account, allowing you to review, delete unwanted periods, and perform cleanups. By default, it shows a list of all scheduled maintenance periods for all your monitors. You can use the monitor filter [SHORTCODE_21] All monitors [SHORTCODE_22]  to make your selection more specific.

![Maintenance periods overview]([LINK_URL_6])

Maintenance periods can be easily filtered by type using the dropdown menu, with options such as **All periods**, **One time periods**, or **Recurring periods**. You can also filter them by monitor name or description using the search bar for easier access. Additionally, you can find more [period filtering options]([LINK_URL_7]) by clicking the [SHORTCODE_23] [SHORTCODE_24] icon.

[SHORTCODE_3] **Note**: Administrators and operators with [Edit settings monitor permissions]([LINK_URL_8]) for at least one monitor can access the **Maintenance periods** overview page. These operators can view, [Clean up]([LINK_URL_9]), or [Delete all]([LINK_URL_10]) maintenance periods for the monitors they have **Edit settings** permissions for. [SHORTCODE_4]

### Clean up past maintenance periods

1. Select *one time periods* or *recurring periods* by clicking the settings button [SHORTCODE_25] ... [SHORTCODE_26] in the upper right-hand corner and click [SHORTCODE_27] Set [SHORTCODE_28].
![Choose periods to display]([LINK_URL_11])
2. Click the [SHORTCODE_29]Clean up[SHORTCODE_30] button.
3. The **Clean up** dialog window will display the number of periods that are in the past. 
4. Click [SHORTCODE_31]Ok[SHORTCODE_32] to delete all selected past events.

### Delete all maintenance periods

Delete all maintenance periods that are currently listed:

1. Select *one time periods* or *recurring periods* by clicking the settings button [SHORTCODE_33] ... [SHORTCODE_34] in the upper right-hand corner and click [SHORTCODE_35] Set [SHORTCODE_36].
2. Click the [SHORTCODE_37]Delete all[SHORTCODE_38] button.
3. The **Delete all** dialog window will display the number of periods that are selected and will be deleted (all periods are selected and will be deleted).
4. Click [SHORTCODE_39]Ok[SHORTCODE_40] to delete all maintenance periods.
