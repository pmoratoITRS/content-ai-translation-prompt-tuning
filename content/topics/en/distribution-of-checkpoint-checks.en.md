{
  "hero": {
    "title": "Distribution of checkpoint checks"
  },
  "title": "Distribution of checkpoint checks",
  "summary": "How does the Uptrends checkpoint system work?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/distribution-of-checkpoint-checks",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/distribution-of-checkpoint-checks"
}

Uptrends features one of the largest server and [website monitoring checkpoint networks]({{< ref path="checkpoints" lang="en" >}}) in the industry. It has never been easier to monitor your websites, servers, and web services from a variety of locations, around the globe.

**But how does Uptrends' checkpoint system work?**

## Checkpoints algorithm

When you add a monitor for tracking, you have the ability to choose a series of checkpoints from our global monitoring network to check your service status from.

The checks that are performed select from these checkpoints at random, never selecting a checkpoint twice in a row.

In the event of an unconfirmed error, the Uptrends service performs a downtime double-check via another checkpoint to ensure that the error is true.

- If that checkpoint also reports an error, the error is confirmed and listed as such in the *Errors overview*({{< AppElement type="menuitem" >}} Dashboards > Synthetics > Errors overview {{< /AppElement >}}).
- If that checkpoint does not report an error, it is assumed that the downtime was temporary.

## Round-robin support (monitoring checks performed by checkpoints in a fixed order)

We do not support a 'round robin' option.
