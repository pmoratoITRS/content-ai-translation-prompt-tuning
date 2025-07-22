{
  "hero": {
    "title": "Check interval explained"
  },
  "title": "Check interval explained",
  "summary": "The check interval is the time between the end of the last check and the beginning of the next.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/check-interval-explained",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/check-interval-explained"
}

The third option in your monitor settings asks you for the interval of your monitoring checks (see figure below). You might set up your checks for as often as once a minute up to once an hour. So, what does “Check interval” mean exactly? **The interval is the time between the end of one check and the start of the next.** Let’s explore this a little bit more.

![](/img/content/b413ee8f-d2b1-4f03-92ec-dc3982d38b61.png)

You might have thought that if you picked one minute for your check interval that Uptrends would check your website 1440 times a day with checks starting at the top of every minute, but no. Uptrends needs to know that the previous check completed successfully before scheduling the next check. Therefore, the number of checks you get each day is dependent on:

-   Monitor type,
-   Page load or response times,
-   Interval you selected,
-   Number of errors Uptrends encounters with your site or service, and
-   System overhead for sending the check definition to the checkpoint, conducting the test, transmitting and processing of the test results.

Let’s take a look at a few examples:

**Uptime Check, interval one minute**

If an uptime check takes ten seconds from start to finish, the next check starts 60 seconds after the successful completion of the first check. So, in this case, you can expect roughly 70-second intervals from the beginning of one check to the beginning of the next. Instead of 1,440 checks per day, you would have approximately 1,234 checks per day.

**Transaction monitor, interval five minutes**

Complex transactions can take a while to complete depending on the number of steps and the responsiveness of your site or service. If a check takes two minutes to complete from start to end, the next check occurs five minutes after the first check finishes or seven minutes after the start of the first check. Instead of 288 checks per day, this scenario results in approximately 206 checks per day.

## How do errors affect my monitor’s interval?

When Uptrends gets an error from your website or service, Uptrends ignores the check interval and schedules the next check to happen right away from a different checkpoint. If Uptrends gets a second error, Uptrends sends an alert. Uptrends then schedules the next check based on your interval settings. When the test interim is up, Uptrends checks again doing a double check again if it gets an error. Notice in the monitor log below that although the monitor has a five-minute check interval the confirmed errors (red) happen right away after the unconfirmed error (yellow). The time interval between the confirmed error and the next check is five minutes.

![](/img/content/c100918a-8fee-42fa-9e5e-98282ddd79cf.png)
