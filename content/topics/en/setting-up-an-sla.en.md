{
  "hero": {
    "title": "Setting up an SLA"
  },
  "title": "Setting up an SLA",
  "summary": "You can monitor your SLAs (service level agreement) for compliance using Uptrends.",
  "url": "/support/kb/dashboards-and-reporting/sla/setting-up-an-sla",
  "translationKey": "https://www.uptrends.com/support/kb/sla/setting-up-an-sla"
}



## SLA definitions

By creating an SLA definition, you can configure the same minimal requirements set by your provider and monitor them using the **SLA overview** dashboard that you find in the menu at {{< AppElement type="menuitem" >}}Dashboards > Synthetics > SLA overview {{< /AppElement >}}. If the site or service fails to meet the minimum requirements, it appears red in the SLA overview. For more information on the SLA overview dashboard see the article [Working with SLA data and reports]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-sla-data-and-reports" lang="en" >}}).

{{< callout >}}
**Note:** If you see dashes and zeros instead of data in your SLA overview report, your tile/dashboard settings have caused a conflict in the data resulting in invalid data. Find out more about the possible causes in the knowledge base article [Missing SLA overview data]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="en" >}}).
{{< /callout >}}

### SLA thresholds

The following elements are referred to as the **SLA thresholds**. Your SLA definition may include only uptime or any of the other SLA thresholds.

- **Error uptime percentage** – SLA uptime results lower than this threshold do not satisfy the SLA target: they will cause a red error in the SLA reports. Values higher than this threshold (but lower than the desired uptime percentage) will cause warnings in the SLA reporting.
- **Desired uptime percentage** – SLA uptime results with this value (or higher) are good; they satisfy the SLA target. Values between this threshold and the error uptime percentage will cause a yellow warning in the SLA reports.
- **Page load time** – The maximum page load time as agreed upon in the SLA.
- **Operator response time** – The amount of time between an Uptrends alert and the time that an operator logs into Uptrends and confirms the alert to indicate they are working on the situation. The **Current alert status** dashboard ({{< AppElement type="menuitem" >}} Alerting > Current alert status {{< /AppElement >}}) has the functionality for confirming an alert.

 If you want to know more about how the uptime percentage is calculated, please read the knowledge base article [Calculation of uptime and downtime]({{< ref path="support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="en" >}}).

 ### SLA schedule {id="sla-schedule"}

In case your SLA isn't active 24/7, for example if it only covers regular office hours, or if you have upcoming scheduled maintenance, you can add an SLA schedule. SLA schedules allow you to specify the times your SLA is active. Any downtime, increased load times, or errors outside of these times will not be taken account in the SLA reporting. You configure your SLA schedule on the {{< AppElement type="tab" >}}Schedule{{< /AppElement >}} tab, where you find the time schedule and the option to exclude days for planned maintenance.

Note that when setting up the SLA schedule the time and date of your main Uptrends account are used. Any date and time of the local computer (where you are editing the SLA schedule) are ignored. This simplifies things when you are working with operators in different time zones as the SLA schedules will be based on the Uptrends account time/date only.

- **Time schedule** – For each hour of every day of the week, you can specify whether this SLA should be active or not. 

- **Exclusion days** – If you have non-routine planned downtime, you can exclude time based on specific calendar days and times.

## Setting up an SLA definition

To define an SLA:

1. Go to  {{< AppElement type="menuitem" >}} Account setup > SLA definitions {{< /AppElement >}}.
2. Click the {{< AppElement type="button" >}}Add SLA definition {{< /AppElement >}} button at the top right.
3. Give your definition a descriptive name.
4. Set the error uptime percentage in the yellow outlined box in the **Uptime** field. Uptime results below this value will be marked red on the SLA overview reports.
5. Set the green outlined box to the percentage where the uptime becomes a point of concern for meeting SLA compliance in the **Uptime** field. Uptime results between this and the error uptime percentage will be marked yellow on the SLA overview reports.
6. (Optional) If required by your SLA, adjust the **Page load time** and/or **Operator response time**.
7. (Optional) If your SLA isn't always active, set up a schedule. In the timetable on the {{< AppElement type="tab" >}}Schedule{{< /AppElement >}} tab the blue squares indicate that the SLA is active at that time while white squares indicate an inactive timeslot. Click on a square to switch between active and inactive. If you want to disable entire days or the same hour of each day, click on the column or row headers instead of individual squares.
8. (Optional) For planned downtime (beyond the time schedule), add exclusion days on the {{< AppElement type="tab" >}}Schedule{{< /AppElement >}} tab:

   1. Click the {{< AppElement type="button" >}}Add new exclusion period{{< /AppElement >}} button.
   2. Give the exclusion period a descriptive name.
   3. Select the start and end dates and times in the **From** and **Until** fields.
   4. Click {{< AppElement type="button" >}}Set{{< /AppElement >}}.

9. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button at the bottom left.
