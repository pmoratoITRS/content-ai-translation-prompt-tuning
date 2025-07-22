{
  "hero": {
    "title": "New operator doesn't receive alerts"
  },
  "title": "Operator Doesn't Get Alerts",
  "summary": "If any new operator within your Uptrends account is failing to receive alerts, it can be a problem. Learn what to do.",
  "url": "/support/kb/alerting/new-operator-does-not-receive-alerts",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/new-operator-does-not-receive-alerts"
}

Knowing what is going on with websites, servers, and web services is crucial for any operations team. If any new operator within your Uptrends account is **failing to receive alerts**, it can be a big problem. But don’t worry, we’re here to help!

## Check Your Alert Definitions

The first thing that you should do is check to see which **Alert Definition** is in place for the monitored service in question.

**Default Alert Definitions**

Every Uptrends account comes with a *Default alert definition*, which sends out alerts to the *Everyone* operator group when any monitor within the *All Monitors* group experiences an error. This means that for every error experienced, all operators will be alerted, because by default all operators are automatically a member of the *Everyone* operator group.

**Edited Default / Custom Alert Definitions**

That being said, some users choose to change the settings of the default alert definition, or create their own *custom alert definition* from scratch. It is in these cases that you’ll find that new operators are not being automatically added to alert definitions, which means they will miss out on alerts.

To learn how to add an operator (or operator group) to an alert definition, please read our knowledge base article [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}).
