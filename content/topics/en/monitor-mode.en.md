{
  "hero": {
    "title": "Monitor Mode"
  },
  "title": "Monitor mode",
  "summary": "Uptrends offers three new monitoring modes: development, staging, and production.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/monitor-mode",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-mode"
}

Most of the time, when you create a new monitor, you want that monitor to become active in your account right away. Once active, the monitor starts producing measurements every minute (depending on the monitor interval). You can inspect those measurements in the monitor log, and Uptrends generates alerts when errors start occurring. For many cases, making your monitor active immediately works very well. However, this immediacy is not always optimal. 

## Running in production mode or not

When you're building a new transaction, for example, you'll likely work on the transaction for some time before you want to run it in production. In the meantime, you may want to let the transaction run for a while to see how stable it is without running the risk of generating false positives (error alerts). False positives have an unwanted effect on your SLAs and other account-wide uptime numbers.

Similarly, if you have an existing transaction that needs replacing by an updated script as soon as you launch your updated website, you'll want to prepare that new transaction and have it ready to go. However, as long as the new transaction script is just sitting there inactive, the monitor uses valuable transaction credits that count towards your total number of available. You can purchase additional credits, but there is a more efficient way to organize your monitors.

## Managing monitor life cycles using monitor mode

We have three different monitor modes: **development**, **staging,** and **production**. You can switch between these modes for all monitor types (not just transactions) if you're using the Professional, Business, or Enterprise plan. For other pricing plans, the monitor mode is always production.

So how will the different monitor modes come in handy?

### Development mode

Monitors in development mode are always inactive. You can't schedule monitor in development mode for execution, so the monitor won't generate any results in the monitor log. This also means that they're free! You can have as many as you want, without any additional cost. That does mean that any data history attached to that monitor disappears  as soon as you switch a monitor back to Development mode.

Development mode monitors are useful for creating and testing draft versions. Suppose you're creating a new transaction or Multi-step API monitor, and that you're running manual tests on it within the editor. Based on the test results, you can tweak it further until you're satisfied with those initial test results. Until you're ready to move a monitor to staging or production, it doesn't cost you anything, and the monitor doesn't have any negative impact on your uptime numbers.

Consequently, development mode also lets you keep multiple (inactive) copies lying around without having to purchase additional monitors, transaction steps, or API steps. It's fine to keep monitors in development mode for a long time. However, when you are ready to promote an inactive development mode monitor to staging or production, you will need space in your account to activate it or swap it around with another monitor.

### Staging mode

Staging mode is typically the next step in a new monitor's life cycle. As opposed to development mode, staging mode does allow you to schedule a monitor for normal execution. Once activated, the monitor produces new measurements as any other monitor would, and the results are visible in the monitor log as usual. The nice thing about using staging mode is that even though you can observe how stable the monitoring results are, it does not affect the uptime percentage of your account, have any impact on your SLAs, and Uptrends doesn't send out any alerts. It's like running your monitors in a sandbox environment; the measurements are real, but the uptime, SLAs, historic statistics, and alerting pipeline stay clean ([learn more](/support/kb/synthetic-monitoring/monitor-settings/the-effects-of-staging-mode-on-reports-and-sla-data)).

Once you move a monitor to staging mode, the monitor counts towards your total number of monitors/credits used in your account. Typically, you want to try and promote a staged monitor to production as soon as you're confident that the monitor is stable. Otherwise, you're not taking advantage of the full range of features while the cost is the same as a production monitor.

### Production mode {id="monitormodeproduction"}

Production is the default mode. While in production mode, a monitor is available for regular execution, the monitor's availability counts towards the overall account uptime, the monitor results are taken into account for SLA calculations, and alerting is available.
