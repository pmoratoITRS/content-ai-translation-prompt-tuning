{
  "hero": {
    "title": "Calculation of uptime and downtime"
  },
  "title": "Calculation of uptime and downtime",
  "summary": "How do you calculate the uptime of your monitor based on check results and how do paused monitors or maintenance affect this calculation?",
  "url": "/support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime",
  "translationKey": "https://www.uptrends.com/support/kb/reporting/calculation-of-uptime-and-downtime"
}

Uptime and downtime calculations are the basis for a number of metrics in data tiles on your dashboards and for your [service level agreements (SLAs)]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="en" >}}). Let's take a look at how the calculation is done and which factors have an impact.
## Introducing the Uptrends double-check

When an error is detected on your website or server, Uptrends always performs a double check on another checkpoint to verify the error. This is why during downtime, you always see a pattern of unconfirmed errors and confirmed errors in your [website monitoring]({{< ref path="products/synthetics/website-monitoring" lang="en" >}}) dashboards.

This is how standard monitoring works. If you are using concurrent monitoring, there are no double checks. Take a look at the article [Errors and alerting for concurrent monitors]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors" lang="en" >}}) to understand the difference.

{{< callout >}}
**Tip:** For detailed analysis of the exact measurements that are performed, and the errors detected, please have a look at your **Monitor log** dashboard which you find in the {{< AppElement type="menuitem" >}} Monitoring > Monitor log {{< /AppElement >}} menu.
{{< /callout >}}

## How is the uptime percentage calculated?

The way to calculate uptime is easy to understand: take the number of seconds that your monitor was down (in a certain time frame), and divide this by the total number of seconds your monitor was being monitored during that time frame. As a result, you get the downtime percentage, which is then subtracted from 100% to get the uptime percentage.

{{< callout >}}
**Tip:** SLAs will give you an uptime as percentage, but how much time is that actually? Use the [Free SLA and uptime calculator]({{< ref path="tools/free-sla-uptime-calculator" lang="en" >}}) to convert downtime in seconds to a percentage and vice versa. 
{{< /callout >}}

### Example

Let's say you monitored a website during 24 hours (which translates to 86,400 seconds), and in that timeframe the website went down for 10 minutes (600 seconds). To define the uptime and downtime percentages, the following calculation is performed:

Total time your website was down: 600 seconds  
Total time your website was monitored: 86,400 seconds  
Downtime percentage = 600 seconds / 86,400 seconds = 0.0069 = 0.69%  
Uptime percentage = 100% - 0.69% = 99.31%  

{{< callout >}}
**Tip:** Play around with the data in your account to retrieve the actual number of seconds. The [custom report tiles]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="en" >}}) of type _data list_ and _data chart_ allow you to display the number of seconds of when your monitors were up or down. Go to a tile and open the three-dot menu {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} to access the tile settings, including the different metrics you can select.
{{< /callout >}}

## Impact of monitor check results

How does Uptrends mark the period between different monitor check results (OK, unconfirmed error, and confirmed error)? Is the time between an unconfirmed error and a confirmed error considered as up, or down? 

The illustration below shows the possible sequences of check results and how the periods are considered. Of course, when continuously monitoring a service or server, there will be many check results in a row. However, all results can be broken down into the following situations:

![illustration check results sequences](/img/content/uptime-calculation-min.svg)

On a detailed level, the check results can change in these ways:   

**Unconfirmed error -> confirmed error**  
The time between the two measurements is being considered as **down**.

**Confirmed error -> unconfirmed error**  
The time between the two measurements is being considered as **down,** because the monitor is still in an error condition. A monitor will be in error until an OK indication is detected.

**Confirmed error -> OK**  
The time between the two measurements is being considered as **down**. A monitor is considered to be up only from the moment an OK indication is detected.

**OK -> unconfirmed error**   
The time between the two measurements is being considered as **up**, because it is not sure there is an actual error yet. 

**Unconfirmed error -> OK**  
The time between the two measurements is being considered as **up**. 

## Which errors contribute towards downtime?

Please keep in mind that **all errors are taken into account** when calculating downtime. 

For example, when you define performance limits in the monitor's error conditions and that limit is reached, an error is generated for that condition. Although your website is not actually down (but performing below your limits), it will show an uptime of less than 100% because the performance condition generated an error.

## How do paused monitors affect uptime?

When you pause a monitor, this time is being registered as 'unknown'. When the uptime percentage is being calculated, please keep in mind that the total number of unknown seconds is included as well, and marked as uptime. The formula for the uptime percentage is **(uptime + unknown) / (uptime + downtime + unknown)**, where uptime, downtime, and unknown are given in seconds.

This has been a deliberate choice, because a lot of customers requested this. If you want to exclude the unknown time from the uptime calculation, you can retrieve the total number of uptime and downtime seconds to do your own calculation. For the uptime percentage, use the formula **uptime / (uptime + downtime)**, where uptime and downtime are given in seconds.

## How does maintenance affect uptime?

Errors that occur during a [maintenance period]({{< ref path="support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="en" >}}) are excluded from the uptime calculations, as long as the *Maintenance type* of the maintenance period is set to **Disable monitoring entirely** versus disabling notifications only.  
