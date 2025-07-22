{
  "hero": {
    "title": "How does Concurrent monitoring work?"
  },
  "title": "How does Concurrent monitoring work?",
  "summary": "An overview about Concurrent monitoring",
  "url": "/support/kb/synthetic-monitoring/concurrent-monitoring/how-does-concurrent-monitoring-work",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/how-does-concurrent-monitoring-work"
}

In Uptrends, there are two ways of monitoring the uptime, performance and correct behavior of your websites, web services and servers: standard monitoring and concurrent monitoring.

## Standard monitoring

A monitor check is done from one checkpoint. If an error occurs, this is regarded an unconfirmed error. Directly afterwards, the same monitor check is done from a different checkpoint. If the same error is received again, the result is a confirmed error. Only confirmed errors can lead to alerts and messages (SMS, email, Slack, other third-party systems).

## Concurrent monitoring

A number of monitor checks are done at the same time (concurrently) instead of one after another. You define how many checks are done concurrently and from which checkpoints.

There are also two limits which are a percentage of the checkpoints returning an error: one limit for when an error is regarded an unconfirmed error and another limit for when an error is regarded a confirmed error. It's up to you to decide which percentage is enough to signal an error. If the first level (for example 30%) is reached, the error is classified as an unconfirmed error. If the second level is reached (for example 60%), you'll see a confirmed error instead.

When a significant (as defined by the user) percentage of checks has returned an error, the result immediately is a confirmed error. An alert can be generated and a notification can be sent quickly.

## Scope

Concurrent monitoring works within the following scope:

-   It is available for all monitor types.
-   The monitor checks must be at usual monitoring frequencies, which are 1 minute for basic monitors and 5 to 15 minutes for browser monitors.
-   For concurrent monitoring, special rules apply for selecting checkpoints: either choose from all checkpoints (at least 5), or choose from checkpoints marked as *high availability* (at least 3). *High availability* checkpoints are generally those locations with more than one server available.
-   In all cases, the maximum number of selected checkpoints is 50.

## Monitoring output

Based on concurrent checks, Uptrends computes one overall measurement (with basic metrics). The data can be used like with other monitors, e.g. in dashboards, alerts or SLA calculations.

The individual measurements will be available in these places:

- The *Monitor log* 
- When opening the overall measurement from the *Monitor log*, you get a details popup which points to the partial measurements.
- Per individual measurement, we will record the usual debug information (screenshots, waterfall, traceroute etc.).

## Advantages and disadvantages

The advantages are that Concurrent monitoring detects an error faster and has higher reliability. Note that the latter depends on the number of checkpoints used.

A disadvantage could be that we do not aggregate transaction steps or calculate an average of the waterfall for reporting purposes (for transactions, full page checks, etc).

Concurrent monitoring comes at a higher price. However, you'll get faster detection and higher reliability in return. Please see the examples below to get an idea about the pricing.

## Subscription plans

The feature will be included in the following subscription plans: Business and Enterprise.  
In order to use concurrent monitoring, you have to individually choose the checkpoints that will be included in the checks. This is possible in the Business and Enterprise plan. Other plans do not offer this option and therefore are not suitable for concurrent monitoring.

The calculation of credits used for concurrent monitors is explained in the KB article [Pricing for concurrent monitoring](/support/kb/synthetic-monitoring/concurrent-monitoring/pricing-calculation-examples).